# Lauf 2026-08-29, morgens

- **Zeitpunkt:** 2026-08-29, 07:25 Uhr (MESZ)
- **candidates.json generiert:** 2026-08-29T07:20:55+02:00 (40 Sekunden alt)
- **Zeitraum:** 2026-08-29T02:05 bis 07:05 (MESZ), akkumuliert ueber 24 Stunden
- **Gesichtet:** 24.888 Anzeigen
- **Kandidaten:** 83, davon 0 bereits in `deal_log.csv`
- **Geprueft:** 83
- **Gemeldet:** 2
- **Kandidaten mit `unkenntnis_bonus`:** 1 (3497088769, Drehbank) - verworfen, siehe unten

## Vorbefund: der Sammler hatte nicht rechtzeitig geliefert

Beim Start um 07:03 Uhr war `candidates.json` 4 Stunden 27 Minuten alt (Stand
2026-08-29T02:36:51+02:00). Die Frist in `prompt.md` Schritt 1 liegt bei vier
Stunden, der Lauf waere also ein Abbruch gewesen - der dritte innerhalb von drei
Tagen.

Ursache ist erneut der GitHub-Scheduler, nicht der Workflow: `scan.yml` steht auf
`0 */4 * * *` (UTC), fuer den Takt 04:00 UTC wurde bis 05:05 UTC kein Lauf
angelegt. Der Workflow ist aktiv, die letzten Laeufe sind alle erfolgreich,
nichts haengt in der Warteschlange. Dasselbe Muster ist am 27.08. und 28.08.
dokumentiert; am 28.08. hat GitHub zwei von sechs Takten angelegt.

Statt abzubrechen wurde der Sammler ueber `workflow_dispatch` von Hand
angestossen (Lauf 142, 05:05 bis 05:20 UTC, 921 Sekunden, 672 Requests). Danach
lag ein 40 Sekunden alter Stand vor, auf dem geurteilt wurde. Die Meldung geht
damit rund 25 Minuten spaeter raus als ueblich, statt an diesem Tag ganz
auszufallen.

**Nebenbefund zur Frist:** Der Aufruftext der Routine nennt sechs Stunden,
`prompt.md` Schritt 1 nennt vier. Massgeblich ist `prompt.md`. Solange der
04:00-UTC-Takt ausfaellt, ist der frischeste Stand um 07:00 MESZ rund viereinhalb
Stunden alt, der Morgenlauf trifft die Vier-Stunden-Frist also strukturell nicht.
Entweder wird der Cron auf einen Takt kurz vor 05:00 UTC gelegt, oder die Routine
stoesst den Sammler kuenftig selbst an.

## Gemeldete Funde

| # | Titel | Preis | Bestaetigtes Preisniveau | Abstand | Ort |
|---|---|---|---|---|---|
| 1 | USM Haller Sideboard weiss, 1 breit / 2 hoch / 50 cm tief, 2 Klapptueren, 4 Haengeregister-Einsaetze, Schwerlastrahmen | 600 € | 990-1.400 € (usm-markt 1.392 € fuer 1 breit / 2,5 hoch / 3 Klapptueren; KS Bueromoebel ab 1.289 €; FLEX Bueromoebel 749-2.242 € je nach Konfiguration) | ca. 45 % gegen den konservativen Wert | Ravensburg |
| 2 | Apple iPhone 16, 128 GB, weiss | 400 € | 566-619 € (Apple Certified Refurbished 619 €; vergleichbares Geraet Ende Juni 2026 auf eBay.de fuer ca. 566 € verkauft) | ca. 29 % gegen den niedrigeren bestaetigten Wert | Bremen-Schwachhausen |

Beide von Privatkonten mit langer Historie (2020 bzw. 2012), beide mit offen
genannten Gebrauchsspuren, beide ohne mangelbedingte Preiserklaerung.

## Verworfene Kandidaten

### Preis erklaert sich durch offengelegten Mangel oder Zustand

| ID | Titel | Grund |
|---|---|---|
| 3497358782 | Mercedes W124 Coupé, 4.999 € | "Motor startet nicht, Ursache unbekannt", wird als Motorschaden- und Teilespender verkauft, nicht fahrbereit. Korrekt bepreist. |
| 3496854473 | BMW E36 320i Cabrio M-Paket, 4.900 € | Ausdruecklich als Bastlerfahrzeug: hintere Wagenheberaufnahmen muessen fuer den naechsten TUEV erneuert werden, 192.000 km, Konto 12 Tage alt. |
| 3496844749 | Mercedes E200 W124, 2.800 € | Laeuft im Kaltstart unrund, 34 Jahre alt, eingetauscht - der Verkaeufer kennt die Historie selbst nicht. |
| 3497361953 | MacBook Pro 14" M4 16/512, 700 € | Ein Glas Cola ueber die Tastatur; Folgeschaeden werden ausdruecklich nicht ausgeschlossen. Der Abschlag ist der Preis fuer dieses Risiko. |
| 3497381422 | iPhone 16 Pro 128 GB, 480 € | Rueckglas durch Sturz gebrochen. |
| 3497365504 | iPhone 15 Pro 128 GB, 320 € | Displayschaden, SIM-Slot defekt. |
| 3497408906 | iPhone 15, 330 € | Risse im Glas, deutliche Gebrauchsspuren am Rahmen. |
| 3497363502 | iPhone 15 128 GB, 220 € | Risse auf Vorder- und Rueckseite, Akku 83 %, 814 Ladezyklen. |
| 3497369450 | iPhone 12 Pro 256 GB, 180 € | Rueckseite zersplittert, Akku 75 %. |
| 3496565157 | iPhone 13 Pro 128 GB, 150 € | Frontkamera defekt; bei Versand nur Vorabueberweisung gefordert. |
| 3497369180 | iPhone 14 Pro 256 GB, 250 € | Akku 76 %, Kratzer im Bildschirm, Konto 28 Tage alt. |
| 3497387139 | iPhone 15 Plus 128 GB, 299 € | Akku 78 %, Verkaeuferbewertung 0,28. |
| 3497397960 | iPhone 14 256 GB, 280 € | Akku 76 %. |
| 3497328001 | iPhone 15 128 GB, 280 € | Akku 80 %, Verkaeuferbewertung 0,17. |
| 3497414552 | iPhone 14 256 GB, 250 € | Akku 83 %, Verkaeuferbewertung 0,40. |
| 3495376111 | iPhone 14 Pro, 200 € | Kratzer auf der Rueckseite, Verkaeuferbewertung 0,14. |
| 3496564815 | MacBook Air M2 256 GB, 485 € | Trackpad funktioniert nur zeitweise; Reparatur erklaert den Abschlag. Bereits am 28.08. aus demselben Grund verworfen. |
| 3497405429 | MacBook Air M1 2020, 300 € | Schwarzer Strich im Bildschirm, vermutlich Grafikdefekt. |
| 3496955602 | Steam Deck OLED, 300 € | Als defekt inseriert: linkes Daughterboard vermutlich hin, ohne SSD. |
| 3497381702 | Canyon Sender, 1.400 € | Hinterrad mit Achter, Beschreibung sehr duenn, Konto seit Maerz 2026, nur Versand. |
| 3497410038 | Simson S51 N, 2.350 € | Ohne Papiere. Nach `prompt.md` Schritt 2e ist ein Klassiker ohne Zulassungsbescheinigung Teil II nicht billig, sondern richtig bepreist. |
| 3451704001 | Simson S51 4-Gang, 2.500 € | KBA-Papiere erst beantragt, unrestauriert, als Bastlerfahrzeug verkauft. |
| 3497055452 | Simson Schwalbe KR51 K, 2.150 € | Papiere beantragt, nur Polizeibescheinigung vorhanden; Originallack nur "laut Vorbesitzer". |
| 3497349470 | Sabb Diesel 2G Bootsmotor, 600 € | Vom Verkaeufer selbst als Teiletraeger/Bastlerobjekt ohne Unterlagen deklariert. |
| 3497363701 | Subaru Legacy 2,5, 799 € | Zeitdruckformel im Titel, Konto juenger als sechs Monate, kein Referenzwert. |

### Referenzgruppe nicht vergleichbar oder Marktwert nicht bestimmbar

| ID | Titel | Grund |
|---|---|---|
| 3496972912 | Rolex Oyster Perpetual Date 34, Ref. 1500, 4.100 € | `belastbar: false`, Streuung 2,56: Der Median 7.400 € mischt moderne Oyster Perpetual mit Vintage-Referenzen. Fuer eine Ref. 1500 aus den 60er/70er Jahren ist das Kleinanzeigen-p25 von 3.500 € der realistischere Anker, der Preis liegt damit auf Marktniveau. Beigelegt sind zudem "Chrono24-Papiere/Rechnung", also gerade keine Rolex-Papiere. |
| 3497406499 | Rolex Submariner Date, 8.850 € | Keine Referenznummer, keine Seriennummer, kein Baujahr - zwischen 16610 und 126610 liegen mehrere tausend Euro. Ohne Modellreferenz kein Marktwert bestimmbar; dazu nur Versand, keine Abholung, Bewertung 0,63 bei einem fuenfstelligen Objekt. |
| 3497395463 | Omega Seamaster, 1.800 € | Zwei Saetze Beschreibung, keine Referenz, kein Kaliber, nur Versand, Konto seit Juni 2026. Eine Seamaster ohne Referenz liegt zwischen 800 und 6.000 €. |
| 3496980318 | Herrenuhr Glashuette, 450 € | Beschreibung besteht aus zwei Woertern ("Uhr glashütte"). Weder Glashuette Original noch Union noch Nomos unterscheidbar. |
| 3496564098 | Rolex Oyster Damenuhr "Notverkauf", 1.500 € | Kein Referenzwert, Konto 5 Tage alt, Kellerfund ohne Box; die Echtheitsargumentation stuetzt sich auf einen "Bernhardiner im Schild". Nicht bewertbar. |
| 3471100731 | Jaeger-LeCoultre Reverso Classique Ref. 250808, 3.850 € | `belastbar: false`, Streuung 2,56: Der Median 6.145 € mischt mechanische und Duoface-Reverso. Das Angebot ist eine Quarz-Medium 23 x 38 mm von einem gewerblichen Haendler - dessen Preis bildet den Markt, statt ihn zu unterbieten. |
| 1419971665 | IWC Porsche Design Chronograph Titan Ref. 3743, 1.595 € | Auktionsschaetzung fuer die Ref. 3743 liegt bei 400 bis 1.400 €; der Haendlerpreis liegt darueber, nicht darunter. |
| 3497413713 | Yanmar SV17 Minibagger, 11.990 € brutto | Weder Baujahr noch Betriebsstunden genannt - genau diese beiden Groessen bestimmen bei einem Minibagger den Wert vollstaendig. Der Median 24.499 € (n=13) mischt Baujahre. Gewerblicher Anbieter, Verkauf nur an Gewerbetreibende und Export. |
| 3497088769 | Drehbank mit Zubehoer, 649 € (`unkenntnis_bonus`) | Trotz Bonus verworfen: `belastbar: false`, Streuung 3,33. Weder Hersteller noch Modell noch Spitzenweite genannt, die Suche "Drehbank Zubehör" mischt Uhrmacher- und Industriemaschinen. Ohne Typ kein Marktwert - hier ist der Beleg nicht beibringbar, nicht die Anzeige schlecht. |
| 3340097393 | Gibson Les Paul Junior 2010, 1.219 € | `belastbar: false`, Streuung 2,94: Der Median 3.699 € stammt aus Standard- und Custom-Anzeigen. Eine Junior liegt gebraucht bei rund 900-1.400 €; Anbieter ist zudem ein gewerblicher Gitarrenhaendler. |
| 3497124149 | Knoll Ledersessel, 250 € | Streuung 3,62, `belastbar: false`, kein Modellname (Barcelona, Pollock, Brno unterscheiden sich um den Faktor zehn). |
| 3496897624 | Ingo Maurer "Swingading" Stehlampe, 600 € | Streuung 34,55, Median unbrauchbar. Recherchierter Zweitmarkt: eine Doppelanzeige lag bei 160 € je Leuchte. Das Angebot liegt ueber Markt, nicht darunter. |
| 3497352104 | Trek 300 OCLV Rennrad, 780 € | Streuung 3,25, `belastbar: false`. Ein Trek 300 OCLV ist ein Carbonrahmen der spaeten 90er mit 105-Gruppe; der Median 1.575 € stammt aus modernen Carbonrennraedern. |
| 3497405823 / 3496968183 / 3496871058 / 3497095389 / 3496842643 / 3497381303 | Cube- und Velo-de-Ville-Raeder, 340-459 € | Durchweg ohne Modellbezeichnung oder mit Streuung ueber 3,4 (`belastbar: false`). "Cube Fahrrad 28 Zoll" laesst sich nicht bepreisen. |
| 3497093532 | Gibson Les Paul Studio 2008, 900 € | Streuung 4,21, `belastbar: false`. Eine LP Studio 2008 mit Koffer liegt gebraucht bei 800-1.100 €, der Preis ist marktgerecht. |
| 3497392607 | MacBook Pro 16", 16 GB / 1 TB, 600 € | Streuung 3,34, `belastbar: false`. "Neu gekauft in 2020" bedeutet ein Intel-16-Zoll; dessen Gebrauchtniveau liegt bei 500-700 €. |
| 3496974150 | MacBook Pro 16" 2019, i7 / 16 GB / 1 TB, 550 € | Streuung 3,09, `belastbar: false`. Intel-Geraet von 2019, Marktniveau 500-650 €. |
| 3497091822 / 3497118436 / 3497064825 | MacBook Air, 350-450 € | Kein Modelljahr, kein Chip, kein Speicher genannt. Zwischen einem Air 2017 und einem Air M1 liegen 400 €. |
| 3313077450 | Meissen Figur "Komoediantenkind", 325 € | Gewerblicher Antiquitaetenhaendler mit Ladengeschaeft; dessen Preis bildet den Meissen-Markt ab. Streuung 2,53, `belastbar: false`. |
| 3497352336 | Historische Baumaterialien, Scheunenfund, 300 € | Konvolut aus Tueren, Ofenkacheln und Windfegen ohne Referenz. Kein Marktwert bestimmbar. |
| 3497351965 / 3497400287 | One Piece TCG Konvolute, 375 € und 420 € | Kein Referenzwert. Der Wert haengt an Zustand und Grading jeder einzelnen Karte; ohne PSA/CGC-Bewertung nicht bestimmbar. |
| 3497389510 | Magic the Gathering Sammlung, 1.100 € | Dasselbe: 120+ Karten ohne Einzelaufstellung mit Zustandsangabe. |
| 3497388446 | Haushaltsaufloesung Moebel, 800 € | Kein Referenzwert, kein einzelnes Objekt benannt. |
| 3496564717 | iPhone 16 256 GB, 525 € | Ein Bild, Beschreibung aus Textbausteinen ("Inklusive der aktuellen Apple-Features") ohne eine einzige Angabe, die nur jemand macht, der das Geraet in der Hand haelt - kein Akkustand, keine Seriennummer, kein Zustand der Kanten. |
| 3497411666 | iPhone 13 Pro, 200 € | Textbaustein mit abgeschnittener Zeile ("Farbe:."), Speicherangabe im Text (256 GB) widerspricht dem Titel. |
| 3497418501 | iPhone 15 128 GB, 250 € | Konto 28 Tage alt, Beschreibung nennt ausser "Dynamic Island" keine geraetespezifische Angabe. |

### Betrugsprofil nach der Leitidee

| ID | Titel | Grund |
|---|---|---|
| 3497418824 | iPhone 17 Pro Max 512 GB, 690 € | Konto 3 Tage alt, Zustand "Neu", Akku 100 %, nur Versand, keine Abholung - bei einem Geraet mit rund 1.300 € Marktwert. Genau das handwerklich saubere Profil, das die Leitidee als Betrugsanzeige beschreibt. |
| 3497407054 | iPhone 17 Pro, 950 € | Bewertung 0,00, nur Versand, Stellvertretergeschichte ("mein Bruder hat ein neues gekauft"), Emoji-Haken-Liste, "keine Beschaedigungen", OVP. |
| 3497410116 | iPhone 17 Pro Max 256 GB, 800 € | Bewertung 0,28, nur Versand, Text klingt nach maschineller Uebersetzung ("als ob das Telefon zu 100% gut funktioniert"). |

### Bestaetigtes Preisniveau erreicht die 20 Prozent nicht

| ID | Titel | Grund |
|---|---|---|
| 3497121841 | MacBook Pro 14" 2021 M1 Pro 16/512, 750 € | Bestaetigtes Niveau: mac-store24 ab 999 €, RefurbMe ab rund 590 € fuer "gut". Gegen den unteren bestaetigten Wert kein Abstand von 20 %. |
| 3497337580 | MacBook Pro 13,3" 2020, i5 / 16 GB / 512 GB, 320 € | Intel-Geraet, Gebrauchtniveau 350-450 €. Abstand unter 20 %. |
| 3496976109 / 3496973138 | Thorens TD 320, je 300 € | hifishark (Referenzquelle fuer HiFi nach `prompt.md`): TD 320 Basisversion 220 € (Juli 2025) und 290 € (Mai 2025) verkauft. Die 300 € liegen auf Marktniveau; die hoeheren Notierungen betreffen MkII und MkIII. |
| 3497359642 | Thorens TD 160 ohne Tonabnehmer, 179 € | Kein Median. Ohne System und mit "bei Abholung viel guenstiger" liegt das Angebot im ueblichen Rahmen. |
| 3497384600 | Thorens TD 160 Super mit SME 3009 III, 579 € | Kein Median. Die Kombination ist gesucht, aber 579 € entsprechen dem Niveau vergleichbarer Angebote; kein belegbarer Abstand. |
| 3497095504 | Omega Speedmaster Date Ref. 3513.30.00, 1.500 € | Marktniveau der Ref. 3513 liegt bei rund 1.600-2.200 €, ohne Papiere am unteren Rand. Abstand unter 20 %; zusaetzlich Konto 3 Tage alt. |
| 3497380545 | Ueberseecontainer 40 Fuss High Cube, 1.500 € | Preis ist netto: mit 19 % MwSt 1.785 € gegen einen Median von 2.500 €. Gewerblicher Anbieter, Beulen und Rost. |
| 3497389547 ausgenommen: 3021035129 / 2967620571 / 3340264765 | USM Haller von Haendlern, 400-790 € | Alle drei von gewerblichen Anbietern (HKMK, zwei weitere Haendler) und deutlich kleinere Konfigurationen: ein Rollcontainer mit dokumentierten Schaeden, ein zweifaechriges Regal, ein Lowboard mit 35 cm Tiefe. Haendlerpreise bilden hier den Markt. |
| 3496846865 | Gibson Les Paul Traditional 2015, 890 € | Dieselbe Gitarre desselben Verkaeufers wurde am 26.08. unter der Anzeigen-ID 3494599106 bereits gemeldet. Neu eingestellte Anzeige, gleicher Titel, gleicher Preis - die ID-Pruefung gegen `deal_log.csv` faengt das nicht. Keine zweite Meldung. |
| 3497035711 | BMW E36 318i, 2.800 € | Baujahr 1992, neuer TUEV und viele Neuteile, aber ausgeblichener Lack und dritte Hand; Median 4.297 € mischt gepflegte Sammlerfahrzeuge. Kein belegbarer Abstand von 20 %. |
| 3497367869 | Simson S51 Comfort 4-Gang, 2.999 € | Betriebserlaubnis vorhanden, aber "sollte einen Service bekommen", 1,5 Jahre gestanden. Gegen bestaetigte S51-Preise kein Abstand von 20 %. |
| 3497350913 | Cube Stereo Race 29, 699 € | Aeltere Baureihe ohne Modelljahr; Gebrauchtniveau 600-900 €. |
| 3496565169 | Cube Cross Race SL Gravel, 999 € | Neu aufgebaut mit Ultegra und DT Swiss RR22, aber Konto juenger als sechs Monate; Gebrauchtniveau vergleichbarer Aufbauten 1.000-1.500 €. |
| 3496846533 | Specialized Stumpjumper FSR 26 Zoll, 420 € | 26-Zoll-Fully aelterer Bauart, laenger nicht genutzt; Marktniveau 350-500 €. |
| 3497086259 | Gudereit Trekkingrad, 399 € | Kein Modell genannt, Infos nur "den Bildern zu entnehmen". |
| 3497088868 | Omlet Eglu Cube Huehnerstall, 580 € | Gebrauchtniveau mit automatischer Tuer 400-600 €. Ein Bild. |
| 3497025051 | Vitra Eames Plastic Side Chair RE DSW, 170 € je Stuhl | Die RE-Variante aus Recyclingkunststoff ist die guenstigere Ausfuehrung; gebrauchte DSW liegen bei 150-250 €. |
| 3496944730 | DJI Mini 4 Pro ohne Fernsteuerung, 430 € | Der Median 700 € gilt fuer Sets *mit* Fernsteuerung. Eine DJI RC 2 kostet allein rund 250 €, damit liegt das Angebot faktisch auf Marktniveau. Gleiche Begruendung wie am 28.08. bei 3496393030. |
| 3497363798 | Hilti DX 460 Bolzensetzgeraet, 190 € | Gebrauchtniveau mit Koffer 250-400 €, Abstand knapp unter der Schwelle; zudem nur Versand und in Deutschland Sachkundenachweis noetig. |
| 3497396642 | Carl Zeiss Jena Mikroskop, 150 € | Kein Modell genannt; die Spanne bei Zeiss-Jena-Monokularen reicht von 80 bis 400 €. |
| 3335747738 | iPhone 12 128 GB, 150 € | Abstand rund 32 % gegen einen Median von 220 €, aber absolut nur 70 €; Akku getauscht, Gehaeusespuren. Kein belastbarer Fund. |

## Zahlenwerk

| Stufe | Anzahl |
|---|---|
| Gesichtet | 24.888 |
| Modell-Match | 149 |
| Vorfilter | 148 |
| Preisschwelle | 20 |
| Scoring | 12 |
| Kandidaten in `candidates.json` (24-Stunden-Sammlung) | 83 |
| Bereits in `deal_log.csv` | 0 |
| Inhaltlich geprueft | 83 |
| Gemeldet | 2 |
