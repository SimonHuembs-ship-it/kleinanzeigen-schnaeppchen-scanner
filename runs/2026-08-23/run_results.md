# Laufprotokoll 2026-08-23, Morgenlauf

**Lauf:** 23. August 2026, 07:05 Uhr (MESZ)
**candidates.json generiert:** 2026-08-23T06:38:37+02:00 (rund 27 Minuten alt, innerhalb der Frist von vier Stunden)
**Zeitraum der Sammlung:** 2026-08-23T01:27:19+02:00 bis 2026-08-23T06:27:19+02:00
**Gesichtete Anzeigen:** 19.172
**Kandidaten in candidates.json:** 189
**Bereits in deal_log.csv (verworfen vor Pruefung):** 0
**Zu pruefende Kandidaten:** 189
**Gemeldete Funde:** 0

## Funde

Keine. Kein Kandidat hat die Pruefung nach prompt.md Schritt 2 bestanden.

Damit bleiben `deals.json`, `email_output.html` und `deal_log.csv` unveraendert, und es wird keine
Mail ausgeloest. Nur dieses Laufprotokoll wird nach `main` gepusht.

## Warum dieser Lauf leer ausgeht

Die sechs Kandidaten mit dem groessten absoluten Abstand sind einzeln und mit externer
Marktwertpruefung geprueft worden. Alle sechs scheitern, und zwar an vier unterschiedlichen
Gruenden, die zusammen den Datensatz gut beschreiben:

**Der Median ist ein Markendurchschnitt.** Der Porsche fuer 29.999 EUR (rechnerisch 29.311 EUR
Abstand, der groesste des Laufs) ist ein 996.2 Carrera Cabrio von 2004 mit 212.000 km. Der Median
von 59.310 EUR stammt aus 97 Anzeigen zu "Porsche Carrera Cabrio" und enthaelt 997, 991 und 992.
prompt.md verlangt fuer Porsche ausdruecklich den Median der exakten Generation, nie einen
Markendurchschnitt. Fuer einen 996 Cabrio mit dieser Laufleistung ist der Preis marktgerecht.

**Der bestaetigte Marktwert liegt naeher am Angebot als der Median.** Die beiden grossen Rolex
sind die einzigen Kandidaten, bei denen sich der Marktwert extern sauber belegen liess - und genau
das hat sie ausgeschieden. Die Yacht-Master II 116680 in Stahl handelt gebraucht bei 14.590 bis
16.600 EUR, Fullset-Exemplare bei 15.950 bis 16.500 EUR; das Angebot liegt bei 15.490 EUR, also
mitten im Korridor statt 20 Prozent darunter. Die Sky-Dweller in Stahl handelt bei 14.500 bis
21.000 EUR, das Angebot liegt bei 14.300 EUR, also am unteren Rand. In beiden Faellen war der
Kleinanzeigen-Median (28.875 bzw. 22.550 EUR) die Phantomgroesse, nicht der Angebotspreis.

**Der niedrige Preis erklaert sich selbst.** Das Tesla Model 3 Long Range fuer 15.900 EUR traegt im
Attributfeld 249 km und in der Beschreibung 249.000 km. Bei dieser Laufleistung sind beide Grenzen
der Akkugarantie (8 Jahre, 192.000 km) ueberschritten. Dasselbe Muster beim W124 Cabrio
(als Unfallfahrzeug inseriert, Korrosion, defekte Stossstangen) und quer durch die gesamte
iPhone-Gruppe, die ihre Displayrisse, Wasserschaeden und defekten Face-ID-Module selbst benennt.

**Das Betrugsprofil aus der Leitidee.** Das Tesla Model X fuer 16.500 EUR kommt von einem
gewerblichen Konto, das seit dreizehn Tagen existiert, mit Telefonnummer statt Beschreibung und
einem Datenbankauszug als Ausstattungsliste. Dazu kommen an diesem Tag: eine originalversiegelte
DJI Mini 5 Pro fuer 540 EUR bei 968 bis 990 EUR Neupreis, deren Beschreibungstext den
Herstellernamen kein einziges Mal nennt und die Drohne als Gewinnspielgewinn ausgibt; ein iPhone 17
fuer 549 EUR von einem am selben Tag angelegten Konto; eine PS5 Pro 2 TB von einem Konto vom Vortag
mit "Ich verkaufe dringend wegen meiner finanziellen Schwierigkeiten"; und ein versiegeltes
MacBook Pro M5 Pro von einem Konto mit Bewertung 0,42, nur gegen Versand. Alle vier sind
handwerklich saubere Anzeigen. Genau das ist das Signal.

## Methodische Hinweise zu diesem Lauf

- Priorisiert wurde nach absolutem Abstand und liquider Ware. Einzeln und mit Volltext geprueft
  wurden saemtliche Kandidaten der Kategorien Uhren, Tesla, Porsche, Youngtimer, Motorraeder,
  Apple, Drohnen, Konsolen, HiFi, Musikinstrumente, Werkzeug, Design und Notverkaeufe sowie alle
  uebrigen Kandidaten mit einem rechnerischen Abstand ueber 400 EUR. Fuer die restlichen Fahrraeder
  wurde die Referenzgruppe gegen Titel, Attribute und Beschreibung gehalten.
- Externe Marktwertpruefung per Websuche fuer alle Kandidaten ueber 1.000 EUR. **Einschraenkung
  dieses Laufs:** hifishark.com, laut prompt.md die Referenzquelle fuer HiFi und Studio, ist vom
  Netzwerk-Proxy blockiert (EGRESS_BLOCKED). Der Accuphase E-307 mit AD-9 fuer 2.400 EUR
  (kein Kleinanzeigen-Median) konnte deshalb nicht belastbar bewertet werden und wurde verworfen,
  statt einen Wert zu schaetzen. Dasselbe gilt fuer die Weiler Condor Drehmaschine fuer 4.200 EUR:
  Maschinensucher und Resale fuehren dieses Modell ausschliesslich mit "Preis auf Anfrage".
- Der einzige Kandidat mit `unkenntnis_bonus` (3491146900, Altsaxophon Yanagisawa, 999 EUR) wurde
  nicht nach Anzeigenqualitaet abgewertet. Er scheitert an etwas anderem: Verkaeufer ist ein
  Blaeserfachgeschaeft, das seinen eigenen Bestand einpreist, und die Anzeige nennt ausser einer
  Seriennummer keine Modellbezeichnung. Yanagisawa-Altsaxophone reichen vom Einsteiger- bis zum
  Profimodell; ohne Modell kein Marktwert.
- Wiederkehrende Referenzgruppen-Fallen in diesem Datensatz: der Simson-Block (Motorruempfe und
  Ersatzteilkonvolute gegen einen Median aus kompletten Mopeds; und bei fuenf der sieben
  fahrbereiten Simson fehlen die Papiere - bei dieser Baureihe der zentrale Wertfaktor, analog zur
  Regel fuer Klassiker ohne Zulassungsbescheinigung Teil II), der USM-Haller-Block (ein Median ueber
  alle Groessen und Konfigurationen, waehrend genau die Konfiguration den Preis macht) und der
  Cube-Block bei den Fahrraedern (99 Anzeigen unter einem Suchwort, ueber zehn Modelljahre hinweg).
- Zwei Anzeigen sind wortgleiche Duplikate desselben Kontos (3491662621 und 3492027923, Simson S51
  Neuaufbau fuer 1.950 EUR, Konto drei Wochen alt, Versand mit Kaeuferschutz angeboten). Das ist
  das Muster der bekannten Simson-Betrugswelle und war der Grund fuer die Verwerfung, nicht der
  ansonsten sorgfaeltig beschriebene Aufbau.

## Verworfene Kandidaten (189)

- **3491851919 — Porsche  Carrera Cabrio  Tausch möglich** (29999 EUR, rechnerischer Abstand 29311 EUR, porsche-911): Der Median mischt alle 911-Generationen (997/991/992) zu einem Markendurchschnitt; das Fahrzeug ist ein 996.2 Cabrio mit 212.000 km, fuer den 29.999 EUR marktgerecht sind. Kein einziges Bild in den Daten.
- **3491130596 — Original Rolex Yachtmaster 2 Uhr Herrenuhr Full Set** (15490 EUR, rechnerischer Abstand 13385 EUR, uhren): Bestaetigtes Marktniveau der Yacht-Master II 116680 in Stahl: 14.590 bis 16.600 EUR (Chrono24), Fullset-Exemplare 15.950 bis 16.500 EUR. 15.490 EUR liegen mitten in diesem Korridor, der Abstand betraegt keine 20 Prozent. Der Median von 28.875 EUR ist eine Phantomgroesse.
- **3491970281 — Tesla Model X Dual** (16500 EUR, rechnerischer Abstand 10270 EUR, tesla): Gewerbliches Konto seit 13 Tagen, Telefonnummer statt Beschreibung, Standard-Datenbankauszug eines Haendlersystems - das polierte Profil aus der Leitidee. Ein belastbarer Marktwert fuer den Model X 90D von 2018 mit 106.551 km liess sich nicht belegen. Tesla-Warnflag: Akkugarantie des Model X (240.000 km / 8 Jahre) laeuft im September 2026 aus.
- **3491214890 — Rolex Skydweller** (14300 EUR, rechnerischer Abstand 8250 EUR, uhren): Referenz unbelastbar (Streuung 3,26). Bestaetigtes Marktniveau der Sky-Dweller in Stahl: 14.500 bis 21.000 EUR; 14.300 EUR liegen am unteren Rand, nicht 20 Prozent darunter. Zifferblatt- und Bandvariante sind aus der Anzeige nicht bestimmbar, sie bewegen den Wert um mehrere Tausend Euro.
- **3491726519 — Tesla Model 3 Long Range AWD** (15900 EUR, rechnerischer Abstand 7500 EUR, tesla): Das Attributfeld nennt 249 km, die Beschreibung 249.000 km. Bei dieser Laufleistung sind sowohl die 8-Jahres- als auch die 192.000-km-Grenze der Akkugarantie des Model 3 Long Range ueberschritten. Die hohe Laufleistung erklaert den Preis - kein Fund, sondern ein korrekt bepreistes Angebot.
- **3491583916 — Mercedes-Benz Cabrio W124, E 200** (8700 EUR, rechnerischer Abstand 7050 EUR, youngtimer-alltag): Als beschaedigtes Unfallfahrzeug inseriert: Stossstangen vorn und hinten defekt, Lackabloesung, Korrosion, Gurtbringer und Radio ohne Funktion. Restaurationsbeduerftig - der Preis erklaert sich selbst.
- **3491267174 — BMW 320i E30** (9150 EUR, rechnerischer Abstand 5205 EUR, youngtimer-alltag): 263.000 km, sechs Vorbesitzer, kein TUEV, Fensterheber ohne Funktion. Der Zustand erklaert den Preis.
- **3491762938 — Rolex Submariner mit Original-Papieren** (8000 EUR, rechnerischer Abstand 4245 EUR, uhren): Beschreibung besteht aus einem Satz ohne Referenznummer, Baujahr oder Ausstattung; Papiere werden nur im Titel behauptet. Ohne bestimmbares Modell (14060, 16610, 116610 oder 124060 unterscheiden sich um mehrere Tausend Euro) laesst sich kein Marktwert bestaetigen.
- **3491767420 — Mercedes 280 SE W126** (4490 EUR, rechnerischer Abstand 4082 EUR, youngtimer-alltag): Restaurationsobjekt: seit 2006 abgemeldet, hintere Radlaeufe muessen geschweisst werden, Kotfluegel liegen unlackiert bei. Der Zustand erklaert den Preis.
- **3491394677 — Weiler Condor Drehmaschine mit Heidenhain Anzeige & Multifix B** (4200 EUR, rechnerischer Abstand 4060 EUR, werkzeug-maschinen): Referenz unbelastbar (Streuung 4,24, nur 10 Anzeigen). Fuer die Weiler Condor werden auf Maschinensucher und Resale ausschliesslich Preise auf Anfrage gefuehrt; ein belastbarer Marktwert liess sich nicht belegen und wird hier nicht geschaetzt.
- **1875648068 — Rolex Submariner "No Date" Oyster Perpetual Edelstahl-Chronometer** (7595 EUR, rechnerischer Abstand 3555 EUR, uhren): Ref. 14060 von 1991/92: bestaetigtes Marktniveau rund 7.000 bis 9.000 EUR, 7.595 EUR vom Haendler mit einem Jahr Gewaehrleistung sind Marktpreis. Zusaetzlich ein Widerspruch in der Anzeige: die 14060 von 1991 traegt Kaliber 3000, das genannte Kaliber 3130 kam erst mit der 14060M.
- **3491527313 — Honda CB 750 four K** (3500 EUR, rechnerischer Abstand 2710 EUR, motorraeder): Referenz unbelastbar (Streuung 2,82). TUEV seit 2023 abgelaufen, drei Jahre Standzeit, abgemeldet - 3.500 EUR liegen im Korridor fuer eine CB 750 Four mit Standschaeden.
- **3491786377 — Honda cb 750 Four supersport** (3600 EUR, rechnerischer Abstand 2610 EUR, motorraeder): Referenz unbelastbar (Streuung 2,82). TUEV abgelaufen, Zustand nur pauschal beschrieben; kein belegbarer Abstand.
- **3491779793 — Bmw E36 320i** (4200 EUR, rechnerischer Abstand 2550 EUR, youngtimer-alltag): Als Unfall- und nicht fahrbereites Fahrzeug im Kaufvertrag vermerkt, geschweisstes Differenzial, Rost und Dellen. Der Preis erklaert sich selbst.
- **3491802375 — Neue Omega seamaster Professional 300M Diver** (2600 EUR, rechnerischer Abstand 2544 EUR, uhren): Die Bezeichnung Seamaster Professional 300M deckt sowohl die alten Referenzen 2531.80/2254.50 (Gebrauchtniveau rund 2.000 bis 3.000 EUR) als auch das aktuelle Modell ab; die Anzeige nennt keine Referenz. Fuer die alte Referenz waeren 2.600 EUR Marktpreis.
- **3491996683 — Cube Stereo Actionteam** (1100 EUR, rechnerischer Abstand 2350 EUR, ebike-rad): Titel nennt die Topausstattung Actionteam, die Beschreibung ein Stereo 120 mit 27,5-Zoll-Laufraedern und Magura-Bremsen. Der Median stammt aus Actionteam-Anzeigen und passt nicht zum beschriebenen Rad; 1.100 EUR sind fuer ein aelteres Stereo 120 marktgerecht.
- **3491986568 — Mercedes w124 oldtimer** (4200 EUR, rechnerischer Abstand 2190 EUR, youngtimer-alltag): 263.000 km, abgemeldet, keine Probefahrt moeglich. Fuer einen W124 mit dieser Laufleistung sind 4.200 EUR marktgerecht.
- **3491602743 — ROLEX OYSTER  PERPETUAL DATE " 34MM " AUTOMATİK** (3211 EUR, rechnerischer Abstand 2129 EUR, uhren): Die genannte 'Referenznummer 902-B 0381' existiert bei Rolex nicht, der Text traegt Merkmale maschineller Uebersetzung (tuerkisches i in AUTOMATIK, Katalogfloskeln), Konto juenger als sechs Monate, nur Versand. Verdacht auf Faelschung - verworfen, nicht gemeldet.
- **3491158119 — Ghost E-Bike mit Bosch CX Motor, Gepäckträger & Licht** (750 EUR, rechnerischer Abstand 2049 EUR, ebike-rad): Weder Modell noch Baujahr noch Akkukapazitaet genannt, Referenzgruppe 'Ghost Bike Bosch' mischt alle Ghost-Pedelecs. 10.500 km Laufleistung, bei der Akkualterung der zentrale Wertfaktor - 750 EUR sind dafuer plausibel.
- **3491662621 — Simson S51 - 12V Vape - Neuaufbau** (1950 EUR, rechnerischer Abstand 2032 EUR, motorraeder): Fachgerechter Neuaufbau, aber: identische Anzeige zweimal parallel eingestellt (3492027923), Konto drei Wochen alt, Versand mit Kaeuferschutz angeboten, Preis rund 50 Prozent unter dem Niveau restaurierter S51. Das Muster ist das der bekannten Simson-Betrugswelle.
- **3492027923 — Simson S51 - 12V Vape - Neuaufbau** (1950 EUR, rechnerischer Abstand 2032 EUR, motorraeder): Wortgleiches Duplikat von 3491662621 desselben Kontos - siehe dort.
- **3491673080 — Simson s50/s51** (1000 EUR, rechnerischer Abstand 1966 EUR, motorraeder): Simson Cross ohne Nummer und ohne Plakette, Vergaser muss eingestellt werden. Fehlende Papiere sind bei Simson der zentrale Wertfaktor; der Median besteht aus Fahrzeugen mit Papieren.
- **3491619054 — Rolex Datejust 36 Sunburst Dial Weißgold Lünette 1601** (3900 EUR, rechnerischer Abstand 1920 EUR, uhren): Ohne Papiere, Konto juenger als sechs Monate, nur Versand. Fuer eine Datejust 1601 im Originalzustand ohne Papiere sind 3.900 EUR marktgerecht, das 25-Prozent-Quartil liegt bei 4.000 EUR.
- **3492012069 — Canyon speedmax CF 8 M Grau Triathlon Rennrad** (1899 EUR, rechnerischer Abstand 1791 EUR, ebike-rad): Referenz unbelastbar (Streuung 2,73). Felgenbremsen und Shimano 105 datieren das Speedmax CF 8 auf die aeltere Generation, deren Gebrauchtniveau bei etwa 1.800 bis 2.300 EUR liegt - 1.899 EUR sind Marktpreis.
- **3491330396 — Simson S51 Motor 4 Gang überholt Motorrumpf Megu Mza** (680 EUR, rechnerischer Abstand 1570 EUR, motorraeder): Angeboten wird ein ueberholter Motorrumpf, der Median besteht aus kompletten Mopeds. Referenzgruppe passt nicht.
- **3491547314 — Mercedes Benz W124 230E** (3500 EUR, rechnerischer Abstand 1540 EUR, youngtimer-alltag): Roststellen und mattierter Lack offengelegt, 199.266 km; 3.500 EUR liegen dicht am 25-Prozent-Quartil von 3.700 EUR.
- **3492003821 — Tudor Oyster Prince Tuxedo** (1200 EUR, rechnerischer Abstand 1540 EUR, uhren): Der offengelegte Fehler am Kronaufzug ist ein realer Mangel, der den Preis mittraegt. Fuer die Kombination Oyster Prince mit Tuxedo-Zifferblatt aus den 1950ern liess sich kein belastbarer Vergleichswert mit zwei konkreten Angeboten desselben Zifferblatts finden.
- **3491871311 — Simson S50 zu verkaufen** (1800 EUR, rechnerischer Abstand 1462 EUR, motorraeder): Keine Papiere vorhanden, Elektrik ungeprueft, als Winterprojekt inseriert.
- **3491979588 — Simson Schwalbe KR51/2 ,vape,motor neu  4 gang** (1800 EUR, rechnerischer Abstand 1350 EUR, motorraeder): Verkaeuferbewertung 0,25. Der Neuaufbau ist detailliert beschrieben, aber zu Papieren schweigt die Anzeige - bei Simson der entscheidende Punkt.
- **3442318790 — BMC URS 01 Three** (2390 EUR, rechnerischer Abstand 1309 EUR, modellbau-sammler): Gewerblicher Radhaendler; 2.390 EUR fuer ein URS 01 Three von 2022 entsprechen dem Haendlerniveau fuer dieses Modell.
- **3491146900 — Altsaxophon Yanagisawa** (999 EUR, rechnerischer Abstand 1101 EUR, musikinstrumente): Kandidat mit unkenntnis_bonus, deshalb nicht nach Anzeigenqualitaet abgewertet. Referenz unbelastbar (Streuung 9,17). Die Anzeige nennt nur eine Seriennummer, keine Modellbezeichnung; Yanagisawa-Altsaxophone reichen vom Einsteigermodell bis zur Profiserie. Ohne Modell kein Marktwert - und ein Blaeserfachgeschaeft, das seinen eigenen Bestand einpreist, ist keine Unkenntnisquelle.
- **3491490800 — Apple MacBook Pro 14,2 Zoll – M5 Pro – 24 GB RAM – 1 TB SSD** (2399 EUR, rechnerischer Abstand 1100 EUR, macbook): Originalversiegeltes Neugeraet, ausschliesslich Versand, Verkaeuferbewertung 0,42. Ein versiegeltes Topmodell 25 Prozent unter Neupreis vom Privatkonto ohne Abholmoeglichkeit ist das Betrugsprofil, nicht das Profil eines ehrlichen Verkaeufers.
- **3491994933 — E-Bike Hercules Futura Comp I-10, Bosch CX Motor, wenig Kilometer** (1350 EUR, rechnerischer Abstand 1100 EUR, ebike-rad): Der Median aus 17 Anzeigen mischt verschiedene Futura-Varianten. Fuer das Comp I-10 liessen sich keine zwei konkreten Vergleichsangebote derselben Ausstattung belegen; 1.350 EUR liegen im plausiblen Korridor gebrauchter Bosch-CX-Trekkingraeder.
- **3491703598 — Simson Schwalbe KR 51/1 Ersatzteile Konvolut für Neuaufbau** (1500 EUR, rechnerischer Abstand 1020 EUR, motorraeder): Ersatzteilkonvolut, kein fahrbereites Fahrzeug; der Median besteht aus kompletten Schwalben. Referenzgruppe passt nicht.
- **3491119801 — Gibson Les Paul Junior** (1500 EUR, rechnerischer Abstand 1000 EUR, musikinstrumente): Referenz unbelastbar (Streuung 3,23), der Median mischt die gesamte Les-Paul-Palette. Fuer die Les Paul Junior 100th Anniversary von 2015 liegt das Gebrauchtniveau unter dem Angebotspreis von 1.500 EUR.
- **3491432998 — Simson S51** (2150 EUR, rechnerischer Abstand 1000 EUR, motorraeder): Ohne Papiere; Typenschild und Rahmennummer passen zwar, aber die Neubeantragung ist Aufwand und Risiko des Kaeufers.
- **3491453343 — cube reaction Mountainbike 29 Zoll xt** (350 EUR, rechnerischer Abstand 999 EUR, ebike-rad): Referenz unbelastbar (Streuung 2,79). Beschriebene Ausstattung (3x10 XT, RockShox SID, DT Swiss) datiert das Rad auf etwa 2013 bis 2015; 350 EUR sind dafuer Marktpreis.
- **3491702883 — Simson S50 N** (1900 EUR, rechnerischer Abstand 979 EUR, motorraeder): Ohne Papiere, Zustand nur pauschal beschrieben.
- **3492037402 — Apple macbook pro .top letzte version  neue 2023** (330 EUR, rechnerischer Abstand 920 EUR, macbook): Weder Baujahr noch Chip, Bildschirmgroesse oder Speicher genannt; 'letzte Version neue 2023' widerspricht sich. Ohne bestimmbares Modell kein Marktwert.
- **3491505107 — Simson Schwalbe kr51/ 1 K** (1600 EUR, rechnerischer Abstand 920 EUR, motorraeder): Sollte komplett ueberarbeitet werden, seit 2001 nicht mehr im Verkehr; 1.600 EUR liegen unter dem 25-Prozent-Quartil von 2.490 EUR, aber der Ueberholungsbedarf erklaert den Abstand.
- **3491293086 — Cassina / Magistretti Sofa Fiandra** (900 EUR, rechnerischer Abstand 890 EUR, design-sammeln): Gewerblicher Anbieter, Referenz unbelastbar (Streuung 3,0); Bezugsstoff mit Patina im Originalzustand - 900 EUR sind fuer ein Fiandra in diesem Zustand marktgerecht.
- **3491160805 — Cube Stereo Race HPA – E-Bike** (1350 EUR, rechnerischer Abstand 850 EUR, ebike-rad): 17.000 km Laufleistung am Bosch-CX-Antrieb plus defekter Seilzug der Sattelstuetze. Die Laufleistung erklaert den Preis.
- **3491155833 — simson star sr 4-2** (1400 EUR, rechnerischer Abstand 841 EUR, motorraeder): Keine Papiere mehr vorhanden, lange Standzeit, springt nur kurz an.
- **3491961135 — Yanmar, Dieselmotor, Motor** (1500 EUR, rechnerischer Abstand 829 EUR, camper-marine): Gebrochener Kolben im ersten Zylinder. Defekt erklaert den Preis.
- **3491168653 — mafell Erika 85** (1150 EUR, rechnerischer Abstand 800 EUR, werkzeug-maschinen): Wackler in der Elektronik offengelegt; Referenz unbelastbar (Streuung 3,66). Der Mangel erklaert den Abstand.
- **3491100161 — E bike Greens Bosch Performance Rücktrittbremse** (1150 EUR, rechnerischer Abstand 800 EUR, ebike-rad): Greens ist eine Haus-/Budgetmarke ohne belastbaren Zweitmarkt; der behauptete Neupreis von 3.000 EUR ist nicht ueberpruefbar. 1.150 EUR liegen im plausiblen Korridor.
- **3491166382 — Cube Stereo Fully 140 HPC - Race 27.5 - Carbon - Größe M** (660 EUR, rechnerischer Abstand 760 EUR, ebike-rad): Der Verkaeufer nennt selbst einen moeglichen Riss im Carbonrahmen und schreibt, der Preis sei deshalb angepasst. Der niedrige Preis erklaert sich vollstaendig.
- **3491137013 — Fully Canyon Neuron XS** (950 EUR, rechnerischer Abstand 700 EUR, ebike-rad): Beschreibung enthaelt ausser einer Kontaktaufforderung keine Angabe; Modelljahr und Ausstattung des Neuron sind unbekannt, damit kein Marktwert bestaetigbar.
- **3491978809 — Truma Mover Smart A mit Truma Mover Powerset** (1499 EUR, rechnerischer Abstand 700 EUR, camper-marine): Referenz unbelastbar (Streuung 10,2), der Median mischt komplette Mover-Sets mit Einzelteilen. Ein belastbares Gebrauchtniveau fuer Mover Smart A plus Powerset liess sich nicht belegen.
- **3492002154 — Macbook pro M4** (1250 EUR, rechnerischer Abstand 700 EUR, macbook): Chip-Generation, Baujahr oder Speicherausstattung sind aus der Anzeige nicht eindeutig ableitbar, damit kein bestaetigter Marktwert.
- **3491597139 — Original USM Haller - Designklassiker auf Rollen** (650 EUR, rechnerischer Abstand 699 EUR, design-sammeln): Referenz unbelastbar (Streuung 3,61), ein Bild, Masse fehlen. USM-Preise haengen vollstaendig an der Konfiguration.
- **3491354140 — Gibson Les Paul Studio Thin Body 1995 - Ebony** (1170 EUR, rechnerischer Abstand 680 EUR, musikinstrumente): Tailpiece und Tonabnehmer ausgetauscht - wertmindernde Umbauten an einer 1995er Les Paul Studio. Referenz unbelastbar (Streuung 3,18).
- **2778957565 — USM Haller Sideboard Weiß Perforiert** (773 EUR, rechnerischer Abstand 654 EUR, design-sammeln): Gewerblicher Anbieter mit Bruttopreisauszeichnung; der Median mischt alle Sideboard-Groessen.
- **3491215814 — Original Vitra Eams Bürostuhl in rot** (600 EUR, rechnerischer Abstand 650 EUR, design-sammeln): Referenz unbelastbar (Streuung 3,08); die Anzeige nennt weder Modellreihe noch Baujahr des Vitra-Stuhls.
- **3491178902 — Cube Cross Race Pro 56 Gravel** (850 EUR, rechnerischer Abstand 649 EUR, ebike-rad): 850 EUR liegen praktisch auf dem 25-Prozent-Quartil von 870 EUR; kein Abstand von 20 Prozent zu einem bestaetigten Marktwert.
- **3491156483 — Fahrrad Cube Cube Kathmandu Hybrid Pro 625** (1150 EUR, rechnerischer Abstand 612 EUR, ebike-rad): Das Kathmandu Hybrid Pro 625 wird je nach Modelljahr und Laufleistung sehr unterschiedlich gehandelt; die Laufleistungsangabe bricht im Text ab. Zwei konkrete Vergleichsangebote derselben Generation liessen sich nicht belegen.
- **3491676406 — Apple MacBook Pro (2023) Laptop 1TB** (750 EUR, rechnerischer Abstand 600 EUR, macbook): Chip-Generation, Baujahr oder Speicherausstattung sind aus der Anzeige nicht eindeutig ableitbar, damit kein bestaetigter Marktwert.
- **3491186055 — Trek Carbon Rennrad mit Shimano Ultegra Ausstattung** (700 EUR, rechnerischer Abstand 599 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 4.0). Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 650 EUR.
- **3491628133 — USM Haller Lowboard Schwarz mit Einschubtüre + Rollen** (550 EUR, rechnerischer Abstand 550 EUR, design-sammeln): Der Median 'USM Haller Lowboard' mischt alle Breiten und Tuerkonfigurationen; Gebrauchsspuren offengelegt.
- **3199203931 — Usm Haller Sideboard schwarz** (950 EUR, rechnerischer Abstand 537 EUR, design-sammeln): Gewerblicher Anbieter, Bruttopreis, marktuebliches Haendlerniveau fuer diese Masse.
- **3199210234 — Usm Haller Sideboard Schwarz** (919 EUR, rechnerischer Abstand 530 EUR, design-sammeln): Gewerblicher Anbieter, gleiche Quelle wie 3199203931, marktuebliches Haendlerniveau.
- **3491164010 — Cube Cross Race** (800 EUR, rechnerischer Abstand 514 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491151645 — Cube Nuroad Pro Gravelbike, 56 cm / M, Metalblack'n Grey** (790 EUR, rechnerischer Abstand 509 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3362837638 — Walter Knoll Sessel Leder schwarz** (499 EUR, rechnerischer Abstand 501 EUR, design-sammeln): Referenz unbelastbar (Streuung 3,18); 'Walter Knoll Sessel' umfasst Modelle von 300 bis mehreren Tausend Euro.
- **3492013729 — iPhone 17 256** (549 EUR, rechnerischer Abstand 500 EUR, apple-mobil): Konto am Tag der Anzeige angelegt, 549 EUR fuer ein iPhone 17 mit bestaetigtem Gebrauchtniveau um 850 bis 950 EUR. Der Abstand ist zu gross fuer ein gepflegtes Geraet mit 93 Prozent Akku und passt zum Profil eines Neukontos.
- **3491186088 — Fender Jazz Bass American Special Made in usa Vintage** (900 EUR, rechnerischer Abstand 495 EUR, musikinstrumente): Referenz unbelastbar (Streuung 3,58); Verkaeuferbewertung 0,47. Fuer einen American Special Jazz Bass von 2011 sind 900 EUR Marktpreis.
- **3491157838 — TAG HEUER Professional 1000** (700 EUR, rechnerischer Abstand 490 EUR, uhren): Ein Bild, sichtbare Gebrauchsspuren, keine Referenznummer. 700 EUR liegen unter dem 25-Prozent-Quartil von 850 EUR - fuer eine getragene Professional 1000 ist das Marktpreis.
- **3491263516 — ​Pegasus Solero SL 24-Gang Trekkingrad / Damenrad (28 Zoll)** (320 EUR, rechnerischer Abstand 479 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491765267 — USM Haller Sideboard Regal weiß** (950 EUR, rechnerischer Abstand 476 EUR, design-sammeln): Verkaeuferbewertung 0,43, nur Versand, Beschreibung aus zwei Zeilen mit Tippfehler im Produktnamen; Konfiguration nicht pruefbar.
- **3492017357 — Gravel-Bike Cube Road/Nuroad SL Gr. 56** (680 EUR, rechnerischer Abstand 469 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 3.07).
- **3491115988 — Canyon Fully Mountainbike 29 Zoll Größe M - Allmountain-Trail** (895 EUR, rechnerischer Abstand 455 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491461916 — USM Haller TV/HIFI Board** (800 EUR, rechnerischer Abstand 450 EUR, design-sammeln): Zwei Maengel an den Klappen offengelegt - der Abstand zum Median erklaert sich damit.
- **3491131838 — Trekking Fahrrad** (350 EUR, rechnerischer Abstand 440 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491427032 — Thonet S32 Freischwinger Original Bauhaus Buche Chrom Rohrgeflech** (250 EUR, rechnerischer Abstand 439 EUR, design-sammeln): Originaler S 32 mit Brandstempel, aber gebrauchte Originale werden regelmaessig zwischen 250 und 450 EUR gehandelt; 250 EUR sind der untere Rand des Marktes, kein Fund darunter.
- **3491493227 — Thonet Tisch ausziehbar mit Rollen** (220 EUR, rechnerischer Abstand 430 EUR, design-sammeln): Modell und Baujahr des Thonet-Tisches nicht genannt; der Median mischt alle ausziehbaren Thonet-Tische.
- **3491571811 — Ortler E-Bike mit Bosch Active Line - fahrbereit** (500 EUR, rechnerischer Abstand 418 EUR, ebike-rad): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 480 EUR.
- **3491400446 — DJI Mini 5 Pro Fly More Combo (DJI RC 2) Kameradrohne** (540 EUR, rechnerischer Abstand 409 EUR, optik-drohnen): Bestaetigter Neupreis des Fly More Combo (RC 2): 968 bis 990 EUR. 540 EUR fuer ein originalversiegeltes Neugeraet, nur Versand, kein Modellname im Beschreibungstext, Herkunft 'aus einem Gewinnspiel' - das ist das handwerklich saubere Betrugsprofil aus der Leitidee, kein Fund.
- **3491106776 — Omlet Eglu Cube + kleiner Omlet mit elektronischer Hühnerklappe** (450 EUR, rechnerischer Abstand 400 EUR, ebike-rad): Huehnerstall in der Kategorie ebike-rad - der Median stammt aus einer voellig anderen Warengruppe. Referenz wertlos.
- **3491404169 — Apple MacBook Pro 16” M1 32GB RAM 512GB SSD** (899 EUR, rechnerischer Abstand 400 EUR, macbook): Akkuzustand in der anzeige offengelegt und eingepreist. Chip-Generation, Baujahr oder Speicherausstattung sind aus der Anzeige nicht eindeutig ableitbar, damit kein bestaetigter Marktwert.
- **3491640679 — Apple MacBook Pro Space Gray mit OVP und Zubehör** (499 EUR, rechnerischer Abstand 400 EUR, macbook): Chip-Generation, Baujahr oder Speicherausstattung sind aus der Anzeige nicht eindeutig ableitbar, damit kein bestaetigter Marktwert. Referenz unbelastbar (Streuung 4.2). Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 450 EUR.
- **3491693178 — Trek Fahrrad 29 Zoll – Türkis – Rahmengröße M/L** (300 EUR, rechnerischer Abstand 400 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 3.01).
- **3491511905 — USM Haller Tisch 200 x 100, perlgrau, gebraucht** (200 EUR, rechnerischer Abstand 395 EUR, design-sammeln): 200 EUR fuer eine 200x100-Platte mit leichten Beschaedigungen; ein bestaetigtes Vergleichsniveau fuer genau diese Groesse und Farbe liess sich nicht belegen.
- **3491655988 — Cube Mountainbike** (300 EUR, rechnerischer Abstand 374 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 6.18).
- **3491084689 — Apple MacBook Air** (380 EUR, rechnerischer Abstand 367 EUR, macbook): Akkuzustand in der anzeige offengelegt und eingepreist. Chip-Generation, Baujahr oder Speicherausstattung sind aus der Anzeige nicht eindeutig ableitbar, damit kein bestaetigter Marktwert.
- **3469659007 — VITRA 4x Eames Plastic Side Chair DSR Stuhl, Setpreis** (460 EUR, rechnerischer Abstand 365 EUR, design-sammeln): Alle vier Stuehle sind an der hinteren Beinbefestigung eingerissen. Der Defekt erklaert den Preis.
- **3491547550 — Fahrrad Trekking Bike Herren** (550 EUR, rechnerischer Abstand 360 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 3.5). Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 500 EUR.
- **3492033383 — MacBook Pro** (450 EUR, rechnerischer Abstand 358 EUR, macbook): Chip-Generation, Baujahr oder Speicherausstattung sind aus der Anzeige nicht eindeutig ableitbar, damit kein bestaetigter Marktwert. Referenz unbelastbar (Streuung 4.44). Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 450 EUR.
- **3491182352 — Cube 28 "Fahrrad** (300 EUR, rechnerischer Abstand 350 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491566465 — Apple MacBook Air 13** (349 EUR, rechnerischer Abstand 350 EUR, macbook): Akkuzustand in der anzeige offengelegt und eingepreist. Chip-Generation, Baujahr oder Speicherausstattung sind aus der Anzeige nicht eindeutig ableitbar, damit kein bestaetigter Marktwert.
- **3491859551 — Cube Town Pro E-Bike mit Bosch Motor schwarz** (600 EUR, rechnerischer Abstand 350 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 2.56). Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 450 EUR.
- **3491881952 — DJI Air 3 more flight Pack** (460 EUR, rechnerischer Abstand 350 EUR, optik-drohnen): Abgebrochener Ausleger, Fernsteuerung fehlt. Defekt erklaert den Preis.
- **3491991296 — [TOP PREIS] USM Haller Gardarobe in Anthrazitgrau** (300 EUR, rechnerischer Abstand 350 EUR, design-sammeln): Konto juenger als 30 Tage; Titel nennt Anthrazitgrau, Text Lichtgrau - Widerspruch in der eigenen Anzeige. Referenz unbelastbar (Streuung 2,92).
- **3491512707 — DJI mini 5 pro** (550 EUR, rechnerischer Abstand 349 EUR, optik-drohnen): Bestaetigtes Neupreisniveau 899 bis 990 EUR je nach Fernsteuerung. Die Anzeige nennt nicht, was zum Lieferumfang gehoert (Fernsteuerung, Akkus, Combo oder Einzelgeraet); ohne dieselbe wesentliche Ausstattung ist kein Vergleich moeglich.
- **3491451988 — Canyon Stitched** (550 EUR, rechnerischer Abstand 345 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491607380 — Mountainbike CUBE** (330 EUR, rechnerischer Abstand 344 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 6.18).
- **3491988526 — MacBook Pro M1 16GB RAM 512 GB SSD Touch Bar** (500 EUR, rechnerischer Abstand 340 EUR, macbook): Akkuzustand in der anzeige offengelegt und eingepreist. Chip-Generation, Baujahr oder Speicherausstattung sind aus der Anzeige nicht eindeutig ableitbar, damit kein bestaetigter Marktwert.
- **3491938387 — Canyon Nerve Fully** (300 EUR, rechnerischer Abstand 324 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491660582 — Canyon Roadlite Fitnessbike in Gelb Größe S** (499 EUR, rechnerischer Abstand 320 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491174354 — Herren Trekking Rad** (500 EUR, rechnerischer Abstand 320 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491676369 — Technics SL-1210 MK2** (480 EUR, rechnerischer Abstand 320 EUR, vintage-hifi): Nadelleuchte defekt, kein Tonabnehmer, Massekabel provisorisch mit Luesterklemme repariert. Die offengelegten Maengel erklaeren den Abstand zum Median.
- **3491674753 — SHIMANO DURA ACE Kurbelgarnitur – FC-R9200 – 172,5 mm – 52/36 Z.** (300 EUR, rechnerischer Abstand 320 EUR, ebike-rad): Einzelne Kurbelgarnitur mit Lackabplatzern; 300 EUR liegen unter dem 25-Prozent-Quartil von 389 EUR, aber der bestaetigte Gebrauchtkorridor fuer eine gefahrene FC-R9200 reicht bis in diesen Bereich.
- **3491991746 — iphone 15 pro max 256gb** (280 EUR, rechnerischer Abstand 310 EUR, apple-mobil): Face id defekt. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3416456667 — Knoll International - Diamond Chair Outdoor - Sessel - Weiß** (590 EUR, rechnerischer Abstand 309 EUR, design-sammeln): Referenz unbelastbar (Streuung 2,88); Outdoor-Variante im gebrauchten Zustand vom Haendler auf marktueblichem Niveau.
- **3492012365 — Cube MTB 29"** (350 EUR, rechnerischer Abstand 308 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 3.34).
- **3491928947 — MacBook Pro M1** (385 EUR, rechnerischer Abstand 304 EUR, macbook): Akkuzustand in der anzeige offengelegt und eingepreist. Chip-Generation, Baujahr oder Speicherausstattung sind aus der Anzeige nicht eindeutig ableitbar, damit kein bestaetigter Marktwert.
- **3491082305 — Original Vitra Eames Aluminium Chair, Leder schokobraun** (549 EUR, rechnerischer Abstand 301 EUR, design-sammeln): Der Median 'Vitra Eames Aluminium' mischt EA 107, EA 108, EA 117 und EA 119; ohne Typbezeichnung kein Vergleich.
- **3491273183 — Herman Miller Vitra Eames Fiberglass Side Chair DSW** (249 EUR, rechnerischer Abstand 301 EUR, design-sammeln): Polsterung fleckig und loest sich an einer Stelle - offengelegter Mangel, der den Abstand erklaert.
- **3491180760 — MacBook Air M3** (550 EUR, rechnerischer Abstand 300 EUR, macbook): Chip-Generation, Baujahr oder Speicherausstattung sind aus der Anzeige nicht eindeutig ableitbar, damit kein bestaetigter Marktwert.
- **3491113433 — Cube Race One Limited 29” Mountainbike** (399 EUR, rechnerischer Abstand 291 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 3.47).
- **3491437423 — Ps5 Pro 2tb** (550 EUR, rechnerischer Abstand 288 EUR, konsolen-sweep): Konto am Vortag angelegt, 'Ich verkaufe dringend wegen meiner finanziellen Schwierigkeiten', Versand auf eigene Kosten angeboten. Lehrbuchprofil einer Betrugsanzeige.
- **3491647366 — Meissen Porzellan Kaffeeservice Wellenspiel Relief Waldflora** (499 EUR, rechnerischer Abstand 281 EUR, design-sammeln): Referenz unbelastbar (Streuung 2,86). Zahlung ausdruecklich nur bar, Sofortueberweisung oder PayPal Freunde - also ohne Kaeuferschutz.
- **3491138993 — DJI Mavic 2 Pro Fly More Combo + iPad Mini 4 – Komplettset** (500 EUR, rechnerischer Abstand 275 EUR, optik-drohnen): Referenz unbelastbar (Streuung 4,61); 500 EUR liegen knapp ueber dem 25-Prozent-Quartil von 499 EUR.
- **3491765954 — Cube AMS Pro Fully Fullsuspension Mountainbike** (325 EUR, rechnerischer Abstand 275 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491267751 — DJI Mavic Pro - Fly More Combo** (230 EUR, rechnerischer Abstand 270 EUR, optik-drohnen): Referenz unbelastbar (Streuung 4,0); die Mavic Pro der ersten Generation von 2016 wird gebraucht um 230 bis 350 EUR gehandelt - Marktpreis.
- **3491856322 — Cube Herren Trekkingrad** (325 EUR, rechnerischer Abstand 265 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 3.33).
- **3491619784 — Trek Fuel EX Fully Mountainbike 26 Zoll – reparaturbedürftig** (400 EUR, rechnerischer Abstand 264 EUR, ebike-rad): Ausdruecklich als reparaturbeduerftig inseriert. Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491774201 — Gut erhaltenes Cube Access Mädchen/Damen Mountainbike** (420 EUR, rechnerischer Abstand 255 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 3.62). Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 400 EUR.
- **3466638391 — Stuhl Eames EA 107 Miller Vintage Hopsack Sessel Vitra** (495 EUR, rechnerischer Abstand 255 EUR, design-sammeln): Bezug an der Lehnenkante aufgehellt; Haendlerangebot auf marktueblichem Niveau.
- **3466644691 — Vitra Stuhl Eames Plastic Side Chair DSW** (239 EUR, rechnerischer Abstand 254 EUR, design-sammeln): Referenz unbelastbar (Streuung 3,15); Kratzer auf der Sitzflaeche, kein Echtheitszertifikat. Neupreis 440 EUR laut Anzeige - 239 EUR sind gebraucht marktgerecht.
- **3466641181 — Vitra Stuhl Eames Plastic Side Chair DSW** (239 EUR, rechnerischer Abstand 254 EUR, design-sammeln): Referenz unbelastbar (Streuung 3,15); gleiche Quelle und gleiches Preisniveau wie 3466644691.
- **3491343085 — Specialized Allez Comp Rennrad weiß-rot** (550 EUR, rechnerischer Abstand 250 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 4.16). Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 480 EUR.
- **3491140958 — DJI Mavic Pro Drohne mit Zubehör im Koffer** (250 EUR, rechnerischer Abstand 250 EUR, optik-drohnen): Referenz unbelastbar (Streuung 4,0), gleiche Modellgeneration wie oben; 250 EUR sind Marktpreis.
- **3491646864 — iPhone 15 pro 128gb** (250 EUR, rechnerischer Abstand 250 EUR, apple-mobil): Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491620990 — Canyon Ultimate AL Rennrad XL** (500 EUR, rechnerischer Abstand 250 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491537761 — USM Haller Schreibtisch 175x75cm** (250 EUR, rechnerischer Abstand 250 EUR, design-sammeln): Der Median aus 17 Anzeigen mischt alle Tischgroessen und Gestellfarben; Selbstabbau erforderlich.
- **3491956700 — CUBE 29 Zoll MTB** (300 EUR, rechnerischer Abstand 250 EUR, ebike-rad): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 3.2).
- **3491806554 — DJI Mini 3 Pro Fly More Combo RC** (300 EUR, rechnerischer Abstand 250 EUR, optik-drohnen): 300 EUR fuer ein Mini 3 Pro Fly More Combo liegen unter dem Median von 550 EUR, aber ein bestaetigtes Gebrauchtniveau liess sich nur ueber Kleinanzeigen selbst belegen, nicht ueber zwei unabhaengige konkrete Vergleichsangebote derselben Ausstattung.
- **3491133422 — DJI Mavic Pro 2 (Nur Fluggerät)** (300 EUR, rechnerischer Abstand 249 EUR, optik-drohnen): Nur das Fluggeraet ohne Fernsteuerung und Akkus, der Median besteht aus vollstaendigen Sets - Referenzgruppe passt nicht.
- **3491312341 — Meissen Mokkaservice** (350 EUR, rechnerischer Abstand 249 EUR, design-sammeln): Mokkaservice teils 2. Wahl; der Median mischt vollstaendige und unvollstaendige Service verschiedener Dekore.
- **3492029124 — Cube Hyde Race mit Riemenantrieb** (400 EUR, rechnerischer Abstand 249 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491141079 — iPhone 16 weiß** (450 EUR, rechnerischer Abstand 245 EUR, apple-mobil): Displayriss offengelegt. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491255387 — Mafell Fugenfräse KFU 1000 in der Originalverpackung** (355 EUR, rechnerischer Abstand 237 EUR, werkzeug-maschinen): 355 EUR liegen praktisch auf dem 25-Prozent-Quartil von 350 EUR.
- **3491398112 — Louis Poulsen PH 5 Pendelleuchte** (200 EUR, rechnerischer Abstand 230 EUR, design-sammeln): Weder Baujahr noch Ausfuehrung genannt; PH-5-Leuchten unterscheiden sich zwischen Original, Neuauflage und Nachbau erheblich im Wert.
- **3491445451 — iPhone 14 Pro Max 256GB Space Black Wasserschaden** (270 EUR, rechnerischer Abstand 229 EUR, apple-mobil): Wasserschaden, geraet schaltet sich alle fuenf minuten ab. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3492027051 — iPhone 15 Pro 128GB** (280 EUR, rechnerischer Abstand 220 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491961417 — Louis Poulsen Lampe** (175 EUR, rechnerischer Abstand 215 EUR, design-sammeln): 'Louis Poulsen Lampe' ohne Modellangabe, Beschreibung aus einem Satz. Kein Marktwert bestimmbar.
- **3491448465 — iPhone 15 Schwarz 128Gb + OVP** (249 EUR, rechnerischer Abstand 213 EUR, apple-mobil): Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491421816 — MTB Fahrrad Cube** (440 EUR, rechnerischer Abstand 210 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 4.88). Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 400 EUR.
- **3491392990 — Smartphone iPhone 14** (150 EUR, rechnerischer Abstand 200 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491336396 — Apple IPhone 14 Pro 128GB Silber - Rückseite gebrochen -** (200 EUR, rechnerischer Abstand 200 EUR, apple-mobil): Face id defekt. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491384951 — iPhone 13 Pro Max 512 GB** (250 EUR, rechnerischer Abstand 200 EUR, apple-mobil): Face id defekt. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491281587 — Apple MacBook Pro** (450 EUR, rechnerischer Abstand 200 EUR, macbook): Chip-Generation, Baujahr oder Speicherausstattung sind aus der Anzeige nicht eindeutig ableitbar, damit kein bestaetigter Marktwert. Referenz unbelastbar (Streuung 3.56). Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 449 EUR.
- **3491228514 — Drehmaschine Rotwerk EDM 300 DR** (250 EUR, rechnerischer Abstand 200 EUR, werkzeug-maschinen): Modellbau-Drehmaschine Rotwerk EDM 300DR; 250 EUR liegen dicht unter dem 25-Prozent-Quartil von 400 EUR, aber ohne Zubehoerangabe kein bestaetigter Vergleich.
- **3491464450 — Marshall Box** (200 EUR, rechnerischer Abstand 200 EUR, musikinstrumente): 'Marshall Box' ohne Modellangabe - Gitarrenbox oder Bluetooth-Lautsprecher ist nicht unterscheidbar. Kein Marktwert bestimmbar.
- **3492004374 — Cube Aim SLX Mountainbike XL 29 Zoll** (300 EUR, rechnerischer Abstand 200 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491976022 — iPhone 15 128 GB Weiß** (300 EUR, rechnerischer Abstand 199 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491852030 — Mountainbike Canyon Nerve AL+** (440 EUR, rechnerischer Abstand 199 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491828657 — Canyon Rennrad Ultimate AL F8 Größe M schwarz** (450 EUR, rechnerischer Abstand 199 EUR, ebike-rad): Displayriss offengelegt. Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 450 EUR.
- **3491933836 — Cube Nature Pro Crossbike Größe L** (350 EUR, rechnerischer Abstand 194 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491857306 — iPhone 14 Pro Apple** (230 EUR, rechnerischer Abstand 190 EUR, apple-mobil): Displayriss offengelegt. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491835949 — iPhone 13 Pro Max** (180 EUR, rechnerischer Abstand 185 EUR, apple-mobil): Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491163327 — iPhone 14 128gb** (200 EUR, rechnerischer Abstand 182 EUR, apple-mobil): Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491825819 — MTB 26" Cube Reaction SL** (320 EUR, rechnerischer Abstand 180 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 2.88).
- **3491814733 — Vitra Headline Bürodrehstuhl mit Kopfstütze** (299 EUR, rechnerischer Abstand 176 EUR, design-sammeln): Gebrauchsspuren offengelegt; 299 EUR liegen im Korridor gebrauchter Vitra-Drehstuehle dieser Baureihe.
- **3491115973 — iphone 15 gut erhalten nur abholung  ohne kabel** (280 EUR, rechnerischer Abstand 175 EUR, apple-mobil): Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491120670 — HP500 pkw anhänger** (150 EUR, rechnerischer Abstand 175 EUR, messtechnik): Abgemeldet, TUEV abgelaufen; 150 EUR liegen unter dem 25-Prozent-Quartil von 200 EUR, der Zustand erklaert das.
- **3491845957 — Cube Mountainbike** (375 EUR, rechnerischer Abstand 175 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Referenz unbelastbar (Streuung 3.29). Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 350 EUR.
- **3492025232 — Apple iPhone 15 – 256 GB – Schwarz – Top Zustand** (380 EUR, rechnerischer Abstand 170 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491998025 — Schreibtisch USM Haller** (350 EUR, rechnerischer Abstand 170 EUR, design-sammeln): Der Median mischt alle USM-Schreibtischgroessen; 350 EUR fuer 175x75 in Perlgrau sind marktgerecht.
- **3491824276 — Cube AMS 100 Fully Mountainbike 26 Zoll** (385 EUR, rechnerischer Abstand 165 EUR, ebike-rad): Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen. Der Preis liegt ohnehin auf oder ueber dem 25-Prozent-Quartil von 370 EUR.
- **3491990509 — Apple iPhone 15** (320 EUR, rechnerischer Abstand 160 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3492019639 — Korg Minilogue XD** (320 EUR, rechnerischer Abstand 160 EUR, musikinstrumente): 320 EUR liegen unter dem 25-Prozent-Quartil von 450 EUR, aber der Abstand zum bestaetigten Gebrauchtniveau des Minilogue XD bleibt unter 20 Prozent.
- **3491971300 — iPhone 15 128 GB – Black – guter Zustand** (320 EUR, rechnerischer Abstand 158 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491176940 — Apple iPhone 14** (200 EUR, rechnerischer Abstand 150 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491104127 — Apple iPhone 13 256GB** (200 EUR, rechnerischer Abstand 150 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491096378 — Rennrad Trek Alpha Aluminum Herren** (300 EUR, rechnerischer Abstand 150 EUR, ebike-rad): Beide reifen platt. Der Median fasst alle Anzeigen des Suchworts ueber Modelljahre, Rahmengroessen und Ausstattungsstufen zusammen; zwei konkrete Vergleichsangebote derselben Variante liessen sich nicht belegen.
- **3491906115 — iPhone 14 128 GB** (200 EUR, rechnerischer Abstand 150 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491823966 — iPhone 14 128 gb** (200 EUR, rechnerischer Abstand 150 EUR, apple-mobil): Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491954922 — iphone 15 128  gb grün** (250 EUR, rechnerischer Abstand 150 EUR, apple-mobil): Displayriss offengelegt. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491909360 — iphone  14 Pro Max** (300 EUR, rechnerischer Abstand 150 EUR, apple-mobil): Face id defekt. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3492026283 — MacBook Air 13” – 8 GB RAM / 256 GB SSD** (350 EUR, rechnerischer Abstand 150 EUR, macbook): Chip-Generation, Baujahr oder Speicherausstattung sind aus der Anzeige nicht eindeutig ableitbar, damit kein bestaetigter Marktwert.
- **3491901501 — Thorens TD 145 Plattenspieler** (140 EUR, rechnerischer Abstand 144 EUR, vintage-hifi): Laeuft nur mit 33 U/min - die 45er-Geschwindigkeit fehlt. Defekt erklaert den Preis.
- **3492027481 — Apple IPhone 12 und IPhone 13** (175 EUR, rechnerischer Abstand 144 EUR, apple-mobil): Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491902082 — Iphone 15 128gb** (310 EUR, rechnerischer Abstand 140 EUR, apple-mobil): Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491906246 — IPhone 15 128gb** (310 EUR, rechnerischer Abstand 140 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491956717 — Iphone 12 Pro 512 gb grau** (185 EUR, rechnerischer Abstand 135 EUR, apple-mobil): Rueckseite gesplittert. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491891057 — Hilti Bohrmaschine TE 6-S** (175 EUR, rechnerischer Abstand 125 EUR, werkzeug-maschinen): Hilti TE 6-S, Beschreibung ohne Zustandsdetails; 175 EUR liegen dicht am 25-Prozent-Quartil von 199 EUR.
- **3491919538 — ⭐️ APPLE IPHONE 14 ⭐️ 128GB MIDNIGHT** (199 EUR, rechnerischer Abstand 121 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491815829 — iPhone 12 Pro Max** (160 EUR, rechnerischer Abstand 110 EUR, apple-mobil): Face id defekt. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491991711 — iPhone 13 128 GB** (150 EUR, rechnerischer Abstand 100 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491874845 — Iphone 12 pro Max 128 GB *Glassprung Beidseitig*** (170 EUR, rechnerischer Abstand 100 EUR, apple-mobil): Glas gesprungen. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491819900 — Apple iPhone 13** (200 EUR, rechnerischer Abstand 100 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3491987339 — iPhone   13** (200 EUR, rechnerischer Abstand 100 EUR, apple-mobil): Akkuzustand in der anzeige offengelegt und eingepreist. Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells in demselben Zustand kein bestaetigter Abstand von 20 Prozent.
- **3492037913 — 2x Technics SL-1200MK2 Silber – DJ-Set, frisch fachgewartet** (1749 EUR, kein Median, vintage-hifi): Kein Kleinanzeigen-Median vorhanden. Zwei gewartete SL-1200MK2 werden zusammen bei etwa 1.600 bis 2.200 EUR gehandelt; 1.749 EUR liegen mitten darin, zumal an einer Haube eine Halterung ausgebrochen ist.
- **3492015011 — Schwebetüren Schrank von Haushaltsauflösung** (300 EUR, kein Median, notverkaeufe): Kein Median, keine Masse, ein Bild. Ohne Angaben kein Marktwert.
- **3492016500 — Pokemon Sammlungsauflösung [SEALED]** (686 EUR, kein Median, notverkaeufe): Kein Median. Der Verkaeufer preist jede Position selbst aus, die Summe entspricht dem Angebotspreis - keine Unterbewertung erkennbar. Zahlung ausdruecklich per PayPal Freunde, also ohne Kaeuferschutz.
- **3492008771 — Scheunenfund + Motorschaden!! Ford Probe II 2.0 16V "Highlight"** (1150 EUR, kein Median, notverkaeufe): Motorschaden und weitere Schaeden, ausdruecklich als nicht fahrbereites Bastlerfahrzeug verkauft. Der Preis erklaert sich selbst.
- **3492044866 — Accuphase E 307 with Phono AD 9** (2400 EUR, kein Median, vintage-hifi): Kein Kleinanzeigen-Median. hifishark.com, die vorgeschriebene Referenzquelle fuer HiFi, ist vom Netzwerk-Proxy blockiert (EGRESS_BLOCKED), und die Suchergebnisse enthielten keine belastbaren Verkaufspreise fuer den E-307. Ohne belegten Referenzwert wird nicht geschaetzt.
- **3492042412 — Funko Pop Sammlungsauflösung** (500 EUR, kein Median, notverkaeufe): Kein Median, ein Bild, Sammlung nur teilweise aufgelistet. Kein bestimmbarer Wert.


---

# Laufprotokoll 2026-08-23, Abendlauf

**Lauf:** 23. August 2026, 19:10 Uhr (MESZ)
**candidates.json generiert:** 2026-08-23T15:49:56+02:00 (rund 3 Stunden 20 Minuten alt, innerhalb der Frist von vier Stunden)
**Zeitraum der Sammlung:** 2026-08-23T09:19:09+02:00 bis 2026-08-23T14:19:09+02:00
**Gesichtete Anzeigen:** 190.973
**Kandidaten in candidates.json:** 192
**Bereits in deal_log.csv (verworfen vor Pruefung):** 0
**Zu pruefende Kandidaten:** 192 (davon 112 bereits im Morgenprotokoll dokumentiert, 80 neu hinzugekommen)
**Gemeldete Funde:** 0

## Funde

Keine. Kein Kandidat hat die Pruefung nach prompt.md Schritt 2 bestanden.

Damit bleiben `deals.json`, `email_output.html` und `deal_log.csv` unveraendert, und es wird keine
Mail ausgeloest. Nur dieses Laufprotokoll wird nach `main` gepusht.

## Wichtigster Befund dieses Laufs: die externe Marktwertpruefung ist eingeschraenkt

Der Morgenlauf hatte bereits gemeldet, dass hifishark.com vom Netzwerk-Proxy blockiert ist. Am
Abend ist der Direktabruf **flaechendeckend** blockiert: getestet wurden hifishark.com,
soundsmarket.com, buyzoxs.de, buycycle.com, swappa.com und geizhals.de - alle sechs antworten mit
`EGRESS_BLOCKED`. Funktionsfaehig ist nur die Websuche, und die liefert bei deutschen
Gebrauchtmaerkten fast ausschliesslich Kategorieseiten ohne Preise auf Angebotsebene, weil sie
US-zentriert sucht.

Praktische Folge fuer diesen Lauf: Wo ein Marktwert aus einer Fachquelle oder aus Neupreisen
belegbar war, ist er belegt worden - und hat in jedem einzelnen Fall den Kandidaten ausgeschieden,
nicht bestaetigt (Beispiele unten). Wo er nur ueber konkrete Gebrauchtangebote zu belegen gewesen
waere, ist der Kandidat nach prompt.md verworfen worden, statt einen Wert zu schaetzen. Das
betrifft vor allem die Mittelklasse zwischen 700 und 2.500 EUR: Fahrraeder, MacBooks, Pedelecs.

Diese Einschraenkung ist behebbar und sollte behoben werden - sie kostet den Scanner genau das
Segment, in dem er sonst am haeufigsten faendig wuerde.

## Was extern belegt werden konnte

- **Technics SL-1200MK2:** Preisleitfaden 2026 (retrotechlab) nennt 900 bis 1.200 USD fuer ein
  zuverlaessiges gebrauchtes MK2/MK3, ein zweiter Beleg setzt bei 915 USD an. Das Berliner Paar
  (3492037913, frisch fachgewartet, Rechnung ueber 370 EUR) kostet 1.749 EUR fuer zwei Geraete,
  also 875 EUR je Stueck bei einem Einzelabgabepreis von 899 EUR. Das ist Marktniveau, kein
  Abstand von 20 Prozent. Damit ist der einzige Kandidat des Laufs, dessen Marktwert sich sauber
  belegen liess, genau daran gescheitert.
- **DJI Mini 5 Pro:** Neupreis Fly More Combo (RC 2) 1.099 USD, ein deutsches Angebot bei rund
  1.009 EUR. Der Kandidat 3491512707 fuer 550 EUR nennt nicht, was zum Lieferumfang gehoert -
  ohne dieselbe wesentliche Ausstattung ist kein Vergleich moeglich (bereits im Morgenprotokoll).
- **Cube Reaction Hybrid Pro 500, Modelljahr 2019:** Neupreis laut Geizhals 1.803 EUR. Der
  Kleinanzeigen-Median von 1.899 EUR bildet damit ungefaehr das Neupreisniveau von 2019 ab und
  nicht den heutigen Gebrauchtwert - eine Falle, die in diesem Datensatz gleich zweimal auftritt
  (3492095732 und 3492134876).

## Warum auch dieser Lauf leer ausgeht

Die Kandidaten mit dem groessten absoluten Abstand sind zuerst geprueft worden, dazu vollstaendig
die liquiden Kategorien Uhren, Tesla, Porsche, Apple, Drohnen und HiFi. Vier Gruende tragen den
gesamten Lauf:

**Der niedrige Preis erklaert sich selbst.** Das ist an diesem Abend der mit Abstand haeufigste
Grund und trifft die vier groessten neuen Kandidaten. Der Tesla Model Y fuer 14.000 EUR (12.999 EUR
rechnerischer Abstand, der groesste des Laufs) traegt 318.000 km und einen BMS-Schaden und ist
ausdruecklich als beschaedigtes Fahrzeug inseriert. Die Honda Fireblade SC57 hatte im Vorjahr einen
Unfall mit Verkleidungstausch. Die Ducati Monster 1100 hat eine haengende Schaltung und eine
verklebte Trockenkupplung, die Monster 821 eine Tankbeule und einen undichten Gabelsimmerring.
Beim gesamten Youngtimer-Block sind es Laufleistungen zwischen 217.000 und 294.000 km.

**Der bestaetigte Marktwert liegt naeher am Angebot als der Median.** Der neue Uhrenblock ist dafuer
das klarste Beispiel. Die Datejust 41 mit blauem Blatt und Full Set fuer 8.950 EUR liegt im
Korridor von 9.000 bis 10.500 EUR statt 20 Prozent darunter; der Median von 14.300 EUR enthaelt
Weissgold-Luenetten und Diamantbesatz. Die Tudor Black Bay Chronograph 79360N fuer 4.490 EUR liegt
auf dem Gebrauchtniveau ihrer Referenz. Die Oyster Perpetual 36 (Ref. 126000, Februar 2026,
deutscher Konzessionaer) fuer 7.500 EUR liegt sogar **ueber** dem Listenpreis von rund 6.100 EUR -
der Median aus elf Anzeigen hat hier eine Ersparnis von 3.279 EUR erzeugt, wo ein Aufschlag ist.

**Die Referenzgruppe passt nicht zur Ware.** Die Omega Seamaster 'Montreal' fuer 1.190 EUR ist an
den neuen Batterien vom Konzessionaer als Quarzuhr erkennbar, waehrend der Median 'Omega Seamaster
Chrono' aus automatischen Chronographen besteht. Der Eames Segmented Tisch sagt im eigenen Titel
'kein Vitra' und wird gegen einen Median aus Originalanzeigen gehalten. Die TAG Heuer fuer
1.250 EUR fuehrt Rolex, Breitling, IWC, Omega, Tudor und Cartier als Suchwoerter im Titel, was den
Median aus fremden Marken zusammensetzt.

**Das Betrugsprofil aus der Leitidee.** Neu an diesem Abend: ein MacBook Air M4 15 Zoll 16/256 fuer
450 EUR bei einem Gebrauchtniveau von 900 bis 1.100 EUR, mit 32 Ladezyklen, drei Zeilen Text und
ausschliesslich Versand. Und eine Jaeger-LeCoultre Master Automatique fuer 3.600 EUR, deren Anzeige
'Papiere (blanko)' anpreist - Blankopapiere sind das Kennzeichen von Faelschungsware, nicht von
Provenienz.

## Methodische Hinweise zu diesem Lauf

- `candidates.json` sammelt die noch nicht gemeldeten Kandidaten der letzten 24 Stunden an. Weil
  der Morgenlauf null Funde gemeldet hat, ist nichts in `deal_log.csv` gewandert, und 112 der 192
  Kandidaten sind dieselben wie heute frueh. Fuer diese 112 gilt die Begruendung aus dem
  Morgenprotokoll unveraendert; sie sind stichprobenhaft gegengeprueft und nicht neu bewertet
  worden. Die 80 neuen Kandidaten sind unten einzeln aufgefuehrt.
- **Kein Kandidat dieses Laufs traegt `signale.unkenntnis_bonus`.** Die Regel aus der Leitidee,
  solche Kandidaten nicht nach Anzeigenqualitaet abzuwerten, kam an diesem Abend also nicht zum
  Tragen.
- Priorisiert wurde nach absolutem Abstand und liquider Ware. Einzeln und mit Volltext geprueft
  wurden saemtliche neuen Kandidaten der Kategorien Uhren, Tesla, Youngtimer, Motorraeder, Apple,
  Drohnen, HiFi, Musikinstrumente, Werkzeug und Design sowie alle uebrigen neuen Kandidaten mit
  einem rechnerischen Abstand ueber 250 EUR.
- Zwei Referenzgruppen-Fallen sind in diesem Datensatz neu bzw. deutlicher geworden: der
  **Pedelec-Neupreis-Median** (siehe oben, der Median bildet den Neupreis des Modelljahrs ab, nicht
  den Gebrauchtwert) und der **USM-Haller-Haendlerblock** - von den zehn neuen USM-Anzeigen sind
  sieben gewerbliche Anbieter mit Bruttopreisauszeichnung, die gegen einen Median gehalten werden,
  in dem sie selbst den groessten Teil der Stichprobe stellen.
- Die Datejust 41 (3492351835) und die Rolex Submariner (3491762938) sind beide mit `preis_typ`
  `PLEASE_CONTACT` bzw. einzeiliger Beschreibung inseriert. Bei vierstelligen bis fuenfstelligen
  Uhren ohne Referenznummer im Text ist eine Bewertung grundsaetzlich nicht moeglich, egal wie eng
  die Referenz ist.

## Verworfene Kandidaten: 80 neu hinzugekommen

- **3492080914 — Tesla Y Long Range Dual** (14000 EUR, rechnerischer Abstand 12999 EUR, tesla): Als beschaedigtes Fahrzeug inseriert: BMS-Schaden, 318.000 km. Der Defekt und die Laufleistung erklaeren den Preis vollstaendig.
- **3492351835 — Rolex Datejust 41 mm Stahl blaues Blatt neu** (8950 EUR, rechnerischer Abstand 5350 EUR, uhren): Bestaetigtes Preisniveau der Datejust 41 in Stahl mit blauem Blatt: rund 9.000 bis 10.500 EUR im Gebrauchthandel. 8.950 EUR liegen darin, nicht 20 Prozent darunter. Der Median von 14.300 EUR stammt aus 'Rolex Datejust 41' und enthaelt Weissgold-Lunetten und Diamantbesatz.
- **3492297072 — Rolex Datejust 36** (5000 EUR, rechnerischer Abstand 5140 EUR, uhren): Datejust 36 von 2003 ohne Papiere; als Ersatz wird ein 'Echtheitszertifikat vom Juwelier' genannt, was kein Papiersurrogat ist. Fuer eine 36er ohne Papiere aus diesem Jahrgang liegt das Niveau bei rund 4.000 bis 6.500 EUR, das 25-Prozent-Quartil der Referenz bei 6.500 EUR. Kein belegbarer Abstand von 20 Prozent.
- **3492397995 — BMW 328i*E36*Cabrio*Automatik*LPG*Tüv neu*** (6500 EUR, rechnerischer Abstand 4750 EUR, youngtimer-alltag): 217.000 km und LPG-Umbau von einem gewerblichen Anbieter. Die Gasanlage ist bei einem E36 Cabrio wertmindernd, die Laufleistung erklaert den Rest.
- **3492165750 — BMW 320i  E36 Cabrio** (4400 EUR, rechnerischer Abstand 3520 EUR, youngtimer-alltag): 250.000 km, Verdeck laesst sich nur noch manuell oeffnen (Ursache dem Verkaeufer selbst unbekannt), Vordersitze stark verschlissen. Die Maengel erklaeren den Preis.
- **3492336948 — Jaeger lecoultre Master Automatique** (3600 EUR, rechnerischer Abstand 3298 EUR, uhren): Die Anzeige nennt 'Papiere (blanko)'. Blankopapiere sind das Kennzeichen von Faelschungsware, nicht von Provenienz. Verworfen, nicht gemeldet.
- **3492183576 — Rolex Oyster Perpetual , 36 , neu , LC 100** (7500 EUR, rechnerischer Abstand 3279 EUR, uhren): Ref. 126000 aus Februar 2026 vom deutschen Konzessionaer. Der Listenpreis der Oyster Perpetual 36 liegt bei rund 6.100 EUR; 7.500 EUR liegen darueber, nicht darunter. Der Median aus nur elf Anzeigen ist keine belastbare Referenz.
- **3309206122 — Cassina - LC 2 - 3-sitzer Sofa - Leder hell - guter Zustand** (4490 EUR, rechnerischer Abstand 3010 EUR, design-sammeln): Referenz unbelastbar (Streuung 3,09, nur 12 Anzeigen). Gewerblicher Anbieter; 4.490 EUR entsprechen dem Haendlerniveau fuer ein gebrauchtes LC2 in hellem Leder.
- **3492328683 — Omega Seamaster** (1150 EUR, rechnerischer Abstand 2840 EUR, uhren): Referenz unbelastbar (Streuung 2,81). Vergoldete Vintage-Seamaster ohne Referenz- oder Kaliberangabe; ohne bestimmbares Modell kein Marktwert.
- **3492081162 — Tudor Black Bay Chronograph 41 mm – Ref. 79360N – ungetragen – Fu** (4490 EUR, rechnerischer Abstand 2830 EUR, uhren): Black Bay Chronograph 79360N ungetragen fuer 4.490 EUR VB. Das Gebrauchtniveau dieser Referenz liegt bei rund 3.800 bis 4.600 EUR und damit auf Hoehe des Angebots. Der Median aus zwoelf Anzeigen traegt nicht.
- **3492350685 — Omega Seamaster Chrono Montreal Albatros** (1190 EUR, rechnerischer Abstand 2760 EUR, uhren): Die Uhr ist eine Quarzuhr - die Anzeige nennt neue Batterien vom Omega-Konzessionaer. Der Median 'Omega Seamaster Chrono' besteht aus automatischen Chronographen und passt nicht zur Ware. Fuer diese Vintage-Quarzreferenz liessen sich keine zwei konkreten Vergleichsangebote belegen.
- **3492545028 — Ducati Monster 1100** (3500 EUR, rechnerischer Abstand 2552 EUR, motorraeder): Schaltung haengt, Trockenkupplung verklebt, ein Jahr Standzeit. Die offengelegten Defekte erklaeren den Preis.
- **3492265078 — Mercedes Benz W201 190E 2.0 Automatik** (4700 EUR, rechnerischer Abstand 2500 EUR, youngtimer-alltag): 266.834 km. Fuer einen 190E 2.0 Automatik mit dieser Laufleistung sind 4.700 EUR eher am oberen Rand des Marktes; das 25-Prozent-Quartil der Referenz liegt bei 4.999 EUR.
- **3492472166 — Mercedes-Benz 190E W201** (3200 EUR, rechnerischer Abstand 2290 EUR, youngtimer-alltag): 294.000 km bei einem 190E 1.8 von 1993. Der Verkaeufer schreibt selbst, wer ein Museumsstueck suche, sei hier falsch. Die Laufleistung erklaert den Preis.
- **3492333321 — Mercedes-Benz E 250 D W124 Oldtimer mit H-Zulassung** (4850 EUR, rechnerischer Abstand 2260 EUR, youngtimer-alltag): 170.000 km, H-Zulassung, umfangreiche Reparaturliste vor dem TUEV, Lackabplatzer an Fahrertuer und Heckklappe. 4.850 EUR sind fuer einen fahrbereiten 250 D marktgerecht; der Median stammt aus nur zwoelf Anzeigen.
- **3492323716 — Ducati Monster 821** (4100 EUR, rechnerischer Abstand 2191 EUR, motorraeder): Beule und Lackschaden am Tank, linkes Standrohr oelt (undichter Gabelsimmerring). Die offengelegten Maengel erklaeren den Abstand.
- **3363564118 — Omega Seamaster Chronograph Albertville/Barcelona Fullset** (1790 EUR, rechnerischer Abstand 2034 EUR, uhren): Quarzchronograph vom gewerblichen Uhrenhaendler mit Artikelnummer und Erstkaufrechnung. 1.790 EUR sind das Haendlerniveau fuer diese Olympia-Sonderserie, nicht ein Abstand darunter.
- **3492504097 — Honda Fireblade SC57** (3400 EUR, rechnerischer Abstand 2000 EUR, motorraeder): Der Verkaeufer nennt selbst einen Unfall im Vorjahr mit Verkleidungstausch. Unfallschaden ist nach prompt.md Schritt 2 ausdruecklich kein Fund, sondern ein korrekt bepreistes Angebot.
- **3491245144 — Gibson Les Paul Studio Faded Worn Brown – 2012 – Made in USA** (950 EUR, rechnerischer Abstand 1994 EUR, musikinstrumente): Referenz unbelastbar (Streuung 8,54). Das Gebrauchtniveau der Les Paul Studio Faded von 2012 liegt bei rund 700 bis 1.100 EUR; 950 EUR sind Marktpreis. Der Median mischt die gesamte Les-Paul-Palette bis zur Custom.
- **3492078942 — Kreidler Vitality Eco 6 EDT E-Bike Bosch Performance line** (749 EUR, rechnerischer Abstand 1450 EUR, ebike-rad): Bosch Performance Line, nicht CX; 5.070 km, Maentel muessen gewechselt werden. Der Median aus zehn Anzeigen (Streuung 2,19) mischt hoehere Ausstattungsstufen. 749 EUR sind fuer diese Konfiguration marktgerecht.
- **3492548803 — ducati monster s4** (2950 EUR, rechnerischer Abstand 1190 EUR, motorraeder): TUEV seit 06/2025 abgelaufen, seit 2024 nicht mehr bewegt. Standzeit und fehlende Hauptuntersuchung erklaeren den Preis.
- **3492130199 — BMC URS Gravel Two Gravelbike Größe L** (1400 EUR, rechnerischer Abstand 1099 EUR, modellbau-sammler): Weder Modelljahr noch Laufleistung genannt, Zustand nur pauschal als 'gut gebraucht mit entsprechenden Spuren' beschrieben. Fuer das URS Two mit GRX Di2 liessen sich keine zwei konkreten Vergleichsangebote derselben Generation belegen - die Baujahre 2020 bis 2026 liegen im Gebrauchtmarkt um mehr als 1.000 EUR auseinander.
- **3492095732 — ❗❗❗ CUBE REACTION HYBRID 29 Zoll❗❗❗** (899 EUR, rechnerischer Abstand 1000 EUR, ebike-rad): Baujahr 2019, 3.150 km. Der Neupreis der Reaction Hybrid Pro 500 von 2019 lag laut Geizhals bei 1.803 EUR; der Median von 1.899 EUR entspricht damit ungefaehr dem damaligen Neupreis und nicht dem heutigen Gebrauchtwert. Fuer ein sieben Jahre altes Pedelec sind 899 EUR marktgerecht.
- **3492311126 — Simson s51** (2300 EUR, rechnerischer Abstand 940 EUR, motorraeder): Papiere fehlen, Blinker ohne Funktion. Bei Simson sind die Papiere der zentrale Wertfaktor; der Median besteht aus Fahrzeugen mit Papieren.
- **3335095037 — USM Haller Garderobe offen** (799 EUR, rechnerischer Abstand 900 EUR, design-sammeln): Gewerblicher Anbieter mit Katalogtext. Der Median 'USM Haller Garderobe' mischt alle Groessen und Konfigurationen, und genau die Konfiguration macht bei USM den Preis.
- **3492401866 — BMC Rennrad** (600 EUR, rechnerischer Abstand 899 EUR, modellbau-sammler): Weder Modelljahr noch Schaltgruppe genannt; die verbauten Shimano WH-R550 datieren das Teammachine auf etwa 2008 bis 2012. Referenz unbelastbar (Streuung 3,57).
- **3492131135 — Simson Schwalbe mit Papiere** (1700 EUR, rechnerischer Abstand 842 EUR, motorraeder): Papiere werden im Titel behauptet, die Beschreibung besteht aus zwei Zeilen mit Telefonnummer und schweigt zu Baujahr und Zustand.
- **2439404123 — Usm Haller Sideboard Beige  Inkl MwSt** (640 EUR, rechnerischer Abstand 780 EUR, design-sammeln): Gewerblicher Anbieter mit Bruttopreisauszeichnung; der Median mischt alle Sideboard-Groessen und -Konfigurationen.
- **3492181242 — Simson Schwalbe** (1700 EUR, rechnerischer Abstand 775 EUR, motorraeder): Umfangreiche Neuteileliste, aber die Anzeige schweigt zu den Papieren - bei Simson der entscheidende Wertfaktor.
- **3492086952 — Cube Ebike neuwertig wenig gefahren Bosch Motor** (1000 EUR, rechnerischer Abstand 750 EUR, ebike-rad): Kein Modell genannt, nur 'Fahrrad der Marke Cube' mit Bosch-Motor und 500 Wh. Ohne Modell und Baujahr kein bestaetigter Marktwert.
- **3442884069 — USM Haller Sideboard Lowboard TV-Board Regal offen weiß** (699 EUR, rechnerischer Abstand 721 EUR, design-sammeln): Gewerblicher Anbieter, der Konfiguration und Aufbau als Zusatzleistung anbietet. Marktuebliches Haendlerniveau.
- **3492337588 — Longines HydroConquest Chronograph** (949 EUR, rechnerischer Abstand 701 EUR, uhren): Der Verkaeufer legt einen deutlichen Schmarren an der roten Luenette offen und bildet ihn ab. Fuer eine getragene L3.696.4 mit sichtbarem Luenettenschaden sind 949 EUR marktgerecht; der Median stammt aus nur zehn Anzeigen.
- **2465237697 — USM HALLER SIDEBOARD WEIß** (749 EUR, rechnerischer Abstand 671 EUR, design-sammeln): Gewerblicher Anbieter; der Median mischt alle Sideboard-Groessen.
- **3492269525 — 2x USM Haller Sideboard mit Klappe, weiß** (750 EUR, rechnerischer Abstand 650 EUR, design-sammeln): Weder Masse noch Zahl der Elemente genannt. Bei USM Haller bestimmt genau das den Preis; ohne Konfiguration kein Vergleich.
- **3492199991 — Hebebühne 4t** (999 EUR, rechnerischer Abstand 601 EUR, werkzeug-maschinen): Weder Hersteller noch Typ noch Baujahr der Hebebuehne genannt, Verkauf 'in Auftrag', Abbau durch den Kaeufer. Der Median aus 18 Anzeigen (Streuung 2,0) mischt Zwei- und Viersaeulenbuehnen. Ohne Typ kein Marktwert.
- **3229204537 — USM Haller Sideboard - Reinweiß - inkl. MwSt.** (825 EUR, rechnerischer Abstand 595 EUR, design-sammeln): Autorisierter USM-Partner mit Bruttopreis. Marktuebliches Haendlerniveau, kein Privatverkauf unter Wert.
- **3492165611 — Apple MacBook Air M4 2025 15 Zoll 16gb/256gb Space Grau** (450 EUR, rechnerischer Abstand 550 EUR, macbook): Das Gebrauchtniveau des MacBook Air M4 15 Zoll 16/256 liegt bei rund 900 bis 1.100 EUR. 450 EUR fuer ein Geraet mit 32 Ladezyklen, nur gegen Versand, Beschreibung aus drei Zeilen - das ist das handwerklich saubere Betrugsprofil aus der Leitidee, kein Fund.
- **3492458422 — Suzuki GSXR 750 SRAD** (1250 EUR, rechnerischer Abstand 523 EUR, motorraeder): Referenz unbelastbar (Streuung 2,75). Der Median mischt alle GSX-R-Generationen; fuer eine SRAD von 1996 bis 1999 mit 27.000 km sind 1.250 EUR marktgerecht.
- **3492249328 — Diamond Chair – Harry Bertoia für Knoll– Designklassiker** (380 EUR, rechnerischer Abstand 519 EUR, design-sammeln): Referenz unbelastbar (Streuung 2,66). Die Anzeige belegt die Herkunft nicht - kein Knoll-Stempel, kein Kaufbeleg genannt. Bei einem Modell, dessen Nachbauten den Markt dominieren, ist die Echtheit der Preis; ohne sie kein Marktwert.
- **3492417227 — **MEISSEN Porzellan - 6 x Kaffee Service - Zwiebelmuster, Tassen*** (375 EUR, rechnerischer Abstand 515 EUR, design-sammeln): Referenz unbelastbar (Streuung 2,60). Gebrauchte Meissen-Zwiebelmuster-Kaffeeservices fuer sechs Personen werden regelmaessig zwischen 300 und 600 EUR gehandelt; 375 EUR liegen darin.
- **3492052384 — TAG HEUER CHRONOGRAPH ROLEX BREITLING IWC OMEGA TUDOR CARTIER** (1250 EUR, rechnerischer Abstand 500 EUR, uhren): Referenz unbelastbar (Streuung 2,64). Der Titel listet Rolex, Breitling, IWC, Omega, Tudor und Cartier als Suchwoerter, verkauft wird eine TAG Heuer Formula 1 CAZ1010 - der Median ist damit aus fremden Marken zusammengesetzt.
- **3492543230 — bmc AL 257** (525 EUR, rechnerischer Abstand 474 EUR, modellbau-sammler): Der Verkaeufer nennt den Neupreis selbst mit rund 1.000 EUR. 525 EUR nach einem Jahr und umlackierten Schutzblechen sind marktgerecht; der Median von 999 EUR (Streuung 3,17, unbelastbar) bildet das Neupreisniveau ab.
- **3492329028 — Tag Heuer Formula 1 Fullset** (850 EUR, rechnerischer Abstand 463 EUR, uhren): Das Gebrauchtniveau der Formula 1 WAZ1110 im Fullset liegt bei rund 700 bis 1.000 EUR. 850 EUR liegen darin, kein Abstand von 20 Prozent.
- **3492134876 — Cube Reaction Hybrid Pro 500 – Bosch CX – 500 Wh – E‑MTB – E‑Bike** (990 EUR, rechnerischer Abstand 460 EUR, ebike-rad): Baujahr 2018, 10.344 km am Bosch-CX-Antrieb. Die Laufleistung ist bei Pedelecs der zentrale Wertfaktor und erklaert den Preis.
- **3492338305 — EAMEs Segmented Tisch Vintage Modern Design kein Vitra  Chrome** (790 EUR, rechnerischer Abstand 452 EUR, design-sammeln): Die Anzeige sagt im Titel selbst 'kein Vitra'. Ein Nachbau hat keinen Bezug zu einem Median aus Originalanzeigen; ausserdem gewerblicher Anbieter.
- **3442845554 — Longines Automatik** (790 EUR, rechnerischer Abstand 435 EUR, uhren): Der Median 'Longines Automatik' fasst 92 Anzeigen ueber die gesamte Modellpalette zusammen. Fuer die L4.708.2 (Flagship/Presence-Groesse) sind 790 EUR marktgerecht.
- **3492115417 — Apple MacBook Pro** (500 EUR, rechnerischer Abstand 424 EUR, macbook): Referenz unbelastbar (Streuung 3,64). Weder Chip noch Baujahr noch Speicher genannt - ohne bestimmbares Modell kein Marktwert.
- **3492343677 — USM Haller Regal Rot Sideboard** (649 EUR, rechnerischer Abstand 411 EUR, design-sammeln): Referenz unbelastbar (Streuung 2,93). Masse und Elementzahl fehlen.
- **3492479915 — Herren Trekking Fahrrad** (300 EUR, rechnerischer Abstand 399 EUR, ebike-rad): Weder Marke noch Modell genannt ('Alu Herren Trekkingrad 28 Zoll'); der Median fasst alle Herren-Trekkingraeder zusammen.
- **3492150418 — Cube Fahrrad 29 zoll** (350 EUR, rechnerischer Abstand 350 EUR, ebike-rad): Referenz unbelastbar (Streuung 3,95). Cube Aim HPA ohne Baujahresangabe.
- **3492219851 — Designer Dieter Knoll Wohnlandschaft Schlafsofa Eckcouch Vienna** (500 EUR, rechnerischer Abstand 350 EUR, design-sammeln): Referenz unbelastbar (Streuung 4,38). Polstermoebel von XXXLutz mit einem vom Verkaeufer genannten Neupreis von knapp 2.000 EUR; 500 EUR gebraucht entsprechen dem ueblichen Wertverlauf.
- **3492486151 — Damen Trekking Fahrrad** (300 EUR, rechnerischer Abstand 345 EUR, ebike-rad): Weder Marke noch Modell genannt; der Median fasst alle Damen-Trekkingraeder zusammen.
- **3492229968 — Apple MacBook Air Laptop - Top Zustand** (339 EUR, rechnerischer Abstand 336 EUR, macbook): Weder Chip noch Baujahr noch Speicher genannt, die Aufzaehlung besteht aus Marketingfloskeln ('helles Retina Display', 'komfortable Tastatur'). Ohne bestimmbares Modell kein Marktwert.
- **3492189652 — Herren trekking bike 28 zoll** (350 EUR, rechnerischer Abstand 329 EUR, ebike-rad): Der Median fasst alle 28-Zoll-Trekkingraeder zusammen, unabhaengig von Marke, Baujahr und Ausstattung.
- **3442852508 — Vitra Herman Miller Eames Side Chair La Fonda Stuhl Fiberglas** (275 EUR, rechnerischer Abstand 315 EUR, design-sammeln): Referenz unbelastbar (Streuung 3,00). Fruehes Fiberglas-Exemplar in Vollpolster - eine Variante, fuer die sich keine zwei konkreten Vergleichsangebote belegen liessen.
- **3492389305 — USM Haller Stehpult, Stahlblau** (350 EUR, rechnerischer Abstand 300 EUR, design-sammeln): Deutliche Gebrauchsspuren offengelegt; der Median aus 29 Anzeigen mischt alle Stehpult-Konfigurationen.
- **3492200140 — DJI mini 3 pro** (250 EUR, rechnerischer Abstand 300 EUR, optik-drohnen): Ohne Fernsteuerung, vom Verkaeufer nie getestet, ausdruecklich ohne Funktionsgarantie. Der fehlende Controller und der ungeklaerte Funktionszustand erklaeren den Preis.
- **3492158540 — Herren Trekking Fahrrad** (300 EUR, rechnerischer Abstand 299 EUR, ebike-rad): Median aus nur neun Anzeigen ueber alle Marken; weder Hersteller noch Baujahr genannt.
- **3492238484 — Knoll Antimott Sessel** (229 EUR, rechnerischer Abstand 271 EUR, design-sammeln): Referenz unbelastbar (Streuung 2,60). Altersbedingte Gebrauchsspuren offengelegt.
- **3492120785 — USM Haller Schreibtisch | Trapez-Form | schwarz | Designklassiker** (250 EUR, rechnerischer Abstand 270 EUR, design-sammeln): Der Median 'USM Haller Schreibtisch' mischt alle Plattengroessen; die seltene Trapezform hat keinen eigenen Vergleichswert im Feld.
- **3492048919 — USM Haller Schreibtisch** (250 EUR, rechnerischer Abstand 270 EUR, design-sammeln): Gebrauchsspuren offengelegt; der Median mischt alle Plattengroessen.
- **3492151462 — MacBook Pro M1** (450 EUR, rechnerischer Abstand 250 EUR, macbook): TouchBar defekt, offengelegt. Fuer ein MacBook Pro M1 13 Zoll von 2020 mit diesem Defekt sind 450 EUR marktgerecht.
- **3492161087 — Rennrad Cube** (500 EUR, rechnerischer Abstand 250 EUR, ebike-rad): Referenz unbelastbar (Streuung 2,72). Weder Modell noch Baujahr noch Gruppe genannt.
- **3492478266 — carver trekking rad** (300 EUR, rechnerischer Abstand 250 EUR, ebike-rad): Referenz unbelastbar (Streuung 2,71). Carver Key West mit XT-Ausstattung ohne Baujahresangabe.
- **3492075001 — USM Haller Tisch 200x100 cm Top Zustand** (350 EUR, rechnerischer Abstand 225 EUR, design-sammeln): Der Median mischt alle USM-Tischgroessen und -Farben; 350 EUR fuer eine 200x100-Platte in Perlgrau liegen im ueblichen Korridor.
- **3492136029 — iPhone 14 – 128 GB  * Batterie: 100 % * Speicher: 128 GB** (230 EUR, rechnerischer Abstand 220 EUR, apple-mobil): Median aus nur neun Anzeigen. Der Abstand von 220 EUR ist zu klein, um ohne zwei konkrete Vergleichsangebote desselben Speicher- und Zustandsprofils belegt zu werden.
- **3492116042 — iPhone 15 pro max , 256 gb** (420 EUR, rechnerischer Abstand 180 EUR, apple-mobil): Preis liegt bei 70 Prozent des Medians - unter dem geforderten Mindestabstand von 20 Prozent zu einem bestaetigten Marktwert.
- **3492138216 — Anhänger. HP 500** (200 EUR, rechnerischer Abstand 180 EUR, messtechnik): TUEV abgelaufen. Ein Anhaenger ohne gueltige Hauptuntersuchung ist nicht billig, sondern richtig bepreist.
- **3492126737 — iphone 15 schwarz 128 gb** (250 EUR, rechnerischer Abstand 179 EUR, apple-mobil): Der Median mischt Speichergroessen und Zustaende; ohne belegten Vergleich desselben Modells kein bestaetigter Abstand.
- **3492057142 — DJI Mavic 2 Zoom, viel Zubehör, 2 Akkus wenig benutzt** (279 EUR, rechnerischer Abstand 171 EUR, optik-drohnen): Mavic 2 Zoom von 2018; das Gebrauchtniveau dieser Generation liegt bei rund 250 bis 450 EUR. 279 EUR liegen darin.
- **3492130402 — iPhone 13 mit 256 GB abzugeben , I Phone zu verkaufen** (180 EUR, rechnerischer Abstand 170 EUR, apple-mobil): Der Median mischt Speichergroessen und Zustaende; kleiner absoluter Abstand ohne belegten Vergleich.
- **3492165768 — CANYON Fully Mountainbike 26-Zol** (349 EUR, rechnerischer Abstand 161 EUR, ebike-rad): Der Median fasst alle Canyon-Fullys mit 26 Zoll ueber Modelljahre und Ausstattungsstufen zusammen.
- **3492100915 — Iphone 15 Pro 128 gb** (330 EUR, rechnerischer Abstand 160 EUR, apple-mobil): Preis liegt bei 67 Prozent des Medians, ohne belegten Vergleich desselben Modells und Zustands.
- **3492100535 — iPhone 15, Black, 128 GB gebraucht** (320 EUR, rechnerischer Abstand 158 EUR, apple-mobil): Preis liegt bei 67 Prozent des Medians, ohne belegten Vergleich desselben Modells und Zustands.
- **3492151294 — iPhone 15 128GB** (300 EUR, rechnerischer Abstand 150 EUR, apple-mobil): Preis liegt bei 67 Prozent des Medians, ohne belegten Vergleich desselben Modells und Zustands.
- **3492051681 — iPhone 14 , 256 GB** (300 EUR, rechnerischer Abstand 150 EUR, apple-mobil): Preis liegt bei 67 Prozent des Medians, ohne belegten Vergleich desselben Modells und Zustands.
- **3492057007 — iphone 15 128 GB** (300 EUR, rechnerischer Abstand 147 EUR, apple-mobil): Preis liegt bei 67 Prozent des Medians, ohne belegten Vergleich desselben Modells und Zustands.
- **3492058143 — Iphone 12 Pro Max 256 GB, alles funktioniert, IOS ist aktuell** (150 EUR, rechnerischer Abstand 140 EUR, apple-mobil): Kleiner absoluter Abstand (140 EUR); der Median mischt Speichergroessen und Zustaende.
- **3492160849 — iPhone 13 Pro Max** (220 EUR, rechnerischer Abstand 135 EUR, apple-mobil): Kleiner absoluter Abstand (135 EUR); der Median mischt Speichergroessen und Zustaende.
- **3391147188 — Fritz Hansen Serie 7 Stuhl | Rot** (220 EUR, rechnerischer Abstand 130 EUR, design-sammeln): Der Titel nennt einen Stuhl, der Text zwei. 220 EUR fuer zwei Serie-7-Stuehle waeren ein Abstand, 220 EUR fuer einen nicht - der Widerspruch in der eigenen Anzeige laesst keine Bewertung zu.

## Verworfene Kandidaten: 112 unveraendert aus dem Morgenlauf

Diese Kandidaten standen bereits heute frueh in `candidates.json` und sind im Morgenprotokoll
oben einzeln begruendet. Sie erscheinen erneut, weil bei null gemeldeten Funden nichts in
`deal_log.csv` eingetragen wird. Keine der Begruendungen hat sich geaendert.

- 3491851919 — Porsche  Carrera Cabrio  Tausch möglich (29999 EUR, Abstand 29311 EUR, porsche-911)
- 3491970281 — Tesla Model X Dual (16500 EUR, Abstand 10270 EUR, tesla)
- 3491726519 — Tesla Model 3 Long Range AWD (15900 EUR, Abstand 7500 EUR, tesla)
- 3491583916 — Mercedes-Benz Cabrio W124, E 200 (8700 EUR, Abstand 7050 EUR, youngtimer-alltag)
- 3491762938 — Rolex Submariner mit Original-Papieren (8000 EUR, Abstand 4245 EUR, uhren)
- 3491767420 — Mercedes 280 SE W126 (4490 EUR, Abstand 4082 EUR, youngtimer-alltag)
- 1875648068 — Rolex Submariner "No Date" Oyster Perpetual Edelstahl-Chronometer (7595 EUR, Abstand 3555 EUR, uhren)
- 3491527313 — Honda CB 750 four K (3500 EUR, Abstand 2710 EUR, motorraeder)
- 3491786377 — Honda cb 750 Four supersport (3600 EUR, Abstand 2610 EUR, motorraeder)
- 3491779793 — Bmw E36 320i (4200 EUR, Abstand 2550 EUR, youngtimer-alltag)
- 3491802375 — Neue Omega seamaster Professional 300M Diver (2600 EUR, Abstand 2544 EUR, uhren)
- 3491996683 — Cube Stereo Actionteam (1100 EUR, Abstand 2350 EUR, ebike-rad)
- 3491986568 — Mercedes w124 oldtimer (4200 EUR, Abstand 2190 EUR, youngtimer-alltag)
- 3491602743 — ROLEX OYSTER  PERPETUAL DATE " 34MM " AUTOMATİK (3211 EUR, Abstand 2129 EUR, uhren)
- 3491662621 — Simson S51 - 12V Vape - Neuaufbau (1950 EUR, Abstand 2032 EUR, motorraeder)
- 3492027923 — Simson S51 - 12V Vape - Neuaufbau (1950 EUR, Abstand 2032 EUR, motorraeder)
- 3491673080 — Simson s50/s51 (1000 EUR, Abstand 1966 EUR, motorraeder)
- 3491619054 — Rolex Datejust 36 Sunburst Dial Weißgold Lünette 1601 (3900 EUR, Abstand 1920 EUR, uhren)
- 3492012069 — Canyon speedmax CF 8 M Grau Triathlon Rennrad (1899 EUR, Abstand 1791 EUR, ebike-rad)
- 3491547314 — Mercedes Benz W124 230E (3500 EUR, Abstand 1540 EUR, youngtimer-alltag)
- 3492003821 — Tudor Oyster Prince Tuxedo (1200 EUR, Abstand 1540 EUR, uhren)
- 3491871311 — Simson S50 zu verkaufen (1800 EUR, Abstand 1462 EUR, motorraeder)
- 3491979588 — Simson Schwalbe KR51/2 ,vape,motor neu  4 gang (1800 EUR, Abstand 1350 EUR, motorraeder)
- 3491994933 — E-Bike Hercules Futura Comp I-10, Bosch CX Motor, wenig Kilometer (1350 EUR, Abstand 1100 EUR, ebike-rad)
- 3491703598 — Simson Schwalbe KR 51/1 Ersatzteile Konvolut für Neuaufbau (1500 EUR, Abstand 1020 EUR, motorraeder)
- 3491702883 — Simson S50 N (1900 EUR, Abstand 979 EUR, motorraeder)
- 3492037402 — Apple macbook pro .top letzte version  neue 2023 (330 EUR, Abstand 920 EUR, macbook)
- 3491961135 — Yanmar, Dieselmotor, Motor (1500 EUR, Abstand 829 EUR, camper-marine)
- 3491978809 — Truma Mover Smart A mit Truma Mover Powerset (1499 EUR, Abstand 700 EUR, camper-marine)
- 3492002154 — Macbook pro M4 (1250 EUR, Abstand 700 EUR, macbook)
- 3491597139 — Original USM Haller - Designklassiker auf Rollen (650 EUR, Abstand 699 EUR, design-sammeln)
- 2778957565 — USM Haller Sideboard Weiß Perforiert (773 EUR, Abstand 654 EUR, design-sammeln)
- 3491676406 — Apple MacBook Pro (2023) Laptop 1TB (750 EUR, Abstand 600 EUR, macbook)
- 3491628133 — USM Haller Lowboard Schwarz mit Einschubtüre + Rollen (550 EUR, Abstand 550 EUR, design-sammeln)
- 3199210234 — Usm Haller Sideboard Schwarz (919 EUR, Abstand 530 EUR, design-sammeln)
- 3492013729 — iPhone 17 256 (549 EUR, Abstand 500 EUR, apple-mobil)
- 3491765267 — USM Haller Sideboard Regal weiß (950 EUR, Abstand 476 EUR, design-sammeln)
- 3492017357 — Gravel-Bike Cube Road/Nuroad SL Gr. 56 (680 EUR, Abstand 469 EUR, ebike-rad)
- 3491571811 — Ortler E-Bike mit Bosch Active Line - fahrbereit (500 EUR, Abstand 418 EUR, ebike-rad)
- 3491640679 — Apple MacBook Pro Space Gray mit OVP und Zubehör (499 EUR, Abstand 400 EUR, macbook)
- 3491693178 — Trek Fahrrad 29 Zoll – Türkis – Rahmengröße M/L (300 EUR, Abstand 400 EUR, ebike-rad)
- 3491511905 — USM Haller Tisch 200 x 100, perlgrau, gebraucht (200 EUR, Abstand 395 EUR, design-sammeln)
- 3491655988 — Cube Mountainbike (300 EUR, Abstand 374 EUR, ebike-rad)
- 3491547550 — Fahrrad Trekking Bike Herren (550 EUR, Abstand 360 EUR, ebike-rad)
- 3492033383 — MacBook Pro (450 EUR, Abstand 358 EUR, macbook)
- 3491566465 — Apple MacBook Air 13 (349 EUR, Abstand 350 EUR, macbook)
- 3491859551 — Cube Town Pro E-Bike mit Bosch Motor schwarz (600 EUR, Abstand 350 EUR, ebike-rad)
- 3491881952 — DJI Air 3 more flight Pack (460 EUR, Abstand 350 EUR, optik-drohnen)
- 3491991296 — [TOP PREIS] USM Haller Gardarobe in Anthrazitgrau (300 EUR, Abstand 350 EUR, design-sammeln)
- 3491512707 — DJI mini 5 pro (550 EUR, Abstand 349 EUR, optik-drohnen)
- 3491607380 — Mountainbike CUBE (330 EUR, Abstand 344 EUR, ebike-rad)
- 3491988526 — MacBook Pro M1 16GB RAM 512 GB SSD Touch Bar (500 EUR, Abstand 340 EUR, macbook)
- 3491938387 — Canyon Nerve Fully (300 EUR, Abstand 324 EUR, ebike-rad)
- 3491660582 — Canyon Roadlite Fitnessbike in Gelb Größe S (499 EUR, Abstand 320 EUR, ebike-rad)
- 3491676369 — Technics SL-1210 MK2 (480 EUR, Abstand 320 EUR, vintage-hifi)
- 3491674753 — SHIMANO DURA ACE Kurbelgarnitur – FC-R9200 – 172,5 mm – 52/36 Z. (300 EUR, Abstand 320 EUR, ebike-rad)
- 3491991746 — iphone 15 pro max 256gb (280 EUR, Abstand 310 EUR, apple-mobil)
- 3492012365 — Cube MTB 29" (350 EUR, Abstand 308 EUR, ebike-rad)
- 3491928947 — MacBook Pro M1 (385 EUR, Abstand 304 EUR, macbook)
- 3491647366 — Meissen Porzellan Kaffeeservice Wellenspiel Relief Waldflora (499 EUR, Abstand 281 EUR, design-sammeln)
- 3491765954 — Cube AMS Pro Fully Fullsuspension Mountainbike (325 EUR, Abstand 275 EUR, ebike-rad)
- 3491856322 — Cube Herren Trekkingrad (325 EUR, Abstand 265 EUR, ebike-rad)
- 3491619784 — Trek Fuel EX Fully Mountainbike 26 Zoll – reparaturbedürftig (400 EUR, Abstand 264 EUR, ebike-rad)
- 3491774201 — Gut erhaltenes Cube Access Mädchen/Damen Mountainbike (420 EUR, Abstand 255 EUR, ebike-rad)
- 3466638391 — Stuhl Eames EA 107 Miller Vintage Hopsack Sessel Vitra (495 EUR, Abstand 255 EUR, design-sammeln)
- 3491646864 — iPhone 15 pro 128gb (250 EUR, Abstand 250 EUR, apple-mobil)
- 3491620990 — Canyon Ultimate AL Rennrad XL (500 EUR, Abstand 250 EUR, ebike-rad)
- 3491537761 — USM Haller Schreibtisch 175x75cm (250 EUR, Abstand 250 EUR, design-sammeln)
- 3491956700 — CUBE 29 Zoll MTB (300 EUR, Abstand 250 EUR, ebike-rad)
- 3491806554 — DJI Mini 3 Pro Fly More Combo RC (300 EUR, Abstand 250 EUR, optik-drohnen)
- 3492029124 — Cube Hyde Race mit Riemenantrieb (400 EUR, Abstand 249 EUR, ebike-rad)
- 3492027051 — iPhone 15 Pro 128GB (280 EUR, Abstand 220 EUR, apple-mobil)
- 3491961417 — Louis Poulsen Lampe (175 EUR, Abstand 215 EUR, design-sammeln)
- 3492004374 — Cube Aim SLX Mountainbike XL 29 Zoll (300 EUR, Abstand 200 EUR, ebike-rad)
- 3491976022 — iPhone 15 128 GB Weiß (300 EUR, Abstand 199 EUR, apple-mobil)
- 3491852030 — Mountainbike Canyon Nerve AL+ (440 EUR, Abstand 199 EUR, ebike-rad)
- 3491828657 — Canyon Rennrad Ultimate AL F8 Größe M schwarz (450 EUR, Abstand 199 EUR, ebike-rad)
- 3491933836 — Cube Nature Pro Crossbike Größe L (350 EUR, Abstand 194 EUR, ebike-rad)
- 3491857306 — iPhone 14 Pro Apple (230 EUR, Abstand 190 EUR, apple-mobil)
- 3491835949 — iPhone 13 Pro Max (180 EUR, Abstand 185 EUR, apple-mobil)
- 3491825819 — MTB 26" Cube Reaction SL (320 EUR, Abstand 180 EUR, ebike-rad)
- 3491814733 — Vitra Headline Bürodrehstuhl mit Kopfstütze (299 EUR, Abstand 176 EUR, design-sammeln)
- 3491845957 — Cube Mountainbike (375 EUR, Abstand 175 EUR, ebike-rad)
- 3492025232 — Apple iPhone 15 – 256 GB – Schwarz – Top Zustand (380 EUR, Abstand 170 EUR, apple-mobil)
- 3491998025 — Schreibtisch USM Haller (350 EUR, Abstand 170 EUR, design-sammeln)
- 3491824276 — Cube AMS 100 Fully Mountainbike 26 Zoll (385 EUR, Abstand 165 EUR, ebike-rad)
- 3491990509 — Apple iPhone 15 (320 EUR, Abstand 160 EUR, apple-mobil)
- 3492019639 — Korg Minilogue XD (320 EUR, Abstand 160 EUR, musikinstrumente)
- 3491971300 — iPhone 15 128 GB – Black – guter Zustand (320 EUR, Abstand 158 EUR, apple-mobil)
- 3491906115 — iPhone 14 128 GB (200 EUR, Abstand 150 EUR, apple-mobil)
- 3491823966 — iPhone 14 128 gb (200 EUR, Abstand 150 EUR, apple-mobil)
- 3491954922 — iphone 15 128  gb grün (250 EUR, Abstand 150 EUR, apple-mobil)
- 3491909360 — iphone  14 Pro Max (300 EUR, Abstand 150 EUR, apple-mobil)
- 3492026283 — MacBook Air 13” – 8 GB RAM / 256 GB SSD (350 EUR, Abstand 150 EUR, macbook)
- 3491901501 — Thorens TD 145 Plattenspieler (140 EUR, Abstand 144 EUR, vintage-hifi)
- 3492027481 — Apple IPhone 12 und IPhone 13 (175 EUR, Abstand 144 EUR, apple-mobil)
- 3491902082 — Iphone 15 128gb (310 EUR, Abstand 140 EUR, apple-mobil)
- 3491906246 — IPhone 15 128gb (310 EUR, Abstand 140 EUR, apple-mobil)
- 3491956717 — Iphone 12 Pro 512 gb grau (185 EUR, Abstand 135 EUR, apple-mobil)
- 3491891057 — Hilti Bohrmaschine TE 6-S (175 EUR, Abstand 125 EUR, werkzeug-maschinen)
- 3491919538 — ⭐️ APPLE IPHONE 14 ⭐️ 128GB MIDNIGHT (199 EUR, Abstand 121 EUR, apple-mobil)
- 3491815829 — iPhone 12 Pro Max (160 EUR, Abstand 110 EUR, apple-mobil)
- 3491991711 — iPhone 13 128 GB (150 EUR, Abstand 100 EUR, apple-mobil)
- 3491874845 — Iphone 12 pro Max 128 GB *Glassprung Beidseitig* (170 EUR, Abstand 100 EUR, apple-mobil)
- 3491819900 — Apple iPhone 13 (200 EUR, Abstand 100 EUR, apple-mobil)
- 3491987339 — iPhone   13 (200 EUR, Abstand 100 EUR, apple-mobil)
- 3492037913 — 2x Technics SL-1200MK2 Silber – DJ-Set, frisch fachgewartet (1749 EUR, Abstand 0 EUR, vintage-hifi)
- 3492015011 — Schwebetüren Schrank von Haushaltsauflösung (300 EUR, Abstand 0 EUR, notverkaeufe)
- 3492016500 — Pokemon Sammlungsauflösung [SEALED] (686 EUR, Abstand 0 EUR, notverkaeufe)
- 3492008771 — Scheunenfund + Motorschaden!! Ford Probe II 2.0 16V "Highlight" (1150 EUR, Abstand 0 EUR, notverkaeufe)
- 3492044866 — Accuphase E 307 with Phono AD 9 (2400 EUR, Abstand 0 EUR, vintage-hifi)
- 3492042412 — Funko Pop Sammlungsauflösung (500 EUR, Abstand 0 EUR, notverkaeufe)
