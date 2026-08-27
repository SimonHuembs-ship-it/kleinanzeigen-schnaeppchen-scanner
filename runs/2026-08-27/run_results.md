# Laufprotokoll 2026-08-27, Morgenlauf — ABGEBROCHEN (veraltete Daten)

**Lauf:** 27. August 2026, 07:05 Uhr (MESZ)
**candidates.json generiert:** 2026-08-27T00:54:09+02:00
**Alter zum Laufzeitpunkt:** 6 Stunden 11 Minuten
**Frist nach prompt.md Schritt 1:** 4 Stunden
**Ergebnis:** Abbruch vor der inhaltlichen Pruefung. Keine Kandidaten geprueft,
keine Funde gemeldet.

## Befund

Die Datenlage ist zu alt. `prompt.md` Schritt 1 verlangt den Abbruch, wenn das
Feld `generiert` aelter als vier Stunden ist. Es ist 6,2 Stunden alt.

Ursache ist nicht ein fehlgeschlagener Sammler-Lauf, sondern ein ausgefallener
Taktgeber: GitHub hat fuer die geplanten Cron-Zeitpunkte **00:00 UTC und
04:00 UTC am 27. August gar keinen Workflow-Lauf angelegt**. In der Lauf-Liste
von `scan.yml` ist der juengste Eintrag Lauf 136 vom 26.08. 22:35 UTC
(abgeschlossen 22:54 UTC, Commit `9a9c838`). Danach folgt nichts mehr.

Geprueft und ausgeschlossen:

- Der Workflow ist nicht deaktiviert: `GET actions/workflows/scan.yml` liefert
  `"state": "active"`.
- Es liegt kein fehlgeschlagener oder abgebrochener Lauf vor. Die letzten
  Laeufe 129 bis 136 sind saemtlich `conclusion: success`.
- Es haengt kein Lauf in `queued` oder `in_progress`. Die
  `concurrency`-Sperre der Gruppe `scan` blockiert also nichts.
- Der letzte erfolgreiche Lauf hat sauber geschrieben: `runs/2026-08-27/scan.md`
  liegt vor, 22.936 gesichtete Anzeigen, 889 Requests, 1.135 Sekunden Laufzeit.

Das Muster passt zu einer verworfenen Cron-Ausloesung auf GitHub-Seite.
Geplante Workflows sind dort ausdruecklich "best effort" und werden bei Last
verzoegert oder ganz uebersprungen. Zwei uebersprungene Takte hintereinander
sind allerdings ungewoehnlich; sollte sich das wiederholen, ist der Takt von
`0 */4 * * *` nicht mehr verlaesslich genug fuer die 07:00-Meldung.

## Datenbestand, der ungeprueft bleibt

| Kennzahl | Wert |
|---|---|
| Kandidaten in candidates.json | 152 |
| davon bereits in deal_log.csv | 0 |
| ungeprueft liegen geblieben | 152 |
| aeltestes Inserat im Bestand | 2026-08-26T00:36:23+02:00 |
| juengstes Inserat im Bestand | 2026-08-27T00:23:43+02:00 |

Es geht nichts dauerhaft verloren: `candidates.json` sammelt die noch nicht
gemeldeten Kandidaten der letzten 24 Stunden an, und `deal_log.csv` wurde nicht
angefasst. Der naechste erfolgreiche Sammler-Lauf traegt diese 152 Kandidaten
also erneut ein, soweit ihre Inserate noch innerhalb des 24-Stunden-Fensters
liegen. Die aeltesten Eintraege vom 26.08. morgens fallen bis zum Abendlauf
allerdings aus dem Fenster, ohne je beurteilt worden zu sein.

## Verworfene Kandidaten

Entfaellt. Es wurde kein Kandidat inhaltlich geprueft, also wird auch keiner
mit Begruendung verworfen. Die 152 Eintraege bleiben unbeurteilt im Bestand.

## Was committet wird

Nach prompt.md Schritt 5 gilt der Fall "kein gemeldeter Fund": Nur dieses
Laufprotokoll geht nach `main`. `email_output.html`, `deals.json` und
`deal_log.csv` bleiben unveraendert, damit kein Versand ueber Resend ausgeloest
wird.

## Naechster Schritt

Der Abendlauf um 19:00 Uhr greift auf die dann aktuelle `candidates.json` zu.
Faengt der Sammler-Takt sich von selbst wieder, ist der Fall erledigt. Bleibt
`scan.yml` weiter stumm, hilft ein manueller Start ueber `workflow_dispatch`
mit `stunden: 12`, um die Luecke zu schliessen, bevor die aelteren Inserate aus
dem 24-Stunden-Fenster fallen.
