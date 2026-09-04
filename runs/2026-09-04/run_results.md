# Lauf 2026-09-04, morgens

- **Ausgeführt:** 4. September 2026, 07:05 Uhr (MESZ)
- **Datenstand `candidates.json`:** 2026-09-04T04:11:31+02:00 (2 h 54 min alt, innerhalb der Vier-Stunden-Grenze)
- **Zeitraum des Sammellaufs:** 2026-09-03T22:59:45+02:00 bis 2026-09-04T03:59:45+02:00
- **Gesichtete Anzeigen:** 18.590
- **Kandidaten in der Warteschlange:** 158
- **Bereits in `deal_log.csv`:** 0
- **Geprüft:** 158 (Vorrang nach absoluter Ersparnis und Liquidität; 47 einzeln gelesen, davon 21 per Websuche gegengeprüft)
- **Gemeldet:** 1

## Gemeldeter Fund

| Titel | Preis | Bestätigter Marktwert | Abstand | Kategorie |
|---|---|---|---|---|
| [Original Louis Poulsen PH5 Pendelleuchte, Vintage](https://www.kleinanzeigen.de/s-anzeige/original-louis-poulsen-ph5-pendelleuchte-poul-henningsen-vintage/3502654019-82-7155) | 180 € | privat ab 250 €, üblich 350–500 €, gewerblich 400–700 € (eBay.de, Kleinanzeigen) | rund 28 % unter dem Marktboden, rund 50 % unter dem üblichen Niveau | design-sammeln |

Der Median von 595 € (n=11, Streuung 2,34) wurde nicht übernommen: die Query
mischt Neuware und andere PH-Modelle. Im Deal steht deshalb ein
`referenz_hinweis` statt `referenz`/`ersparnis_eur`.

## Warum nur ein Fund

Der Lauf hatte eine ungewöhnlich hochwertige Warteschlange: vier Rolex, zwei
Tudor, ein Tesla, ein Leica Q, drei MacBook Pro. Bei jedem einzelnen dieser
Kandidaten ist der Kleinanzeigen-Median an der Websuche zerbrochen, und zwar
immer in dieselbe Richtung: der Median liegt auf Wunschpreisniveau, der
tatsächliche Handelspreis nahe am Angebot.

| Kandidat | Median laut Stufe 1 | Bestätigter Marktwert | Angebot | Echter Abstand |
|---|---|---|---|---|
| Rolex GMT-Master II 16710LN | 16.000 € | 10.600–10.668 € Full Set | 9.916 € | rund 7 % |
| Rolex Datejust 41 126300 weiß | 15.450 € | 8.900–11.075 € | 9.999 € | 0 % |
| Rolex Datejust 41 grün | 14.490 € | rund 11.000 € | 10.300 € | rund 6 % |
| Tudor Black Bay Chrono 79360N | 7.475 € | 4.106 € gebraucht Full Set | 3.990 € | rund 3 % |

Vier von vier. Die Uhren-Referenz der ersten Stufe erzeugt in dieser
Preisklasse systematisch Phantomersparnisse von 3.500 bis 6.000 Euro. Wer dem
Median folgt, meldet vier vierstellige Fehlkäufe.

Die zweite große Gruppe erklärte sich selbst: vier iPhones mit gerissener
Rückseite oder defekter Kamera, ein Haibike ohne Akku, ein Pegasus mit
Original-Akku von 2015, eine Simson mit festem Motor, ein W124 mit unruhigem
Motor, eine defekte Drehmaschine, ein Volvo-Penta-Motor als Bastelobjekt. Das
sind korrekt bepreiste Angebote, keine Funde.

Vier Kandidaten trugen das Ausschlusskriterium aus Schritt 2c offen im Text:
PS5 Pro (3502204459), SRAM Red AXS (3502760286) und Tudor Black Bay 41
(3502375555) verlangen ausdrücklich „PayPal als Freund“ statt Käuferschutz;
die TAG Heuer Aquaracer (3501982198) kommt von einem 71 Tage alten Konto mit
Händlernamen auf Privatprofil, das „nur Barzahlung oder sichere Überweisung“
akzeptiert und einem Privatverkauf eine einjährige „Verkäufergarantie“
beilegt.

## Nebenbefund: die Steam-Deck-Meldungen sind keine Funde mehr

Das ist der wichtigste Befund des Laufs, und er widerspricht der Meldung von
gestern Abend.

`candidates.json` enthielt ein Steam Deck OLED 512 GB für 360 € (3502122191),
neuwertig, mit 1-TB-Karte und OVP, Median 600 € bei n=27 und Streuung 1,14 —
formal ein sauberer Kandidat. Die externe Prüfung schien ihn zu bestätigen:
Valve hat den Neupreis am 27. Mai 2026 von 569 auf 779 € angehoben, neu kostet
das Gerät heute 799,90 € (Geizhals/heise), refurbished rund 600 €.

Der Blick in `deal_log.csv` kippt das Urteil. Seit dem 12. August wurde ein
Steam Deck OLED 512 GB **achtmal** gemeldet:

| Datum | Preis | Median laut Meldung |
|---|---|---|
| 12.08. | 360 € | 624,50 € |
| 19.08. | 370 € | — |
| 19.08. | 315 € | 600 € |
| 25.08. | 360 € | 620 € |
| 25.08. | 310 € | 620 € |
| 02.09. | 290 € | 610 € |
| 03.09. | 250 € | 615 € |
| (04.09.) | 360 € | 600 € |

Dazu vier 1-TB-Geräte zwischen 340 und 470 €. Ein Preisniveau, das drei Wochen
lang mit dieser Dichte wiederkehrt, ist kein wiederkehrendes Schnäppchen,
sondern der Markt. Der Median von 600 bis 620 € besteht aus Wunschpreisen, die
niemand zahlt; gehandelt wird zwischen 250 und 370 €. Der heutige Kandidat
liegt mit 360 € am **oberen** Rand dieses Bandes.

Der Abendlauf vom 03.09. hat die Preiserhöhung korrekt erkannt und daraus den
falschen Schluss gezogen: Er hat den Valve-Neupreis als Referenz gesetzt und
zwei Steam Decks gemeldet. Der Neupreis eines Herstellers, der seine Preise
wegen einer Speicherkrise anhebt, ist aber kein Wiederbeschaffungswert für ein
Gebrauchtgerät, dessen Gebrauchtmarkt der Erhöhung nicht gefolgt ist. Der
eigene `deal_log.csv` ist hier die bessere Quelle als jeder Preisvergleich —
er ist ein Protokoll tatsächlich beobachteter Angebotspreise über sechs Wochen.

Zwei Konsequenzen, beide für Stufe 1 und damit nicht in diesem Lauf zu
entscheiden:

1. Die Watchlist `konsolen-sweep` sollte für Steam Deck OLED eine feste
   Preisschwelle statt des Medians bekommen; bei 250 € beginnt der Bereich, in
   dem ein Angebot wieder auffällig ist.
2. Ein Kandidat, dessen Kategorie in `deal_log.csv` bereits mehr als dreimal im
   selben Preisband gemeldet wurde, sollte der Routine mit diesem Hinweis
   vorgelegt werden. Die Information steht in der Datei, aber nur, wenn man
   gezielt danach sucht.

## Nebenbefund: zwei Kandidaten blieben mangels Quelle ungeprüft

Die Leica Q Typ 116 für 2.799 € (3502866920) und die fünf `notverkaeufe`-Posten
tragen `referenz: null`. Für die Leica ist MPB.com — die in Schritt 2d
vorgesehene Referenzquelle für Kameras — über den Egress-Proxy dieser Umgebung
blockiert (`EGRESS_BLOCKED`), ebenso picclick.de. Nach „Erfinde keine
Marktwerte“ wurde deshalb nicht geschätzt. Die Anzeige ist inhaltlich
unauffällig (Konto seit 2012, Mängel offengelegt, Zubehörliste, Käuferschutz)
und wäre bei einer erreichbaren Quelle prüfenswert gewesen. Falls MPB dauerhaft
blockiert bleibt, braucht Schritt 2d für Kameras eine erreichbare
Ausweichquelle.

## Verworfene Kandidaten (157)

- **Tesla Model S 85 *Free Supercharging*Pano*Luft*AHK*CCS** – 12950 €, `3502594050` (tesla): 319.486 km und SOH 86 %; die Akkugarantie (8 Jahre) ist seit 2022 abgelaufen – die Laufleistung erklärt den Preis. Referenzquery „Tesla Model Free 85“ mischt zudem Baujahre.
- **Rolex GMT Master  II** – 9916 €, `3502706175` (uhren): Marktwert bestätigt: 10.600 € und 10.668 € für 16710LN Full Set (Chrono24.de). 9.916 € sind rund 7 % Abstand, nicht 20 %. Der KA-Median von 16.000 € mischt Pepsi, Coke und die neuere 116710.
- **Rolex Datejust 41mm 126300 Full Set ungetragen mit weißem Zifferb** – 9999 €, `3502409586` (uhren): Marktwert bestätigt: 8.900 € bis 11.075 € für Datejust 41 126300 (Chrono24.de). 9.999 € liegen im Markt; der Median von 15.450 € ist Wunschpreisniveau.
- **Golf 2 GTI H- Kennzeichen** – 6500 €, `3502502896` (youngtimer-alltag): 240.000 km; Golf II GTI beginnen laut AutoUncle (112 Angebote) bei 3.725 €. Ein 20-%-Abstand zu einem bestätigten Wert ist nicht belegbar. Gewerbetext auf Privatprofil, Konto 177 Tage alt.
- **Rolex Datejust 41mm Grün Neu Fullset** – 10300 €, `3502356936` (uhren): Datejust 41 126300 mit grünem Zifferblatt bestätigt bei rund 11.000 € (Chrono24). 10.300 € = 6 % Abstand. Konto 23 Tage alt, nur Abholung, 10.300 € Bargeld.
- **Mercedes Benz S-Klasse Bundeswehr w126** – 7200 €, `3502151806` (youngtimer-alltag): Fahrersitz beschädigt, 236.241 km, Bundeswehr-Provenienz ist Nischenware. Kein Referenzwert gefunden, der 7.200 € als 20 % unter Markt belegt.
- **Rolex datejust 41** – 8900 €, `3502558741` (uhren): „Datejust 41“ gibt es erst seit 2016; Baujahr September 2011 bedeutet Datejust II 116300, Markt 7.000–9.500 €. 8.900 € sind marktgerecht. Verkäuferbewertung 0,22.
- **Tudor Black Bay Chrono ‼️ 79360N Schwarz | 2026 Inz. Rolex** – 3990 €, `3502871597` (uhren): Marktwert bestätigt: 4.106 € für 79360N Full Set gebraucht (Chrono24.de). 3.990 € vom Händler sind 3 % Abstand; der Median von 7.475 € existiert für dieses Modell nicht.
- **Weiler Drehmaschine  defekt** – 1500 €, `3502585043` (werkzeug-maschinen): Ausdrücklich defekt (Vorschübe), als Teilespender angeboten. referenz.belastbar false (Streuung 6,8).
- **Mercedes W124  230E Automatik Oldtimer** – 4700 €, `3502393508` (youngtimer-alltag): W124-Limousinen in solidem Zustand liegen bei 5.000–10.000 €; ein 20-%-Abstand zu 4.700 € ist nicht belegbar. Die Angabe „HU bis November 2029“ ist im September 2026 zudem unplausibel.
- **Mercedes 300 D W124 H-Zulassung** – 5900 €, `3502393527` (youngtimer-alltag): 5.900 € für einen 300 D von 1990 mit H-Zulassung und TÜV neu liegen im Korridor 5.000–10.000 €; ein 20-%-Abstand ist nicht belegbar.
- **Mercedes W124 300e** – 5500 €, `3502715555` (youngtimer-alltag): Als Projekt verkauft, Klebereste am Lack, Nachrüstungen – der Preis erklärt sich.
- **Mercedes Benz W124 230 E** – 2900 €, `3502582648` (youngtimer-alltag): Motor läuft unruhig, Batterie leer, Kabelbaum zu prüfen, 260.000 km – der Verkäufer schreibt selbst „Auto braucht Zeit und Geld investieren“.
- **Volvo 850 T5** – 4999 €, `3502455994` (youngtimer-alltag): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Suzuki GSX-R 750 W** – 2000 €, `3502616287` (motorraeder): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Wohnwagen HP 400 Qek Junior** – 1799 €, `3502825072` (messtechnik): TÜV abgelaufen, Aufbereitung von außen nötig – für einen unrestaurierten Qek Junior ist 1.799 € marktgerecht.
- **SRAM eTAP Sram Red AXS-Gruppe (NEU)** – 725 €, `3502760286` (ebike-rad): „Barzahlung und Abholung oder PayPal als Freund“, Waren und Dienstleistungen ausdrücklich ausgeschlossen – Zahlung außerhalb des Käuferschutzes.
- **Tudor prince date** – 1300 €, `3502115678` (uhren): Ohne Papiere, Revisionsstand unbekannt – der Verkäufer nennt das selbst als Preisgrund. Ein bestätigter Marktwert für die Ref. 79410P mit 20 % Abstand ließ sich nicht belegen.
- **Pegasus Trekking E-Bike** – 600 €, `3502148575` (ebike-rad): Pegasus Premio E10 von 2015 mit dem originalen Bosch Powerpack 400; die Anzeige nennt selbst rund 28 km Restreichweite – das Akkualter erklärt den Preis.
- **Santa Cruz Bronson A R  Gr. XS** – 1700 €, `3502816879` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Rennrad BMC Roadmachine 01  Four Force AXS** – 2350 €, `3502534579` (modellbau-sammler): Kein bestätigter Marktwert mit mindestens 20 Prozent Abstand.
- **Riese & Müller Swing City E-Bike** – 1500 €, `3502156305` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Riese & Müller E-Bike Nevo4 Gt Varo in weiß , Pedelec** – 2500 €, `3457478523` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Specialized Turbo Como SL 5.0 E-Bike – Rahmengröße M** – 2050 €, `3502840658` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Cube Stereo 140 HPC Carbon Fully Mountainbike – Top Fox Kashima F** – 1250 €, `3502135324` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **TUDOR Black Bay 41mm - Fullset- Kautschukband neu + Natostrap** – 2222 €, `3502375555` (uhren): „Bezahlung in bar, Überweisung oder PayPal (Freunde)“ und Versandrisiko beim Käufer. Zudem liegt die BB 41 79230N gebraucht bei 2.400–2.900 €, also rund 10–15 % über dem Angebot.
- **Damen Trekking E-Bike Fischer** – 790 €, `3502153642` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **BMW 316i Limo E36, ** – 2000 €, `3502425383` (youngtimer-alltag): Kein bestätigter Marktwert mit 20 Prozent Abstand; die Referenzquery mischt Motorisierungen und Baujahre derselben Baureihe.
- **Quooker CUBE** – 960 €, `3502224503` (ebike-rad): Gewerbliche Verkaufsanzeige mit Beratung, Montageservice und Gewährleistung – ein Ladenpreis, kein Fehlpreis.
- **USM Haller Regal | Reinweiß | 5 Fächer** – 870 €, `3450998110` (design-sammeln): Gewerblicher Händler; 870 € plus 109 € Lieferung liegen im üblichen Gebrauchtkorridor für ein 180er USM-Regal. Kein Fehlpreis eines Privatverkäufers.
- **Cube Stereo Hybrid 140 HPC Race 625** – 1350 €, `3502192193` (ebike-rad): Der Verkäufer schreibt selbst, er verkaufe unter Preis, weil Bremshebel, Griffe und Optik nachzuarbeiten sind.
- **Herrenrad Cube Touring One - 54cm** – 500 €, `3502123868` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Cube Ebike** – 600 €, `3502810524` (ebike-rad): Die Referenzquery „Cube Ebike“ (n=8) mischt alle Cube-Pedelecs quer über Baujahre und Klassen und ist nicht vergleichbar. Für ein neun Jahre altes Hardtail ließ sich kein eigener Marktwert mit zwei konkreten Vergleichsangeboten belegen; das Profil (Akku 2024, Motor 2019, Bremsen 2026, Konto seit 2011, Bewertung 0,93) wäre sonst interessant.
- **Simson Schwalbe Kr51/1 K mit KBA Papieren Tausch möglich** – 1200 €, `3502853520` (motorraeder): „Der Motor ist leider Fest“, Hauptständeraufnahme geschweißt und nachzuarbeiten, Kleinteile fehlen – der Preis erklärt sich.
- **Specialized Stumpjumper evo S-Works Rahmen S4** – 1300 €, `3502838796` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Bosch E-Trekking Victoria Rad Damen** – 500 €, `3502395566` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Specialized Ebike Turbo Como 3.0** – 1000 €, `3502822706` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Velo de Ville AEB 890 Trekking E-Bike Tiefeinsteiger** – 1499 €, `3502183849` (ebike-rad): Gewerbliches Refurbished-Angebot mit Artikelnummer – Ladenpreis.
- **MacBook Pro M5 1TB** – 1299 €, `3502667365` (macbook): 42 % unter Neupreis (M5 24/1 TB rund 2.200 €), dabei „keinerlei Kratzer“, Vollzubehör, exakte Spezifikation, ausschließlich Versand, Konto seit Januar 2026 ohne Bewertung – das Muster aus Schritt 2c, nicht das eines ehrlichen Verkäufers.
- **Mountainbike - CUBE STEREO 140 HPC SL** – 1600 €, `3502814136` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Cube Stereo One 77 Pro M Fully Enduro MTB** – 1850 €, `3494285620` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **TAG Heuer Aquaracer Chronograph 300M** – 830 €, `3501982198` (uhren): Konto 71 Tage alt, Händlername „SS Times“ auf einem Privatprofil, „Nur Barzahlung oder sichere Überweisung“ und eine „Verkäufergarantie: 1 Jahr“ beim Privatverkauf – Betrugsprofil. referenz.belastbar ist zudem false.
- **Eames Chair EA 217** – 1450 €, `3502505826` (design-sammeln): Bestätigt sind 2.390 € und 2.980 € (Sebworld, II. Hand) – das sind Händlerpreise mit Gewährleistung. Privat liegt ein EA 217 in Leder bei 1.500–2.200 €, damit sind 1.450 € unter 20 % Abstand.
- **Möbel Dieter Knoll Badezimmer–Möbel XXXLutz Hirschaid** – 799 €, `3476097233` (design-sammeln): Gewerbliche Abverkaufsanzeige mit Streichpreis (4.270 € durchgestrichen, „Sie sparen 81 %“) – ein Ladenpreis, kein Fehlpreis.
- **Simson Schwalbe kr51 1  K Oldtimer** – 2150 €, `3502726893` (motorraeder): „Papiere sind beantragt“ – ohne Zulassungsbescheinigung Teil II ist ein Fahrzeug nicht billig, sondern richtig bepreist. p_ratio 0,72.
- **Cube Touring Damenrad - TOP ZUSTAND** – 700 €, `3502144624` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Specialized E-Bike XL Rahmen** – 950 €, `3502147715` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Honda Fireblade CBR 900 RR (SC28)** – 1690 €, `3502522370` (motorraeder): Kein bestätigter Marktwert mit 20 Prozent Abstand für dieses Modell und Baujahr.
- **Tag Heuer Carrera Calibre 5 Automatik Day Date Komplettset!!** – 1250 €, `3502640220` (uhren): Der bestätigte Gebrauchtmarkt liegt bei diesem Modell näher am Angebotspreis als der Kleinanzeigen-Median suggeriert; der 20-Prozent-Abstand ist nicht belegbar.
- **Tag Heuer Carrera Caliber 16 Day-Date** – 1650 €, `3502765945` (uhren): Der bestätigte Gebrauchtmarkt liegt bei diesem Modell näher am Angebotspreis als der Kleinanzeigen-Median suggeriert; der 20-Prozent-Abstand ist nicht belegbar.
- **MacBook Pro M2 Pro 32 GB RAM mit Originalverpackung** – 999 €, `3502795251` (macbook): Delle im Displaydeckel, Gebrauchsspur an der Ecke, ohne Netzteil (70 € Aufpreis), gewerblich mit Bewertung 0,40 – der Preis erklärt sich.
- **Cube Stereo 120 Pro Fully Mountainbike Größe S 2022** – 1200 €, `3502132825` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **MacBook Pro 14 (M5)** – 1300 €, `3502623656` (macbook): MacBook Pro 14 M5 16/512 ab 1.449 € neu (Geizhals). 1.300 € für ein sechs Monate altes Gerät sind rund 10 % Abstand.
- **Simson S51 Enduro Rahmen mit KBA Papieren** – 1299 €, `3502673949` (motorraeder): Kein bestätigter Marktwert mit 20 Prozent Abstand für dieses Modell und Baujahr.
- **Tag Heuer Formula 1 Chronograph Quarz 43mm** – 799 €, `3502902302` (uhren): Der bestätigte Gebrauchtmarkt liegt bei diesem Modell näher am Angebotspreis als der Kleinanzeigen-Median suggeriert; der 20-Prozent-Abstand ist nicht belegbar.
- **Gravelbike Cube Nuroad Pro, Gr. S** – 650 €, `3502496517` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **USM Haller Sideboard Lowboard Aktenschrank Regal Container** – 899 €, `3502527819` (design-sammeln): Für dieses Stück ließ sich kein bestätigter Marktwert mit zwei konkreten Vergleichsangeboten in gleicher Ausführung und gleichem Zustand belegen.
- **Apple MacBook Pro 1TB wie neu** – 980 €, `3502175704` (macbook): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **MacBook Pro 14" M2 Pro | 32 GB | 1 TB | US-QWERTY** – 1100 €, `3502559855` (macbook): Getauschtes Logicboard, Delle an der Kante, Deckel schließt nicht bündig und öffnet sich selbst – die Mängel erklären den Preis.
- **Cube Reaction Hybrid E-Bike** – 1300 €, `3502892828` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Vitra - Original Aluminium Chair EA 117** – 1000 €, `3458802262` (design-sammeln): Kunstleder statt Leder, Mitte der 1990er, dokumentierte Verfärbungen und Kratzer – 1.000 € liegen im Gebrauchtkorridor eines 30 Jahre alten EA 117.
- **Longines HydroConquest Automatik Herrenuhr** – 600 €, `3502211621` (uhren): Ohne Box und Papiere; HydroConquest Automatik gebraucht 650–900 €, also unter 20 % Abstand. Konto 51 Tage alt, ausschließlich Versand.
- **Specialized Allez** – 620 €, `3502215519` (ebike-rad): Trägt unkenntnis_bonus und wurde deshalb nicht nach Anzeigenqualität abgewertet – aber referenz.belastbar ist false (Streuung 2,73), und die Beschreibung nennt nur die Rahmenhöhe. Ohne Modelljahr und Ausstattung ist kein eigener Marktwert zu belegen.
- **Sony PlayStation 5 Pro PS5 Pro 2 TB mit Laufwerk & OVP** – 530 €, `3502204459` (konsolen-sweep): „PayPal Freunde bei Versand, über PayPal sind Waren und Dienstleistungen nicht möglich“ – Zahlung außerhalb des Käuferschutzes, Ausschlusskriterium nach Schritt 2c.
- **Rennrad specialized elite secteur zu verkaufen!!** – 450 €, `3502622820` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Canyon spectral al** – 850 €, `3502763951` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Trek Farley Fatbike Mountainbike** – 450 €, `3502553763` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Canyon Strive AL Enduro Fully** – 599 €, `3502738362` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **USM Haller Sideboard** – 1000 €, `3502450634` (design-sammeln): Für dieses Stück ließ sich kein bestätigter Marktwert mit zwei konkreten Vergleichsangeboten in gleicher Ausführung und gleichem Zustand belegen.
- **Original USM Haller Board in Grün - inkl. Softclose** – 930 €, `3318513954` (design-sammeln): „Autorisierter USM Haller Partner“ – Händlerpreis.
- **Haibike XDURO TREKKING PRO E-bike** – 400 €, `3502211752` (ebike-rad): „AKKU IST NICHT DABEI“. Ein Bosch-Ersatzakku kostet 579–599 € neu – der fehlende Akku erklärt den Preis vollständig.
- **Cube Stereo 120 Race - S - 29"** – 999 €, `3502880061` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Mafell Kettenstemmer** – 700 €, `3502554129` (werkzeug-maschinen): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Cube Cross Pro Damenrad** – 550 €, `3502748639` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Cube Performance 500 E-Bike** – 1000 €, `3502840026` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Ps5 Pro 2TB** – 610 €, `3502898606` (konsolen-sweep): PS5 Pro 2 TB gebraucht liegt bei 600–650 €; 610 € sind kein Abstand. Zusätzlich verkauft ein PRO-Konto namens „Schlatterer Tankanlagen“ eine Spielkonsole.
- **Canyon Strive AL Mountainbike weiß** – 650 €, `3502713370` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Truma Aventa Comfort Ausseneinheit - Klimaanlage** – 800 €, `3400941253` (camper-marine): „hatte Kälteleistungsprobleme“ – der Defekt erklärt den Preis.
- **Cube Nuroad Gravelbike** – 850 €, `3502112320` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Arne Jacobsen Oxford - Fritz Hansen Designklassiker Bürostuhl** – 500 €, `3502657030` (design-sammeln): Bestätigt: gebrauchte Fritz-Hansen-Oxford-Stühle liegen bei 150–465 € (eBay.de), ein Vintage-Stück von 1979 bei 749 €. 500 € liegen im oder über dem Markt.
- **Cube Mountainbike Größe S** – 500 €, `3502400497` (ebike-rad): Trägt unkenntnis_bonus, aber referenz.belastbar ist false (Streuung 4,44) und die Anzeige nennt kein Modell. Kein eigener Marktwert belegbar.
- **MacBook Air** – 400 €, `3502835448` (macbook): Anzeige nennt weder RAM noch SSD; ein M1 Air liegt gebraucht bei 430–500 €, 400 € sind kein Fund.
- **Haibike Xduro Trekking** – 459 €, `3502836915` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Rennrad Cube Attain** – 579 €, `3502186930` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Volvo Penta Bootsmotor mit Z-Antrieb** – 400 €, `3502180918` (camper-marine): Ausdrücklich als Bastelobjekt und Ersatzteilträger verkauft.
- **Fahrrad Herren Trekking** – 350 €, `3502373455` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Pegasus Solero SL Disc  Damen Trekingrad 28 Zoll** – 350 €, `3502762583` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Cube EXC Trekkingrad Damenrad** – 450 €, `3502546142` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **USM Haller** – 800 €, `3502667076` (design-sammeln): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Diamond Chair von Knoll, Designersessel** – 499 €, `3345201576` (design-sammeln): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Vitra Eames Stool Modell A Design Nussbaum Hocker** – 600 €, `3502511709` (design-sammeln): Für dieses Stück ließ sich kein bestätigter Marktwert mit zwei konkreten Vergleichsangeboten in gleicher Ausführung und gleichem Zustand belegen.
- **MacBook Air** – 400 €, `3502112211` (macbook): Der bestätigte Gebrauchtpreis liegt dicht am Angebotspreis; der 20-Prozent-Abstand ist nicht belegbar.
- **Trek Marlin 6 29 Zoll Gr. M Deore Mountainbike Jugendfahrrad** – 350 €, `3502770550` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **iphone 16 pro** – 400 €, `3502217740` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **Cube Fahrrad** – 350 €, `3502666444` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **6 x Vitra Eames Plastic Armchair DAR Original Thonet Design** – 175 €, `3502892867` (design-sammeln): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **4er Set Vitra Stühle HAL Wood mit Sitzpolster Jasper Morrison Des** – 585 €, `3055047580` (design-sammeln): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Fahrrad 28" Trekking, Pegasus SL Primo** – 350 €, `3502777634` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Specialized Stumpjumper FSR 26 Zoll Größe L** – 350 €, `3502405719` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Trekkingrad Herren KTM Life Force** – 350 €, `3502441472` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **E bike Pedelec Citybike Trekkingrad Top-Zustand sofort fahrbereit** – 599 €, `3502177660` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **DJI MINI 5 Pro + DJI Care Refresh** – 600 €, `3502604384` (optik-drohnen): Neupreis bestätigt: Drohne ab 638 €, Fly More Combo 899 € (Geizhals). Ein sieben Wochen altes Bundle mit Care Refresh liegt gebraucht bei 700–780 €; 600 € sind 14–20 % und damit unter der Schwelle. Verkäuferprofil ist einwandfrei, der Abstand reicht nicht.
- **Kalkhoff Damen-Trekkingrad 28 zoll** – 300 €, `3502767289` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Trekkingrad KTM** – 320 €, `3502151374` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Cube MTB größe M 29 Zoll** – 350 €, `3502843725` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **29 Zoll CUBE** – 300 €, `3502388831` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Apple MacBook Pro** – 320 €, `3502686499` (macbook): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Apple MacBook Air M2 Top Zustand** – 480 €, `3502137260` (macbook): MacBook Air M2 8/256 gebraucht 550–650 €; 480 € sind unter 20 % Abstand. Konto 80 Tage alt, Gewerbetext auf Privatprofil.
- **MacBook Air 13  guter Zustand!!** – 450 €, `3502182997` (macbook): Der bestätigte Gebrauchtpreis liegt dicht am Angebotspreis; der 20-Prozent-Abstand ist nicht belegbar.
- **e bike Trekkingrad  von Fischer** – 350 €, `3502691899` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Trek Mountainbike schwarz-rot** – 315 €, `3502193828` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Neuwertig Steam Deck OLED 512GB mit Speicherkarte** – 360 €, `3502122191` (konsolen-sweep): Siehe Nebenbefund: Steam Deck OLED 512 GB wurde seit dem 12. August achtmal zwischen 250 und 370 € gemeldet. 360 € sind der obere Rand des tatsächlichen Marktbands, nicht 40 % darunter.
- **Apple MacBook Space Grau** – 480 €, `3502662277` (macbook): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **iPhone 15 128GB** – 235 €, `3502215432` (apple-mobil): „Kamera macht Bilder jedoch wird es nicht in der Galerie angezeigt“, Akku 80 % – der Defekt erklärt den Preis.
- **Original Vitra Eames Stühle, schwarz, 2 Stk. vorhanden** – 195 €, `3466943734` (design-sammeln): Für dieses Stück ließ sich kein bestätigter Marktwert mit zwei konkreten Vergleichsangeboten in gleicher Ausführung und gleichem Zustand belegen.
- **iPhone 15 Pro Grau** – 320 €, `3502147991` (apple-mobil): Rückglas gesprungen – der Schaden erklärt den Preis.
- **iPhone 14 Pro 256GB Space Schwarz – Rückglas gesprungen** – 250 €, `3502644814` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **iPhone 15, 128 GB /Originalverpackung** – 290 €, `3502801874` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **CUBE, ATTENTION.** – 300 €, `3502813857` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Original iPhone 13 Pro Max 256GB** – 200 €, `3502820019` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **iPhone 15 Pro 128gb** – 300 €, `3502209565` (apple-mobil): „Hinten backover ist leider defekt“ – der Schaden erklärt den Preis. Verkäuferbewertung 0,18.
- **Iphone 14 Plus** – 150 €, `3502899389` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **iPhone 13 mini 512 GB** – 220 €, `3502760049` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **Original Panton Chair schwarz** – 160 €, `3502188627` (design-sammeln): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **iPhone 15 schön** – 315 €, `3502805060` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **IPhone 15 128gb Schwarz** – 250 €, `3502180826` (apple-mobil): „Rückseite stark beschädigt/gerissen“ – der Schaden erklärt den Preis.
- **INTEX Ultra XTR Frame Pool 549x274x132 - abgebaut + eingelagert** – 330 €, `3502810766` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **Cube Access Pro W - Hardtail Shimano Mountainbike** – 325 €, `3502222041` (ebike-rad): Fahrräder und E-Bikes lassen sich ohne Modelljahr, Rahmengröße, Antriebsgeneration und Akkualter nicht mit zwei konkreten Vergleichsangeboten desselben Modells belegen; die Referenzquery fasst hier ganze Modellfamilien zusammen. Kein bestätigter Marktwert, damit kein Fund.
- **iphone 14 pro max 128gb** – 280 €, `3502891033` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **iPhone 14 Pro Max sehr guter Zustand 128GB** – 280 €, `3502795220` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **Vitra Eames Plastic Chair DSX schwarz mit Sitzpolster** – 190 €, `3502798518` (design-sammeln): Für dieses Stück ließ sich kein bestätigter Marktwert mit zwei konkreten Vergleichsangeboten in gleicher Ausführung und gleichem Zustand belegen.
- **iPhone 15 128 gb Black** – 299 €, `3502813640` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **Apple MacBook Air M1 13“ 2020** – 300 €, `3502778264` (macbook): Der bestätigte Gebrauchtpreis liegt dicht am Angebotspreis; der 20-Prozent-Abstand ist nicht belegbar.
- **Specialized Mountainbike** – 350 €, `3502860706` (ebike-rad): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **iPhone 14 Pro Max 128 GB** – 300 €, `3502813854` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **DJI Air 2 Fly More Combo | Sehr wenig benutzt** – 249 €, `3502850741` (optik-drohnen): Der bestätigte Gebrauchtpreis liegt dicht am Angebotspreis; kein 20-Prozent-Abstand.
- **DJI Mavic Pro** – 260 €, `3502753695` (optik-drohnen): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **iPhone 14 Pro 128GB** – 260 €, `3502872181` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **iPhone 14 128 GB Midnight** – 189 €, `3502670790` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **iPhone 14 plus 128GB Blau sehr guter Zustand ❎FESTPREIS❎** – 219 €, `3502855284` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **iPhone 13, 128GB, Grün** – 150 €, `3502754797` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **Apple iPhone 13, blau, mit Zubehör und OVP** – 150 €, `3502740541` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **iPhone 13 Pro** – 200 €, `3502650980` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **iPhone 14 128 GB** – 210 €, `3502871199` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **iPhone 12 Pro Max 128 GB** – 150 €, `3502635604` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **Iphone 12 Pro Max 256GB** – 180 €, `3502846236` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **IPhone 13 Pro 256 GB** – 250 €, `3502751219` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **IPhone 13 Handy** – 150 €, `3502659097` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **Apple iPhone 12 Pro Graphite** – 150 €, `3502804215` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **Panasonic Lumix Digitalkamera mit Leica Objektiv** – 189 €, `3502840905` (foto-sweep): referenz.belastbar ist false beziehungsweise referenz.streuung über 2,5 – der Median hat verschiedene Produkte gemischt und zählt nach Schritt 2a nicht. Ein eigener Marktwert war ohne exakte Modell- und Ausstattungsangabe nicht zu belegen.
- **Handy iPhone 12 Schwarz guter Zustand** – 150 €, `3502875382` (apple-mobil): iPhone-Gebrauchtpreise dieser Generation liegen dicht am Angebotspreis; der 20-Prozent-Abstand zu einem bestätigten Marktwert ist nicht belegbar.
- **Leica Q Typ 116 19000 24.2MP Vollformat Digitalkamera Summilux 28** – 2799 €, `3502866920` (kameras-leica): referenz null, und MPB.com ist über den Egress-Proxy nicht abrufbar. Ohne belastbaren Referenzwert wird nicht geschätzt – der Kandidat bleibt ungeprüft, nicht verworfen-weil-schlecht.
- **REMKO Climat 50 A Warmluftheizung – Scheunenfund – ungeprüft** – 399 €, `3502893206` (notverkaeufe): referenz null. Ohne Kleinanzeigen-Median und ohne belegbaren eigenen Referenzwert wird nach Schritt „Was du nicht tust“ nicht geschätzt.
- **Scheunenfund Vespa PK50 XL  1990** – 800 €, `3502868906` (notverkaeufe): referenz null. Ohne Kleinanzeigen-Median und ohne belegbaren eigenen Referenzwert wird nach Schritt „Was du nicht tust“ nicht geschätzt.
- **Gilde Clowns * Sammlungsauflösung * top Editionen** – 999 €, `3502861078` (notverkaeufe): referenz null. Ohne Kleinanzeigen-Median und ohne belegbaren eigenen Referenzwert wird nach Schritt „Was du nicht tust“ nicht geschätzt.
- **NOTVERKAUF!!  Motorschaden skoda octavia 1.9tdi** – 1200 €, `3502891759` (notverkaeufe): referenz null. Ohne Kleinanzeigen-Median und ohne belegbaren eigenen Referenzwert wird nach Schritt „Was du nicht tust“ nicht geschätzt.
- **R4 TL scheunenfund als Teileträger oder zum restaurieren .** – 900 €, `3502907614` (notverkaeufe): referenz null. Ohne Kleinanzeigen-Median und ohne belegbaren eigenen Referenzwert wird nach Schritt „Was du nicht tust“ nicht geschätzt.

# Lauf 2026-09-04, abends

- **Ausgeführt:** 4. September 2026, 19:05 Uhr (MESZ)
- **Datenstand `candidates.json`:** 2026-09-04T18:43:08+02:00 (22 Minuten alt, innerhalb der Vier-Stunden-Grenze)
- **Zeitraum des Sammellaufs:** 2026-09-04T12:26:10+02:00 bis 2026-09-04T17:26:10+02:00
- **Gesichtete Anzeigen:** 162.022
- **Kandidaten in der Warteschlange:** 163
- **Bereits in `deal_log.csv`:** 0
- **Geprüft:** 163 (Vorrang nach absoluter Ersparnis und Liquidität; 41 einzeln gelesen, davon 13 per Websuche gegengeprüft)
- **Gemeldet:** 4

## Gemeldete Funde

| Anzeige | Preis | Median (n) | Bestätigtes Preisniveau | Abstand |
|---|---|---|---|---|
| Wohnwagen HP 400 Qek Junior (3502825072) | 1.799 € | 3.700 € (20) | 2.900–4.000 € (mobile.de, autoline) | rund 38 % unter dem unteren Niveau |
| Yamaha RD 350 YPVS 1984 (3475951001) | 3.900 € | 5.760 € (33) | 6.798–7.500 € (Classic Trader, vier 1984er Angebote) | rund 33 % auch gegen ein vorsichtiges Privatniveau von 5.800 € |
| Riese & Müller Nevo4 GT Vario (3457478523) | 2.500 € | 3.999 € (62) | 3.790–4.599 € (Gebrauchtrad24, Upway, Kleinanzeigen) | rund 34 % unter dem günstigsten bestätigten Angebot |
| DJI Mavic Air 2 Fly More Combo (3502850741) | 249 € | 394 € (64) | 579–649 USD gebraucht (MPB) | mindestens 37 % |

## Verworfene Kandidaten

### Preis erklärt sich von selbst

- **BMW 320 Cabrio E30 Benzin/LPG** (3503412896, 7.700 €, youngtimer-alltag): Attribut "Beschädigtes Fahrzeug", 230.000 km, ohne TÜV, längere Standzeit, Heckscheibe defekt, Delle und Klarlackablösung. Der Median von 15.210 € gilt fahrbereiten Autos mit HU.
- **BMW E36 Cabrio M Paket** (3503326855, 3.950 €, youngtimer-alltag): 295.000 km und HU nur bis März 2026, also abgelaufen. Die Laufleistung erklärt den Abstand zum Median vollständig.
- **E36 Cabrio + Hardtop** (3503376113, 4.000 €, youngtimer-alltag): TÜV abgelaufen, Verdeck erneuerungsbedürftig, Türschloss und Türverkleidung fehlen, Beifahrerfenster defekt. Der Verkäufer nennt es selbst ein Sommerprojekt.
- **Mercedes W124 300e** (3502715555, 5.500 €, youngtimer-alltag): 13 Jahre Scheunenstand, muss mit Hänger geholt werden, Auspuff abgerostet, Reifen alt, Attribut "Beschädigtes Fahrzeug".
- **Rolex Lady-Datejust 26 mm** (3502932188, 4.000 €, uhren): Lünette nachträglich mit Aftermarket-Steinen besetzt, Box und Papiere fehlen. Beides senkt den Wert genau um die Differenz zum Median; dazu Konto 20 Tage alt.
- **Simson Schwalbe KR51/1 K Scheunenfund** (3502853520, 1.200 €, motorraeder): Motor fest, Hauptständeraufnahme schon einmal geschweißt und erneut fällig.
- **Simson S51 mit KBA Papieren** (3503283823, 2.200 €, motorraeder): Läuft aktuell nicht, Laufverhalten nach dem Einstellen unbekannt. Der Verkäufer benennt den Marktwert selbst korrekt.
- **Specialized Stumpjumper evo S-Works Rahmen S4** (3502838796, 1.300 €, ebike-rad): Angeboten wird nur ein Rahmenset, der Median von 2.349 € enthält Komplettbikes. Phantomersparnis.
- **Cube Stereo 170 Race Rahmenset** (3503175981, 629 €, ebike-rad): Ebenfalls nur Rahmen ohne Sattelstütze, Dämpfer müsste zum Service; der Median mischt komplette Räder.
- **Omega Constellation Vintage Automatic** (3503253535, 790 €, uhren): "Spider Dial" heißt gerissenes Zifferblatt, der Titel widerspricht sich zwischen Chronometer und Chronograph, Konto 45 Tage alt.

### Referenz nicht belastbar oder Marktwert nicht bestimmbar

- **Rolex Lady-Datejust President Yellow Gold Diamond** (3503219765, 2.500 €, uhren): Streuung 26,63 bei 98 gemischten Anzeigen, p25 bei 300 €. Eine echte Lady President in Gelbgold liegt fünfstellig; 2.500 € bei reinem Versand, Konto seit 73 Tagen und drei Zeilen Beschreibung sind das Profil einer Betrugsanzeige, kein Fund.
- **Omega Seamaster Chronometer Chronograph** (3503168041, 2.400 €, uhren): Streuung 3,24. Ohne Referenznummer lässt sich das Modell nicht bestimmen, damit kein belastbarer Marktwert.
- **Tudor Prince Oysterdate Ref. 72033** (3503409342, 1.650 €, uhren): Streuung 3,56. Ohne Box und Papiere liegt eine 72033 im Bereich 1.200 bis 2.000 €, der Preis liegt mitten darin.
- **Omega Constellation Damenuhr** (3503432978, 599 €, uhren): Streuung 3,0, Quarzuhr von 1999 ohne Zertifikat. Kein Abstand nachweisbar.
- **TAG Heuer Formula 1** (3503246172, 575 €, uhren): Keine Referenznummer genannt; die Formula-1-Palette reicht von 300 bis 1.500 €, ein Marktwert ist so nicht bestimmbar.
- **Zenith El Primero Rainbow** (3503193032, 2.400 €, uhren): "kein paypal nur Banküberweisung", also Zahlung ohne Käuferschutz. Zudem widerspricht die Beschreibung (44 mm, Stahl/Gold) der bekannten Rainbow-Referenz.
- **SRAM Red AXS eTAP-Gruppe neu** (3502760286, 725 €, ebike-rad): Der Verkäufer verlangt ausdrücklich Barzahlung oder "PayPal als Freund"; dazu Streuung 3,54 und eine unvollständige Gruppe.
- **Möbel Dieter Knoll Badezimmer XXXLutz** (3476097233, 799 €, design-sammeln): Streuung 3,34, der Median mischt Einzelmöbel und Sets.
- **USM Haller, drei Anzeigen** (3502970804 600 €, 3502996723 650 €, 3502667076 800 €, design-sammeln): Streuung jeweils 3,27; der Median mischt Einzelelemente, Rollcontainer und ganze Anlagen.
- **Designer Dieter Knoll Schlafzimmer** (3503332587, 519 €), **2 Walter Knoll Sessel Classic Edition** (3503164182, 560 €), **Herman Miller Eames Fiberglas Schale** (3503237303, 180 €), **6 x Vitra Eames Plastic Armchair DAR** (3502892867, 175 €), **Stuhl Dieter Knoll Leder** (3502921843, 395 €): Streuung 3,3 bis 6,0, jeweils Mischung aus Originalen, Nachbauten, Einzelstücken und Sets.
- **Riese & Müller Charger Vario** (3502988207, 1.899 €, ebike-rad): Inhaltlich der stärkste Kandidat nach den vier gemeldeten, aber nur ein einziges konkretes Vergleichsangebot auffindbar (2.650 € VB für einen New Charger Vario mit 5.500 km, 500 Wh, Enviolo-Riemen). Zwei Belege verlangt die Regel, ein geschätzter Marktwert ist keiner.
- **Specialized Turbo Vado SL 4.0 EQ** (3502957734, 1.300 €, ebike-rad): Zu gebrauchten Vado SL 4.0 EQ waren nur Prozentangaben ("bis zu 60 Prozent unter Neupreis") und US-Neupreise zu finden, keine konkreten Euro-Vergleichsangebote.
- **Cube Kathmandu Hybrid One** (3503020245, 1.250 €, ebike-rad): Kein konkreter Gebrauchtpreis belegbar; dazu ein Fremdakku von E-Bike Vision statt des Bosch 625, was den Wert drückt.
- **Apple MacBook Pro 14" M4 16/512** (3503191647, 1.100 €, macbook): Trotz sauberer Anzeige mit Originalrechnung kein konkreter Euro-Gebrauchtpreis für genau diese Konfiguration auffindbar, nur allgemeine Refurbished-Rabattangaben.
- **MacBook Pro M2 Pro 32 GB** (3502795251, 999 €, macbook): Ohne Ladegerät, mit Delle im Displaydeckel; kein belastbarer Vergleichspreis für diese Konfiguration bestätigt.
- **Simson Schwalbe Baujahr 1975** (3503396154, 1.500 €, motorraeder): "Lange Standzeit in der Garage", zwei Zeilen Beschreibung, keine Papiere erwähnt. Ohne Papiere ist der Median von 2.700 € nicht der richtige Vergleich.
- **Simson Schwalbe Scheunenfund** (3503250572, 850 €, notverkaeufe): Streuung 2,59, Zustand unklar.
- **Mafell Erika Tischkreissäge** (3503236792, 450 €), **Hilti TE 5** (3502957865, 150 €): Streuung 3,63 beziehungsweise 3,0, kein Modelljahr.
- **Hilti TE 76-ATC Kombihammer** (3502984778, 150 €, werkzeug-maschinen): Schlagfunktion defekt, im Titel offengelegt. Der Preis ist korrekt.
- **Panasonic Lumix mit Leica Objektiv** (3502840905, 189 €, foto-sweep): Streuung 3,12, kein Modell genannt.
- **Ducati Monster** (3503278150, 3.750 €, motorraeder): Streuung 3,21, der Median mischt alle Monster-Baureihen von 600 bis 1200.
- **47 weitere Fahrräder und E-Bikes** aus `ebike-rad` mit Streuung über 2,5 oder ohne genanntes Modell und Modelljahr (unter anderem 3503264250, 3503029366, 3503328734, 3503264616, 3502956348, 3502666444, 3502777634, 3503229080, 3502919653, 3502843725, 3502860706, 3503343687): Ohne Modelljahr mischt der Median mehrere Jahrgänge desselben Namens.

### Marktwert bestätigt, aber Abstand unter 20 Prozent

- **Rolex GMT-Master II Ref. 16710 LN** (3502706175, 9.916 €, uhren): Der größte nominale Abstand des Laufs, hält der eigenen Prüfung aber nicht stand. WatchCharts weist für die 16710 einen durchschnittlichen Transaktionspreis von rund 12.400 USD (Anfang 2026) aus, das sind etwa 11.500 €, und dieser Schnitt enthält die teureren Pepsi- und Coke-Lünetten. Für die schwarze LN-Variante bleiben rund 10.000 bis 11.000 €, damit liegen 9.916 € keine 20 Prozent darunter. Dazu: Übergabe nur per Versand bei einer Uhr dieses Werts.
- **Tudor Black Bay Chrono, Baujahr 2019** (3502938796, 2.600 €, uhren): Gebrauchte 79350 liegen konkret bei 3.650 € und 3.880 €, das sind aber Händlerpreise mit Box, Papieren und Gewährleistung. Verkauft wird hier "Nur Uhr" ohne beides; privat ohne Papiere sind rund 3.000 € realistisch, damit bleibt kein sicherer 20-Prozent-Abstand. Bei einer papierlosen Tudor ist genau das die Konstellation, in der Fälschungen sitzen.
- **Tudor Black Bay Chrono 79360N, neu** (3502871597, 3.990 €, uhren): Händlerkonto seit genau einem Jahr, angeboten wird eine ungetragene 2026er Uhr unter dem üblichen Gebrauchtniveau von rund 4.300 bis 4.800 €. Kein 20-Prozent-Abstand und ein Profil, das eher nach Anzahlungsmasche als nach Fund aussieht.
- **TAG Heuer Carrera Calibre 16 Day-Date CV2A10** (3502765945, 1.650 €, uhren): Ein Komplettset ging auf dem WatchCharts-Marktplatz für 1.700 USD weg, gebrauchte CV2A10 liegen zwischen etwa 900 und 2.700 €. 1.650 € sind Marktniveau.
- **TAG Heuer Carrera Calibre 5 Day-Date** (3502640220, 1.250 €, uhren): Dieselbe Preisklasse, dasselbe Ergebnis.
- **Leica Q Typ 116** (3502866920, 2.799 €, kameras-leica): `referenz: null`. Gebrauchte Leica Q Typ 116 liegen bei etwa 2.000 bis 2.700 €; 2.799 € liegen mit dem Zubehör am oberen Rand, nicht darunter.
- **Santa Cruz Bronson A R Gr. XS** (3502816879, 1.700 €, ebike-rad): Modelljahr 2019 mit getauschter Sattelstütze und Schaltung; gebrauchte Bronson dieser Generation liegen bei 1.800 bis 2.400 €, Größe XS verkleinert den Käuferkreis zusätzlich.
- **Vitra Aluminium Chair EA 117** (3458802262, 1.000 €, design-sammeln): Original aus den 1990ern mit Patina; gebrauchte EA 117 liegen bei 800 bis 1.400 €. Der Preis liegt mitten im Markt.
- **PS5 Pro 2TB** (3502898606, 610 €, konsolen-sweep): Neupreis 799 €, gebraucht 620 bis 700 €. Kein 20-Prozent-Abstand.
- **DJI Mini 5 Pro** (3502915839, 600 €, optik-drohnen): Neu 799 €, gebraucht 650 bis 700 €. Wie beim Kandidaten vom 3. September kein Fund.
- **Cube Ebike / Reaction Hybrid Baujahr 2017** (3502810524, 600 €, ebike-rad): Neuer Motor 2019, Akku 2024, Bremsen 2026 — inhaltlich plausibel, aber der Median stützt sich auf nur acht Anzeigen und ein konkreter Gebrauchtpreis für ein Reaction Hybrid von 2017 war nicht zu belegen.

### Anzeige selbst spricht dagegen

- **Cluster "MacBook Pro M5" zu Tiefstpreisen** (3503396226 1.000 €, 3502667365 1.299 €, 3503375286 1.399 €, 3503393262 1.499 €, macbook): Vier Anzeigen desselben Musters innerhalb von 24 Stunden — generische, maschinell klingende Beschreibungen ohne Seriennummer, Prozessor als "Sonstiger Prozessor" hinterlegt, überwiegend reiner Versand. Bei 3503375286 sagt der Titel MacBook Pro M5 und die Beschreibung MacBook Air; bei 3503396226 erwähnt der Text den M5 überhaupt nicht. Ein Marktwert wurde hier nicht gegengeprüft, weil die Anzeigen selbst nicht tragen.
- **Apple MacBook Pro 14,2" M5 32/1 TB, neu** (3503447907, 2.250 €, macbook): Neu und originalverpackt; die Apple-Konfiguration liegt bei rund 2.500 €, damit unter 20 Prozent Abstand.

## Anmerkung zum Lauf

Die Warteschlange war mit 163 Kandidaten die längste bisher, aber inhaltlich dünn: 47 Einträge waren Fahrräder ohne Modelljahr, 37 iPhones mit Ersparnissen unter 200 € und 21 Designmöbel mit Streuungen über 3. Die vier Meldungen kommen aus vier verschiedenen Kategorien; keine trägt den Unkenntnis-Bonus. Der einzige Kandidat mit Bonus (3503343687, Rennrad von Trek, 450 €) wurde nicht wegen der Anzeigenqualität verworfen, sondern weil ein zehn Jahre altes Trek One Series 1.5 mit Tiagra gebraucht bei 350 bis 550 € liegt.
