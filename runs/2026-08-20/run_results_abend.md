# Lauf 2026-08-20, abends

- **Zeitpunkt:** 20. August 2026, 19:04 Uhr (MESZ)
- **Datenstand:** `candidates.json` generiert 2026-08-20T15:47:31+02:00, Fenster 09:26 bis 14:26 Uhr,
  rund 3 Stunden 17 Minuten alt — unter der Vier-Stunden-Schwelle aus prompt.md Schritt 1
- **Gesichtet (Stufe 1):** 180.129 Anzeigen in der Statistik, 203 Kandidaten in der Warteschlange
- **Bereits im `deal_log.csv`:** 68 Einträge (u. a. die zwei Meldungen des Morgenlaufs vom 20.08.);
  keine Überschneidung mit den 203 Kandidaten dieses Fensters
- **Inhaltlich geprüft:** die ~40 Kandidaten mit dem größten absoluten Abstand plus die liquiden
  Kategorien Uhren, Drohnen, Apple und Konsolen sowie ausgewählte hoch-priorisierte Fahrräder
- **Gemeldete Funde:** 5

## Funde

| # | Titel | Preis | Bestätigter Marktwert | Abstand | Ort |
|---|---|---|---|---|---|
| 1 | Riese & Müller Load 60 vario, Bj. 01/2022, 6.694 km, Enviolo/Belt, Bosch Cargo Line Gen4, 500 Wh | 2.880 € | 4.000–5.000 € (Upway Load 60 vario Refurbished und ein aktuelles Kleinanzeigen-Angebot Load 60 vario 2022 „−2.740 € vs. UVP 7.839 €" bei 5.099 €) | ~30 % | Wettringen |
| 2 | Specialized Turbo Vado SL 4.0 EQ, 04/2023, 1.800 km, 100 % Akku, Jobrad-Historie | 1.800 € | 2.400–2.800 € (2023er Vado SL 4.0 EQ auf Kleinanzeigen aktuell in dieser Spanne; Neupreis 3.130 € laut Vergleichsangebot Juli 2023) | ~30 % | Rheda-Wiedenbrück |
| 3 | Specialized Turbo Vado SL 4.0 ST, 2022, 1.200 km, Service frisch, immer trocken gelagert | 1.500 € | 2.200–2.600 € (identische ST-2022er auf Kleinanzeigen) | ~35 % | Eurasburg |
| 4 | Tudor Black Bay GMT 79830, Bj. 2019, Wempe-Revision 2025, Garantie bis 2027, Full Set | 2.400 € | 3.100–3.800 € (Chrono24 Full Set 79830RB deutsche Anbieter zwischen 2.616 und 3.190 €, international 3.200–4.600 USD; Trusted Seller Chrono24 ab 3.150 €) | ~25 % | Hamburger Raum |
| 5 | Cube Stereo 120 Race 2022, XT, Rahmen 52, Cassette/Kette/Reifen nahezu neu, 20 Fotos | 1.100 € | 1.550–1.900 € (bike-resale.de 2022er ab 1.539 €, marktplatz.bike ~1.785 €) | ~30 % | Hamburg-Nordost |

Kein Fund trägt `unkenntnis_bonus`; die Reihenfolge ergibt sich daher rein aus der absoluten
Ersparnis. Von den kategoriespezifischen Pflicht-Warnflags aus prompt.md Schritt 2e trifft keines zu:
keine RTX 4090, keine Switch 2 mit Spielen, keine AirPods, kein Apple-Gerät (der Apple-Cluster ist
insgesamt verworfen, siehe unten), kein Tesla, kein Porsche 991/992, kein Klassiker ohne
Zulassungsbescheinigung Teil II, kein NAS mit Platten, keine Threadripper Pro.

## Anmerkung zum R&M Load 60 vario

Der Morgenlauf hat denselben Kandidaten (`3489349287`) mit 17,7 % Abstand knapp unter der Schwelle
verworfen — der damalige Untergrenzwert von 3.500 € kam allerdings aus einem **Load 75 vario** aus
dem Flottenbetrieb und aus einem Upway Load 60 **Touring** (Kette/Umwerfer statt Enviolo/Riemen).
Beide Vergleichspunkte liegen unter dem echten Preisniveau eines Load 60 **vario**:
- Der Vario-Antrieb (Enviolo 380 Nabenschaltung, Gates-Riemen) hat gegenüber dem Touring rund
  700–1.000 € Aufpreis in der Basisausstattung.
- Ein aktuelles Kleinanzeigen-Angebot Load 60 vario 2022 wirbt mit „−2.740 € vs. UVP 7.839 €",
  also 5.099 € Aufruf; das ist die stärkste unmittelbar bestätigbare Marktreferenz für die
  vario-Variante.
- Upway ruft für ein Load 60 **vario** Refurbished aktuell rund 4.000–4.500 € auf.
Gegen 4.000 € Untergrenze bleiben 28 %, gegen 5.100 € rund 43 %. Damit ist der 20-%-Abstand aus
prompt.md sicher gerissen und die Meldung gerechtfertigt.

## Verworfene Kandidaten

### Betrugsprofil überwiegt (Kernmuster: teure Ware, nur Versand, dünne oder widersprüchliche Angaben)

- **Rolex GMT-Master II 116710LN, 8.900 €** (`3489237865`) — dasselbe Muster wie der Morgenlauf
  bereits notiert hat: perfekt aussehendes Datenblatt, aber Seriennummer „F98557" (fünf statt sechs
  Ziffern, Format eines F-Serials 2003/04, während 116710LN erst 2007 erschien), Baujahr „2010"
  passt nicht dazu, „Leider sind die Zertifikaten verloren", nur Versand, Preisverhandlung
  angeboten. Konto seit 2023, keine Verkaufshistorie.
- **Rolex Datejust 41 Ref. 126300 „ohne Zubehör", 5.990 €** (`3488976586`) — Bewertung 0,59,
  Versand ohne Abholung, vier Zeilen Beschreibung, verweist im Text selbst auf 7.700 € Chrono24.
  Wer den Marktpreis kennt und trotzdem 25 % darunter verschickt, ist kein ahnungsloser Verkäufer.
- **Rolex Datejust 41 Wagner Gräfelfing, 8.000 €** (`3488921472`) — schon der Morgenlauf hat
  denselben Verkäufer (ID 62548913) mit zwei wortgleichen „Full Set 2022"-Angeboten zu 8.000/8.500 €
  markiert; die Doppellistung besteht weiter, nur Versand.
- **Rolex Deepsea James Cameron 116660, 9.000 €** (`3489462139`) — 2010er Deepsea ohne Papiere
  liegen auf Chrono24 bei rund 10.000–12.000 €; 9.000 € sind höchstens 15 % Abstand. Konto seit
  2022, keine Bewertung, „Vorabüberweisung" als Zahlungsart genannt.
- **Rolex Datejust 36 mm Ref. 1601, Diamant-Zifferblatt, 4.555 €** (`3489094856`) — nachträglich
  gesetzte Diamanten senken den Wert; „Restgarantie ca. 6 Monate" auf ein 1964er-Modell ergibt
  keinen Sinn.
- **Rolex Two Tone Ref. 15053, 3.500 €** (`3489165484`) — Konto 13 Tage alt, nur Versand,
  Käuferschutz, Beschreibung besteht aus vier Zeilen. Streuung 3,65 macht den Median ohnehin
  unbrauchbar.
- **Rolex Datejust Brillant, 7.000 €** (`3489356993`) — Bewertung 0,25, „bei den A Jewelers London
  gekauft (Juwelier von Stars und Rappern)", Echtheit „vom lokalen Uhrmacher geprüft" — keine
  belastbare Provenienz. Referenz-Streuung 8,53.
- **DJI Mini 5 Pro Fly More Combo, 499 €** (`3489361036`) — dasselbe Cluster wie im Morgenlauf.
  Neupreis-UVP der Fly More Combo mit RC 2 liegt aktuell bei 1.129 €; 499 € sind rund 55 % darunter,
  Versand-only, Bewertung leer.
- **DJI Mini 4 Pro Fly More, 400 €** (`3489208561`) — Konto am 19.08.2026 angelegt, keine
  Bewertung, nur Versand.
- **iPhone-17-Cluster, u. a. 500 € (`3489384924`), 650 € (`3489375420`)** — Neupreis rund 1.200 €,
  aktueller Straßenpreis unbeschadeter Geräte 900–1.000 €; 500 € und 650 € liegen bei 40–55 %
  darunter. Bei Apple gilt zusätzlich prompt.md Schritt 2e: iCloud-Sperre und MDM-Bindung. Kein
  Einzelfall rechtfertigt eine externe Marktwertprüfung, das Muster als Ganzes disqualifiziert es.
- **MacBook Pro M2 13", 749 €** (`3489467846`) — Konto am 20.08.2026 angelegt (an dem Tag noch keine
  drei Tage alt), „Gewerbetext auf Privatprofil", nur Versand.
- **MacBook Air M1 (Mira, 490 €)** (`3489672675`) und **MacBook Air M1 15" (Ali, 530 €)**
  (`3489123485`) — 15"-Air hat „eine Linie führt über das Display", das erklärt den Preis; beim
  M1-13" ist der Aufruf mit 100 % Akku nur rund 20 % unter dem Marktniveau, und der Verkäufer trägt
  „Gewerbetext auf Privatprofil".
- **iPhone 15 Pro 512 GB „beschädigt/voll funktionsfähig", 399 €** (`3489381849`) — Rückseite
  gebrochen, USB-C-Buchse defekt, Bewertung 0,50, „Hoechstens ein Bild". Der niedrige Preis erklärt
  sich aus den Defekten.

### Niedriger Preis erklärt sich von selbst (prompt.md Schritt 2a)

- **Mercedes W126 420 SE H-Zulassung, 8.000 €** (`3489298460`) — Attribut „Beschädigtes Fahrzeug"
  vom Verkäufer selbst gesetzt, dazu „Amaturenbrett 2x eingerissen". Auch wenn der Fließtext
  „nicht beschädigt und fahrbereit" behauptet, gilt für den Wertansatz das Datenfeld: Ein W126 in
  Zustand 3 bewegt sich um 8.000 €, das ist der Marktpreis, nicht darunter. Der Morgenlauf hat
  denselben Kandidaten bereits mit derselben Begründung verworfen.
- **BMW E36 320i Cabrio Spandau, 4.799 €** (`3489417079`) — kein TÜV, seit Jahren abgemeldet,
  Cabrio-Dach nur manuell, Verkleidungsteile lose, Bastlerangebot des Verkäufers selbst („D.h. auch
  der Preis"). Der Median gilt für zugelassene Autos.
- **W124 200, 282.000 km, 2.000 €** (`3489690181`) — Verkäufer nennt Rost, Kratzer, sich lösenden
  Dachhimmel, „bitte kein neues Auto erwarten". Die hohe Laufleistung und Zustandsangaben erklären
  den Preis.
- **W124 230 CE Coupé, 337.000 km, 3.200 €** (`3489723026`) — Attribut „Beschädigtes Fahrzeug",
  „steht seit Jahren nur rum und sieht deswegen auch nicht mehr so schön aus", heute abgemeldet.
  Neues Konto ohne Bewertung.
- **W124 E220 T-Modell, 401.000 km, 4.000 €** (`3489547394`) — „typische Roststellen an den
  Kotflügeln", IR-Fernbedienung defekt; 401.000 km sind der Grund für den Aufruf.
- **Oldtimer Mercedes 190E W201 2,0 Automatik, 2.600 €** (`3489240032`) — „mit Aufbruchschaden
  ersteigert und mit Gebrauchtteilen wieder aufgebaut". Wie im Morgenlauf beschrieben, ist das
  Reparaturbedarf ohne Preisrabatt.
- **BMW E36 318i Cabrio 3. Hand, 7.999 €** (`3489386057`) — gewerbliches Konto seit 04.04.2026
  (137 Tage), Bewertung 0,33. Für ein 188.000-km-318i-Cabrio mit Alpina-Umbau kein Schnäppchen.
- **Yamaha XT 500, teilzerlegt, 2.000 €** (`3489653049`) — Anzeigenlage: „teilzerlegt als
  Bastlerfahrzeug". 2.000 € ist der übliche Bastleraufruf, nicht 20 % darunter.
- **Simson Schwalbe KR51/2 Kirche, 1.450 €** (`3489130409`) und **Simson S51 4-Gang Kirche,
  1.900 €** (`3489634962`) — beide „Papiere müssen neu beantragt werden". Nach der Klassiker-Regel
  aus prompt.md Schritt 2e sind Fahrzeuge ohne Papiere richtig bepreist.
- **Simson S51 Papiere fehlen (Tim), 2.295 €** (`3489383094`) — „Das Moped hat keine Papiere".
  Selber Grund.
- **Vitra Alcove Highback Work Lobby Sessel, 1.195 €** (`3145148357`) — „Die Seitenteile fehlen,
  können bei Vitra nachbestellt werden". Die Nachbestellung kostet vierstellig, deshalb ist der
  niedrige Preis erklärt.
- **Gibson Les Paul Black Beauty 1957 Historic Collection Bj. 1994, 2.990 €** (`3489127419`) —
  fehlendes Zertifikat plus getauschte Kleinteile; der Morgenlauf hat dieselbe Anzeige mit derselben
  Begründung verworfen.

### Marktwert eigenständig geprüft, Abstand reicht nicht

- **Rolex Datejust 41 mit Full Set, 8.000 €** (`3488921472`) — vergleichbare Full-Set-Datejust 41
  von 2022 mit Papieren beginnen auf Chrono24 bei rund 9.500 € (deutscher Markt); 8.000 € sind
  höchstens 16 % Abstand. Zusätzlich s. Betrugsprofil oben (Doppellistung).
- **Tag Heuer Aquaracer 200 Quarz Ref. WBP1110.BA0627, 1.200 €** (`3488902038`) — vergleichbare
  Aquaracer 200 auf Chrono24 zwischen 1.499 und 1.810 USD, Watchcharts-Modellwert Juli 2025 rund
  1.550 USD, deutscher Markt ~1.400–1.600 €. 1.200 € sind 20–25 % darunter, das ist der Grenzfall
  — kombiniert mit Bewertung 0,66 und Versand-only zu wenig für „Ich bin überzeugt".
- **Jaeger-LeCoultre Master Control Réveil Ref. 141.880.972, 4.500 €** (`2905976652`) — gewerblich
  (Andreas Grimmeissen, eigene Website), von 5.750 € reduziert, Box und Papiere. Vergleichbare
  Master-Control-Réveil in Stahl mit Papieren liegen bei Chrono24 zwischen 4.400 und 5.500 €; der
  Preis ist Marktniveau. Wie im Morgenlauf.
- **Rolex Oyster Perpetual 34 (`1901710761`, 3.195 €)** — gewerblicher Uhrenhändler, Uhr von 1971,
  reine Abholung. Der Median mischt neuere OP-34 mit Vintage; Vintage OP-34 aus den 1970ern
  bewegen sich bei 2.500–3.500 €. Kein 20 %-Abstand.
- **Breitling Navitimer Chrono-Matic 1806, 3.250 €** (`3464436331`) — 1972er Navitimer ohne Box und
  Papiere, gewerblicher Verkäufer mit Bewertung 0,73. Vergleichbare Chrono-Matic 1806 ohne Papiere
  bewegen sich bei 3.000–4.500 €; 3.250 € sind kein 20 %-Abstand.
- **Steam Deck 512 GB LCD, 400 €** (`3489181561`) — Steam Deck LCD 512 GB gebraucht liegt bei
  350–500 €. 400 € ist Marktniveau.
- **DJI Mini 5 Pro Fly Combo (Guido), 600 €** (`3489609722`) — 47 % unter UVP 1.129 €, aber Konto
  seit 2013 ohne Verkaufshistorie und Versand-only; das Muster ist zu nah am Betrugscluster für
  „ich bin überzeugt". Selbst wenn die Anzeige echt ist, überschreitet der verbleibende
  Betrugsrisiko-Faktor die Meldeschwelle.
- **Cube Stereo one 77 pro (Niklas), 1.550 €** (`3489336182`) — Fully für nur Versand, keine
  Bewertung, drei-Zeilen-Beschreibung, „Preis nur 44 % des Marktwerts"-Rotsignal. Wie im
  Morgenlauf: der Versandweg passt nicht zur Ware.

### Referenzgruppe nicht belastbar (`belastbar: false` oder Streuung > 2,5)

`3489084196` Minibagger Yanmar SV17-EX (Streuung 2,68), `3489240032` Oldtimer 190E (2,74),
`3489547394` W124 E220 T (2,51), `3489356993` Rolex Datejust Brillant (8,53), `3489165484` Rolex
Two Tone (3,65), `3489084196` Minibagger, `3489357033`/`3489320690`/`3489486127`/`3488893655`
DJI Mavic Pro (3,61 bis 4,29), `3489490785` DJI Mavic Pro Platinum (3,61), `3489321010`/`3489130232`
Vitra AM Chair (3,69/3,50), `3488961034`/`3489108597`/`3489005856` USM Haller Regale (2,53–3,26),
`3488547323` Meuser-Drehmaschine (5,31 nach früherem Lauf), `3489356967` Mafell Erika 85 (3,76),
`3489082405` Technics SL-1200 (13,95), `3488685649` Revox B251 (2,97), sowie die restlichen
Cube-Fahrradanzeigen mit Streuung über 2,5.

### Marktwert nicht bestätigbar

- **Specialized Levo XL Bj. 2020, 5.123 km, 1.500 €** (`3489451099`) — der Verkäufer nennt weder
  Trim (Alloy Comp vs. Comp Carbon vs. Expert/S-Works) noch Motorleistung noch Rahmenmaterial;
  gebrauchte Turbo-Levo-2020er bewegen sich je nach Ausstattung zwischen 1.800 € (Alloy Comp) und
  4.500 € (S-Works Carbon). Ohne bestimmbares Modell kein bestätigter Marktwert.
- **Trek Slash 8, 555 €** (`3489098444`) — Bike verwendet 26"-Laufräder (Hope Pro 2/Flow) und
  Suntour Durolux fest auf 160 mm; das deutet auf 2013–2015, damit ist es außer für gezielte
  Restaurationen kaum wertstabil, konkretes Modelljahr fehlt.
- **BMC Teammachine SLR Five Di2, 1.850 €** (`3489141818`) — der Beschreibungstext bricht nach
  „Antrieb läuft zurz…" ab, Rahmengröße „54 = S" widerspricht der BMC-Größentabelle (54 ist M).
  Referenz nur n=20. Bewertung 0,62.
- **iPhone 15 Pro Bastler, 250 €** (`3489199987`) — als „Für Bastler" verkauft; Marktwert für
  Ersatzteilspender variiert stark.

### Nicht geprüft

Die restlichen rund 130 Kandidaten — überwiegend USM Haller Möbelchen, weitere Fahrräder unter
600 € Ersparnis und kleinere Uhren-/Apple-Cluster-Angebote — liegen unterhalb der
Priorisierungsschwelle aus prompt.md („größter absoluter Abstand zuerst, liquide Ware zuerst") und
wurden nach den fünf bestätigten Funden nicht mehr einzeln geprüft. Sie bleiben in
`candidates.json` und stehen dem nächsten Morgenlauf zur Verfügung, da sie nicht ins
`deal_log.csv` gewandert sind.
