# Lauf 2026-09-03, morgens

- **Ausgefuehrt:** 3. September 2026, 07:05 Uhr (MESZ)
- **Datenstand `candidates.json`:** 2026-09-03T04:22:34+02:00 (2 h 42 min alt, innerhalb der Vier-Stunden-Grenze)
- **Zeitraum des Sammellaufs:** 2026-09-02T23:03:41+02:00 bis 2026-09-03T04:03:41+02:00
- **Gesichtete Anzeigen:** 39.008
- **Kandidaten in der Warteschlange:** 166
- **Bereits in `deal_log.csv`:** 0
- **Geprueft:** 166 (Vorrang nach absoluter Ersparnis und Liquiditaet; die 45 aussichtsreichsten einzeln mit Websuche gegengeprueft)
- **Gemeldet:** 5

## Gemeldete Funde

| Titel | Preis | Bestaetigter Marktwert | Abstand | Kategorie |
|---|---|---|---|---|
| [BMW R100GS, 1993, 64.407 km](https://www.kleinanzeigen.de/s-anzeige/bmw-r100gs/3501544476-305-8014) | 4.200 € | 6.500–11.900 € (Marktkorridor Gebrauchtberatung Motorrad Online) | rund 35 % unter der Korridoruntergrenze | motorraeder |
| [Tudor Black Bay 58 Navy Blue 79030B](https://www.kleinanzeigen.de/s-anzeige/tudor-black-bay-58-navy-blue-uhr-guter-zustand-/3501945319-157-20462) | 2.349 € | rund 3.000 € Full Set (Chrono24, Spanne 3.000–3.900 €) | rund 22 % | uhren |
| [MacBook Pro 16" M4 Pro, 48/512 GB](https://www.kleinanzeigen.de/s-anzeige/macbook-pro-16-m4-pro-48-gb-512-gb-20-core-gpu/3501332352-278-25996) | 1.799 € | 2.400–3.300 € gebraucht, 2.724 € KA-Median (n=12) | rund 25–34 % | macbook |
| [Vitra Eames EA 119 Aluminium Chair, Orange](https://www.kleinanzeigen.de/s-anzeige/original-vitra-eames-ea-119-aluminium-chair-orange/3501831809-93-7155) | 890 € | 1.495–1.975 € gebraucht (eBay.de), 1.500 € KA-Median (n=51) | rund 40 % | design-sammeln |
| [DJI Mini 4 Pro Fly More Combo + ND-Filter](https://www.kleinanzeigen.de/s-anzeige/dji-mini-4-pro-fly-more-combo-nd-filter/3501863885-245-7244) | 400 € | 894–929 USD gebraucht (MPB), 680 € KA-Median (n=89) | rund 40 % | optik-drohnen |

## Nebenbefund: die Tudor ist eine Wiedereinstellung

Anzeige 3501945319 (Tudor Black Bay 58 Navy Blue, 2.349 Euro, Freising) ist
zeichengleich mit Anzeige 3493265891, die am 24.08.2026 gemeldet wurde. Titel,
Preis und der Verkaeufer-Suffix der URL (`-157-20462`) stimmen ueberein, nur die
Anzeigen-ID ist neu. Die Pruefung gegen `deal_log.csv` laeuft ueber die `id` und
faengt Wiedereinstellungen deshalb nicht; derselbe Befund wurde bereits am
26.08. (Gibson Les Paul) und am 30.08. (Tudor Prince Day-Date) notiert.

Zwei Folgerungen:

1. Die Uhr steht seit mindestens zehn Tagen unverkauft zum selben Preis. Das
   spricht dagegen, dass der Abstand zum Marktwert so gross ist wie berechnet;
   ein Full Set mit 22 Prozent Abstand waere in zehn Tagen normalerweise weg.
   Der Fund ist damit schwaecher, als die Mail ihn ausweist.
2. Ein Abgleich ueber `verkaeufer.id` plus Titel plus Preis statt allein ueber
   die Anzeigen-ID wuerde diese Klasse von Doppelmeldungen schliessen. Das ist
   eine Aenderung an Stufe 1 beziehungsweise an Schritt 1 der Anweisung, nicht
   etwas, das diese Routine im Lauf entscheiden sollte.

Der DJI-Mini-4-Pro-Fund ist keine Wiedereinstellung: Anzeige 3497781939 vom
29.08. traegt den Verkaeufer-Suffix `-245-27379`, die heutige `-245-7244`.

## Verworfene Kandidaten (161)

- **Porsche 911 SC Targa 3.0** (3501315474, 29911 €, porsche-911): Eigene Marktpruefung: Classic-Data-Marktwert 911 SC (1977-1983) in Zustand 2 liegt im Mai 2026 bei 50.600 bis 52.300 Euro, Zustand 3 damit bei rund 30.000 Euro. Mit 265.000 km, Patina-Lack, nicht belegten Getriebearbeiten und programmierbarem Steuergeraet statt Lambdaregelung ist das Fahrzeug ein Zustand-3-Auto und mit 29.911 Euro korrekt bepreist. Der Kleinanzeigen-Median von 53.901 Euro mischt Zustand-2-Wagen ein.
- **Tesla Model S 90D** (3501582359, 12345 €, tesla): Unfallschaden rechte Seite (13.000 Euro Reparaturkosten laut Gutachten), undichtes Luftfahrwerk und 285.000 km: Der Preis erklaert sich vollstaendig selbst. Zusaetzlich liegt die Laufleistung weit ueber der Akkugarantiegrenze von 160.000 km.
- **BMW 325i E30 TÜV Neu** (3502078738, 9990 €, youngtimer-alltag): E30 325i Coupe von 1984, das laut Anzeige komplett neu lackiert werden muss; solche Aufarbeitungsbasen liegen im Markt bei rund 9.000 bis 12.000 Euro. Bei 9.990 Euro kein Abstand zum Markt. Zusaetzlich gewerblicher Anbieter mit 101 Tage altem Konto ohne Bewertung.
- **Rolex Datejust 41 Diamond ( iced out )** (3501758137, 8990 €, uhren): 'Iced out' heisst nachtraeglich gesetzte Diamanten; solche Umbauten senken den Wiederverkaufswert deutlich, waehrend der Median aus 'Rolex Datejust Diamond 41' auch werkseitig besetzte Uhren enthaelt. Zusammen mit einer Verkaeuferbewertung von 0,23, reinem Versand und einer Dreizeilen-Beschreibung kein belegbarer Fund.
- **Mercedes W126 420SE** (3501866289, 5500 €, youngtimer-alltag): Eigene Pruefung: Ein W126 420 SE liegt in durchschnittlichem Zustand bei rund 4.800 Pfund (etwa 5.600 Euro). Verschlissene Ventilschaftdichtungen, defektes Schiebedach, beginnender Rost und 310.000 km machen 5.500 Euro zu einem korrekten Preis, nicht zu einem Fund. Das genannte Wertgutachten ueber 12.000 Euro ist eine Verkaeuferangabe ohne Marktbeleg.
- **BMW e36 320i Cabrio Klima** (3501970766, 4950 €, youngtimer-alltag): 250.600 km, stark verschlissene Vordersitze: Der Preis erklaert sich durch Laufleistung und Zustand. E36-Cabrios in dieser Laufleistungsklasse liegen im Markt bei 4.000 bis 6.000 Euro.
- **Mercedes-Benz 190E W201 TÜV neu H. Zulassung** (3501990495, 3700 €, youngtimer-alltag): Gewerbetext auf Privatprofil und Konto juenger als sechs Monate; ohne eigene Marktwertbestaetigung fuer den konkreten 190E-Ausstattungsstand nicht als Fund belegbar.
- **Simson S51 Neuaufbau 4-Gang KBA Papiere vorhanden** (3501571955, 1750 €, motorraeder): Ein professioneller S51-Neuaufbau kostet rund 4.000 Euro, funktionsfaehige Fahrzeuge 2.500 bis 3.000 Euro. 1.750 Euro fuer den beschriebenen Vollaufbau von einem 16 Tage alten Konto, verbunden mit dem Angebot 'Reservierung gegen Anzahlung', ist das Standardmuster des Vorkassebetrugs in einer der meistgefaelschten Kategorien.
- **Mercedes W124 200D** (3501819030, 3500 €, youngtimer-alltag): W124 200D mit 250.000 km ueber der Median-Referenz von Fahrzeugen ohne Laufleistungsangabe; kein eigener Marktwertnachweis gefuehrt, Abstand nicht belegbar.
- **Specialized Levo Turbo MTB Fully EBike** (3496627454, 1400 €, ebike-rad): Levo Turbo ohne Modelljahr und ohne Ausstattungsvariante; der Median aus 99 Anzeigen mischt Generationen von 2016 bis heute und Akkugroessen von 500 bis 700 Wh. Ohne Modelljahr kein belastbarer Vergleich.
- **GEFORCE RTX 5090** (3501993613, 2800 €, grafikkarten): Eine RTX 5090 kostet neu Anfang September 2026 im deutschen Handel 4.850 bis 5.000 Euro, die Preise sind allein im August um 6,6 Prozent gestiegen. Eine 'praktisch nagelneue' Karte mit OVP zu 2.800 Euro von einem Konto mit Bewertung 0,26 ist die klassische Betrugsform bei liquider Ware: exakte Modellangabe, keine Maengel, Versand.
- **E Bike - Cube Kathmandu Hybrid One 750 - (50 cm)** (3501305695, 900 €, ebike-rad): Der Akku lagerte ein Jahr und die Kapazitaet kann laut Verkaeufer auf 70 bis 80 Prozent gefallen sein; ein Bosch-750-Wh-Ersatzakku kostet 700 bis 800 Euro. Der Preis erklaert sich durch das Akkurisiko.
- **BMC URS ONE Gravelbike | Wie neu | Frische Inspektion** (3501828940, 2450 €, modellbau-sammler): BMC URS ONE von 07/2024, neu rund 3.500 Euro; zweijaehrige Gravelbikes liegen gebraucht bei 50 bis 60 Prozent davon, das p25 der Referenz liegt bei 1.949 Euro. 2.450 Euro sind eher ueber als unter Markt, der Median von 3.799 Euro mischt hoeherwertige URS-Varianten ein (Streuung 2,26).
- **HAIBIKE TREKKING 10** (3501279596, 1200 €, ebike-rad): Haibike Trekking 10 ohne Angabe der Motorgeneration und Akkugroesse; Median mischt Modelljahre. Verkaeuferbewertung 0,38. Kein eigener Marktwertnachweis moeglich.
- **Simson S51 Moped 4 Gang läuft Crossmoped** (3501761374, 1850 €, motorraeder): Ohne Zustands-, Papier- und Laufleistungsangaben kein eigener Marktwertnachweis moeglich.
- **Simson S51 4 Gang** (3501564920, 1950 €, motorraeder): Ohne Zustands-, Papier- und Laufleistungsangaben kein eigener Marktwertnachweis moeglich.
- **Simson S51 B** (3501630008, 2100 €, motorraeder): Ohne Zustands-, Papier- und Laufleistungsangaben kein eigener Marktwertnachweis moeglich.
- **Simson s51** (3501846390, 2000 €, motorraeder): Ohne Zustands-, Papier- und Laufleistungsangaben kein eigener Marktwertnachweis moeglich.
- **cube stereo hybrid** (3502091856, 1650 €, ebike-rad): Rad ohne Modelljahr und Ausstattungsvariante; der Median mischt Generationen und Akkugroessen, ein belastbarer Vergleich ist nicht moeglich.
- **Bosch Performance Line CX eBike Winora Yakun 12 Trecking Fahrrad** (3502013487, 1800 €, ebike-rad): Rad ohne Modelljahr und Ausstattungsvariante; der Median mischt Generationen und Akkugroessen, ein belastbarer Vergleich ist nicht moeglich.
- **Specialized Epic Comp Fully Mountainbike** (3501626835, 480 €, ebike-rad): Specialized Epic Comp mit 26-Zoll-Laufraedern, also ein Rad von etwa 2010; der Median aus 'Specialized Epic Comp' enthaelt ueberwiegend aktuelle 29-Zoll-Modelle. Zusaetzlich gebrochene Speiche. Phantomersparnis.
- **Simson s51** (3501896096, 2100 €, motorraeder): Simson S51 ohne Zustandsangaben und ohne Papierlage; Konto juenger als sechs Monate. Ohne eigene Wertbestaetigung kein Fund.
- **USM Haller Sideboard Lichtgrau** (3501946099, 550 €, design-sammeln): Der Titel sagt 'Sideboard', der Text beschreibt einen Rollcontainer. Gebrauchte USM-Haller-Rollcontainer liegen im Handel bei 390 bis 890 Euro, ein lichtgrauer bei 590 Euro. 550 Euro sind Marktpreis; der Median von 1.590 Euro stammt aus Sideboards, also einem anderen Produkt.
- **Trek Powerfly 4 E-MTB/ sehr wenig gefahren/ Bosch** (3502021109, 1500 €, ebike-rad): Trek Powerfly 4 ohne Modelljahr; das p25 der Referenz liegt bei 1.600 Euro, der Angebotspreis von 1.500 Euro damit nur knapp unter dem unteren Viertel des Vergleichsfelds. Kein 20-Prozent-Abstand.
- **E-Bike Gr. S / Specialized Vado SL 4.0** (3501389873, 1250 €, ebike-rad): Specialized Vado SL 4.0 ohne Modelljahr; Median mischt Generationen und die SL-Varianten mit 320-Wh-Akku. Kein belastbarer Vergleich.
- **Simson S51 N** (3501990279, 2200 €, motorraeder): Simson S51 N ohne Zustandsbeschreibung, Konto juenger als sechs Monate; kein eigener Marktwertnachweis.
- **Cube Touring Hybrid ONE** (3501295853, 799 €, ebike-rad): Cube Touring Hybrid ONE ohne Modelljahr und Akkugroesse; Gewerbetext auf Privatprofil. Kein belastbarer Vergleich.
- **E-Bike Bosch CX Motor Electra zahnriemenantrieb  Smartphone Grip** (3501353386, 1499 €, ebike-rad): E-Bike ohne Marken- und Modellangabe im Titel, Median aus gemischten Bosch-CX-Raedern. Kein belastbarer Vergleich.
- **Trek Slash 9 Mountainbike, RockShox Fahrwerk, SRAM Ausstattung** (3502054196, 1550 €, ebike-rad): Trek Slash 9 ohne Modelljahr; die Slash-9-Ausstattung reicht ueber zehn Modelljahre von Alu bis Carbon. Kein belastbarer Vergleich.
- **Trekking-E-Bike** (3501319399, 990 €, ebike-rad): 'Trekking-E-Bike' ohne Marke und Modell; ein Median dazu vergleicht nichts Bestimmtes.
- **Damenuhr  Tudor** (3501736596, 650 €, uhren): Traegt den Unkenntnis-Bonus, scheitert aber am Nachweis: Ein Rondawerk ist ein Schweizer Quarz-Zulieferwerk, das Tudor nicht verbaut, und ohne Referenznummer laesst sich das Modell nicht bestimmen. Streuung 2,4 bei nur 14 Anzeigen. Ich kann keinen belastbaren Marktwert bilden und schaetze keinen.
- **USM Haller Sideboard Beige** (2919925425, 950 €, design-sammeln): Gewerblicher Anbieter (PRO) mit Haendlerpreis; ein USM-Haller-Sideboard M mit zwei Klappen liegt gebraucht im Handel bei 900 bis 1.400 Euro. 950 Euro sind Marktpreis.
- **CUBE ATTAIN C:62 RACE** (3502007912, 1000 €, ebike-rad): Cube Attain C:62 Race ohne Modelljahr, Gewerbetext auf Privatprofil; kein belastbarer Vergleich.
- **USM Haller Highboard Weiß** (2919916758, 950 €, design-sammeln): Gewerblicher Anbieter (PRO); der Text beschreibt ein Sideboard mit zwei Klappen, nicht das im Titel genannte Highboard. Haendlerpreis auf Marktniveau.
- **Canyon Fully Mountainbike weiß Nerve AM Größe M** (3501909566, 390 €, ebike-rad): Canyon Nerve AM ohne Modelljahr, ein Rad aus den Jahren 2010 bis 2014; Median mischt neuere Fullys ein. Phantomersparnis.
- **Cube Reaction Hybrid smartsystem I neuwertig| kleine Personen** (3502026235, 1290 €, ebike-rad): Cube Reaction Hybrid ohne Modelljahr und Akkugroesse, Verkaeuferbewertung 0,38; kein belastbarer Vergleich.
- **CUBE Reaction Hybrid Pro Allroad E-Bike Bosch CX Trapeze** (3502065644, 1299 €, ebike-rad): Cube Reaction Hybrid Pro Allroad ohne Modelljahr; Median mischt 500-, 625- und 750-Wh-Varianten. Kein belastbarer Vergleich.
- **Cube Stereo 120 Mountainbike Fully - fast neuwertig** (3502072704, 1300 €, ebike-rad): Cube Stereo 120 ohne Modelljahr und Ausstattungslinie; Median mischt Race, Pro und SLT. Kein belastbarer Vergleich.
- **USM Haller Highboard, Sideboard, Aktenschrank, schwarz** (3501842632, 1000 €, design-sammeln): USM Haller ohne Angabe von Groesse und Elementzahl; ohne die Konfiguration ist kein Vergleich moeglich, sie bestimmt den Wert vollstaendig.
- **E bike 29 zoll Bosch Performance cx  625 Akku  E Mountainbike** (3501362968, 1250 €, ebike-rad): E-Bike ohne Marke im Titel; Median vergleicht nichts Bestimmtes.
- **Bulls Street Flyer Damen Trekkingrad 28 Zoll** (3501575187, 380 €, ebike-rad): Bulls Street Flyer, ein Trekkingrad ohne Motor, gegen einen Median aus neun Anzeigen mit hohem Neupreisanteil. Ohne Modelljahr kein belastbarer Vergleich.
- **Dachklimaanlage Truma Aventa Compact** (3501779285, 500 €, camper-marine): Nur acht Vergleichsanzeigen, und die Anzeige laesst offen, ob der Luftverteiler und der Dachadapter mitgeliefert werden; genau diese Teile machen den Wert einer ausgebauten Dachklimaanlage aus. Kein belastbarer Marktwert.
- **Gravelbike Cube Nuroad S** (3502081793, 740 €, ebike-rad): Cube Nuroad S ohne Modelljahr; kein belastbarer Vergleich.
- **Wie neu - Cube Cross Pro Damenrad** (3501704752, 549 €, ebike-rad): Cube Cross Pro ohne Modelljahr; kein belastbarer Vergleich.
- **USM Haller Lowboard Weiß inkl.MwSt** (2919907460, 770 €, design-sammeln): Gewerblicher Anbieter (PRO) mit Haendlerpreis auf Marktniveau.
- **Hilti TE 1000-AVR Abbruchhammer im Koffer** (3502086226, 750 €, werkzeug-maschinen): Nur acht Vergleichsanzeigen (Streuung 1,65), und bei einem Profi-Abbruchhammer bestimmen Betriebsstunden und Serviceintervall den Wert, zu denen die Anzeige nichts sagt. Verkaeuferbewertung 0,72, reiner Versand. Kein belastbarer Abstand.
- **Haibike ebike sduro trekking 28 Zoll** (3501811770, 500 €, ebike-rad): Haibike SDURO ohne Modelljahr und Akkugroesse; kein belastbarer Vergleich.
- **TV Board USM Haller** (3502046577, 935 €, design-sammeln): USM Haller TV Board ohne Elementkonfiguration; kein belastbarer Vergleich.
- **Rennrad Cube  Axial** (3456135031, 400 €, ebike-rad): Cube Axial ohne Modelljahr; kein belastbarer Vergleich.
- **Iphone 17 256GB** (3502098225, 600 €, apple-mobil): Ein fabrikneues, ungeoeffnetes iPhone 17 mit 256 GB zu 600 Euro Festpreis liegt rund 40 Prozent unter dem Neupreis. Bei einem Geraet, das keinen Zustandsabschlag hat, gibt es fuer diesen Abstand keinen ehrlichen Grund; zusammen mit Bewertung 0,72 ist das die typische Form fuer Betrug oder Hehlerware.
- **Cube Nuroad Gravel Bike blau mit Gepäckträger** (3501382616, 950 €, ebike-rad): Cube Nuroad ohne Modelljahr; kein belastbarer Vergleich.
- **Birdy Riese & Müller Nexus 8 Gang Nabenschaltung grau** (3502018517, 950 €, ebike-rad): Birdy von Riese & Mueller ohne Baujahr und Rahmengeneration bei nur acht Vergleichsanzeigen; kein belastbarer Vergleich.
- **MacBook Air 13,6" M4 – 16GB, 256GB SSD, Mitternacht, 9 Zyklen** (3502081698, 470 €, macbook): Ein vier Monate altes MacBook Air M4 mit Rechnung und AppleCare zu 470 Euro liegt rund 50 Prozent unter dem Gebrauchtmarkt. Fuer diesen Abstand nennt die Anzeige keinen Grund; Bewertung 0,60, ausschliesslich Versand. Nicht ueberzeugend.
- **Apple MacBook Air silber** (3501674286, 400 €, macbook): Traegt den Unkenntnis-Bonus, doch die Anzeige nennt weder Baujahr noch Chip noch Speicher, und der Median aus 'Apple MacBook Air' reicht vom 2015er i5 bis zum M4. Ohne Modellbestimmung kein Marktwert und damit kein Fund; ich schaetze keinen.
- **canyon Dirt bike Stitched** (3501935914, 450 €, ebike-rad): Canyon Stitched ohne Modelljahr; kein belastbarer Vergleich.
- **MacBook Pro 16" (2021) M1 Pro, 16GB RAM, 512GB SSD ** (3501346472, 500 €, macbook): Das Display hat einen Pixelfehler in Form zweier durchgehender Streifen. Ein M1 Pro 16 Zoll mit defektem Display liegt bei rund 500 Euro; der Preis erklaert sich selbst.
- **Shimano Dura Ace Di2 11 fach Gruppe - Schaltung gebraucht** (3501917939, 490 €, ebike-rad): Streuung 2,3 bei einem p25 von 499 Euro: Das Vergleichsfeld mischt Einzelteile und komplette Gruppen, mechanische und hydraulische Varianten. Der Angebotspreis liegt praktisch auf dem p25.
- **Rennrad Cube** (3501993022, 500 €, ebike-rad): 'Rennrad Cube' ohne Modell und Baujahr, ein Bild; kein belastbarer Vergleich.
- **Cube Nuroad Pro  Gravel  Bike** (3501324295, 750 €, ebike-rad): Cube Nuroad Pro ohne Modelljahr, ein Bild, Bewertung 0,61; kein belastbarer Vergleich.
- **MACBOOK AIR - 2 TB Speicher** (3501555048, 550 €, macbook): 'MACBOOK AIR - 2 TB Speicher' ohne Chip und Baujahr, Konto juenger als sechs Monate, Bewertung 0,20. Kein Modell bestimmbar, kein Marktwert.
- **Trekkingrad Pegasus für Damen** (3501855942, 455 €, ebike-rad): Pegasus Trekkingrad ohne Modell und Baujahr, Gewerbetext auf Privatprofil; kein belastbarer Vergleich.
- **Stehleuchte "Panthella" von Louis Poulsen- Designer Verner Panton** (3501817310, 400 €, design-sammeln): Die Anzeige nennt die Panthella-Variante nicht (160, 250, 320, 400 oder Floor), und die Preise reichen je nach Variante von 509 Euro Neupreis bis weit darueber. Bei nur zehn Vergleichsanzeigen und dem hohen Replikaanteil bei Acryl-Panthellas kein belastbarer Marktwert.
- **Meissen Kaffee Porzellan MOKKASERVICE Blumen Mokka für 6 Personen** (3501751858, 519 €, design-sammeln): Streuung 2,49 bei 19 Anzeigen, Meissen-Service ohne Angabe von Dekornummer, Teilezahl und Schleifstrichen; bei Porzellan bestimmen genau diese Angaben den Wert.
- **Cube AMS 100 Mountainbike Fully** (3501889398, 300 €, ebike-rad): Cube AMS 100 ohne Modelljahr, ein Bild; kein belastbarer Vergleich.
- **Cube Reaction TM Mountainbike, Rahmengröße M, 29 Zoll** (3501623116, 450 €, ebike-rad): Cube Reaction TM ohne Modelljahr; kein belastbarer Vergleich.
- **Victoria 8.8 e Trekking** (3501898832, 500 €, ebike-rad): Victoria 8.8 e ohne Modelljahr und Akkugroesse bei 16 Vergleichsanzeigen; kein belastbarer Vergleich.
- **Apple MacBook Pro 14” (2021) – gebraucht** (3501715843, 500 €, macbook): Konto juenger als drei Tage bei einem liquiden Apple-Geraet; ohne Historie und ohne konkrete Zustandsangaben nicht ueberzeugend.
- **MacBook Air** (3501784526, 500 €, macbook): 'MacBook Air' ohne Chip und Baujahr, Gewerbetext auf Privatprofil; kein Modell bestimmbar.
- **Apple MacBook Air 13, 1,6 GHz Dual-Core i5** (3501780463, 320 €, macbook): MacBook Air mit 1,6-GHz-Dual-Core-i5, also Baujahr 2018/2019 mit ausgelaufenem macOS-Support; 320 Euro sind fuer dieses Modell Marktpreis. Streuung 2,25.
- **Steam Deck 512 GB** (3501950470, 300 €, konsolen-sweep): Der Median aus 'Steam Deck 512 GB' mischt LCD- und OLED-Modelle. Das angebotene Geraet ist die LCD-Version von 2022, deren Gebrauchtmarkt bei 280 bis 350 Euro liegt; zudem fehlt das Netzteil. 300 Euro sind Marktpreis.
- **iPhone 16 Pro** (3502060016, 450 €, apple-mobil): Riss im Display oben links und Akkukapazitaet 83 Prozent: Der Preis erklaert sich durch den Schaden.
- **Canyon Endurace AL XXL** (3502030207, 650 €, ebike-rad): Canyon Endurace AL ohne Modelljahr und Ausstattungsstufe; kein belastbarer Vergleich.
- **Kalkhoff Endeavour Trekking Herrenfahrrad 28“ Zoll Neuwertig !** (3501912719, 330 €, ebike-rad): Kalkhoff Endeavour ohne Modelljahr bei elf Vergleichsanzeigen; kein belastbarer Vergleich.
- **Apple iPhone 16 Pro Max 256 GB Natural Titanium sehr gut** (3502096730, 475 €, apple-mobil): 480 Ladezyklen bei angeblich 'keinerlei sichtbaren Kratzern', Konto erst seit April 2026, ausschliesslich Versand, 38 Prozent unter dem Median: Die Kombination passt auf das Betrugsmuster bei liquider Apple-Ware, nicht auf einen ehrlichen Verkauf.
- **MacBook Air 13,3** (3501862549, 400 €, macbook): 'MacBook Air 13,3' ohne Chip und Baujahr; kein Modell bestimmbar.
- **iPhone 15 weiß** (3501940994, 260 €, apple-mobil): Verkaeuferbewertung 0,10 bei einem liquiden Apple-Geraet; kein vertrauenswuerdiges Angebot.
- **DJI Mini 3 Pro mit DJI RC Controller im Case** (3502036695, 280 €, optik-drohnen): DJI Mini 3 Pro zu 280 Euro gegen einen Median von 545 Euro, aber die Anzeige nennt weder Akkuzahl noch Flugstunden, und ein gleichartiges Set wurde am 2. September bereits gemeldet (Anzeige 3501800151). Bewertung 0,75.
- **Neuwertig Steam Deck OLED 512GB mit Speicherkarte ** (3501995034, 360 €, konsolen-sweep): Steam Deck OLED 512 GB neu bei 569 Euro, gebraucht neuwertig rund 450 Euro; 360 Euro liegen damit nur etwa 20 Prozent darunter, bei einem Konto ohne jede Bewertung und reinem Versand. Zu knapp fuer einen Fund.
- **MacBook Pro 16 Zoll 2019 i9 – 16 GB RAM – 1 TB SSD** (3501759175, 349 €, macbook): MacBook Pro 16 Zoll von 2019 mit i9: Intel-Modell mit auslaufendem macOS-Support und bekanntem Hitzeproblem; 349 Euro sind fuer dieses Geraet Marktpreis.
- **Vitra Aluminium Chair EA 108 – Design-Bürostuhl, Hopsak, Original** (3501734506, 400 €, design-sammeln): Vitra EA 108 ohne Angabe zum Bezugszustand, doppelt inseriert (siehe 3501713072); der Abstand von 250 Euro zum Median liegt unter 40 Prozent und ohne Zustandsangaben nicht belegbar.
- **Vitra Aluminium Chair EA 108 – Design-Bürostuhl, Hopsak, Original** (3501713072, 400 €, design-sammeln): Doppelinserat zu 3501734506, gleiche Beurteilung: ohne Zustandsangaben kein belegbarer Abstand.
- **Apple MacBook Air in Schwarz** (3501999193, 550 €, macbook): 'MacBook Air in Schwarz' ohne Chip und Baujahr; kein Modell bestimmbar.
- **Apple MacBook silber** (3502053009, 350 €, macbook): 'Apple MacBook silber' ohne Modell, Chip und Baujahr; kein Modell bestimmbar.
- **iPhone 16 128GB Schwarz** (3502061594, 379 €, apple-mobil): iPhone 16 128 GB zu 379 Euro gegen Median 620 Euro, aber die Anzeige nennt keinen Akkuzustand und keine Zyklen; ohne diese Angaben ist der Abstand nicht belegbar.
- **Apple iPhone 15 sehr gut erhalten mit Originalzubehör** (3501919447, 265 €, apple-mobil): iPhone 15 zu 265 Euro; Anzeige ohne Akkuzustand, Bewertung 0,75. Abstand nicht belegbar.
- **Simson Schwalbe Blechkleid Originallack Beulenfrei** (3501628612, 500 €, motorraeder): Nur das Blechkleid, kein vollstaendiges Fahrzeug; der Median aus 'Simson Schwalbe' vergleicht ganze Mopeds. Phantomersparnis.
- **Trek Mountainbike Fully 26 Zoll** (3501541668, 300 €, ebike-rad): Rad ohne Modelljahr und Ausstattungsvariante; der Median mischt Generationen und Akkugroessen, ein belastbarer Vergleich ist nicht moeglich.
- **Cube Aerium Pro Racing Series** (3451224151, 380 €, ebike-rad): Rad ohne Modelljahr und Ausstattungsvariante; der Median mischt Generationen und Akkugroessen, ein belastbarer Vergleich ist nicht moeglich.
- **Apple iPhone 15 Pro, 2 Jahre alt** (3501363769, 350 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 16 Pro 128 GB** (3501384568, 450 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **MacBook Pro 13” mit M1 Chip.** (3501868502, 350 €, macbook): MacBook ohne eindeutige Modell-, Chip- oder Baujahrangabe; ohne Modellbestimmung kein Marktwert.
- **Specialized Rockhopper Mountainbike** (3502001858, 300 €, ebike-rad): Rad ohne Modelljahr und Ausstattungsvariante; der Median mischt Generationen und Akkugroessen, ein belastbarer Vergleich ist nicht moeglich.
- **Fahrrad Cube Acid 29 Zoll** (3502096400, 350 €, ebike-rad): Rad ohne Modelljahr und Ausstattungsvariante; der Median mischt Generationen und Akkugroessen, ein belastbarer Vergleich ist nicht moeglich.
- **Apple iPhone 14** (3501286082, 180 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 15 128gb 87%** (3501326140, 340 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **Stuhl Vitra Wire** (3501365122, 210 €, design-sammeln): Designstueck ohne Angabe von Ausfuehrung, Groesse oder Konfiguration; diese bestimmen den Wert vollstaendig, ein belastbarer Vergleich ist nicht moeglich.
- **Gebrauchtes iPhone 14** (3502053057, 150 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **Handy iPhone 14** (3502102394, 170 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **Vitra Eames Plastic Chair DsX weiß** (3156550904, 169 €, design-sammeln): Designstueck ohne Angabe von Ausfuehrung, Groesse oder Konfiguration; diese bestimmen den Wert vollstaendig, ein belastbarer Vergleich ist nicht moeglich.
- **iPhone 15 Pro Max 256 GB** (3501304211, 420 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **Apple iPhone 13 256 GB Mitternachtsblau! Guter Zustand!** (3501312749, 150 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **Iphone 15 Pro Titan Schwarz** (3502036986, 399 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 15 128GB** (3501280690, 280 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **Canyon Mountainbike Fully 26 Zoll** (3502042197, 330 €, ebike-rad): Rad ohne Modelljahr und Ausstattungsvariante; der Median mischt Generationen und Akkugroessen, ein belastbarer Vergleich ist nicht moeglich.
- **iphone 14. VB** (3501345388, 210 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 15 128GB** (3502062686, 250 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 15 schwarz** (3502040310, 295 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **Apple iPhone 15 Pro 128 GB in Schwarz** (3501310068, 350 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 14 Pro Max 128 GB Schwarz – Rahmen gebrochen** (3502029374, 299 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 14. 128 GB** (3502097981, 200 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 14 in Weiß mit 256GB** (3502101540, 250 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **Apple iPhone 15 schwarz** (3502017859, 300 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **anhänger hp 300** (3502041897, 150 €, messtechnik): Anhaenger ohne Angabe von Baujahr, TUEV und Aufbau; kein belastbarer Vergleich.
- **Handy iPhone 14** (3502019355, 215 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 13 Pro** (3502006340, 200 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 14 Plus** (3501306656, 200 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 14 Pro Max** (3501974792, 300 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 14 Pro Max** (3502049641, 300 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iphone 13 256 GB** (3501291593, 200 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **Apple iPhone 14 Pro in Dunkellila** (3502085875, 275 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **PKW Anhänger HP 500** (3501337143, 250 €, messtechnik): Anhaenger ohne Angabe von Baujahr, TUEV und Aufbau; kein belastbarer Vergleich.
- **iPhone 13 grün** (3502007587, 160 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **Drohne DJI Mavic Pro Platinum Fly More Combo** (3502018815, 250 €, optik-drohnen): Ohne Angabe von Flugstunden und Akkuzustand kein belastbarer Abstand.
- **iPhone 13 Pro 128 GB gebraucht** (3502067667, 199 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **Fritz Hansen Arne Jacobsen 3107 stuhl** (3400563922, 169 €, design-sammeln): Designstueck ohne Angabe von Ausfuehrung, Groesse oder Konfiguration; diese bestimmen den Wert vollstaendig, ein belastbarer Vergleich ist nicht moeglich.
- **iPhone 14. 128GB** (3502096063, 230 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 14 Plus** (3501391330, 225 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 12 Pro 128GB** (3502097521, 150 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **iPhone 13 in dunkelgrün** (3501329852, 170 €, apple-mobil): Gebrauchtes iPhone ohne belegten Akkuzustand oder Zyklenzahl; der Kleinanzeigen-Median besteht aus Angebotspreisen und mischt Speichergroessen, ein eigener Marktwertnachweis mit 20 Prozent Abstand war damit nicht zu fuehren.
- **Fatbike Cube Nutrail Race, Top Zustand** (3501852139, 600 €, ebike-rad): Median nicht belastbar (Streuung 2.84, 12 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Specialized Stumpjumper Mountainbike, Gr. L, Shimano XTR** (3501867977, 500 €, ebike-rad): Median nicht belastbar (Streuung 3.22, 99 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **CUBE Stereo 120 SL 29 - FOX Factory Kashima - Shimano XT** (3502057877, 1250 €, ebike-rad): Median nicht belastbar (Streuung 2.55, 11 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Fahrrad  Giant City Tourer/Trekking** (3501807360, 350 €, ebike-rad): Median nicht belastbar (Streuung 7.02, 19 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Fender Precision Bass Japan Lefthand Linkshänder** (3501700954, 1100 €, musikinstrumente): Median nicht belastbar (Streuung 3.54, 39 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Canyon Pathlite – Größe S** (3501734745, 400 €, ebike-rad): Median nicht belastbar (Streuung 3.25, 36 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Specialized Enduro Fully Mountainbike – Fox Float R – RockShox** (3501939139, 329 €, ebike-rad): Median nicht belastbar (Streuung 3.0, 75 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Simson s51 komplett Motor** (3502068796, 1050 €, motorraeder): Median nicht belastbar (Streuung 4.09, 87 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Specialized Fully Mountainbike** (3411236718, 550 €, ebike-rad): Median nicht belastbar (Streuung 4.55, 62 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Matra Drehbank** (3501843652, 1150 €, werkzeug-maschinen): Median nicht belastbar (Streuung 5.54, 11 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Porzellan-Sammlung MEISSEN uvm** (3501798704, 300 €, design-sammeln): Median nicht belastbar (Streuung 7.6, 12 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Simson Schwalbe KR51-1 60km/h DDR Modell Nr.:A2724 Weinböhla** (3475643497, 1190 €, motorraeder): Median nicht belastbar (Streuung 2.52, 9 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Simson Schwalbe KR51-1 60km/h DDR Modell Nr.:A2727 Weinböhla** (3475636165, 1190 €, motorraeder): Median nicht belastbar (Streuung 2.52, 9 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Meissen Porzellan Indische Malerei Rot Service Blumen 1. Wahl** (3501631192, 300 €, design-sammeln): Median nicht belastbar (Streuung 4.27, 12 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Sessel Knoll Leder Bauhaus Mid Century Design Clubsessel Lounge** (3501533310, 700 €, design-sammeln): Median nicht belastbar (Streuung 2.87, 99 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Original Eames Aluminium Group Chair /Vitra / schwarz/ Bürostuhl** (3473730977, 200 €, design-sammeln): Median nicht belastbar (Streuung 3.26, 11 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Mountainbike Specialized Stumpjumper FSR Comp** (3502005981, 1100 €, ebike-rad): Median nicht belastbar (Streuung 3.41, 99 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Knoll Bertoia. Diamond Sessel** (3501914831, 450 €, design-sammeln): Median nicht belastbar (Streuung 2.66, 54 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Cube Rennrad RH60** (3501941322, 450 €, ebike-rad): Median nicht belastbar (Streuung 2.54, 11 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Herman Miller Eames Side Hoppsack Schale | gelb/senf** (3502102275, 250 €, design-sammeln): Median nicht belastbar (Streuung 3.19, 99 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Apple MacBook Air 13 Zoll, 1,6 GHz i5, Spacegrau** (3501943928, 300 €, macbook): Median nicht belastbar (Streuung 2.81, 14 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Cube Race One 29 – gepflegt, leichte Gebrauchsspuren** (3501830738, 400 €, ebike-rad): Median nicht belastbar (Streuung 3.58, 69 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **macbook pro** (3502019152, 620 €, macbook): Median nicht belastbar (Streuung 2.88, 91 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Vitra Eames Stuhl Fiberglas Orange** (3502047590, 320 €, design-sammeln): Median nicht belastbar (Streuung 3.98, 96 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Fritz Hansen / Arne Jacobsen DROP Sitzgruppe** (3501329188, 244 €, design-sammeln): Median nicht belastbar (Streuung 4.6, 99 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Diamant Trekkingrad** (3502077921, 300 €, ebike-rad): Median nicht belastbar (Streuung 3.33, 99 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Trekkingrad/ Fahrrad Giant ThoughRoad SLR EX** (3501323230, 300 €, ebike-rad): Median nicht belastbar (Streuung 2.85, 58 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Cube Herrenrad 28 Zoll Rahmen XL** (3501703819, 350 €, ebike-rad): Median nicht belastbar (Streuung 3.33, 41 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Vitra Bürostuhl** (3501575120, 200 €, design-sammeln): Median nicht belastbar (Streuung 4.8, 94 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **"Cube" Trekking-Fahrrad 28"** (3501382735, 325 €, ebike-rad): Median nicht belastbar (Streuung 3.56, 23 Anzeigen) – nach prompt.md wie nicht vorhanden behandelt; ein eigener Referenzwert liess sich aus der Anzeige nicht belegen.
- **Panasonic Leica DG Summilux 15mm F1.7 ASPH H-X015E-K MFT** (3501402824, 350 €, kameras-leica): Kein Kleinanzeigen-Median vorhanden. Das 2018 gekaufte 15-mm-Summilux liegt gebraucht ueblicherweise bei 280 bis 350 Euro, und der Originaldeckel fehlt; 350 Euro sind damit Marktpreis, kein Fund. Ich habe fuer dieses Objektiv keine zwei belastbaren Vergleichsangebote gefunden und schaetze keinen Abstand.
- **Panasonic Leica DG Summilux 9mm F1.7 ASPH H-X09 Micro Four Thirds** (3501383345, 350 €, kameras-leica): Kein Kleinanzeigen-Median vorhanden. Eigene Pruefung: Das Objektiv kostet neu ab 411,99 Euro und gebraucht im Zustand 'near mint' 375 bis 410 Euro. 350 Euro liegen unter 20 Prozent darunter.


# Lauf 2026-09-03, abends

- **Ausgefuehrt:** 3. September 2026, 19:15 Uhr (MESZ)
- **Datenstand `candidates.json`:** 2026-09-03T18:58:12+02:00 (17 Minuten alt, weit innerhalb der Vier-Stunden-Grenze)
- **Zeitraum des Sammellaufs:** 2026-09-03T12:28:22+02:00 bis 2026-09-03T17:28:22+02:00
- **Gesichtete Anzeigen:** 173.775
- **Kandidaten in der Warteschlange:** 169
- **Bereits in `deal_log.csv`:** 0
- **Davon heute frueh schon geprueft und verworfen:** 89 (Begruendungen stehen im Morgenprotokoll oben, sie werden hier nicht wiederholt)
- **Neu seit dem Morgenlauf:** 80
- **Gemeldet:** 6

Vorrang nach absoluter Ersparnis und Liquiditaet: zuerst Uhren, Apple-Geraete,
Drohnen, Grafikkarten und die Fahrzeuge mit dem groessten Abstand, danach der
Rest. 21 Kandidaten wurden einzeln per Websuche gegengeprueft.

## Gemeldete Funde

| Titel | Preis | Bestaetigter Marktwert | Abstand | Kategorie |
|---|---|---|---|---|
| [Rolex Explorer II 226570](https://www.kleinanzeigen.de/s-anzeige/rolex-explorer-ii-226570/3502351037-157-4763) | 6.900 € | 10.990–11.950 € bei deutschen Haendlern, WatchCharts-Marktwert rund 11.075 USD; ohne Papiere rund 9.000–9.500 € | rund 26 % | uhren |
| [Cassina LC2 Sessel, schwarzes Leder](https://www.kleinanzeigen.de/s-anzeige/cassina-lc2-sessel-le-corbusier-schwarz-leder/3502474300-93-1158) | 1.500 € | 3.290–4.250 € im Gebrauchthandel (Sebworld, blucom 3.998 €), KA-Median 2.500 € (n=25) | ueber 40 % | design-sammeln |
| [DJI Mini 5 Pro Fly More Combo mit RC 2](https://www.kleinanzeigen.de/s-anzeige/dji-mini-5-pro-fly-more-combo-mit-rc-2/3502617752-168-1900) | 490 € | 657,90 € gebraucht (Galaxus), neu ab 899 € (Geizhals), UVP 1.129 € mit RC 2 | 25 % zum Gebraucht-, 45 % zum Neupreis | optik-drohnen |
| [Steam Deck OLED 512 GB](https://www.kleinanzeigen.de/s-anzeige/steam-deck-oled-512gb/3502484049-279-1684) | 250 € | 459 € zertifiziert generalueberholt bei Valve, 779 € neu seit Mai 2026 | rund 46 % | konsolen-sweep |
| [DJI Mini 4 Pro Fly More Combo, RC 2, 4 Akkus](https://www.kleinanzeigen.de/s-anzeige/dji-mini-4-pro-fly-more-combo-mit-dji-rc-2-und-4-ak/3502572387-168-2632) | 340 € | 894–929 USD gebraucht (MPB), UVP 1.129 € | rund 60 % | optik-drohnen |
| [Steam Deck OLED 1 TB](https://www.kleinanzeigen.de/s-anzeige/steam-deck-oled-1tb/3502582007-279-4240) | 350 € | 919 € neu seit Mai 2026 (vorher 679 €) | rund 62 % | konsolen-sweep |

## Nebenbefund: die Speicherkrise hat die Konsolen-Referenz verschoben

Valve hat die Steam-Deck-OLED-Preise am 27. Mai 2026 wegen der Speicherkrise
angehoben, von 569 auf 779 Euro (512 GB) und von 679 auf 919 Euro (1 TB); das
LCD-Modell gibt es nur noch generalueberholt ab 299 Euro. Der
Kleinanzeigen-Median liegt mit 600 bis 700 Euro noch auf dem alten Niveau und
unterschaetzt den heutigen Wiederbeschaffungswert damit deutlich. Fuer beide
gemeldeten Steam Decks wurde deshalb nicht der Median, sondern der aktuelle
Valve-Preis als Referenz gesetzt. Derselbe Effekt trug heute frueh schon die
Verwerfung der RTX 5090: Grafikkarten und Handhelds sind 2026 teurer geworden,
nicht billiger, und ein Angebot weit unter Median ist in diesen Kategorien
eher ein Betrugs- als ein Schnaeppchensignal.

## Nebenbefund: 89 der 169 Kandidaten waren heute frueh schon abgelehnt

Die Warteschlange sammelt 24 Stunden lang an und leert sich nur ueber
`deal_log.csv`, in das ausschliesslich gemeldete Funde eintragen werden.
Verworfene Kandidaten laufen deshalb beim Abendlauf ein zweites Mal durch und
werden ein zweites Mal geprueft. Beim heutigen Lauf betraf das mehr als die
Haelfte der Liste. Ein Ablage-Vermerk fuer verworfene IDs mit Gueltigkeit bis
zum Ende des 24-Stunden-Fensters wuerde die Doppelarbeit sparen; das ist eine
Aenderung an Stufe 1, nicht etwas, das diese Routine im Lauf entscheiden sollte.

## Verworfene Kandidaten (163)

### Heute frueh bereits geprueft (89)

Diese Anzeigen standen schon in der Morgenliste und sind dort einzeln
begruendet. Es hat sich an Preis, Text und Verkaeuferprofil nichts geaendert,
die Verwerfung bleibt bestehen.

### Neu seit dem Morgenlauf (74)

- **Tesla Model S 85** (3502594050, 12950 €, tesla): 319.486 km bei einem Fahrzeug von 2014 und SOH 86 Prozent. Die Laufleistung liegt beim Doppelten der Akkugarantiegrenze von 160.000 km und erklaert den Preis vollstaendig; der Median aus 19 Model-S-Anzeigen enthaelt keine Laufleistungskorrektur. Zusaetzlich gewerblicher Anbieter mit 83 Tage altem Konto ohne Bewertung.
- **Rolex Datejust 41mm 126300 Full Set ungetragen** (3502409586, 9999 €, uhren): Eigene Pruefung: Auf Chrono24 liegen 126300 in Stahl bei 8.900 bis 11.075 Euro, ein neues Modell von 2026 beim Trusted Seller bei 10.700 Euro. 9.999 Euro sind damit Marktpreis und keine 20 Prozent Abstand. Der Kleinanzeigen-Median von 15.450 Euro besteht aus Angebotspreisen und ueberzeichnet den Markt um rund die Haelfte.
- **Golf 2 GTI H-Kennzeichen** (3502502896, 6500 €, youngtimer-alltag): Der Titel sagt GTI, der Beschreibungstext des Verkaeufers sagt "Golf zwei GT". GT und GTI trennen im Markt mehrere tausend Euro; solange nicht geklaert ist, welches Modell verkauft wird, ist der Vergleich wertlos. Zusaetzlich 240.000 km und ein Konto juenger als sechs Monate.
- **Rolex Datejust 41mm Gruen Neu Fullset** (3502356936, 10300 €, uhren): Gruenes Zifferblatt in der Datejust 41 liegt bei rund 12.000 bis 13.000 Euro, der Abstand betraegt damit keine 20 Prozent. Verkaeuferkonto 23 Tage alt, ohne Bewertung, bei einer ungetragenen Uhr im fuenfstelligen Bereich: das Standardmuster des Vorkassebetrugs.
- **Mercedes Benz S-Klasse Bundeswehr w126** (3502151806, 7200 €, youngtimer-alltag): 260 SE von 1986 mit 236.241 km und beschaedigtem Fahrersitz. W126 dieser Motorisierung und Laufleistung liegen im Markt bei 6.000 bis 9.000 Euro, 7.200 Euro VB sind Marktpreis; das p25 der Referenz liegt bei 8.500 Euro und der Median mischt 500er und Coupes ein.
- **Rolex datejust 41** (3502558741, 8900 €, uhren): Baujahr September 2011 bei einer als "Datejust 41" bezeichneten Uhr heisst Datejust II 116334, ein anderes Modell als die 126300-Referenz des Medians. Verkaeuferbewertung 0,22, dreizeilige Beschreibung, nur Versand. Kein belegbarer Fund.
- **Weiler Drehmaschine defekt** (3502585043, 1500 €, werkzeug-maschinen): Vorschuebe defekt, ausdruecklich als Teilespender angeboten. Der Preis erklaert sich selbst; die Referenz ist mit Streuung 6,8 ohnehin nicht belastbar.
- **Mercedes W124 230E Automatik Oldtimer** (3502393508, 4700 €, youngtimer-alltag): W124 230 E von 1988 mit 171.000 km. Classic-analytics fuehrt diese Baureihe im Zustand 3 bei rund 4.700 bis 5.500 Euro; der Preis ist korrekt und nicht zu niedrig. Der Median aus acht Anzeigen enthaelt Zustand-2-Fahrzeuge.
- **Mercedes 300 D W124 H-Zulassung** (3502393527, 5900 €, youngtimer-alltag): 504.000 km und umfangreiche Schweissarbeiten am Fahrzeug. Die Laufleistung erklaert den Preis. Zusaetzlich Verkaeuferkonto sieben Tage alt.
- **Mercedes Benz W124 230 E** (3502582648, 2900 €, youngtimer-alltag): Der Verkaeufer schreibt selbst "Auto braucht Zeit und Geld investieren", Motor laeuft unruhig, Batterie leer, Kabelbaum zu pruefen. Korrekt bepreistes Projektfahrzeug.
- **Volvo 850 T5** (3502455994, 4999 €, youngtimer-alltag): Rund 400.000 km. Der Preis erklaert sich durch die Laufleistung; die Referenz ist mit Streuung 3,12 nicht belastbar und die Anzeige steht ausserdem in der Rubrik Ersatzteile.
- **Suzuki GSX-R 750 W** (3502616287, 2000 €, motorraeder): Referenz mit Streuung 2,8 nicht belastbar. Eine GSX-R 750 W von 1994 mit 56.000 km liegt im Markt bei 2.000 bis 3.500 Euro; ohne engeren Vergleich ist kein 20-Prozent-Abstand belegbar.
- **Tudor prince date** (3502115678, 1300 €, uhren): Eigene Pruefung: Die Ref. 79410P liegt auf Chrono24.de bei 1.479 bis 1.911 Euro, das sind Haendlerpreise mit Gewaehr. Die Uhr hat keine Papiere und der Verkaeufer schreibt selbst, dass der Revisionsstand unbekannt ist und "deswegen der niedrige Preis". Der Preis erklaert sich damit selbst. Der Median von 2.990 Euro mischt Prince-Date-Chronographen ein, die ein anderes Produkt sind.
- **Pegasus Trekking E-Bike** (3502148575, 600 €, ebike-rad): Pegasus Premio E10 Modelljahr 2015 mit dem originalen Bosch Powerpack 400. Ein elf Jahre alter Akku ist der wertbestimmende Teil und erklaert den Preis; der Median von 2.149 Euro stammt aus aktuellen Trekking-Pedelecs.
- **Rennrad BMC Roadmachine 01 Four Force AXS** (3502534579, 2350 €, modellbau-sammler): Kein Modelljahr genannt. Die einzige belastbare Gebrauchtreferenz, die ich finden konnte, ist eine hoeher ausgestattete Roadmachine 01 ONE von 2023, die auf buycycle fuer 2.700 Euro verkauft wurde. Damit liegt der Angebotspreis zu nah am belegbaren Gebrauchtniveau; der KA-Median von 3.849 Euro mischt Modelljahre und Ausstattungsstufen.
- **Riese & Mueller Swing City E-Bike** (3502156305, 1500 €, ebike-rad): Kein Modelljahr, Konto juenger als sechs Monate. Der Median mischt Generationen; kein belastbarer Vergleich.
- **Cube Stereo 140 HPC Carbon Fully** (3502135324, 1250 €, ebike-rad): Kein Modelljahr. Das Stereo 140 HPC lief ueber zehn Modelljahre mit stark unterschiedlichen Fahrwerken; der Median vergleicht nichts Bestimmtes.
- **TUDOR Black Bay 41mm 79230N Fullset** (3502375555, 2222 €, uhren): Eigene Pruefung: Die 79230N liegt gebraucht im Full Set bei 2.421 bis 4.444 USD, das guenstigste Angebot liegt damit unter dem Angebotspreis. Zieht man den ueblichen Privatverkaufsabschlag von den Haendlerpreisen ab, bleibt kein 20-Prozent-Abstand. Zusaetzlich verlangt der Verkaeufer PayPal Freunde und legt das Versandrisiko dem Kaeufer auf.
- **Damen Trekking E-Bike Fischer** (3502153642, 790 €, ebike-rad): Referenz mit Streuung 3,06 nicht belastbar, kein Modell und kein Baujahr genannt.
- **BMW 316i Limo E36** (3502425383, 2000 €, youngtimer-alltag): Servolenkung defekt, Tonnenlager faellig, TUEV abgelaufen. Der Preis erklaert sich vollstaendig.
- **Quooker CUBE** (3502224503, 960 €, ebike-rad): Referenz mit Streuung 2,55 nicht belastbar; der Median mischt Armatur-Komplettsysteme mit dem reinen CUBE-Zusatzgeraet.
- **USM Haller Regal Reinweiss 5 Faecher** (3450998110, 870 €, design-sammeln): Gewerblicher Anbieter mit Haendlerpreis plus 109 Euro Lieferkosten. Der Median aus "USM Haller Regal 5" mischt Breiten und Hoehen (Streuung 2,17); 870 Euro fuer ein 180x75x37-Regal sind Marktniveau.
- **Cube Stereo Hybrid 140 HPC Race 625** (3502192193, 1350 €, ebike-rad): Der Verkaeufer nennt selbst ein Haendlerankaufgebot von 1.650 Euro und schreibt, dass Bremshebel und Griffe zu erneuern sind. Der niedrige Preis erklaert sich durch den Zustand.
- **Herrenrad Cube Touring One 54cm** (3502123868, 500 €, ebike-rad): Referenz mit Streuung 3,34 nicht belastbar, kein Modelljahr.
- **Bosch E-Trekking Victoria Rad Damen** (3502395566, 500 €, ebike-rad): Referenz mit Streuung 2,67 nicht belastbar, weder Modell noch Akkugroesse genannt.
- **Velo de Ville AEB 890 Trekking E-Bike** (3502183849, 1499 €, ebike-rad): Anzeige eines Rebike-Stores in Koeln-Marsdorf, also ein gewerblicher Refurbished-Preis mit Gewaehrleistung. Haendlerpreis auf Marktniveau.
- **TAG Heuer Aquaracer Chronograph 300M** (3501982198, 830 €, uhren): Referenz mit Streuung 2,52 nicht belastbar. Die Ref. CAY111B ist ein Quarzchronograph, der gebraucht bei rund 900 bis 1.300 Euro liegt; 830 Euro sind kein 20-Prozent-Abstand. Zusaetzlich Konto 71 Tage alt und die Zusage einer "Verkaeufergarantie" auf einem Privatprofil.
- **Eames Chair EA 217** (3502505826, 1450 €, design-sammeln): Die einzige belegbare Haendlerreferenz, die ich fand, betrifft einen EA 217 Softpad fuer 2.250 Euro, also eine hoeherwertige Variante. Fuer den hier angebotenen EA 217 ohne Softpad konnte ich keine zwei vergleichbaren Angebote finden; der Median beruht auf acht Anzeigen. Ich schaetze nicht.
- **Cube Touring Damenrad** (3502144624, 700 €, ebike-rad): Referenz mit Streuung 4,73 nicht belastbar.
- **Specialized E-Bike XL Rahmen** (3502147715, 950 €, ebike-rad): Referenz mit Streuung 5,0 nicht belastbar, kein Modell genannt.
- **Honda Fireblade CBR 900 RR SC28** (3502522370, 1690 €, motorraeder): Verkaeuferbewertung 0,35. Eine SC28 von 1995 mit 75.270 km liegt im Markt bei rund 2.000 bis 3.500 Euro; der Abstand ist nicht gross genug, um das Verkaeuferprofil aufzuwiegen.
- **Cube Stereo 120 Pro Fully Groesse S 2022** (3502132825, 1200 €, ebike-rad): Modelljahr genannt, aber der Median beruht auf nur zwoelf Anzeigen bei Streuung 2,36; ein Stereo 120 Pro von 2022 liegt gebraucht bei rund 1.200 bis 1.500 Euro. Kein belegbarer Abstand.
- **MacBook Pro 14 (M5)** (3502623656, 1300 €, macbook): Ein M5-MacBook-Pro 14 mit 16/512 GB kostet neu 1.799 Euro und gebraucht nach einem halben Jahr rund 1.400 bis 1.500 Euro. 1.300 Euro sind kein 20-Prozent-Abstand.
- **Gravelbike Cube Nuroad Pro Gr. S** (3502496517, 650 €, ebike-rad): Nuroad Pro ohne Modelljahr; gebraucht liegen diese Raeder bei 700 bis 900 Euro. Kein 20-Prozent-Abstand.
- **USM Haller Sideboard Lowboard** (3502527819, 899 €, design-sammeln): Sideboard mit zwei abschliessbaren Schubladen; solche Korpusse liegen gebraucht im Handel bei 900 bis 1.400 Euro. Marktpreis. Der Median mischt Breiten (Streuung 2,07).
- **Apple MacBook Pro 1TB wie neu** (3502175704, 980 €, macbook): Laut Attributen ein MacBook Pro 13" M1; solche Geraete mit 1 TB liegen gebraucht bei 600 bis 750 Euro. Der Angebotspreis liegt ueber dem Markt, nicht darunter. Referenz mit Streuung 2,99 ohnehin nicht belastbar.
- **MacBook Pro 14" M2 Pro 32/1TB** (3502559855, 1100 €, macbook): Das Logicboard wurde ersetzt und eine Delle am Gehaeuse verhindert, dass der Deckel buendig schliesst. Beides erklaert den Preis; ein intaktes Geraet dieser Konfiguration liegt bei 1.300 bis 1.500 Euro.
- **Longines HydroConquest Automatik** (3502211621, 600 €, uhren): Keine Referenznummer, keine Papiere, keine Box; die HydroConquest gibt es in Groessen und Werken mit deutlich unterschiedlichen Preisen. Ohne Modellbestimmung kein Marktwertnachweis. Konto 51 Tage alt.
- **Specialized Allez** (3502215519, 620 €, ebike-rad): Traegt den Unkenntnis-Bonus, scheitert aber am Nachweis: Ein Allez ohne Modelljahr und Ausstattung reicht vom Einsteiger-Alurad bis zum Sprint-Rahmen, die Referenz hat Streuung 2,73. Kein Marktwert bestimmbar, und ich schaetze nicht.
- **Sony PlayStation 5 Pro 2 TB** (3502204459, 530 €, konsolen-sweep): Der Verkaeufer verlangt ausdruecklich PayPal Freunde und schliesst Waren und Dienstleistungen aus, also Zahlung ohne Kaeuferschutz. Das ist ein Ausschlussgrund unabhaengig vom Preis; zudem liegt eine gebrauchte PS5 Pro bei rund 600 bis 650 Euro, der Abstand betraegt keine 20 Prozent.
- **Rennrad Specialized Elite Secteur** (3502622820, 450 €, ebike-rad): Referenz mit Streuung 2,58 nicht belastbar.
- **Trek Farley Fatbike** (3502553763, 450 €, ebike-rad): Kein Modelljahr und keine Ausstattungsangabe; die Farley-Reihe reicht von Alu bis Carbon. Median aus 17 Anzeigen mischt diese Varianten.
- **USM Haller Sideboard schwarz** (3502450634, 1000 €, design-sammeln): Beschreibung besteht aus zwei Zeilen ohne Masse; ohne Korpusgroesse ist kein Vergleich moeglich, und der Median mischt Breiten.
- **Original USM Haller Board in Gruen** (3318513954, 930 €, design-sammeln): Autorisierter USM-Partner mit Rechnung und 24 Monaten Gewaehrleistung, also ein Haendlerpreis. Ein 77x74x38-Board mit einer Klappe liegt im Handel genau dort.
- **Haibike XDURO Trekking Pro** (3502211752, 400 €, ebike-rad): Der Akku ist nicht dabei. Ein Bosch-Ersatzakku kostet 500 bis 800 Euro; der Preis erklaert sich vollstaendig.
- **Mafell Kettenstemmer** (3502554129, 700 €, werkzeug-maschinen): Referenz mit Streuung 4,6 nicht belastbar, kein Modell genannt.
- **Truma Aventa Comfort Ausseneinheit** (3400941253, 800 €, camper-marine): Referenz mit Streuung 2,67 nicht belastbar; angeboten wird nur die Ausseneinheit, der Median enthaelt Komplettanlagen.
- **Cube Nuroad Gravelbike** (3502112320, 850 €, ebike-rad): Modelljahr 2023 genannt, aber ein Nuroad von 2023 liegt gebraucht bei 800 bis 1.000 Euro. Kein 20-Prozent-Abstand.
- **Cube Mountainbike Groesse S** (3502400497, 500 €, ebike-rad): Traegt den Unkenntnis-Bonus, scheitert aber am Nachweis: weder Modell noch Modelljahr genannt, Referenz mit Streuung 4,44. Kein Marktwert bestimmbar.
- **Rennrad Cube Attain** (3502186930, 579 €, ebike-rad): Attain Modelljahr 2022 mit Claris 2x8, also die Einstiegsvariante; solche Raeder liegen gebraucht bei 550 bis 700 Euro. Der Median von 999 Euro enthaelt die hoeheren Attain-GTC-Varianten.
- **Volvo Penta Bootsmotor mit Z-Antrieb** (3502180918, 400 €, camper-marine): Referenz mit Streuung 10,0 nicht belastbar.
- **Fahrrad Herren Trekking** (3502373455, 350 €, ebike-rad): Weder Marke noch Modell genannt, Streuung 5,71.
- **Cube EXC Trekkingrad Damenrad** (3502546142, 450 €, ebike-rad): Referenz mit Streuung 6,0 nicht belastbar.
- **Diamond Chair von Knoll** (3345201576, 499 €, design-sammeln): Referenz mit Streuung 3,12 nicht belastbar; der Median mischt Originale und Nachbauten, und die Anzeige belegt die Herkunft nicht.
- **Vitra Eames Stool Modell A** (3502511709, 600 €, design-sammeln): Der Verkaeufer legt offen, dass die Leimfuge hervorsteht. Median aus acht Anzeigen; gebrauchte Eames Stools liegen bei 900 bis 1.200 Euro, mit dem beschriebenen Mangel ist der Preis korrekt.
- **MacBook Air (M1, rosegold)** (3502112211, 400 €, macbook): Macke im Gehaeuse, Speichergroesse nicht angegeben, Verkaeuferbewertung 0,58. Ein M1 Air mit 8/256 GB liegt bei 400 bis 450 Euro, also auf Marktniveau.
- **iphone 16 pro** (3502217740, 400 €, apple-mobil): Die Frontkamera funktioniert bei Videoanrufen nicht. Der Defekt erklaert den Preis.
- **4er Set Vitra Stuehle HAL Wood** (3055047580, 585 €, design-sammeln): Referenz mit Streuung 4,07 aus zehn Anzeigen nicht belastbar; der Median mischt Einzelstuehle und Sets.
- **Specialized Stumpjumper FSR 26 Zoll** (3502405719, 350 €, ebike-rad): 26-Zoll-Laufraeder datieren das Rad auf etwa 2010; der Median enthaelt aktuelle 29-Zoll-Modelle. Phantomersparnis.
- **Trekkingrad Herren KTM Life Force** (3502441472, 350 €, ebike-rad): Referenz mit Streuung 2,5 an der Grenze, kein Modelljahr. Kein belastbarer Vergleich.
- **E-Bike Pedelec Citybike Trekkingrad** (3502177660, 599 €, ebike-rad): Weder Marke noch Modell im Titel, Referenz aus acht Anzeigen mit Streuung 2,84.
- **DJI MINI 5 Pro + DJI Care Refresh** (3502604384, 600 €, optik-drohnen): Angeboten wird das Standardset mit zwei Akkus, nicht die Fly More Combo. Die Mini 5 Pro allein kostet neu 779 bis 799 Euro und gebraucht 480,90 Euro bei Galaxus. 600 Euro liegen ueber dem Gebrauchtpreis, es ist kein Fund.
- **Trekkingrad KTM** (3502151374, 320 €, ebike-rad): Kein Modell und kein Baujahr, Streuung 2,38 bei 99 gemischten Anzeigen.
- **29 Zoll CUBE** (3502388831, 300 €, ebike-rad): Referenz mit Streuung 3,91 nicht belastbar.
- **Apple MacBook Air M2 Top Zustand** (3502137260, 480 €, macbook): Ein M2 Air mit 8/256 GB liegt gebraucht bei 550 bis 650 Euro, der Abstand betraegt keine 20 Prozent. Zusaetzlich Konto 80 Tage alt und Gewerbetext auf Privatprofil.
- **MacBook Air 13 guter Zustand** (3502182997, 450 €, macbook): Titel sagt Air, die Attribute sagen MacBook Pro 13" M1; welches Geraet verkauft wird, ist unklar. Beide Varianten liegen mit 8/256 GB bei 450 bis 600 Euro, kein belegbarer Abstand.
- **Trek Mountainbike schwarz-rot** (3502193828, 315 €, ebike-rad): Referenz mit Streuung 5,62 nicht belastbar, kein Modell genannt.
- **Neuwertig Steam Deck OLED 512GB mit Speicherkarte** (3502122191, 360 €, konsolen-sweep): Gegen den bestaetigten Referenzpreis von 459 Euro (Valve, zertifiziert generalueberholt, mit einem Jahr Gewaehrleistung) betraegt der Abstand knapp 22 Prozent, und die Gewaehrleistung des Refurbished-Geraets gleicht diesen Rest aus. Zu knapp fuer eine Meldung.
- **iPhone 15 128GB** (3502215432, 235 €, apple-mobil): Die Kamera nimmt auf, die Bilder erscheinen aber nicht in der Galerie, Akku bei 80 Prozent, Verkaeuferbewertung 0,30. Der Defekt erklaert den Preis.
- **iPhone 15 Pro Grau** (3502147991, 320 €, apple-mobil): Rueckglas gesprungen. Der Schaden erklaert den Preis.
- **iPhone 15 Pro 128gb** (3502209565, 300 €, apple-mobil): Rueckseite defekt, Verkaeuferbewertung 0,18. Der Schaden erklaert den Preis.
- **Original Panton Chair schwarz** (3502188627, 160 €, design-sammeln): Referenz mit Streuung 3,0 nicht belastbar; der Median mischt Vitra-Originale und Nachbauten, und die Anzeige belegt die Herkunft nicht.
- **IPhone 15 128gb Schwarz** (3502180826, 250 €, apple-mobil): Rueckseite stark beschaedigt und gerissen. Der Schaden erklaert den Preis.
- **Cube Access Pro W Hardtail** (3502222041, 325 €, ebike-rad): Kein Modelljahr; der Median aus 99 Anzeigen mischt zehn Jahrgaenge des Access-Hardtails.
