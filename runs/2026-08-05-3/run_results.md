# Routine-Lauf 2026-08-05T12:35+02:00

- Datenquelle: `candidates.json`, generiert 2026-08-05T12:20:44+02:00 (14 Minuten alt, Frist 12 h eingehalten)
- Zeitraum des Scans: 2026-08-04T11:23:06+02:00 bis 2026-08-05T11:23:06+02:00
- Gesichtete Anzeigen laut Scan: 138.932
- Kandidaten in der Datei: 40 (davon eine Dublette: `3469441405` steht unter `vintage-hifi` und `hifi-sweep`)
- Bereits in `deal_log.csv` und deshalb übersprungen: 0 — der neue Scan enthält keinen der sechs bereits gemailten Funde
- Inhaltlich geprüft: 39 eindeutige Kandidaten
- **Gemeldete Funde: 2**

Erster Lauf mit vollständigen Referenzfeldern: `referenz.belastbar` und `referenz.streuung` sind
diesmal in jedem Kandidaten mit Median gesetzt. Von 32 Kandidaten mit Median sind 6 als
`belastbar: false` markiert oder haben eine Streuung über 2,5; deren Median wurde als nicht
vorhanden behandelt.

## Gemeldete Funde

| ID | Titel | Preis | Bestätigtes Preisniveau | Abstand |
|---|---|---|---|---|
| 3471486713 | Leitz Biomed Mikroskop mit vier Leitz-Objektiven | 200 € | Objektiv NPL Fluotar 50/1,00 Oel allein 299 € (mikroskop-online.de) und 369 € (microscopia.de); Leitz-Biomed-Stativ allein 350 € (eBay.de) | über 50 % |
| 3469441405 | Thorens TD 160 Plattenspieler | 165 € | 250 € (Kleinanzeigen, Abholung München), 280 € (Kleinanzeigen), 300 € VB, eBay.de 255–280 € | 34 % gegen den niedrigsten Beleg |

Beide ohne `unkenntnis_bonus`; sortiert nach Höhe des bestätigten Abstands. Der Mikroskop-Kandidat
hat keinen Kleinanzeigen-Median, dort steht `referenz_hinweis` statt `ersparnis_eur`.

Ein Hinweis zur Mail: Beim Thorens zeigt die Karte den Kleinanzeigen-Median von 320 € und damit
155 € Ersparnis. Mein eigener bestätigter Marktwert liegt mit 250–300 € niedriger; die Begründung
im Deal nennt diese Zahlen ausdrücklich, damit die Karte nicht mehr verspricht als belegt ist.

## Verworfene Kandidaten

### Über 1.000 € — externe Marktwertprüfung

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3476864873 | Apple MacBook Pro 14 M5 1TB 16 GB, „wie neu", 6 Ladezyklen | 1.299 € | Neupreis der Konfiguration 1.899 € (Apple DE) bis 2.005 € (Bechtle); Apple-Refurbished liegt rund 15 % darunter, also bei etwa 1.615 €. Gegen dieses Gebrauchtniveau sind 1.299 € nur rund 20 % Abstand, und der Verkäufer ist ein gewerblicher Handyladen (Frankfurt, Zeil 115) mit Differenzbesteuerung, Bewertung 0,72, genau einem Bild und ausschließlich Abholung ohne Käuferschutz. Das ist keine schlechte Anzeige eines ehrlichen Verkäufers, sondern eine handwerklich saubere Händleranzeige mit auffällig niedrigem Preis. Kein sicherer Abstand, verworfen. |
| 3476763017 | Mercedes W124 230TE | 3.200 € | 333.333 km, beginnender Rost an Heckklappe und Kotflügeln, Euro 2, HU nur bis 2026. Referenz nicht belastbar (Streuung 6,22, n=8). AutoScout24 nennt für 230 TE eine Spanne von 6.900–24.900 €, das sind durchweg deutlich bessere Fahrzeuge; classic-analytics Zustand 3 setzt ein mängelfreies, fahrbereites Auto voraus, was auf dieses hier nicht zutrifft. Hohe Laufleistung plus Rost erklären den Preis von selbst. |

### Referenz nicht belastbar oder Produkt nicht bestimmbar

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3461866661 | Leica Summicron-R 1:2/50, Kanada | 450 € | Streuung 7,39, Median verworfen. Eigene Bestätigung: eBay nennt für Summicron-R 50 mm f/2 einen Verkaufstrend von 524 $ (rund 480 €) über 90 Tage, Händlerangebote liegen bei 580–690 €. 450 € sind gegen das Verkaufsniveau nur rund 6 % Abstand. |
| 3474292753 | Leitz Summicron-R 50 mm f/2 | 379 € | Gleiche Referenz: 379 € gegen 480 € Verkaufstrend sind 21 % und damit nur haarscharf über der Schwelle, dazu stammt der Wert aus einer Dollar-Umrechnung. Zu dünn für eine Meldung, verworfen. |
| 3469679301 | Leica Summicron-R 90 mm f/2 | 450 € | Zustand „Defekt", Fungus laut Verkäufer und Fotos. Pilzbefall erklärt den Preis, und eine Reinigung kostet bei diesem Objektiv einen erheblichen Teil des Restwerts. |
| 3449853894 | Wohnungs Auflösung!! | 300 € | Konvolut ohne definierten Inhalt („Coach ausziehbar Fitness Geräte usw Bücher"), Streuung 2,63. Kein Marktwert bestimmbar. |
| 3476702063 | MacBook Air, Intel Core i5, 4 GB RAM, 512 GB | 400 € | Ein Intel-Air mit 4 GB RAM ist ein Gerät von 2015–2017 am Ende des macOS-Supports und liegt gebraucht deutlich unter 400 €. Die Anzeige liegt über Markt, nicht darunter. Konto am selben Tag angelegt. |

### Preis erklärt sich von selbst (Defekt, Schaden, Akku unter 80 %)

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3476461881 | iPhone 13 Pro 256 GB | 150 € | Schwarzer Fleck im Display, Backcover-Glas gesprungen. Zusätzlich fordert der Verkäufer bei Versand „Bankanweisung oder Paypal an Freunde", also Zahlung ohne Käuferschutz. |
| 3476820569 | iPhone 14 Pro 128 GB | 200 € | Sturzschaden, Face ID nur sporadisch, Hauptkamera nur im Nahbereich scharf, vom Verkäufer als Bastlergerät deklariert. |
| 3476808383 | iPhone 14 Pro 256 GB | 260 € | Akku 75 %, Displaykratzer, Konto am selben Tag angelegt, Versand angeboten. |
| 3476752333 | iPhone 13 Pro Max | 250 € | Glasschaden vorne und hinten, Akku 74 %. Rückglastausch ist die teuerste Reparatur am Gerät. |
| 3476732922 | iPhone 13 Pro 128 GB | 200 € | Vom Verkäufer ausdrücklich als defekt verkauft: Fremdakku, Gerät wird warm, Kameraglas gesprungen. |
| 3476850514 | iPhone 15 128 GB | 280 € | Akku 78 %, also unter Apples 80-%-Schwelle, plus Kratzer und Macken. Für ein privat verkauftes iPhone 15 in diesem Zustand ließen sich keine zwei belastbaren Vergleichsangebote finden; Händler-Refurbished-Preise sind wegen Garantie und ≥85 % Akku nicht übertragbar. |
| 3474181096 | iPhone 13 Pro Gold 256 GB | 249 € | Akku 74 %, Tausch rund 100 €. Damit schrumpft der Abstand zum Marktniveau von 330–400 € unter die Schwelle. |
| 3476786222 | iPhone 13 128 GB | 155 € | Akku 71 %, Verkäuferbewertung 0,00. |
| 3476791579 | iPhone 14 128 GB | 220 € | „Ich verkaufe im Auftrag von Dritten (da kein Kleinanzeigen Account)" ist die in prompt.md genannte Stellvertretergeschichte. Ohne Zugriff auf den eigentlichen Eigentümer ist Herkunft und iCloud-Status nicht klärbar. |
| 3476835589 | iPhone 12 Pro 256 GB | 200 € | Akku 77 %. Gegen ein Marktniveau von 250–300 € bleibt kein 20-%-Abstand. |
| 3476810634 | iPhone 13 128 GB | 189 € | Akku 74 %, Kerben am Rahmen. Median 270 €, nach Akkutausch kein Abstand. |
| 3476826557 | iPhone 12 Pro 128 GB | 160 € | Rückseite gesplittert, nur zwei Bilder. |
| 3476733585 / 3476733506 | BMW E36 316i Compact (zwei identische Anzeigen desselben Verkäufers) | je 1.500 € | Dieselben vier Bilder und derselbe Text, aber einmal 230.000 km und einmal 23.000 km im Attribut. Ein Fahrzeug, dessen Laufleistung in zwei parallelen Anzeigen um den Faktor zehn abweicht, ist nicht bewertbar. Zudem nur 31 % unter einem Median von 2.182 €, was für einen 316i Compact mit 230.000 km dem Markt entspricht. |
| 3476726195 | Technics SL-1210 MK2 | 455 € | Der Verkäufer nennt selbst Service-Bedarf von 300–350 € und eine beschädigte Abdeckung. 455 € plus Service liegen bei rund 780 € und damit im Marktband von 690–900 €. Korrekt bepreist. |
| 3476457654 | Nintendo 64 + 3 Controller | 95 € | In Zelda-Farben lackiert, ursprünglich rot. Lackierung senkt den Sammlerwert, der Preis ist richtig. |

### Kein ausreichender Abstand zum bestätigten Marktwert

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3473122789 | Thorens TD 166 | 120 € | Belegtes Preisniveau für den TD 166: Durchschnitt rund 147 €, konkrete Angebote 225 € und 270 € betreffen die höherwertige MkII-Variante. Gegen 147 € sind 120 € nur 18 % Abstand. Knapp verfehlt, verworfen. |
| 3458735634 | Neumann TLM 102 | 380 € | Gebrauchtniveau 400–450 € bei einem Neupreis um 600 €. Dazu ist der Verkäufer als COMMERCIAL geführt, schreibt im Text aber „Privatverkauf" — ein Widerspruch, der den Gewährleistungsausschluss unwirksam macht oder auf ein falsches Profil hindeutet. |
| 3476292315 | Nintendo N64 + 4 Controller | 150 € | pricecharting ist laut prompt.md als Obergrenze zu lesen. Konsole plus vier überholte Controller liegen dort in der Größenordnung des geforderten Preises. Kein Abstand. |
| 3476619579 | Gamecube Wavebird + Empfänger | 70 € | Marktniveau 80–120 €, dazu Verfärbungen und Gebrauchsspuren am linken Stick. Kein 20-%-Abstand. |
| 3476532591 | Nintendo 64 Konsole | 90 € | Konsole mit einem Controller liegt beim Marktniveau. |
| 3476346611 | Nintendo 64 + Controller + Super Mario 64 | 95 € | Marktniveau 100–120 €. Kein Abstand. |
| 3476307384 | Nintendo 64 + Controller + Spiele | 100 € | Ein Originalcontroller, drei No-Name-Controller, Spiele nicht einzeln benannt. Kein bestimmbarer Abstand. |
| 3475360449 | Original Leica Lederbereitschaftstasche M2/M3/M4 | 200 € | Bereitschaftstaschen dieser Baureihe werden im zweistelligen bis niedrig dreistelligen Bereich gehandelt. 200 € liegen eher über als unter Markt. |
| 3453917258 | Zwei Original Technics Headshells | 100 € | 50 € je Headshell entspricht dem üblichen Niveau. Kein Abstand. |

### Kein belastbarer Referenzwert gefunden — kein geschätzter Marktwert

| ID | Titel | Preis | Grund |
|---|---|---|---|
| 3474938006 | Leitz Leica Focotar-2, Teil eines Focomat-Vergrößerers | 200 € | Die Preise für Focotar-Vergrößerungsobjektive streuen von rund 50 € (eBay.de) bis in den dreistelligen Fachhandelsbereich, und die Anzeige lässt offen, welche Variante und wie viel vom Focomat dabei ist („Bei Interesse einfach mal einen Preis vorschlagen"). Kein bestätigter Marktwert, deshalb keine Meldung und keine Schätzung. |
| 3462067539 | Neumann N451 FET 80, 1 Kanal | 125 € | Angebote existieren auf Reverb und eBay, konkrete Europreise ließen sich nicht belegen. Ohne bestätigtes Preisniveau keine Meldung. |
| 3423977545 | Gefell Neumann N 692 Vorverstärker | 130 € | „Funktion kann mangels Ausgangskabel nicht getestet werden." Ungeprüftes Gerät, der Preis erklärt sich damit selbst, und ein Marktwert für ein ungetestetes Exemplar ist nicht bestimmbar. |
| 3314993448 | Refox DFE-35 Reparaturstation | 100 € | Werkstattzubehör ohne belegbares Gebrauchtniveau. Das Signal `tippfehler_im_titel: "refox"` ist ein Fehlalarm der Tippfehler-Erkennung, „Refox" ist der korrekte Herstellername. |
| 3464310020 | Refox RF20 | 139 € | Titel nennt RF20, der Beschreibungstext durchgehend RP30. Zwei verschiedene Modelle in einer Anzeige, das Produkt ist nicht bestimmbar. Auch hier ist `tippfehler_im_titel: "refox"` ein Fehlalarm. |

## Befund zur Pipeline

Die Tippfehler-Erkennung aus `scanner/typos.py` markiert „Refox" als Tippfehler und hebt damit zwei
Anzeigen eines real existierenden Herstellers in den Kandidatenbestand. Beide Male ist der
`unkenntnis_bonus` nicht gesetzt, der Schaden bleibt also auf zwei zusätzliche Kandidaten begrenzt.
Falls die Markenliste erweitert wird, gehört „Refox" auf die Ausnahmeliste.

Der Kandidat `3469441405` steht doppelt in der Datei, einmal über `vintage-hifi` und einmal über
`hifi-sweep`. Bei der Auswertung wurde er einmal gezählt; für die Meldung wurde er dedupliziert.

## Belegquellen dieses Laufs

- microscopia.de und mikroskop-online.de für das Objektiv NPL Fluotar 50/1,00 Oel
- picclick.de / eBay.de für das Leitz-Biomed-Stativ
- hifishark.com, kleinanzeigen.de und eBay.de für Thorens TD 160 und TD 166
- eBay-Verkaufstrend und Leica Classic Store für Summicron-R 50 mm f/2
- apple.com/de, Bechtle und Apple Refurbished für MacBook Pro 14 M5 16 GB / 1 TB
- AutoScout24 und classic.com für Mercedes-Benz 230 TE

## Commit

Zwei Funde, also nach prompt.md Schritt 5: `deals.json`, `email_output.html`, `deal_log.csv` und der
`runs/`-Ordner werden committet und direkt nach `main` gepusht. Der Push löst
`.github/workflows/send-email.yml` aus.
