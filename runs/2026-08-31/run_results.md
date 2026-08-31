# Lauf 2026-08-31, 07:10 Uhr (morgens)

- `candidates.json` generiert: 2026-08-31T04:35:09+02:00 (rund 2,5 Stunden alt, innerhalb der Vier-Stunden-Grenze)
- Zeitraum: 2026-08-30T23:20:07+02:00 bis 2026-08-31T04:20:07+02:00
- Gesichtet: 24.382 Anzeigen, 166 Kandidaten in der Liste
- Bereits in `deal_log.csv`: 0 Kandidaten
- Geprüft: 166 Kandidaten gesichtet, davon 31 inhaltlich geprüft (nach absoluter Ersparnis und Liquidität sortiert), 3 gemeldet

## Gemeldete Funde

| Preis | Titel | Bestätigter Marktwert | Abstand | Ort |
|---|---|---|---|---|
| 7.900 € | Mercedes W124 300 CE 24V Automatik, EZ 5/1991, TÜV 9/2027 | Median 12.581 €, mittlerer Bereich 9.500–15.990 € (12gebrauchtwagen.de, C124-Coupé, 83 Angebote, Stand 30.08.2026) | rund 37 % | Hürth |
| 7.000 € | Mercedes 300 SL R129, 2/1991, 190.000 km, H-Zulassung, TÜV 10/2027 | 14.900 € (1992, 252.000 km) und 21.449 € (1991, 122.000 km), günstigstes Gesamtangebot ab 9.500 € | rund 53 % gegen das schlechtere Vergleichsfahrzeug | Schwalmtal |
| 9.800 € | BMW 320i E30 Cabrio, 4/1993, 163.050 km, Oldtimergutachten | 14.700 € (123.700 km) und 15.000 € (317.000 km), realisiert 8–12 % darunter, also rund 13.000 € | rund 25 % | Öhningen |

Alle drei sind Klassiker ohne ausdrückliche Erwähnung der Zulassungsbescheinigung Teil II. Der Prüfpunkt steht bei jedem Fund in der Empfehlung.

## Verworfene Kandidaten

### Marktwert selbst geprüft, Abstand hält nicht

- **3499338994 Porsche 911 Carrera 996, 2002, 138.000 km, 35.900 €** – der Median von 57.330 € stammt aus der Suche „Porsche CARRERA 911“, also einem Markendurchschnitt über alle Baureihen, nicht der exakten Generation. Für den 996 Carrera Facelift nennt 911Finder Zustand 2 mit 24.000 bis 40.000 € (Stand Mai 2026). 35.900 € liegen mitten im Band, kein Abstand.
- **3498751694 MacBook Pro 14 Zoll M5, 16/512 GB, 1.350 €** – Apple Refurbished führt genau diese Konfiguration für 1.439 €, Neupreis 1.599 €. 1.350 € sind rund 6 % unter dem Refurbished-Preis. Der Median von 2.000 € mischte M5-Pro- und M5-Max-Konfigurationen ein.
- **3499276652 und 3498466158 DJI Mini 5 Pro, 500 € und 575 €** – die Mini 5 Pro kostet neu inzwischen 638,99 bis 799 € (Geizhals, billiger.de, August 2026). Der Kleinanzeigen-Median von 899 € bildet veraltete Angebotspreise ab, nicht den Markt. Kein Abstand von 20 Prozent zu einem Gebrauchtwert von rund 450 bis 550 €.
- **3499427355 Rolex Datejust 36 Ref. 16030, 1981, Full Set, 6.100 €** – Ref. 16030 handelt bei rund 4.500 bis 6.000 € (Chrono24: 4.916 $, 5.590 $, 6.100 $; eBay.de 5.603 € mit schwarzem Blatt). 6.100 € liegen am oberen Rand. Der Median von 13.000 € vermengte die moderne Datejust 41 mit der Vintage-Referenz.
- **3499053414 Rolex Datejust 41 ungetragen 2/2024, Full Set, 9.550 €** – vergleichbare ungetragene 126300 mit Jubilee stehen bei 11.300 € und 11.453 € (Chrono24). 9.550 € sind rund 16 Prozent darunter, also ein fairer Privatpreis, aber unter der Schwelle.
- **3499376072 Gibson Les Paul Standard 2012, 1.710 €** – `referenz.streuung` 6,8 und `belastbar: false`, der Median von 3.520 € zählt nicht. Eigene Einordnung des Marktes für eine 2012er Standard: rund 1.900 bis 2.500 €, kein Abstand von 20 Prozent. Zudem gewerblicher Händlerpreis, also selbst der Markt.
- **3499414146 Riese & Müller Charger GT, Baujahr 2023, 12.000 km, 1.900 €** – Upway und Rebike verkaufen aufgearbeitete Charger3 GT touring im Bereich um 2.200 bis 2.800 €, bei 12.000 km Laufleistung und gealtertem Akku ist 1.900 € privat ein normaler Preis. Zusätzlich: nur Versand, keine Abholung für ein E-Bike dieser Klasse.

### Preis erklärt sich von selbst

- **3499282742 BMW e30 318i Coupé, 5.300 €** – kein TÜV, Motor läuft unrund (Verdacht Benzindruckregler), Rost vorhanden, 268.564 km. Projektfahrzeug, korrekt bepreist.
- **3498830887 Mercedes W124 300E, 5.000 €** – Attribut „Beschädigtes Fahrzeug“, 367.000 km, TÜV abgelaufen, Tempomat und Standheizung ohne Funktion, Automatik schaltet ruppig.
- **3498783625 Mercedes w126 300se, 5.000 €** – 490.000 km. Ehrliche, sehr gute Anzeige, aber die Laufleistung erklärt den Preis vollständig.
- **3498415724 Simson Star mit Vape Zündung, 1.500 €** (`unkenntnis_bonus: true`) – „ohne Motor“. Der Median von 3.051 € gilt für vollständige Fahrzeuge. Der Bonus wurde nicht gegen die Anzeigenqualität gewertet, sondern der fehlende Motor gegen den Referenzgegenstand.
- **3499095563 Hanomag Scheunenfund C224, 900 €** – ausdrücklich als Teileträger und Projekt angeboten.
- **3499220854 DJI Mavic 3 Pro, 730 €** – „Defekt nach Absturz“, wird als Ersatzteilspender verkauft.
- **3499220196 MacBook Air M3, 330 €** – Zustand „Defekt“, Tastatur, Touchpad und Akku ohne Funktion.
- **3498916270 DJI Mini 3 Pro, 280 €** – Gimbal-/Pitch-Motor defekt.
- **3498525579 Schlauchboot 320, 500 €** – ohne Motor, „leicht reparaturbedürftig“.

### Zahlung außerhalb der Plattform verlangt

- **3499371954 PlayStation 5 Pro 2 TB, 455 €** – „nur PayPal Freunde oder Barzahlung“, Käuferschutz wird ausdrücklich abgelehnt. Zusammen mit 44 Prozent des Marktwerts das Standardmuster.
- **3499507031 PlayStation 5 Pro, 499 €** – gleiches Muster, „Kein Verkauf hier über das System oder über PayPal Waren“.
- **3498541724 Truma Aventa Compact, neu und originalverpackt, 745 €** – „Versand und PayPal FF bitte! Alles andere funktioniert bei mir nicht.“ Neuware weit unter Marktwert plus erzwungene Zahlung ohne Käuferschutz.

### Referenzgruppe nicht belastbar und kein eigener Beleg gefunden

- **3499460347 Rolex date just, 6.000 €** – `streuung` 3,07, `belastbar: false`. Zusätzlich inhaltlich unstimmig: „Referenznummer: 0684“ ist keine Rolex-Referenz, Diamantlünette und Perlmuttblatt ohne Papierbeleg, ausschließlich Versand, keine Abholung.
- **3499469901 Leica M9-P silber, 4.500 €** – kein Kleinanzeigen-Median vorhanden. Die Anzeige enthält nach eigener Angabe nur Symbolfotos, also keine Bilder des tatsächlichen Objekts. Ohne Bild der konkreten Kamera, ohne Seriennummer und ohne Auslösezahl ist kein belastbares Urteil möglich.
- **3499349304 USM Haller Sideboard, sechs Fächer, 102 × 37,5 × 109,5 cm, 990 €** – vermutlich deutlich unter Markt, aber für genau diese Konfiguration ließen sich keine zwei konkreten Vergleichsangebote finden, nur allgemeine Händlerspannen. Kein bestätigter Marktwert, daher nicht gemeldet.
- **3499515419 Riese & Müller UBN Five touring, 2023, 2.000 km, 1.700 €** – Vergleichsangebote vorhanden (Rebike 2.639 € und 2.689 €, Upway ab 2.049 €), der Abstand wäre ausreichend. Verworfen wegen des Anzeigentexts: Akku, Rahmengröße, Farbe und Laufleistung stehen in Klammern wie unausgefüllte Platzhalter einer Vorlage, das Konto ist ohne Bewertung. Textbaustein-Verdacht wiegt hier schwerer als der rechnerische Abstand.
- **3498773355 MacBook Pro M1 Max 64 GB, 1.200 €** – Beschreibung besteht aus vier Wörtern, Bildschirmgröße nicht genannt, Attribut nennt widersprüchlich „Intel Core i7“. Konfiguration nicht bestimmbar, damit kein Marktwert zuzuordnen.
- **3499411269 Geschäftsauflösung Restposten, 3.000 €** und **3498871060 Haushaltsauflösung, 500 €** – `streuung` 3,45 und 15,43, `belastbar: false`. Konvolute ohne bestimmbaren Einzelwert.
- **3498797347 Jaeger-LeCoultre Atmos Vendome, 2.250 €** – `streuung` 3,5, `belastbar: false`. Vier Bilder, Konto drei Monate alt, kein eigener Beleg für ein Preisniveau über 2.800 € gefunden.
- **USM-Haller- und Design-Posten gewerblicher Anbieter** (3370101211, 3370101545, 3370182294, 3397577403, 3397648899, 3423670628, 3022326483) – Händler mit aufgearbeiteter Ware. Deren Preis ist der Markt, nicht der Abstand zum Markt.

### Sonstige

- **3498689389 TAG Heuer Carrera Calibre 16, 1.499 €** – gewerblicher Anbieter mit Werkstattaufbereitung und Gewährleistung, Händlerpreis.
- **3499139289 TAG Heuer Autavia, 2.450 €** – Median 3.650 €, Abstand 33 Prozent laut Median, aber `p25` liegt bei 2.490 €. Der Autavia-Markt liegt real bei rund 2.300 bis 2.900 €, damit kein Abstand.
- Restliche Kandidaten (Simson-Teile, Cube- und Canyon-Räder, iPhones der Reihen 12 bis 15, Meissen- und KPM-Porzellan, Kleinwerkzeug) mit Ersparnissen unter 500 € nicht einzeln geprüft: nach zehn bestätigten Funden wäre ohnehin Schluss, und die Reihenfolge nach absoluter Ersparnis und Liquidität hat sie nach hinten gestellt.

---

# Lauf 2026-08-31, 19:05 Uhr (abends)

- Start des Laufs: 31. August 2026, 19:04 Uhr (MESZ)
- `candidates.json` beim Start: generiert 2026-08-31T13:31:48+02:00, **5 Stunden 33 Minuten alt**. Nach prompt.md Schritt 1 (Frist vier Stunden) waere das ein Abbruch gewesen.
- Stattdessen Sammler per `workflow_dispatch` angestossen (Lauf 154, `stunden=7`, 17:06 bis 19:03 UTC). Geurteilt wurde auf `candidates.json` generiert 2026-08-31T21:03:44+02:00, beim Lesen **eine Minute alt**.
- Zeitraum des massgeblichen Scans: 2026-08-31T12:06:18+02:00 bis 2026-08-31T19:06:18+02:00
- Gesichtet: 252.115 Anzeigen, Pool 249.640
- Kandidaten in `candidates.json`: 149, davon 0 bereits in `deal_log.csv`
- Geprueft: 189 Kandidaten gesichtet (166 aus dem 13:31-Stand, 40 neu im 21:03-Stand, Ueberschneidung abgezogen), davon 41 einzeln recherchiert
- Gemeldete Funde: 1

## Warum der Sammler angestossen wurde

Der GitHub-Scheduler hat am 31.08. fuer die Cron-Zeitpunkte 12:00 und 16:00 UTC
**keinen Lauf von `scan.yml` angelegt**. Der letzte planmaessige Lauf (153) startete
um 10:15 UTC und committete um 11:31 UTC. Workflow aktiv, letzte Laeufe erfolgreich,
nichts in der Warteschlange. Anders als am 29. und 30.08. lief also auch kein
Sammler, auf den man haette warten koennen; der naechste Takt waere 20:00 UTC
gewesen, drei Stunden nach dem Meldezeitpunkt.

Das Fenster wurde auf sieben statt fuenf Stunden gesetzt, damit zwischen dem Ende
des 11:31-Scans (10:15 UTC) und jetzt keine Luecke bleibt. Laufzeit dadurch
7.047 Sekunden statt der ueblichen rund 4.600.

**Das ist der fuenfte Tag in Folge mit demselben Befund** (27., 28., 29., 30., 31.08.).
Er wurde bisher nur in Commit-Nachrichten festgehalten. Empfehlung unveraendert:
entweder Cron auf 05:00 und 17:00 UTC legen, oder die Frist in prompt.md auf sechs
Stunden anheben, wie sie der Aufruftext der Routine ohnehin nennt. Solange beides
nicht passiert, muss jeder Lauf den Sammler selbst anstossen und rund zwei Stunden
warten.

## Gemeldeter Fund

| Preis | Titel | Bestaetigter Marktwert | Abstand | Ort |
|---|---|---|---|---|
| 1.100 € | Tag Heuer Carrera 41mm, Ref. WBN2012.BA0640, blaues Blatt | 1.844 € (Chrono24, dieselbe Referenz), weitere derselben Referenz 2.843 und 2.869 USD; gut erhaltene Gebrauchte allgemein rund 2.020 USD | rund 30 % nach Abzug fuer fehlende Papiere | Titisee-Neustadt |

Verkaeuferprofil: Konto seit 2014, Bewertung 1,00. Die Anzeige nennt die exakte
Referenz, legt das Fehlen von OVP und Unterlagen offen, verweigert Versand
ausdruecklich ("Kein Versand nur Selbstabholer!") und bietet Besichtigung und
Pruefung vor Ort an. Das ist das Gegenteil des Betrugsmusters aus der Leitidee.

**Anmerkung zur Herkunft des Fundes:** Die Anzeige stand im 13:31-Stand von
`candidates.json`, auf dem dieser Lauf begonnen hat, und wurde dort vollstaendig
geprueft. Im 21:03-Stand ist sie nicht mehr enthalten: `_zusammenfuehren` verwirft
Kandidaten, deren Feld `eingestellt` aelter ist als 24 Stunden vor dem Fensterende.
Die Anzeige stammt vom 30.08. um 13:17 Uhr, die Grenze lag bei 30.08. um 19:06 Uhr.
Sie ist also nicht aus dem Angebot verschwunden, sondern aus der Warteschlange
gefallen, und zwar genau in den zwei Stunden, die das Nachstossen des Sammlers
gekostet hat. Gemeldet wird sie trotzdem, weil sie regulaerer Kandidat dieses
Laufs war und die Pruefung nach a) bis e) bestanden hat.

## Verworfene Kandidaten

### Marktwert selbst geprueft, Abstand haelt nicht

- **3499877336 Leica Apo-Summicron-M 2/90 ASPH, 1.750 €** – gebrauchte Exemplare stehen bei 1.906 € (non-6bit) und 2.147 € (6bit) auf eBay.de, neu 5.090 €. 1.750 € liegen nur 8 bis 19 Prozent darunter. Der Median von 2.749,50 € war zu hoch angesetzt. Ansonsten eine vorbildliche Anzeige: Konto seit 2014, Bewertung 1,00, Seriennummer genannt, Kaeuferschutz.
- **3499846633 Leica Summilux-M 35/1.4 ASPH 11874 6bit, 2.899 €** – MPB fuehrt dieselbe Referenz gebraucht bei 2.249 bis 2.429 USD, also rund 2.070 bis 2.235 €. Das Angebot liegt **ueber** dem Marktwert. Zudem autorisierter Leica-Haendler mit 12 Monaten Garantie: dessen Preis ist der Markt.
- **3499643179 Jaeger-LeCoultre Master Compressor Diving GMT Titan, Ref. 160.T.05, 4.997 €** – guenstigstes Vergleichsangebot derselben Referenz 5.765 € aus Deutschland, weitere bei 6.629 und 8.888 USD. Die Anzeige nennt ehrlich "Kratzer und kleine Dellen". Kein Abstand von 20 Prozent.
- **3499645368 MacBook Pro 14 M3, 8 GB / 1 TB, 980 €** – Back Market fuehrt genau diese Konfiguration im Zustand "gut" bei 999 USD, rund 920 €. Damit ist der Abstand weg. Refurbished-Haendlerpreis 1.549 € ist nicht der Vergleichsmassstab.
- **3498746516 ausgenommen, alle uebrigen Uhren-Kandidaten geprueft:** 3499605016 ROLEX Oyster Perpetual Date 34 mm 3.211 €, 3499549974 Rolex Datejust 36 mm 5.500 €, 3499599336 Rolex Submariner 8.000 € – siehe naechster Abschnitt.
- **3500067860 Omega Seamaster Diver 300M Quartz, Ref. 2541.80, Baujahr 1995, 2.350 €** – gewerblicher Haendler (TyrolChrono). Der Median von 4.490 € mischt die moderne Automatik-Seamaster ein; eine Quarz-Seamaster von 1995 liegt bei rund 1.800 bis 2.600 €. Haendlerpreis, also selbst der Markt.
- **2917414181 ROLEX Datejust Ref. 1601, 5.450 €** – gewerblicher Haendler, und das Zifferblatt ist ausdruecklich ein Aftermarket-Diamantblatt, "nicht original Rolex". Wertmindernder Umbau, damit kein zu niedriger Preis.
- **3499666523 MacBook Pro 14 M4 Pro, 24 GB / 512 GB, 1.100 €** – Marktwert bestaetigt (eBay 1.649 €, Allzeittief neu 1.799 €), der Abstand von rund 33 Prozent waere da. Verworfen wegen des Profils: exakte Modellangabe, kein einziger Mangel genannt, ausschliesslich Versand, Konto ohne jede Bewertung, dazu ein Widerspruch zwischen Attribut "Grau" und Text "Space Schwarz". Das ist Punkt fuer Punkt das Betrugsmuster aus der Leitidee, nicht das Muster eines Verkaeufers, der den Wert nicht kennt.
- **3499636068 Vitra EA 104 Aluminium Chair, 849 €** – fuer genau diese Ausfuehrung liessen sich keine zwei konkreten Vergleichsangebote finden, nur ein Neupreis von 2.595 € und gebrauchte EA 108 zwischen 650 und 899 €. Kein bestaetigter Marktwert, daher nicht gemeldet.
- **3499560740 USM Haller Rollcontainer 550 €, 3498774542 USM Haller Sideboard olivgruen 450 €, 3499373693 USM Haller Regal weiss 450 €** – die Mediane von 900 bis 1.560 € stammen aus Suchen, die geschlossene Sideboards mit Klappen einschliessen. Ein gebrauchtes offenes USM-Haller-Regal mit zwei Faechern wird vom Haendler fuer rund 490 € brutto angeboten. Die drei Angebote liegen am Markt, nicht darunter.
- **3499694892 Omega Constellation Day-Date Vintage, 690 €** – vorbildlich ehrliche Anzeige (Verkaeufer legt offen, dass er kein Uhrmacher ist, Referenz und Kaliber nicht geprueft, keine Aussage zur Dichtigkeit). Ohne bestimmbare Referenz laesst sich aber kein belastbarer Marktwert zuordnen.
- **3499411904 Omega Seamaster vergoldet, Kal. 501, 34 mm, 900 €** – `p25` liegt bei 790 €, das Angebot damit am oberen Rand des Vergleichsfelds. Zusaetzlich Konto erst seit Mai 2026, nur Versand.
- **3499177392 MacBook Air 13 M1, 16/256 GB, 530 €** und **3499447307 iPhone 15 256 GB, 390 €** – Abstand unter 20 Prozent; beim iPhone erklaert die Akkukapazitaet von 77 Prozent den Rest.
- **3500094983 BMC Urs 01 Three Ekar, 2.250 €** – `p25` bei 1.900 €, der Median von 3.699 € bildet Neupreise ab. Kein bestaetigter Abstand.
- **3499784425 Verner Panton Chair, 250 €** und **3499869908 Fritz Hansen Oxford, 450 €** – ersterer am Markt, letzterer von einem gewerblichen Anbieter mit fuenf Stueck.

### Preis erklaert sich von selbst

- **3500152370 Tesla Model 3, 13.800 €** – Attribut "Beschaedigtes Fahrzeug", 205.000 km, Fehlermeldung **BMS a079** und Restreichweite 280 km. Nach der Pflicht-Warnflagge aus prompt.md liegt die Akkugarantiegrenze fuer Model 3 mit Heckantrieb bei 160.000 km; die ist um 45.000 km ueberschritten, ein BMS-Fehler faellt damit vollstaendig auf den Kaeufer. Der Preis ist richtig, nicht zu niedrig.
- **3500015597 BMW E36 328i Cabrio, 7.000 €** – Unfall waehrend der Besitzzeit, 249.948 km, Euro 2, Verdeck schliesst nur mit Nachhelfen.
- **3500041137 Mercedes W124 200, 2.000 €** – TÜV laeuft in diesem Monat ab, Schweissarbeiten an der Wagenheberaufnahme noetig, 258.947 km. Ehrliche Anzeige, aber der Preis stimmt.
- **3500071703 Mercedes 190E W201, 4.250 €** – gewerblich, 228.200 km, Beschreibung besteht aus einer Zeile.
- **3499878122 MacBook Air M3 2024, 499 €** – "Display defekt".
- **3499848217 MacBook Pro 16 M1 Pro, 499 €** – Zustand "Defekt", Streifen und Fleck im Panel.
- **3499357525 iPhone 15 Pro 300 €, 3499705726 iPhone 15 220 €, 3499715064 iPhone 14 Pro 250 €, 3499512975 iPhone 15 219 €, 3499396138 iPhone 15 190 €, 3499718550 iPhone 14 Pro Max 300 €** – der Reihe nach: deutliche optische Maengel, "alles defekt", Wasserschaden mit FaceID-Ausfall, Ersatzteiltraeger, Display vorne und hinten beschaedigt, Riss und getauschte Kamera.
- **3500031923 Revox B795, 400 €** – der Verkaeufer schreibt selbst, er wisse nicht, ob das Geraet funktioniert.
- **3499755347 Truma Aventa comfort, 900 €** – `p25` liegt exakt bei 900 €.

### Referenzgruppe nicht vergleichbar

- **3499556245 DJI Mini 4 Pro Fly More Zubehoer, 250 €** – verkauft wird **nur das Zubehoerset**: Tasche, drei Akkus, Ladestation, Propeller. Der Median von 680 € gilt fuer vollstaendige Drohnen. Reine Phantomersparnis.
- **3499699119 DJI Mavic Pro Fly More, 280 €** – die Referenzsuche lautet "DJI Mavic Pro 2" und zieht die deutlich teurere Mavic 2 Pro herein. Die urspruengliche Mavic Pro von 2016 liegt bei rund 250 bis 350 €.
- **3499565188 DJI Mini 4 Pro, 390 €** – "mit Wasserschaden (defekt)" steht im Titel.
- **3499869350 Rolex Lady Datejust 6917, 2.590 €**, **3500063088 Glashuette Senator 3.850 €**, **3500081929 Omega Speedmaster Ref. 3520.50.00 2.850 €**, **3500168472 Omega Constellation 1.050 €** – alle mit `belastbar: false` und Streuung zwischen 2,57 und 3,47. Bei keinem liess sich aus der Anzeige eine Referenz herleiten, die einen eigenen Marktwert getragen haette; die Speedmaster Reduced 3520.50.00 liegt mit Box und Karte bei rund 2.000 bis 3.000 € und damit am Angebotspreis.

### Erfundene Referenznummern: ein wiederkehrendes Muster bei Uhren

Drei Uhren-Anzeigen dieses Laufs tragen Referenznummern, die es bei den
angegebenen Marken nicht gibt. Das ist kein Zufall, sondern eine Vorlage:

- **3499549974 "Rolex Datejust 36 mm", 5.500 €, Ulm** – "Referenznummer: 0684". Dieselbe erfundene Nummer stand in **3499460347 "Rolex date just", 6.000 €**, die der Morgenlauf verworfen hat. Zeichengleiches Textgeruest, beide nur Versand, keine Abholung, Bewertung 0,50.
- **3499605016 "ROLEX oyster Perpetual Date 34mm", 3.211 €, Hamm** – "Referenznummer: 902-B 0381". Konto 91 Tage alt, Beschreibung im Werbetexter-Ton ("exquisites Sammlerstueck", "analoges Anzeigeformat"), nur Versand.
- **3499599336 "Rolex Submariner", 8.000 €, Bochum** – die Beschreibung gibt den Gehaeusedurchmesser mit **30 mm** an. Keine Submariner hat je 30 mm gehabt (40 bzw. 41 mm). Dazu "Glidelock" in einem Text, der sonst eine Datumslupe und ein Automatikwerk generisch aufzaehlt, Konto ohne Bewertung, nur Abholung, kein Kaeuferschutz.

Empfehlung fuer Stufe 1: eine Plausibilitaetspruefung der im Text genannten
Referenznummern gegen die bekannten Rolex-Referenzformate wuerde diese Gruppe
schon vor dem Scoring aussortieren.

### Modelljahr passt nicht zur Baureihe

- **3495882620 Omega Speedmaster Professional "Chocolate", 3.700 €** – die einzige Speedmaster Professional in Stahl mit Schokoladenblatt ist Ref. 311.30.42.30.13.001, gebaut **2007 bis 2013**, urspruenglich fuer den japanischen Markt. Die Anzeige schreibt "Die Uhr ist aus 2021". Gebrauchte dieser Referenz stehen bei 5.009 bis 7.600 USD, ein Full Set bei 6.000 USD; der Abstand waere also da. Solange aber offen ist, welche Uhr tatsaechlich verkauft wird, gibt es keinen bestaetigten Marktwert. Der Verkaeufer nennt sie selbst "selten", kennt den Wert also, und preist trotzdem 30 Prozent darunter: das spricht gegen Unkenntnis und fuer eine ungeklaerte Anzeige.

### Sonstige

- Restliche Kandidaten (Simson S51 und Schwalbe, Cube-, Canyon-, Specialized- und BMC-Raeder, Gibson Les Paul, iPhones der Reihen 12 bis 14, Konvolute und Haushaltsaufloesungen, USM- und Design-Posten gewerblicher Anbieter) nicht einzeln geprueft: nach absoluter Ersparnis und Liquiditaet stehen sie hinten, und die im Morgenlauf bereits namentlich verworfenen Kandidaten wurden nicht erneut aufgerollt.
