# Lauf 2026-09-21, abends — **abgebrochen, Daten zu alt**

- **Zeitpunkt:** 2026-09-21, 19:05 Uhr (17:05 UTC)
- **candidates.json generiert:** 2026-09-21T12:27:36+02:00 → **6,6 Stunden alt**
- **Grenze nach prompt.md Schritt 1:** vier Stunden (Kurzfassung der Routine: sechs Stunden) — **beide überschritten**
- **Zeitraum des letzten Scans:** 2026-09-21T06:25:08+02:00 bis 2026-09-21T11:25:08+02:00
- **Gesichtete Anzeigen im letzten Scan:** 139.652
- **Kandidaten in der Datei:** 166, davon 0 bereits in `deal_log.csv` → 166 ungemeldet
- **Inhaltlich geprüft:** 0 (Abbruch vor Schritt 2)
- **Gemeldete Funde:** 0

## Funde

Keine. `deals.json`, `email_output.html` und `deal_log.csv` bleiben unverändert,
`python -m scanner.report` wurde nicht ausgeführt, es wird keine Mail ausgelöst.

## Verworfene Kandidaten

Alle 166 Kandidaten wurden **ohne inhaltliche Einzelprüfung** zurückgestellt. Grund
für jeden einzelnen ist derselbe: Die Datenbasis war beim Start über der
Abbruchgrenze, damit ist nach prompt.md Schritt 1 kein Urteil zu fällen. Die
Kandidaten verfallen nicht — `candidates.json` sammelt ungemeldete Funde über
24 Stunden an, und `deal_log.csv` hat keinen von ihnen. Der nächste Lauf mit
frischen Daten sieht sie wieder, soweit sie dann noch im Fenster liegen.

## Befund: der Sammler hat nicht rechtzeitig geliefert

Kein Fehler im Scanner-Code. Alle 257 Läufe der Scan-Action sind auf
`conclusion: success`, der letzte hat um 10:27 UTC sauber committet. Das Problem
ist die Auslieferung des Cron-Triggers durch GitHub gegen die Laufzeit des Scans.

Cron steht auf `0 */4 * * *`, also 00, 04, 08, 12, 16 UTC. Tatsächlich am 21.09.:

| Slot (UTC) | Start | Verzug |
|---|---|---|
| 00:00 | 02:21 | +141 min |
| 04:00 | **nie gestartet** | — |
| 08:00 | 09:24 | +84 min |
| 12:00 | **nie gestartet** | — |
| 16:00 | um 17:03 noch nicht gestartet | — |

Zwei von fünf Slots sind ausgefallen, die übrigen liefen 1,5 bis 2,5 Stunden zu
spät. Ein Lauf braucht dazu 62 bis 90 Minuten (heute 3.748 Sekunden). Damit ist
zum Urteilszeitpunkt der Abendroutine der letzte *fertige* Scan strukturell sechs
bis sieben Stunden alt. Anders als am 17.09. lief diesmal auch kein Scan, auf den
sich hätte warten lassen: der 12-UTC-Slot ist ausgefallen, der 16-UTC-Slot war um
17:03 UTC weder gestartet noch in der Warteschlange.

Das ist keine neue Beobachtung. Das Protokoll vom 17.09. abends nennt denselben
Mechanismus, zählt die Abendabbrüche vom 14., 15. und 16. September auf und
empfiehlt, den Cron auf etwa `0 1,5,9,13,16 * * *` umzustellen oder den
16-UTC-Lauf auf 15:00 UTC vorzuziehen. Der Cron in `.github/workflows/scan.yml`
steht unverändert auf `0 */4 * * *`. **Die Empfehlung ist seit vier Tagen offen.**

## Zweiter Befund: die Routine hat seit dem 17.09. abends nichts protokolliert

Im Repo gibt es für den 18., 19., 20. und den Morgen des 21.09. **kein**
`run_results.md` — die Ordner `runs/2026-09-18` bis `runs/2026-09-21` enthalten
nur die `scan.md` des Sammlers. Auch `deal_log.csv` endet am 17.09., und
`email_output.html` wurde zuletzt am 17.09. um 17:26 UTC geändert.

Nach prompt.md Schritt 5 muss selbst ein Lauf mit null Funden sein Protokoll nach
`main` pushen. Dass vier Tage lang keines angekommen ist, heißt: entweder sind
rund sieben Routineläufe gar nicht gestartet, oder sie sind gestartet und haben
ihren Commit nicht abgesetzt. Von hier aus ist nicht unterscheidbar, welches von
beidem — die Protokolle, die es sagen könnten, sind genau die fehlenden. In
beiden Fällen ist es vier Tage lang still ausgefallen, ohne dass jemand
benachrichtigt wurde.

## Was in der Warteschlange liegt (ungeprüft, kein Urteil)

Nur zur Einordnung, ob ein manueller Nachlauf lohnt. Keine dieser Zahlen ist ein
bestätigter Marktwert, die Mediane sind ungeprüft:

- **166 ungemeldete Kandidaten**, 119 davon mit `belastbar: true` und Streuung ≤ 2,5
- Schwerpunkte: `apple-mobil` 31, `ebike-rad` 28, `design-sammeln` 27, `uhren` 16,
  `macbook` 16, `motorraeder` 10, `optik-drohnen` 8
- `unkenntnis_bonus`: **0 Kandidaten** — in diesem Bestand liegt kein Fall der
  Klasse, die prompt.md ausdrücklich nicht nach Anzeigenqualität abwerten will
- **Inseratsalter: 7,7 h jüngstes, 22,1 h Median, 31,0 h ältestes.** Das ist der
  eigentliche Schaden des Ausfalls: Selbst ein sofortiger Nachlauf urteilt über
  Ware, die im Median seit fast einem Tag öffentlich steht. Genau davor warnt
  prompt.md mit dem Fund vom 5. August, der bei der Meldung schon reserviert war.
- Größte nominale Lücke: „Porsche 911 Turbo Cabrio", 29.900 €, 33.055 € unter dem
  Median. Ein Blick in die Beschreibung zeigt, warum die Vorstufe kein Urteil
  ersetzt: „5. Zylinder beschädigt, nicht fahrbereit", 996 mit 230.000 km,
  eingestellt als beschädigtes Fahrzeug. Nach prompt.md Schritt 2a ein
  selbsterklärender Preis und damit kein Fund, unabhängig vom Median.

## Empfehlung an den Betreiber

1. **Cron der Scan-Action verschieben**, damit vor der Abendroutine ein fertiger
   Scan liegt: `0 1,5,9,13,16 * * *`, oder den 16-UTC-Lauf auf 15:00 UTC. Das ist
   die schon am 17.09. ausgesprochene und weiterhin offene Empfehlung.
2. **Ausgefallene Slots einkalkulieren.** GitHub verwirft Cron-Läufe unter Last,
   heute zwei von fünf. Ein engerer Takt oder ein zweiter Trigger kurz vor den
   Meldezeiten macht die Routine unabhängig von einem einzelnen Slot.
3. **Den viertägigen Protokollausfall klären**, bevor an den Schwellen gedreht
   wird. Ein Scanner, der vier Tage stillsteht, ohne es zu melden, ist das
   größere Problem als ein zu alter Datensatz.

Nicht getan: keine Daten nachgesammelt, kein `workflow_dispatch` ausgelöst, keine
Schwelle aufgeweicht, kein Marktwert geschätzt, nichts an `scan.yml` geändert.
