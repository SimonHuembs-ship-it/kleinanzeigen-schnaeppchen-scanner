# Lauf 2026-09-24, morgens

- **Zeitpunkt:** 24. September 2026, 07:05 Uhr (MESZ)
- **candidates.json generiert:** 2026-09-24T04:27:21+02:00 (2 h 38 min alt, innerhalb der Vier-Stunden-Grenze)
- **Zeitraum des Scans:** 2026-09-23T23:13:32+02:00 bis 2026-09-24T04:13:32+02:00
- **Gesichtete Anzeigen (letzter Scan):** 26.851
- **Kandidaten in der Warteschlange:** 153
- **Bereits in deal_log.csv:** 0
- **Bereits am 22./23. September mit Grund verworfen:** 77 (nicht erneut aufgerollt, siehe unten;
  Ausnahme: die Leica M8 wurde bewusst noch einmal aufgerollt, siehe naechster Abschnitt)
- **Neu geprueft:** 76
- **Gemeldet:** 0

## Funde

Keine. `deals.json`, `email_output.html` und `deal_log.csv` bleiben unveraendert, es wird keine Mail
ausgeloest.

## Der knappste Fall: Leica M8, 1.200 € (`3521065944`)

Dieser Kandidat war im Lauf dieses Morgens bereits als Fund ausgeschrieben und ist nach erneuter
Pruefung wieder verworfen worden. Der Vorgang gehoert ins Protokoll, weil die Umkehr auf neuen
Belegen beruht:

Fuer den Fund sprach: Konto seit 2011, Bewertung 0,86, alle drei Abzeichen auf Stufe 2, im Text
ausdruecklich "Vorbeikoommen, testen, kaufen", und eine Haeufung vertippter Doppelbuchstaben
("Vooll", "BAazahlung", "oohne"), also das Gegenteil des glatten Textbausteins, an dem
Betrugsanzeigen zu erkennen sind. Dazu 1.200 Euro gegen ein eBay.de-Gebrauchtband von 1.626 bis
1.938 Euro, gegen den Kleinanzeigen-Median von 1.979 Euro (n=9, Streuung 1,59, belastbar) und gegen
den usedcameratracker-Median von 2.300 US-Dollar - und zwar fuer das Gehaeuse allein, waehrend die
Anzeige vier Akkus, Leica-Ladegeraet, Classic-Case-Halbschale, Gurt und ein Jupiter-8 in M39 mit
Adapter enthaelt.

Dagegen sprach, und das hat den Ausschlag gegeben:

1. **Der Lauf vom 23. September abends hat genau diese Anzeige schon geprueft und verworfen**
   (`runs/2026-09-23/run_results.md`), mit zwei Gruenden: die Anzeige verlangt "PayPal for
   friends & family", also Zahlung ohne Kaeuferschutz, was prompt.md Schritt 2c als Warnsignal
   nennt; und die Preisangaben von usedcameratracker.com liessen sich nicht in Einklang bringen,
   weil dieselbe Seite neben der Spanne von 2.185 bis 2.629 US-Dollar ein guenstigstes aktives
   Angebot von 687 US-Dollar bei MPB fuehrt.
2. **Die heutige Recherche hat diesen Widerspruch nicht aufgeloest, sondern erklaert - zulasten des
   Fundes.** Der haeufigste Ausfallpunkt der M8 ist der Verschluss, und Leica repariert an der M8
   weder den CCD-Sensor noch das rueckseitige Display noch. Ein Gehaeuse in schwaecherer
   Zustandsstufe ist deshalb tatsaechlich einen Bruchteil wert, das 687-Dollar-Angebot ist kein
   Ausreisser, sondern das untere Ende einer sehr breiten Verteilung. Die Anzeige beschreibt das
   Geraet als "altersentsprechend gebraucht" und nennt weder Ausloesezahl noch Seriennummer noch
   den Zustand des Sensordeckglases - sie liegt also genau in dem Bereich der Verteilung, der sich
   nicht bepreisen laesst.

Das Band von 1.626 bis 1.938 Euro ist damit kein Marktwert, sondern der Angebotspreis der besser
erhaltenen Exemplare. Ein bestaetigter Marktwert fuer *dieses* Gehaeuse liegt nicht vor, und ohne
ihn sind die geforderten 20 Prozent Abstand nicht nachweisbar. hifishark.com, usedcameratracker.com,
mpb.com, asgoodasnew.de und ebay.de sind aus dieser Umgebung nicht direkt abrufbar, eine
Aufloesung ueber die Fachquelle selbst war also nicht moeglich. Nach prompt.md Schritt 3 - lieber
null Funde als ein schwacher Fund - wird nicht gemeldet.

## Nicht gemeldet, die groessten Abstaende zuerst

- `3521291073` **Mercedes SL 500 R129, 11.500 €** (5.600 € unter Median): TUEV abgelaufen, Verdeck
  funktioniert nicht zuverlaessig, ABS- und ASR-Kontrollleuchten an, vom Verkaeufer selbst als
  Bastler- und Projektfahrzeug ausgeschrieben. Der Preis erklaert sich aus den offengelegten
  Maengeln. Zusaetzlich Konto erst 23 Tage alt.
- `3521206162` **BMW E36 325i Coupe, 8.500 €** (4.730 €): Der Median von 13.230 Euro stammt aus nur
  acht Anzeigen bei Streuung 2,44, und das 25-Prozent-Quartil derselben Gruppe liegt mit 7.800 Euro
  **unter** dem Angebot. 254.000 km bei einem 33 Jahre alten Coupe: das Angebot liegt im Markt,
  nicht darunter. Verkaeuferbewertung 0,75.
- `3521279379` **Rolex Datejust 36, 4.990 €** (4.300 €): Plexiglas und Erstverkaufsjahr 1980 machen
  das zu einer Vintage-Referenz 1601, der Median von 9.290 Euro mischt sie mit modernen
  126xxx-Gehaeusen unter Saphirglas - keine vergleichbare Referenzgruppe. Eigene Pruefung: Chrono24
  setzt die 1601 mit Weissgold-Riffellunette und blauem Zifferblatt bei 5.000 bis 6.000 Euro an.
  4.990 Euro sind damit hoechstens 17 Prozent darunter, die geforderten 20 Prozent sind nicht erreicht.
- `3521398118` **Mercedes W201 190E 2.3, 2.899 €** (3.918 €): Referenz nicht belastbar (Streuung 2,9).
  Inhaltlich erledigt sich der Fall ohnehin: "Projektaufgabe", seit 2019 abgemeldet, bekommt keinen
  Zuendfunken, Rost in Reserveradmulde und Innenkotfluegel, ausdruecklich nicht fahrbereit.
- `3521322840` **BMW 320i Touring E36, 1.999 €** (3.311 €): Der Verkaeufer listet selbst fehlende
  Handbremsseile, defektes Fensterhebergestaenge, Airbag-Leuchte, nicht eingetragenes Lenkrad und
  nicht eingetragene Felgen auf 268.000 km. Ein ehrlich beschriebener Winterbeater zum Beaterpreis,
  kein Fund.
- `3521488549` **BMW R100 GS, 2.900 €** (2.365 €): Referenz nicht belastbar (Streuung 7,51, das
  Quartil liegt bei 1.050 Euro). Die Anzeige nennt weder Baujahr noch Laufleistung noch Zustand,
  das Motorrad steht seit fuenf Jahren und ist nicht fahrbereit, und es hat nur oesterreichische
  Papiere. Ein Klassiker ohne deutsche Zulassungsbescheinigung Teil II ist nach prompt.md Schritt 2e
  nicht billig, sondern richtig bepreist.
- `3521386712` **Thonet S 411 Freischwinger-Sessel, 1.200 €** (1.700 €): Referenz nicht belastbar
  (Streuung 2,53, Quartil 1.500 Euro). Ein belastbarer Gebrauchtpreis fuer genau diese Ausfuehrung
  liess sich nicht belegen, also kein bestaetigter Marktwert und damit kein Fund.
- `3418665990` **IWC Portugieser Chronograph IW371447, 4.200 €** (1.690 €): Eigene Pruefung ergibt
  fuer gebrauchte IW371447 ein Niveau von 3.950 bis 4.850 Euro. Das Angebot liegt mitten darin.
  Dazu gewerblicher Verkaeufer mit Bewertung 0,59, ohne Papiere, mit selbst ausgestelltem
  "Echtheit Zertifikat".
- `3521429414` **Cube Touring One Damenrad, 429 €** (1.171 €): Der Median von 1.600 Euro stammt aus
  E-Bike-Anzeigen, das hier ist ein Trekkingrad ohne Motor mit Originalpreis 619 Euro laut Rechnung.
  Phantomersparnis.
- `3521456685` **Vitra Alcove Sofa 3-Sitzer Lowback, 1.850 €** (1.149 €): Eigene Pruefung findet fuer
  einen gebrauchten 3-Sitzer Lowback 2.730 Euro und fuer weitere gebrauchte Alcove-Sofas 3.000 bis
  3.600 Euro - allerdings durchweg Haendlerpreise fuer die teurere Highback-Variante oder
  Neuzustand. Gegen den relevanten Vergleich, einen gewerblichen Buero-Gebrauchtmoebelhaendler,
  ist 1.850 Euro fuer die Lowback-Ausfuehrung der uebliche Preis. Verkaeufer ist gewerblich mit
  Bewertung 0,47.
- `3521287928` **USM Haller Teile, 390 €** (1.120 €): 13 lose Metalltablare gegen einen Median aus
  kompletten Moebeln. Nicht vergleichbar.
- `3521350751` **Union Glashuette Noramis, 1.000 €** (1.100 €): Die Anzeige nennt keine
  Referenznummer, und die Noramis-Linie reicht von der schlichten Dreizeigeruhr ueber Datum und
  Gangreserve bis zum Chronographen. Konkrete Gebrauchtangebote liegen bei 1.300 Euro (D012.407,
  2023) und 1.450 Euro (D005.424 Gangreserve) - ohne Referenznummer laesst sich nicht sagen, welches
  davon das Vergleichsstueck ist. Kein bestaetigter Marktwert, also kein Fund.

## Nicht gemeldet, uebrige neue Kandidaten

- `3521521893` Accuphase P4100, 3.100 €: Das Modell existiert (Stereoendstufe, 2008-2013,
  Neupreis rund 7.090 Euro), hifishark.com ist aus dieser Umgebung nicht abrufbar. Ueber die
  Websuche belegbare Gebrauchtpreise liegen bei 3.299 Euro (aktuelles Angebot) in einer Spanne von
  2.249 bis 5.800 Euro. 3.100 Euro liegen damit im Markt, nicht 20 Prozent darunter.
- `3521501295` Steam Deck OLED 1 TB, 465 €: Valve verkauft dasselbe Geraet generalueberholt mit
  voller Garantie fuer 549 Euro. Gegen diese Obergrenze fehlen die 20 Prozent. Der Median von
  710 Euro mischt Neugeraete ein.
- `3521535732` Steam Deck OLED 512 GB, 360 €: dieselbe Rechnung gegen 459 Euro generalueberholt von
  Valve. Ausserdem bei Versand ausschliesslich PayPal Freunde.
- `3521335181` PS5 Pro 2 TB mit Laufwerk, 519 €: Der Median von 1.199 Euro liegt oberhalb des
  Neupreises der Konsole und kann nicht stimmen. 519 Euro mit Laufwerk und OVP sind fuer eine im
  Januar 2026 gekaufte PS5 Pro der uebliche Gebrauchtpreis.
- `3521448013` PS5 Pro "Limitierte Edition" mit Spielen, 550 €: Referenz nicht belastbar
  (Streuung 9,99). Konto sechs Tage alt, keine Abholung, nur Versand, keine Angabe welche Edition.
  Das ist das Betrugsmuster, kein Fund.
- `3520973219` MacBook Pro 14 M5 1 TB, 1.350 €: Das 14-Zoll-M5-Modell startet neu bei 1.499 Euro,
  die 1-TB-Variante liegt neu bei rund 1.730 Euro. 1.350 Euro fuer ein drei Monate altes Geraet
  sind der normale Gebrauchtpreis, keine 20 Prozent darunter. Dazu: keine Haendlerrechnung mehr
  vorhanden, keine Abholung, Bewertung 0,63.
- `3330736281` Longines HydroConquest L3.742.4.56.6 Fullset, 850 €: Gebrauchte HydroConquest in
  Stahl mit Box und Papieren liegen bei 750 bis 950 Euro. Das Angebot liegt im Markt.
- `3521350581` TAG Heuer Carrera Calibre 5 WAR211A, 1.300 €: Gebrauchtniveau dieser Referenz
  1.100 bis 1.500 Euro, Angebot mittendrin.
- `3521211371` RTX 3090 Manli 24 GB, 720 €: bereits am 23. September verworfen, Gebrauchtmarkt
  800 bis 950 Euro, also rund 10 Prozent Abstand statt der geforderten 20. Ergaenzend: der
  Verkaeufer beschreibt selbst Reste von Waermeleitpaste eines fremden Kuehlkoerpers vom
  Vorbesitzer, also eine umgebaute Karte.
- `3521450582` Cube Reaction Hybrid Pro 500, 900 €: "gechipt", Unterstuetzung bis 45 km/h. Eine
  entfernte Abregelung kostet Betriebserlaubnis und Versicherungsschutz - eine wertmindernde
  Umbaute, der Preis ist richtig.
- `3521521053` Yamaha Aerox NOTVERKAUF, 850 €: 70-cm3-Zylinder und Rennauspuff statt 25er-Papiere,
  dazu "springt nicht an, kein Funke". Umbau plus Defekt.
- `3521534195` Aprilia Tuono 125 NOTVERKAUF, 1.000 €: Sturzschaden, TUEV abgelaufen, Maengelliste
  vom Verkaeufer selbst.
- `3521529374` TVR 3000 M, 7.999 €: verkauft in Teilen, es fehlen Motor, Sitze, Tueren,
  Armaturenbrett, Differenzial, Scheiben und Felgen. Kein Marktwert fuer ein unvollstaendiges
  Fahrzeug ableitbar.
- `3501198452` Simson Star in Einzelteilen, 4.000 €: "Der Rahmen wurde von keinen Professionellen
  Schweisser Geschweisst" - ein nicht fachgerecht geschweisster Rahmen ist kein Teilewert, sondern
  ein Mangel.
- `3521499891` YT Tues Uncaged 11, 3.500 €: zwei Saetze Beschreibung, kein Zustand, keine Laufleistung,
  Versand statt Abholung, Verkaeufer ohne Bewertung. Ohne Angaben kein bestaetigbarer Marktwert.
- `3521359540` YT Industries Tues, 850 €: kein Modelljahr, "typische Gebrauchsspuren", Konto juenger
  als sechs Monate. Ein Downhiller ohne Jahrgang laesst sich nicht bewerten.
- `3521341755` Le Corbusier Liege "LC4 Stil", 275 €: ausdruecklich eine Nachbildung, nicht das
  Original. Der Median aus echten LC4 ist nicht die richtige Referenzgruppe.
- `3521271339` Vitra/Herman Miller Eames Fiberglas Stuhl, 279 €: Der Median liegt bei 462 Euro, aber
  gerade bei Fiberglas-Schalen ist die Echtheit der Kernpunkt, und die Anzeige zeigt kein Label und
  keine Praegung. Bei 184 Euro absolutem Abstand nicht genug, um das Risiko zu melden.
- `3521466934` KPM Urbino Teetassen, 165 €: Referenz nicht belastbar (Streuung 3,03), sechs
  Obertassen ohne Untertassen gegen einen Median aus gemischten KPM-Posten.
- `3521464960` Vitra Chefsessel, 190 €: Referenz nicht belastbar (Streuung 4,98), kein Modellname.
- `3521401399`, `3521385886`, `3521486878`, `3521046006`, `3521161163`, `3520808231` USM Haller
  Sideboards, Lowboards und Rollcontainer zwischen 380 und 899 €: Der USM-Gebrauchtmarkt haengt an
  Korpusmass, Farbe und Zahl der Klappen. Keine dieser Anzeigen nennt eine Konfiguration, die sich
  gegen zwei konkrete Vergleichsangebote stellen liesse.
- `3521509165` Drehbank von Weiler, 600 €: Referenz nicht belastbar (Streuung 5,63), Verkaeufer aus
  einem Nachlass kann "nicht mehr dazu sagen" - kein Typ, kein Spitzenabstand, kein Zustand.
- `3521304963`, `3521290045`, `3521301937`, `3521506008`, `3521321595`, `3521323712`, `3521292023`,
  `3521291300`, `3521351281`, `3521318565`, `3521367918`, `3521310046`, `3521521752`, `3521360427`,
  `3521473329` Fahrraeder und E-Bikes zwischen 300 und 1.000 €: durchweg ohne Modelljahr,
  Akkuzustand oder Laufleistung, und die Mediane mischen E-Bikes mit Rädern ohne Motor. Kein
  einzelner Fall kam ueber einen belegbaren 20-Prozent-Abstand.
- `3521477925` MacBook Pro M2, 600 €, `3521487949` MacBook Air, 400 €, `3521511385` MacBook Air M1
  8/256, 449 €: die ersten beiden nennen weder Bildschirmgroesse noch Speicher, der dritte liegt mit
  449 Euro im Gebrauchtband des M1 Air (400 bis 500 Euro).
- `3521291397` iPhone 14 Pro Max "fuer Bastler", 230 €, `3521515770` iPhone 13 Pro 1 TB, 270 € und
  die uebrigen elf Apple-Mobilgeraete zwischen 150 und 320 €: entweder ausdruecklich defekt
  (Display, Rueckglas) oder mit offengelegten Beschaedigungen und Akkukapazitaet unter 80 Prozent.
  In allen Faellen erklaert der Zustand den Preis; die absoluten Abstaende liegen unter 400 Euro.
- `3521396635` Thorens TD 320, 300 €, `3521514396`/`3521512891` Vitra EA105, je 460 €,
  `3521517657` Haushaltsaufloesung, 1.000 €, `3521448013` und die uebrigen Restkandidaten: entweder
  ohne Referenz, ohne pruefbare Angaben oder mit einem absoluten Abstand unter 350 Euro.

## Nicht erneut aufgerollt

77 der 153 Kandidaten standen schon am 22. oder 23. September in `candidates.json` und sind in
`runs/2026-09-22/run_results.md` und `runs/2026-09-23/run_results.md` mit Grund aufgefuehrt -
darunter die drei groessten Abstaende des heutigen Gesamtfelds (Mercedes SL 300 24V US-Import
6.607 €, Rolex Datejust 41 Full Set 4.290 €, Drehmaschine Weiler Praktikant 160 3.790 €). Die
Begruendungen tragen unveraendert: US-Import ohne Zulassungsbescheinigung Teil II, nur sechs
Prozent unter dem guenstigsten Chrono24-Angebot, Referenz nicht belastbar.

## Methodik dieses Laufs

Gepruefte Reihenfolge: absteigend nach absolutem Abstand zum Median, innerhalb gleicher Groessen-
ordnung zuerst die liquiden Kategorien (Uhren, Apple, Grafikkarten, Drohnen, Kameras). Kein
Kandidat hat die Beweislast aus prompt.md Schritt 2a getragen: zwei konkrete Vergleichsangebote
desselben Modells mit derselben wesentlichen Ausstattung oder eine der Referenzquellen aus
Schritt 2d, und darauf mindestens 20 Prozent Abstand.

Das Feld dieses Laufs bestand ueberwiegend aus drei Gruppen, in denen der Median systematisch zu
hoch liegt: Fahrzeuge mit offengelegten Maengeln (der Preis erklaert sich selbst), Fahrraeder und
E-Bikes ohne Modelljahr (der Median mischt Motor und kein Motor), und Apple-Mobilgeraete mit
Displayschaden oder Akku unter 80 Prozent. Die einzigen beiden Kandidaten mit einem belegbaren
Abstand - Leica M8 und Union Glashuette Noramis - sind an der Bestaetigung des Marktwerts
gescheitert, nicht an der Anzeigenqualitaet.

Einschraenkung dieser Umgebung: Der Egress-Proxy blockiert hifishark.com, usedcameratracker.com,
mpb.com, asgoodasnew.de und ebay.de fuer den Direktabruf. Die Zahlen dieser Quellen waren nur ueber
die Websuche und deren Zusammenfassungen zu bekommen. Beim Accuphase P-4100 ist das der Grund,
warum kein Median einer Fachquelle, sondern nur eine breite Angebotsspanne belegt werden konnte -
und bei der Leica M8 der Grund, warum sich der Widerspruch in den usedcameratracker-Zahlen nicht
an der Quelle aufloesen liess.
