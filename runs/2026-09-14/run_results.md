# Lauf 2026-09-14, 19:06 Uhr (abends) — abgebrochen, veraltete Datenbasis

**Ergebnis: keine Prüfung, keine Funde, keine Mail.** Abbruch nach Schritt 1 der
Anweisung, weil `candidates.json` zu alt ist.

## Befund

- `candidates.json` generiert: `2026-09-14T12:28:17+02:00`
- Laufzeitpunkt der Routine: `2026-09-14T19:06+02:00`
- Alter der Datei: **6,6 Stunden** — die Grenze in `prompt.md` Schritt 1 liegt bei
  vier Stunden, die Kurzfassung des Auftrags nennt sechs. Beide sind überschritten.
- Zeitraum des letzten Sammellaufs: `2026-09-14T06:22:40+02:00` bis `2026-09-14T11:22:40+02:00`
- Kandidaten in der Warteschlange: **178**, davon 0 bereits in `deal_log.csv`

Die Liste ist also nicht leer, sondern schlicht nicht aktuell: Alles, was seit
11:22 Uhr eingestellt wurde, fehlt. Genau dafür ist die Frist da, und deshalb wurde
kein Kandidat inhaltlich geprüft.

## Ursache: ausgefallene Sammelläufe

`.github/workflows/scan.yml` läuft per Cron alle vier Stunden (00, 04, 08, 12, 16 UTC).
Der letzte erfolgreiche Lauf ist Run #223, gestartet 09:22 UTC, beendet 10:28 UTC — das
war der 08-UTC-Takt mit 82 Minuten Verspätung. Für 12 UTC und 16 UTC wurde bis 17:06 UTC
**kein Workflow-Run angelegt**, auch keiner mit Fehlschlag. Die geplanten Läufe sind
nicht fehlgeschlagen, sie wurden von GitHub gar nicht erst gestartet.

Dasselbe Muster zeigen die letzten Tage: statt sechs Läufen pro Tag kommen vier bis
fünf an, jeweils ein bis zwei Stunden verspätet. Bei einem Abendlauf um 19:00 Uhr
Ortszeit trifft eine ausgefallene 12-UTC-Runde die Routine direkt.

## Ausgefallene Stufe-2-Läufe

Der letzte durchgeführte Urteilslauf ist der Morgenlauf vom **2026-09-13**
(Commit `aca4db4`, ein gemeldeter Fund). Der Abendlauf vom 13., der Morgenlauf vom 14.
und nun dieser Abendlauf sind ohne Meldung geblieben — die ersten beiden ohne Eintrag
im Laufprotokoll, also vermutlich gar nicht gestartet. Die Warteschlange wächst
entsprechend: 175 Kandidaten am 13. morgens, 178 jetzt.

## Warteschlange zum Zeitpunkt des Abbruchs

Ungeprüft, nur zur Einordnung, sortiert nach dem Kleinanzeigen-Median (der laut
Anweisung kein Beleg ist):

| Anzeige | Preis | Median-Abstand | Referenz belastbar |
|---|---|---|---|
| Porsche 944 Oldtimer | 8.900 € | 6.355 € | ja (Streuung 1,90) |
| Mercedes S-Klasse W126 300 SE | 5.980 € | 5.630 € | ja (2,00) |
| BMW E36 328i Cabrio | 5.500 € | 5.390 € | ja (1,71) |
| Mercedes W126 420 SEL | 5.950 € | 5.300 € | **nein** (3,09) |
| BMW 320i E36 Oldtimer | 4.200 € | 4.799 € | ja (1,88) |
| Gibson Les Paul Standard 1959 Reissue Custom Shop VOS | 4.399 € | 3.600 € | ja (1,68) |
| Rolex Explorer II | 6.100 € | 3.100 € | ja (1,25) |

Diese Kandidaten bleiben in der Warteschlange und werden vom nächsten Lauf mit
frischen Daten geprüft; `deal_log.csv` wurde nicht angefasst, es geht nichts verloren.

## Committet

Nur diese Datei, nach `main`. `deals.json`, `email_output.html` und `deal_log.csv`
bleiben unverändert, damit kein Versand ausgelöst wird.
