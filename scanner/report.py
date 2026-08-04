"""Rendert email_output.html aus deals.json.

Die Routine liefert das Urteil, dieses Modul das Layout. So bleibt die Mail
ueber alle Laeufe identisch aufgebaut, und die Routine muss kein HTML schreiben.
"""

from __future__ import annotations

import html
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
DEALS = WURZEL / "deals.json"
AUSGABE = WURZEL / "email_output.html"
BERLIN = timezone(timedelta(hours=2))

MONATE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli",
          "August", "September", "Oktober", "November", "Dezember"]

NAVY = "#0f2440"
ROT = "#c62828"
GRAU = "#5b6472"
RAHMEN = "#e2e6ec"


def _datum_lang(wert: str) -> str:
    zeitpunkt = datetime.fromisoformat(wert)
    return f"{zeitpunkt.day}. {MONATE[zeitpunkt.month - 1]} {zeitpunkt.year}"


def _datum_zeit(wert: str) -> str:
    zeitpunkt = datetime.fromisoformat(wert)
    return f"{_datum_lang(wert)}, {zeitpunkt:%H:%M} Uhr"


def _zahl(wert) -> str:
    return f"{wert:,}".replace(",", ".")


def _euro(betrag) -> str:
    if betrag is None:
        return "keine Angabe"
    return f"{betrag:,.0f} €".replace(",", ".")


def _verkaeufer_zeile(verkaeufer: dict) -> str:
    teile = []
    if verkaeufer.get("konto_seit"):
        teile.append(f"Konto seit {verkaeufer['konto_seit'][:4]}")
    if verkaeufer.get("bewertung") is not None:
        teile.append(f"Bewertung {verkaeufer['bewertung']:.0%}")
    abzeichen = verkaeufer.get("abzeichen") or {}
    if abzeichen.get("reliability"):
        teile.append(f"Zuverlässigkeit Stufe {abzeichen['reliability']}")
    if verkaeufer.get("anzahl_anzeigen") is not None:
        teile.append(f"{verkaeufer['anzahl_anzeigen']} aktive Anzeigen")
    if verkaeufer.get("typ") == "COMMERCIAL":
        teile.append("gewerblich")
    return " · ".join(teile) or "keine Verkäuferdaten"


def _karte(deal: dict) -> str:
    bild = (deal.get("bilder") or [None])[0]
    uebergabe = deal.get("uebergabe", {})
    weg = "Abholung" if uebergabe.get("abholung") else "Versand"
    if uebergabe.get("abholung") and uebergabe.get("versand"):
        weg = "Abholung oder Versand"
    if uebergabe.get("kaeuferschutz"):
        weg += ", Käuferschutz möglich"

    ersparnis = ""
    if deal.get("ersparnis_eur") and deal.get("p_ratio"):
        ersparnis = (
            f'<div style="font-size:15px;color:{ROT};font-weight:bold;padding-top:2px">'
            f'{_euro(deal["ersparnis_eur"])} unter Marktwert '
            f'<span style="font-weight:normal;color:{GRAU}">'
            f'(Median {_euro(deal["referenz"]["median"])} aus {deal["referenz"]["n"]} Vergleichsanzeigen, '
            f'Angebot bei {deal["p_ratio"]:.0%})</span></div>'
        )
    elif deal.get("referenz_hinweis"):
        ersparnis = (f'<div style="font-size:14px;color:{GRAU};padding-top:2px">'
                     f'{html.escape(deal["referenz_hinweis"])}</div>')

    marke = ""
    if deal.get("unkenntnis_bonus"):
        marke = (f'<span style="background:{ROT};color:#fff;font-size:11px;'
                 f'padding:2px 7px;border-radius:3px;margin-left:8px;'
                 f'vertical-align:middle">Verkäufer kennt den Wert vermutlich nicht</span>')

    bildzelle = ""
    if bild:
        bildzelle = (
            f'<td width="160" valign="top" style="padding-right:16px">'
            f'<img src="{html.escape(bild)}" width="160" alt="" '
            f'style="width:160px;border-radius:4px;display:block"></td>'
        )

    zeilen = [
        f'<div style="font-size:13px;color:{GRAU};padding-bottom:6px">'
        f'{html.escape(deal.get("ort") or "")} · {weg} · eingestellt '
        f'{_datum_zeit(deal["eingestellt"]) if deal.get("eingestellt") else "unbekannt"}</div>',
        f'<div style="font-size:13px;color:{GRAU};padding-bottom:10px">'
        f'{html.escape(_verkaeufer_zeile(deal.get("verkaeufer", {})))}</div>',
    ]
    if deal.get("begruendung"):
        zeilen.append(f'<div style="font-size:14px;padding-bottom:6px">'
                      f'<b>Warum das ein Fund ist:</b> {html.escape(deal["begruendung"])}</div>')
    if deal.get("risiko"):
        zeilen.append(f'<div style="font-size:14px;padding-bottom:6px">'
                      f'<b>Risiko:</b> {html.escape(deal["risiko"])}</div>')
    if deal.get("empfehlung"):
        zeilen.append(f'<div style="font-size:14px">'
                      f'<b>Vorgehen:</b> {html.escape(deal["empfehlung"])}</div>')

    return f"""
    <table width="100%" cellpadding="0" cellspacing="0" role="presentation"
           style="border:1px solid {RAHMEN};border-radius:6px;margin-bottom:18px">
      <tr><td style="padding:18px">
        <table width="100%" cellpadding="0" cellspacing="0" role="presentation"><tr>
          {bildzelle}
          <td valign="top">
            <div style="font-size:17px;font-weight:bold;line-height:1.3">
              <a href="{html.escape(deal["url"])}" style="color:{NAVY};text-decoration:none">
                {html.escape(deal["titel"])}</a>{marke}
            </div>
            <div style="font-size:22px;font-weight:bold;color:{NAVY};padding-top:8px">
              {_euro(deal.get("preis"))}</div>
            {ersparnis}
            <div style="padding-top:12px">{"".join(zeilen)}</div>
          </td>
        </tr></table>
      </td></tr>
    </table>"""


def rendern(daten: dict) -> str:
    deals = daten.get("deals", [])
    zeitraum = daten.get("zeitraum", {})
    anzahl = len(deals)
    wort = "Fund" if anzahl == 1 else "Funde"

    return f"""<table width="100%" cellpadding="0" cellspacing="0" role="presentation"
       style="background:#f6f7f9;padding:24px 12px">
<tr><td align="center">
<table width="640" cellpadding="0" cellspacing="0" role="presentation"
       style="max-width:640px;background:#ffffff;border-radius:8px;padding:28px;
              font-family:Arial,Helvetica,sans-serif;color:#1a1f28">
  <tr><td>
    <div style="font-size:26px;font-weight:bold;color:{NAVY}">
      Kleinanzeigen Schnäppchen, {_datum_lang(daten["generiert"])}</div>
    <div style="border-top:3px solid {ROT};margin:12px 0 14px"></div>
    <div style="font-size:13px;color:{GRAU};padding-bottom:4px">
      Zeitraum: {_datum_zeit(zeitraum.get("von", daten["generiert"]))} bis
      {_datum_zeit(zeitraum.get("bis", daten["generiert"]))}</div>
    <div style="font-size:15px;padding-bottom:20px">
      <b>{anzahl} {wort}</b> aus {_zahl(daten.get("gesichtet", 0))} gesichteten Anzeigen.
    </div>
    {"".join(_karte(d) for d in deals)}
    <div style="font-size:12px;color:{GRAU};border-top:1px solid {RAHMEN};
                padding-top:14px;margin-top:6px">
      Preisvergleich gegen den Median gleichartiger Anzeigen auf Kleinanzeigen.
      Verkäuferangaben stammen aus der Plattform und sind kein Echtheitsnachweis:
      Das höchste Zuverlässigkeits-Abzeichen braucht sechs Bewertungen, und
      bewerten darf man sich ohne Kauf. Vor Ort prüfen, bar bei Abholung zahlen.
    </div>
  </td></tr>
</table>
</td></tr></table>"""


def main() -> int:
    daten = json.loads(DEALS.read_text(encoding="utf-8"))
    AUSGABE.write_text(rendern(daten), encoding="utf-8")
    print(f"{len(daten.get('deals', []))} Funde nach {AUSGABE.name} geschrieben")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
