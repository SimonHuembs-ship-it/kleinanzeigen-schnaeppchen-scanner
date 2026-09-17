# Lauf 2026-09-17, morgens

- **Zeitpunkt:** 2026-09-17, 07:05 Uhr (05:05 UTC)
- **candidates.json generiert:** 2026-09-17T04:35:26+02:00 (2,5 Stunden alt, innerhalb der Vier-Stunden-Grenze)
- **Zeitraum des Scans:** 2026-09-16T23:25:32+02:00 bis 2026-09-17T04:25:32+02:00
- **Gesichtete Anzeigen:** 9.081
- **Kandidaten in der Datei:** 163
- **Bereits im deal_log.csv:** 0 der 163 (Log enthielt 169 Altmeldungen)
- **Inhaltlich geprüft:** 31 Kandidaten einzeln, der Rest klassenweise verworfen (siehe unten)
- **Gemeldete Funde:** 3

## Funde

| Titel | Preis | Bestätigter Marktwert | Abstand | Ort |
|---|---|---|---|---|
| IWC Pilot's Watch Mark XX, Full-Set 01/2023 | 3.000 € | 3.900–5.200 €, Ø 4.416 € (Chrono24, Ref. IW328201) | 23–42 % | Hamburg Blankenese |
| Steam Deck OLED 1TB, 12/2025, OVP + Rechnung | 350 € | 550 € Valve-Refurb mit Garantie, 680 € neu, 749 € gebraucht eBay.de | 36 % unter dem günstigsten Referenzpreis | Lichtenfels |
| Apple MacBook Air 13,6" M2, 16 GB / 512 GB, OVP | 360 € | 600–800 € (eBay.de 799 €, Back Market refurbished) | 40–55 % | Sagard (Rügen) |

Alle drei tragen `unkenntnis_bonus: false`. Bei allen dreien wurde der Marktwert per
Websuche selbst bestätigt und nicht dem Kleinanzeigen-Median entnommen; bei IWC und
MacBook Air wurde der Median als nicht vergleichbar verworfen und durch
`referenz_hinweis` ersetzt.

## Einzeln geprüft und verworfen

| Kandidat | Preis | Grund |
|---|---|---|
| Porsche 911 Carrera Roadster (996 Cabrio, EZ 07/2000, 83.000 km) | 29.900 € | Median 83.619 € stammt aus der Abfrage „Porsche Carrera Roadster 911" und mischt alle Generationen, also ein Markendurchschnitt, den prompt.md ausdrücklich ausschließt. Der Preis erklärt sich mehrfach selbst: US-Import, Euro 1, Tiptronic, GT3-Heckflügel und GT3-Räder als wertmindernde Umbauten, defekte Öldruckanzeige, fällige Verdeckschließung, Verkauf „im vorhandenen Zustand". |
| Tesla Model 3 Standard Plus RWD, 118.000 km | 15.500 € | `Fahrzeugzustand: Beschädigtes Fahrzeug`, Heckschaden links mit gebrochener Rückleuchte und ausgerastetem Stoßfänger. Unfallschaden ist laut prompt.md ein korrekt bepreistes Angebot. Zusätzlich Verkäuferbewertung 0,29. |
| Mercedes W124 300 TE, 269.000 km | 2.600 € | Nicht fahrbereit, als beschädigtes Fahrzeug eingestellt, alle Flüssigkeiten fällig. Preis erklärt sich selbst. Median zudem nicht belastbar (Streuung 3,33). |
| Oldtimer Mercedes-Benz W124/300 D, 450.200 km, frische HU | 4.350 € | Grenzfall: Das zitierte Sachverständigengutachten von 06/2026 nennt 5.900 €, Marktdaten für gepflegte 300 D liegen bei 6.000–12.000 €. Die 450.200 km sind aber genau die hohe Laufleistung, die prompt.md als selbsterklärenden Grund nennt, und die einzige fahrzeugbezogene Wertangabe stammt aus dem Anzeigentext des Verkäufers selbst. Kein belastbar bestätigter Abstand von 20 %. |
| BMW E36 Cabrio 320i, 330.000 km | 4.800 € | 330.000 km, Beschreibung aus zwei Zeilen ohne Angaben zu Zustand oder Historie, Verkäufer ohne Bewertung. Für die Laufleistung marktgerecht. |
| Honda CB 750 Four K6, EZ 1977 | 2.900 € | „In Einzelteile zerlegt", seit 2010 abgemeldet. Ein zerlegtes Motorrad ist gegenüber fahrbereiten Vergleichsangeboten korrekt bepreist. |
| Honda CBR 1000RR Fireblade Repsol, EZ 2005, 56.000 km | 4.750 € | Median mischt Baujahre 2004 bis 2020. Für eine 2005er mit 56.000 km, Remus-Anlage und Kratzern an der Verkleidung ist der Preis marktgerecht. |
| Ducati Monster 821, 31.650 km | 3.800 € | Eigene Prüfung: vergleichbare Monster 821 mit rund 30.000 km stehen bei 3.750–3.850 €. Das Angebot liegt auf Marktniveau, und Beule, Lackschaden am Tank sowie ein leicht ölendes linkes Standrohr erklären den unteren Rand. |
| Simson Schwalbe KR51/2 | 1.700 € | Median nicht belastbar (Streuung 2,60, n=9). |
| Jaeger-LeCoultre Master Compressor Lady, Ref. 148.8.60 | 3.499 € | Eigene Prüfung: gebrauchte 148.8.60 liegen bei 3.900–4.200 € (Cresus 4.200 €, deutsches Angebot 3.900 €). Abstand nur rund 10–15 %, damit unter der Mindestschwelle. Der Median von 7.674 € mischt Master Control und Reverso ein. |
| Rolex Oyster Perpetual 36, Ref. 116000, Box und Papiere | 5.500 € | Gewerblicher Verkäufer, und gebrauchte OP 36 liegen auf Chrono24 im Bereich 5.500–7.500 €. Kein bestätigter Abstand von 20 %. Median 7.890 € mischt OP 39 und OP 41 ein. |
| Omega Seamaster Chrono-Quartz „Albatross", Ref. ST 396.0839 | 2.450 € | Eigene Prüfung: Dorotheum-Zuschlag 1.430 €, privates Forumsangebot 1.500 €. Das Angebot liegt **über** Markt, nicht darunter. |
| Omega Seamaster De Ville Goldhaube | 895 € | Median nicht belastbar (Streuung 3,49). Vintage-Seamaster mit Goldhaube bewegen sich in genau diesem Bereich. |
| Omega Seamaster Quartz, grundüberholt | 1.000 € | Median nicht belastbar (Streuung 3,67). Vintage-Quarz-Seamaster liegen darunter, kein Fund. |
| DJI Mavic 3 Thermal, Kauf 06/2024, 1 Akku | 3.500 € | Der Median von 5.409 € ist exakt der Neupreis, also kein Gebrauchtmarkt-Median. Eigene Prüfung: eBay.de 4.690 € mit 7 Akkus, Kleinanzeigen 5.835–5.900 €. Um die sechs fehlenden Akkus bereinigt liegt das Vergleichsniveau bei etwa 4.000 €, der Abstand damit unter 20 %. |
| DJI Mavic 2 Enterprise Dual mit Smart Controller, 5 Akkus | 1.699 € | Abstand zum Median nur 31 %, und für die 2019er Baureihe ließ sich kein belastbarer Gebrauchtpreis in Euro finden. Ohne bestätigten Referenzwert kein Fund. |
| DJI Mini 5 Pro Fly More Combo, Kauf 03/2026 | 515 € | Neupreis aktuell 839–899 € (MediaMarkt, Geizhals). Ein gebrauchter Referenzpreis desselben Sets ließ sich nicht belegen, und ein aus dem Neupreis abgeleiteter Wert wäre geschätzt. Kein Fund ohne Beleg. |
| DJI Mini 3 Pro (zwei Anzeigen) | 280 €, 320 € | Absolute Ersparnis unter 270 €, Median aus gemischten Bundles (mit/ohne Fly-More-Combo, RC vs. RC-N1). |
| Leica Elmarit-M 28mm f/2.8, 11809 | 1.250 € | Eigene Prüfung: 30-Tage-Median 1.315 €, gebraucht ab 931 €, neuwertig 1.495 €. Das Angebot liegt auf Median-Niveau. |
| Leica Summicron-R 50mm f/2, Leitz Canada | 500 € | Median nicht belastbar (Streuung 2,92, Abfrage mischt Summicron-M ein). R-Optiken dieser Brennweite liegen genau in diesem Bereich. |
| Apple MacBook Pro 14" M3 Pro, 36 GB | 1.400 € | Marktniveau für ein M3 Pro mit 36 GB und 512 GB. Zusätzlich Versand-only mit Aufschlag für eine „zusätzliche Transportversicherung", ein bekannter Textbaustein. |
| MacBook Air 15,3" M4, 16 GB / 1 TB | 600 € | Konto 26 Tage alt, keine Bewertung, makellose Spezifikationsliste, kein Mangel genannt, Versand angeboten: das Muster einer gut gemachten Betrugsanzeige, nicht das einer schlechten Anzeige eines ehrlichen Verkäufers. |
| MacBook Air 13" M5, 16 GB / 512 GB | 890 € | Verkäufer nennt selbst 1.039,99 € Kaufpreis von 06/2026, Abstand damit nur 14 %. Verkäuferbewertung 0,40. |
| MacBook Pro M1 16" 32 GB, MacBook Pro 16" M1 Pro, MacBook Pro M2 14", MacBook Pro M1 512 GB und neun weitere MacBook-Air-Anzeigen | 300–890 € | Durchweg Abstände unter 35 % gegen Mediane, deren Abfragen Chipgeneration, RAM und SSD nicht trennen (z. B. „Apple MacBook Air" mit n=82). Kein Kandidat mit belastbarer Vergleichsgruppe und ausreichender absoluter Ersparnis. |
| Steam Deck 512 GB OLED | 360 € | Gegenüber dem 512-GB-Gebrauchtniveau von rund 500–660 € kein gesicherter Abstand von 20 %, zumal die 1-TB-Anzeige desselben Laufs besser belegt ist. |
| USM Haller Regal schwarz 2x3 | 825 € | Median aus n=10 mit p25 bei 1.099 €, USM-Preise hängen vollständig von der Konfiguration ab. Kein konfigurationsgenauer Referenzwert belegbar, Text wirkt zudem maschinell erzeugt („Versand ab 2,99" für ein Stahlregal). |
| Vitra Jean Prouvé Fauteuil Direction | 1.100 € | Median nicht belastbar (Streuung 13,29). |
| Cube Kathmandu Bosch (`unkenntnis_bonus: true`) | 1.490 € | Der Bonus ist hier ein Fehlalarm: gewerblicher Verkäufer, Konto ohne Bewertung, generischer Werbetext. Modelljahr, Motorgeneration und Akkukapazität fehlen völlig, ohne die ein Kathmandu Hybrid nicht bewertbar ist. |
| Cube NuRoad Pro (`unkenntnis_bonus: true`) | 550 € | Ehrliche Anzeige mit offengelegten Mängeln, aber Neupreis des NuRoad Pro liegt bei 1.199 €, Modelljahr und Ausstattung fehlen, und im Fließtext steht nur „Cube Nuroad" ohne Pro. Mit defektem Licht und fehlendem Schutzblech kein belegbarer Abstand von 20 %. |
| Riese & Müller Swing, Cube Stereo 140 HPC, Cube Reaction Hybrid und 35 weitere E-Bike- und Fahrrad-Anzeigen | 300–2.000 € | E-Bike-Mediane trennen Akkukapazität (500/625/750 Wh), Motorgeneration und Modelljahr nicht, die drei Faktoren, die den Preis bestimmen. Keine der Anzeigen nennt genug, um eine Vergleichsgruppe zu bilden. |
| 39 Anzeigen der Liste `apple-mobil` (iPhone 12 bis 15 Pro Max) | 150–400 € | Klassenweise verworfen. Die Anzeigen mit dem größten Abstand tragen durchweg einen selbsterklärenden Grund (gesprungene Rückseite, defekte Face ID, unscharfe Frontkamera, Akku 84 %) oder das Betrugsmuster: Konten jünger als 30 Tage, keine Bewertung, nur Versand, Dringlichkeitsformeln wie „muss es schnell loswerden" und „um meine Schulden zu begleichen", teils ohne jedes Foto. Absolute Ersparnis in allen Fällen unter 270 €. |
| Gibson Les Paul Studio und Special (drei Anzeigen) | 1.100–1.250 € | Median nicht belastbar (Streuung 2,80, Abfrage mischt Standard, Studio und Special). |
| Yamaha CS Synthesizer | 300 € | Median nicht belastbar (Streuung 5,00, n=9). |
| Accuphase E-303 | 1.600 € | Kein Kleinanzeigen-Median vorhanden, und für den E-303 ließ sich kein belastbarer Referenzwert belegen. Laut prompt.md dann keine Schätzung. |
| Übrige Kandidaten aus `design-sammeln`, `werkzeug-maschinen`, `musikinstrumente`, `messtechnik`, `camper-marine`, `notverkaeufe`, `konsolen-sweep` | — | Absolute Ersparnis unter 600 € bei gleichzeitig nicht belastbarer oder konfigurationsblinder Vergleichsgruppe. |

## Anmerkungen

- Die Prüfreihenfolge folgte prompt.md: zuerst der größte absolute Abstand, dann die
  liquiden Klassen Drohnen, Uhren, Apple-Geräte und Grafikkarten. Grafikkarten waren
  in diesem Lauf nicht unter den Kandidaten, die Pflicht-Warnflags für RTX 4090,
  Switch 2 und AirPods kamen deshalb nicht zum Tragen.
- Für beide gemeldeten Apple- beziehungsweise Konsolen-Funde greift der Pflichthinweis
  zur Zahlung: beide Verkäufer verlangen bei Versand „PayPal Freunde". Das steht als
  `risiko` in der Mail, die Empfehlung lautet in beiden Fällen Abholung und Barzahlung.
- Für den MacBook-Air-Fund steht zusätzlich der Pflichthinweis für Apple-Geräte in der
  Mail: iCloud-Aktivierungssperre und MDM vor der Übergabe prüfen lassen.
- Die Domains chrono24.de, mpb.com und wristler.eu antworten in dieser Umgebung nicht
  (Egress-Sperre). Alle Preisniveaus stammen deshalb aus Websuchen, die konkrete
  Angebote und Zuschläge nennen, nicht aus Direktabrufen.
