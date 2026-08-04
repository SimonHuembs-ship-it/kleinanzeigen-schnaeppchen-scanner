"""Deterministische Vorfilter.

Laufen vor jeder Preislogik und kosten keinen zusaetzlichen Request. Reihenfolge
ist nicht beliebig: Gesuche muessen zuerst raus, weil Haendler-Ankaufsanzeigen
saemtliche Typcodes auf einmal enthalten und damit jede Modellsuche treffen.
"""

from __future__ import annotations

import re
import unicodedata

# "Suche Porsche 911 TURBO Ankauf 993 964 930 996 997 991 G Modell"
GESUCH = re.compile(
    r"^\s*(suche|suchen|ankauf|ankaufe|kaufe|gesucht|wir\s+kaufen|ich\s+suche)\b"
    r"|\bankauf\b.*\b(alle\s+modelle|zustand|defekt)\b"
    r"|\bsuche\b.*\bankauf\b",
    re.IGNORECASE,
)

FAELSCHUNG = re.compile(
    r"\b(nachmache|nachbau|replika|replica|clone|klon|kopie|fake|imitat|"
    r"1\s*:\s*1|wie\s+original|no\s+original|kein[e]?\s+original(ware)?)\b",
    re.IGNORECASE,
)

# Lockpreise, die nur der Sortierung dienen
LOCKPREISE = {1.0, 10.0, 11.0, 12.0, 111.0, 123.0, 1234.0}

# Emoji und Zierzeichen, die vor dem Matching weg muessen
ZIERRAT = re.compile(
    "[\u2190-\u27bf\u2b00-\u2bff\u3000-\u303f\ufe0f\u200d\u2600-\u26ff"
    "\U0001f000-\U0001faff]+"
)


def normalisieren(text: str) -> str:
    """Zierrat raus, HTML raus, Whitespace vereinheitlichen."""
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = ZIERRAT.sub(" ", text)
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"[\u2018\u2019\u201a\u201c\u201d\u201e\u2032\u2033\"']", "", text)
    return re.sub(r"\s+", " ", text).strip()


def ist_gesuch(titel: str) -> bool:
    return bool(GESUCH.search(normalisieren(titel)))


def ist_faelschung(text: str) -> bool:
    return bool(FAELSCHUNG.search(normalisieren(text)))


def ist_lockpreis(preis) -> bool:
    return preis is None or preis <= 0 or float(preis) in LOCKPREISE


def passt_zum_ziel(titel: str, ziel: dict) -> bool:
    """Positives Modell-Matching plus Ausschlussliste.

    Markenfilter allein waeren wertlos: Eine Porsche-Suche liefert ueberwiegend
    Cayenne, Macan und Panamera.
    """
    text = normalisieren(titel).lower()

    for wort in ziel.get("ausschluss", []):
        if re.search(rf"\b{re.escape(str(wort).lower())}", text):
            return False

    muster = ziel.get("muster") or []
    if not muster:
        return True
    return any(re.search(str(m), text, re.IGNORECASE) for m in muster)


def tippfehler_im_titel(titel: str, ziel: dict) -> str | None:
    """Gibt die gefundene Falschschreibung zurueck, sonst None.

    Ein Tippfehler im Modellnamen ist ein starkes Signal: die Anzeige ist ueber
    die normale Suche kaum auffindbar, der Verkaeufer kennt sich oft nicht aus.
    """
    text = normalisieren(titel).lower()
    for falsch in ziel.get("tippfehler", []):
        if re.search(rf"\b{re.escape(str(falsch).lower())}\b", text):
            return str(falsch)
    return None


def wirkt_generisch(titel: str) -> bool:
    """Titel ohne Modellbezeichnung, typisch fuer Verkaeufer ohne Sachkenntnis."""
    text = normalisieren(titel)
    hat_zahl = bool(re.search(r"\d", text))
    hat_versalien = bool(re.search(r"\b[A-Z]{2,}\b", text))
    return len(text) < 30 and not hat_zahl and not hat_versalien
