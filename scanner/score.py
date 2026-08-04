"""Seriositaets-Scoring.

Grundsatz: Das Ergebnis heisst nie "serioes", sondern "keine roten Flaggen".
Es gibt auf Kleinanzeigen kein Merkmal, das Serioesitaet positiv beweist. Das
hoechste Zuverlaessigkeits-Abzeichen braucht sechs Bewertungen aus maximal
zehn, und bewerten darf man sich schon nach zwei gewechselten Nachrichten,
ganz ohne Kauf.
"""

from __future__ import annotations

import re
from datetime import timezone

from .api import eingestellt
from .filter import normalisieren

# -- Harte Ausschluesse ------------------------------------------------------

AUSSCHLUESSE = [
    ("messenger", re.compile(r"\b(whats\s*app|wa\.me|telegram|t\.me|signal\b|viber|threema)\b", re.I)),
    ("externer_link", re.compile(r"\b(?:https?://|www\.)(?!(?:www\.)?kleinanzeigen\.de)[a-z0-9.-]+\.[a-z]{2,}", re.I)),
    ("zahlung_ohne_schutz", re.compile(
        r"\b(freunde\s*(und|&|\+)\s*familie|f\s*&\s*f|friends\s*(and|&)\s*family|western\s*union|"
        r"money\s*gram|paysafe|neosurf|bitcoin|btc\b|krypto|usdt|"
        r"google\s*play[- ]?(karte|code)|amazon[- ]?gutschein)", re.I)),
    ("fake_treuhand", re.compile(
        r"\b(treuhand(service|konto|abwicklung)?|escrow|ebay\s*motors|"
        r"kleinanzeigen[- ]?(liefer|versand)service)\b", re.I)),
    ("auslandslegende", re.compile(
        r"\b(bin|befinde\s*mich|arbeite|wohne)\s+(derzeit|momentan|zur\s*zeit|gerade|aktuell)?\s*"
        r"(im|in)\s+ausland\b|\b(bohrinsel|auslandseinsatz|stationiert|montage\s+im\s+ausland)\b", re.I)),
    ("spedition", re.compile(
        r"\b(spedition|logistik(firma|partner)|transportunternehmen)\b.{0,60}"
        r"\b(holt\s+ab|uebernimmt|übernimmt|organisiert|liefert)\b", re.I)),
    ("vorab_gebuehren", re.compile(
        r"\b(zoll(gebuehren|gebühren|kosten)|einfuhrumsatzsteuer|transportversicherung|kaution)\b"
        r".{0,80}\b(vorab|im\s*voraus|vorher|zuerst|ueberweisen|überweisen)\b", re.I)),
    # Realfund: eine Anzeige begann woertlich mit "Natuerlich, hier ist die
    # fertige Verkaufsanzeige fuer ..."
    ("ki_prompt_rest", re.compile(
        r"^\s*(natuerlich|natürlich|gerne|klar|selbstverstaendlich|selbstverständlich)\s*[,!]\s|"
        r"\bhier\s+ist\s+(die|dein[e]?|eine|ein)\s+(fertige\s+)?(verkaufs)?(anzeige|beschreibung)\b|"
        r"\b(als\s+(ki|ai|sprachmodell)|ich\s+bin\s+ein\s+(ki|sprachmodell))\b", re.I)),
]

# -- Textmuster fuer Flaggen -------------------------------------------------

KEINE_ABHOLUNG = re.compile(
    r"\b(nur\s+versand|versand\s+only|kein[e]?\s*(selbst)?abholung|"
    r"abholung\s+(leider\s+)?nicht\s+m(oe|ö)glich)\b", re.I)
ABHOLUNG = re.compile(
    r"\b(selbstabholung|abholung|abzuholen|besichtigung|barzahlung\s+bei\s+abholung)\b", re.I)
VORKASSE = re.compile(
    r"\b(vorkasse|vorauszahlung|zahlung\s+vor\s+versand|nach\s+zahlungseingang)\b", re.I)
ZEITDRUCK = re.compile(
    r"\b(muss\s+(heute|schnell|dringend)\s+(weg|raus)|nur\s+(heute|noch\s+bis)|"
    r"letzte\s+chance|schnell\s+zugreifen|viele\s+(interessenten|anfragen))\b", re.I)
MAENGEL = re.compile(
    r"\b(gebrauchsspuren|kratzer|delle|riss|abnutzung|nicht\s+mehr\s+ganz|"
    r"kleiner?\s+(mangel|defekt)|akku\s+(schw(ae|ä)chelt|nicht\s+mehr))\b", re.I)
PREISBEGRUENDUNG = re.compile(
    r"\b(wegen\s+(umzug|umzugs|wohnungsaufl(oe|ö)sung|renovierung|platzmangel|trennung|"
    r"krankheit|todesfall|auswanderung)|haushaltsaufl(oe|ö)sung|nachlass|erbschaft|"
    r"sammlungsaufl(oe|ö)sung|h(oe|ö)re\s+mit\s+dem\s+hobby\s+auf|brauche\s+den\s+platz|"
    r"steht\s+nur\s+rum)\b", re.I)
SPEZIFIK = re.compile(
    r"\b(seit\s+\d{4}\s+in\s+gebrauch|gekauft\s+(im|am)\s+\w+\s*\d{4}|"
    r"\d+\s*(std|stunden|betriebsstunden|km|tkm)\b|akkukapazit(ae|ä)t\s+\d+|"
    r"zyklen\s*:?\s*\d+|seriennummer|scheckheft|rechnung\s+(liegt\s+bei|vorhanden))\b", re.I)
GEWERBETEXT = re.compile(
    r"\b(widerrufsrecht|widerrufsbelehrung|gew(ae|ä)hrleistung|mwst\.?\s*ausweisbar|"
    r"differenzbesteuert|§\s*25a)\b", re.I)

# Orte, an denen Abholung faktisch ausscheidet. Realfall: Klimaanlage mit
# Abholort Helgoland, Konto einen Tag alt.
UNERREICHBAR = re.compile(
    r"\b(helgoland|hallig|juist|baltrum|langeoog|spiekeroog|wangerooge|norderney|"
    r"borkum|amrum|f(oe|ö)hr|pellworm|hiddensee|neuwerk)\b", re.I)


def bewerten(anzeige, detail, referenz, ziel, verkaeufer_anzeigen=None) -> dict:
    """Gibt Punktzahl, Signale und Ausschlussgrund zurueck."""
    text = normalisieren(f"{anzeige.title} {detail.beschreibung}")
    verkaeufer = detail.verkaeufer

    for name, muster in AUSSCHLUESSE:
        if muster.search(text):
            return {"ausschluss": name}

    p_ratio = None
    if referenz and referenz["median"]:
        p_ratio = round(float(anzeige.price) / referenz["median"], 3)

    abholung = bool(ABHOLUNG.search(text)) and not KEINE_ABHOLUNG.search(text)
    abholung = abholung or not detail.versand_moeglich
    kaeuferschutz = detail.versand_moeglich

    # Die schaerfste Einzelregel: schneidet praktisch den gesamten
    # Vorkassebetrug weg.
    if p_ratio is not None and p_ratio < 0.70 and not abholung and not kaeuferschutz:
        return {"ausschluss": "kein_abholung_kein_schutz"}
    if p_ratio is not None and p_ratio < 0.25:
        return {"ausschluss": "preis_unplausibel"}

    alter = None
    if verkaeufer.konto_seit:
        bezug = eingestellt(anzeige)
        if bezug:
            alter = (bezug.astimezone(timezone.utc) - verkaeufer.konto_seit.astimezone(timezone.utc)).days

    punkte = 50
    rot, gruen = [], []

    def minus(betrag, grund):
        nonlocal punkte
        punkte -= betrag
        rot.append(grund)

    def plus(betrag, grund):
        nonlocal punkte
        punkte += betrag
        gruen.append(grund)

    # Konto
    if alter is not None:
        if alter < 3:
            minus(30, "Konto juenger als 3 Tage")
        elif alter < 30:
            minus(18, "Konto juenger als 30 Tage")
        elif alter < 180:
            minus(8, "Konto juenger als 6 Monate")
        elif alter > 730:
            plus(12, f"Konto seit {verkaeufer.konto_seit.year}")

    # Historie. Ein Konto von 2016, dessen saemtliche Anzeigen von heute
    # stammen, ist gefaehrlicher als ein neues Konto mit plausiblen Anzeigen.
    anzahl_anzeigen = None
    if verkaeufer_anzeigen is not None:
        anzahl_anzeigen = len(verkaeufer_anzeigen)
        monate = {d.strftime("%Y-%m") for d in (eingestellt(a) for a in verkaeufer_anzeigen) if d}
        alle_frisch = len(monate) <= 1
        if alter and alter > 540 and alle_frisch and anzahl_anzeigen >= 3:
            if not _haushaltsaufloesung(verkaeufer_anzeigen):
                minus(35, "Altes Konto, aber alle Anzeigen frisch")
        elif len(monate) >= 3:
            plus(15, "Anzeigenhistorie ueber mehrere Monate gestreut")

    # Bewertung
    if verkaeufer.bewertung is not None:
        if verkaeufer.bewertung < 0.70:
            minus(25, f"Bewertung {verkaeufer.bewertung:.2f}")
        elif verkaeufer.bewertung < 0.85:
            minus(10, f"Bewertung {verkaeufer.bewertung:.2f}")
        elif verkaeufer.bewertung >= 0.90 and verkaeufer.abzeichen.get("reliability", 0) >= 2:
            plus(15, f"Bewertung {verkaeufer.bewertung:.2f}, zuverlaessig")

    # Uebergabe
    if KEINE_ABHOLUNG.search(text):
        minus(30, "Abholung ausgeschlossen")
    elif abholung:
        plus(20, "Abholung moeglich")
    if detail.versand_moeglich and not kaeuferschutz:
        minus(30, "Versand ohne Kaeuferschutz")
    elif kaeuferschutz:
        plus(18, "Kaeuferschutz verfuegbar")
    if UNERREICHBAR.search(anzeige.city or ""):
        minus(25, f"Abholort faktisch unerreichbar ({anzeige.city})")
    if VORKASSE.search(text):
        minus(25, "Vorkasse gefordert")
    if ZEITDRUCK.search(text):
        minus(12, "Zeitdruckformel im Text")

    # Preis
    if p_ratio is not None and p_ratio < 0.45:
        minus(20, f"Preis nur {p_ratio:.0%} des Marktwerts")

    # Inhalt
    if len(detail.bilder) <= 1 and anzeige.price and anzeige.price > 200:
        minus(12, "Hoechstens ein Bild")
    elif len(detail.bilder) >= 4:
        plus(12, f"{len(detail.bilder)} Bilder")
    if len(detail.beschreibung) < 80 and anzeige.price and anzeige.price > 200:
        minus(12, "Beschreibung sehr duenn")
    if MAENGEL.search(text):
        plus(15, "Maengel offengelegt")
    if PREISBEGRUENDUNG.search(text):
        plus(15, "Preisbegruendung genannt")
    if SPEZIFIK.search(text):
        plus(12, "Konkrete Angaben zum Geraet")
    if verkaeufer.typ == "PRIVATE" and GEWERBETEXT.search(text):
        minus(12, "Gewerbetext auf Privatprofil")

    punkte = max(0, min(100, punkte))

    return {
        "punkte": punkte,
        "p_ratio": p_ratio,
        "rot": rot,
        "gruen": gruen,
        "konto_alter_tage": alter,
        "anzahl_anzeigen": anzahl_anzeigen,
        "abholung": abholung,
        "kaeuferschutz": kaeuferschutz,
    }


def _haushaltsaufloesung(anzeigen) -> bool:
    """Haushaltsaufloesung und Kontouebernahme sehen zunaechst gleich aus.

    Unterschied: die Aufloesung ist heterogen und niedrigpreisig, an einem Ort,
    mit Abholung. Die Uebernahme ist homogen hochpreisig und versandfaehig.
    """
    preise = [a.price for a in anzeigen if a.price]
    staedte = {a.city for a in anzeigen if a.city}
    if len(anzeigen) < 5 or not preise:
        return False
    preise.sort()
    median = preise[len(preise) // 2]
    return median < 80 and len(staedte) == 1


def unkenntnis_profil(anzeige, detail, score, tippfehler, generisch) -> bool:
    """Das wertvollste Fundmuster.

    Nur Abholung, wenige Bilder, altes Konto mit wenigen Anzeigen, Tippfehler
    im Modellnamen. Sieht nach klassischen Qualitaetsmassstaeben schlecht aus,
    ist aber gleichzeitig schnaeppchenreich und betrugssicher: ohne Versand
    verdient ein Betrueger nichts.
    """
    if score.get("p_ratio") is None or score["p_ratio"] >= 0.60:
        return False
    if detail.versand_moeglich or not score.get("abholung"):
        return False
    if len(detail.bilder) > 3:
        return False
    if not (tippfehler or generisch):
        return False
    if (score.get("konto_alter_tage") or 0) <= 365:
        return False
    anzahl = score.get("anzahl_anzeigen")
    return anzahl is None or anzahl <= 5
