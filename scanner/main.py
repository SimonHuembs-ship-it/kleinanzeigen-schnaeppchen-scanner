"""Stufe 1: der Sammler.

Holt Rohdaten, filtert deterministisch, rechnet Referenzpreise, scort die
Serioesitaet und schreibt candidates.json. Das inhaltliche Urteil faellt Stufe 2.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

from .api import Api, Gesperrt, eingestellt, jetzt
from . import filter as vorfilter
from . import reference, score as scoring, typos

WURZEL = Path(__file__).resolve().parent.parent
SEEN = WURZEL / "seen_ads.csv"
KANDIDATEN = WURZEL / "candidates.json"
BERLIN = timezone(timedelta(hours=2))


def gesehene_laden() -> set:
    if not SEEN.exists():
        return set()
    with SEEN.open(encoding="utf-8") as datei:
        return {zeile["ad_id"] for zeile in csv.DictReader(datei)}


def gesehene_ergaenzen(neu: set, stempel: str) -> None:
    existiert = SEEN.exists()
    with SEEN.open("a", newline="", encoding="utf-8") as datei:
        schreiber = csv.writer(datei)
        if not existiert:
            schreiber.writerow(["ad_id", "erste_sichtung"])
        for ad_id in sorted(neu):
            schreiber.writerow([ad_id, stempel])


def anzeigen_sammeln(api: Api, ziel: dict, von: datetime, bis: datetime, statistik: dict,
                     pool: list | None = None) -> list:
    """Kategorie-Sweep oder Keyword-Suchen, je nach Ziel.

    Liegt ein Pool vor, wurde ganz Kleinanzeigen bereits einmal abgefragt und
    alle Sweep-Ziele bedienen sich daraus. Das ist der Unterschied zwischen
    einem Abruf und vierzehn.
    """
    gefunden = {}

    if ziel.get("verfahren") == "sweep" and pool is not None:
        unten, oben = ziel.get("preis_min"), ziel.get("preis_max")
        for anzeige in pool:
            preis = anzeige.price or 0
            if unten and preis < unten:
                continue
            if oben and preis > oben:
                continue
            gefunden[anzeige.id] = anzeige
    elif ziel.get("verfahren") == "sweep":
        for anzeige in api.fenster(category_id=ziel["kategorie"], von=von, bis=bis,
                                   min_price=ziel.get("preis_min"),
                                   max_price=ziel.get("preis_max")):
            gefunden[anzeige.id] = anzeige
    else:
        begriffe = list(ziel.get("begriffe", [])) + list(ziel.get("tippfehler", []))

        # Von Hand gepflegte Tippfehlerlisten sind immer unvollstaendig.
        # Systematisch erzeugte Varianten decken die Fehlerklassen ab, die
        # deutsche Nutzer tatsaechlich produzieren.
        anzahl = int(ziel.get("tippfehler_auto", 4))
        if anzahl:
            for begriff in list(ziel.get("begriffe", [])):
                begriffe.extend(typos.erzeugen(begriff, anzahl))
        begriffe = list(dict.fromkeys(b.lower() for b in begriffe))

        for begriff in begriffe:
            for anzeige in api.suche(begriff,
                                     category_id=ziel.get("kategorie"),
                                     min_price=ziel.get("preis_min"),
                                     max_price=ziel.get("preis_max"),
                                     seiten=1):
                gefunden[anzeige.id] = anzeige

    # Beim Gesamtsweep ist der Pool schon gezaehlt; sonst zaehlt jedes Ziel
    # dieselben Anzeigen erneut und die Statistik meldet ein Vielfaches.
    if not (ziel.get("verfahren") == "sweep" and pool is not None):
        statistik["gesichtet"] += len(gefunden)
    return list(gefunden.values())


def lauf(watchlist_pfad: Path, stunden: int, limit: int | None) -> dict:
    konfiguration = yaml.safe_load(watchlist_pfad.read_text(encoding="utf-8"))
    einstellungen = konfiguration.get("einstellungen", {})
    ziele = [z for z in konfiguration["ziele"] if z.get("aktiv", True)]

    # Die Kleinanzeigen-Suche ist unscharf und liefert auch lose Verwandtes.
    # Ohne positives Modellmuster sammelt ein Ziel deshalb ein, was ihm die
    # Suche vorsetzt. Das faellt sonst erst in der Mail auf.
    ohne_muster = [z["id"] for z in ziele if not z.get("muster")]
    if ohne_muster:
        raise ValueError(f"Ziele ohne Modellmuster: {', '.join(ohne_muster)}")

    api = Api(rate_limit=float(einstellungen.get("rate_limit", 0.8)))
    bis = jetzt()
    von = bis - timedelta(hours=stunden)
    gesehen = gesehene_laden()
    neue_ids: set = set()
    kandidaten = []
    statistik = {"gesichtet": 0, "nach_modellmatch": 0, "nach_vorfilter": 0,
                 "nach_preisschwelle": 0, "nach_scoring": 0, "ausschluesse": {}}
    start = time.time()

    budget = int(einstellungen.get("max_requests", 4000))

    # Ein Sweep ueber ganz Kleinanzeigen statt einer je Kategorie. Ohne
    # Preisuntergrenze waeren es zwei Millionen Anzeigen am Tag; ab 150 Euro
    # bleibt ein Viertel davon, und darunter liegen fast nur Kleinteile.
    pool = None
    if einstellungen.get("gesamtsweep"):
        pool = api.fenster(von=von, bis=bis,
                           min_price=einstellungen.get("preis_ab", 150))
        statistik["pool"] = len(pool)
        statistik["gesichtet"] += len(pool)
        print(f"  Gesamtsweep: {len(pool)} Anzeigen, {api.requests} Requests",
              file=sys.stderr, flush=True)

    for ziel in ziele:
        if api.requests >= budget:
            statistik["budget_erschoepft"] = True
            print(f"Budget erschoepft, Ziel {ziel['id']} und folgende uebersprungen",
                  file=sys.stderr)
            break
        cache: dict = {}
        anzeigen = anzeigen_sammeln(api, ziel, von, bis, statistik, pool)
        print(f"  {ziel['id']}: {len(anzeigen)} Anzeigen gesichtet, "
              f"{api.requests} Requests bisher", file=sys.stderr, flush=True)

        # Bei einem Sweep ist "posted" der einzige Zeitfilter, denn modAfter
        # erfasst auch Bearbeitungen. Rund 2 Prozent sind gebumpte Altanzeigen.
        #
        # Nischen-Ziele laufen ohne Zeitfilter: dort stehen wenige Anzeigen
        # wochenlang unverkauft, und eine unterbewertete Leica waere nach Tag
        # eins sonst fuer immer unsichtbar. Wiederholungen faengt seen_ads.csv.
        if ziel.get("zeitfilter", True):
            anzeigen = [a for a in anzeigen if (eingestellt(a) or von) >= von]

        passend = []
        for anzeige in anzeigen:
            if anzeige.id in gesehen:
                continue
            if vorfilter.ist_gesuch(anzeige.title):
                continue
            if not vorfilter.passt_zum_ziel(anzeige.title, ziel):
                continue
            passend.append(anzeige)
        statistik["nach_modellmatch"] += len(passend)

        gefiltert = []
        for anzeige in passend:
            neue_ids.add(anzeige.id)
            if vorfilter.ist_lockpreis(anzeige.price):
                continue
            if vorfilter.ist_faelschung(f"{anzeige.title} {anzeige.description or ''}"):
                continue
            gefiltert.append(anzeige)
        statistik["nach_vorfilter"] += len(gefiltert)

        # Erst der billige Teil: Referenzpreis fuer alle, gecacht ueber die
        # Referenzfrage. Danach wird sortiert, damit die anschliessende
        # Deckelung die guenstigsten Treffer behaelt und nicht die ersten.
        schwelle = float(ziel.get("schwelle", 0.80))
        ohne_referenz = int(ziel.get("ohne_referenz", 0))
        vorgemerkt = []

        # Die Referenzfrage kommt aus dem Titel und ist damit fast immer
        # einmalig, der Cache greift also kaum: eine Suche pro Anzeige. Deshalb
        # gedeckelt, und zwar bei den guenstigsten zuerst. Der Preis allein ist
        # ein grober, aber brauchbarer Vorsortierer, solange der Marktwert noch
        # nicht bekannt ist.
        referenz_limit = int(ziel.get("referenz_limit",
                                      einstellungen.get("referenz_limit", 80)))
        gefiltert.sort(key=lambda a: float(a.price or 0))
        if len(gefiltert) > referenz_limit:
            statistik["referenz_gekappt"] = (statistik.get("referenz_gekappt", 0)
                                             + len(gefiltert) - referenz_limit)
            gefiltert = gefiltert[:referenz_limit]

        for anzeige in gefiltert:
            if api.requests >= budget:
                statistik["budget_erschoepft"] = True
                break

            referenzwert = reference.referenzpreis(api, ziel, anzeige, cache=cache)
            if referenzwert:
                verhaeltnis = float(anzeige.price) / referenzwert["median"]
                if verhaeltnis > schwelle:
                    continue
            elif ohne_referenz > 0:
                # Ohne Vergleichsbasis faellt der Preisfilter aus. Nur begrenzt
                # zulassen, sonst laeuft jede gematchte Anzeige in den teuren
                # Detailabruf.
                ohne_referenz -= 1
                verhaeltnis = 1.0
            else:
                statistik["ohne_referenz_verworfen"] = statistik.get("ohne_referenz_verworfen", 0) + 1
                continue
            statistik["nach_preisschwelle"] += 1
            vorgemerkt.append((verhaeltnis, anzeige, referenzwert))

        # Detailabruf und Verkaeuferhistorie kosten zwei Requests pro Anzeige
        # und sind der teuerste Teil des Laufs. Was die Deckelung abschneidet,
        # steht im Laufprotokoll, damit die Kappung nicht still passiert.
        grenze = int(ziel.get("detail_limit", einstellungen.get("detail_limit", 30)))
        vorgemerkt.sort(key=lambda eintrag: eintrag[0])
        if len(vorgemerkt) > grenze:
            statistik["detail_gekappt"] = statistik.get("detail_gekappt", 0) + len(vorgemerkt) - grenze
            vorgemerkt = vorgemerkt[:grenze]

        for _, anzeige, referenzwert in vorgemerkt:
            if api.requests >= budget:
                statistik["budget_erschoepft"] = True
                break

            detail = api.detail(anzeige.id)
            if not detail:
                continue

            verkaeufer_anzeigen = None
            if detail.verkaeufer.id:
                verkaeufer_anzeigen = api.anzeigen_des_verkaeufers(detail.verkaeufer.id)

            bewertung = scoring.bewerten(anzeige, detail, referenzwert, ziel, verkaeufer_anzeigen)
            if "ausschluss" in bewertung:
                grund = bewertung["ausschluss"]
                statistik["ausschluesse"][grund] = statistik["ausschluesse"].get(grund, 0) + 1
                continue
            # Zwischen 25 und 45 Prozent des Marktwerts liegt der Bereich, in
            # dem Betrug und Totalschaden haeufiger sind als echte Funde. Dort
            # reicht die normale Mindestpunktzahl nicht.
            grenzwert = int(einstellungen.get("mindestpunkte", 60))
            if bewertung["p_ratio"] is not None and bewertung["p_ratio"] < 0.45:
                grenzwert = max(grenzwert, int(einstellungen.get("mindestpunkte_tiefpreis", 80)))
            if bewertung["punkte"] < grenzwert:
                statistik["ausschluesse"]["score_zu_niedrig"] = \
                    statistik["ausschluesse"].get("score_zu_niedrig", 0) + 1
                continue

            tippfehler = vorfilter.tippfehler_im_titel(anzeige.title, ziel)
            generisch = vorfilter.wirkt_generisch(anzeige.title)
            bonus = scoring.unkenntnis_profil(anzeige, detail, bewertung, tippfehler, generisch)

            ersparnis = None
            if referenzwert:
                ersparnis = round(referenzwert["median"] - float(anzeige.price), 2)

            kandidaten.append({
                "id": anzeige.id,
                "watchlist_id": ziel["id"],
                "titel": anzeige.title,
                "url": anzeige.url,
                "preis": anzeige.price,
                "preis_typ": anzeige.price_type,
                "referenz": referenzwert,
                "p_ratio": bewertung["p_ratio"],
                "ersparnis_eur": ersparnis,
                "ort": anzeige.city,
                "plz": anzeige.zip_code,
                "eingestellt": eingestellt(anzeige).isoformat() if eingestellt(anzeige) else None,
                "bilder": detail.bilder[:4],
                "beschreibung": detail.beschreibung[:1500],
                "attribute": detail.attribute,
                "verkaeufer": {
                    "id": detail.verkaeufer.id,
                    "name": detail.verkaeufer.name,
                    "typ": detail.verkaeufer.typ,
                    "konto_seit": detail.verkaeufer.konto_seit.date().isoformat()
                                  if detail.verkaeufer.konto_seit else None,
                    "konto_alter_tage": bewertung["konto_alter_tage"],
                    "bewertung": detail.verkaeufer.bewertung,
                    "abzeichen": detail.verkaeufer.abzeichen,
                    "anzahl_anzeigen": bewertung["anzahl_anzeigen"],
                },
                "uebergabe": {
                    "abholung": bewertung["abholung"],
                    "versand": detail.versand_moeglich,
                    "kaeuferschutz": bewertung["kaeuferschutz"],
                },
                "score": bewertung["punkte"],
                "signale": {
                    "gruen": bewertung["gruen"],
                    "rot": bewertung["rot"],
                    "unkenntnis_bonus": bonus,
                    "tippfehler_im_titel": tippfehler,
                },
            })
            statistik["nach_scoring"] += 1

    # Ein Sweep und ein Keyword-Ziel koennen dieselbe Anzeige finden. Der
    # hoehere Score gewinnt, damit sie nur einmal in der Mail landet.
    beste: dict = {}
    for kandidat in kandidaten:
        vorhanden = beste.get(kandidat["id"])
        if vorhanden is None or kandidat["score"] > vorhanden["score"]:
            beste[kandidat["id"]] = kandidat
    statistik["doppelt_zusammengefasst"] = len(kandidaten) - len(beste)
    kandidaten = list(beste.values())

    kandidaten.sort(key=lambda k: ((k["signale"]["unkenntnis_bonus"], k["ersparnis_eur"] or 0)),
                    reverse=True)
    if limit:
        kandidaten = kandidaten[:limit]

    statistik["requests"] = api.requests
    statistik["laufzeit_sekunden"] = round(time.time() - start)

    ergebnis = {
        "generiert": datetime.now(BERLIN).isoformat(timespec="seconds"),
        "zeitraum": {"von": von.astimezone(BERLIN).isoformat(timespec="seconds"),
                     "bis": bis.astimezone(BERLIN).isoformat(timespec="seconds")},
        "statistik": statistik,
        "kandidaten": kandidaten,
    }

    # Bei kurzen Fenstern liefert ein einzelner Lauf zu wenig. Deshalb sammeln
    # sich Kandidaten ueber 24 Stunden an, bis die Routine sie abholt oder sie
    # veralten. Schon gemeldete verschwinden ueber deal_log.csv.
    ergebnis["kandidaten"] = _zusammenfuehren(kandidaten, bis)

    KANDIDATEN.write_text(json.dumps(ergebnis, ensure_ascii=False, indent=2), encoding="utf-8")
    gesehene_ergaenzen(neue_ids - gesehen, bis.date().isoformat())
    _protokoll_schreiben(ergebnis)
    return ergebnis


def _zusammenfuehren(neu: list, bis: datetime) -> list:
    """Neue Kandidaten mit den noch offenen aus frueheren Laeufen mischen."""
    gemeldet = set()
    log = WURZEL / "deal_log.csv"
    if log.exists():
        with log.open(encoding="utf-8") as datei:
            gemeldet = {z.get("ad_id") for z in csv.DictReader(datei)}

    gesammelt = {}
    if KANDIDATEN.exists():
        try:
            alt = json.loads(KANDIDATEN.read_text(encoding="utf-8")).get("kandidaten", [])
        except json.JSONDecodeError:
            alt = []
        grenze = bis - timedelta(hours=24)
        for kandidat in alt:
            zeit = kandidat.get("eingestellt")
            if not zeit:
                continue
            if datetime.fromisoformat(zeit) < grenze.astimezone(BERLIN):
                continue
            gesammelt[kandidat["id"]] = kandidat

    for kandidat in neu:
        gesammelt[kandidat["id"]] = kandidat

    offen = [k for k in gesammelt.values() if k["id"] not in gemeldet]
    offen.sort(key=lambda k: (k["signale"]["unkenntnis_bonus"], k["ersparnis_eur"] or 0),
               reverse=True)
    return offen


def _protokoll_schreiben(ergebnis: dict) -> None:
    tag = datetime.now(BERLIN).date().isoformat()
    ordner = WURZEL / "runs" / tag
    nummer = 1
    while ordner.exists():
        nummer += 1
        ordner = WURZEL / "runs" / f"{tag}-{nummer}"
    ordner.mkdir(parents=True)

    statistik = ergebnis["statistik"]
    zeilen = [
        f"# Scan-Lauf {ergebnis['generiert']}",
        "",
        f"Zeitraum: {ergebnis['zeitraum']['von']} bis {ergebnis['zeitraum']['bis']}",
        "",
        "| Filterstufe | verbleibend |",
        "|---|---|",
        f"| gesichtet | {statistik['gesichtet']} |",
        f"| Modell-Match | {statistik['nach_modellmatch']} |",
        f"| Vorfilter | {statistik['nach_vorfilter']} |",
        f"| Preisschwelle | {statistik['nach_preisschwelle']} |",
        f"| Scoring | {statistik['nach_scoring']} |",
        "",
        f"Requests: {statistik['requests']}, Laufzeit: {statistik['laufzeit_sekunden']} Sekunden",
        "",
    ]
    if statistik["ausschluesse"]:
        zeilen += ["## Ausschlussgruende", ""]
        for grund, anzahl in sorted(statistik["ausschluesse"].items(), key=lambda p: -p[1]):
            zeilen.append(f"- {grund}: {anzahl}")
        zeilen.append("")
    (ordner / "scan.md").write_text("\n".join(zeilen), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Kleinanzeigen Schnaeppchen-Scanner, Stufe 1")
    parser.add_argument("--watchlist", default=str(WURZEL / "watchlist.yaml"))
    parser.add_argument("--stunden", type=int, default=24)
    parser.add_argument("--limit", type=int, default=40)
    argumente = parser.parse_args()

    try:
        ergebnis = lauf(Path(argumente.watchlist), argumente.stunden, argumente.limit)
    except Gesperrt as fehler:
        print(f"ABBRUCH: {fehler}", file=sys.stderr)
        return 2

    statistik = ergebnis["statistik"]
    print(f"gesichtet {statistik['gesichtet']}, "
          f"Modell-Match {statistik['nach_modellmatch']}, "
          f"Preisschwelle {statistik['nach_preisschwelle']}, "
          f"Kandidaten {len(ergebnis['kandidaten'])}, "
          f"{statistik['requests']} Requests in {statistik['laufzeit_sekunden']}s")

    # Eine leere Ergebnismenge bei vorher erfolgreichen Laeufen sieht fuer den
    # Client genauso aus wie eine Sperre. Deshalb hart melden.
    if statistik["gesichtet"] == 0:
        print("ABBRUCH: keine einzige Anzeige gesichtet, vermutlich gesperrt", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
