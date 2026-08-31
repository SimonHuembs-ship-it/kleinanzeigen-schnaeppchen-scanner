# Lauf 2026-08-31, 07:10 Uhr (morgens)

- `candidates.json` generiert: 2026-08-31T04:35:09+02:00 (rund 2,5 Stunden alt, innerhalb der Vier-Stunden-Grenze)
- Zeitraum: 2026-08-30T23:20:07+02:00 bis 2026-08-31T04:20:07+02:00
- Gesichtet: 24.382 Anzeigen, 166 Kandidaten in der Liste
- Bereits in `deal_log.csv`: 0 Kandidaten
- Geprüft: 166 Kandidaten gesichtet, davon 31 inhaltlich geprüft (nach absoluter Ersparnis und Liquidität sortiert), 3 gemeldet

## Gemeldete Funde

| Preis | Titel | Bestätigter Marktwert | Abstand | Ort |
|---|---|---|---|---|
| 7.900 € | Mercedes W124 300 CE 24V Automatik, EZ 5/1991, TÜV 9/2027 | Median 12.581 €, mittlerer Bereich 9.500–15.990 € (12gebrauchtwagen.de, C124-Coupé, 83 Angebote, Stand 30.08.2026) | rund 37 % | Hürth |
| 7.000 € | Mercedes 300 SL R129, 2/1991, 190.000 km, H-Zulassung, TÜV 10/2027 | 14.900 € (1992, 252.000 km) und 21.449 € (1991, 122.000 km), günstigstes Gesamtangebot ab 9.500 € | rund 53 % gegen das schlechtere Vergleichsfahrzeug | Schwalmtal |
| 9.800 € | BMW 320i E30 Cabrio, 4/1993, 163.050 km, Oldtimergutachten | 14.700 € (123.700 km) und 15.000 € (317.000 km), realisiert 8–12 % darunter, also rund 13.000 € | rund 25 % | Öhningen |

Alle drei sind Klassiker ohne ausdrückliche Erwähnung der Zulassungsbescheinigung Teil II. Der Prüfpunkt steht bei jedem Fund in der Empfehlung.

## Verworfene Kandidaten

### Marktwert selbst geprüft, Abstand hält nicht

- **3499338994 Porsche 911 Carrera 996, 2002, 138.000 km, 35.900 €** – der Median von 57.330 € stammt aus der Suche „Porsche CARRERA 911“, also einem Markendurchschnitt über alle Baureihen, nicht der exakten Generation. Für den 996 Carrera Facelift nennt 911Finder Zustand 2 mit 24.000 bis 40.000 € (Stand Mai 2026). 35.900 € liegen mitten im Band, kein Abstand.
- **3498751694 MacBook Pro 14 Zoll M5, 16/512 GB, 1.350 €** – Apple Refurbished führt genau diese Konfiguration für 1.439 €, Neupreis 1.599 €. 1.350 € sind rund 6 % unter dem Refurbished-Preis. Der Median von 2.000 € mischte M5-Pro- und M5-Max-Konfigurationen ein.
- **3499276652 und 3498466158 DJI Mini 5 Pro, 500 € und 575 €** – die Mini 5 Pro kostet neu inzwischen 638,99 bis 799 € (Geizhals, billiger.de, August 2026). Der Kleinanzeigen-Median von 899 € bildet veraltete Angebotspreise ab, nicht den Markt. Kein Abstand von 20 Prozent zu einem Gebrauchtwert von rund 450 bis 550 €.
- **3499427355 Rolex Datejust 36 Ref. 16030, 1981, Full Set, 6.100 €** – Ref. 16030 handelt bei rund 4.500 bis 6.000 € (Chrono24: 4.916 $, 5.590 $, 6.100 $; eBay.de 5.603 € mit schwarzem Blatt). 6.100 € liegen am oberen Rand. Der Median von 13.000 € vermengte die moderne Datejust 41 mit der Vintage-Referenz.
- **3499053414 Rolex Datejust 41 ungetragen 2/2024, Full Set, 9.550 €** – vergleichbare ungetragene 126300 mit Jubilee stehen bei 11.300 € und 11.453 € (Chrono24). 9.550 € sind rund 16 Prozent darunter, also ein fairer Privatpreis, aber unter der Schwelle.
- **3499376072 Gibson Les Paul Standard 2012, 1.710 €** – `referenz.streuung` 6,8 und `belastbar: false`, der Median von 3.520 € zählt nicht. Eigene Einordnung des Marktes für eine 2012er Standard: rund 1.900 bis 2.500 €, kein Abstand von 20 Prozent. Zudem gewerblicher Händlerpreis, also selbst der Markt.
- **3499414146 Riese & Müller Charger GT, Baujahr 2023, 12.000 km, 1.900 €** – Upway und Rebike verkaufen aufgearbeitete Charger3 GT touring im Bereich um 2.200 bis 2.800 €, bei 12.000 km Laufleistung und gealtertem Akku ist 1.900 € privat ein normaler Preis. Zusätzlich: nur Versand, keine Abholung für ein E-Bike dieser Klasse.

### Preis erklärt sich von selbst

- **3499282742 BMW e30 318i Coupé, 5.300 €** – kein TÜV, Motor läuft unrund (Verdacht Benzindruckregler), Rost vorhanden, 268.564 km. Projektfahrzeug, korrekt bepreist.
- **3498830887 Mercedes W124 300E, 5.000 €** – Attribut „Beschädigtes Fahrzeug“, 367.000 km, TÜV abgelaufen, Tempomat und Standheizung ohne Funktion, Automatik schaltet ruppig.
- **3498783625 Mercedes w126 300se, 5.000 €** – 490.000 km. Ehrliche, sehr gute Anzeige, aber die Laufleistung erklärt den Preis vollständig.
- **3498415724 Simson Star mit Vape Zündung, 1.500 €** (`unkenntnis_bonus: true`) – „ohne Motor“. Der Median von 3.051 € gilt für vollständige Fahrzeuge. Der Bonus wurde nicht gegen die Anzeigenqualität gewertet, sondern der fehlende Motor gegen den Referenzgegenstand.
- **3499095563 Hanomag Scheunenfund C224, 900 €** – ausdrücklich als Teileträger und Projekt angeboten.
- **3499220854 DJI Mavic 3 Pro, 730 €** – „Defekt nach Absturz“, wird als Ersatzteilspender verkauft.
- **3499220196 MacBook Air M3, 330 €** – Zustand „Defekt“, Tastatur, Touchpad und Akku ohne Funktion.
- **3498916270 DJI Mini 3 Pro, 280 €** – Gimbal-/Pitch-Motor defekt.
- **3498525579 Schlauchboot 320, 500 €** – ohne Motor, „leicht reparaturbedürftig“.

### Zahlung außerhalb der Plattform verlangt

- **3499371954 PlayStation 5 Pro 2 TB, 455 €** – „nur PayPal Freunde oder Barzahlung“, Käuferschutz wird ausdrücklich abgelehnt. Zusammen mit 44 Prozent des Marktwerts das Standardmuster.
- **3499507031 PlayStation 5 Pro, 499 €** – gleiches Muster, „Kein Verkauf hier über das System oder über PayPal Waren“.
- **3498541724 Truma Aventa Compact, neu und originalverpackt, 745 €** – „Versand und PayPal FF bitte! Alles andere funktioniert bei mir nicht.“ Neuware weit unter Marktwert plus erzwungene Zahlung ohne Käuferschutz.

### Referenzgruppe nicht belastbar und kein eigener Beleg gefunden

- **3499460347 Rolex date just, 6.000 €** – `streuung` 3,07, `belastbar: false`. Zusätzlich inhaltlich unstimmig: „Referenznummer: 0684“ ist keine Rolex-Referenz, Diamantlünette und Perlmuttblatt ohne Papierbeleg, ausschließlich Versand, keine Abholung.
- **3499469901 Leica M9-P silber, 4.500 €** – kein Kleinanzeigen-Median vorhanden. Die Anzeige enthält nach eigener Angabe nur Symbolfotos, also keine Bilder des tatsächlichen Objekts. Ohne Bild der konkreten Kamera, ohne Seriennummer und ohne Auslösezahl ist kein belastbares Urteil möglich.
- **3499349304 USM Haller Sideboard, sechs Fächer, 102 × 37,5 × 109,5 cm, 990 €** – vermutlich deutlich unter Markt, aber für genau diese Konfiguration ließen sich keine zwei konkreten Vergleichsangebote finden, nur allgemeine Händlerspannen. Kein bestätigter Marktwert, daher nicht gemeldet.
- **3499515419 Riese & Müller UBN Five touring, 2023, 2.000 km, 1.700 €** – Vergleichsangebote vorhanden (Rebike 2.639 € und 2.689 €, Upway ab 2.049 €), der Abstand wäre ausreichend. Verworfen wegen des Anzeigentexts: Akku, Rahmengröße, Farbe und Laufleistung stehen in Klammern wie unausgefüllte Platzhalter einer Vorlage, das Konto ist ohne Bewertung. Textbaustein-Verdacht wiegt hier schwerer als der rechnerische Abstand.
- **3498773355 MacBook Pro M1 Max 64 GB, 1.200 €** – Beschreibung besteht aus vier Wörtern, Bildschirmgröße nicht genannt, Attribut nennt widersprüchlich „Intel Core i7“. Konfiguration nicht bestimmbar, damit kein Marktwert zuzuordnen.
- **3499411269 Geschäftsauflösung Restposten, 3.000 €** und **3498871060 Haushaltsauflösung, 500 €** – `streuung` 3,45 und 15,43, `belastbar: false`. Konvolute ohne bestimmbaren Einzelwert.
- **3498797347 Jaeger-LeCoultre Atmos Vendome, 2.250 €** – `streuung` 3,5, `belastbar: false`. Vier Bilder, Konto drei Monate alt, kein eigener Beleg für ein Preisniveau über 2.800 € gefunden.
- **USM-Haller- und Design-Posten gewerblicher Anbieter** (3370101211, 3370101545, 3370182294, 3397577403, 3397648899, 3423670628, 3022326483) – Händler mit aufgearbeiteter Ware. Deren Preis ist der Markt, nicht der Abstand zum Markt.

### Sonstige

- **3498689389 TAG Heuer Carrera Calibre 16, 1.499 €** – gewerblicher Anbieter mit Werkstattaufbereitung und Gewährleistung, Händlerpreis.
- **3499139289 TAG Heuer Autavia, 2.450 €** – Median 3.650 €, Abstand 33 Prozent laut Median, aber `p25` liegt bei 2.490 €. Der Autavia-Markt liegt real bei rund 2.300 bis 2.900 €, damit kein Abstand.
- Restliche Kandidaten (Simson-Teile, Cube- und Canyon-Räder, iPhones der Reihen 12 bis 15, Meissen- und KPM-Porzellan, Kleinwerkzeug) mit Ersparnissen unter 500 € nicht einzeln geprüft: nach zehn bestätigten Funden wäre ohnehin Schluss, und die Reihenfolge nach absoluter Ersparnis und Liquidität hat sie nach hinten gestellt.
