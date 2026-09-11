# Lauf 2026-09-11, 07:05 Uhr (morgens)

- `candidates.json` generiert: 2026-09-11T04:19:47+02:00 (2 h 45 min alt, innerhalb der Vier-Stunden-Grenze aus prompt.md)
- Zeitraum des letzten Scans: 2026-09-10T23:03 bis 2026-09-11T04:03
- Gesichtet laut Statistik: 29.357 Anzeigen
- Kandidaten in der Datei: 172
- Bereits in `deal_log.csv`: 0 (alle 172 waren neu)
- Inhaltlich geprüft: 172 gesichtet, 48 im Detail geprüft (Priorität: größter absoluter Abstand, dann liquide Ware – Uhren, Drohnen, Apple, Konsolen; Grafikkarten waren nicht im Pool)
- **Gemeldete Funde: 2**

## Werkzeug-Einschränkung dieses Laufs

`WebFetch` war in dieser Umgebung durchgehend blockiert (`EGRESS_BLOCKED`, auch für
mpb.com, chrono24.de, classic-trader.com, buyzoxs.de). Direkte Aufrufe per `curl`
kamen ebenfalls nicht durch. Die externe Marktwertprüfung stützt sich deshalb
ausschließlich auf `WebSearch` und die dort zitierten Preisangaben. Mehrere sonst
knappe Kandidaten sind aus diesem Grund verworfen statt gemeldet worden – die
Bestätigung des Preisniveaus war nicht in der geforderten Qualität zu bekommen.

## Funde

| Preis | Titel | Bestätigter Marktwert | Abstand | Ort |
|---|---|---|---|---|
| 1.100 € | [DJI Mavic 3 Cine Combo mit 3 Akkus und Fernbedienung](https://www.kleinanzeigen.de/s-anzeige/dji-mavic-3-cine-combo-mit-3-akkus-und-fernbedienung/3509075813-245-6611) | ca. 1.700–1.800 € gebraucht (MPB: 7 Exemplare zu 1.839–1.919 USD; Kleinanzeigen-Median 1.800 € aus n=17, Streuung 1,35) | ca. 37 % darunter | Neuburg a.d. Donau |
| 350 € | [Ubiquiti UniFi USW-Pro-Max-48-PoE](https://www.kleinanzeigen.de/s-anzeige/ubiquiti-unifi-usw-pro-max-48-poe-top-zustand-48-port-poe/3509176488-168-9430) | neu ab 1.386,96 € (Amazon.de), generalüberholt 1.429 €, Händler-Gebraucht um 1.350 € | deutlich über 20 % auch bei hartem Gebrauchtabschlag | Hamburg Eimsbüttel |

Belege Mavic 3 Cine: Einführungspreis der Cine Premium Combo 4.799 € (11/2021); MPB
führt gebrauchte Cine Premium Combos zu 1.839–1.919 USD; deutsche Gebrauchthändler
(fotoprofi, buyZOXS) listen das Set zustandsbewertet. Verkäuferprofil: Konto seit
2013, Bewertung 100 %, nur Abholung (kein Versandvektor), C-Klassen-Kennzeichnung
erwähnt, Mängel offengelegt.

Belege Ubiquiti: `referenz.belastbar: false` (Streuung 2,71) – Median als nicht
vorhanden behandelt, deshalb `referenz_hinweis` statt `ersparnis_eur`. Neupreis
Amazon.de ab 1.386,96 €, refurbished 1.429 €, gebraucht bei Händlern um 1.350 €;
zum Vergleich kostet der kleinere Pro Max 24 PoE im offiziellen EU-Store 739 €.
Ein belastbarer *privater* Gebrauchtwert war nicht zu belegen – das steht so im
`referenz_hinweis` und im Risiko-Satz der Mail.

## Verworfene Kandidaten mit Begründung

### Uhren (alle verworfen)
- **Rolex Datejust 41 Full Set LC100, 7.450 €** (3509059911) – Chrono24 führt gebrauchte 126300-Full-Sets bei 7.999–8.490 €. Abstand rund 7–12 %, unter der 20-Prozent-Schwelle. Zusätzlich: Beschreibung besteht aus zwei Sätzen, keine Referenznummer.
- **Rolex Datejust 36, Dez. 2023, Full Set, 6.500 €** (3508904381) – konkretes Vergleichsangebot: 126200 mit schwarzem Zifferblatt für 6.950 € auf Chrono24. Abstand rund 7 %, kein Fund.
- **Rolex Datejust 16030 (1988), 5.650 €** (3508814835) – gewerblicher Verkäufer; der Median 9.390 € stammt aus der Query „Rolex Datejust" und mischt moderne 36/41-mm-Modelle mit Vintage. Für die 16030 selbst ist der Preis marktgerecht. Beschreibung zudem widersprüchlich („Plexiglas" – die 16030 hat Saphirglas).
- **Rolex Sea-Dweller Stahl 44 mm, 7.500 €** (3508714411) – Modellangabe widerspricht sich: 44 mm gibt es erst ab Ref. 126600 (2017), „Baujahr 2008" wäre die Deepsea 116660. Konto seit 07/2025, nur Versand, keine Box, keine Papiere, „Tauschangebote willkommen". Nicht belegbar, Profil passt auf die Betrugsmasche.
- **Rolex Air-King 14000 (1992), 3.100 €** (3509091148) – ohne Box und Papiere ist das Marktniveau; nur Versand, Gewerbetext auf Privatprofil.
- **IWC Pilot's Watch Chronograph Spitfire Racing Green, 3.200 €** (3508908832) – lehrbuchhafte Betrugssignatur nach der Leitidee: Konto 44 Tage alt, keine Bewertung, nur Versand, 19 scharfe Bilder, exakte Modell- und Limitierungsangabe, Garantie bis 2028, keine Mängel. Kein `unkenntnis_bonus`.
- **Tudor Black Bay 58 Blau, 2.550 €** (3508659886) – Konto einen Tag alt; Marktniveau gebraucht 2.700–3.300 €, Abstand unter 20 %.
- **Omega Seamaster Diver 300M 212.30.41.20.01.003, 3.000 €** (3508697041) – WatchCharts: Durchschnitt rund 3.200 USD, Spanne 2.600–4.400 USD. Der Preis liegt auf Marktniveau; der Median 4.650 € mischt die neueren 8800-Modelle ein.
- **Omega Seamaster Professional 300m Vintage, 1.350 €** (3508875610) – Heliumventil fehlt, Krone lässt sich nicht verschrauben. Der niedrige Preis erklärt sich selbst.
- **Longines HydroConquest L3.781.4069, 850 €** (3508692074) – konkretes Vergleichsangebot: L3.781.4.56.6 gebraucht für 950 €. Abstand rund 11 %.
- **Sinn 104 St Sa, 850 €** (3508969520) – ohne Papiere ist das Marktniveau (gebraucht 850–1.100 €).
- **TAG Heuer Carrera Chronograph, 1.095 €** (3508680963) – keine Referenznummer, ohne Box und Papiere; „Carrera Chronograph" reicht von 1.200 € (CV2010) bis 3.500 € (Heuer 02). Ohne Modellzuordnung kein Marktwert bestätigbar.
- **TAG Heuer Aquaracer 500, 1.099 €** (3509060078) – Zahlung nur per PayPal-Freunde erbeten, Kronenverschraubung angeschlagen; Preis auf Marktniveau.
- **TAG Heuer Formula 1 Full Set, 800 €** (3508387395) und **Formula 1 Limited, 900 €** (3509130399) – beides Quarzuhren (Ronda 6003.D); der Median 1.350 € mischt Automatik- und Chronographenmodelle ein. Beide Preise liegen über dem Marktwert der Quarzvariante.
- **Jaeger-LeCoultre Atmos Tischuhr, 2.000 €** (3509193657) – `referenz.belastbar: false`, Streuung 3,62. Kein eigener Referenzwert für die konkrete Kaliber-/Baujahrvariante zu belegen.

### Drohnen und Kameras
- **DJI Mini 5 Pro, 360 €** (3508996771) – nur ein Akku, Standard-Fernsteuerung, Zahlung ausdrücklich „PayPal Freunde". Aktuelle Modellgeneration zu 41 % des Marktwerts bei ausgeschlossenem Käuferschutz: kein Fund, sondern ein Warnsignal.
- **DJI Mini 5 Pro Fly More Combo RC2, 479 €** (3509174564) und **PS5 Pro 2 TB, 465 €** (3509183760) – derselbe Verkäufer (ID 28156332) bietet zwei aktuelle Geräte zu rund 45 % des Marktwerts an und schließt in beiden Anzeigen ausdrücklich jede abgesicherte Zahlung aus. Beide verworfen.
- **DJI Mini 5 Pro + RC2 + 2 Akkus, 620 €** (3508981469) – Absturzschaden, vom Verkäufer als Defekt/Ersatzteilspender deklariert. Preis erklärt sich selbst.
- **DJI Mini 4 Pro + RC 2 + 4 Akkus, 435 €** (3508626030) – Konto 41 Tage alt, nur Versand, makellose Zustandsbeschreibung. Betrugsprofil.
- **DJI Mini 4 Pro, 3 Akkus, 350 €** (3508763863) – Verkauf ohne Fernsteuerung; gegen komplette Sets gerechnet ist der Median nicht vergleichbar.
- **DJI Mini 3 Pro Fly More Combo, 290 €** (3509109083) – Konto 125 Tage, höchstens ein Bild, generischer Werbetext.
- **DJI Mavic Pro Platinum, 250 €** (3508887309) – Drohne von 2016, Drittanbieter-Akkus, nur Versand; Marktniveau 250–400 €.
- **DJI Mavic 3 Cine Kamera/Gimbal-Teile und übrige Mavic-Pro-Angebote** – unter der Schwelle oder Ersatzteile.
- **Leica Elmarit-M 135 mm (390 €), Elmarit-M 90 mm (649 €), Summicron-M 90 mm (990 €)** (3509193480, 3509193311, 3509193826) – alle drei vom gewerblichen Händler NSHOT mit Shop-Link, Rabattcode und Zustandsklassen. Das sind Händlerpreise, kein Abstand zum Markt.

### Fahrzeuge und Youngtimer
- **BMW 318 E30, 6.000 €** (3508763044) – nicht fahrbereit, steht seit zwei Jahren, Rost an den üblichen Stellen, kein TÜV. Preis erklärt sich selbst.
- **BMW E36 328i Touring, 5.400 €** (3508954603) – TÜV abgelaufen, Verkäuferbewertung 0,33, Beschreibung zwei Zeilen. Kein belastbarer Abstand.
- **BMW E36 Cabrio 328i, 5.999 €** (3509069124) – ist ein 318i Individual Cabrio mit eingebautem 528i-Motor. Der Median vergleicht mit echten 328i-Cabrios; ein Motorumbau senkt den Wert, statt ihn zu belegen.
- **BMW E36 Compact 323ti, 3.000 €** (3509174155) – umfangreiche eingetragene Umbauten inklusive Motorumbau, Folierung, Tieferlegung. Umbauten dieser Art senken den Sammlerwert, der Preis ist damit erklärt.
- **Mercedes W124, 3.200 €** (3509114172) – Motorisierung nicht genannt; die Query „Mercedes Benz Klasse W124" mischt 200E bis 500E, Limousine, Coupé und Cabrio. Referenzgruppe nicht vergleichbar.
- **Mercedes 190E 1.8, 2.500 €** (3509156285) – als „Beschädigtes Fahrzeug" eingestellt, zwei durchgerostete Wagenheberaufnahmen, 254.832 km. Preis erklärt sich selbst.
- **Simson S51 Neuaufbau, 2.350 €** (3508751828) – MZA-Rahmen ohne Typenschild und Fahrgestellnummer; der Käufer muss die Nummer selbst beschaffen. Das erklärt den Abschlag.
- **Simson Sperber SR4-3 mit Papieren, 1.500 €** (3509191432) – der stärkste Grenzfall des Laufs. Belegt ist nur das Niveau restaurierter Sammlerstücke (3.500–4.300 €); für ein unrestauriertes Patina-Projekt ließen sich keine zwei zustandsgleichen Vergleichsangebote finden, und bei einem 55 Jahre alten Moped entscheidet genau der Zustand über den Wert. Ohne bestätigten zustandsgleichen Marktwert nicht gemeldet.
- **Simson S51 Comfort (2.700 €), Simson Star (1.300 € / 1.350 €), Simson S51 Enduro (2.400 €), Ducati Monster S4 (2.850 €), Yamaha XT 500 Tank (550 €)** – jeweils unter 20 Prozent Abstand nach eigener Prüfung, Referenzgruppe gemischt (`belastbar: false` bei der XT 500, Streuung 11,8) oder Zustand nicht bestimmbar.

### Apple, Konsolen, Computer
- **MacBook Pro 14" M5 1 TB, 1.490 €** (3508685629) – Konto sieben Tage alt, keine Rechnung, nur Versand, Zeitdruck („kann heute noch bis 17:00 verschickt werden"), Zahlungsabwicklung der Plattform ausdrücklich abgelehnt. Betrugsprofil.
- **MacBook Pro 14" M5, 900 €** (3508701356) – Flüssigkeitsschaden steht im Titel. Preis erklärt sich selbst.
- **Übrige MacBooks (M1/M2/M4, 300–1.100 €)** – Abstand nach eigener Prüfung unter 20 Prozent oder Konfiguration (RAM/SSD/Baujahr) nicht eindeutig genug für eine zustandsgleiche Referenz.
- **PS5 Pro 2 TB, 529 €** (3508931507), **499 €** (3509080865), **500 €** (3509121449) – der Median von rund 1.075–1.100 € ist nicht haltbar: die PS5 Pro 2 TB kostet neu 799 €, gebraucht rund 600–700 €. Damit liegt keines der Angebote 20 Prozent unter dem bestätigten Gebrauchtwert.
- **Steam Deck OLED 512 GB, 230 €** (3508431685) – nur Versand, keine Abholung, Beschreibung besteht aus einem kopierten Datenblatt samt Wettbewerbervergleich. 38 % des Marktwerts bei ausgeschlossener Besichtigung: zu riskant.
- **Steam Deck 512 GB, 300 € / 389 €** (3508870110, 3508391950) – Abstand unter 20 Prozent.
- **iPhone 17 256 GB, 699 €** (3509182245) – neu 949 €, gebraucht mit Rechnung rund 750–850 €. Abstand unter 20 Prozent, Verkäuferbewertung 0,20.
- **Übrige iPhones (12 bis 16 Pro, 150–500 €)** – durchweg unter 20 Prozent Abstand zum bestätigten Gebrauchtniveau. Pflichthinweis iCloud-Sperre/MDM wäre ohnehin zu setzen gewesen.

### Fahrräder und E-Bikes
- **Canyon Aeroad CF, 999 €** (3508440143) – Shimano 105 mechanisch, 11-fach: ein älteres Aeroad CF. Der Median 3.650 € stammt aus einer Query, die aktuelle CFR-Modelle einschließt. Referenzgruppe nicht vergleichbar.
- **Canyon Speedmax CF SLX Ultegra Di2, 2.500 €** (3509134739) – Verkauf ausdrücklich ohne Laufräder, Median rechnet gegen komplette Räder.
- **Simplon Kagu Bosch CX, 1.399 €** (3509134462) – Rahmengröße XS und ein vier Jahre alter 625-Wh-Akku ohne Zustandsangabe erklären einen Teil des Abstands; zustandsgleiche Vergleichsangebote nicht zu belegen.
- **Cube Cargo Hybrid, 1.999 €** (3509099136) – 8.158 km Laufleistung. Die hohe Laufleistung erklärt den Abschlag, auch wenn frisch inspiziert.
- **Specialized Turbo Levo, 2.000 €** (3509160687) – weder Modelljahr noch Motorgeneration noch Akkugröße genannt; die Baureihe reicht von 2016 bis 2026. Nicht bestimmbar.
- **Cube Stereo One22, 1.500 €** (3509112170) – Ausstattungsvariante nicht genannt, Preis liegt exakt auf dem 25-Prozent-Quartil.
- **Übrige rund 30 Fahrräder und E-Bikes (300–1.790 €)** – überwiegend `belastbar: false` (Streuung 2,6 bis 6,55, die Query „Cube Bike"/„TREK Fahrrad" mischt Kinderräder mit Fullys) oder Modell/Baujahr/Akkugröße nicht bestimmbar. Keines nach eigener Prüfung sicher 20 Prozent unter Markt.
- **Brompton 3-Gang, 599 €** (3509109768) – Reifen platt, als ungeprüft verkauft, Modelljahr unbekannt.

### Design, Möbel, Sonstiges
- **Louis Poulsen PH5 Vintage, 180 €** (3508928947) – knapp verworfen. Die Suchbelege widersprechen sich (eBay-Angebote 250–750 €, daneben eine Quelle mit 320 € Neupreis, was auf eine Replik oder ein anderes Modell deutet). Ohne WebFetch war das nicht aufzulösen; ein bestätigter Marktwert über 225 € ließ sich nicht belegen.
- **Charles Eames Alu Chair, 370 €** (3458022024) – Beschreibung besteht aus zwei Zeilen, nur Versand, keine Angabe zu Hersteller-Kennzeichnung. Bei Alu Chairs ist der Replikatanteil hoch; Echtheit nicht prüfbar.
- **USM Haller Sideboards/Tische/Rollwagen (180–1.020 €)** – Maße und Konfiguration entscheiden den Wert, der Median mischt Größen (Streuung 1,9 bis 3,46). Kein zustandsgleicher Vergleich.
- **Dieter-Knoll- und Cassina-Polstermöbel (600–780 €)** – `belastbar: false`, kein belegbarer Referenzwert.
- **Gibson Les Paul Tribute 2016, 730 €** (3508387119) – `belastbar: false`, Streuung 2,59; Marktniveau gebraucht 800–950 €, Abstand unter 20 Prozent.
- **Thorens TD 160 MK II, 250 €** (3508033211) – Konto zwei Tage alt, Angaben widersprüchlich („Kein Versand" im Text, Versand im Datenfeld), Zustand und Tonarm/System nicht genannt.
- **Hilti TE 30-C, 280 €** (3509123508) – 25-Prozent-Quartil liegt bei 300 €, Stichprobe n=9. Abstand nicht belastbar.
- **Hilti TE DRS-M Absaugung, 150 €** (3508941557) – Abstand unter der Schwelle.
- **Lego Sammlungsauflösung, 7.800 €** (3509185220) – „Preise auf Anfrage", Set-Liste nur über einen externen Google-Drive-Link. Kein bewertbares Einzelangebot; ein Bündelpreis ohne Inhaltsangabe ist nicht prüfbar.
- **Lego Technic 42056 Porsche, 200 €** (3509183777) – Abstand unter 20 Prozent gegenüber dem bestätigten Sammlerniveau.
- **PKW-Anhänger HP400, 150 €** (3508418582) – Zustand und Baujahr nicht genannt.

## Pflicht-Warnflags in dieser Mail

- Keine RTX 4090, keine Switch 2, keine AirPods und kein Tesla/Porsche im Pool.
- Kein Apple-Gerät gemeldet, der iCloud-/MDM-Hinweis war damit nicht anzuwenden.
- Der Ubiquiti-Switch ist ein Netzwerkgerät ohne Datenträger und wurde auf Werkseinstellungen zurückgesetzt; das DSGVO-Risiko aus der NAS-/Server-Regel greift hier nicht. Stattdessen steht der Herkunfts- und Adoptionsnachweis als Risiko in der Mail.
