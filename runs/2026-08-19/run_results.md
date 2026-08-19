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
