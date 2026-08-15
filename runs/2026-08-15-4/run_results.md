# Lauf 2026-08-15, abends (19:05 Uhr MESZ)

`candidates.json` generiert: 2026-08-15T15:40:06+02:00 (3 h 25 min alt, innerhalb der
Vier-Stunden-Grenze aus Schritt 1). Zeitraum des Sammellaufs: 2026-08-15T09:17:36+02:00 bis
2026-08-15T14:17:36+02:00, gesichtet 171.296 Anzeigen.

- Kandidaten in `candidates.json`: 200
- davon schon in `deal_log.csv`: 0
- Referenz nicht belastbar (`belastbar: false` oder Streuung > 2,5): 47 — Median als nicht
  vorhanden behandelt
- inhaltlich geprüft: 71 (sortiert nach absoluter Ersparnis und nach Liquidität der Ware:
  Uhren, Apple, Drohnen, Konsolen zuerst; die übrigen 129 liegen unter 250 Euro Ersparnis
  oder sind Massenware aus `ebike-rad` und `apple-mobil` ohne belastbaren Abstand)
- `unkenntnis_bonus` in diesem Lauf: 3 Kandidaten, alle `ebike-rad`, alle ohne belastbare
  Referenz und ohne Modellangabe — siehe unten
- gemeldete Funde: 1

## Funde

| Ware | Preis | bestätigter Marktwert | Abstand | Ort |
|---|---|---|---|---|
| [Rennrad BMC Timemachine 01 Road Three, Ultegra Di2, DT Swiss ARC 1400](https://www.kleinanzeigen.de/s-anzeige/rennrad-bmc-timemachine-01-road-three/3485117939-230-2790) | 1.900 € | UVP 6.499–7.999 €; Laufradsatz allein neu 1.957 €; modellgenauer Plattform-Median 4.100 € (n=34) | mindestens −35 %, gegen Median −54 % | Northeim |

Belege: BikeRadar-Test und 99spokes zum Modelljahr 2019–2022 (UVP 6.499 £/€ bzw. 7.999 €),
bike-discount und Geizhals zum DT Swiss ARC 1400 Dicut 62 Carbon-Laufradsatz (1.957 € neu).
Zwei konkrete Gebrauchtangebote desselben Modells konnte ich nicht belegen: buycycle,
Chrono24 und wristler sind in dieser Umgebung vom Egress-Proxy blockiert, und die Websuche
hat für den Gebrauchtmarkt nur Prozentangaben ohne Einzelpreise geliefert. Der bestätigte
Wert stützt sich deshalb auf UVP, den Neupreis eines Einzelbauteils und den belastbaren
modellgenauen Median. Das ist als Untergrenze belastbar: Ein fahrbereites Komplettrad kann
nicht unter dem Gebrauchtwert seines eigenen Laufradsatzes liegen. Der Hinweis steht auch
im `risiko`-Feld der Mail.

Warum kein Selbstläufer-Preis: Der Verkäufer nennt alle Mängel (Lackabplatzer am
Flaschenhalter, Kratzer an Bremshebel, Kurbelarm und Schaltwerk), das Rad ist fahrbereit,
Originalrechnung liegt vor, 8.000 km Laufleistung bei Kauf 2020/21. Nichts davon erklärt
einen Abschlag von mehr als der Hälfte. Konto seit 2014, Bewertung 1,00, 13 Bilder, nur
Abholung. Das rote Signal `Gewerbetext auf Privatprofil` ist ein Fehlalarm auf den üblichen
Privatverkaufs-Haftungsausschluss.

## Verworfene Kandidaten

### Referenzgruppe nicht vergleichbar (Median zählt nicht)

- 3484865386 Apple MacBook Pro M5, 1.222 € — Median 2.249 € stammt aus der Suche
  „MacBook Pro M5 **1TB**", das Gerät hat laut Attributen 512 GB; die 1-TB-SSD ist eine
  extern angeklebte Platte. Dazu Widersprüche (Beschreibung „Silber", Attribut „Grau"),
  Werbetext ohne Seriennummer, Konto jünger als 6 Monate, nur Versand. Phantomersparnis.
- 47 Kandidaten mit `belastbar: false` oder Streuung > 2,5, darunter alle Gibson-Les-Paul-
  Anzeigen (Streuung 2,6–3,6), Walter Knoll und Dieter Knoll Sofas, „Zubehör für
  Fräsmaschine", Vitra Eames Table, Suzuki GSX-R 750 W.

### Marktwert selbst geprüft, Abstand unter 20 Prozent

- 3484418963 Rolex Datejust 31 278240, 6.400 € — Chrono24 zeigt für die Stahlreferenz
  7.000–8.500 €, der Plattform-Median von 14.150 € mischt Gold- und Bicolor-Datejust ein.
  Rund 15 Prozent Abstand, zu wenig.
- 3484932776 Rolex Datejust 41, 7.800 € — Privatmarkt für die 126300 liegt bei 7.650–8.500 €
  (Uhrforum, Chronoto), Händlerpreise ab 10.800 €. Das Angebot liegt auf Privatmarktniveau.
  Zusätzlich ohne Referenznummer, nur zwei Bilder, Versand mit Käuferschutz.
- 3436118902 Jaeger-LeCoultre Grande Reverso Lady Ultra Thin Q3224420, 6.499 € — gebraucht
  laut Chrono24 und Jomashop 3.300–6.500 USD. Das Angebot liegt über Markt, nicht darunter.
- 3484530501 Jaeger-LeCoultre Reverso Lady 260.8.86 Quarz ohne Box und Papiere, 3.390 € —
  der Median 6.290 € stammt aus der Suche „Jaeger LeCoultre Reverso" und enthält
  Herrenmodelle. Für eine Quarz-Damen-Reverso von 2005 ohne Papiere ist 3.390 € Marktpreis.
- 3485011436 Omega Speedmaster Professional 145.022-71, 4.000 € — Fratello nennt für ein
  145.022-71 in sehr gutem Zustand rund 4.600 €. Damit rund 13 Prozent Abstand. Chrono24
  führt zwar Händlerstücke bei 8.500–9.000 USD, das sind aber revidierte, polierte
  Exemplare mit Händlermarge. Dazu: Konto jünger als 30 Tage, kein Abholtermin, nur
  Versand, fehlendes Bandglied. Nicht belegbar auf 20 Prozent.
- 3411664053 Omega Seamaster Aqua Terra Quarz 36 mm, 1.590 € — Händlerangebot inklusive
  Mehrwertsteuer und 12 Monaten Gewährleistung, liegt auf normalem Händlerniveau.
- 3485154243 TAG Heuer Carrera CBM2110, 1.850 € — Gebrauchtangaben streuen zwischen 1.000
  und 7.395 USD, kein belastbares Preisniveau für die konkrete Ausführung ermittelbar.
  Nach der Regel „lieber null Funde" nicht gemeldet.
- 3484706962 Omega Constellation Manhattan 196.0360, 500 € — Preisniveau plausibel bei
  800–1.100 €, ich habe aber nur ein konkretes Vergleichsangebot gefunden (Chrono24,
  1.617 USD, abweichendes Zifferblatt). Nachweis reicht nicht für eine Meldung.
- 3484709853 Steam Deck OLED 1TB, 375 € — Median 699 € ist der Neupreis, nicht der
  Gebrauchtwert. Gegen ein realistisches Gebrauchtniveau um 500 € bleibt zu wenig Abstand
  bei einem drei Tage alten Konto.
- 3355489095 und 3355505343 USM Haller Lowboard je 495 €, 3484970274 USM Haller Lowboard
  550 € (Neupreis 950 €, Kauf 2024), 3484917707 USM Haller weiß 1.300 €, 3484926914,
  3435913489, 2508499789 — durchweg Händler- oder Fachhändlerpreise auf Marktniveau. Der
  Median 1.615 € mischt große geschlossene Sideboards mit kleinen offenen TV-Boards.
- 3484483661 Vitra Soft Pad Chair EA 208, 1.200 € — entspricht dem p25 der Vergleichsgruppe.

### Niedriger Preis erklärt sich von selbst

- 3485175419 Mercedes SL 300 R129, 9.500 € — Verdeck lässt sich nicht öffnen und
  Zentralverriegelung defekt. Eine Verdeckhydraulik am R129 kostet vierstellig; der Preis
  ist damit richtig und nicht zu niedrig.
- 3484708485 BMW E36 328i Touring, 5.500 € — 370.000 km, Rost an mehreren Stellen offen
  dokumentiert.
- 3484853465 BMW E36 323i, 1.999 € — als beschädigt eingetragen, teilgeschweißt, innen
  ausgebaut, ausdrücklich „zum Schlachten oder Fertigstellen".
- 3484725615 BMW E36 320i, 3.100 € — 354.200 km, Rost am Schweller und am Heckblech,
  Kühlkreislauf nach Schaden zu beobachten.
- 3484439676 Mercedes 190 D, 2.900 € — 445.000 km, beschädigt, HU seit Januar 2026
  abgelaufen.
- 3484456637 BMW E36 Cabrio, 5.250 € — Verdeck lässt sich nicht vollständig öffnen.
- 3477389173 BMW 318i E36, 4.000 € — Drift- und Rennstreckenaufbau mit Sperrdifferential,
  scharfer Nockenwelle und freiem Steuergerät: wertmindernde Umbauten nach Schritt 2.
- 3484489206 Mercedes 230E W124, 2.490 € — Streuung 2,58, Referenz zählt nicht; dazu
  Standschaden, Rost, gewerbliches Konto seit 30 Tagen.
- 3484982809 Mercedes 190 2.0, 2.555 € — vier Attribute, keine Angabe zu HU, Rost oder
  Zustand; nicht beurteilbar.
- Alle zwölf Simson- und MZ-Anzeigen (3484632412, 3484905826, 3484690928, 3485196703,
  3484948779, 3485152653, 3484734602, 3485055878, 3484920014, 3485135407, 3484945979) —
  ausnahmslos ohne Papiere, mit festem Motor, zerlegt oder als Bastlerobjekt beschrieben.
  Der Regelfall aus prompt.md: Ohne Papiere ist ein Fahrzeug nicht billig, sondern richtig
  bepreist.
- 3484495450 Suzuki GSX-R 750 W, 1.900 € — undichter Benzinschlauch, als defekt verkauft.
- 3485081752 DJI Mavic 2 Pro, 300 € — tiefentladene Akkus, kein Ladegerät, ungeprüft, als
  Bastlerware ausgeschrieben.
- 3484795590 Suzuki GS 500 E und 3484795268 Vespa Ciao, je 500 € — Scheunenfunde ohne
  Papiere.
- 3484820930 Mazda RX-7, 1.000 € — Papiere verloren, zehn Jahre Standzeit,
  Verkäuferbewertung 0,00.
- 3484798169 Ninebot G2 Max, 495 € — auf 45 km/h getunt, damit ohne gültige
  Betriebserlaubnis für den öffentlichen Verkehr.

### Sonstige

- 3484846086, 3484725298, 3484886779 — die drei Kandidaten mit `unkenntnis_bonus`. Ich habe
  sie bewusst nicht nach Anzeigenqualität abgewertet, aber alle drei haben eine nicht
  belastbare Referenz (Streuung 3,35–3,82) **und** nennen kein konkretes Modell
  („E-Bike Cube", „Cube Rennrad", „Rennrad Cube"). Ohne Modellangabe gibt es keinen
  Marktwert, den ich bestätigen könnte, und geschätzt wird nicht.
- 3484776735 DJI Mavic 2 Pro mit Zubehör, 380 € — gegen ein Gebrauchtniveau um 500 € rund
  24 Prozent, aber nur 120 € absolut und ein generischer, werblicher Anzeigentext ohne
  Seriennummer. Nicht überzeugend genug.
- 3484708667 Wurlitzer Lyric Jukebox, 849 € — Fachhändler pauls50s ruft für eine
  unrestaurierte Lyric von 1979 950 € auf. Kein ausreichender Abstand.
- 3484823439 Altdeutschland-Sammlung, 2.500 € bei Michel-Katalogwert 27.000 € — rund
  9 Prozent des Katalogwerts ist bei Altdeutschland-Nachlässen der normale Handelspreis,
  kein Fund.
- 3484821465 „Kira, Schäferhündin, Notverkauf", 400 € — Lebewesen, kein Handelsgut. Der
  Scanner sollte hier nicht suchen; Hinweis für die Watchlist `notverkaeufe`.

## Anmerkung zur Umgebung

Der Egress-Proxy dieser Umgebung blockiert chrono24.de, buycycle.com und wristler.eu für
den Direktabruf. Preisrecherche war nur über die Websuche und deren Snippets möglich, was
die Beschaffung von zwei konkreten Einzelangeboten je Kandidat spürbar erschwert. Für
Kategorien wie Uhren und Fahrräder, in denen genau diese beiden Seiten die
Referenzquellen sind, senkt das die Trefferquote dieses Laufs.
