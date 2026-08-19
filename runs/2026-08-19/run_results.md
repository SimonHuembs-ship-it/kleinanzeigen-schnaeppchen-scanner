# Lauf 2026-08-19, morgens

- **Zeitpunkt:** 19. August 2026, 07:05 Uhr (MESZ)
- **Datenstand:** `candidates.json` generiert 2026-08-19T06:39:35+02:00, Fenster 01:26 bis 06:27 Uhr, 25 Minuten alt, also frisch
- **Gesichtet (Stufe 1):** 23.882 Anzeigen, davon 200 Kandidaten in der Warteschlange
- **Bereits im `deal_log.csv`:** 57 Einträge, keine Überschneidung mit den 200 Kandidaten
- **Inhaltlich geprüft:** die 45 Kandidaten mit dem größten absoluten Abstand plus die vollständigen liquiden Kategorien (Drohnen, Uhren, Apple, Konsolen, Foto)
- **Gemeldete Funde:** 4

## Funde

| # | Titel | Preis | Bestätigter Marktwert | Abstand | Ort |
|---|---|---|---|---|---|
| 1 | Knoll Barcelona Chair, schwarzes Nappaleder | 2.200 € | 3.500–4.000 € (Sebworld 3.990 €, eBay.de ab 3.750 €) | ca. 40 % | Höchst im Odenwald |
| 2 | USM Haller Sideboard 153 × 39 × 74 cm, beige | 750 € | 1.295 € gebraucht (Vedera, 150 × 35 × 74 cm), 1.914 € neu (smow.de) | ca. 42 % | Berlin-Weißensee |
| 3 | PS5 Pro 2 TB + Disc-Laufwerk + 2 Controller | 480 € | 610–650 € gebraucht (eBay.de: 612 € und 650 €), neu ab 798,90 € | ca. 22 % ohne Zubehör | Chemnitz |
| 4 | Steam Deck OLED 512 GB + Dock + 512-GB-Karte | 370 € | 440–500 € nackt (Valve refurbished 459 €, rebuy 438,99 €), Paket 550–590 € | ca. 34 % aufs Paket | Norden |

Kein Fund trägt `unkenntnis_bonus`; die Reihenfolge ergibt sich daher rein aus der
absoluten Ersparnis. Keine der kategoriespezifischen Pflicht-Warnflags aus
prompt.md Schritt 2e trifft auf einen der vier Funde zu (keine RTX 4090, keine
Switch 2 mit Spielen, keine AirPods, kein Apple-Gerät, kein Tesla, kein Porsche,
kein Klassiker ohne Brief, kein NAS, kein Threadripper Pro).

## Verworfene Kandidaten

### Marktwert eigenständig geprüft, Abstand reicht nicht

- **Rolex Oyster Perpetual 41 grün Ref. 124300 Fullset, 7.850 €** (`3439044587`) —
  Chrono24.de führt dieselbe Referenz als Fullset für 8.699 € und ein Exemplar von
  2023 mit Papieren für 9.088 €. Der Kleinanzeigen-Median von 12.450 € (n=11) ist
  von Wunschpreisen aus der Hype-Phase 2021 verzerrt. Gegen das tatsächlich
  bestätigte Niveau von 8.700 bis 9.100 € sind 7.850 € rund 10 Prozent Abstand,
  also unter der Schwelle. Zusätzlich: die Anzeigen-ID stammt aus einer deutlich
  älteren Nummernserie, die Anzeige läuft also seit Monaten — bei 35 Prozent unter
  Markt wäre sie längst weg.
- **Tudor Black Bay Chronograph 79360N Full Set, 3.700 €** (`3487891987`) —
  Anzeige selbst ist vorbildlich (privat seit 2013, Abholung, Mängel offengelegt,
  Kaufdatum 19.03.2022, Score 100). Gebrauchte 79360N beginnen auf Chrono24 aber bei
  rund 3.700 €, das Gros liegt bei 4.300 bis 5.100 €. Der Preis liegt am unteren
  Rand des Marktes, nicht 20 Prozent darunter. Median 7.390 € (n=11) mischt
  Sondermodelle wie das rosa „Flamingo“-Zifferblatt ein.
- **Technics SL-1210 MK2, 500 €** (`3487949782`) — wird ohne Tonabnehmer und ohne
  Haube verkauft, beides zusammen 150 bis 250 € Wiederbeschaffung. Gegen den Median
  von 765 € für komplette Geräte bleibt kein Abstand. Nur ein Bild.
- **Cassina Maralunga Zweisitzer, 800 €** (`3488484327`) — vom Polsterbetrieb neu
  bezogen, also kein Originalbezug. Genau das ist bei Cassina der wertmindernde
  Punkt, der den Preis erklärt; der Median von 2.774 € gilt für Originalbezüge.
- **Ernst Leitz Wetzlar Binokular-Mikroskop, 249 €** (`3488250249`) — die
  Referenzgruppe „Ernst Leitz Wetzlar“ (Median 499 €, n=19) mischt Objektive,
  Kameras und Mikroskope. Zum konkreten Gerät (Seriennummer 786315, Modell nicht
  genannt) ließ sich kein belastbarer Referenzwert finden. Statt zu schätzen:
  verworfen.

### Niedriger Preis erklärt sich von selbst

- **BMW 328i E36 Cabrio, 6.890 €** (`3487632534`) — 217.000 km, „ganz leichte
  Hagelschäden“, LPG-Umbau, Euro 3, vierter Halter. Alle vier Punkte drücken den
  Preis zu Recht.
- **Mercedes 300 SE W126, 7.499 €** (`3487982510`) — 300.500 km, Rostansatz am
  Kotflügel, Motor geht im Leerlauf aus. Verkäuferkonto am Tag der Anzeige angelegt.
- **Mercedes W124 E200, 3.000 €** (`3487742657`) — mehrere geschweißte
  Aufnahmen, „die ein oder andere Roststelle“, 243.000 km, Schiebedach nur kippbar.
- **BMW E36 323i, 6.000 €** (`3488338979`) und **BMW E36 318i Touring, 2.350 €**
  (`3488065595`) — `referenz.belastbar` ist false (Streuung 2,76 bzw. 3,39), kein
  verwertbarer Median.
- **Specialized FSR E-Bike Fully, 900 €** (`3488309596`) — trägt
  `unkenntnis_bonus`, wurde deshalb nicht nach Anzeigenqualität bewertet. Verworfen
  allein wegen des Sachmangels: „Leider verliert der Motor gelegentlich an
  Leistung.“ Ein Motorschaden am E-Bike ist ein Reparaturposten im vierstelligen
  Bereich, der Preis ist damit richtig.
- **Cube Stereo Race HPA E-Bike, 900 €** (`3488306848`) — 16.679 km Laufleistung.
  Ein Bosch PowerTube 625 Wh liegt nach dieser Strecke typisch bei 60 bis 70 Prozent
  Restkapazität, Ersatz kostet 650 bis 750 €. Hohe Laufleistung ist nach prompt.md
  Schritt 2a ein selbsterklärender Grund; ein mit der Laufleistung vergleichbares
  Angebot war nicht zu finden.
- **Ducati Monster, 2.850 €** (`3488498446`) — der Median von 5.310 € über die
  Suchanfrage „Ducati Monster“ mischt 620, 696, 796, 821 und 937 zu einem
  Phantomwert. Für eine Monster 620 von 2002 mit 28.000 km ist der Preis marktüblich.
- **Riese & Müller Homage touring, 3.540 €** (`3471727215`) — Händler-Abverkauf mit
  rollender Frist („Preis gültig bis 23.08.“) bei nur zwei Bildern. Aus
  Shimano 11-fach und Magura MT4/MT5 lässt sich das Modelljahr nicht bestimmen, und
  ohne Modelljahr ist kein Vergleichsangebot zuzuordnen. Der Homage5 touring 2026
  liegt bei 7.899 € UVP, reduziert bei 5.799 €; die naheliegende Erklärung für 3.540 €
  ist mehrjährige Lagerware mit gealtertem Akku. Marktwert nicht bestätigbar.

### Betrugsprofil überwiegt

- **Rolex Daytona „NEU UNGETRAGEN“, 25.990 €** (`3487666633`) — ein einziges Bild,
  vier Zeilen Text, keine Referenznummer, kein Baujahr, nur Versand trotz „sofort
  abholbereit“, Verkäufer ohne jede Bewertung. Der Median von 42.500 € mischt Gold-
  und Diamantmodelle ein; das Angebot liegt sogar über dem p25 der Vergleichsgruppe
  von 23.950 €. Handwerklich glatte Anzeige ohne prüfbare Angabe bei fünfstelligem
  Betrag: genau das Muster aus prompt.md.
- **Rolex Datejust 36 mit Diamant-Zifferblatt, 8.800 €** (`3487644662`) — keine
  Referenznummer, Verkäuferbewertung 0,46, nur Versand. Nachträglich gesetzte
  Diamanten senken den Wert bei Rolex erheblich, statt ihn zu heben.
- **Omega Speedmaster Date Ref. 3511.50, 1.500 €** (`3488177759`) — Konto 28 Tage
  alt, nur Versand, keine Originalpapiere, dafür Kaliber und Referenz auf die
  Stelle genau. Poliertes Datenblatt plus frisches Konto plus Versandzwang.
- **Tudor Black Bay Heritage, 2.100 €** (`3488150658`) — Verkäuferbewertung 0,38,
  nur Versand, und die Uhr kommt ohne Stahlband („muss selber gekauft werden“), was
  400 bis 600 € Nachkauf bedeutet.
- **DJI Mini 5 Pro Fly More Combo, 2 × 500 €** (`3487886050`, `3488207301`) — zwei
  Anzeigen desselben aktuellen Topmodells zum identischen Preis, beide nur Versand,
  beide gut ausformuliert. Rund 55 Prozent unter Marktwert bei einem Gerät, das sich
  zum vollen Preis binnen Stunden verkauft.
- **iPhone-Cluster, 37 Anzeigen zwischen 150 und 400 €** (`3487609358` u. a.) —
  iPhone 13, 14 und 15 durchgehend bei 50 bis 65 Prozent des Median, überwiegend
  Versand, kurze Texte. Bei Apple-Geräten in dieser Preislage sind iCloud-Sperre,
  MDM-Bindung und Hehlerware die Regel, nicht die Ausnahme. Kein Einzelfall
  gerechtfertigte eine externe Marktwertprüfung.
- **MacBook-Cluster, 17 Anzeigen** (`3487641049` u. a.) — darunter ein „MacBook Pro
  M5 14"“ für 1.300 € und ein „MacBook Air M3“ für 500 €. Gleiches Muster.

### Referenzgruppe nicht belastbar (`belastbar: false` oder Streuung > 2,5)

`3487996806` Laverda 1000 (Streuung 9,43), `3487986391` Ducati 996 (17,74),
`3487820989` EMCO Fräsmaschine (28,89), `3414247593` VDF Boehringer Drehmaschine
(2,75), `3488460148` Cube Agree Rennrad (3,64), `3488342633` und `3487765196`
Gibson Les Paul Studio (3,75 bzw. 3,38), `3067230267` Jaeger-LeCoultre Atmos
(5,54), `3488332983` Cube Touring One (3,02), `3488145675` MacBook Pro (2,70),
`3488262675` MacBook Pro Silber (3,12), `3487990557` DJI Mavic Pro (3,26),
`3487632764` und `3488253562` DJI Mavic Pro (4,06 bzw. 4,14).

### Ohne Referenz, nicht bewertbar

`3488465846`, `3488486918`, `3488484975`, `3488494363`, `3488494266` — die fünf
Kandidaten aus der Watchlist `notverkaeufe` haben `referenz: null`. Zu einer
„hochwertigen Einbauküche aus Wohnungsauflösung“ oder einem „antiken Esstisch mit
4 Stühlen“ ohne Marke, Modell oder Maße lässt sich kein belastbarer Marktwert
recherchieren. Nicht geschätzt, sondern verworfen.

### Nicht geprüft

Die restlichen rund 130 Kandidaten liegen sämtlich unter 850 € absoluter Ersparnis
und wurden nach der Priorisierung aus prompt.md („größter absoluter Abstand zuerst,
liquide Ware zuerst“) nicht mehr einzeln geprüft. Sie bleiben in `candidates.json`
und stehen dem Abendlauf zur Verfügung, da sie nicht ins `deal_log.csv` gewandert
sind.

---

# Lauf 2026-08-19, abends (19:10 Uhr MESZ)

- **Datenstand:** `candidates.json` generiert 2026-08-19T15:44:50+02:00, also 3 h 25 min
  alt und damit innerhalb der Vier-Stunden-Frist aus Schritt 1
- **Zeitraum des Sammellaufs:** 2026-08-19T09:24:07+02:00 bis 2026-08-19T14:24:07+02:00
- **Gesichtet (Stufe 1):** 179.005 Anzeigen, 197 Kandidaten in der Warteschlange
- **Bereits im `deal_log.csv`:** 61 Einträge, keine Überschneidung mit den 197 Kandidaten
  (die vier Funde vom Morgenlauf sind aus der Warteschlange verschwunden)
- **Referenzqualität:** 144 Kandidaten mit belastbarem Median und Streuung ≤ 2,5,
  48 mit unbelastbarem Median (als nicht vorhanden behandelt), 5 ohne Referenz
- **Inhaltlich geprüft:** die 45 Kandidaten mit dem größten absoluten Abstand plus die
  vollständigen liquiden Kategorien (Uhren, Drohnen, Apple, Konsolen) plus alle drei
  Kandidaten mit `unkenntnis_bonus`
- **Gemeldete Funde:** 5

## Funde

| # | Titel | Preis | Bestätigter Marktwert | Abstand | Ort |
|---|---|---|---|---|---|
| 1 | BMC Roadmachine X TWO, Rival AXS XPLR, Gr. 54 | 1.800 € | 3.100 € gebraucht im Auslieferungszustand, neu ab 3.500 € (UVP 4.799 €) | ca. 42 % | Tann (Niederbay) |
| 2 | Koga Miyata Full Pro, Dura Ace, RH 58 | 340 € | 700–1.200 € (eBay.de: 699 € Full Pro Dura Ace 7200 EX, 1.190 € Proluxe/FullPro-L) | ca. 51 % | Hamburg Eilbek |
| 3 | DJI Mini 4 Pro Fly More Combo + RC 2 | 320 € | 450–550 € gebraucht, neu 799 € (Geizhals) bis 899 € (heise), Drohne allein 636 € | ca. 35 % | Klettgau |
| 4 | Sony PS5 Pro 2 TB + Alan Wake 2 | 499 € | 650–700 € gebraucht, neu 798,90–899 € | ca. 25 % | Meerbusch |
| 5 | Steam Deck OLED 512 GB + Dock + Tasche | 315 € | 459 € Valve refurbished, 500 € eBay.de | ca. 30 % | Hamburg Wilhelmsburg |

Kein Fund trägt `unkenntnis_bonus`; die Reihenfolge ergibt sich daher rein aus der
absoluten Ersparnis. Keine der kategoriespezifischen Pflicht-Warnflags aus prompt.md
Schritt 2e trifft zu (keine RTX 4090, keine Switch 2 mit Spielen, keine AirPods, kein
Apple-Gerät, kein Tesla, kein Porsche, kein Klassiker ohne Brief, kein NAS, kein
Threadripper Pro). Bei Fund 4 ist der Ausschluss des Bezahlsystems zugunsten von
PayPal-Freunde als `risiko` in der Mail vermerkt.

## Verworfene Kandidaten

### Uhren: der Kleinanzeigen-Median ist durchweg zu hoch, eigene Prüfung reicht nicht

Fünf Rolex-Anzeigen bilden die Spitze der Nominalersparnis. Keine hat die eigene
Marktwertbestätigung bestanden — Chrono24 führt gebrauchte Datejust 41 Ref. 126300
Full Set von 2022 bei 7.999 bis 8.900 €, der Kleinanzeigen-Median von 13.000 €
mischt Bi-Color- und Diamant-Varianten ein.

- **Rolex Datejust 41, 8.500 €** (`3488715142`) — Full Set 2022, deutsche Auslieferung.
  Gegen das bestätigte Niveau von 8.000 bis 8.900 € ist das der Marktpreis, kein Abstand.
- **Rolex Datejust 41 Ref. 126300-0007, 8.990 €** (`3488351022`) — dieselbe Referenz,
  dasselbe Ergebnis. Liegt sogar am oberen Rand des bestätigten Bandes.
- **Rolex Datejust 36 Ref. 126200 ombré grün, 8.990 €** (`3488317840`) — im Juli 2026
  beim Konzessionär gekauft, ungetragen, Erstkaufrechnung. Der Preis liegt oberhalb des
  Listenpreises, was bei einem frischen Zifferblatt normal ist; der Median von 13.300 €
  gilt für Varianten mit Diamantlünette. Anzeige selbst ist untadelig (Abholung,
  Kaufvertrag, Bankübergabe) — nur eben kein Schnäppchen.
- **Rolex Datejust 126300 blau/römisch Full Set, 9.500 €** (`3488670486`) — der
  Verkäufer nennt selbst 11.500 € Händlerpreis, das sind 17 Prozent Abstand und damit
  unter der Schwelle. Verkäuferbewertung 0,67.
- **Rolex Oyster mit Handaufzug, 3.500 €** (`3488866704`) — „Oyster" ist ein
  Gehäusename, kein Modell: der Median von 8.500 € (n=97) mischt Submariner, Datejust
  und Oyster Perpetual. Eine handaufzügige Oyster Precision in Stahl liegt bei 1.500
  bis 3.000 €. Der Preis ist eher zu hoch als zu niedrig. Dazu Versand mit
  Käuferschutz und 41 Prozent des vermeintlichen Marktwerts — das Muster der Leitidee.
- **Omega Speedmaster Date Ref. 3511.50, 1.500 €** (`3488177759`) — Konto 28 Tage alt,
  ausschließlich Versand, keine Papiere. Chrono24 führt die Referenz bei 1.800 bis
  3.000 €, der Abstand wäre da. Das Verkäuferprofil ist es, das den Ausschlag gibt:
  neues Konto plus Versandzwang bei einer liquiden Marke.
- **Omega Speedmaster Reduced mit Box, 2.199 €** (`3488563183`) — Konto seit gestern,
  nur Versand. Gleiches Muster, noch deutlicher.
- **Tudor Black Bay Heritage, 2.100 €** (`3488150658`) — Verkäuferbewertung 0,38,
  Versandzwang. Ohne Referenznummer lässt sich nicht unterscheiden, ob eine 79230 oder
  eine 79220 gemeint ist, deren Gebrauchtniveaus 800 € auseinanderliegen.
- **Tag Heuer Formula 1 Chronograph CAZ1011.BA0842 Full Set, 920 €** (`3488818643`) —
  Quarz-Chronograph, Kauf April 2024. Gebrauchtniveau dieser Referenz 700 bis 1.100 €,
  der Preis liegt mittig. Der vom Verkäufer genannte Neupreis von 2.600 € ist der
  Listenpreis, nicht der erzielbare Wert.
- **Longines HydroConquest, 600 €** (`3488175464`) — Konto 36 Tage, nur Versand, keine
  Referenznummer, und der Text liest sich generiert („zeitloser Begleiter",
  „authentischer Charakter" für Gebrauchsspuren). Verworfen.

### Niedriger Preis erklärt sich von selbst

- **Honda CB 750 Four K2 Scrambler-Umbau, 4.800 €** (`3488696916`) — der Median von
  7.987 € gilt für originale K2. Gekürztes Rahmenheck, Einzelanfertigungs-Alutank,
  fremdes Hinterrad und 4-in-1-Krümmer einer F2: genau die Umbauten, die den
  Sammlerwert senken. Anzeige und Verkäufer sind vorbildlich, der Preis ist richtig.
- **Mercedes-Benz 300 SE W126, 7.499 €** (`3487982510`) — 300.500 km, Rostansatz am
  Kotflügel, Motor geht im Leerlauf aus. Dazu Konto am selben Tag angelegt und
  Stellvertretergeschichte („verkaufe im Auftrag meines Vaters").
- **BMW E36 318i Cabrio, 2.500 €** (`3488786967`) — 286.000 km, wird vom Verkäufer
  selbst „ausdrücklich als defekt an Schrauber oder Export" angeboten.
- **Mercedes W201 190E 2.6, 2.999 €** (`3488544877`) — zerlegt, in der Rubrik
  Ersatz- und Reparaturteile eingestellt. Der Median gilt für fahrbereite Autos.
- **Specialized FSR E-Bike Fully, 900 €** (`3488309596`) — trägt `unkenntnis_bonus`
  und wurde deshalb nicht nach Anzeigenqualität abgewertet, aber „der Motor verliert
  gelegentlich an Leistung" ist ein Defekt am teuersten Bauteil.
- **iPhone 15 Pro 128 GB, 250 €** (`3488676753`) — Zustand „Defekt", Rückseite und
  Temperatursensor der Kamera hin.
- **iPhone 16 128 GB, 360 €** (`3488596006`) — verbauter China-Akku, entlädt schnell.
- **Trek Slash 8, 555 €** (`3488853759`) — laut Verkäufer „vermutlich aus 2015",
  27,5 Zoll, 10-fach Deore, nicht aus erster Hand, Kinder-Enduro-Einsatz. Der Median
  von 1.800 € gilt für aktuelle Slash 8. Bei 600 bis 900 € realistischem Niveau
  bleibt kein Abstand.

### Referenzgruppe nicht vergleichbar oder Marktwert nicht bestätigbar

- **Cube Stereo ONE22 Pro, 1.350 €** (`3488452601`) — UVP des ONE22 Pro sind 1.999 €;
  der Median von 2.599 € entsteht, weil die Suche die Hybrid-E-MTB-Variante
  (2.899–3.199 €) mit einmischt. Bei 1.100 bis 1.500 € gebraucht ist 1.350 € Markt.
- **Cube Stereo Race HPA E-Bike, 900 €** (`3488306848`) — Bosch CX 85 Nm, PowerTube
  625 Wh, Fox 34, XT, gestern beim Kundendienst mit Nachweis, Abholung, Mängel
  offengelegt: das Verkäuferprofil ist das beste im ganzen Feld. Aber 16.679 km
  bedeuten einen Akku am Ende seiner Zyklenzahl (Ersatz 600–800 €), und zu einem
  Vergleichsangebot derselben Laufleistung ließ sich kein Beleg finden — die
  auffindbaren Referenzen haben 188 bzw. 490 km. Ohne belastbaren Referenzwert wird
  nicht geschätzt. Bleibt für den nächsten Lauf offen.
- **USM Haller Sideboard 2×2 Bicolor, 950 €** (`3488855421`) — Fachhändler bieten
  generalüberholte 2×2-Sideboards mit 35 cm Tiefe ab 990 € mit Gewährleistung an,
  gebrauchte auf eBay ab 966 €. Ein Privatverkauf ohne Gewährleistung bei 950 € ist
  damit Marktpreis, nicht 20 Prozent darunter. Der Median von 1.895 € ist zu hoch.
- **Gibson Les Paul Junior 57 Custom Shop VOS, 2.799 €** (`3488694375`) — vor sechs
  Monaten neu gekauft, Lackfehler offengelegt, gutes Profil. Neupreis in den USA
  4.699 $; die deutschen Belegquellen (Thomann) sind in dieser Umgebung gesperrt, und
  Custom-Shop-Gibsons liegen gebraucht typisch bei 70 bis 75 Prozent vom Neupreis.
  Ohne bestätigtes Gebrauchtniveau kein Fund. Bleibt offen.
- **Revox B251, 450 €** (`3488685649`) — `referenz.belastbar` ist false (Streuung
  2,97), also eigene Prüfung: hifishark.com führt B251 von 368 € (revidiert) über
  549 €, 625 € und 725 € bis 1.000 € (serviciert). Das Gerät hier ist „In Ordnung"
  und nicht revidiert; 450 € liegen mitten im Band, nicht 20 Prozent darunter.
- **Ernst Leitz Wetzlar Binokular-Mikroskop, 249 €** (`3488250249`) — wie schon im
  Morgenlauf: Referenzgruppe mischt Objektive, Kameras und Mikroskope, Modell wird
  nicht genannt. Kein belastbarer Referenzwert.
- **Drehmaschine Meuser, 1.000 €** (`3488547323`) — trägt `unkenntnis_bonus`, aber die
  Beschreibung ist zwei Zeilen ohne Modell, Spitzenweite oder Umlaufdurchmesser. Bei
  Werkzeugmaschinen entscheiden genau diese Angaben über den Wert. Nicht bewertbar.
- **Cassina Maralunga Sofa, 1.800 €** (`3488620158`) — Beschreibung nennt weder Größe
  noch Bezug noch Zustand über „Gut" hinaus; ohne Zweisitzer/Dreisitzer-Unterscheidung
  ist der Median von 3.049 € nicht anwendbar.
- **Cassina Maralunga Zweisitzer, 800 €** (`3488484327`) — bereits im Morgenlauf
  verworfen (kein Originalbezug), unverändert.
- **Steiger Trekkingrad, 769 €** (`3488622569`) — „Steiger" ist eine No-Name-Marke;
  der Median von 2.499 € stammt aus Treffern anderer Hersteller. Gewerblicher
  Verkäufer mit „von 1699 € auf 769 € reduziert".
- **Riese & Müller Homage touring, 3.540 €** (`3471727215`) — Händlerangebot für
  Neuware mit UVP 6.749 €, aber mit Zeitdruck („Preis gültig bis 23.08.", „nur
  1 Stück"). Eine Händleraktion ist kein schlecht bepreistes Privatangebot.
- **MacBook Air 2020 Intel i3, 349 €** (`3488343133`) — der Median von 800 € für
  „Apple MacBook Air" mischt M1 bis M4 ein. Intel-Airs von 2020 liegen bei 250 bis
  350 €, der Preis ist Markt.
- **Apple MacBook M2 512 GB, 600 €** (`3488364543`) — die Attribute widersprechen
  sich (Prozessor M1, Erscheinungsjahr 2026, 14 Zoll, Farbe Blau) und die
  Beschreibung nennt 8 GB statt der im Titel implizierten Ausstattung. Zwei Dellen.
  Nicht eindeutig identifizierbar.
- **Vitra EA 119 Aluminium Chair, 900 €** (`3488189778`) — Leder Snow, gepflegt.
  Gebrauchte EA 119 in Leder liegen bei 1.000 bis 1.500 €, das p25 der Referenz bei
  1.069 €. Abstand unter 20 Prozent.
- **Ingo Maurer Bulb, 250 €** (`3488103113`) — der Verkäufer verlinkt selbst eine
  Auktionsreferenz, kennt den Wert also. Originale von Design M und spätere
  Neuauflagen sind auf vier Bildern nicht zu unterscheiden, die Preise liegen
  Faktor drei auseinander.

### Betrugsmuster der Leitidee: gut gemachte Anzeige, schlechtes Profil

- **DJI Mavic 3 Thermal, 3.000 €** (`3488542428`) — nominal der größte Abstand im
  Drohnensegment (neu 5.899 €, gebraucht zuletzt 4.990 € auf eBay). Konto 22 Tage alt,
  ausschließlich Versand, keine Abholung bei 3.000 € Warenwert, dazu eine
  Stellvertreterfigur („Service läuft weiterhin über die Firma Copterpro, Kontakt
  wird dem Käufer mitgeteilt"). Bei diesem Profil lieber kein Fund als ein schwacher.
- **iPhone 15 Pro 256 GB, 350 €** (`3488529683`) — Konto vier Tage alt, nur Versand,
  zwei Zeilen Text.
- **DJI Mini 5 Pro Fly More Combo, 500 €** (`3488207301`) — die Beschreibung ist
  wörtlich aus einem Shop-Listing kopiert („Benötigt zur Fertigstellung: USB
  Netzteil", „Schwierigkeitsgrad: 1. Einsteiger"), höchstens ein Bild, nur Versand.

### Kurz gefasst: restliche 130 Kandidaten

Der Rest der Warteschlange besteht aus iPhones der Generationen 12 bis 14 mit 70 bis
200 € Nominalabstand (Streuungen unter 1,5, also saubere Referenzen — die Preise sind
schlicht Markt), aus Cube-, Canyon- und Pegasus-Rädern im üblichen Preisband ihrer
Baureihe, aus USM-Haller-Teilen, deren Median durch die Fachhändlerpreise nach oben
gezogen wird, und aus fünf `notverkaeufe`-Kandidaten ohne jede Referenz
(Wohnungsauflösungen, Einbauküche, E-Fatbike). Keiner erreicht nach eigener Prüfung
20 Prozent Abstand.
