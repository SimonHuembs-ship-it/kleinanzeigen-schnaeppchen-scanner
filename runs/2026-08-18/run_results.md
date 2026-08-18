# Lauf 2026-08-18, morgens (07:07 Uhr MESZ)

`candidates.json` generiert: 2026-08-18T06:39:57+02:00 (28 min alt, klar innerhalb der
Vier-Stunden-Grenze aus Schritt 1). Zeitraum des Sammellaufs: 2026-08-18T01:25:11+02:00 bis
2026-08-18T06:25:11+02:00, gesichtet 24.496 Anzeigen.

- Kandidaten in `candidates.json`: 199
- davon schon in `deal_log.csv`: 0 (56 Eintraege im Log, keine Ueberschneidung)
- Referenz nicht belastbar (`belastbar: false`, Streuung > 2,5 oder `referenz: null`): 50 —
  Median als nicht vorhanden behandelt, davon 9 komplett ohne Referenz
- inhaltlich geprueft: 61 (sortiert nach absoluter Ersparnis, dazu vollstaendig alle
  Kandidaten der liquiden Kategorien `tesla`, `uhren`, `apple-mobil`, `macbook`,
  `optik-drohnen`, `konsolen-sweep` und `foto-sweep`; die uebrigen 138 liegen unter 300 Euro
  absoluter Ersparnis oder sind Massenware aus `ebike-rad` und `design-sammeln` mit
  gemischtem Median)
- `unkenntnis_bonus` in diesem Lauf: 5 Kandidaten, alle geprueft, siehe eigener Abschnitt
- gemeldete Funde: 1

Hinweis zur Recherche: die Netzwerkrichtlinie dieser Umgebung blockiert den Direktabruf von
chrono24.com, buycycle.com, bikeflip.com, bicyclebluebook.com, marktplatz.bike und
kleinanzeigen.de. Die Marktwertbestaetigung lief deshalb ausschliesslich ueber Websuche. Wo
das keine zwei konkreten Vergleichsangebote desselben Modells ergab, wurde verworfen statt
geschaetzt.

## Funde

| Ware | Preis | bestaetigter Marktwert | Abstand | Ort |
|---|---|---|---|---|
| [BMC Teammachine ALR ONE, RH 54, SRAM Rival eTap AXS](https://www.kleinanzeigen.de/s-anzeige/bmc-rennrad-teammachine-sram-etap-rival-axs/3486753338-230-4915) | 1.500 € | gebraucht 2.943 € (buycycle, dasselbe Modell mit derselben Rival-eTap-AXS-Gruppe); neu 3.123–3.599 € (bike-room.com, MJ 2023/2024); UVP 3.999 € (marktplatz.bike) | −32 % auf ein konservativ angesetztes privates Niveau von 2.200 €, −49 % auf den belegten Gebrauchtpreis | Niedernhausen |

Beleg:

- **BMC Teammachine ALR ONE** — die Anzeige nennt Modell ("Teammachine ALR ONE"),
  Rahmenmaterial (Alu mit Carbongabel), Rahmenhoehe (54 cm) und Gruppe (SRAM eTap Rival AXS
  2x12) exakt, das Produkt existiert genau so. Zwei konkrete Vergleichsangebote desselben
  Modells mit derselben wesentlichen Ausstattung: ein gebrauchtes Teammachine ALR ONE 2023
  mit Rival eTap AXS auf buycycle zu 2.943 €, und Neuangebote auf bike-room.com zu 3.123 €
  (MJ 2024) beziehungsweise 3.599 € (MJ 2023); marktplatz.bike fuehrt die UVP des MJ 2023 mit
  3.999 €. Zusaetzlich als Untergrenze: allein das Teammachine-**Rahmenset** in RH 54 mit
  Rival XPLR AXS kostet auf eBay.de 1.299 € — der Kandidat ist ein komplettes Rad fuer
  1.500 €. Weil Plattformpreise ueber Privatpreisen liegen, rechne ich konservativ mit
  2.200 bis 2.400 € privatem Gebrauchtniveau; 1.500 € liegen selbst dagegen 32 Prozent
  darunter.
  Ein wertmindernder Grund ist nicht erkennbar: kein Defekt, kein Sturzschaden, kein
  Verschleiss genannt, laut Verkaeufer "2x um den Block gefahren" und ohne Gebrauchsspuren.
  Verkaeuferprofil passt zur Leitidee: Konto seit 2023, Bewertung 0,92 mit allen drei
  Abzeichen auf Stufe 2, **nur Abholung, kein Versand, kein Kaeuferschutz**, 7 Bilder,
  Festpreis ohne Verhandlungsdruck — das ist das Muster eines Privatverkaeufers, der das Rad
  loswerden will, nicht das eines Betrugsinserats mit Versandangebot.
  Der Kleinanzeigen-Median von 3.499 € (n = 99) wurde **nicht** als Massstab verwendet:
  `referenz.belastbar` steht auf `false` und die Suchanfrage "BMC RENNRAD Teammachine" mischt
  Carbon-SLR- mit Alu-ALR-Modellen. In `deals.json` steht deshalb statt `ersparnis_eur` ein
  `referenz_hinweis` mit dem selbst bestaetigten Niveau, damit die Mail keine
  Phantomersparnis von 1.999 € ausweist.

## Verworfene Kandidaten

### Groesste absolute Abstaende zuerst — Fahrzeuge

- **Tesla Model 3 Performance, EZ 01/2019, 319.000 km, 17.900 € (3487600256)** — groesster
  Rohabstand des Laufs (9.055 € unter Median). Der Preis erklaert sich von selbst: 319.000 km
  liegen weit jenseits der Akkugarantie (Model 3 Performance: 8 Jahre / 192.000 km), die
  Garantie ist nach Alter **und** Laufleistung erloschen. Die Anzeige nennt selbst "bei 100%
  kann man 400 km fahren" gegen rund 530 km WLTP im Neuzustand, also etwa 75 Prozent
  Restkapazitaet. Korrekt bepreistes Angebot, kein Fund. Pflicht-Warnflag Tesla
  (Kilometerstand gegen Akkugarantiegrenze) trifft zu und ist genau der Grund fuer die
  Verwerfung.
- **Tesla Model Y Dual Motor AWD, EZ 11/2022, 205.000 km, 19.100 € (3486805545)** — die
  Anzeige sagt selbst: "Schweizer Papiere (Preis fuer EU +10% Zoll +19% MwSt)". Der reale
  Landepreis liegt bei rund 25.000 €, nicht bei 19.100 €. Dazu 205.000 km (Akkugarantie
  Model Y AWD 8 Jahre / 192.000 km bereits ueberschritten) und ein Riss in der
  Windschutzscheibe. Keine Ersparnis, sondern eine unvollstaendige Preisangabe.
- **Mercedes-Benz 300 D/W124, EZ 05/1991, 450.500 km, 5.500 € (3487494408)** — sehr ehrliche,
  detaillierte Anzeige (instandgesetzter Rost an Kotfluegeln und Seitenteilen, defekte
  Gurtgeber, Schiebedach nur kippbar). Genau diese Offenheit macht aber auch klar, warum der
  Preis stimmt: 450.500 km plus Rostinstandsetzungen. Ohne Zustandsnote aus einer Fachquelle
  (classic-analytics Zustand 3 war ueber Websuche fuer diese Baureihe nicht belegbar zu
  bekommen) kein bestaetigter Marktwert. Zusaetzlich: Verkaeuferkonto am Anzeigentag
  angelegt.
- **Mercedes W124 230 CE, 3.200 € (3486934765)** — maessig reparierter Heckschaden, Rost an
  Radlaeufen und unter der Heckklappe, Front- **und** Heckscheibe gerissen. Preis erklaert
  sich vollstaendig aus dem Zustand.
- **BMW e36 323i Automatik, EZ 04/1997, 315.000 km, 5.999 € (3487485313)** — TUEV abgelaufen,
  315.000 km, eingetragenes Fahrwerk und Zubehoerauspuff (bei einem E36 eher wert- als
  preismindernd). 6.000 € sind fuer diesen Zustand kein Abschlag, sondern der Markt.
- **Mercedes 190 W201, 3.900 € (3487571639)**, **BMW E36 316 Limo, 1.500 € (3487405875)** —
  Median aus gemischten Zustandsklassen, keine zwei belastbaren Vergleichsangebote mit
  vergleichbarer Laufleistung und Zustandsbeschreibung gefunden.
- **Honda CBR 929 Fireblade, Bj. 2000, 85.000 km, 1.500 € (3486814216)**, **Vespa Sprint 50,
  Bj. 2014, 10.500 km, 1.999 € (3486855044)**, **Ducati Monster 750, Bj. 2001, 26.500 km,
  2.990 € (3486968507)** — alle drei liegen im normalen Marktband ihres Modells; bei der
  Fireblade erklaeren 85.000 km den Preis zusaetzlich.

### Uhren — der Median mischt Referenzen, die Einzelpruefung ergibt Marktpreis

Durchgaengiges Muster: der Kleinanzeigen-Median einer Modellfamilie ("Rolex Datejust",
"Omega Seamaster Diver 300", "Tudor Black Bay") mischt Stahl, Gold, Groessen und Kaliber.
Sobald man die Referenznummer der einzelnen Anzeige gegen den Markt haelt, verschwindet der
Abstand.

- **Rolex Submariner Date, Bj. 2001, Box/Papiere/Rechnung, 7.750 € (3486845681)** — der
  aussichtsreichste Uhrenkandidat, trotzdem verworfen. Bestaetigtes Niveau fuer die
  Referenz 16610: watch.de fuehrt ein Exemplar von 2001 zu 9.449 €, ein Full Set von 2001
  wurde auf eBay.de zu 10.900 € verkauft, uhrenworld liegt bei 12.480 €. Das sind
  **Haendlerpreise inklusive Marge**; das private Niveau liegt darunter, sodass 7.750 € die
  20-Prozent-Schwelle nicht sicher reissen. Dazu kommt: die Anzeige nennt in drei Zeilen
  weder Referenznummer noch Gehaeusegroesse, und bei einer Uhr dieser Preisklasse ist das
  ohne eigene Inaugenscheinnahme kein bestaetigter Fund.
- **Rolex Yachtmaster Everrose, "Baujahr 2026, neu vom Juwelier", 12.345 € (3487225324)** —
  ein Bild, Feld "Referenz:" leer gelassen, "Gehaeusedurchmesser: ich meine 40 mm". Bei einem
  angeblich fabrikneuen Stueck knapp unter Listenpreis ist die fehlende Referenznummer kein
  Unkenntnis-Signal, sondern das Gegenteil eines Belegs. Modell nicht bestimmbar, verworfen.
- **Rolex Datejust 41 Ref. 126300, Bj. 2019, Box/Papiere, 8.400 € (3303074523)** — gut
  dokumentiert (10 Bilder, Referenz, Jahr), aber gewerblicher Verkaeufer. Gebrauchtband fuer
  126300 laut Chrono24-Uebersicht 7.999 bis 15.500 €, Full Sets ungetragen ab 8.599 €. 8.400 €
  liegen am unteren Rand des Marktes, nicht 20 Prozent darunter.
- **Rolex Datejust, Gelbgold 750, ohne Box und Papiere, 5.500 € (3487501032)** — keine
  Referenznummer, keine Groesse, keine Jahresangabe; nachtraeglich gesetzte Diamanten an den
  Indizes senden den Wert eher, als sie ihn heben. Marktwert nicht bestimmbar.
- **Rolex Datejust Ref. 16233, Bj. 1997, 6.999 € (3413156677)** — sehr sauber beschriebener
  Haendlerartikel, genau deshalb zum Marktpreis. Kein Abschlag.
- **Rolex Datejust 36mm, 4.000 € (3486944636)** — drei Zeilen, keine Referenz, Verkaeufername
  "Berlin Watches" auf Privatprofil bei Bewertung 0,50.
- **Rolex Oysterdate 6694, 2.150 € (3486817347)** — Roulette-Datum ist ein echtes
  Sammlermerkmal, 2.150 € sind dafuer aber der Markt.
- **Omega Seamaster Aqua Terra Ref. 2518.50.00, 36 mm Quarz, 1.900 € (3487211419)** — der
  Median von 3.690 € stammt aus 41-mm-Automatikmodellen. Eine 36-mm-Quarz-Aqua-Terra liegt bei
  1.400 bis 2.000 €: Phantomersparnis.
- **Omega Seamaster Diver 300M Ref. 2533.50.00, 2.780 € (3438515446)** (Pfandhaus, Marktpreis),
  **Omega Seamaster Diver 300M Chronograph Ref. 213.30.42.40.01.001 Full Set, 2.950 €
  (3487413893)**, **Omega Seamaster GMT "Great White", ohne Papiere, 2.900 € (3487260142)**,
  **Omega Speedmaster Reduced, 1.999 € (3486867191)** (Bewertung 0,42), **Omega Constellation
  Pie Pan, 1.350 € (3486785448)** (Glas und Zeiger getauscht — wertmindernd) — alle im
  Marktband ihres konkreten Modells.
- **Tudor Black Bay Bronze Ref. 79350BM, 2.750 € (3461790295)** (gewerblich,
  differenzbesteuert, Marktpreis), **Tudor Black Bay Red 79230R Full Set, 2.599 €
  (3487371578)** — Marktpreis.
- **TAG Heuer Carrera Calibre 16 CV2010.BA0794, 1.350 € (3486788128)**, **TAG Heuer Aquaracer
  Calibre 5, ohne Box/Papiere, 780 € (3487567852)**, **TAG Heuer Aquaracer Quarz aus
  Haushaltsaufloesung, 679 € (3487311644)** — der Median von 1.900 € mischt Automatik- und
  Quarzmodelle; die Quarzvariante liegt bei 600 bis 900 €.

### Apple und Elektronik — Pflicht-Warnflags und Betrugsmuster

- **MacBook Pro 14" M4 (A3112, MW2U3D/A), 16/512 GB, 659 € (3487024672)** — 39 Prozent des
  Marktwerts bei exakter Modell- und Bestellnummer, "Akku 100 %", keinerlei Maengel, Versand
  per DHL/Hermes und eine Laptoptasche gratis dazu. Das ist genau das handwerklich gute
  Inserat aus der Leitidee, nicht die schlechte Anzeige eines ehrlichen Verkaeufers. Bei rund
  1.400 € realem Gebrauchtwert ist der Abstand zu gross, um plausibel zu sein. Verworfen.
- **"MacBook Pro m5", 1.350 € (3487186545)** — Konto 30 Tage alt, Attribute widersprechen
  sich (M4 gegen M5, 15" gegen 16"), Beschreibungstext generisch bis maschinell. Verworfen.
- **MacBook Pro M5, 16/512 GB, 1.380 € (3486871929)** — das M5-MacBook-Pro 14" kam im Oktober
  2025 zu 1.799 € UVP; gebraucht liegt es bei rund 1.400 bis 1.500 €. Kein 20-Prozent-Abstand.
- **iPhone 17 Pro Max 256 GB, 680 € (3487570590)** — Konto 152 Tage, keine Bewertung, nur
  Versand, "keine Dellen keine Kratzer" bei 40 Prozent unter Markt. Verworfen.
- **iPhone 17 Pro 256 GB Orange, 730 € (3487550640)** — die Anzeige nennt selbst "einige
  Kratzer und Dellen" am Gehaeuse. Zustandsbereinigt liegt der Markt bei 850 bis 900 €, der
  Abstand damit unter 20 Prozent.
- **Uebrige `apple-mobil`-Kandidaten (iPhone 12 bis 16, 34 Stueck)** — durchgaengig unter
  250 € absoluter Ersparnis; die Mediane sind eng (Streuung 1,2–1,5) und die Angebote liegen
  im normalen Zustands- und Speicherkorridor. Fuer alle gilt ohnehin das Pflicht-Warnflag
  iCloud-Aktivierungssperre und MDM, das aber ohne Fund nicht zu melden ist.
- **PlayStation 5 Pro mit Laufwerk und MediaMarkt-Beleg, 470 € (3487542010)** — Referenz nicht
  belastbar (Streuung 5,8). Die Anzeige fordert bei Versand "PayPal per Freunde", also Zahlung
  ausserhalb des Kaeuferschutzes: Warnsignal nach Schritt 2c. Absoluter Abstand ohnehin gering.
- **Steam Deck 512 GB, 400 € (3486812476)** — Marktpreis.

### Drohnen und Foto

- **DJI Mini 3 Pro mit ESC-Fehler, 330 € (3486958166)** — als defekt beschrieben, Gimbal
  getauscht, Start nicht moeglich. Vorbildlich ehrliche Anzeige, aber der Preis erklaert sich
  vollstaendig.
- **DJI Mavic Pro Fly More Combo, 250 € (3487228346)** und **DJI Mavic Pro Platinum, 280 €
  (3487437775)** — beide mit `belastbar: false` (Streuung 4,5 beziehungsweise 4,7). Die
  Mavic-Pro-Generation von 2016/2017 liegt gebraucht bei 300 bis 450 €; der Abstand ist zu
  klein und der absolute Betrag zu gering fuer eine Meldung.
- **DJI Mavic Air 2, 210 € (3486839357)**, **DJI Mavic Air Fly More Combo, 220 €
  (3487174186)** — im Marktband.
- **Leica R Vario-Elmar 28-70, 225 € (3486839639)** — makelloses Verkaeuferprofil (Bewertung
  1,00, alle Abzeichen Stufe 2). Das Objektiv ist aber die von Sigma gefertigte R-Variante mit
  entsprechend flachem Preisniveau; usedlenstracker liess sich per Websuche nicht mit zwei
  konkreten Abschluessen zu genau diesem Objektiv belegen, und der absolute Abstand betraegt
  150 €. Verworfen ohne bestaetigten Referenzwert, statt zu schaetzen.
- **Carl Zeiss Vario-Sonnar T*, 200 € (3487493676)** — Anzeige nennt weder Brennweite noch
  Anschluss; Produkt nicht bestimmbar.

### Fahrraeder und E-Bikes (57 Kandidaten, die grosse Masse des Laufs)

- **BMC URS 01 FOUR Gravel, Kauf 10/2023 mit Rechnung, 2.350 € (3486805826)** — der zweite
  aussichtsreiche Kandidat, sauber verworfen: UVP 5.299 €, realer Neupreis zuletzt rund
  3.200 €, aufbereitete Exemplare werden mit rund 2.159 € gefuehrt. 2.350 € liegen damit
  **ueber** dem belegten Aufbereitungsniveau. Kein Fund.
- **Santa Cruz Nomad CC X01 Air, MJ 2020, Gr. XL, 2.950 € (3487560455)** — nur ein Bild bei
  einem 3.000-Euro-Rad, Konto 312 Tage. Gebrauchtband fuer ein 2020er Nomad CC X01 liegt bei
  2.800 bis 3.800 €, der Preis also im Band.
- **Canyon Spectral CF 8, MJ 2021, 2.000 km, 1.700 € (3487550487)** — ehrliche Anzeige, aber
  gegen ein privates Gebrauchtniveau von 1.800 bis 2.200 € kein 20-Prozent-Abstand.
- **Canyon Speedmax CF, MJ 2018, Shimano 105, 1.600 € (3487578557)** — Triathlonraeder
  verlieren stark; 1.600 € sind fuer ein 2018er Speedmax CF 105 der Markt.
- **Brompton Elektro-Klapprad "Black Edition", MJ 2022, mit Rechnung, 1.900 €
  (3487564745)** — Brompton ist liquide Ware und der Kandidat wurde deshalb vorgezogen
  geprueft. Es liessen sich per Websuche jedoch **keine zwei konkreten Vergleichsangebote**
  eines 2022er Brompton Electric finden (die Treffer betrafen 2019er Modelle und
  Titan-Varianten). Ohne belastbaren Referenzwert verworfen statt geschaetzt.
- **KTM Macina Style 730, MJ 2023, 3.255 km, 1.745 € (3487602347)** — gut dokumentiert, aber
  Verkaeuferbewertung 0,33; gegen ein Gebrauchtniveau von 1.900 bis 2.300 € grenzwertig unter
  20 Prozent.
- **Giant Explore Trekking XL, 450 € (3487001273)** — Musterfall Phantomersparnis: der Median
  von 1.669 € stammt ueberwiegend aus dem **Giant Explore E+**, also der E-Bike-Variante. Ein
  mechanisches Explore mit Nexus liegt bei 450 bis 600 €.
- **Cube-Kandidaten (28 Stueck von "Cube Race One" bis "Cube AMS")** — bei fast allen ist der
  Median aus Hardtails, Fullys und E-Bikes derselben Modellfamilie gemischt (Streuung 2,0 bis
  5,2). Wo die Referenz belastbar war, lagen die Preise im normalen Gebrauchtband der
  jeweiligen Ausstattung.
- **Uebrige `ebike-rad`-Kandidaten** — unter 300 € absoluter Ersparnis oder ohne
  Modellbezeichnung, die eine Marktwertbestaetigung erlauben wuerde.

### Design, Musik, Werkzeug, Notverkaeufe

- **Gibson Les Paul Standard, 790 € (3472750505)** — die Anzeige ist bemerkenswert ehrlich:
  urspruenglich Linkshaenderinstrument, auf Rechtshaender umgebaut, Kopfplattenbruch
  fachgerecht repariert, und die Seriennummer wurde herausgefraest und durch eine Metallplatte
  ersetzt. Jeder einzelne Punkt senkt den Wert erheblich, zusammen erklaeren sie den Preis
  vollstaendig. Kein Fund, sondern ein korrekt bepreistes Instrument.
- **Gibson Les Paul Gothic Morte 2011, 620 € (3487287138)**, **Fender Jazz Bass Player
  Series, 575 € (3487211378)**, **Gibson Les Paul Special 2001, 1.170 € (3486984605)** —
  Referenz nicht belastbar (Streuung 3,2 bis 3,5) beziehungsweise Marktpreis.
- **Neumann TLM 103 D AES42, 850 €, `referenz: null` (3487579277)** — "wurde mir geschenkt und
  ich kann es nicht nutzen" ist ein starkes Unkenntnis-Signal. Die Recherche ergab aber nur
  Preise fuer die **analoge** TLM 103 (gebraucht rund 800 bis 1.140 USD); zur digitalen
  AES42-Variante liess sich kein belastbarer Gebrauchtpreis finden. Und die AES42-Version
  braucht einen digitalen Vorverstaerker, was den Kaeuferkreis real verkleinert und einen
  Abschlag rechtfertigt. Ohne bestaetigten Referenzwert verworfen.
- **Fraesmaschine mit Zubehoer, 1.800 € (3486795636)** — Erbstueck, ehrliche Anzeige, aber die
  Anzeige nennt weder Hersteller noch Typ. Ohne Modellbezeichnung ist kein Marktwert
  bestimmbar.
- **USM-Haller-Kandidaten (9 Stueck, 190 bis 920 €)** — USM-Preise haengen vollstaendig an
  Konfiguration und Abmessung. Bei den Anzeigen mit dem groessten Rohabstand (Sideboard
  schwarz 4 Faecher zu 900 €, Sideboard schwarz/reinweiss zu 650 €) fehlen entweder die Masse
  oder es handelt sich um kleine Korpusse; der Median aus 97 gemischten Konfigurationen ist
  kein Massstab.
- **Vitra, Knoll, Thonet, Cassina, Walter Knoll (18 Kandidaten)** — durchgehend unter 500 €
  absoluter Ersparnis, ueberwiegend mit gemischtem Median.
- **8 Kandidaten aus `notverkaeufe` (`referenz: null`)** — Werkstattliteratur Audi TT und
  Audi V8, Pruefrex Motortester, zwei Kukirin-G2-Scooter mit Zeitdruck-Textbausteinen
  ("WER HEUTE KOMMT 390 €"), Huelsta-Schlafzimmer, Nissan-Motor, Mercedes C280. Kein
  Kleinanzeigen-Median vorhanden; fuer keines dieser Objekte liess sich per Websuche ein
  belastbarer Marktwert mit zwei Vergleichsangeboten bestimmen. Die Zeitdruck-Formulierungen
  der Kukirin-Anzeigen sind zusaetzlich ein Warnsignal nach Schritt 2c.

### Kandidaten mit `unkenntnis_bonus` (nicht nach Anzeigenqualitaet heruntergewertet)

Fuenf Stueck in diesem Lauf. Alle wurden bevorzugt geprueft und ausdruecklich **nicht** wegen
schlechter Anzeigenqualitaet verworfen, sondern jeweils am fehlenden Marktwertabstand:

- **"Fahrrad Cube Race One", 550 € (3486936923)** — Tippfehler im Text ("Zusatnd",
  "Harttail"), Modellname falsch zusammengesetzt, Maengel offengelegt, nur Abholung: genau das
  Muster der Leitidee. Die Referenz ist aber nicht belastbar (Streuung 4,0), und ein Cube
  Hardtail mit XT-Bremsen und 2x12 liegt gebraucht bei 700 bis 900 € — der Abstand ist real,
  aber mit 200 bis 350 € zu klein und ohne zwei konkrete Vergleichsangebote nicht belegbar.
- **Bulls E-Trekking "Street Mover E", 800 € (3486805093)** — Bosch-Motor und Akkugroesse
  werden im Text vermischt ("500 Watt Bosch CX Akku"), was zum Unkenntnis-Bild passt. Gegen
  ein Gebrauchtniveau von 900 bis 1.400 € fuer ein Bulls-Trekking-E-Bike mit CX-Motor kein
  gesicherter 20-Prozent-Abstand.
- **Canyon Endurace AL, 500 € (3487120571)** — Rahmengroesse laut Anzeige noch nicht einmal
  abgelesen. Referenz nicht belastbar (Streuung 3,2), Verkaeuferbewertung 0,15.
- **DJI Mavic Pro Fly More Combo, 250 € (3487228346)** — siehe Drohnen.
- **Vitra Eames Plastic Armchair mit Hopsak-Polster, 150 € (3486929388)** — Neupreis 470 €
  genannt, ein Gleiter defekt. Der Abstand zum Gebrauchtmarkt (250 bis 350 €) ist echt, der
  absolute Betrag mit rund 150 € aber zu gering fuer eine Meldung.

## Pflicht-Warnflags in diesem Lauf

Keine RTX 4090, keine Switch 2 mit Spielen, keine AirPods, kein NAS/Server mit Platten, kein
Threadripper Pro, kein Porsche 991/992 und kein Klassiker ohne Zulassungsbescheinigung Teil II
unter den Kandidaten. Das Tesla-Flag (Kilometerstand gegen Akkugarantiegrenze) und das
Apple-Flag (iCloud-Sperre, MDM) waren einschlaegig, haben aber jeweils zur Verwerfung gefuehrt
statt zu einer Meldung.
