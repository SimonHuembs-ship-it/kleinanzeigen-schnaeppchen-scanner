"""Zugriff auf die Kleinanzeigen-Mobile-API.

Kapselt zwei Dinge, die der Client von Haus aus nicht kann: Zeitfenster-Abfragen
ueber modAfter/modBefore, und ein Anhalten mit klarer Fehlermeldung, wenn die API
uns aussperrt statt still leere Listen zu liefern.
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from kleinanzeigen_api import KleinanzeigenAPI
from kleinanzeigen_api.client import API_HOST

WINDOW_FMT = "%Y-%m-%dT%H:%M:%SZ"

# Die API deckelt den Offset bei 10.000. Darueber kommt eine leere Liste ohne
# Fehler zurueck, was von einer Sperre nicht zu unterscheiden ist.
MAX_OFFSET = 10_000
PAGE_SIZE = 100


class Gesperrt(RuntimeError):
    """Die API hat uns abgewiesen (401/403) oder liefert dauerhaft nichts."""


@dataclass
class Verkaeufer:
    id: str | None
    name: str | None
    typ: str | None
    konto_seit: datetime | None
    bewertung: float | None
    abzeichen: dict


@dataclass
class Detail:
    beschreibung: str
    verkaeufer: Verkaeufer
    versand_moeglich: bool
    bilder: list
    attribute: dict


class Api:
    def __init__(self, rate_limit: float = 0.8):
        self.client = KleinanzeigenAPI()
        self.client.rate_limit = rate_limit
        self.requests = 0

    # -- Grundlagen ----------------------------------------------------------

    def _seite(self, **params) -> tuple:
        params.setdefault("size", PAGE_SIZE)
        params.setdefault("adType", "OFFERED")
        for versuch in range(4):
            try:
                self.requests += 1
                antwort = self.client._get(f"{API_HOST}/api/ads.json", params=params)
                return self.client._parse_ads_block(antwort.json())
            except RuntimeError as fehler:
                # Der Client wirft bei 401/403 sofort, ohne Wiederholung.
                if "credentials" in str(fehler).lower() or "401" in str(fehler) or "403" in str(fehler):
                    raise Gesperrt(f"API weist uns ab: {fehler}") from fehler
                raise
            except Exception:
                if versuch == 3:
                    raise
                time.sleep(5 * (versuch + 1))
        return 0, []

    # -- Suchverfahren -------------------------------------------------------

    def suche(self, q: str, *, category_id=None, min_price=None, max_price=None,
              seiten: int = 1) -> list:
        """Keyword-Suche, nach Datum sortiert."""
        treffer = []
        for seite in range(seiten):
            params = {"page": seite, "q": q, "sortType": "DATE_DESCENDING"}
            if category_id:
                params["categoryId"] = category_id
            if min_price is not None:
                params["minPrice"] = min_price
            if max_price is not None:
                params["maxPrice"] = max_price
            _, anzeigen = self._seite(**params)
            treffer.extend(anzeigen)
            if len(anzeigen) < PAGE_SIZE:
                break
        return treffer

    def fenster(self, *, category_id=None, von: datetime, bis: datetime,
                min_price=None, max_price=None) -> list:
        """Alle Anzeigen einer Kategorie in einem Zeitfenster.

        Schneidet das Fenster so lange in Haelften, bis jedes Teilfenster unter
        die 10.000er-Decke passt. Ergebnisse werden ueber die Anzeigen-ID
        entdoppelt, weil aufeinanderfolgende Seiten aus verschiedenen
        Cache-Schnappschuessen stammen und sich ueberlappen.
        """
        gefunden: dict = {}
        offen = [(von, bis)]

        while offen:
            fenster_von, fenster_bis = offen.pop()
            basis = {"sortType": "DATE_DESCENDING",
                     "modAfter": fenster_von.strftime(WINDOW_FMT),
                     "modBefore": fenster_bis.strftime(WINDOW_FMT)}
            if category_id:
                basis["categoryId"] = category_id
            if min_price is not None:
                basis["minPrice"] = min_price
            if max_price is not None:
                basis["maxPrice"] = max_price

            anzahl, erste = self._seite(page=0, **basis)

            if anzahl > MAX_OFFSET and (fenster_bis - fenster_von) > timedelta(minutes=2):
                mitte = fenster_von + (fenster_bis - fenster_von) / 2
                offen.extend([(fenster_von, mitte), (mitte, fenster_bis)])
                continue

            for anzeige in erste:
                gefunden[anzeige.id] = anzeige

            seiten = min((anzahl + PAGE_SIZE - 1) // PAGE_SIZE, MAX_OFFSET // PAGE_SIZE)
            for seite in range(1, seiten):
                _, anzeigen = self._seite(page=seite, **basis)
                if not anzeigen:
                    break
                for anzeige in anzeigen:
                    gefunden[anzeige.id] = anzeige

        return list(gefunden.values())

    # -- Detailabruf ---------------------------------------------------------

    def detail(self, ad_id: str) -> Detail | None:
        self.requests += 1
        try:
            roh = self.client._fetch_ad_json(ad_id)
        except Exception:
            return None
        if not roh:
            return None
        wert = list(roh.values())[0].get("value", {})

        seit = (wert.get("user-since-date-time") or {}).get("value")
        bewertung = ((wert.get("user-rating") or {}).get("averageRating") or {}).get("value")
        abzeichen = {b.get("name"): int(b.get("level", 0) or 0)
                     for b in (wert.get("userBadges") or {}).get("badges", [])}
        versand = wert.get("shipping-options")

        attribute = {}
        for eintrag in (wert.get("attributes") or {}).get("attribute", []) or []:
            name = eintrag.get("localized-label") or eintrag.get("name")
            werte = eintrag.get("value") or []
            if isinstance(werte, dict):
                werte = [werte]
            if name and werte:
                attribute[name] = werte[0].get("localized-label") or werte[0].get("value")

        return Detail(
            beschreibung=(wert.get("description") or {}).get("value", "") or "",
            verkaeufer=Verkaeufer(
                id=(wert.get("user-id") or {}).get("value"),
                name=(wert.get("contact-name") or {}).get("value"),
                typ=(wert.get("seller-account-type") or {}).get("value"),
                konto_seit=_datum(seit),
                bewertung=float(bewertung) if bewertung is not None else None,
                abzeichen=abzeichen,
            ),
            versand_moeglich=bool(versand and versand.get("shipping-option")),
            bilder=[b.get("link", [{}])[0].get("href")
                    for b in (wert.get("pictures") or {}).get("picture", []) or []],
            attribute=attribute,
        )

    def anzeigen_des_verkaeufers(self, user_id: str) -> list:
        """Alle aktiven Anzeigen eines Kontos, fuer die Historienpruefung."""
        self.requests += 1
        try:
            antwort = self.client._get(f"{API_HOST}/api/users/{user_id}/ads.json",
                                       params={"page": 0, "size": 50})
            _, anzeigen = self.client._parse_ads_block(antwort.json())
            return anzeigen
        except Exception:
            return []


def eingestellt(anzeige) -> datetime | None:
    """Der Client liefert `posted` als String. Immer hierueber gehen.

    Achtung: Das ist das Reaktivierungsdatum, nicht das Ersteinstelldatum.
    Rund 2 Prozent der datumssortierten Treffer sind gebumpte Altanzeigen.
    """
    return _datum(getattr(anzeige, "posted", None))


def _datum(wert) -> datetime | None:
    if not wert:
        return None
    try:
        return datetime.fromisoformat(str(wert).replace("Z", "+00:00"))
    except ValueError:
        return None


def jetzt() -> datetime:
    return datetime.now(timezone.utc)
