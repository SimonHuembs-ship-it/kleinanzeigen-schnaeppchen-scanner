"""Referenzpreis aus Kleinanzeigen selbst.

Kleinanzeigen ist seine eigene Preisdatenbank. Fuer jeden Kandidaten laeuft eine
Suche nach derselben Modellbezeichnung, daraus kommt der Median. Das kostet eine
Zusatzsuche pro Kandidat und braucht keinen externen Preisdienst.
"""

from __future__ import annotations

import statistics

from . import filter as vorfilter

MINDEST_VERGLEICHE = 8


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
    frage = ziel.get("referenz_query") or ziel.get("id", "")

    # Unterscheidende Attribute anhaengen, damit nicht 256 GB gegen 512 GB
    # verglichen wird.
    if detail:
        for schluessel in ziel.get("referenz_attribute", []) or []:
            wert = detail.attribute.get(schluessel)
            if wert:
                frage = f"{frage} {wert}"

    if cache is not None and frage in cache:
        return cache[frage]

    treffer = api.suche(
        frage,
        category_id=ziel.get("kategorie"),
        min_price=ziel.get("preis_min"),
        max_price=ziel.get("preis_max"),
        seiten=2,
    )

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
        preise.append(float(kandidat.price))

    if len(preise) < MINDEST_VERGLEICHE:
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
