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

---

# Lauf 2026-09-17, abends

- **Zeitpunkt:** 2026-09-17, 19:25 Uhr (17:25 UTC)
- **candidates.json generiert:** 2026-09-17T19:21:41+02:00 (0,1 Stunden alt, innerhalb der Vier-Stunden-Grenze)
- **Zeitraum des Scans:** 2026-09-17T12:52:44+02:00 bis 2026-09-17T17:52:44+02:00
- **Gesichtete Anzeigen:** 175.543
- **Kandidaten in der Datei:** 159
- **Bereits im deal_log.csv:** 0 der 159
- **Inhaltlich geprüft:** 34 Kandidaten einzeln, der Rest klassenweise verworfen
- **Gemeldete Funde:** 3

## Vorlauf: Abbruchgrenze war beim Start überschritten

Beim Start um 19:04 Uhr war `candidates.json` noch der Stand des Sammellaufs von
12:07 Uhr, also 6,96 Stunden alt und damit über der Vier-Stunden-Grenze aus
prompt.md Schritt 1. Der Lauf wäre damit ein Abbruch gewesen — der vierte
Abendabbruch in Folge nach dem 14., 15. und 16. September.

Grund ist kein Fehler im Sammler, sondern seine Laufzeit im Verhältnis zum
Cron-Takt. Die Scan-Action steht auf `0 */4 * * *`, GitHub startet die Läufe
aber verzögert (heute: 08:00-UTC-Lauf um 09:00 gestartet, 12:00-UTC-Lauf um
15:52), und ein Lauf braucht inzwischen 50 bis 90 Minuten (heute 5.336
Sekunden). Um 17:00 UTC, wenn die Abendroutine urteilt, ist der letzte
*fertige* Scan deshalb regelmäßig sieben Stunden alt, während der nächste noch
läuft.

Statt den Lauf sofort abzubrechen, wurde der bereits laufende Scan #238
abgewartet. Er hat um 17:21 UTC committet, `candidates.json` war damit frisch
und die Prüfung konnte regulär stattfinden. Die Vorab-Triage der alten
Warteschlange war nicht verloren: Da `candidates.json` die noch nicht
gemeldeten Kandidaten der letzten 24 Stunden ansammelt, waren 19 der 28 vorab
geprüften Anzeigen auch in der neuen Datei enthalten, darunter alle drei Funde.

**Empfehlung an den Betreiber:** Den Cron der Scan-Action von `0 */4 * * *` auf
etwa `0 1,5,9,13,16 * * *` umstellen oder den 16-UTC-Lauf auf 15:00 UTC
vorziehen. Dann ist vor der Abendroutine ein fertiger Scan vorhanden, statt
dass sie in die Lücke zwischen zwei Läufen fällt.

## Funde

| Titel | Preis | Median (n) | Bestätigtes Marktniveau | Abstand | Ort |
|---|---|---|---|---|---|
| [Rolex Lady Datejust 28](https://www.kleinanzeigen.de/s-anzeige/rolex-lady-datejust-28/3514983875-157-6420) | 6.500 € | 13.500 € (9) | Händler 12.226–15.880 USD für Ref. 279173 Champagner/Jubilé, privat rund 8.000–10.000 € | mind. 20 %, real eher 30–35 % | Neuhausen |
| [DJI Mini 5 Pro Fly More Combo RC 2](https://www.kleinanzeigen.de/s-anzeige/dji-mini-5-pro-fly-more-combo-dji-rc-2/3514635571-245-19313) | 515 € | 899,50 € (36) | Neu 899 € (Geizhals) bis 968 € (heise); Vorgänger Mini 4 Pro FMC gebraucht 750 € | rund 31 % zum nächstliegenden Gebrauchtwert | Glücksburg |
| [Steam Deck OLED Weiß 1TB](https://www.kleinanzeigen.de/s-anzeige/steam-deck-oled-weiss-1tb/3515069230-279-1739) | 320 € | 694,50 € (72) | Neu/OVP 649 € (eBay.de), gebraucht neuwertig 646–749 € | rund 42–51 % | Iserlohn |

Pflicht-Warnflags nach prompt.md Schritt 2e: Keine der gelisteten Kategorien
(RTX 4090, Switch 2, AirPods, Apple-Gerät, Tesla, Porsche 991/992, Klassiker
ohne ZB II, NAS mit Platten, Threadripper Pro) trifft auf die drei Funde zu.
Grafikkarten waren in diesem Lauf gar nicht unter den Kandidaten.

## Verworfene Kandidaten, einzeln geprüft

- **Porsche 911 Carrera Roadster** (3514845928, 29.900 €, nominell 53.719 € unter Median): Größter absoluter Abstand des Laufs und eine reine Phantomersparnis. Der Median aus „Porsche Carrera Roadster 911" mischt Generationen von 993 bis 992; das Fahrzeug ist ein 996 Carrera Cabrio Tiptronic von 07/2000, Euro 1, US-Import. Bestätigter Marktwert: 25.000–32.900 € je nach Zustand, Classic Data Zustand 3 bei 17.500 €. Dazu spinnende Öldruckanzeige, fällige Verdeckschließung, GT3-Flügel und GT3-Räder als wertmindernde Umbauten, Verkauf ausdrücklich „für Schrauber". Der Preis erklärt sich selbst.
- **Jaeger-LeCoultre Master Compressor** (3514328832, 3.499 €, nominell 4.175 € unter Median): Median aus „Jaeger LeCoultre Master" mischt Master Control, Ultra Thin und Geographic. Für die konkrete Ref. 148.8.60 (Lady, 37 mm, Stahl) liegen gebrauchte Angebote auf Chrono24 bei 3.899–4.300 €, der Kollektionseinstieg bei gut 4.000 €. 3.499 € sind rund 13–18 % darunter, kein 20-%-Abstand. Zusätzlich ist das Armband ein Zukauf.
- **DJI Mavic 3 Thermal** (3514707608, 3.500 €, nominell 1.909 € unter Median): Der Median von 5.409 € entspricht exakt dem in der Anzeige genannten Neupreis, die Referenz besteht also aus Neuware. Nur ein Akku statt der üblichen drei der Enterprise-Combo. Ein konkreter Gebrauchtwert ließ sich nicht belegen, damit kein bestätigter 20-%-Abstand.
- **Leica Elmarit-M 28mm 2.8 11809** (3514904191, 1.250 €, kein Median): Eigene Recherche: gebrauchte 11809 (4. Version, E46) liegen bei einem 30-Tage-Median von 1.315 €, Spanne 931–1.833 €, neu 1.495 €. 1.250 € sind rund 5 % unter dem Median — Marktpreis, kein Fund.
- **Rolex Datejust 36mm Fullset** (3515027855, 6.800 €, nominell 2.724 € unter Median): Ref. 16233 aus den 1990ern, Revision überfällig, gewerblicher Verkäufer mit Bewertung 0,39. Der Median aus „Rolex Datejust Fullset 36mm" enthält moderne 126233/126234. 6.800 € entsprechen dem Marktband für eine 16233 in diesem Zustand.
- **Rolex Oyster Perpetual** (3514491921, 5.500 €, nominell 2.390 € unter Median): Ref. 116000 von 07/2016, Händler („PRO"-Profil). Der Preis liegt mit 5.500 € praktisch auf dem p25 der eigenen Referenz (5.200 €) und im Marktband von 5.000–6.500 €. Kein 20-%-Abstand.
- **Honda CB 750 Four K6** (3514503419, 2.900 €, nominell 4.502 € unter Median): „in Einzelteile zerlegt", seit 2010 abgemeldet. Der Median stammt aus fahrbereiten K6. Der Preis erklärt sich selbst.
- **Mercedes-Benz W124/300 Diesel H-Kennzeichen** (3514584888, 4.350 €, nominell 4.649 € unter Median): 450.200 km. Der Median aus „Oldtimer Mercedes Benz W124 300" mischt 300 E, 300 CE und 300 TE, die deutlich über einer 300-D-Limousine liegen. Hohe Laufleistung ist nach prompt.md ein selbsterklärender Preisgrund.
- **BMW 328 coupe e36** (3515292686, 7.000 €, nominell 6.590 € unter Median): Rennfahrzeug mit Fahrgastzelle, Renntank, Schalensitzen und 850er-Bremsanlage, dazu ein auf 328 umgebauter 316. Keine deutsche Straßenzulassung, nur polnische Papiere. Nach prompt.md ohne Zulassungsbescheinigung Teil II richtig bepreist, nicht billig.
- **Ducati Monster 821** (3514810346, 3.800 €, nominell 2.351 € unter Median): Beule und Lackschaden am Tank, linkes Standrohr ölt. Die genannten Mängel erklären den Abstand zum Median von Monster 821 ohne Defekte.
- **Sony PlayStation 5 Pro 2TB** (3515473336, 510 €, nominell 590 € unter Median): Der Anzeigentext verlangt ausdrücklich „PayPal an Freunde bei Versand", also Zahlung ohne Käuferschutz. Nach prompt.md Schritt 2c ein Ausschlussgrund, unabhängig vom Preisabstand.
- **MacBook Air 15,3" M4** (3514430511, 600 €, nominell 549 € unter Median): Konto 26 Tage alt, keine Bewertung, mängelfreie Spec-Sheet-Beschreibung mit Sternchen-Fußnoten, Versand angeboten. Für ein M4-Air 16/1 TB mit Neupreis 1.899 € sind 600 € kein plausibler Ehrlichkeitspreis, sondern das Muster gut gemachter Betrugsanzeigen.
- **Omega Seamaster 36 mm Automatik** (3515285521, 1.100 €, nominell 1.252 € unter Median): Gutes Verkäuferprofil, 19 Bilder, Seriennummer gegen die Unterlagen geprüft. Das Modell ist aber nicht bestimmbar: „Seamaster 36 mm" reicht von einer Vintage-Seamaster (rund 800–1.500 €) bis zur Aqua Terra 36 (gebraucht 2.756–3.892 € auf Chrono24). Ohne belastbaren Referenzwert kein Fund — geschätzt wird nicht.
- **Macbook Pro M5** (3515318358, 1.400 €, nominell 874 € unter Median): 14 Zoll, 16/512 GB. Der Median aus „Macbook Pro M5" mischt M5-Pro- und M5-Max-Konfigurationen. Gegen den Neupreis von rund 1.799 € sind 1.400 € für ein nahezu neues Gerät Marktpreis. Verkäuferbewertung 0,38.
- **MacBook Pro 14" M1 Pro 32GB/1TB** (3515431684, 990 €, nominell 758 € unter Median): Akku bei 87 %, Bewertung 0,50, höchstens ein Bild. 990 € liegen unter dem p25 der eigenen Referenz (1.075 €) und im Marktband von 900–1.200 €. Kein gesicherter 20-%-Abstand.
- **DJI Mavic 3 mit RC-Controller** (3515483688, 635 €, nominell 514 € unter Median): Laut Text eine Mavic 3 **Classic**, nur ein Akku, keine Originalverpackung. Der Median aus „DJI Mavic RC 3" enthält die teurere Mavic 3 und Cine. Für eine Classic mit einem Akku sind 635 € kein bestätigter 20-%-Abstand.
- **MacBook Air 13 Zoll M5** (3514531529, 890 €, nominell 385 € unter Median): Der Verkäufer nennt die eigene Rechnung: gekauft am 02.06.2026 bei OTTO für 1.039,99 €. Gegen diesen belegten Wert sind 890 € rund 14 % Abstand, nicht 20 %.
- **Apple MacBook Pro 14" M3 Pro 36GB** (3514107686, 1.400 €, nominell 750 € unter Median): Marktband für ein M3 Pro 36/512 von 2023 liegt bei 1.300–1.600 €. Zusätzlich Gewerbetext auf Privatprofil und eine dem Käufer aufgebürdete „Transportversicherung".
- **Simson Schwalbe KR51/1k** (3514930683, 1.600 €, nominell 1.437 € unter Median): Unrestaurierter Scheunenfund. Der Median stammt aus fahrbereiten KR51 (Marktband 2.500–3.800 €, im Lauf vom 16.09. bestätigt). Für Scheunenfundzustand ist 1.600 € der richtige Preis.
- **Riese & Müller Cruiser Vario Urban** (3515076101, 1.800 €, nominell 1.724 € unter Median): Der Median aus „Riese Müller Bike" mischt die gesamte Modellpalette bis zu Load und Superdelite. Magura-Felgenbremsen und ein vier Jahre alter 500-Wh-Akku; kein konkreter Vergleichswert für genau dieses Modell bestätigt.
- **Riese & Müller Charger 3** (3514922661, 1.699 €, nominell 1.250 € unter Median): 8.599 km. Der Preis liegt mit 1.699 € praktisch auf dem p25 der eigenen Referenz (1.690 €). Kein Abstand.
- **Yamaha CS Synthesizer** (3514575593, 300 €, nominell 899 € unter Median): Referenz nicht belastbar (Streuung 5,0) und irreführend: 37 Tasten und kompaktes Gehäuse bedeuten einen Yamaha reface CS (neu rund 330–400 €), keine Vintage-CS-Serie. 300 € mit OVP sind Marktpreis.
- **Cube Kathmandu Bosch** (3514870629, 1.490 €, `unkenntnis_bonus`): Nicht wegen der Anzeigenqualität verworfen, sondern weil der Verkäufer gewerblich ist und sich als privat ausgibt („mein gepflegtes Cube E-Bike") und weil der Median aus „Cube Kathmandu Bosch" Modelljahre und Akkugrößen mischt. Ohne Modelljahr und Akkuangabe kein bestätigter Vergleichswert.
- **Cube NuRoad Pro** (3514692515, 550 €, `unkenntnis_bonus`): Ehrliches Profil mit offengelegten Mängeln, aber der Text nennt ein „Cube Nuroad", der Median stammt aus „Cube NuRoad Pro" inklusive Pro-, Race- und SL-Varianten. Für ein Basis-Nuroad mit fehlendem Schutzblech und defektem Licht sind 550 € Marktpreis.
- **Vitra / Eames Tisch** (3515000131, 450 €, `unkenntnis_bonus`): Referenz nicht belastbar (Streuung 2,84) und die Anzeige nennt weder Modell noch Maße („der abgebildete Tisch"). Ohne Modellbestimmung kein Marktwert belegbar.
- **Leica Summicron-R 50mm f/2** (3514442498, 500 €, nominell 599 € unter Median): Referenz nicht belastbar (Streuung 2,92); der Median aus „Leica Summicron 50mm 2" enthält die deutlich teureren Summicron-M. R-Objektive liegen bei 350–600 €, 500 € sind Marktpreis.
- **Accuphase E-303** (3514886224, 1.600 €, kein Median): Der Text nennt selbst „1450 € VB bester Preis auf allen Portalen", der reale Preis liegt also unter der Ausschreibung. Keine Angaben zu Revision oder Seriennummer, Verkäuferkonto 246 Tage alt, Bewertung 0,67. Kein belegbarer Abstand zum Marktband.
- **Notverkauf One Piece EB-01** (3514903462, 700 €, kein Median): Eine versiegelte EB-01-Booster-Box mit 24 Packs für 700 € entspricht rund 29 € pro Pack und liegt damit weit **über** Markt, nicht darunter. Dazu nur ein Bild und „Notverkauf" als Dringlichkeitssignal.
- **iPhone 13 Pro 512 GB** (3514964087, 180 €), **iPhone 15 Pro** (3514278931, 250 €), **iPhone 15 256 GB** (3514956994, 270 €): Alle drei nennen den Preisgrund selbst — gesplittertes Display, defekte Face ID plus beschädigtes Backcover, Display mit Riss und Akku bei 79 %. Selbsterklärender Preis, kein Fund. Beim iPhone 15 Pro zusätzlich ein neun Tage altes Konto.

## Klassenweise verworfen, ohne eigene Marktwertrecherche

- **36 Kandidaten mit `belastbar: false` oder Streuung über 2,5** (14 E-Bikes, 5 Musikinstrumente, 4 Design, 4 Werkzeug/Maschinen, 3 Uhren, 3 MacBooks, je 1 Youngtimer, Leica, Drohne): Nach prompt.md Schritt 2a gilt der Median als nicht vorhanden. Ohne eigenen Beleg kein Fund.
- **24 weitere iPhone-Anzeigen der Watchlist `apple-mobil`** mit p_ratio zwischen 0,50 und 0,70: Massenware, bei der der Median Speicher- und Zustandsvarianten mischt. Preise um die Hälfte des Medians bei Versandangebot sind das bekannte Betrugsmuster; ohne eigenen bestätigten Marktwert nicht gemeldet.
- **Die übrigen MacBook-, E-Bike- und USM-Haller-Kandidaten** unterhalb von 800 € nominellem Abstand: Nach der Prioritätsregel (absoluter Abstand, liquide Ware zuerst) nachrangig, Referenzgruppen mischen Varianten, und ein Median ohne eigene Bestätigung ist kein Beleg.

## Anmerkungen

- Prüfreihenfolge nach prompt.md: zuerst der größte absolute Abstand (Porsche, BMW 328, W124, Rolex), dann die liquiden Klassen Drohnen, Uhren, Apple-Geräte und Grafikkarten. Grafikkarten waren nicht unter den Kandidaten.
- Die Zehn-Funde-Grenze wurde nicht erreicht, es wurde bis zum Ende der priorisierten Liste geprüft.
- chrono24.de und mpb.com antworten in dieser Umgebung nicht auf Direktabruf. Alle Preisniveaus stammen aus Websuchen, die konkrete Angebote nennen, nicht aus Direktabrufen.
