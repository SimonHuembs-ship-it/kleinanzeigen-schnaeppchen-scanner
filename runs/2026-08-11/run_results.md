# Lauf 2026-08-11, 07:14 Uhr (morgens)

- `candidates.json` generiert: 2026-08-11T07:12:13+02:00 (bei Laufbeginn 1 Minute alt, Frist von vier Stunden eingehalten)
- Zeitraum: 2026-08-11T01:58:07+02:00 bis 2026-08-11T06:58:07+02:00
- Gesichtete Anzeigen: 28.414
- Kandidaten in der Liste: 197
- Bereits in `deal_log.csv`: 0
- Inhaltlich geprueft: 197 (im Detail gelesen: 41; die uebrigen ueber Kategorie- und Referenzpruefung gesammelt verworfen, siehe unten)
- Gemeldete Funde: 2

## Hinweis zum Repo-Zustand

Der Klon stand auf einem losgeloesten HEAD (4087c17, Scan 01:24Z), waehrend der lokale
`main` noch auf dem Stand vom 5. August lag. Nach `git fetch origin main` zeigte sich
`origin/main` auf c60c8e7 (Scan 05:12Z). Der Lauf wurde auf diesem frischeren Stand
wiederholt; beide Funde sind auch dort enthalten. Zehn Kandidaten waren gegenueber
dem 01:24Z-Stand neu, darunter die beiden Rolex Datejust (siehe unten).

## Funde

| Kandidat | Preis | Bestaetigtes Preisniveau | Abstand | Kategorie |
|---|---|---|---|---|
| [Pegasus PREMIO EVO 10 Lite, Bj. 2022, 1.515 km](https://www.kleinanzeigen.de/s-anzeige/pegasus-premio-evo-10-lite-e-bike-trekkingrad-tourenrad-citybike/3481019438-217-2236) | 1.000 € | ca. 1.700–2.000 € (neu 2.849–3.599 €, gebraucht ca. 2.000 €) | ca. 45 % | ebike-rad |
| [Union Glashuette Viro, Bj. 2022, Full Box](https://www.kleinanzeigen.de/s-anzeige/union-glashuette-viro-top-zustand-full-box/3481015886-157-4501) | 650 € | ca. 1.050–1.300 € (Chrono24 gebraucht ab 1.057 €, chronoto ab 1.105 €) | ca. 38 % | uhren |

Beim Pegasus blieb der Kleinanzeigen-Median (1.999 €, n=21, Streuung 1,39) erhalten,
weil er belastbar ist und mit der externen Recherche uebereinstimmt. Bei der Union
Glashuette liegt die Streuung mit 2,56 ueber der Grenze von 2,5 und `belastbar` ist
`false`; der Median wurde deshalb als nicht vorhanden behandelt und durch einen
recherchierten `referenz_hinweis` ersetzt, `ersparnis_eur` entfaellt.

Kein Kandidat mit `unkenntnis_bonus` unter den Funden. Der einzige Kandidat mit
diesem Flag (3481114419) wurde verworfen, siehe unten.

## Verworfene Kandidaten

### Preis erklaert sich von selbst (Unfall, Defekt, Laufleistung, Bastlerzustand)

| Kandidat | Preis | Grund |
|---|---|---|
| 3481571256 Porsche 911 (997.1, 2007) | 38.800 € | Als "Beschaedigtes Fahrzeug" eingestellt, Unfallschaden hinten rechts vom Verkaeufer beschrieben; 133.000 km. Der Preis ist damit richtig, nicht zu niedrig. |
| 3481601033 BMW E36 325i Cabrio | 5.900 € | Ausdruecklich Bastlerfahrzeug, kein gueltiger TUEV, Motor lief zuletzt unrund, Rost an beiden Wagenheberaufnahmen. |
| 3481165176 BMW E36 328 Coupé M-Paket | 9.200 € | Verkaeufer schreibt selbst "muss definitiv komplett restauriert werden": Servopumpe defekt, alle vier Kotfluegel und Wagenheberaufnahmen faellig, 270.000 km. |
| 3481063879 Mercedes E 250 W124 | 3.000 € | 500.000 km, mit Maengeln durch den TUEV gefallen, als beschaedigt eingestellt. |
| 3481093896 Mercedes 190 E W201 | 1.950 € | 450.024 km, TUEV abgelaufen, ungeklaertes Ruckeln bei 80 km/h, Schiebedach defekt. |
| 3481751631 BMW E28 525eta, zwei Fahrzeuge | 8.500 € | Ausdruecklich Bastlerfahrzeuge, Heckschaden an einem, kein Startversuch unternommen, Kilometerstand als 999.999 eingetragen. |
| 3456211403 Ducati Monster 900 i.e. | 1.400 € | Steht seit sechs Jahren, kein TUEV, Rueckholfeder des Schalthebels defekt, nur bedingt fahrbereit. |
| 3481235926 Suzuki GSX-R 1100 (1992) | 1.100 € | 90.220 km bei einem 34 Jahre alten Motorrad; Referenz zudem nicht belastbar (Streuung 2,82). |
| 3480976524 Cube Reaction Hybrid EXC 625 | 700 € | 14.000 km auf einem E-Bike von 2020, Zustand "In Ordnung". |
| 3481590784 Haibike Trekking 4.0 | 399 € | Vom Verkaeufer als defekt angeboten, Geschwindigkeitserkennung ohne Funktion, "zum Reparieren oder Ausschlachten". |
| 3481576286 Cube Access Hybrid Pro Allroad 500 | 700 € | Kaufjahr 2018, 6.534 km, 500-Wh-Akku am Ende der Lebensdauer. |
| 3481678151 iPhone 15 Pro Max 256 GB | 300 € | eSIM defekt, ausdruecklich als Reparaturobjekt angeboten. |
| 3481689404 iPhone 14 Pro | 150 € | Nach Sturz ohne Funktion, Zustand "Defekt". |
| 3481213853 Vitra Eames Soft Pad Chair | 850 € | Gasfeder defekt, sichtbare Lederabnutzung; Preis entspricht dem Zustand. |
| 3481275489 Gibson Les Paul Special (1989) | 1.299 € | P100-Pickups gegen Seymour Duncan getauscht und Koffer nicht original: wertmindernde Umbauten. Der Median mischt zudem Standards und Customs unter die deutlich guenstigere Special. |

### Referenzgruppe nicht vergleichbar oder Marktwert nicht bestaetigt

| Kandidat | Preis | Grund |
|---|---|---|
| 3481488439 Porsche 911 Carrera Cabrio (996.1, 2000) | 27.900 € | Median 61.199 € mischt 993, 996, 997 und 991 zu einem Markendurchschnitt. Das 996.1 Cabrio mit Tiptronic und Japan-Import ist die guenstigste 911-Variante ueberhaupt; 27.900 € bei 56.500 km liegt im Markt, nicht darunter. Prompt-Warnflag: Zylinderlaufbahnschaeden betreffen genau die 996. |
| 3481517433 Tesla Model S (2015) | 18.200 € | Query "Tesla Model" mischt Model 3, Y, S und X. Das Fahrzeug ist ein US-Import, nicht bei Tesla Deutschland registriert und faehrt dauerhaft offline: kein Supercharger-Zugang, keine Softwareupdates. Der Preis erklaert sich damit selbst. |
| 3481740086 Rolex Datejust Ref. 1601 (1974) | 4.800 € | Websuche bestaetigt fuer die Ref. 1601 in Stahl ein Preisniveau von 3.772 bis 4.300 € auf Chrono24: Das Angebot liegt am oberen Rand des Marktes, nicht darunter. Der Median von 10.500 € entsteht aus der Beimischung moderner Datejust-Referenzen. |
| 3481740204 Rolex Datejust Ref. 16013 (1984) | 6.190 € | Gleicher Verkaeufer, gleicher Medianfehler. Bicolor-16013 liegt bei rund 4.500 bis 6.500 €, das Angebot damit im Markt. |
| 3481229849 Rolex Sea Dweller | 5.500 € | Die genannte Referenz "Rolex 12800" existiert nicht; Sea-Dweller-Referenzen sind 1665, 16600, 116600, 126600, 126603. Ohne belegbare Modellangabe kein bestaetigbarer Marktwert. Verkaeuferbewertung 0,32. |
| 3350951151 Jaeger-LeCoultre Reverso Shadow | 4.390 € | Haendlerangebot mit Garantie, dessen exakte Reverso-Variante die Anzeige nicht nennt; ohne Referenz keine Vergleichsgruppe. Die Anzeigen-ID liegt weit unter dem aktuellen Nummernkreis, das Angebot steht also seit Monaten. |
| 3379664884 Tudor Prince Date 79280 | 3.400 € | Referenz nicht belastbar (Streuung 8,8). |
| 3447685308 Jaeger-LeCoultre Atmos Classique | 1.800 € | Referenz nicht belastbar (Streuung 3,5). |
| 3481717839 Rolex Brillant Datejust | 7.000 € | Referenz nicht belastbar (Streuung 8,12), Brillantbesatz ohne Herkunftsnachweis. |
| 3481014435 Tudor Black Bay GMT | 2.500 € | Sauber dokumentierte Anzeige (Kauf 11/19 KaDeWe, Revision 03/25 bei Wempe, Belege vorhanden), aber Chrono24 fuehrt vergleichbare Full Sets von 2019 und 2020 bei 3.006 bzw. 3.125 US-Dollar, also rund 2.750 bis 2.870 €. Im Privatverkauf sind 2.500 € damit ein normaler Preis und nicht 20 Prozent darunter. |
| 3480918978 Leica Elmarit-M 21mm ASPH 11135 | 1.090 € | Keine Referenz vorhanden, eigene Recherche ergab ein Haendlerniveau von rund 1.290 € (Ken Hansen, mint) bis 1.760 € (Ricardo, sehr gut). Im Privatverkauf liegt das Objektiv damit bei etwa 1.100 bis 1.400 €; die geforderten 20 Prozent Abstand sind nicht belegbar. |
| 3481722858 Riese & Mueller Supercharger² GT Touring | 2.250 € | Konkrete Anzeige (09/2023, 1.800 km, DualBattery 1000 Wh), aber es liess sich nur ein einziges konkretes Vergleichsangebot finden; die Preisseiten von Upway, bikeflip und JobRad Loop sind aus dieser Umgebung nicht abrufbar. Ohne zwei belegte Vergleichswerte kein Fund. Verfuegbar zudem erst ab Mitte September. |
| 3468005430 BMC URS ONE Gravel | 1.385 € | Neupreis 2021/2022 lag bei 2.799 bis 2.999 €; gebrauchte Carbon-Gravelbikes dieses Alters liegen bei 1.300 bis 1.600 €. Der Preis ist marktueblich, nicht 20 Prozent darunter. |
| 3481704357 Cube Stereo Hybrid Race 120 | 950 € | Anzeige nennt kein Modelljahr. Bei E-MTBs entscheidet der Jahrgang ueber mehrere hundert Euro Wert; ohne ihn kein bestaetigbarer Marktwert. |
| 3481114419 Cube Race One (einziger Kandidat mit `unkenntnis_bonus`) | 595 € | Nicht wegen Anzeigenqualitaet verworfen. Die beschriebene Ausstattung (2x12, RockShox, Shimano XT BR-M8100) passt zu keinem Cube-Modell namens "Race One"; ohne identifizierbares Modell laesst sich kein Referenzwert bilden. Referenz zudem nicht belastbar (Streuung 4,45). |
| 3481083631 Hasselblad 500 C | 800 € | Fuenfzeilige Anzeige nennt weder Objektiv noch Magazin noch Sucher. Body allein und komplettes Set unterscheiden sich um ein Vielfaches; nicht bewertbar. Referenz nicht belastbar (Streuung 3,94). |
| 3481015886 ist gemeldet; 3481610810 Vitra Eames Lounge Chair | 3.000 € | Referenz nicht belastbar (Streuung 4,31), siehe zusaetzlich Scammuster unten. |
| 3480986498 USM Haller Sideboard Rubinrot | 990 € | Mit 75 x 35 x 105 cm ein schmales Einzelelement, nicht das im Median enthaltene 200-cm-Sideboard. Verkaeuferbewertung 0,42. |
| 3297394664, 3060052896, 2926566277, 3351236981, 3481520362, 3405980875, 3323508121, 3296683503, 3351047112, 3481415250, 3481583198, 3468787903, 3351041711, 3481452941, 3481754081 (USM Haller und Umfeld) | 199–1.250 € | Durchweg Haendlerangebote mit Rechnung, deren Preise bereits Marktpreise sind; die Anzeigen-IDs liegen ueberwiegend weit unter dem aktuellen Nummernkreis, stehen also seit Monaten. Kein Fund. |
| 3481424737, 3481229768, 3481005380, 3481280934, 3481020150, 3481667873, 3481250440, 3480942168, 3481700320, 3481021712, 3481042819, 3481544561, 3481611670, 3481417661 (design-sammeln, Rest) | 160–1.450 € | Modellbezeichnung fehlt oder Referenz nicht belastbar (Streuung ueber 2,5); kein bestaetigbarer Marktwert. |
| 3481200540 Deckel FP1 Fraesmaschine | 2.300 € | Konto 15 Tage alt, keine Abholung angeboten, dafuer "Versand ab 7,69 €" fuer eine rund 1.000 kg schwere Fraesmaschine. Unmoegliche Uebergabe, Referenz zusaetzlich nicht belastbar. |
| 3481236699, 3481624364, 3481401324, 3466651846, 3379822351, 3481734280 (Werkzeug und Maschinen) | 220–1.300 € | Referenz durchweg nicht belastbar (Streuung 2,63 bis 6,58). |
| 3481675236 Hilti TE 70 AVR | 550 € | Verkaeuferbewertung 0,34, nur zwei Bilder, Text in Werbesprache ohne geraetespezifische Angaben. |
| 3481744224 Adidas ZX Sammlungsaufloesung | 5.200 € | Drei Zeilen Text, keine Aufstellung, welche Paare in welchem Zustand enthalten sind; nicht bewertbar. |
| 3480913281 Notverkauf G2 MAX, 3481726637 Rose The Bruce 1 | 420 / 450 € | Keine Referenz; recherchierte Marktwerte liegen fuer beide im Bereich des Angebotspreises. |
| 3481203916 Mercedes 500 SEL W126 | 7.999 € | 250.000 km und eine dreizeilige Anzeige ohne Historie oder Serviceunterlagen; ohne Zustandsnachweis laesst sich der classic-analytics-Wert (Zustand 3) nicht ansetzen. |
| 3481388012, 3481530495, 3481561594, 3481598457, 3481344796, 3481385120 (Youngtimer, Rest) | 1.500–5.000 € | Referenz entweder nicht belastbar oder Fahrzeuge mit Laufleistungen jenseits 200.000 km ohne belegte Historie. |
| 3481023475 BMC Team 01, 3481012943, 3481344732, 3481365200, 3481016147, 3431547679, 3481261434 und weitere ebike-rad-Kandidaten | 300–2.400 € | Ganz ueberwiegend ohne Modelljahr in der Anzeige oder mit nicht belastbarer Referenz (Streuung ueber 2,5). |
| 3481699764 Kreidler Vitality Eco 10 | 1.299 € | Leasingrueckläufer ohne Baujahr, ohne Laufleistung und ohne Angabe zur Akkukapazitaet. |
| 3481282539, 3481214918 PS5 Pro | 450 / 550 € | Ein einziges Bild, Titel und Attribute widersprechen sich (zwei bzw. drei Controller), nur Versand. Referenzgruppe mit n=8. |
| 3481559190 Zeiss Fernglas 8x56 B | 290 € | Referenz nicht belastbar (Streuung 2,63). |
| 3480959701 Thorens TD 160 MK II, 3480922238 Thorens TD 146 | 250 / 125 € | Beim MK II ist das Haubenscharnier defekt; der Abstand zum bestaetigten Niveau bleibt unter 20 Prozent. Vergleichbare Thorens wurden am 5. August bereits gemeldet. |

### Scammuster nach der Leitidee (gut gemachte Anzeige, zu guenstig, Versand)

| Kandidat | Preis | Grund |
|---|---|---|
| 3481618012 DJI Mini 5 Pro Fly More Combo "NEU" | 425 € | Neupreis der Combo liegt laut Geizhals und heise Preisvergleich bei 899 bis 1.129 €. Ein aktuelles Modell "wie neu" zu 45 Prozent, mit Werbetext ohne einen einzigen geraetespezifischen Wert (keine Flugstunden, keine Seriennummer), Gewerbetext auf Privatprofil und Versandangebot. Im `deal_log` stehen bereits zwei auffaellig aehnliche Mini-5-Pro-Anzeigen. |
| 3481610810 Vitra Eames Lounge Chair und Ottoman | 3.000 € | Perfekt formulierte Anzeige mit exakter Ausfuehrungsbezeichnung und ohne jeden Mangel, Konto fuenf Monate alt, keine Abholung moeglich, "Versand ab 23,99 €" fuer ein rund 50 kg schweres Sesselpaar. |
| 3481704956 iPhone 17 Pro 512 GB | 900 € | Kein einziges Bild, Zahlung wahlweise per Ueberweisung oder PayPal angeboten. |
| 3481740150 iPhone 17 Pro Max 512 GB | 800 € | Verkaeuferbewertung 0,28, nur Versand, Text widerspricht sich selbst ("neu und kratzerfrei", zugleich "vorher hatte es einen kleinen Displayfleck"). |
| 3481238552 Tag Heuer Carrera Chronograph | 1.499 € | "Nur Bankueberweisung, kein PayPal und keine Abwicklung ueber Kleinanzeigen": ausdrueckliche Aufforderung zur Zahlung ausserhalb der Plattform. Keine Referenznummer genannt. |
| apple-mobil und macbook gesamt, 52 Kandidaten (u. a. 3481105079, 3480911395, 3481328397, 3481398298, 3480922972, 3481482503, 3481306872, 3480966081, 3481490403, 3481166513, 3480922991, 3480908914, 3481726434, 3480979281, 3481705090, 3481738934, 3481067113, 3481153533, 3480988144, 3481497836, 3481453626, 3481609159, 3481419641, 3481551642, 3481362812, 3481417793, 3481300966, 3481730714, 3480928584, 3481094226, 3480969787, 3480987209, 3481006614, 3481050581, 3480989253, 3481716728, 3480924736, 3480912516, 3480925967, 3481012575, 3481122579, 3481100922, 3481223140, 3481217048, 3481211422, 3481735250, 3481590303, 3481175124, 3481703692, 3481739376, 3481744570, 3481746774) | 150–900 € | Homogener Block von ueber 50 iPhones und MacBooks, fast durchgaengig bei 50 bis 60 Prozent des Medians, ganz ueberwiegend mit "Versand ab 0,49 €", vielfach mit Verkaeuferbewertungen unter 0,7 oder Konten juenger als sechs Monate, mehrfach mit identischen Textbausteinen. Wo ein Geraet tatsaechlich guenstig ist, ist es als defekt gekennzeichnet. Kein einzelnes Angebot hebt sich als Verkauf eines ahnungslosen Privatverkaeufers ab; die Pflicht-Warnflags fuer Apple-Geraete (iCloud-Aktivierungssperre, MDM) waeren bei jedem einzelnen zu setzen. Gesammelt verworfen. |
| 3481040302, 3481403339, 3481623422, 3481020211, 3481154195, 3481156823, 3481383231 (DJI Mavic und Mini 3 Pro) | 250–350 € | Referenz ueberwiegend nicht belastbar (Streuung 3,1 bis 3,3); die Mavic-Pro-Generation von 2016/2017 ist zudem ohne aktuelle Firmware- und Fernidentifikationspflicht in der EU nur eingeschraenkt nutzbar, was den Preis erklaert. |
| 3480937713 Vespa Sprint | 1.650 € | Konto 38 Tage alt, keine Bewertung, einzeiliger Text ohne Kilometerstand. |
| 3481612603, 3480929014, 3481430998, 3481022188, 3481637758 (Simson) | 1.190–2.000 € | Preise liegen im Bereich des tatsaechlichen Simson-Marktes; der Median mischt restaurierte und unrestaurierte Fahrzeuge. |
| 3481733275 Gibson Les Paul | 1.200 € | Referenz nicht belastbar (Streuung 3,04), Anzeige nennt weder Modellvariante noch Baujahr. |
| 3481369873 Shimano Dura Ace 7400 Gruppe, 3481185360 SRAM Red Powermeter | 500 / 300 € | Beide plausibel, aber ohne zwei belegte Vergleichsangebote fuer exakt diesen Lieferumfang kein bestaetigter Marktwert; absolute Ersparnis in beiden Faellen gering. |
| 3481751612 CUBE Fahrrad, 3481694748, 3481115590, 3481630143, 3481632950, 3481590473, 3481389371, 3480917270, 3481104452, 3481650545, 3481074485 u. a. | 200–600 € | Titel ohne Modellbezeichnung ("CUBE Fahrrad", "Cube Mountainbike"); ohne Modell kein Referenzwert. |
| 3481735166 Kueche Wohnungsaufloesung | 950 € | Keine Referenz, Sammelposten aus Einbaugeraeten ohne Modellangaben. |

## Was nicht getan wurde

Keine Verkaeufer angeschrieben, nichts geboten, nichts gekauft, keine Logins. Keine
Daten von Kleinanzeigen nachgesammelt. Marktwerte wurden ausschliesslich per Websuche
belegt; wo kein belastbarer Referenzwert zu finden war, ist das oben als Grund
vermerkt statt geschaetzt. mobile.de und AutoScout24 wurden nicht direkt abgerufen.

Anmerkung zur Recherche: die Preisseiten von mpb.com, chrono24.de, classic.leica-camera.com,
ebay.de, upway.de, bikeflip.com, auspreiser.de, leicastoremiami.com und kenhansennyc.com
sind aus dieser Umgebung nicht direkt abrufbar (Egress-Sperre). Die oben genannten Zahlen
stammen daher aus Suchergebnis-Auszuegen dieser Quellen.
