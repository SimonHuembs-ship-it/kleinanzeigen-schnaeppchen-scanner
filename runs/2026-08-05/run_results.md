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
