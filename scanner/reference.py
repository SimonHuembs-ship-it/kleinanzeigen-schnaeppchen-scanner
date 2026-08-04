"""Referenzpreis aus Kleinanzeigen selbst.

Kleinanzeigen ist seine eigene Preisdatenbank. Fuer jeden Kandidaten laeuft eine
Suche nach derselben Modellbezeichnung, daraus kommt der Median. Das kostet eine
Zusatzsuche pro Kandidat und braucht keinen externen Preisdienst.
"""

from __future__ import annotations

import re
import statistics

from . import filter as vorfilter

MINDEST_VERGLEICHE = 8

# Fuellwoerter, die keine Modellbezeichnung sind und die automatische
# Referenzfrage nur verwaessern.
RAUSCHEN = {
    "vb", "verhandelbar", "festpreis", "neu", "neuwertig", "top", "guter", "gute",
    "sehr", "wie", "top-zustand", "zustand", "gepflegt", "gepflegter", "originaler",
    "original", "selten", "rar", "schoen", "schön", "voll", "komplett", "inkl",
    "inklusive", "mit", "und", "oder", "ohne", "von", "der", "die", "das", "ein",
    "eine", "einer", "fuer", "für", "aus", "zu", "im", "am", "auf", "an", "in",
    "tuev", "tüv", "hu", "au", "km", "ez", "bj", "baujahr", "erstzulassung",
    "verkaufe", "verkauf", "biete", "abzugeben", "privatverkauf", "privat",
    "nachlass", "sammlungsaufloesung", "sammlungsauflösung", "haushaltsaufloesung",
    "haushaltsauflösung", "notverkauf", "umzug", "umzugsbedingt", "wegen",
    "guenstig", "günstig", "schnaeppchen", "schnäppchen", "defekt", "bastler",
    "mein", "meine", "meinen", "meiner", "unser", "unsere", "hier", "sofort",
    "gebraucht", "gebrauchter", "guterhalten", "kaum", "benutzt", "genutzt",
}


def _auto_query(titel: str, ziel: dict | None = None) -> str:
    """Baut die Referenzfrage aus dem Anzeigentitel.

    Noetig fuer heterogene Ziele wie Youngtimer, wo eine feste Frage nie
    passen kann. Vier Kerntoken reichen: mehr verengt die Vergleichsbasis
    unter die Mindestzahl.
    """
    text = vorfilter.normalisieren(titel)

    # Steht der Tippfehler im Titel, darf er nicht in die Referenzfrage:
    # danach findet die Suche genauso wenig wie ein normaler Nutzer.
    if ziel:
        ersatz = ziel.get("referenz_marke", "")
        for falsch in ziel.get("tippfehler", []) or []:
            text = re.sub(rf"\b{re.escape(str(falsch))}\b", ersatz, text, flags=re.I)
    token = []
    for wort in re.split(r"[\s,;|/*#\-]+", text):
        sauber = wort.strip(".:!?()[]\"'")
        if sauber.lower() in RAUSCHEN:
            continue
        if len(sauber) < 2 and not (sauber.isupper() or sauber.isdigit()):
            continue
        if not sauber:
            continue
        if not re.search(r"[A-Za-zÄÖÜäöü0-9]", sauber):
            continue
        if sauber.lower() in {t.lower() for t in token}:
            continue
        token.append(sauber)
        if len(token) == 4:
            break
    return " ".join(token)


def _frage_token(frage: str) -> list:
    return [t.lower() for t in re.split(r"\s+", frage)
            if len(t) > 2 or any(z.isdigit() for z in t)]


def _passt_zur_frage(titel: str, token: list) -> bool:
    """Prueft, ob eine Vergleichsanzeige wirklich dasselbe Produkt ist.

    Die Kleinanzeigen-Suche ist unscharf: eine Suche nach "iPhone 13 Pro 128"
    liefert auch 14er und 15er. Ohne diese Pruefung ist der Median eine
    Mischung ueber mehrere Generationen und die Ersparnis frei erfunden.
    """
    if not token:
        return False
    text = vorfilter.normalisieren(titel).lower()
    treffer = sum(1 for t in token if t in text)
    return treffer >= max(2, round(len(token) * 0.75))


def _kennwerte(preise: list) -> tuple:
    preise = sorted(preise)
    median = statistics.median(preise)
    p25 = preise[max(0, len(preise) // 4 - 1)]
    return median, p25


def referenzpreis(api, ziel: dict, anzeige, detail=None, cache: dict | None = None) -> dict | None:
    """Median vergleichbarer Anzeigen, oder None wenn die Basis zu duenn ist.

    Die Preisgrenzen des Ziels dienen als Plausibilitaetsrahmen: ohne sie
    verseuchen Zubehoeranzeigen (Felgen, Huellen, Ersatzteile) den Median.
    """
    vorgabe = ziel.get("referenz_query")
    if not vorgabe or vorgabe == "auto":
        frage = _auto_query(anzeige.title, ziel)
    else:
        frage = vorgabe

    # Unterscheidende Attribute anhaengen, damit nicht 256 GB gegen 512 GB
    # verglichen wird.
    if detail:
        for schluessel in ziel.get("referenz_attribute", []) or []:
            wert = detail.attribute.get(schluessel)
            if wert:
                frage = f"{frage} {wert}"

    if cache is not None and frage in cache:
        return cache[frage]

    if not frage:
        if cache is not None:
            cache[frage] = None
        return None

    treffer = api.suche(
        frage,
        category_id=ziel.get("kategorie"),
        min_price=ziel.get("preis_min"),
        max_price=ziel.get("preis_max"),
        seiten=1,
    )

    token = _frage_token(frage)
    preise = []
    for kandidat in treffer:
        if kandidat.id == anzeige.id:
            continue
        if not kandidat.price or kandidat.price <= 0:
            continue
        if vorfilter.ist_gesuch(kandidat.title):
            continue
        if not vorfilter.passt_zum_ziel(kandidat.title, ziel):
            continue
        if not _passt_zur_frage(kandidat.title, token):
            continue
        preise.append(float(kandidat.price))

    if not frage:
        ergebnis = None
    elif len(preise) < MINDEST_VERGLEICHE:
        ergebnis = None
    else:
        median, p25 = _kennwerte(preise)
        # Angebotspreise liegen ueber Transaktionspreisen. Bei Fahrzeugen ist
        # der Abstand mit 8 bis 15 Prozent belegt, deshalb der Abschlag.
        korrektur = float(ziel.get("angebotsaufschlag", 0.0))
        median = median * (1 - korrektur)
        ergebnis = {
            "median": round(median, 2),
            "p25": round(p25, 2),
            "n": len(preise),
            "query": frage,
            "korrektur": korrektur,
        }

    if cache is not None:
        cache[frage] = ergebnis
    return ergebnis
