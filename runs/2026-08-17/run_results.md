# Lauf 2026-08-17, morgens (07:07 Uhr MESZ)

`candidates.json` generiert: 2026-08-17T06:44:14+02:00 (23 min alt, klar innerhalb der
Vier-Stunden-Grenze aus Schritt 1). Zeitraum des Sammellaufs: 2026-08-17T01:31:37+02:00 bis
2026-08-17T06:31:37+02:00, gesichtet 20.843 Anzeigen.

- Kandidaten in `candidates.json`: 189
- davon schon in `deal_log.csv`: 0
- Referenz nicht belastbar (`belastbar: false` oder Streuung > 2,5): 51 — Median als nicht
  vorhanden behandelt
- inhaltlich geprueft: 53 (sortiert nach absoluter Ersparnis, dazu vollstaendig alle
  Kandidaten der liquiden Kategorien `apple-mobil`, `macbook`, `optik-drohnen`,
  `kameras-leica`, `konsolen-sweep` und `uhren`; die uebrigen 136 liegen unter 300 Euro
  absoluter Ersparnis oder sind Massenware aus `ebike-rad` und `design-sammeln` mit
  gemischtem Median)
- `unkenntnis_bonus` in diesem Lauf: 1 Kandidat (Mini-Drehbank, 300 €) — Referenz nicht
  belastbar (Streuung 3,28), siehe unten
- gemeldete Funde: 1

Hinweis zur Recherche: die Netzwerkrichtlinie dieser Umgebung blockiert den Direktabruf von
mascus.de, machineryzone, truckscout24, classic.com, zwischengas.com und buycycle. Die
Marktwertbestaetigung lief deshalb ausschliesslich ueber Websuche. Wo das keine zwei
konkreten Vergleichsangebote desselben Modells ergab, wurde verworfen statt geschaetzt.

## Funde

| Ware | Preis | bestaetigter Marktwert | Abstand | Ort |
|---|---|---|---|---|
| [Specialized S-Works Turbo Kenevo SL, Gr. S3, 3.100 km](https://www.kleinanzeigen.de/s-anzeige/specialized-s-works-turbo-kenevo-sl-s3-light-e-bike-fully/3486703079-217-5531) | 5.000 € | 6.300 € (2021er S-Works) bis 7.990 € (gebrauchte 2022er S-Works, marktplatz.bike); Bicycle Blue Book fuehrt das 2022er S-Works bei 7.900–9.200 USD | −21 % auf die Untergrenze, −29 % auf 7.000 € | Rettenberg |

Beleg:

- **Specialized S-Works Turbo Kenevo SL** — der Neupreis lag bei 12.999 bis 13.999 €. Fuer
  das gebrauchte S-Works-Modell habe ich zwei konkrete Angebote gefunden: ein 2021er
  S-Works Kenevo SL bei rund 6.300 € und gebrauchte 2022er S-Works ab 7.990 € auf
  marktplatz.bike; Bicycle Blue Book fuehrt das 2022er S-Works Turbo Kenevo SL 29 fuer 2023
  bei 7.905 bis 9.180 US-Dollar. Ein auf eBay gefundenes Angebot zu 3.799 € wurde bewusst
  **nicht** als Vergleich gewertet: das ist die Kenevo SL **Expert**, ein anderer und
  deutlich guenstigerer Aufbau. Dass es beim Kandidaten wirklich das S-Works ist, belegt die
  Ausstattungsliste der Anzeige (FOX FLOAT 38 Factory, FLOAT X2 Factory, SRAM XX1 Eagle AXS,
  RockShox Reverb AXS) — genau die Serienausstattung dieser Variante.
  Gegen das konservativste bestaetigte Niveau von 6.300 € liegen 5.000 € 21 Prozent
  darunter, gegen realistische 7.000 € 29 Prozent. Ein wertmindernder Grund ist nicht
  erkennbar: 3.100 km sind fuer ein E-MTB wenig, 59 Ladezyklen, Akku laut App bei 100
  Prozent, Gabel 2024 und Daempfer 2025 im Service, dazu Aufpreisteile (Magura MT7 Pro mit
  220-mm-Scheiben, Syntace C33i Carbonlaufraeder). Verkaeuferprofil passt zur Leitidee:
  Konto seit 2015, Bewertung 0,83 bei allen drei Abzeichen auf Stufe 2, **nur Abholung, kein
  Versand**, Probefahrt angeboten, und die Anzeige nennt von sich aus Kratzer, dass der Rahmen
  "nicht makellos" ist und die genauen Servicezeitpunkte.
  Der Kleinanzeigen-Median von 12.645 € (n = 8) wurde **nicht** als Massstab verwendet, obwohl
  `belastbar: true` gesetzt ist: die Suchanfrage lautete "Specialized Works Turbo S3" und hat
  Neu- und Fastneuraeder eingemischt — ein Median nahe am Neupreis. In `deals.json` steht
  deshalb statt `ersparnis_eur` ein `referenz_hinweis` mit dem selbst bestaetigten Niveau, damit
  die Mail keine Phantomersparnis von 7.644 € ausweist.

## Verworfene Kandidaten

### Grosse Betraege, an der eigenen Marktwertpruefung gescheitert

- **Minibagger Yanmar SV17, Bj. 2014, 3.010 Bh, 12.300 € (3477950844)** — groesste
  Nominalersparnis des Laufs (12.678 €), aber nicht bestaetigt. Vergleichsangebote: 2014 mit
  3.300 Bh fuer 18.663 € (Polen) und ein 2014er SV17-EX mit 3.200 Bh fuer 19.000 €
  (Rumaenien) — aber ein deutsches Angebot von 2014 mit nur 1.581 Bh liegt bei 11.800 €, also
  unter dem Kandidatenpreis bei halber Betriebsstundenzahl. Damit ist der Abstand von
  20 Prozent zum **deutschen** Markt nicht belegbar. Dazu: Verkaeufer ist ein gewerblicher
  Baumaschinenhaendler mit Adresse und Telefonnummer im Text; ein Haendlerpreis ist der Markt
  und nicht dessen Unterschreitung. Der Median von 24.978 € hat neuere Maschinen eingemischt,
  das p25 der Referenz liegt mit 14.700 € deutlich naeher an der Realitaet.
- **Yanmar sv 17 Minibagger, Bj. 2012, 5.630 Bh, 13.500 € inkl. MwSt (3277047547)** — teurer
  als der obige Kandidat bei aelterem Baujahr und fast doppelter Betriebsstundenzahl,
  Haendlerkonto erst seit 02/2025 mit Bewertung 0,57. Kein Fund.
- **BMW E30 325iX Touring, EZ 06/1990, 308.000 km, 8.999 € (3486531770)** — vom Modell her
  echte Raritaet mit H-Zulassung und TUEV bis 10/2026, aber der Abstand traegt nicht. Das
  naechstliegende Vergleichsangebot ist ein 325iX Touring von 1988 mit 300.000 km zu 10.702 €;
  8.999 € liegen damit nur rund 16 Prozent darunter und verfehlen die Zwanzig-Prozent-Huerde.
  Die hoeheren Notierungen (13.750 € bei 166.000 km, 19.900 € und 28.000 € bei Classic Trader)
  gelten Fahrzeugen mit halber Laufleistung. Hohe Laufleistung ist nach Schritt 2 ein Grund,
  der den Preis von selbst erklaert. Nebenbefund: das Attributfeld nennt 30.800 km, der
  Anzeigentext 308.000 km — vor jedem Kontakt zu klaeren.
- **Specialized S-Works Kenevo SL** — siehe Funde, angenommen.

### Uhren: Referenzgruppe passt nicht oder Anzeige traegt Betrugsmuster

- **Rolex Daytona 116503, Full Set 2021, 20.500 € (3486545802)** — Lehrbuchfall der Leitidee
  in umgekehrter Richtung: exakte Referenznummer, Kaufdatum, Kaliberangabe, "Full Set", keine
  echten Maengel — und dabei **kein Abholung, nur Versand**, bei einem Verkaeufer mit Bewertung
  0,46. Eine 20.500-Euro-Uhr, die ausschliesslich verschickt wird, wird nicht gemeldet.
- **Rolex Oyster Datejust Ref. 69163, 26 mm Damenuhr, 4.600 € (3356962373)** — der Median von
  9.999 € stammt aus der Suche "Rolex Oyster Datejust" und damit ueberwiegend aus 36- und
  41-mm-Herrenuhren. Eine 26-mm-Lady-Datejust ist ein anderes Produkt in einer anderen
  Preisklasse; die Ersparnis ist ein Phantom.
- **Rolex Datejust 41 mm gruen, 10.000 € (3486490488)** — Median 14.275 € aus nur acht
  Anzeigen, die teurere Zweifarb- und Diamantvarianten einmischen. Die Stahlvariante mit
  gruenem Blatt liegt selbst im Bereich des Angebotspreises. Zusaetzlich "Keine Bargeld
  Annahme!" — bei Abholung ein Warnzeichen.
- **Omega Speedmaster Professional Mark IV, 1.850 € (3486143708)** — klarster Fall einer
  falschen Referenzgruppe: der Median von 5.900 € kommt aus der Suche "Omega Speedmaster
  Professional", also der Moonwatch. Die Mark IV ist ein Automatikchronograph mit Kaliber
  1040/1045 und ein voellig anderes Modell; Chrono24 fuehrt sie ab rund 1.650 € und in gutem
  Zustand bis rund 3.465 €. Ohne Papiere sind 1.850 € Marktpreis, keine Ersparnis.
- **Rolex Submariner, 8.500 € (3485750390)** — die Beschreibung besteht aus einem Satz ohne
  Referenznummer, Baujahr oder Papiere. Ohne Modellbestimmung ist kein Marktwert
  bestaetigbar, und ohne bestaetigten Marktwert kein Fund.
- **Rolex Datejust 36 Full Set, 5.750 € (3486167880)**, **Rolex Datejust Stahl/Gold 36 mm,
  4.600 € (3486169336)**, **Rolex Lady Datejust 6917, 2.750 € (3486625749)**, **Rolex Lady
  Date 6916, 2.999 € (3461000959)** — durchweg ohne Referenznummer bzw. mit Versandangebot
  "ab 0,49" bei vierstelligen Betraegen; kein Modell exakt genug bestimmbar, um zwei
  Vergleichsangebote mit derselben Ausstattung zu finden.
- **Tudor Black Bay 79230R Full Set, 2.599 € (3485744813)** und **Tudor Black Bay Bronze,
  2.799 € (3385228339)** — beide liegen im normalen Marktband dieser Referenzen, der Abstand
  von 20 Prozent ist nicht gegeben.
- **Jaeger-LeCoultre "Rue de la Paix" Recital 8, 1.400 € (3485768401)** — eine Tischuhr, der
  Median (Streuung 5,34, nicht belastbar) stammt aus Armbanduhren. Keine vergleichbare Basis.

### Zahlungsaufforderung ausserhalb der Plattform

- **Truma Aventa Compact 2. Generation, NEU und OVP, 725 € (3485669150)** — auf dem Papier der
  auffaelligste Kandidat des Laufs (31 Prozent des Medians fuer Neuware mit Rechnung), im Text
  steht aber woertlich "Versand (DHL) und PayPa FF bitte!". PayPal Freunde und Familie hat
  keinen Kaeuferschutz; neuwertige Ware weit unter Marktpreis plus Zahlung ohne Absicherung ist
  das Standardmuster. Nicht gemeldet.
- **Walter Knoll DRIFT Sessel, 490 € (3485728700)** — ebenfalls "Paypal Freunde"; zudem ergab
  die Websuche keine zwei konkreten Gebrauchtangebote mit Preis fuer genau dieses Modell, der
  Marktwert bleibt unbestaetigt.

### Der niedrige Preis erklaert sich von selbst

- **Vespa Sprint 125, 2.000 € (3486084470)** — verliert Oel, rechts verkratzt, der Verkaeufer
  schreibt selbst von noetiger Reparatur.
- **Canyon CF SLX 9.0, 1.699 € (3486674304)** — professionell reparierte Beschaedigung am
  Carbonrahmen, offengelegt.
- **Suzuki GSX-R 750, 2.300 € (3485759569)** — als Bastlerfahrzeug angeboten, Gabelholm
  undicht, Sturzschaden.
- **Mercedes W124 E220, 2.900 € (3486422148)** und **Mercedes 190er W201, 2.400 €
  (3486019598)** — beide im Attributfeld als "Beschaedigtes Fahrzeug" gefuehrt, der 190er
  ausdruecklich als nicht fahrbereites Bastlerfahrzeug nach zehn Jahren Standzeit.
- **Simson Star SR4-2/1, 1.200 € (3486377608)** — ausdruecklich Restaurationsobjekt.
- **Simson Schwalbe KR51 Hycomat, 1.249 € (3485970401)** — Motor springt nur mit Hilfe an,
  lange gestanden, Rahmennummer schlecht lesbar.
- **Cube Hybrid Race 625, 1.200 € (3485677105)** — 7.685 km, Kette faellig.
- **iPhone- und MacBook-Block (35 + 9 Kandidaten)** — nahezu vollstaendig durch offengelegte
  Defekte erklaert: gerissene Rueckseite, defekte Ruecckamera, getauschtes Nicht-Original-
  Display, Bastlergeraete. Die Restposten liegen im normalen Gebrauchtband. Kein einziger
  erreichte 20 Prozent Abstand zu einem selbst bestaetigten Marktwert.

### Referenz nicht belastbar und kein eigener Marktwert bestaetigt

- **Mini-Drehbank GMD 400, 300 € (3486464133)** — der einzige Kandidat mit
  `unkenntnis_bonus: true` in diesem Lauf und deshalb ausdruecklich **nicht** wegen
  Anzeigenqualitaet abgewertet. Er scheitert allein an der Referenz: Streuung 3,28,
  `belastbar: false`, die Suche "Mini Drehbank" mischt Tischbohrmaschinen und
  Groessenklassen. Zur GMD 400 selbst ergab die Websuche keine zwei belastbaren
  Gebrauchtangebote. Bei 250 € Nominalersparnis lohnt kein weiterer Aufwand, geschaetzt wird
  nicht.
- **Cube Litening SRAM Red, 1.250 €**, **Raymon E-Bike, 900 €**, **Drehbank HAE, 850 €**,
  **Colchester Triumph, 1.899 €**, **BMC Rennrad, 1.200 €**, **Specialized Damen MTB Jett,
  400 €**, **Trek Madone, 500 €**, **Mafell Erika 65, 500 €** — Streuung zwischen 2,85 und
  8,81, der Median mischt erkennbar verschiedene Produkte. Keiner traegt genug absoluten
  Betrag, um die Eigenrecherche zu rechtfertigen.
- **Gibson Les Paul Junior BJA Signature 1.700 €**, **Les Paul Standard 1992 1.890 €**,
  **Les Paul Junior 2024 1.000 €** — Median jeweils aus der Sammelsuche "Gibson Les Paul",
  die Junior-, Studio- und Standard-Modelle in voellig verschiedenen Preisklassen mischt.

### Marktband erreicht, aber Abstand unter 20 Prozent

- **Cube Kathmandu Hybrid EXC 750 XL, 1.450 € (3486669937)** — generalueberholte Exemplare
  des Modelljahrs 2022 starten bei 1.799 €, das sind nur 19 Prozent Abstand; neue 2022er
  werden noch ab 1.999 € gehandelt. Knapp verfehlt.
- **Riese & Müller Nevo 4 vario, 2.350 € (3486692201) und 2.300 € (3486693359)** — zwei fast
  identische Leasingrueckläufer-Anzeigen ohne Verkaeuferbewertung. Die Websuche lieferte nur
  Neupreise (5.799–5.899 €) und Haendlerangebote, keine zwei konkreten Gebrauchtangebote
  desselben Modelljahrs. Marktwert unbestaetigt.
- **Cube Cargo Sport Dual Hybrid, 1.800 € (3486728489)** — nur ein Bild, und zum deutschen
  Gebrauchtmarkt dieses Lastenrads gab die Websuche keine verwertbaren Preise her (nur
  norwegische Angebote).
- **Cassina Maralunga Zweisitzer, 1.200 € (3437522879)** — beide Kopfstuetzenseiten teilweise
  defekt, vom gewerblichen Haendler offengelegt; der Abschlag ist der Defekt.
- **USM-Haller-Block (10 Kandidaten, 450–1.100 €)** und uebrige `design-sammeln` — Handelsware
  mit stark konfigurationsabhaengigem Preis; ohne Abgleich der exakten Elementzahl, Masse und
  Farbe ist kein Median vergleichbar, und mehrere Anbieter sind selbst gewerbliche
  Wiederverkaeufer.

### Betrugsmuster ohne belegbaren Gegenwert

- **DJI Mini 4 Pro Drohne, 350 € (3486613286)** — der Titel nennt die Mini 4 Pro, der Text
  durchgehend die **Mini 3 Pro**. Modellangabe und Beschreibung widersprechen sich, Konto
  seit 07/2026, nur Versand. Verworfen.
- **Apple iPhone 15 Pro Max 256 GB, 350 € (3486704396)** — "neu und nur ausgepackt", Konto am
  Vortag angelegt, nur Versand. Klassisches Muster.
- **Simson S51 Neuaufbau, 1.950 € (3485798314)** — vollstaendig beschriebener
  Profi-Neuaufbau, aber Konto juenger als drei Tage und "Versand ab 0,49" fuer ein Moped.
- **iPhone 16 128 GB, 400 € (3486717982)** — "Akku neu, Display neu, Backcover neu, Rahmen
  neu": ein Geraet, an dem alles ausgetauscht wurde, ist kein guenstiges Original.

### Geprueft und schlicht kein Fund

- **Valve Steam Deck OLED 1 TB, 370 €** und **Steam Deck 512 GB OLED, 360 €** — beide liegen
  im normalen Gebrauchtband; bei 330 € bzw. 210 € Nominalersparnis kein Fund.
- **DJI Mavic 2 Pro, 220 € (3485817444) und 320 € (3486125001)** — beide Anzeigen sind ehrlich
  und detailliert, aber die Mavic 2 Pro ist ein abgekuendigtes Modell von 2018 mit breitem
  Preisband; der bestaetigte Abstand reicht nicht, und die absolute Ersparnis liegt bei 324 €
  bzw. 230 €.
- **Leica Summicron-R 50 mm f/2, 650 € (3485756958)** — Streuung 2,53, Median nicht belastbar;
  das Summicron-R 50/2 aus kanadischer Fertigung liegt selbst in diesem Bereich.
- **MacBook Pro 14" M4, 16/512 GB, 1.300 € (3485855313)** — im normalen Gebrauchtband fuer ein
  M4-Geraet, kein Abstand von 20 Prozent.
- **BMW E30 316, 5.000 €**, **Mercedes W124 200E, 3.500 €**, **Mercedes 190E 2,3, 3.150 €**,
  **Mercedes W124 230, 3.300 €**, **Ducati Monster 1000 ie, 3.200 €**, **Suzuki GSX-R 1100 W,
  1.200 €** — alle im ueblichen Preisband ihrer Baureihe; der Kleinanzeigen-Median liegt bei
  Youngtimern systematisch ueber dem erzielbaren Preis, weil Traumpreise lange stehenbleiben.
