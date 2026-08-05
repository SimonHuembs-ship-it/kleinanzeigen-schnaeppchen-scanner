"""Falschschreibungen systematisch erzeugen.

Von Hand gepflegte Tippfehlerlisten sind immer unvollstaendig. Diese
Transformationen decken die Klassen ab, die bei deutschen Nutzern tatsaechlich
auftreten. Zufaellige Nachbartasten sind bewusst nicht dabei: sie erzeugen
Varianten, die niemand tippt, und kosten trotzdem je eine Suchanfrage.

Kleinanzeigen normalisiert selbst ss/ss und Plurale, ein fehlendes Fugen-s
aber nicht. Genau solche Luecken sind das Ziel.
"""

from __future__ import annotations

import re

# Deutsch-englische und phonetische Verwechslungen, in beide Richtungen.
LAUTPAARE = [
    ("sch", "sh"), ("c", "k"), ("k", "c"), ("z", "s"), ("s", "z"),
    ("ph", "f"), ("f", "ph"), ("ie", "i"), ("y", "i"), ("i", "y"),
    ("v", "w"), ("w", "v"), ("ck", "k"), ("tz", "z"),
]

UMLAUTE = [("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")]


def _dreher(wort: str) -> set:
    """Zwei benachbarte Buchstaben vertauscht: Telsa statt Tesla."""
    return {wort[:i] + wort[i + 1] + wort[i] + wort[i + 2:]
            for i in range(len(wort) - 1) if wort[i] != wort[i + 1]}


def _ausgelassen(wort: str) -> set:
    """Ein Buchstabe fehlt: Porche statt Porsche."""
    return {wort[:i] + wort[i + 1:] for i in range(1, len(wort) - 1)}


def _verdoppelt(wort: str) -> set:
    """Ein Buchstabe zu viel: Ducatti statt Ducati."""
    return {wort[:i] + wort[i] + wort[i:] for i in range(1, len(wort) - 1)}


def _lautlich(wort: str) -> set:
    varianten = set()
    for alt, neu in LAUTPAARE:
        if alt in wort:
            varianten.add(wort.replace(alt, neu, 1))
    for umlaut, ersatz in UMLAUTE:
        if umlaut in wort:
            varianten.add(wort.replace(umlaut, ersatz))
        if ersatz in wort and len(ersatz) > 1:
            varianten.add(wort.replace(ersatz, umlaut, 1))
    return varianten


def _fugen_s(begriff: str) -> set:
    """Fehlendes Fugen-s in Komposita: Haushalsaufloesung.

    Kleinanzeigen normalisiert das nicht, deshalb sind solche Anzeigen ueber
    die normale Suche praktisch unauffindbar.
    """
    return {re.sub(rf"s{teil}", teil, begriff, count=1)
            for teil in ("auflösung", "aufloesung", "verkauf", "wagen", "haus")
            if f"s{teil}" in begriff.lower()}


def erzeugen(begriff: str, anzahl: int = 6) -> list:
    """Liefert bis zu `anzahl` plausible Falschschreibungen eines Begriffs.

    Transformiert nur das laengste Wort: bei "Technics SL-1200" ist die Marke
    fehleranfaellig, die Typnummer tippt niemand falsch ab.
    """
    woerter = [w for w in re.split(r"[\s\-]+", begriff) if len(w) >= 5]
    if not woerter:
        return []
    ziel = max(woerter, key=len).lower()

    varianten = set()
    for erzeuger in (_dreher, _ausgelassen, _verdoppelt, _lautlich):
        varianten |= erzeuger(ziel)
    varianten |= _fugen_s(begriff.lower())
    varianten.discard(ziel)

    # Kuerzere Varianten zuerst: ausgelassene Buchstaben und Dreher sind
    # haeufiger als Verdopplungen.
    sortiert = sorted(varianten, key=lambda v: (len(v), v))
    return [begriff.lower().replace(ziel, v) if ziel in begriff.lower() else v
            for v in sortiert[:anzahl]]
