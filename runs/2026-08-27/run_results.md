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

---

# Laufprotokoll 2026-08-27, Abendlauf — ABGEBROCHEN (veraltete Daten)

**Lauf:** 27. August 2026, 19:06 Uhr (MESZ)
**candidates.json generiert:** 2026-08-27T08:08:29+02:00
**Alter zum Laufzeitpunkt:** 10 Stunden 57 Minuten
**Frist nach prompt.md Schritt 1:** 4 Stunden
**Ergebnis:** Abbruch vor der inhaltlichen Pruefung. Keine Kandidaten geprueft,
keine Funde gemeldet.

Damit ist der 27. August der erste Tag, an dem **beide** Meldungen ausfallen.

## Befund: der Sammler-Takt ist seit 05:45 UTC stumm

Der Morgenlauf hatte vermutet, GitHub habe fuer 00:00 und 04:00 UTC gar keinen
Lauf angelegt. Das war nur zur Haelfte richtig. Die Lauf-Liste von `scan.yml`
zeigt jetzt:

| Lauf | angelegt (UTC) | fertig (UTC) | Commit |
|---|---|---|---|
| 137 | 27.08. 05:45 | 27.08. 06:08 | `c8049fc` |
| 136 | 26.08. 22:35 | 26.08. 22:54 | `9a9c838` |
| 135 | 26.08. 16:41 | 26.08. 18:06 | `2484183` |
| 134 | 26.08. 12:30 | 26.08. 13:05 | `6b27262` |

Lauf 137 ist also doch noch gekommen, nur um 1 Stunde 45 verspaetet: das war
der 04:00-Takt. Danach ist nichts mehr passiert. Die Takte **08:00, 12:00 und
16:00 UTC haben keinen Lauf erzeugt**, obwohl inzwischen 17:06 UTC ist und die
uebliche Verspaetung bei 30 bis 45 Minuten liegt, im schlechtesten beobachteten
Fall bei 2 Stunden 40.

Erneut geprueft und ausgeschlossen:

- `scan.yml` ist aktiv, nicht deaktiviert.
- Kein Lauf ist fehlgeschlagen: die letzten 30 Laeufe sind saemtlich
  `conclusion: success`.
- Nichts haengt in `queued` oder `in_progress`, die `concurrency`-Sperre der
  Gruppe `scan` blockiert also nichts.
- Lauf 137 selbst hat sauber gearbeitet: 38.053 gesichtete Anzeigen,
  1.030 Requests, 1.373 Sekunden, `runs/2026-08-27-2/scan.md` liegt vor.

Drei uebersprungene Takte hintereinander nach einem stark verspaeteten sind
kein normales Cron-Rauschen mehr. `0 */4 * * *` traegt die 07:00- und
19:00-Meldung nicht mehr verlaesslich.

## Was der Ausfall kostet

| Kennzahl | Wert |
|---|---|
| Kandidaten in candidates.json | 156 |
| davon bereits in deal_log.csv | 0 |
| ungeprueft liegen geblieben | 156 |
| aeltestes Inserat im Bestand | 2026-08-26T08:04:20+02:00 |
| juengstes Inserat im Bestand | 2026-08-27T07:58:36+02:00 |
| davon aelter als rund 20 Stunden | 120 |

Die 120 aelteren Inserate fallen bis zum naechsten Sammler-Lauf aus dem
24-Stunden-Fenster und werden nie beurteilt. Unter ihnen stehen die derzeit
groessten rechnerischen Abstaende, unter anderem eine Rolex Datejust fuer
7.400 Euro (Median 12.200, `belastbar: true`, Streuung 1,38) und ein
MacBook Pro 16 M4 Pro fuer 1.500 Euro (Median 3.150, Streuung 1,59). Ob das
Funde gewesen waeren, ist offen: die eigene Marktwertbestaetigung nach
prompt.md Schritt 2 hat nicht stattgefunden, und ohne sie wird hier nichts
behauptet.

`deal_log.csv`, `deals.json` und `email_output.html` bleiben unangetastet.

## Nebenbefund: der Sammler loescht Laufprotokolle

Beim Nachsehen in der Historie ist aufgefallen, dass Commit `b297e8b`
("Scan 2026-08-25T17:45Z") die 95 Zeilen des **Abendprotokolls vom 25. August**
wieder aus `runs/2026-08-25/run_results.md` entfernt hat. Das Protokoll aus
Commit `e6297e0` existiert seitdem nicht mehr im Baum.

Die Ursache steht im Commit-Schritt von `scan.yml`. Der Sammler setzt mit
`git reset --soft origin/main` den HEAD vor und legt seinen eigenen Arbeitsbaum
darauf. Fuer `deal_log.csv`, `deals.json` und `email_output.html` holt er sich
danach ausdruecklich den aktuellen Stand zurueck:

    git checkout -q origin/main -- deal_log.csv deals.json email_output.html

`runs/` steht nicht in dieser Zeile. Hat die Routine waehrend eines laufenden
Scans ein Protokoll committet, kennt der aeltere Arbeitsbaum des Sammlers die
Datei nicht, und das anschliessende `git add -A` stellt ihre Loeschung mit ein.
Genau das ist am 25. August passiert: Lauf 129 wurde um 16:24 UTC ausgecheckt,
die Routine hat um 17:15 UTC committet, der Sammler um 17:45 UTC gepusht.

Heute ist nichts verloren gegangen, weil Lauf 137 nach dem Morgenprotokoll
ausgecheckt wurde und gerade kein Scan laeuft. Der Fehler ist trotzdem
dauerhaft und trifft jedes Protokoll, das in ein laufendes Scan-Fenster faellt.
Eine Aenderung an `scan.yml` liegt ausserhalb dessen, was diese Routine nach
prompt.md Schritt 5 committen darf, deshalb hier nur der Vorschlag:

    git checkout -q origin/main -- deal_log.csv deals.json email_output.html
    git checkout -q origin/main -- runs/ || true

Die zweite Zeile stellt fremde Protokolle wieder her und laesst das eigene,
noch unverfolgte `runs/<datum>-<n>/scan.md` unberuehrt, weil ein
Pfad-Checkout keine unverfolgten Dateien loescht.

## Verworfene Kandidaten

Entfaellt. Es wurde kein Kandidat inhaltlich geprueft, also wird auch keiner
mit Begruendung verworfen.

## Was committet wird

Fall "kein gemeldeter Fund" nach prompt.md Schritt 5: nur dieses Laufprotokoll
geht nach `main`. `email_output.html`, `deals.json` und `deal_log.csv` bleiben
unveraendert, damit kein Versand ueber Resend ausgeloest wird.

## Naechster Schritt

Der Takt repariert sich nicht von selbst, wenn er drei Mal hintereinander
ausfaellt. Zwei Dinge helfen, in dieser Reihenfolge:

1. `scan.yml` einmal ueber `workflow_dispatch` mit `stunden: 12` starten. Das
   fuellt `candidates.json` wieder auf, bevor der Morgenlauf um 07:00 danach
   greift. Der Lauf dauert 25 bis 90 Minuten.
2. Den Cron entzerren. `0 */4 * * *` liegt auf der vollen Stunde, wo GitHub
   die meisten geplanten Laeufe verwirft. Ein krummer Takt wie
   `17 1,5,9,13,17,21 * * *` wird erfahrungsgemaess seltener uebersprungen und
   legt den letzten Lauf naeher an die 07:00- und 19:00-Meldung.

Ich habe den Sammler nicht selbst angestossen: prompt.md schliesst
Nachsammeln aus, und ein Lauf um 19:00 Uhr waere bis zum Morgenlauf ohnehin
wieder 12 Stunden alt.
