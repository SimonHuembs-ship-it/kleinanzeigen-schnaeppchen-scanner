# Lauf 2026-08-20, morgens

- **Zeitpunkt:** 20. August 2026, 07:05 Uhr (MESZ)
- **Datenstand:** `candidates.json` generiert 2026-08-20T06:40:34+02:00, Fenster 01:27 bis 06:27 Uhr,
  25 Minuten alt, also frisch (Schwelle prompt.md Schritt 1: vier Stunden)
- **Gesichtet (Stufe 1):** 23.731 Anzeigen im letzten Fenster, 201 Kandidaten in der Warteschlange
- **Bereits im `deal_log.csv`:** 67 Einträge, keine Überschneidung mit den 201 Kandidaten
- **Inhaltlich geprüft:** die 60 Kandidaten mit dem größten absoluten Abstand plus die vollständigen
  liquiden Kategorien (Uhren, Drohnen, Apple, Konsolen, Foto/Leica)
- **Gemeldete Funde:** 2

## Funde

| # | Titel | Preis | Bestätigter Marktwert | Abstand | Ort |
|---|---|---|---|---|---|
| 1 | Honda CRX del Sol ESi, 1996, 183.000 km, HU 08/2028 | 2.300 € | 8.000–10.000 € (AutoScout24: 1995er/205.000 km für 8.000 €, 1996er/168.000 km für 10.000 €; Classic-Trader 1996er ESi 8.900 €) | über 70 % | Darmstadt |
| 2 | USM Haller Sideboard 150 × 35 × 74 cm, 2×2, 4 Klappen, bicolor | 950 € | 1.295–1.425 € gebraucht (Vedera, identisches Format, schwarz bzw. mittelgrau) | ca. 27 % | Schwedeneck |

Kein Fund trägt `unkenntnis_bonus`; die Reihenfolge ergibt sich daher rein aus der absoluten
Ersparnis. Von den kategoriespezifischen Pflicht-Warnflags aus prompt.md Schritt 2e trifft keines zu
(keine RTX 4090, keine Switch 2, keine AirPods, kein Apple-Gerät, kein Tesla, kein Porsche, kein NAS,
kein Threadripper Pro). Die Klassiker-Regel „ohne Zulassungsbescheinigung Teil II ist ein Fahrzeug
richtig bepreist" greift beim del Sol nicht: das Auto ist zugelassen und hat frische HU bis 08/2028.

## Warum nur zwei Funde

Die Warteschlange bestand zu weit über der Hälfte aus zwei Betrugsclustern (35 iPhones, 12 MacBooks,
jeweils bei 50 bis 65 Prozent des Median, überwiegend Versand) und aus Fahrrad- und Uhrenanzeigen,
bei denen sich das konkrete Modell nicht bestimmen ließ. Erschwerend kam hinzu, dass die
Egress-Policy dieser Session den Direktabruf fast aller Preisportale blockiert (mpb.com, vedera.de,
usm-markt.de, upway.de, audio-markt.de, bikemarkt.mtb-news.de, autobild.de, classic.leica-camera.com
antworten mit `EGRESS_BLOCKED`). Belastbare Vergleichspreise ließen sich daher nur über
Suchergebnis-Snippets gewinnen. Wo dabei keine zwei konkreten Vergleichsangebote zusammenkamen, ist
der Kandidat verworfen und nicht geschätzt worden — siehe die Rubrik „Marktwert nicht bestätigbar".

## Verworfene Kandidaten

### Marktwert eigenständig geprüft, Abstand reicht nicht

- **Accuphase DG-38 Digital Voicing Equalizer, 1.750 €** (`3489362787`) — `referenz: null`, also
  selbst recherchiert: audio-markt.de führt ein DG-38 in Top-Zustand mit komplettem Zubehör für
  1.700 € (März 2026) und eines für 1.900 € (Juli 2025). Das hier angebotene Gerät ist „kein
  PIA-Gerät" und es fehlen zwei Slotabdeckungen. 1.750 € liegen damit auf Marktniveau, nicht darunter.
- **Leica Summicron-M 50 mm f/2 Rigid Typ II Chrom, 1964, Nr. 2052740, 1.250 €** (`3489354969`) —
  `referenz: null`, selbst recherchiert: der Leica Classic Store führt ein Rigid von 1964/65 für
  1.200 €, ein privat gehandeltes Rigid Version II Chrom von 1960 ging im DSLR-Forum für 980 € weg.
  US-Händler liegen bei 1.150 bis 1.595 USD. Der Aufruf liegt am oberen Rand des deutschen Marktes,
  nicht 20 Prozent darunter. Die Anzeige selbst ist tadellos (Seriennummer, Leica-Inspektion,
  Konto seit 2014) — es ist schlicht kein Schnäppchen.
- **Gibson Les Paul Black Beauty 1957 Historic Collection, Bj. 1994, 2.990 €** (`3489127419`) —
  vergleichbare '57 Historic Reissue Black Beauty stehen auf eBay.de bei rund 3.450 bis 3.590 €.
  Das sind 13 bis 17 Prozent Abstand, zu wenig. Dazu fehlt das Zertifikat, und Sattel und Stegeinlage
  sind getauscht.
- **Riese & Müller Load 60 vario, Bj. 2022, 6.694 km, 2.880 €** (`3489349287`) — Neupreis 2022:
  7.049 €. Bestätigtes Gebrauchtniveau: Upway ruft für ein Load 60 Touring von 2022 4.249 € auf,
  Feine Räder für ein Load 75 vario aus dem Flottenbetrieb mit dreijährigem Wartungsnachweis
  3.500 € inkl. MwSt. Gegen die untere bestätigte Grenze von 3.500 € bleiben 17,7 Prozent — unter der
  Schwelle. Ein zweites konkretes Vergleichsangebot für die vario-Variante des Load 60 war nicht zu
  finden. Knapp verfehlt, nicht gemeldet.
- **Rolex Datejust 41 mm Ref. 126300, 5.990 €** (`3488976586`) — größter Nominalabstand der ganzen
  Warteschlange (7.000 €), trotzdem verworfen. Gebrauchte 126300 beginnen auf Chrono24 bei 7.999 €,
  der Verkäufer nennt in der Anzeige selbst 7.700 €. 5.990 € wären knapp 25 Prozent Abstand — aber
  die Anzeige besteht aus vier Zeilen ohne Seriennummer, ohne Referenzangabe und ohne Baujahr, der
  Verkäufer hat eine Bewertung von 0,59 und bietet ausschließlich Versand an. Wer den Chrono24-Preis
  kennt und trotzdem 25 Prozent darunter verschickt, ist kein ahnungsloser Verkäufer.
- **Rolex Datejust 126300 blau/römisch, Full Set ungetragen, 9.500 €** (`3488670486`) — Abholung,
  elf Bilder, plausible Beschreibung. Chrono24 führt ungetragene 126300 bei rund 10.700 €, der
  Verkäufer nennt selbst 11.500 € Händleraufruf. Höchstens 12 bis 17 Prozent Abstand.
- **Rolex Datejust 16233, 36 mm, 5.500 €** (`2876152064`) — gewerblicher Uhrenhändler, Uhr gewartet
  und mit Gangwerten, Band mit Stretch. Für eine servicierte Stahl/Gold-16233 ist das der übliche
  Händlerpreis. Der Median von 8.500 € („Rolex Datejust 36mm") mischt Stahlmodelle mit Vollgold.
- **Jaeger-LeCoultre Master Control Réveil Ref. 141.880.972, 4.500 €** (`2905976652`) — gewerblich,
  von 5.750 € reduziert, mit Box und Papieren. Der Preis liegt im normalen Händlerkorridor für eine
  Stahl-Memovox von 1998, nicht 20 Prozent darunter.
- **Steam Deck OLED 1 TB, 450 €** (`3488859341`) — Neupreis 679 €, gebrauchte OLED-1-TB-Geräte liegen
  bei 500 bis 560 €. 450 € sind rund 15 Prozent Abstand, dazu nur Versand.
- **USM Haller Kommode weiß, 77 × 74 × 37 cm, mit Klappe, 580 €** (`3488961034`) und
  **USM Haller Regal weiß, 77 × 65 × 37 cm, 480 €** (`3489151886`) — Vedera verkauft das kleinste
  gebrauchte USM-Sideboard für 480 €. Beide Aufrufe liegen auf oder über diesem Niveau.
- **USM Haller Bürotische 175 × 75 cm, 250 € pro Stück** (`3488640592`) — gegen refurbishte
  Händlerware (USM-Markt 550 €, Refurbished ab 474 €) wären das 47 bis 55 Prozent, gegen das
  Privatniveau von 299 bis 350 € aber nur 16 bis 28 Prozent. `belastbar: false` (Streuung 3,41).
  Der maßgebliche Vergleich ist der private, damit kein Fund.
- **Technics SL-1200 MK2, 700 €** (`3489082405`) — Originalzustand, funktionsfähig, kein Clubeinsatz.
  Genau das ist der Marktpreis für ein gutes MK2. Referenz ohnehin nicht belastbar (Streuung 13,95).

### Niedriger Preis erklärt sich von selbst

- **Honda CB 750 Four K2, Umbau zum Scrambler, 4.800 €** (`3488696916`) — sehr sorgfältig
  dokumentierter Umbau (gekürztes Rahmenheck, Alutank in Einzelanfertigung, fremder Krümmer, fremdes
  Hinterrad). Der Median von 7.987 € gilt für originale K2. Umbauten, die den Sammlerwert senken,
  sind nach prompt.md Schritt 2a ein selbsterklärender Grund.
- **Mercedes-Benz W124 250 D, 3.300 €** (`3488719830`) — TÜV seit Mai 2025 abgelaufen, Fahrzeug
  abgemeldet, Dachhimmel ausgebaut, 201.000 km. Der Median von 6.210 € gilt für zugelassene Autos.
- **BMW E36 318i Cabrio, 286.000 km, 2.500 €** (`3488786967`) — vom Verkäufer ausdrücklich „als
  defekt an Schrauber oder Export als Ersatzteilspender" angeboten.
- **Mercedes W201 190E 2,6, 2.999 €** (`3488544877`) — das Auto ist zerlegt und steht in der Rubrik
  „Ersatz- & Reparaturteile". Verkäuferbewertung 0,40.
- **Oldtimer Mercedes 190E W201 2,0 Automatik, 2.600 €** (`3489240032`) — vom Verkäufer als
  Aufbruchschaden ersteigert und mit Gebrauchtteilen wieder aufgebaut; Türpappen, Himmel und
  Aufbruchspuren sind offen benannt. `belastbar: false` (Streuung 2,74).
- **Mercedes W126 420 SE, H-Zulassung, 8.000 €** (`3489298460`) — Classic Data führt den 420 SE mit
  rund 10.900 € in Zustand 2 und 2.300 € in Zustand 4; ein Wagen mit zweifach eingerissenem
  Armaturenbrett und im Datenfeld hinterlegtem „Beschädigtes Fahrzeug" liegt in Zustand 3. Nach
  prompt.md Schritt 2d ist Zustand 3 der Maßstab, und dagegen ist der Aufruf nicht 20 Prozent zu
  niedrig, sondern eher zu hoch.
- **BMW E36 318i Cabrio, 3. Hand, 7.999 €** (`3489386057`) — gewerblicher Verkäufer, Konto 137 Tage
  alt, Bewertung 0,33. Für ein 188.000-km-318i-Cabrio mit Alpina-Umbau ist der Aufruf marktüblich.
- **Simson Schwalbe KR51/2, 1.450 €** (`3489130409`) — „Papiere müssen neu beantragt werden". Nach
  der Klassiker-Regel aus prompt.md Schritt 2e ist ein Fahrzeug ohne Papiere nicht billig, sondern
  richtig bepreist.
- **Gibson Les Paul Junior DC Bass Shortscale, 850 €** (`3489332452`) — Originalelektronik nicht mehr
  vorhanden, fremder Pickup, angefertigtes Pickguard, andere Brücke. Die Mods erklären den Preis.
- **Cube Stereo one 77 pro, 1.550 €** (`3489336182`), **Trek Slash 8, 2 × 555 €**
  (`3488853759`, `3489098444`), **Steiger Trekking, 769 €** (`3488622569`) — beim Cube passt der
  Versandweg nicht zur Ware (Fully „nur Versand ab 0,49 €", keine Abholung, Verkäufer ohne Bewertung),
  das Trek ist laut Anzeige „vermutlich aus 2015" mit 10-fach Deore, und „Steiger" ist eine
  No-Name-Marke, deren Ankerpreis von 1.699 € der Händler selbst gesetzt hat.

### Betrugsprofil überwiegt

- **Rolex GMT-Master II Ref. 116710LN, 8.900 €** (`3489237865`) — die Anzeige ist ein perfektes
  Datenblatt bis hin zu Kaliber 3186 und Cerachrom-Lünette, aber die Angaben widersprechen sich: die
  genannte Seriennummer „F98557" hat das Format eines Rolex-F-Serials (2003/2004), während die
  Referenz 116710LN erst 2007 eingeführt wurde und die Anzeige „Baujahr 2010" behauptet. Dazu fünf
  statt sechs Ziffern, „Zertifikate verloren", nur Versand und „Über den Preis kann man reden ….".
  Genau das Muster aus prompt.md: handwerklich gut gemacht, inhaltlich nicht haltbar.
- **Rolex Datejust 41, 2 × identischer Anzeigentext, 8.000 € und 8.500 €**
  (`3488921472`, `3488715142`) — derselbe Verkäufer (ID 62548913, Gräfelfing) bietet zweimal
  dasselbe „Full Set" von 2022 mit wortgleichem Text zu zwei verschiedenen Preisen an, beide nur
  Versand. Doppellistung desselben Objekts zu Streupreisen ist ein bekanntes Muster.
- **Rolex Datejust 36 mm Ref. 1601 mit Diamant-Zifferblatt, 4.555 €** (`3489094856`) — nachträglich
  gesetzte Diamanten senken bei Rolex den Wert, statt ihn zu heben; „Restgarantie ca. 6 Monate" auf
  eine Uhr von 1964 ergibt keinen Sinn. Der Median von 7.199 € gilt für Serienzifferblätter.
- **Rolex „Oyster" mit Handaufzug, 3.500 €** (`3488866704`) — der Median von 8.500 € stammt aus der
  Suchanfrage „Rolex Oyster" und mischt Oyster Perpetual, Submariner und Datejust ein. Eine Vintage
  Oyster Precision mit Handaufzug liegt bei 1.500 bis 3.000 €; der Aufruf ist eher zu hoch.
- **DJI Mavic 3 Thermal, 3.000 €** (`3488542428`) — Konto am 27.07.2026 angelegt, also 24 Tage alt,
  ausschließlich Versand, bei einem Gerät, das sich zum vollen Preis binnen Tagen verkauft. Die
  konkreten Angaben (Kaufdatum, C2-Zertifizierung, Rehkitzrettung) sind gut gemacht — genau deshalb
  ist die Kombination aus frischem Konto und Versandzwang bei vierstelligem Betrag nicht tragbar.
- **DJI Mini 5 Pro Fly More Combo mit Care Refresh, 499 €** (`3489361036`) und **DJI Mini 4 Pro Fly
  More, 400 €** (`3489208561`, Konto am 19.08.2026 angelegt) — aktuelle Topmodelle bei rund der
  Hälfte des Median, nur Versand. Dasselbe Cluster wie in den Vorläufen.
- **iPhone-Cluster, 35 Anzeigen zwischen 150 und 650 €** (`3489384924` u. a.) — iPhone 12 bis 17
  durchgehend bei 45 bis 62 Prozent des Median, überwiegend Versand, kurze Texte, auffallend viele
  Konten aus 2026. Darunter zwei iPhone 17 (aktuelles Modell) für 500 und 650 €. Bei Apple-Geräten
  in dieser Preislage sind iCloud-Sperre, MDM-Bindung und Hehlerware die Regel; kein Einzelfall
  rechtfertigte eine externe Marktwertprüfung.
- **MacBook-Cluster, 12 Anzeigen zwischen 300 und 530 €** (`3489241490` u. a.) — gleiches Muster,
  darunter „Apple macbook pro .top letzte version neue" für 335 €.

### Referenzgruppe nicht belastbar (`belastbar: false` oder Streuung > 2,5)

`3489084196` Minibagger Yanmar SV17-EX (Streuung 2,68; zusätzlich Nettopreis zzgl. MwSt., also
14.280 € brutto — vergleichbare SV17 von 2012 mit 3.800 bis 5.000 h liegen bei rund 21.900 € netto,
das Angebot ist plausibel bepreist, aber nicht mit zwei Vergleichsangeboten belegbar),
`3489356993` Rolex Datejust Brillant (8,53), `3489165484` Rolex Two Tone (3,65; Konto 13 Tage alt),
`3488594485` Omega Seamaster (3,46), `3448218195` BMW R100GS (12,24), `3488566956` BMC Teammachine
SLR (2,91), `3489356967` Mafell Erika 85 (3,76), `3488928257` Drehmaschine mit Zubehör (5,31),
`3489230800` BMC Twostroke (2,56), `3488893382` Truma Combi 6 (5,69), `3489320690` und `3488893655`
DJI Mavic Pro (3,95 bzw. 4,29), `3489102247` und `3489241490` MacBook Pro (3,22 bzw. 2,62),
`3488685649` Revox B251 (2,97), `3489082405` Technics SL-1200 (13,95), `3488822277` Meissen
Porzellan (4,23), `3488797152` Thonet Esszimmerstühle (9,37), `3488806282` KPM Kurland (3,00),
die USM-Regale `3489151886` (2,53), `3488625026` (2,60), `3463693376` (2,55),
`3488569517` (2,65), `3488640592` (3,41), `3489005856` (3,26), `3068395048` Vitra AM Chair (3,69),
`3489130232` Bürostuhl Vitra (3,50), `3068142640` Thonet S33 (2,83), `3488617094` Thonet Stuhl (3,75)
sowie die übrigen Cube-Fahrradanzeigen mit Streuung über 2,5.

### Marktwert nicht bestätigbar

- **Drehmaschine Meuser, 1.000 €** (`3488547323`) — der einzige Kandidat der Warteschlange mit
  `unkenntnis_bonus`, deshalb zuerst geprüft und ausdrücklich **nicht** wegen der dünnen Anzeige
  abgewertet. Die Anzeige nennt aber weder Modell noch Spitzenweite noch Umlaufdurchmesser, und genau
  daran hängt bei Meuser-Drehmaschinen der Preis: die Baureihen reichen von 700 bis 3.800 mm
  Spitzenweite. Ein Vergleichsangebot (Spitzenweite 1.000 mm, Drehdurchmesser 410 mm) steht bei
  2.500 € netto, ein anderes ist nicht bepreist. Ohne Modellangabe ist kein belastbarer Referenzwert
  zu bilden — nach prompt.md wird nicht geschätzt, sondern verworfen. **Empfehlung für den nächsten
  Lauf:** taucht dieser Kandidat wieder auf und ist in der Zwischenzeit eine Modellangabe ergänzt
  worden, lohnt die erneute Prüfung.
- **Specialized Stumpjumper EVO, 799 €** (`3488865495`) — Anzeigenprofil eines ehrlichen Verkäufers
  (Konto seit 2013, Bewertung 0,96, Abholung, offen genannte Laufleistung und Upgrades). Es fehlen
  aber Modelljahr, Rahmenmaterial und Antriebsgruppe; „S5, 29 Zoll, 150/140 mm, 14,9 kg" passt weder
  eindeutig auf ein EVO (160/150 mm) noch auf ein bestimmtes Baujahr. Die auffindbaren Vergleiche
  (S-Works-EVO-Rahmen in S5 für 1.500 bis 1.800 €) betreffen ein anderes Produkt. Ohne bestimmbares
  Modell kein bestätigter Marktwert.
- **Mafell Erika 85, 850 €** (`3489356967`) — die aktuelle Erika 85 Ec kostet neu 3.927 €, ältere
  Erika-85-Generationen liegen deutlich darunter. Die einzeilige Anzeige nennt die Generation nicht.
  Dazu: gewerbliches Konto seit Februar 2026 ohne jede Bewertung. Nicht bestätigbar.
- **USM Haller Regal schwarz-weiß, 228 × 110/75 × 36 cm, 699 €** (`3489108597`) — von der
  Materialmenge her das interessanteste USM-Angebot der Liste, aber für die stufenförmige
  Sonderkonfiguration ließ sich kein konkretes Vergleichsangebot mit Preis finden, und USM-Werte
  hängen vollständig an der Konfiguration. Zusätzlich steht das Möbel in Bremerhaven, während die
  Anzeige in Hamburg läuft.
- **Cassina Maralunga, 1.800 €** (`3488620158`) — die Anzeige besteht ausschließlich aus
  Rechtsformeln; weder Sitzzahl noch Bezugsart noch Baujahr sind genannt. Gebrauchte Maralunga
  bewegen sich je nach Größe und Bezug zwischen 950 € (konkretes 2-Sitzer-Angebot auf PicClick) und
  3.500 €. Ohne Konfiguration kein zuordenbarer Vergleichswert.
- **Canyon Endurace Rennrad Ultegra, 580 €** (`3489211978`) — weder Modelljahr noch Rahmengeneration
  (AL/CF/CF SL) genannt; die Ultegra-Angabe allein reicht nicht, um ein Vergleichsangebot zuzuordnen.
- **Thorens Rumpelmesskoppler, 350 €** (`3489362829`) und **Thorens Plattenstabilisator, 100 €**
  (`3489362770`) — `referenz: null`. Für ein Werkstatt-Messwerkzeug dieser Seltenheit ist keine
  belastbare Preisreihe zu finden; hifishark führt das Teil nicht.
- **Haushaltsauflösung Nagold, 2.800 €** (`3489390687`) und **Piaggio ZIP 125 Notverkauf, 1.300 €**
  (`3489375530`) — beide aus der Watchlist `notverkaeufe` mit `referenz: null`. Zu einem
  Paketangebot aus Wohnwand, Boxspringbett, Waschmaschine und Fernseher lässt sich kein
  Einzelmarktwert bilden; beim ZIP fehlt jede Angabe zu Baujahr und Laufleistung.

### Nicht geprüft

Die restlichen rund 100 Kandidaten — überwiegend Fahrräder unter 800 € Ersparnis sowie die kleineren
USM-, Vitra-, Thonet- und Simson-Anzeigen — liegen sämtlich unter der Priorisierungsschwelle aus
prompt.md („größter absoluter Abstand zuerst, liquide Ware zuerst") und wurden nach den beiden
bestätigten Funden nicht mehr einzeln geprüft. Sie bleiben in `candidates.json` und stehen dem
Abendlauf zur Verfügung, da sie nicht ins `deal_log.csv` gewandert sind.
