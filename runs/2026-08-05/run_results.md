# Routine-Lauf 2026-08-05T00:37+02:00

- Datenquelle: `candidates.json`, generiert 2026-08-05T00:06:08+02:00 (31 Minuten alt, Frist 12 h eingehalten)
- Zeitraum des Scans: 2026-08-04T17:49:47+02:00 bis 2026-08-04T23:49:47+02:00
- Kandidaten in der Datei: 31
- Bereits gemeldet und deshalb übersprungen: 6
- Inhaltlich geprüft: 25
- **Gemeldete Funde: 0**

Kein Fund heißt nach prompt.md Schritt 5: nichts committen, nichts pushen, keine Mail.
`deals.json` und `email_output.html` bleiben unverändert auf dem Stand der letzten Mail,
`python -m scanner.report` wurde nicht ausgeführt.

## Zwei Befunde zur Pipeline

**1. `deal_log.csv` existierte nicht.** Der Lauf von gestern (`dc6fbef`, sechs Funde) hat
Schritt 4.2 ausgelassen und die Datei nie angelegt. Die Doppelmeldungssperre war damit leer.
Die sechs bereits gemailten Anzeigen habe ich ersatzweise über die committete `deals.json`
ausgeschlossen. Diese Notlösung trägt nur so lange, wie `deals.json` nicht überschrieben wird —
beim nächsten Lauf mit Funden ist sie weg. Die Datei ist jetzt lokal mit Kopfzeile angelegt,
wird aber mangels Fund nicht committet und geht mit dem Container verloren.

Ausgeschlossene IDs: 3431889887, 3475862357, 3476454355, 3476468044, 3476665944, 3476671905

**2. `candidates.json` stammt aus dem Scan *vor* den letzten beiden Fixes.** Der Scan lief
00:06, die Commits `dc6fbef` (TA-Technix-Fehltreffer) und `b7cdcf2` (schärfere Referenzfrage,
`streuung`/`belastbar`) kamen 00:09 und 00:17. Folgen für diesen Lauf:

- Kein Kandidat trägt `referenz.belastbar` oder `referenz.streuung`. Die Prüfung aus
  prompt.md Schritt 2a lief damit ins Leere, jeder Marktwert wurde eigenständig belegt.
- Alle Mediane kommen aus dem alten Vier-Wort-Query-Builder, den `b7cdcf2` gerade wegen
  Phantomersparnissen ersetzt hat. Sichtbar an Fragen wie `Apple MacBook OVP`,
  `Ich iPhone 13` oder `iPhone 13 Pro` ohne Speichergröße. Kein Median wurde als Beleg benutzt.
- Vier TA-Technix-Fehltreffer stehen noch in der Liste.

## Verworfene Kandidaten

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3476623613 | iPhone 13 Pro | 200 € | Frontglas gerissen, offengelegt. Displaytausch 13 Pro liegt bei 150–250 €, der Preis erklärt sich damit selbst. Speichergröße nirgends genannt, Marktwert nicht bestimmbar. |
| 3476443651 | iPhone 14 Plus | 160 € | Display gerissen, Rückkamera defekt, vom Verkäufer selbst als Teildefekt deklariert. Korrekt bepreist. |
| 3476554204 | iPhone 13 Pro Max | 200 € | Rückglas und Kameraglas gebrochen, Akku 84 %. Rückglastausch ist die teuerste Reparatur am Gerät. Korrekt bepreist. |
| 3476446919 | iPhone 14 Pro Max 128 GB | 280 € | Akku und Backcover mit Nicht-Originalteilen getauscht. Fremdteile lösen dauerhafte iOS-Warnungen aus und mindern den Wert. Korrekt bepreist. |
| 3476632539 | iPhone 12 Pro 512 GB | 175 € | Kein Schaden genannt, aber Akku 79 %, unter Apples 80-%-Schwelle, Tausch ~100 €. Belegt gefunden: Ankauf 512 GB bis 270,81 € (handyverkauf.net), Refurb-Handel 299–399 €, beides Händlerware mit Garantie und ≥80 % Akku. Zwei private Vergleichsangebote derselben Ausstattung mit vergleichbarem Akku nicht gefunden, Marktwert damit nicht bestätigt. |
| 3476469639 | iPhone 13 Pro | 215 € | Akku 77 %, Konto 112 Tage alt, nur Versand, Beschreibung ohne prüfbare Angaben. Kein bestätigter Abstand. |
| 3476680020 | iPhone 13 Pro Max Gold 128 GB | 220 € | Display mit zwei Sprüngen, Rückglas kaputt. Korrekt bepreist. |
| 3476671705 | Ich verkaufe iPhone 13 | 180 € | "Weitere Details per Anfrage", keine Angabe zu Speicher, Akku oder Zustand. Konto 140 Tage. Referenzfrage "Ich iPhone 13" ist unbrauchbar. Nicht bewertbar. |
| 3476633605 | iphone 12 pro max 256gb | 200 € | Lädt nur noch kabellos, Ladebuchse also defekt, Akku 75 %. Defekt erklärt den Preis. |
| 3476677075 | Apple MacBook OVP | 390 € | Laut Attributen MacBook Pro 13" 2019 Intel i5 / 16 GB / 256 GB. Vergleichbares Gerät auf eBay bei rund 365 €, die Anzeige liegt darüber statt darunter. Zusätzlich Intel-Mac am Ende des macOS-Supports. |
| 3476629439 | Apple MacBook Air 13" 2020 | 349 € | Titel sagt Air, Attribut sagt MacBook Pro 13" (2020, Intel), Beschreibung sagt Air. Intel oder M1 nicht unterscheidbar, dazu Delle am Gehäuse. Ohne eindeutiges Modell kein Marktwert. |
| 3476456055 | Mercedes Benz 190 W201 | 2.500 € | Fahrzeugzustand "Beschädigtes Fahrzeug", 182.192 km, abgemeldet, Kotflügel verbreitert, tiefergelegt auf H&R. Umbauten senken den Sammlerwert, der Preis ist richtig. |
| 3476633976 | BMW E36 Compact 316i | 1.500 € | Zwei Unfälle, laut Verkäufer "eher mäßig als professionell repariert", 238.000 km, Fahrzeugzustand "Beschädigtes Fahrzeug". Preis erklärt sich selbst. |
| 3476674868 | Neumann M50c | 8.000 € | Originale M50 liegen bei rund 16.000 €, aber die Anzeige nennt selbst eine eingebaute M49-M7-Kapsel. Das M50c trug ab Werk die K83-Kapsel, das Gerät ist damit kein originales M50c und sein Wert nicht aus M50-Preisen ableitbar. Dazu Konto 33 Tage, Weltversand, Textbaustein "nach Auktionsende" aus einer eBay-Vorlage. Kein bestätigter Marktwert. |
| 3476464219 | TA Technix Sportauspuff Golf 4 | 130 € | Fehltreffer. TA Technix ist eine Fahrwerks- und Auspuffmarke, kein HiFi-Hersteller. |
| 3476672928 | TA Technix Gewindefahrwerk Golf 2 | 200 € | Fehltreffer, siehe oben. |
| 3461568097 | TA Technix Gewindefahrwerk Astra F | 220 € | Fehltreffer, siehe oben. |
| 3476643228 | TA Technix 5x120 Radsatz | 750 € | Fehltreffer, tatsächlich ein BMW-Radsatz mit Nexen-Reifen. |
| 3476636757 | Nakamichi Dragon | 2.750 € | Revidierte Dragons liegen 2026 bei 2.500–4.500 € (hifishark, Fachhandel), 2.750 € liegt im Band statt 20 % darunter. Die Anzeige nennt keinen Servicestand, keine Seriennummer, nichts zu Riemen, Andruckrolle oder NAAC, also genau die Punkte, an denen ein Dragon hängt. Werbeprosa ohne prüfbare Angaben, Zahlung nur per Überweisung. |
| 3476625679 | Marinucci Piano-Akkordeon 120 Bass | 750 € | Konto 3 Tage alt, nur Versand, generischer Werbetext. Für Marinucci-120-Bass-Instrumente kein belastbarer Referenzwert gefunden, deshalb kein geschätzter Marktwert. |
| 3476559533 | Haushaltsauflösung Geislingen | 800 € | Konvolut ohne definierten Inhalt: CDs, Platten, Bücher, Schlafzimmer, Gläser. Kein Marktwert bestimmbar. |
| 3476471318 | Beko Küche mit E-Geräten | 800 € | Einbauküche zum Selbstabbau, Wert hängt vollständig von Maßen und Zustand vor Ort ab. Kein Marktwert bestimmbar. |
| 3476641702 | Wohnungsauflösung Lüdenscheid | 999 € | Beschreibung besteht aus einem Satz, kein Inhalt genannt. Nicht bewertbar. |
| 3476469206 | Haushaltsauflösung Ahlbeck | 1.498 € | Ware steht in Swinemünde, verfügbar erst ab Mitte September, Fotos nur per Mail, Telefonnummer im Text. Verlagerung der Kommunikation von der Plattform, dazu nur ein Bild. |
| 3468854544 | Mercedes A220 4Matic AMG Line | 23.990 € | Marktband für A 220 Baujahr 2019 laut AutoScout24 und mobile.de rund 19.590–26.870 €. 23.990 € bei 64.000 km liegt mittig, kein Abstand. Restgarantie ist ein Santander-Care-Vertrag aus einer Finanzierung, Übertragbarkeit offen. |

## Belegquellen dieses Laufs

- hifishark.com und Fachhandel für Nakamichi Dragon
- AutoScout24 und mobile.de für Mercedes A 220 Baujahr 2019
- handyverkauf.net, Clevertronic, asgoodasnew für iPhone 12 Pro 512 GB
- eBay für MacBook Pro 13" 2019 i5 / 16 GB / 256 GB
- recordinghacks.com und slashcam für Neumann M50 / M50c Kapselbestückung und Preisniveau

---

# Zweiter Routine-Lauf 2026-08-05T07:08+02:00

- Datenquelle: unverändert `candidates.json`, generiert 2026-08-05T00:06:08+02:00 (7 h 02 min alt, Frist 12 h eingehalten)
- Kandidaten in der Datei: 31, bereits in `deal_log.csv`: 6, inhaltlich geprüft: 25
- **Gemeldete Funde: 0**

`deal_log.csv` existiert inzwischen (Commit `ff45765`) und hat die sechs Anzeigen der
ersten Mail diesmal regulär ausgeschlossen. Der Befund 1 des ersten Laufs ist damit erledigt.

## Der Lauf hat keine neuen Daten bekommen

Der um 00:41 eingerichtete Cron (`15 3 * * *`, also 05:15 Berliner Zeit) ist bis 07:08 nicht
gelaufen. Die Actions-Historie kennt für `scan.yml` genau drei Läufe, alle vom 4. August und
alle per `workflow_dispatch`; ein `schedule`-Lauf hat nie stattgefunden. `origin/main` steht
weiterhin auf `dbc9995`, `candidates.json` ist unverändert die Datei von 00:06.

Wahrscheinlichste Ursache: Ein frisch gepushter Cron greift bei GitHub Actions oft erst ab
dem übernächsten Fenster, dazwischen liegen bei Scheduled Workflows regelmäßig Verzögerungen
von mehreren Stunden. Zwischen Push (22:41 UTC) und erstem Termin (03:15 UTC) lagen nur
4 h 34 min. Ob sich das morgen von selbst einrenkt, zeigt der Lauf am 6. August. Wenn nicht,
bleibt der `workflow_dispatch` als manueller Auslöser, oder der Scan wird an den Anfang der
Routine gehängt, statt ihn auf einen eigenen Cron zu setzen.

## Ergebnis der erneuten Prüfung

Geprüft wurde derselbe Bestand noch einmal unabhängig, inklusive erneuter Websuche für die
vier Posten über 1.000 €. Die Bewertung deckt sich in allen 25 Fällen mit der Tabelle oben,
kein Kandidat kippt in die andere Richtung. Die drei Fälle, die überhaupt in die Nähe eines
Fundes kamen:

| ID | Titel | Preis | Bestätigtes Preisniveau | Ergebnis |
|---|---|---|---|---|
| 3476636757 | Nakamichi Dragon | 2.750 € | 3.400 € (willhaben, 12.06.2026), 3.699 € (Audioweb, 07.06.2026), 3.800 € (Catawiki-Zuschlag, 12.07.2026), 3.500 € refurbished (Kleinanzeigen, 06.06.2026) | Alle belegten Preise betreffen revidierte oder als funktionsgeprüft angebotene Geräte. Die Anzeige nennt keinen Servicestand. Gegen den niedrigsten Beleg sind es 19,1 % Abstand, die 20-%-Schwelle ist damit nicht erreicht. Verworfen. |
| 3476674868 | Neumann M50c | 8.000 € | ~16.000 € für originale M50 (slashcam zur M-50-V-Neuauflage, recordinghacks zur Baureihe) | Das M50c von 1965 trägt ab Werk die Mylar-Kapsel K83. Die Anzeige nennt selbst eine eingebaute M49-M7-Kapsel, das Gerät ist damit kein originales M50c und der M50-Preis nicht übertragbar. Dazu Konto 33 Tage alt, Weltversand, eBay-Baustein "nach Auktionsende". Kein bestätigter Marktwert, verworfen. |
| 3468854544 | Mercedes A220 4Matic AMG Line | 23.990 € | 19.590–26.870 € (AutoScout24), 19.411–27.937 € (mobile.de), beide für Baujahr 2019 | 23.990 € bei 64.000 km liegt mittig im Band. Kein Abstand, verworfen. |

Der einzige Kandidat mit `unkenntnis_bonus` (3476623613, iPhone 13 Pro, 200 €) scheitert nicht
an der Anzeigenqualität, sondern am gerissenen Frontglas: Der Preis erklärt sich selbst, und
ohne Angabe der Speichergröße ist kein Marktwert bestimmbar.

`referenz.belastbar` und `referenz.streuung` fehlen weiterhin in jedem der 31 Kandidaten, weil
die Datei aus dem Scan vor Commit `b7cdcf2` stammt. Die Prüfung aus prompt.md Schritt 2a lief
erneut ins Leere, jeder Marktwert wurde eigenständig belegt.

Kein Fund heißt nach prompt.md Schritt 5: nur dieses Protokoll wird committet.
`deals.json`, `email_output.html` und `deal_log.csv` bleiben unverändert,
`python -m scanner.report` wurde nicht ausgeführt, es geht keine Mail raus.

---

# Routine-Lauf 2026-08-05T16:31+02:00 (zweiter Lauf des Tages)

- Datenquelle: `candidates.json`, generiert 2026-08-05T16:19:55+02:00 (12 Minuten alt, Frist 12 h eingehalten)
- Zeitraum des Scans: 2026-08-04T13:18:25+02:00 bis 2026-08-05T13:18:25+02:00
- Gesichtete Anzeigen laut Scan: 503.904
- Kandidaten in der Datei: 40
- Bereits in `deal_log.csv` und deshalb übersprungen: 0
- Inhaltlich geprüft: 40
- **Gemeldete Funde: 1**

Dies ist ein neuer Bestand, nicht der des Laufs von 00:37 Uhr: Der Scan von 16:19 Uhr
(`runs/2026-08-05-2/scan.md`) hat den Zeitraum auf 24 Stunden geweitet und liefert 40 statt
31 Kandidaten. Anders als beim Bestand von heute Nacht sind `referenz.belastbar` und
`referenz.streuung` diesmal in allen Kandidaten gesetzt.

## Fund

| ID | Titel | Preis | Bestätigtes Preisniveau | Abstand |
|---|---|---|---|---|
| 3476798448 | DJI Mavic 3 Cine Premium Combo | 1.100 € | ~1.700 € | 35 % |

Belege für das Preisniveau: MPB (Referenzquelle für Kameras nach prompt.md Schritt 2d) führt
sieben gebrauchte Cine Premium Combos zu 1.839–1.919 US-Dollar, also rund 1.690–1.765 €. Ein
deutsches Händlerangebot auf gebrauchte-veranstaltungstechnik.de mit RC Pro, drei Akkus,
ND-Filtern, Tasche und OVP steht bei 1.700 €. Der Kleinanzeigen-Median (1.750 €, n = 29,
Streuung 1,43, belastbar) deckt sich damit, war aber nicht die Grundlage der Entscheidung.

Kein Umstand erklärt den Preis: kein Absturz, kein Defekt, Zubehör vollständig, Verkäufer
steigt auf die Mavic 4 um. Konto seit 2013, Bewertung 0,97, 14 Bilder, Käuferschutz möglich.
Warnflags aus prompt.md Schritt 2e greifen bei dieser Kategorie nicht; als Risiko ist der
Akkuverschleiß nach vier Jahren und das C1-Klassenlabel vermerkt, als Prüfpunkt zusätzlich
die verbaute 1-TB-SSD mit möglichen Aufnahmen des Vorbesitzers.

## Verworfene Kandidaten

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3476715579 | Cube Mtb Fahrrad | 300 € | `unkenntnis_bonus`, aber weder Modell noch Baujahr genannt, ein Bild. Für ein unbestimmtes Cube-MTB ist kein Marktwert belegbar; Referenz nicht belastbar (Streuung 4,64). Nicht nach Anzeigenqualität verworfen, sondern mangels bestimmbarem Objekt. |
| 3476554968 | Honda Fireblade 1000 | 4.000 € | Baujahr fehlt, die CBR1000RR reicht von 2004 bis 2023 mit Preisen von 4.000 bis 15.000 €. Referenz nicht belastbar (2,83). Ohne Modelljahr kein Marktwert. |
| 3476927039 | Mercedes W201 190er | 2.600 € | 301.216 km, reparierter Frontunfall, Rost, Tieferlegung, HU Februar 2026 abgelaufen. Der Preis erklärt sich selbst. |
| 3454937502 | Gibson LP Special 57 Reissue TV Yellow | 2.550 € | Eigene Prüfung: ein '57 LP Special VOS Reissue ging auf eBay Deutschland für 2.997 US-Dollar (≈ 2.552 €) weg, US-Händler verlangen 3.130–3.598 US-Dollar. Der Angebotspreis liegt auf dem bestätigten Niveau, nicht 20 % darunter. Der Median 4.600 € stammt aus der Suche "Gibson Les Paul 57" und mischt Goldtop- und Black-Beauty-Reissues ein. |
| 3476827083 | Mercruiser/Volvo Penta Lenkung | 1.850 € | Referenz nicht belastbar (5,88), Nischenteil ohne Typbezeichnung, Set unvollständig (zwei Schläuche fehlen). Kein belegbarer Marktwert. |
| 3476670704 | Tudor Black Bay Pro | 2.200 € | Konto sieben Tage alt, englischer Textbaustein ("Bought it two years ago, just wear it four times"), Versand trotz Attribut "Nur Abholung". Betrugsprofil bei hochliquider Ware, kein `unkenntnis_bonus`. Verworfen. |
| 3375969368 | Jaeger LeCoultre Uhr | 1.300 € | Referenz nicht belastbar (5,03), kein Referenzmodell genannt, nur Kaliber K886 und 34 mm. Vintage-JLC ohne Modellbestimmung nicht bewertbar. |
| 3471192328 | Tudor Black Bay 41 Fullset | 2.249 € | Chrono24 führt Fullsets der Ref. 79540 zu 2.390–2.997 €, Einzelvarianten ab rund 2.000 €. 2.249 € liegen höchstens 6 % unter dem belegten Niveau, die 20-%-Schwelle ist nicht erreicht. |
| 3476216336 | Rolex Oysterdate Precision 6694 | 1.999 € | Belegte Händlerpreise 2.410 € bzw. ~3.300 US-Dollar enthalten Händlermarge; im Privatmarkt liegt die 6694 bei 1.500–2.200 €. Kein Abstand von 20 % belegbar. Zusatzbedenken: Bewertung 0,66 und ein "Echtheitszertifikat", das Rolex nicht nachträglich ausstellt. |
| 3475062349 | Tudor Prince Date | 1.899 € | Konto drei Tage alt bei einer 1.899-€-Uhr mit Versandangebot. Verworfen. |
| 3476822088 | Tag Heuer Aquaracer | 850 € | Keine Referenznummer, Batteriewechsel weist auf Quarzwerk hin; gebrauchte Quarz-Aquaracer liegen bei 600–900 €. Preis auf Marktniveau. |
| 3476515699 | Fender Jazz Bass 1978 | 1.750 € | Neu bundiert, Hals angeschliffen, Pickups neu gewickelt, Brücke, Elektronik und Mechaniken getauscht. Umbauten dieser Tiefe senken den Sammlerwert, der Preis ist damit richtig. |
| 3476491670 | Gibson Les Paul Studio 2020 | 1.200 € | Referenz nicht belastbar (2,58); gebrauchte LP Studio liegen bei 900–1.300 €. Preis auf Marktniveau. |
| 3476674397 | Simson Star DDR | 1.350 € | Papiere und Schlüssel fehlen, Verkauf als Bastlerfahrzeug. Nach prompt.md Schritt 2e ohne Zulassungsbescheinigung Teil II richtig bepreist, nicht billig. |
| 3476543389 | JLC Atmos Tischuhr | 650 € | Referenz nicht belastbar (4,89), Kaliber und Baujahr fehlen. Gängige Vintage-Atmos liegen bei 400–900 €, kein Abstand belegbar. |
| 3476581731 | Hilti Kernbohrgerät | 480 € | Referenz nicht belastbar (3,3), und die Anzeige nennt keine Typbezeichnung (DD 130, DD 150-U, DD 200 unterscheiden sich um den Faktor drei). Ohne Modell kein belastbarer Referenzwert; geschätzt wird nicht. |
| 3476343058 | Damen Trekking-Fahrrad | 300 € | Marke "Bike Manufaktur" ohne belegbares Preisniveau, Referenz nicht belastbar (4,01). Der genannte Neupreis von 1.300 € ist eine Verkäuferangabe. Gebrauchte Trekkingräder dieser Klasse liegen bei 250–400 €. |
| 3476746718 | Gibson LP Junior Tribute DC 2019 | 1.100 € | Referenz nicht belastbar (3,56). Gebrauchtniveau 700–950 €; der getauschte Humbucker statt des originalen P90 senkt den Wert zusätzlich. Preis liegt über Markt. |
| 3465629604 | Truma Aventa Comfort | 899 € | Baujahr 2011, Referenz nicht belastbar (3,22). 15 Jahre alte Dachklimaanlagen liegen bei 700–1.000 €. Preis auf Marktniveau. |
| 3476971684 | Apple iPhone 16 128GB | 285 € | Rückseitenglas gebrochen, Sturzmacken, Displaykratzer. Der Preis erklärt sich selbst. |
| 3476186282 | Eames Fiberglass Armchair PACC | 280 € | Referenz nicht belastbar (2,98), belegbare Spanne für gebrauchte Eames-Fiberglasschalen 199–1.389 € je nach Hersteller, Alter und Zustand. Bei "starken Gebrauchsspuren" und nachträglicher Vollpolsterung kein Abstand belegbar. |
| 3458067537 | Specialized Sirrus X 2.0 | 350 € | UVP 725 €, Straßenpreis neu ab 688 €. Für ein drei Monate altes Rad wären 350 € auffällig, aber zwei konkrete Gebrauchtvergleiche desselben Modelljahrs fand ich nicht, und das Konto ist drei Wochen alt ohne Bewertung. Nicht überzeugt, verworfen. |
| 3476581313 | Cube Travel 28 Zoll | 350 € | Baujahr fehlt, Shimano Altus deutet auf Einstiegsklasse. Ohne Modelljahr reicht die Gebrauchtspanne von 250 bis 600 €, kein Abstand belegbar. |
| 3476656447 | MacBook Air 13" 2020 M1 | 380 € | M1 Air 8/256 GB liegt Mitte 2026 bei 350–450 €. Preis auf Marktniveau. |
| 3476899238 | Apple MacBook Air Laptop | 400 € | Weder Baujahr noch Chip, RAM oder SSD genannt; die Beschreibung listet nur Gehäuse und Tastatur. Ohne Modellbestimmung kein Marktwert. |
| 3476790153 | TAG Heuer Damenuhr CL1212 | 650 € | Referenz nicht belastbar (3,2). Quarz-Damenuhren der 2000er-Serie liegen bei 250–450 €, ohne Box und Papiere eher darunter. Preis über Markt. |
| 3476947459 | MacBook Pro M2 13" | 590 € | Gebrauchtniveau 550–700 €. Kein Abstand. |
| 3476314216 | Specialized Mountainbike | 350 € | Kein Modell, kein Baujahr, Bowdenzug defekt. Referenz nicht belastbar (3,43). Nicht bewertbar. |
| 3476706032 | Prophete Trekking E-Bike | 333 € | Verkäufer beschreibt selbst ein beschädigtes Planetengetriebe im Motor. Der Preis erklärt sich selbst. |
| 3476768887 | iPhone 15 Pro Max | 325 € | Kameragehäuse defekt, dazu Konto seit Mai 2026, nur Versand, drei Bilder, zwei Sätze Beschreibung. Defekt erklärt den Preis, das Profil spricht zusätzlich dagegen. |
| 3476687897 | DJI Mavic Pro + More Combo | 250 € | Referenz nicht belastbar (2,85). Die ursprüngliche Mavic Pro von 2016 liegt gebraucht bei 250–350 €. Kein Abstand. |
| 3476619512 | Intex Ultra XTR Frame Pool | 300 € | Komplettset neu bei 600–800 €; für einen gebrauchten Aufstellpool mit Sandfilter ist 300 € Marktniveau, dazu saisonaler Verschleißartikel. |
| 3476348448 | Herren Trekking-Fahrrad | 300 € | Gegenstück zu 3476343058, gleiche Begründung: Referenz nicht belastbar (4,21), Marke ohne belegbares Preisniveau. |
| 3476499778 | Trek Marlin 7 (2018) | 330 € | Acht Jahre altes Einstiegs-MTB, Gebrauchtniveau 300–450 €. Kein Abstand. |
| 3476833512 | LEGO Minas Tirith Figuren | 349 € | Verkauft werden nur die zehn Minifiguren, der Median 567 € stammt aus Anzeigen für komplette Sets. Referenzgruppe nicht vergleichbar, die Ersparnis ist ein Phantom. Die genannte Setnummer 11377 ist zudem keine reguläre LEGO-Nummer. |
| 3476958211 | iPhone 15 Pro 256 GB | 390 € | Kameraglas gesprungen, 1x-Kamera verschwommen. Der Preis erklärt sich selbst. Zudem kein Bild in der Anzeige. |
| 3476260941 | Freischwinger Mart Stam | 180 € | Die Anzeige sagt "im Bauhaus-/Thonet-Stil", also gerade kein Thonet-Original. Referenz nicht belastbar (2,72), Konto einen Tag alt. Für eine Nachbildung ist 180 € kein Fund. |
| 2948649270 | N64 Banjo-Tooie OVP | 150 € | Gewerblicher Händler (retroworld.de UG). Pricecharting ist nach prompt.md als Obergrenze zu lesen, CIB-PAL-Preise liegen bei 100–160 €. Preis auf Marktniveau. |
| 3476334149 | Hilti TE 30 | 220 € | Variante nicht genannt (TE 30, TE 30-AVR, TE 30-A36 unterscheiden sich deutlich). Belegte Auktionszuschläge liegen bei 100–130 €, Händlerangebote bei 189–995 €. Kein belastbarer Referenzwert. |

## Was committet wird

Ein Fund heißt nach prompt.md Schritt 5: `deals.json`, `email_output.html`, `deal_log.csv`
und der `runs`-Ordner gehen direkt nach `main`. `python -m scanner.report` wurde ausgeführt,
die Änderung an `email_output.html` löst den Versand über Resend aus.

# Routine-Lauf 2026-08-05T18:21+02:00 (dritter Lauf des Tages)

- Datenquelle: `candidates.json`, generiert 2026-08-05T16:19:55+02:00 (2 h 01 min alt, Frist 4 h eingehalten)
- Zeitraum des Scans: 2026-08-04T13:18:25+02:00 bis 2026-08-05T13:18:25+02:00
- Gesichtete Anzeigen laut Scan: 503.904
- Kandidaten in der Datei: 40
- Bereits in `deal_log.csv` und deshalb übersprungen: 1 (3476798448, DJI Mavic 3 Cine Premium Combo)
- Inhaltlich geprüft: 39
- **Gemeldete Funde: 0**

## Befund zur Pipeline: kein neuer Bestand

`candidates.json` ist unverändert der Bestand, den der Lauf von 16:31 Uhr schon vollständig
abgearbeitet hat — gleiches `generiert`-Feld (16:19:55), gleiches Zeitfenster, gleiche 40 IDs.
Mit 2 h 01 min liegt die Datei noch innerhalb der Vier-Stunden-Frist aus prompt.md Schritt 1,
ein Abbruch war deshalb nicht angezeigt.

Grund für den fehlenden Nachschub: Der nächste Scan läuft bereits, er ist um 18:25 Uhr
gestartet und war bei Ende dieses Laufs noch `in_progress`. Das Klonen des Repos fiel also
genau in die Lücke zwischen zwei Scans. Die Pipeline ist in Ordnung, es fehlt nur der
Bestand dieses Fensters.

Eine Randbeobachtung zum Cron: Von den Scan-Läufen der letzten beiden Tage wurde genau
einer (05:59 Uhr UTC) per `schedule` ausgelöst, alle übrigen per `workflow_dispatch`.
Der Zwei-Stunden-Takt aus `bc03293` ist frisch, das kann sich noch einlaufen — beim
nächsten Lauf ist zu prüfen, ob der Zeitplan von selbst greift.

Der einzige Unterschied zum Lauf von 16:31 Uhr: Die Mavic 3 steht jetzt in `deal_log.csv` und
fällt korrekt aus der Prüfung. Die Doppelmeldungssperre funktioniert.

## Prüfung

Die 39 verbliebenen Kandidaten habe ich unabhängig neu bewertet, zuerst die mit dem größten
absoluten Abstand und die liquide Ware (Uhren, Apple, Drohnen). Ergebnis deckt sich mit dem
Lauf von 16:31 Uhr; keine Bewertung ist gekippt. Die eigenständig gegengeprüften Marktwerte:

| ID | Titel | Preis | Eigene Marktwertprüfung | Ergebnis |
|---|---|---|---|---|
| 3471192328 | Tudor Black Bay 41 Fullset (Ref. 79540) | 2.249 € | Chrono24: gebrauchte 79540 zwischen 1.643 € und 2.970 €, Einzelangebote 2.400 €, 2.490 €, 2.500 €, 2.623 €. Bestätigtes Niveau rund 2.400 €. | Höchstens 6 % Abstand, 20-%-Schwelle verfehlt. Der Kleinanzeigen-Median von 3.499 € ist die Neupreis-Ecke, nicht der Gebrauchtmarkt. Verworfen. |
| 3476670704 | Tudor Black Bay Pro (M79470) | 2.200 € | Chrono24: Einzelangebote 2.715 $ und 2.998 $, Gesamtspanne 3.046–4.755 $. Bestätigtes Niveau rund 2.800 €. | Abstand rechnerisch knapp über 20 %, aber das Verkäuferprofil trägt nicht: Konto sechs Tage alt, keine Bewertung, zweizeiliger englischer Textbaustein, Attribut "Nur Abholung" bei gleichzeitigem Versandangebot. Kein `unkenntnis_bonus`, exakte Modellbezeichnung, acht Bilder — das ist das Betrugsmuster aus der Leitidee, nicht der schlecht gemachte Verkauf eines Ahnungslosen. Verworfen. |
| 3476216336 | Rolex Oysterdate Precision 6694 | 1.999 € | Händlerangebote 2.395 $ und 3.159 $, ein Vintage-Portfolio-Angebot zu 4.040 €; alle mit Händlermarge und Gewährleistung. Privatmarkt liegt darunter. | Kein Abstand von 20 % zu einem belastbaren Privatmarktwert belegbar. Dazu Bewertung 0,66 und ein "Echtheitszertifikat", das es für die 6694 privat nicht gibt. Verworfen. |
| 3454937502 | Gibson LP Special '57 Reissue Custom Shop TV Yellow (2019) | 2.550 € | GuitarPoint (deutscher Fachhändler) führt dasselbe Modell gebraucht zu 2.936,97 €; Reverb-Angebot USA 3.200 $. Bestätigtes Niveau rund 2.900 € Händler, privat darunter. | 13 % unter dem Händlerpreis, und Privatpreise liegen ohnehin unter Händlerpreisen. 20-%-Schwelle verfehlt. Verworfen. |
| 3476543389 | Jaeger-LeCoultre Atmos Tischuhr | 650 € | Dorotheum-Zuschlag 02/2025: 1.105 €. Aber Chrono24-Privatangebote derselben Bauart ab 745 € und 1.550 €, Händler bis 3.500 €. Spanne zu breit. | Gegen das untere Privatniveau von 745 € ist kein Abstand von 20 % belegbar. Kein belastbarer Referenzwert, deshalb keine Schätzung. Verworfen. |
| 3476334149 | Hilti TE 30 | 220 € | eBay.de gebraucht: 220 €, 350 €, 379,99 €, 399 €. Bestätigte Spanne 220–399 €. | 220 € ist selbst der untere Rand der belegten Spanne, kein Abstand. Zudem nennt die Anzeige die Variante nicht. Verworfen. |
| 3458067537 | Specialized Sirrus X 2.0 | 350 € | Neupreis laut Specialized 799–899 $. Zwei konkrete Gebrauchtangebote desselben Modelljahrs habe ich nicht gefunden: Bicycle Blue Book und buycycle antworten auf Abruf mit 403. | Ohne belegten Gebrauchtwert wird nicht geschätzt. Dazu Konto 22 Tage alt, keine Bewertung, drei Monate altes Rad zu 40 % des Neupreises. Verworfen. |
| 3476186282 | Vitra/Herman Miller Eames Fiberglass Armchair PACC | 280 € | Belegt sind nur Händlerpreise für Fiberglas-*Beistuhl*-Schalen (400–575 €) und 1stDibs-Niveaus; kein Vergleichsangebot für die PACC-Armlehnvariante mit Rollenfuß im Privatmarkt. | Kein belastbarer Referenzwert für genau diese Ausführung, Zustand nur "In Ordnung". Verworfen. |

Die übrigen 31 Kandidaten sind aus denselben Gründen verworfen wie im Protokoll des Laufs
von 16:31 Uhr weiter oben: Referenz nicht belastbar oder Referenzgruppe nicht vergleichbar
(3375969368, 3476491670, 3476746718, 3476790153, 3465629604, 3476581731, 3476827083,
3476343058, 3476348448, 3476314216, 3476581313, 3476715579, 3476260941, 3476833512,
3476899238), Preis erklärt sich selbst durch Defekt, Umbau oder fehlende Papiere
(3476971684, 3476768887, 3476958211, 3476515699, 3476674397, 3476706032, 3476927039),
oder Preis auf Marktniveau ohne 20 % Abstand (3476822088, 3476656447, 3476947459,
3476687897, 3476619512, 3476499778, 2948649270, 3476334149, 3476554968).

Zu 3476554968 (Honda Fireblade 1000, 4.000 €) ausdrücklich: Die Anzeige nennt kein Baujahr.
Die CBR1000RR läuft von 2004 bis 2023 mit Gebrauchtwerten zwischen 4.000 und 15.000 €. Ohne
Modelljahr ist kein Marktwert bestimmbar, der Median (n=10, Streuung 2,83, `belastbar: false`)
trägt nicht. Kein Fund, sondern nicht bewertbar.

## Was committet wird

Kein Fund heißt nach prompt.md Schritt 5: **nur** dieses Laufprotokoll geht nach `main`.
`deals.json`, `email_output.html` und `deal_log.csv` bleiben unverändert,
`python -m scanner.report` wurde nicht ausgeführt, es wird keine Mail ausgelöst.

---

# Routine-Lauf 2026-08-05T20:25+02:00 (vierter Lauf des Tages)

- Datenquelle: `candidates.json`, generiert 2026-08-05T19:59:13+02:00 (26 Minuten alt, Frist 4 h eingehalten)
- Zeitraum des Scans: 2026-08-05T12:25:32+02:00 bis 2026-08-05T18:25:32+02:00
- Gesichtete Anzeigen laut Scan: 211.463
- Kandidaten in der Datei: 69
- Bereits in `deal_log.csv` und deshalb übersprungen: 0
- Inhaltlich geprüft: 69
- **Gemeldete Funde: 4**

Der Scan, der beim letzten Lauf um 18:25 Uhr noch `in_progress` war, ist durchgelaufen und
hat einen komplett neuen Bestand geliefert: 69 Kandidaten statt 40, andere Warengruppen
(erstmals Uhren im oberen Preisband, W126, USM Haller). Keine einzige ID überschneidet sich
mit `deal_log.csv`, die Doppelmeldungssperre hatte nichts zu tun.

Geprüft wurde in der Reihenfolge aus prompt.md: erst der größte absolute Abstand und die
liquide Ware (Uhren, Apple, Drohnen), dann der Rest. Nach vier bestätigten Funden war die
Liste abgearbeitet, die Zehner-Grenze also nicht bindend.

## Funde

| # | ID | Titel | Preis | Bestätigtes Preisniveau | Abstand |
|---|---|---|---|---|---|
| 1 | 3477232373 | Mercedes Benz 300 SE, W126 | 6.500 € | 8.700–11.000 € | 25–41 % |
| 2 | 3477182939 | Sideboard (USM Haller-System) | 480 € | 820 € (Händler gebraucht, gleiche Konfiguration) | 41 % |
| 3 | 3477252817 | Apple MacBook Pro M5 1TB | 1.400 € | 2.195–2.288 € | 36–39 % |
| 4 | 3477248587 | Koga Miyata Full Pro Dura Ace | 360 € | 685–699 € | 47–48 % |

Kein Fund trägt `unkenntnis_bonus`; die Sortierung richtet sich deshalb allein nach der
absoluten Ersparnis. Die beiden Kandidaten mit `unkenntnis_bonus` (3466536786, 3476715579)
sind unten aus sachlichen Gründen verworfen, nicht wegen der Anzeigenqualität.

### Belege im Einzelnen

**1. Mercedes 300 SE W126, 6.500 €.** theclassicvaluer nennt für den W126 300 SE im
Durchschnittszustand 7.589 GBP (≈ 8.700 €); deutsche Inserate für Ende-80er-Exemplare
beginnen bei 11.900 €, ein 1989er mit 322.000 km steht bei 16.900 €. Der Kandidat hat
177.000 km, H-Zulassung, TÜV bis 10/2026, Garagenhaltung, frische Bremsen, Radlager und
Frontscheibe, und der Verkäufer legt Lackkratzer und oberflächige Anrostungen selbst offen.
Auch gegen den untersten Beleg von 8.700 € bleiben 25 % Abstand. classic-analytics selbst
ist nicht frei abrufbar, deshalb der Umweg über theclassicvaluer und laufende Inserate;
der Kleinanzeigen-Median (11.250 €, n = 59) war nicht die Grundlage der Entscheidung.
Kein preiserklärender Umstand: kein Unfall, kein Defekt, für einen 37 Jahre alten W126 ist
177.000 km wenig.

**2. USM Haller Sideboard, 480 €.** Die Konfiguration (eine Klapptür oben, eine Schublade
mit Hängehefter-Halterung unten) entspricht einem 1x2-Sideboard. Zertifizierte USM-Second-Hand-
Partner geben genau diese Größe gebraucht für 820 € ab; der Neupreis eines vergleichbaren
Sideboards liegt bei 1.599 €, und gebrauchte USM-Möbel handeln laut Fachhandel 15–30 % darunter,
also 1.120–1.360 €. Selbst gegen den Händler-Gebrauchtpreis von 820 € sind 480 € noch 41 %
darunter, und das mit offengelegten Gebrauchsspuren und fehlenden Schlüsseln. USM Haller ist
kein Nischenprodukt, sondern eines der wertstabilsten Möbelsysteme überhaupt.

**3. Apple MacBook Pro M5 1TB, 1.400 €.** Attribute nennen 14 Zoll, 24 GB RAM, 1 TB SSD,
die Beschreibung einen M5 mit 10 Kernen und Akku bei 100 %. buyZOXS führt genau diese
Konfiguration refurbished ab 2.288 €, neu kostet sie laut Geizhals ab 2.479 €, der
Kleinanzeigen-Median liegt bei 2.195 € (n = 48, Streuung 1,34). Damit sind 1.400 € rund 36 %
unter dem bestätigten Niveau. Das Modell existiert: Der M5 mit 10-Kern-CPU ist die
Basisvariante des 14-Zoll-MacBook Pro, 24 GB / 1 TB eine reguläre CTO-Option.

**4. Koga Miyata Full Pro Dura Ace, 360 €.** Zwei laufende eBay-Angebote desselben Modells
mit Dura-Ace-Gruppe stehen bei 685 € und 699 €. Der Full Pro war Kogas Topmodell, nicht das
Alltagsrad. Verkäufer seit 2017, Bewertung 0,92, zehn Bilder, Probefahrt angeboten, und die
Beschreibung ist genau so knapp wie bei jemandem, der das Rad nicht als Sammlerstück begreift.

## Verworfene Kandidaten

### Uhren

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 2142985917 | Rolex Submariner Date 16610, Bj. 1991 | 7.995 € | Chrono24: 1991er 16610 ohne Papiere bei 9.134 €, ein Full Set mit Revision 2026 bei 8.600 €. Gegen das bestätigte Niveau von 8.600–9.100 € sind es 7–12 % Abstand, die 20-%-Schwelle ist verfehlt. Der Median von 12.400 € ist die Angebotsecke gewerblicher Anbieter, nicht der erzielbare Preis. Anzeige selbst ist unauffällig (Fachhändler, Revision, ein Jahr Gewährleistung) — nur eben kein Schnäppchen. |
| 3477027929 | Rolex Datejust mit Brillanten | 6.900 € | Referenz nicht belastbar (Streuung 7,71). Keine Referenznummer, kein Modelljahr, keine Größe — der Marktwert ist nicht bestimmbar. Die genannten Brillanten stammen laut Anzeige von einem Londoner Juwelier, also nachträglich gesetzt; Aftermarket-Steine senken den Rolex-Wert. Dazu "100 % echt" als Textbaustein und nur Versand ohne Abholoption. |
| 3477219438 | Rolex Lady Datejust 26, Stahlgold | 3.200 € | Chrono24 führt die Ref. 69173 mit Diamantzifferblatt bei 4.777–4.931 $ (Händler), ein Vintage-Angebot bei 2.700 €. Der Verkäufer nennt selbst ein Band, das "nur noch wenig Spannung" hat — ein ausgelängtes Stahlgold-Jubilé-Band ist die teuerste Einzelposition an dieser Uhr. Der Preis erklärt sich damit selbst; zusätzlich Bewertung 0,41. |
| 3477021334 | Omega Seamaster Diver Chronograph, Ref. 2598.8000, Bj. 1994 | 1.850 € | Chrono24 für genau diese Referenz: 1.899 CHF, 2.270 $, 2.596 CHF, 2.695 CHF, also rund 2.030–2.880 € — alles Händlerangebote mit Gewährleistung. Im Privatmarkt liegt die Uhr darunter, ein Abstand von 20 % ist nicht belegbar. Der Median von 4.000 € stammt aus der Suche "Omega Seamaster Diver" und mischt die aktuelle Keramik-Diver-300M-Serie ein, ein Phantom. Die Anzeige selbst ist die beste im ganzen Bestand (Bewertung 1,00, elf Bilder, exakte Referenz, Versand inklusive) — der Preis ist nur fair, nicht zu niedrig. |
| 3477225076 | Breitling Navitimer B01 Chronograph 43 | 4.555 € | Chrono24 gebraucht: 4.999–6.590 €, typisch 5.500–6.100 €. Gegen den untersten Beleg von 4.999 € sind es 9 % Abstand. 20-%-Schwelle verfehlt. |
| 3476670704 | Tudor Black Bay Pro | 2.200 € | Wie im Lauf von 18:21 Uhr: Konto sechs Tage alt, keine Bewertung, zweizeiliger englischer Textbaustein, exakte Modellbezeichnung ohne Referenznummer, Attribut "Nur Abholung" bei gleichzeitigem Versandangebot. Betrugsmuster bei hochliquider Ware, kein `unkenntnis_bonus`. Zudem mischt der Median ("Tudor Black Bay") BB58, BB GMT und BB Pro. |
| 3475062349 | Tudor Prince Date Ref. 74034 | 1.899 € | Konto zwei Tage alt bei einer 1.899-€-Uhr mit Versandangebot, dazu ein Werbetext in Katalogprosa samt öffentlich genannter Seriennummer. Gebrauchte 74034 liegen bei 1.800–2.500 €, ein Abstand von 20 % ist ohnehin nicht belegbar. |
| 3476822088 | Tag Heuer Aquaracer | 850 € | Unverändert zum Lauf von 16:31 Uhr: keine Referenznummer, der Batteriewechsel weist auf ein Quarzwerk hin, gebrauchte Quarz-Aquaracer liegen bei 600–900 €. Der Median mischt die Automatikmodelle ein. Preis auf Marktniveau. |
| 3375969368 | Jaeger LeCoultre Uhr | 1.300 € | Referenz nicht belastbar (5,03), kein Referenzmodell genannt. Unverändert nicht bewertbar. |
| 3476543389 | Tischuhr Jaeger-LeCoultre (Atmos) | 650 € | Referenz nicht belastbar (4,89), Kaliber und Baujahr fehlen. Gegen das untere Privatniveau von 745 € kein Abstand belegbar. |
| 3476790153 | TAG Heuer Damenuhr | 650 € | Referenz nicht belastbar (3,2). Quarz-Damenuhren dieser Serie liegen bei 250–450 €, der Preis liegt über Markt. |

### Fahrzeuge und Youngtimer

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3477065220 | VW Golf 2 GTI 16v KR | 8.000 € | Die Anzeige nennt spanische Auslieferung und "Deutschpapiere würden gemacht", also noch nicht vorhandene deutsche Papiere, bei gleichzeitig behaupteter H-Zulassung — ein Widerspruch. Nach prompt.md Schritt 2e ist ein Klassiker ohne Zulassungsbescheinigung Teil II nicht billig, sondern richtig bepreist. Belegtes Niveau für einen guten Golf 2 GTI mit H liegt bei rund 10.900 €, der rechnerische Abstand wäre da, der Papierstand trägt ihn nicht. |
| 3477090557 | Bmw e30 zu verkaufen | 6.000 € | Referenz nicht belastbar (3,71) und die Suche "Bmw verkaufen e30" mischt M3, 325i und Cabrios ein. Tatsächlich ein 316er Limousine, abgebrochenes M3-Umbauprojekt. Für den schwächsten E30 als Projektfahrzeug ist 6.000 € kein Fund. |
| 3477204268 | Mercedes W201 190D | 3.800 € | 296.057 km, und der Verkäufer hat den Wagen vor 2,5 Monaten selbst gekauft und dreht ihn weiter. Nur "Gebrauchsspuren" genannt, keine Substanzangaben — das ist Zustand 4, nicht 3, und in dem Band ist 3.800 € richtig bepreist. |
| 3477110107 | W124 230ce Coupe mit H | 3.250 € | Fahrzeugzustand laut Attribut "Beschädigtes Fahrzeug", 300.000 km, steht seit Jahren, Dichtungen fällig, heute abgemeldet. Der Verkäufer schreibt selbst "Absoluter Festpreis deswegen so günstig alles wurde berücksichtigt". Der Preis erklärt sich selbst. |
| 3477056942 | Mercedes 190E W201 2.0 | 3.200 € | Lack matt, Kratzer und Dellen, und eine "leichte Undichtigkeit Windschutzscheibe Fahrerseite" — am W201 der Einstieg in Rost im Scheibenrahmen. 265.000 km. Der Preis erklärt sich selbst. |
| 3476927039 | Mercedes Benz W201 / 190er | 2.600 € | Referenz nicht belastbar (2,74); unverändert zum Lauf von 16:31 Uhr: reparierter Frontunfall, Rost, Tieferlegung, HU abgelaufen. |
| 3477261196 | Mercedes W124 E220 | 5.500 € | Referenz nicht belastbar (3,23), die Suche mischt Coupés und Cabrios der Baureihe ein. Kein eigenständig bestätigter Marktwert, damit kein Fund. |
| 3477249216 | MERCEDES-BENZ W124 | 4.000 € | Referenz nicht belastbar (2,55) und der Titel nennt keine Motorisierung; die W124-Palette reicht vom 200D bis zum 500E. Ohne Modellbestimmung kein Marktwert. |
| 3476554968 | Honda Fireblade 1000 | 4.000 € | Referenz nicht belastbar (2,83), kein Baujahr genannt, die CBR1000RR reicht von 2004 bis 2023 mit 4.000–15.000 €. Dazu Bewertung 0,00 und eine Stellvertretergeschichte ("war die ganze Zeit im Besitz meines Opas"). |
| 3477214691 | Simson Schwalbe KR51/1 | 1.550 € | "Keine Papiere", Sitz- und Lenkschloss fehlen, Benzinhahnhebel abgebrochen, seit 2014 abgemeldet. Ohne Zulassungsbescheinigung Teil II richtig bepreist, nicht billig. Referenz zudem nicht belastbar (2,83). |
| 3476674397 | Simson Star DDR | 1.350 € | Unverändert: Papiere und Schlüssel fehlen, Verkauf als überholungsbedürftiges Projekt. |

### Apple

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3477135411 | apple macbook pro 2025 | 1.100 € | Beschreibung ist wörtlich Apples Marketingtext zum M5-MacBook-Pro, das Attribut sagt "Anderes Modell". Das Basis-M5-MacBook-Pro 14" kostet neu ab 1.449 € (Geizhals), gebraucht 1.250–1.400 €. Bei 1.100 € sind das rund 15 %, die 20-%-Schwelle ist verfehlt. |
| 3477254771 | MacBook Pro M4 | 1.200 € | Höchstens ein Bild, Bewertung 0,53, OVP und Ladekabel fehlen. Ein M4 14" ohne Zubehör liegt bei 1.200–1.400 €, kein belegbarer Abstand. |
| 3477011971 | Apple MacBook Pro 14 (M1 Pro, 16/1TB) | 650 € | Beschreibung besteht aus fünf Wörtern ("M1 Pro, hat nur 51 Zyklen"), nur Versand. Refurbished-M1-Pro-Geräte beginnen bei 799 € mit Garantie, privat liegt das Niveau bei 750–850 €. Gegen diesen Wert sind es unter 20 %; der Median (1.394 €) stammt aus "Apple MacBook Pro 14" und mischt M1 bis M5. |
| 3477232538 | MacBook Air 13 M2 16GB | 480 € | Drei Dellen im Gehäuse, offengelegt. M2 Air 16/256 GB liegt gebraucht bei 550–650 €, mit Dellen darunter. Kein Abstand von 20 %. |
| 3476947459 | MacBook Pro M2 | 590 € | Unverändert: Gebrauchtniveau 550–700 €, kein Abstand. |
| 3476656447 | MacBook Air (2020, M1, 8/256) | 380 € | Unverändert: M1 Air 8/256 GB liegt Mitte 2026 bei 350–450 €, Preis auf Marktniveau. |
| 3476899238 | Apple MacBook Air Laptop | 400 € | Weder Baujahr noch Chip, RAM oder SSD genannt; die Beschreibung ist maschinell klingender Fülltext über Gehäuse und Trackpad. Ohne Modellbestimmung kein Marktwert. |
| 3477182555 | Apple MacBook Pro (13", 2019, Intel, 256 GB) | 350 € | Referenz nicht belastbar (2,81). Intel-Mac am Ende des macOS-Supports — nach prompt.md erklärt ausgelaufener Support den Preis. Beschreibung derselbe Füllbaustein wie bei 3476899238 und 3477231068. |
| 3477231068 | Apple MacBook Pro (13", 2017) | 399 € | Referenz nicht belastbar (2,81). 2017er Intel-Mac ohne macOS-Support, dazu derselbe generische Textbaustein. Preis nicht unter Markt. |
| 3476983653 | MacBook Pro inkl OVP (13", 2020, Intel i5) | 300 € | Referenz nicht belastbar (2,97). Verkäufer nennt selbst "Batterie hält ca. 3 Stunden" und "Service empfohlen". Intel-Mac, auslaufender Support, Akku fällig — der Preis erklärt sich selbst. |
| 3476971684 | Apple iPhone 16 128GB Titan Black | 285 € | Rückseitenglas gebrochen, Sturzmacken, Displaykratzer, alles offengelegt. Rückglastausch ist die teuerste Reparatur am Gerät. Der Preis erklärt sich selbst. |
| 3476768887 | iPhone 15 Pro Max | 325 € | Kameragehäuse defekt, Konto seit Mai 2026 ohne Bewertung, zwei Sätze Beschreibung. Defekt erklärt den Preis. |
| 3476958211 | iPhone 15 Pro 256 GB | 390 € | Kameralinse gesprungen, im Titel offengelegt. Der Preis erklärt sich selbst. |

### Drohnen und Kamera

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3477080971 | DJI Mini 5 Pro Fly More Combo | 585 € | Die Fly More Combo kostet **neu** ab 899 € (Geizhals, mit RC-N3), die RC-2-Variante 1.129 € UVP. Der Median von 905 € ist damit kein Gebrauchtmedian, sondern das Neupreisniveau. Gebraucht liegt die knapp ein Jahr alte Drohne bei 650–750 €, gegen diesen Wert sind 585 € rund 10–20 % — die Schwelle ist nicht sicher erreicht. Die Anzeige selbst ist sauber (Konto seit 2016, Bewertung 1,00, Käuferschutz), nur der Abstand trägt nicht. |
| 3477227101 | Zubehör DJI Mini 3 Pro | 300 € | Verkauft wird ausdrücklich **keine Drohne**, sondern nur Restzubehör nach Drohnenverlust. Der Median (599 €) stammt aus Anzeigen für komplette Sets, die Referenzgruppe ist nicht vergleichbar. Zwei Akkus, Ladestation, RC-N1, ND-Filter und Propeller liegen zusammen bei 200–280 €. Preis auf Marktniveau. |
| 3476687897 | DJI Mavic Pro + More Combo | 250 € | Referenz nicht belastbar (2,85). Die Mavic Pro von 2016 liegt gebraucht bei 250–350 €. Kein Abstand. |

### Musikinstrumente

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3477209872 | Gibson Les Paul Studio 2013 + Grover Tuner | 650 € | Der Verkäufer legt vorbildlich offen, dass das Tronical-Stimmsystem entfernt und durch normale Mechaniken ersetzt wurde, dazu getauschte Potiknobs, Pickuprahmen und Trussrodcover sowie Lackabnutzung. Gebrauchte LP Studio liegen bei 650–950 €, mit Umbauten am unteren Rand — 650 € ist Marktniveau, nicht 20 % darunter. Der Median (2.150 €) stammt aus "Gibson Les Paul 2013" und mischt Standard und Custom ein. |
| 3476985359 | Gibson Les Paul Studio Bj. 1996 gold | 1.350 € | Referenz nicht belastbar (2,93); der Median mischt erneut Standard-Modelle ein. Gebrauchte 90er-LP-Studio liegen bei 900–1.400 €, kein Abstand belegbar. |
| 3477187528 | Gibson Les Paul Special TV Yellow | 1.300 € | Referenz nicht belastbar (2,99). Kein Abstand zum Gebrauchtniveau belegbar. |
| 3476491670 | Gibson Les Paul Studio E-Gitarre mit Koffer | 1.200 € | Referenz nicht belastbar (2,58); gebrauchte LP Studio bei 900–1.300 €. Preis auf Marktniveau. |
| 3476746718 | Gibson LP Junior Tribute DC 2019 | 1.100 € | Referenz nicht belastbar (3,56). Gebrauchtniveau 700–950 €, der getauschte Humbucker statt des originalen P90 senkt den Wert. Preis über Markt. |
| 3476515699 | Fender Jazz Bass 1978 Player Condition | 1.750 € | Neu bundiert, Hals angeschliffen, Pickups neu gewickelt, Brücke, Elektronik, Halsplatte und Mechaniken getauscht. Umbauten dieser Tiefe senken den Sammlerwert, der Preis ist damit richtig. Der Verkäufer nennt den Zustand selbst "Player Condition". |

### Design und Möbel

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3108524087 | Usm Haller Highboard Beige | 835 € | Gewerblicher Anbieter, laut Anzeige "Autorisierter USM Haller Second Hand Partner" mit Ladengeschäft. 835 € für 76 × 37 × 74 cm mit Softclose **ist** der Händler-Gebrauchtpreis, also der Marktwert selbst. Der Median mischt größere Highboards ein. |
| 3108453085 | Original USM Haller Nachttisch beige | 820 € | Ebenfalls zertifizierter USM-Second-Hand-Händler, Preis inklusive MwSt. und Rechnung, Zustand "refurbished". Händlerpreis = Marktwert, kein Abstand. |
| 3477076941 | USM Haller Lowboard, schwarz | 725 € | 125 × 35 × 35 cm ohne Türen und Schubladen — die günstigste USM-Konfiguration, im Gebrauchthandel 700–900 €. 725 € liegt auf Marktniveau. |
| 3477121782 | Bürostuhl Vitra EA119 | 875 € | Referenz nicht belastbar (2,59). Ohne Angabe zu Bezug, Baujahr und Zustand der Alu-Group-Ausführung kein belegbarer Referenzwert. |
| 3477220838 | Walter Knoll Foster 500 Sessel Leder | 1.200 € | Referenz nicht belastbar (2,52). Kein eigenständig bestätigtes Preisniveau für diese Ausführung gefunden, deshalb keine Schätzung. |

### Fahrräder

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3466536786 | Trekking Bike Koga Miyata (`unkenntnis_bonus`) | 300 € | Nicht wegen der Anzeigenqualität verworfen: Referenz nicht belastbar (2,79), und es handelt sich um ein Alltags-Trekkingrad Typ "Roadrunnerlady", kein Sammlerstück wie der Full Pro. Generalüberholt 2024, sehr gut beschrieben — für ein gebrauchtes Damen-Trekkingrad ist 300 € ein normaler, kein auffälliger Preis. |
| 3476715579 | Cube Mtb Fahrrad (`unkenntnis_bonus`) | 300 € | Ebenfalls nicht nach Anzeigenqualität: Referenz nicht belastbar (4,64), und die Anzeige nennt weder Modell noch Baujahr noch Ausstattung. Ohne bestimmbares Objekt kein Marktwert. |
| 3477037692 | Cube Touring Pro Wave | 450 € | Der Median (1.600 €) stammt aus "Cube Touring Pro" und zieht die E-Bike-Variante Touring Hybrid Pro herein — Phantomersparnis. Ein gebrauchtes unmotorisiertes Cube Touring Pro liegt bei 400–600 €, Preis auf Marktniveau. |
| 3458067537 | Specialized Sirrus X 2.0 | 350 € | Unverändert zum Lauf von 18:21 Uhr: Neupreis 688–899 €, aber zwei konkrete Gebrauchtvergleiche desselben Modelljahrs sind nicht auffindbar (Bicycle Blue Book und buycycle antworten mit 403). Ohne Beleg wird nicht geschätzt. |
| 3476581313 | Cube Travel 28 Zoll | 350 € | Baujahr fehlt, Shimano Altus weist auf die Einstiegsklasse. Gebrauchtspanne 250–600 €, kein Abstand belegbar. |
| 3477020056 | 29 Zoll TREK Marlin 6 | 369 € | Baujahr fehlt. Das Marlin 6 ist Treks Einstiegs-MTB, neu ab rund 600 €; gebraucht 300–450 €. Kein Abstand. |
| 3476499778 | Trek Marlin 7 (2018) | 330 € | Unverändert: acht Jahre altes Einstiegs-MTB, Gebrauchtniveau 300–450 €. |
| 3477205818 | Cube Mountainbike | 300 € | Referenz nicht belastbar (5,0), kein Modell, kein Baujahr, drei Zeilen Beschreibung. Nicht bewertbar. |
| 3476990324 | Fischer E-Bike Trekking | 450 € | Zustand laut Attribut nur "In Ordnung", kein Modell, kein Baujahr, keine Akkuangabe. Bei E-Bikes ist der Akku der halbe Wert; ohne Kapazitätsangabe kein belastbarer Referenzwert. |
| 3476706032 | Prophete Trekking E-Bike | 333 € | Fünf Jahre alt, 9.256 km. Prophete-Pedelecs dieser Klasse liegen gebraucht bei 300–450 €, kein Abstand. |

### Übriges

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3476827083 | Mercruiser/Volvo Penta hydraulische Lenkung | 1.850 € | Referenz nicht belastbar (5,88), Nischenteil ohne Typbezeichnung. Kein belegbarer Marktwert. |
| 3476581731 | Hilti Kernbohrgerät | 480 € | Referenz nicht belastbar (3,3), und die Anzeige nennt keine Typbezeichnung — DD 130, DD 150-U und DD 200 unterscheiden sich um den Faktor drei. Ohne Modell kein Referenzwert; geschätzt wird nicht. |
| 3477030711 | Truma Aventa Comfort | 450 € | Referenz nicht belastbar (2,67), kein Baujahr genannt. Gebrauchte Dachklimaanlagen liegen bei 400–1.000 € je nach Alter; ohne Baujahr kein Abstand belegbar. |
| 3465629604 | Klimaanlage Truma Aventa Comfort | 899 € | Referenz nicht belastbar (3,22), Baujahr 2011. 15 Jahre alte Anlagen liegen bei 700–1.000 €. Preis auf Marktniveau. |
| 3476619512 | Intex Ultra XTR Frame Pool | 300 € | Komplettset neu 600–800 €; für einen gebrauchten Aufstellpool mit Sandfilter ist 300 € Marktniveau, dazu ein saisonaler Verschleißartikel. |
| 3476833512 | LEGO 11377 Minas Tirith Figuren | 349 € | Verkauft werden nur Minifiguren, der Median stammt aus Anzeigen für komplette Sets — Referenzgruppe nicht vergleichbar. Die genannte Setnummer 11377 ist zudem keine reguläre LEGO-Nummer. |

## Belegquellen dieses Laufs

- theclassicvaluer.com (Buyer's Guide W126 300 SE) und laufende deutsche Inserate für den W126
- Chrono24 für Submariner 16610, Lady-Datejust 69173, Omega 2598.80, Navitimer B01 43
- buyZOXS und Geizhals für MacBook Pro 14" M5 24 GB / 1 TB, refurbished und neu
- Geizhals und heise Preisvergleich für die DJI Mini 5 Pro Fly More Combo
- eBay.de für zwei Koga Miyata Full Pro mit Dura-Ace-Gruppe
- usm-markt.de, FLEX Büromöbel und prooffice für gebrauchte USM-Haller-Preise (die Händlerseiten
  selbst antworten auf Direktabruf mit 403, die Preise stammen aus den Suchergebnissen)

## Was committet wird

Vier Funde heißt nach prompt.md Schritt 5: `deals.json`, `email_output.html`, `deal_log.csv`
und der `runs`-Ordner gehen direkt nach `main`. `python -m scanner.report` wurde ausgeführt,
die Änderung an `email_output.html` löst den Versand über Resend aus.
