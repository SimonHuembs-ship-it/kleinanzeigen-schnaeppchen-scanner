# Lauf 2026-09-01, morgens

**Zeitpunkt:** 1. September 2026, 07:05 Uhr (Berlin)
**Datenstand `candidates.json`:** 2026-09-01T04:53:43+02:00, also 2 Stunden 12 Minuten alt zum Laufbeginn. Innerhalb der Frist aus prompt.md Schritt 1 (vier Stunden), Lauf regulaer durchgefuehrt.
**Zeitraum des letzten Sammellaufs:** 2026-08-31T23:37:30+02:00 bis 2026-09-01T04:37:30+02:00
**Gesichtete Anzeigen laut Sammler:** 31.260

## Zahlen

| | |
|---|---|
| Kandidaten in `candidates.json` | 124 |
| davon bereits in `deal_log.csv` | 0 |
| geprueft | 124 |
| davon Beschreibung, Attribute und Verkaeuferprofil vollstaendig gelesen | 61 |
| extern per Websuche gegengeprueft | 12 |
| gemeldete Funde | 3 |

Der Lauf hat die Zehner-Grenze nicht erreicht, es wurde also nicht vorzeitig
abgebrochen. Die Reihenfolge der Pruefung folgte dem absoluten Abstand zum
Median und den liquiden Kategorien (Uhren, Apple, Drohnen). Der lange Rest mit
Ersparnissen unter rund 700 EUR wurde auf Aktenlage beurteilt, also anhand von
Titel, Referenzguete, Uebergabeweg und Warnsignalen, ohne eigene externe
Marktwertrecherche. Das ist in den Verwurfsgruenden so gekennzeichnet.

## Gemeldete Funde

| Anzeige | Preis | Bestaetigtes Marktniveau | Abstand |
|---|---|---|---|
| [Omega Speedmaster Professional Chocolate (Brown) Dial](https://www.kleinanzeigen.de/s-anzeige/omega-speedmaster-professional-chocolate-brown-dial/3495882620-157-12896) | 3.700 EUR | 4.700 bis 5.800 EUR (WatchCharts: 5.166 USD Privatmarkt, 5.962 USD Haendler; konkrete Angebote 6.000 USD Full Set und rund 6.400 USD aus Deutschland) | 22 bis 36 Prozent |
| [Gibson Les Paul Standard, Baujahr 2016](https://www.kleinanzeigen.de/s-anzeige/gibson-les-paul-standard/3500143360-74-1679) | 1.100 EUR | 2.000 bis 2.200 EUR (eBay.de 2.184 EUR fuer Baujahr 2016 mit Hartschalenkoffer; Gitarre & Bass nennt rund 2.000 EUR fuer eine gebrauchte Standard) | rund 45 bis 50 Prozent |
| [DJI Mini 3 Pro inklusive DJI RC mit Display](https://www.kleinanzeigen.de/s-anzeige/dji-mini-3-pro-drohne-inklusive-der-dji-rc-fernsteuerung-display/3500348963-249-13374) | 350 EUR | 450 bis 500 EUR (eBay.de 450 EUR, Kleinanzeigen 450 EUR und 480 EUR VB fuer dieselbe Kombination) | 22 bis 30 Prozent |

Keiner der drei Kandidaten traegt `signale.unkenntnis_bonus`. In diesem
Kandidatensatz trug ihn kein einziger Kandidat.

### Anmerkungen zu den Funden

**Omega Speedmaster.** Die Anzeige datiert die Uhr auf 2021, das beschriebene
Chocolate-Zifferblatt mit Saphirglas und Glasboden gehoert aber zur Referenz
311.30.42.30.13.001, die von 2007 bis 2013 gebaut wurde. Wahrscheinlich ist 2021
das Kaufjahr des Verkaeufers. Genau diese Sonderausfuehrung ist der Grund fuer
den Fund: Der Verkaeufer preist die Uhr wie eine gewoehnliche gebrauchte
Speedmaster ein. Der Abgleich Gehaeuseboden gegen Garantiekarte steht als
Pruefpunkt in der Mail.

**Gibson Les Paul Standard.** Nur Abholung, kein Versand, kein Kaeuferschutz,
offengelegter kosmetischer Mangel am 5. Bund, funfjaehriges Konto mit allen drei
Abzeichen auf Stufe 2. Das ist das Profil, das prompt.md als schlechte Anzeige
eines ehrlichen Verkaeufers beschreibt. Der Kleinanzeigen-Median war mit
Streuung 3,19 nicht belastbar und wurde deshalb durch `referenz_hinweis` ersetzt,
`ersparnis_eur` bleibt weg.

**DJI Mini 3 Pro.** Der schwaechste der drei Funde. Der Abstand liegt gegen das
guenstigste gleich ausgestattete Vergleichsangebot bei 22 Prozent und damit knapp
ueber der Schwelle. Die Anzeige nennt die Akkuzahl nicht, ein Teil des Abstands
koennte auf fehlendes Zubehoer entfallen; das steht als Risiko in der Mail.

## Verworfene Kandidaten

| ID | Titel | Preis | Grund |
|---|---|---|---|
| `3500152370` | Tesla 3  Standard Range Plus RWD | 13800 EUR | Tesla Model 3, 205.000 km, Fahrzeugzustand "Beschaedigtes Fahrzeug", Fehlermeldung BMS a079 und nur noch 280 km Reichweite: Akkuschaden erklaert den Preis, kein Fund. Kilometerstand liegt zudem ueber der Akkugarantiegrenze von 160.000 km fuer Model 3 RWD. |
| `3500210124` | Rolex Yachtmaster | 9500 EUR | Rolex Yacht-Master 2003, Referenz belastbar=false (Streuung 2,88, Median mischt Stahl/Gold- und Vollgoldmodelle). Versand ab 0,49 EUR ohne Abholung bei einer fuenfstelligen Uhr ist ein Betrugsmuster, das Material bleibt zwischen Attribut (Gelbgold) und Text (ungenannt) offen. Kein belastbarer Marktwert, verworfen. |
| `3499599336` | Rolex Submariner | 8000 EUR | Rolex Submariner 8.000 EUR: Der Text enthaelt den unausgefuellten Platzhalter "[Edelstahl/Oystersteel]" und nennt 30 mm Gehaeusedurchmesser, die Submariner hat 40/41 mm. Textbaustein- bzw. KI-Rueckstand plus falsche Spezifikation, verworfen. |
| `3500188347` | Rolex Datejust 41 / NEU | 8400 EUR | Rolex Datejust 41 Full Set 2022, extern geprueft: vergleichbare 126300 Full Sets von 2022 auf dem deutschen Markt ab 8.900 EUR (Chrono24), Bandbreite bis rund 11.500 EUR. 8.400 EUR liegen nur rund 6 bis 12 Prozent darunter, Mindestabstand von 20 Prozent verfehlt. |
| `3500015597` | BMW BMW e36 328i | 7000 EUR | BMW E36 328i Cabrio: 249.948 km und ein vom Verkaeufer selbst genannter, reparierter Unfallschaden. Der Preis erklaert sich, kein Fund. |
| `3500218297` | Rolex Datejust 31 | 7900 EUR | Rolex Datejust 31 Ref. 278240 Stahl fuer 7.900 EUR: Der Median 11.590 EUR stammt aus "Rolex Datejust 31" und mischt Gold- und Diamantvarianten mit der reinen Stahlreferenz. Fuer 278240 in Stahl liegt der Angebotspreis auf Marktniveau, kein Abstand. |
| `3500041137` | Mercedes Benz W124 200 | 2000 EUR | Mercedes W124 200 Vergaser, 258.947 km, Fahrzeugzustand "Beschaedigtes Fahrzeug", HU faellig, Schweissarbeiten an der Wagenheberaufnahme noetig. Der Verkaeufer legt die Maengel offen, der Preis ist dadurch erklaert. |
| `3499549974` | Rolex Datejust 36 mm | 5500 EUR | Rolex Datejust 36 mit Perlmuttblatt und Diamantluenette fuer 5.500 EUR: angegebene "Referenznummer 0684" entspricht keinem Rolex-Referenzformat, Versand ab 0,49 EUR ohne Abholung, Verkaeuferbewertung 0,50. Verworfen. |
| `2888542924` | Tudor Black Bay Chronograph Stahl Automatik Herrenuhr 7936 | 4190 EUR | Tudor Black Bay Chronograph 79360N neu vom Haendler fuer 4.190 EUR: Der Median 7.220 EUR aus "Tudor Black Bay 79360N" liegt deutlich ueber dem realen Gebrauchtniveau dieser Referenz; 4.190 EUR entsprechen ungefaehr dem Marktpreis, kein 20-Prozent-Abstand. |
| `3415337819` | Omega Seamaster 300M Titan und Gelbgold, in sehr nahe Neuz | 3750 EUR | Omega Seamaster 300M Titan/Gelbgold: Referenz belastbar=false (Streuung 3,19 bei n=10). Die Anzeigen-ID 3415337819 stammt aus einem deutlich frueheren Nummernkreis, das Angebot laeuft also seit Langem zu diesem Preis, was gegen eine Unterbewertung spricht. Kein eigener belastbarer Referenzwert gefunden. |
| `3500188197` | BMW e36 Cabrio | 5000 EUR | BMW E36 Cabrio, 253.000 km, Verdeckstoff gerissen, eingetragene Tieferlegung und Spurverbreiterung, Verkaeuferbewertung 0,14. Preis erklaert sich durch Zustand und wertmindernde Umbauten. |
| `3499614671` | Honda Fireblade 1000rr | 4500 EUR | Honda CBR 1000RR von 2004 mit 50.000 km: Der Median 6.930 EUR aus "Honda Fireblade 1000rr" enthaelt deutlich juengere Baujahre. Fuer eine SC57 von 2004 mit dieser Laufleistung ist 4.500 EUR Marktniveau. |
| `3499643179` | Jaeger-LeCoultre Master Compressor Diving GMT – Titan | 4997 EUR | Jaeger-LeCoultre Master Compressor Diving GMT Titan: Der Median stammt aus der Suche "Jaeger LeCoultre Master" und mischt Reverso, Master Control und Master Ultra Thin. Die Master Compressor Diving GMT handelt gebraucht im Bereich der geforderten 4.997 EUR, zusaetzlich Warnsignal "Vorkasse gefordert". |
| `3500067860` | OMEGA SEAMASTER DIVER 300M BLAU QUARTZ | 2350 EUR | Omega Seamaster Diver 300M Ref. 254180 von 1995 mit Quarzwerk: Der Median 4.490 EUR aus "OMEGA SEAMASTER DIVER 300M" besteht ueberwiegend aus modernen Automatikmodellen. Eine Vintage-Quarzvariante ist nicht dasselbe Produkt, Referenzgruppe nicht vergleichbar. |
| `3500063088` | Glashütte Senator - Original | 3850 EUR | Glashuette Senator: Referenz belastbar=false (Streuung 3,47). Die Beschreibung laesst offen, ob es sich um eine Glashuette Original Senator oder eine GUB-Vintageuhr handelt, zwischen beiden liegt ein Faktor zehn. Ohne Modellklaerung kein Marktwert. |
| `3500071703` | Mercedes 190E W201 | 4250 EUR | Mercedes 190E 1.8 von 1990 mit 228.200 km, gewerblicher Anbieter, Beschreibung besteht aus einer Zeile. Der Median aus "Mercedes 190E W201" enthaelt auch 2.3-16V und gepflegte H-Kennzeichen-Fahrzeuge, hier keine belastbare Vergleichbarkeit. |
| `3315713639` | Drehmaschine-konventionell-elektronisch HEIDENREICH & HARB | 2618 EUR | Drehmaschine Heidenreich & Harbeck, Baujahr 1970: Der Median stammt aus der generischen Suche "Drehmaschine konventionell elektronisch" ueber alle Baugroessen und Hersteller. Ohne Typenbezeichnung kein vergleichbarer Marktwert. |
| `3499590586` | BMW E36 316i – Blau – ohne TÜV | 1999 EUR | BMW E36 316i, 250.000 km, ausdruecklich ohne TUEV und als Projektfahrzeug angeboten. Preis erklaert sich, zusaetzlich Referenz belastbar=false. |
| `3500316797` | Riese und Müller Nevo GT Vario | 1800 EUR | Riese & Mueller Nevo GT Vario von 2023 mit 12.286 km fuer 1.800 EUR: Fuer eine Laufleistung dieser Groessenordnung liess sich kein belastbares Vergleichsangebot finden, die recherchierten Angebote betreffen nahezu neuwertige Raeder bei ueber 5.000 EUR. Akkualterung und anstehender Bosch-CX-Service erklaeren zudem einen Teil des Abstands. |
| `3500081929` | Omega Speedmaster | 2850 EUR | Omega Speedmaster Ref. 35205000 (Speedmaster Date/Automatik, kein Moonwatch): Der Median aus "Omega Speedmaster" wird von Professional-Moonwatches getragen, Referenzgruppe nicht vergleichbar. Zusaetzlich Konto juenger als sechs Monate. |
| `3500328930` | Cube Stereo Hybrid 140 E-Mountainbike Top Zustand | 1200 EUR | Cube Stereo Hybrid 140 fuer 1.200 EUR: Weder Modelljahr noch Ausstattungsvariante genannt ("Beschreibung auf den Bildern"), die Baureihe laeuft von 2016 bis heute mit Neupreisen von 2.500 bis 6.000 EUR. Ohne Modelljahr ist die Referenzgruppe nicht vergleichbar. |
| `3236699838` | Simson S51 | 1600 EUR | Simson S51 Ungarn-Reimport ohne Papiere, mehrjaehrige Standzeit, keine Startversuche, Fehlteile nicht ausgeschlossen, 21er Abnahme noetig. Preis erklaert sich. |
| `3500203516` | Fender Deluxe Reverb Tone Master | 750 EUR | Fender Deluxe Reverb Tone Master fuer 750 EUR: Der Median 2.300 EUR stammt aus "Fender Deluxe Reverb" und besteht aus Roehrenverstaerkern (65 Deluxe Reverb Reissue und Vintage). Der Tone Master ist der digitale Modeling-Amp mit rund 1.000 EUR Neupreis, 750 EUR sind Marktniveau. Phantomersparnis durch falsche Referenzgruppe. |
| `3499605016` | ROLEX oyster Perpetual Date 34mm | 3211 EUR | Absolute Ersparnis von 1539 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500094983` | BMC Urs 01 Three Gravelbike Campagnolo Ekar Gr. M | 2250 EUR | BMC URS 01 Three mit Campagnolo Ekar, 2023, fuer 2.250 EUR: Es liessen sich keine zwei konkreten Gebrauchtangebote desselben Modells mit Preis finden, nur Neupreise (rund 7.200 USD UVP). Ohne bestaetigten Gebrauchtmarktwert kein Fund, obwohl das Angebot ansonsten sauber wirkt. |
| `3500234815` | Ducati Monster 900 ie | 1900 EUR | Ducati Monster 900 ie von 2000 mit 40.000 km, muss zum TUEV, Bremsenservice und neue Zahnriemen stehen an. Preis erklaert sich. |
| `3500084230` | Simson S51 Enduro 4Gang | 2200 EUR | Simson S51 Enduro, Papiere muessen neu beantragt werden, ausdruecklich als "Basis fuer einen Neuaufbau" angeboten. Preis erklaert sich. |
| `3499700305` | Simson Schwalbe KR51/2 | 1450 EUR | Simson Schwalbe KR51/2, nicht fahrbereit, Papiere muessen neu beantragt werden. Preis erklaert sich. |
| `3499722059` | Simson S51 | 1900 EUR | Simson S51 B2-4, komplett neu aufgebaut, mit KBA-Papieren, 1.900 EUR. Verkaeuferkonto wurde am 31.08.2026 angelegt, also am Vortag. Neues Konto plus hochwertiges, sofort weiterverkaeufliches Fahrzeug deutlich unter Markt ist ein Betrugsmuster, verworfen. |
| `3500172655` | Simson Sperber | 1500 EUR | Simson Sperber: eingestellt in der Kategorie "Ersatz- & Reparaturteile", zwei Zeilen Beschreibung, nur Versand ohne Abholung. Unklar, ob Fahrzeug oder Teile, kein Urteil moeglich. |
| `3500403723` | Drehbank, Drehmaschine mit Zubehör | 750 EUR | Drehbank ohne bekannten Hersteller, automatischer Vorschub defekt, Oelverlust, Riemen beschaedigt. Preis erklaert sich, Referenz zudem belastbar=false (Streuung 3,75). |
| `3499685072` | Simson S51 | 2100 EUR | Absolute Ersparnis von 1095 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500315775` | Gibson Les Paul Studio E-Gitarre mit Koffer Sunburst | 1300 EUR | Gibson Les Paul Studio 1.300 EUR: Referenz belastbar=false (Streuung 3,19, Median mischt Studio, Standard und Custom). Eine Les Paul Studio handelt gebraucht in genau dieser Preisregion, kein Abstand. Zudem nur Versand, kein Baujahr, keine Seriennummer. |
| `3500322444` | Canyon CF SL 7 Ultimate (Größe L) | 1000 EUR | Canyon Ultimate CF SL 7 fuer 1.000 EUR: wird ausdruecklich ohne Sattel und ohne Pedale verkauft, was gegenueber den Vergleichsanzeigen mit vollstaendigem Aufbau rund 100 bis 200 EUR ausmacht. Damit bleibt kein gesicherter 20-Prozent-Abstand. |
| `3500231876` | Tag Heuer aquaracer | 800 EUR | TAG Heuer Aquaracer 800 EUR: Der Median 1.695 EUR aus "Tag Heuer aquaracer" umfasst Quarz- und Automatikmodelle von 400 bis 3.000 EUR. Die genannte Referenz WAY101.E.FC8222 entspricht keinem gaengigen TAG-Heuer-Referenzformat, zudem nur Versand. |
| `3499700711` | Trek Procaliber 8 | 850 EUR | Referenz belastbar=false (Streuung 2,64), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 850 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500397717` | Cassina Maralunga 2-Sitzer Sofa / Design-Klassiker | 800 EUR | Cassina Maralunga 2-Sitzer Stoff fuer 800 EUR: Referenz belastbar=false (Streuung 3,53). Ein vergleichbarer gebrauchter Stoff-Zweisitzer in sehr gutem Zustand steht bei 950 EUR (PicClick DE), damit liegt der Abstand unter 20 Prozent. |
| `3500318462` | Cube Rennrad Pro Litening blau/weiß/rot | 360 EUR | Referenz belastbar=false (Streuung 2,73), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 839 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3499719954` | Cube E bike Reaction hpa | 820 EUR | Absolute Ersparnis von 830 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500168472` | Omega Constellation  | 1050 EUR | Omega Constellation ohne Rechnung und Box, vier Zeilen Beschreibung, Referenz belastbar=false (Streuung 3,25). Weder Referenznummer noch Kaliber genannt, kein Marktwert bestimmbar. |
| `3500165318` | Simson Schwalbe KR 51/1 | 1700 EUR | Absolute Ersparnis von 820 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500213863` | Piaggio Vespa Sprint S 50 | 1800 EUR | Absolute Ersparnis von 810 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499718064` | Cube Nuroad One FE Gr. M Gravel Bike neuwertig Rennrad Gra | 850 EUR | Absolute Ersparnis von 784 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500199854` | Gibson Les Paul Standard Goldtop | 1600 EUR | Gibson Les Paul Standard Goldtop 2016 fuer 1.600 EUR: Referenz belastbar=false. Gegen das bestaetigte Niveau von rund 2.000 bis 2.200 EUR liegt der Preis nur etwa 20 bis 27 Prozent darunter, aber die Anzeige nennt weder Koffer noch Zertifikat und die Delle im Korpus druckt den Wert. Grenzfall, nicht ueberzeugt, verworfen. |
| `3499652155` | Mountainbike Cube Reaction TM ONE gold - Rahmenhöhe XL | 695 EUR | Referenz belastbar=false (Streuung 2,67), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 755 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3499606201` | Stevens Triton Trekking e-bike - mit Strassenausstattung | 850 EUR | Absolute Ersparnis von 749 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499701897` | Simson Star | 1250 EUR | Absolute Ersparnis von 721 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499600488` | Dieter Knoll Sofa in Beige - sehr guter Zustand | 500 EUR | Absolute Ersparnis von 700 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500318332` | Cube Reaction Pro 29 Zoll Mountainbike | 900 EUR | Referenz belastbar=false (Streuung 2,5), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 700 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500381165` | Gravelbike Specialized Diverge Base E5 | 850 EUR | Absolute Ersparnis von 650 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499666523` | Apple MacBook Pro 14“ m4 pro | 1100 EUR | MacBook Pro 14 M4 Pro 24/512 GB fuer 1.100 EUR: nur Versand ohne Abholung, Verkaeufer ohne jede Bewertung, Beschreibung ist reiner Werbetext ohne Seriennummer, Ladezyklen oder Akkuzustand. Aktuelle Apple-Hardware rund 40 Prozent unter Markt bei genau diesem Profil ist das klassische Betrugsmuster, verworfen. |
| `3499601476` | Haibike Trekking 5.0 Ebike Schulrad Pedelec | 550 EUR | Absolute Ersparnis von 649 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499559825` | USM Haller Kommode Sideboard TV Möbel | 750 EUR | USM Haller TV-Moebel 150 cm anthrazit fuer 750 EUR: Die recherchierten Vergleichspreise streuen von 607 bis ueber 2.000 EUR je nach Konfiguration, ein belastbarer Marktwert fuer genau diesen Aufbau (eine Hoehe, eine Klapptuer, Schluessel fehlt) liess sich nicht bestimmen. |
| `3500340453` | Canyon Neuron 6 Mountainbike Fully | 850 EUR | Absolute Ersparnis von 649 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500387784` | Trek ex Fuel Fully Mountainbine (M Rahmen) | 1100 EUR | Referenz belastbar=false (Streuung 2,87), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 639 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3499694892` | Omega Constellation Automatic Chronometer Day-Date Vintage | 690 EUR | Omega Constellation Day-Date, vermutlich fruehe 1970er, ungeprueft und ungewartet. Der Verkaeufer beschreibt ehrlich, dass er weder Referenz noch Kaliber kennt. Vintage-Constellations in diesem Zustand handeln bei rund 600 bis 1.200 EUR, 690 EUR sind Marktniveau. |
| `3500000050` | USM Haller Sideboard (gebraucht) mittelfristig | 868 EUR | Absolute Ersparnis von 631 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500316172` | Specialized Mountainbike Hardtail | 370 EUR | Referenz belastbar=false (Streuung 3,8), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 625 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3499645368` | Macbook Pro 14" M3 1TB 8GB - Wie Neu | 980 EUR | MacBook Pro 14 M3 mit 8 GB RAM und 1 TB SSD fuer 980 EUR: Kein belastbares Gebrauchtniveau fuer genau diese Konfiguration recherchierbar (Haendler fuehren fast ausschliesslich 16-GB-Varianten). Ohne bestaetigten Marktwert kein Fund, der geschaetzte Abstand liegt zudem unter 20 Prozent. |
| `3499989996` | USM Haller Sideboard weiß mit 2 Schubladen und Regalfach | 590 EUR | Absolute Ersparnis von 610 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500330854` | Cube Custom Bike – Top Zustand | 670 EUR | Referenz belastbar=false (Streuung 3,45), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 580 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500231236` | Apple Macbook Air M2 15 Zoll 16 GB Ram | 333 EUR | MacBook Air 15 M2 fuer 333 EUR: Der Verkaeufer legt einen Fluessigkeitsschaden offen (gezuckerter Kaffee, Tastaturbeleuchtung defekt, Tastatur klebt, Lautsprecher kratzt). Ehrlich beschrieben, aber der Defekt erklaert den Preis und birgt Korrosionsfolgerisiko. |
| `3467084457` | Fender Jazz Bass Mexico   | 470 EUR | Referenz belastbar=false (Streuung 2,67), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 550 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3499666104` | Fully specialized Mountainbike Fahrrad shimano | 450 EUR | Specialized Fully ohne Modell- und Jahresangabe, Referenz belastbar=false (Streuung 5,10). Ohne Modell kein Marktwert. |
| `3500210584` | Apple MacBook Pro Laptop | 300 EUR | MacBook Pro Retina 15 von Mitte 2015 mit Staingate und macOS Monterey: ausgelaufener Support und Displayschaden, Preis erklaert sich. Referenz zudem belastbar=false. |
| `3500212117` | 4 Eames Plastic Armchair DAW (neue Höhe 4) Orange /Ahorn s | 420 EUR | 4 Eames Plastic Armchair DAW: Der Anzeigenpreis von 420 EUR gilt laut Beschreibung pro Stuhl, der Median 897,50 EUR bezieht sich auf Vierer-Sets. 420 EUR fuer einen gebrauchten Vitra DAW sind Marktniveau, die Ersparnis ist ein Artefakt der Referenzgruppe. |
| `3424293064` | Gibson Les Paul Melody Maker 120th Anniversary 2014 – Made | 899 EUR | Gibson Les Paul Melody Maker 120th Anniversary 2014 mit Lackbeschaedigung fuer 899 EUR: Der Median aus "Gibson Les Paul 120th 2014" enthaelt Standards und Traditionals. Eine Melody Maker handelt gebraucht unterhalb dieses Preises, kein Fund. |
| `3500394513` | e-bike Haibike SDURO 6.0 Trekking ebike | 650 EUR | Absolute Ersparnis von 450 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500182409` | iPhone 16 zu verkaufen | 250 EUR | iPhone 16 fuer 250 EUR: Beschreibung nennt weder Speichergroesse noch Akkuzustand, wirbt stattdessen mit "Dual-Kamera" und "Grosses Display", und die Anzeige fuehrt keine Bilder. Aktuelles iPhone zu 36 Prozent des Marktwerts ohne pruefbare Angaben, verworfen. |
| `3499636068` | Vitra EA 104 Aluminium Chair Elfenbein Warmgrau Bürostuhl | 849 EUR | Absolute Ersparnis von 430 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499556245` | DJI Mini 4 Pro Fly More Zubehör | 250 EUR | DJI Mini 4 Pro "Fly More Zubehoer": Es wird ausschliesslich das Zubehoerset verkauft (Tasche, drei Akkus, Ladestation, Propeller), nicht die Drohne. Der Median 680 EUR gilt fuer die komplette Drohne, Referenzgruppe nicht vergleichbar. |
| `3500349427` | Mountainbike Canyon | 450 EUR | Referenz belastbar=false (Streuung 3,44), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 400 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500230770` | Trekking Rad | 400 EUR | Referenz belastbar=false (Streuung 3,38), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 372 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500028715` | BMC Twostroke AL Hardtail Mountainbike Gr.S | 390 EUR | Absolute Ersparnis von 360 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499560740` | Original USM Haller Rollcontainer - 4 Schubladen, top Zust | 550 EUR | Absolute Ersparnis von 350 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500046771` | Canyon Nerve AL+ | 450 EUR | Absolute Ersparnis von 350 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499707879` | Pegasus Damen Trekkingrad schwarz mit Korb 28 Zoll | 450 EUR | Referenz belastbar=false (Streuung 2,97), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 349 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500399437` | Trek Mountainbike 29 Zoll Sehr guter Zustand mit Rechnung | 350 EUR | Referenz belastbar=false (Streuung 3,34), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 349 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500129887` | USM HALLER Rollcontainer, NEUWERTIG, reinweiss | 350 EUR | Absolute Ersparnis von 349 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500408075` | IPhone 17 Pro Max | 800 EUR | iPhone 17 Pro Max 256 GB fuer 800 EUR: extern geprueft, refurbished handelt das Modell derzeit bei rund 760 bis 850 EUR (refurb.me). 800 EUR sind Marktniveau, kein Abstand. Der Median 1.149 EUR wird von versiegelter Neuware getragen. Zusaetzlich widerspricht der Anzeigentext ("Preis: 1.000 EUR VB") dem Anzeigenpreis. |
| `3500347983` | Thonet Stühle schwarz, stapelbar, 4 Stück | 150 EUR | Referenz belastbar=false (Streuung 3,62), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 340 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500238706` | USM Haller Schreibtisch, Tisch 200x100 | 165 EUR | Referenz belastbar=false (Streuung 2,91), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 335 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3398206292` | USM Haller Container Rollcontainer schwarz | 375 EUR | Absolute Ersparnis von 324 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500111895` | Giant Damen Trekkingrad Citybike | 300 EUR | Referenz belastbar=false (Streuung 3,58), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 324 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500204232` | Apple MacBook, neuwertiger Zustand | 550 EUR | "Apple MacBook" ohne Modell-, Chip- und Jahresangabe, Verkaeuferbewertung 0,12, nur Versand. Ohne identifizierbares Modell kein Marktwert bestimmbar. |
| `3499997395` | Weißes Brautkleid mit Swarovski steine Perlenstickerei & R | 300 EUR | Referenz belastbar=false (Streuung 2,85), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 309 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500296557` | Cube Mountainbike „29“ | 350 EUR | Referenz belastbar=false (Streuung 3,96), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 300 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3499681640` | USM Haller Schreibtisch – Weiß – 200 × 100 cm | 300 EUR | Absolute Ersparnis von 299 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499565188` | DJI Mini 4 Pro mit Wasserschaden (defekt) | 390 EUR | DJI Mini 4 Pro mit Wasserschaden, laesst sich nicht mehr einschalten, ausdruecklich als defekt verkauft. Kein Fund. |
| `3500356059` | Cube Moutainbike Herren / Top Zustand | 300 EUR | Referenz belastbar=false (Streuung 4,22), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 270 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500269989` | iPhone 15 Pro | 300 EUR | iPhone 15 Pro fuer 300 EUR: Beschreibung besteht aus vier Woertern, keine Speichergroesse, kein Akkuzustand, keine Bilder, nur Versand. Nicht beurteilbar. |
| `3499656693` | Stevens Herren Trekkingrad | 300 EUR | Absolute Ersparnis von 255 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500357768` | Cube Trekking-/Citybike | 300 EUR | Referenz belastbar=false (Streuung 2,71), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 240 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3499705726` | iPhone 15 128 gb | 220 EUR | Absolute Ersparnis von 230 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499715064` | Iphone 14 Pro 256GB | 250 EUR | iPhone 14 Pro 256 GB fuer 250 EUR: Zustand "Defekt", Wasserschaden, Face ID ausgefallen. Preis erklaert sich. |
| `3500412175` | iPhone 15 Pro Max 256 GB – Titan Schwarz | 400 EUR | Absolute Ersparnis von 220 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499699119` | DJI Mavic Pro Fly More Combo inkl 2 Akkus | 280 EUR | DJI Mavic Pro (Erstgeneration 2016) fuer 280 EUR: Der Median stammt aus der Suche "DJI Mavic Pro 2" und enthaelt die deutlich teurere Mavic 2 Pro. Fuer die Erstgeneration ist 280 EUR Marktniveau, zusaetzlich gebrochene Kameraabdeckung. |
| `3499569803` | Rennrad Cube Streamer schwarz-orange | 300 EUR | Absolute Ersparnis von 200 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500386135` | iPhone 15 (Blau) | 300 EUR | iPhone 15 fuer 300 EUR: Rueckseite geplatzt, Kanten mit Macken, Akku bei 85 Prozent. Preis erklaert sich. |
| `3499718550` | iPhone 14 Pro Max // 256GB | 300 EUR | Absolute Ersparnis von 199 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499627764` | USM Haller Tisch, Schreibtisch, 200 x 100, schwarz Eiche H | 400 EUR | Absolute Ersparnis von 195 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500374166` | iPhone 14 pro max (deep purpel) | 250 EUR | Absolute Ersparnis von 190 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500322954` | Mountainbike von Cube  | 300 EUR | Referenz belastbar=false (Streuung 2,97), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 190 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500375411` | Iphone 15 128 GB | 249 EUR | Absolute Ersparnis von 186 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3499661117` | Wilkhahn Bürostuhl – ergonomisch & vielseitig verstellbar | 190 EUR | Referenz belastbar=false (Streuung 3,94), der Kleinanzeigen-Median mischt verschiedene Produkte und zaehlt damit nicht. Absolute Ersparnis 184 EUR lag unterhalb der Pruefprioritaet dieses Laufs, kein eigener Marktwert recherchiert. |
| `3500363237` | iPhone 14 128 GB schwarz | 170 EUR | Absolute Ersparnis von 180 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500408674` | iPhone 15 Pro 128 GB | 340 EUR | iPhone 15 Pro 128 GB fuer 340 EUR: Rueckseite gesprungen, Akku bei 81 Prozent. Preis erklaert sich. |
| `3500395898` | iPhone 14 Pro 256GB | 300 EUR | Absolute Ersparnis von 150 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500388870` | DJI Mavic Pro Platinum mit Fly more Combo Kit und Zubehör | 300 EUR | DJI Mavic Pro Platinum, am hinteren rechten Flugarm fehlt eine Motorabdeckung, nur Versand. Gebrauchtniveau fuer eine Mavic Pro Platinum liegt bei rund 250 bis 350 EUR, kein Abstand. |
| `3500346711` | IPhone 13 Pro 128GB | 179 EUR | Absolute Ersparnis von 140 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500335055` | iPhone 14 128gb Midnight Blue OVP | 165 EUR | Absolute Ersparnis von 135 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500356255` | iPhone 15 schwarz | 300 EUR | iPhone 15 fuer 300 EUR: Verkaeufer seit 2009 mit Bewertung 1,0 und ehrlicher Beschreibung, aber die Speichergroesse fehlt. Zwischen 128 und 512 GB liegen rund 200 EUR, damit ist die Referenzgruppe nicht bestaetigbar. Grenzfall, verworfen. |
| `3500367485` | iPhone 13 Pro Blau | 220 EUR | Absolute Ersparnis von 127 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500379381` | Apple iPhone 14, 128 GB | 225 EUR | Absolute Ersparnis von 125 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500340149` | iPhone 13 Pro Max – 256 GB – | 270 EUR | iPhone 13 Pro Max 256 GB fuer 270 EUR: Der Verkaeufer legt einen Schaden an der Rueckseite offen. Der Preis erklaert sich. |
| `3500393740` | iPhone 12 Pro | 150 EUR | Absolute Ersparnis von 100 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500391277` | Iphone 12 Pro Max 256 GB - GOLD | 200 EUR | Absolute Ersparnis von 100 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500326149` | VITRA Occasional Table LTR Beistelltisch weiß - Glanzchrom | 175 EUR | Absolute Ersparnis von 95 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500385430` | Iphone 13 128GB Weiß | 160 EUR | Absolute Ersparnis von 90 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500384441` | Iphone 13 Weiß 128GB | 160 EUR | Absolute Ersparnis von 90 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |
| `3500410923` | iPhone 12 Pro 128 GB Schwarz | 150 EUR | Absolute Ersparnis von 80 EUR lag unterhalb der Pruefprioritaet dieses Laufs (Reihenfolge nach absolutem Abstand und Liquiditaet). Aktenlage ohne Auffaelligkeit, aber ohne eigene externe Marktwertbestaetigung kein meldefaehiger Fund. |

## Beobachtungen fuer den Sammler

1. **Uhren-Mediane sind systematisch zu hoch.** Bei `Rolex Datejust 31`,
   `Rolex Datejust 41`, `Omega Speedmaster`, `Tag Heuer aquaracer` und
   `Jaeger LeCoultre Master` mischt die Referenzsuche Stahl-, Gold- und
   Diamantvarianten derselben Modellfamilie. `belastbar` steht dabei mehrfach auf
   `true`, weil die Streuung unter 2,5 bleibt, obwohl die Produkte nicht
   vergleichbar sind. Eine Einschraenkung auf das Attribut `Material` wuerde hier
   viel Phantomersparnis wegnehmen.
2. **Zubehoer wird gegen Vollgeraete gemessen.** `DJI Mini 4 Pro Fly More
   Zubehoer` (nur das Zubehoerset) lief gegen den Median der kompletten Drohne,
   und bei den vier Eames-Stuehlen gilt der Anzeigenpreis pro Stueck, der Median
   aber fuer Vierer-Sets. Ein Filter auf Worte wie "Zubehoer", "Ersatzteile" oder
   "pro Stueck" im Titel und in der Preiszeile wuerde beide Faelle abfangen.
3. **Produktgenerationen laufen zusammen.** `DJI Mavic Pro` gegen den Median von
   `DJI Mavic Pro 2` und `Fender Deluxe Reverb Tone Master` (Digitalamp) gegen
   Roehren-Deluxe-Reverbs erzeugen zweistellige Phantomabstaende.
4. **Der iPhone-Block ist fast vollstaendig durch Defekte erklaert.** Von den
   sechs am tiefsten unter Median liegenden iPhones hatten fuenf eine
   offengelegte gesprungene Rueckseite, einen Wasserschaden oder einen Akku unter
   85 Prozent. Ein Regex auf "gesprungen", "geplatzt", "Wasserschaden",
   "Face ID" und Akkuprozentangaben in der Beschreibung wuerde diese Kandidaten
   schon in Stufe 1 aussortieren.
