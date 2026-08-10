# Laufprotokoll 10. August 2026, 19:15 Uhr (Abendlauf)

- `candidates.json` generiert: **2026-08-10T16:01:28+02:00** (3 h 06 min alt, innerhalb der Vier-Stunden-Grenze)
- Zeitraum: 10. August 2026, 09:44 Uhr bis 10. August 2026, 14:44 Uhr
- Gesichtete Anzeigen laut Sammler: **162.751**
- Kandidaten in der Warteschlange: **213**
- Bereits in `deal_log.csv` und damit verworfen: **0**
- Inhaltlich geprueft: **213** - davon 38 einzeln am Anzeigentext beurteilt und 12 zusaetzlich per Websuche gegen externe Marktwerte gehalten
- **Gemeldete Funde: 3**

## Funde

| # | Fund | Preis | Bestaetigtes Marktniveau | Ersparnis | Ort |
|---|---|---|---|---|---|
| 1 | [Vitra Grand Repos inkl. Ottoman](https://www.kleinanzeigen.de/s-anzeige/vitra-grand-repos-inkl-ottoman/3480923628-88-5538) | 2.100 EUR | 3.300-4.100 EUR (vier konkrete Gebrauchtangebote desselben Modells auf Ricardo, davon eines ebenfalls Bezug Cosy 2; Neupreis Vitra rund 9.900 EUR) | 1.675 EUR | Immenstadt |
| 2 | [USM Haller Highboard M offen in Graphitschwarz](https://www.kleinanzeigen.de/s-anzeige/usm-haller-highboard-m-offen-in-graphitschwarz/3480492715-88-4260) | 500 EUR | 600-830 EUR (Neupreis 1.194 EUR vom Verkaeufer selbst genannt, USM-Zweithandhaendler bei 50-70 Prozent des Neupreises) | 1.099 EUR* | Leipzig |
| 3 | [USM Haller Rollcontainer weiss mit 3 Schubladen](https://www.kleinanzeigen.de/s-anzeige/usm-haller-rollcontainer-weiss-mit-3-schubladen-nur-bis-dienstag/3480477255-93-1176) | 350 EUR | rund 550 EUR (zwei konkrete Vergleichsangebote: 580 EUR Kleinanzeigen, 530 EUR eBay) | 390 EUR* | Ahaus |

\* Die Spalte `ersparnis_eur` in `deals.json` und `deal_log.csv` bezieht sich formatbedingt auf den
Kleinanzeigen-Median. Massgeblich fuer die Entscheidung war in allen drei Faellen das extern
bestaetigte Preisniveau in der Spalte daneben, nicht der Median.

### Pflicht-Warnflags angewandt
- Unter den Funden ist kein Apple-Geraet, keine RTX 4090, keine Switch 2, keine AirPods, kein Tesla,
  kein Porsche, kein Klassiker, kein NAS und kein Threadripper - die kategoriespezifischen
  Pflichtflags aus Schritt 2e greifen bei diesen drei Funden nicht.
- Als `risiko` steht in der Mail beim Vitra das erst im April 2026 angelegte Konto ohne belastbare
  Bewertungshistorie, beim Highboard das ohne Tueren fehlende teuerste Systembauteil und beim
  Rollcontainer die kuenstliche Verknappung im Titel.

## Befund des Laufs: koordinierter Scam-Cluster in der Nacht

Sechs Kandidaten mit hohem Warenwert bilden ein zusammenhaengendes Muster und wurden geschlossen
verworfen. Alle sechs Konten wurden zwischen dem 3. und 9. Juli 2026 angelegt, alle sechs Anzeigen
wurden in derselben Nacht zwischen 00:05 und 01:50 Uhr eingestellt, alle bieten ausschliesslich
Versand ohne Abholung an, und alle tragen dieselbe maschinell wirkende Satzeinleitung
("Zum Verkauf angeboten wird ein originaler ..."):

| Anzeige | Preis | Konto seit | Eingestellt |
|---|---|---|---|
| Studer A80 RC MkII Tonbandmaschine Butterfly | 8.000 EUR | 07.07.2026 | 01:22 Uhr |
| Technics SL-1210G neuwertig OVP | 2.450 EUR | 05.07.2026 | 00:07 Uhr |
| Accuphase DP-80L / DC-81L | 1.850 EUR | 09.07.2026 | 01:47 Uhr |
| Thorens 2300 Series High-End-Anlage | 1.500 EUR | 05.07.2026 | 00:05 Uhr |
| Accuphase E-305 Vollverstaerker | 1.350 EUR | 09.07.2026 | 01:50 Uhr |
| DJI Mavic 3 Thermal Waermebild-Drohne | 3.300 EUR | 08.07.2026 | 00:13 Uhr |

Das ist exakt das Gegenteil der Leitidee: handwerklich saubere Anzeigen, korrekte Modellbezeichnungen,
keine Maengel ausser der pflichtschuldig erwaehnten "Gebrauchsspuren", Versand statt Abholung. Kein
einziger dieser sechs Kandidaten wurde weiter geprueft. Auffaellig ist, dass die erste Stufe fuenf
davon mit Score 87 bis 99 bewertet hat - das Alterskriterium "Konto juenger als 6 Monate" allein
gewichtet den Cluster nicht stark genug ab.

Getrennt davon: die Anzeigen **RTX 5080 ASUS ROG Astral fuer 620 EUR** und **PlayStation 5 Pro 2 TB
fuer 479 EUR** stammen vom selben Verkaeuferkonto (ID 41142970, seit 2016, Bewertung 0,94) und
verlangen beide ausdruecklich PayPal Freunde statt der Plattformabwicklung. Ein etabliertes Konto
mit guter Bewertung, das bei zwei hochliquiden Artikeln zu deutlich unter Marktwert konsequent aus
dem Kaeuferschutz herausdraengt, ist der klassische Uebernahmefall. Beide verworfen.

## Verworfene Kandidaten mit Begruendung

### Einzeln am Anzeigentext geprueft

| Anzeige | Preis | Grund der Verwerfung |
|---|---|---|
| Yanmar Minibagger SV15 | 9.999 EUR | Planierschild faehrt hoch, aber nicht runter, Verkaeufer nennt die Maschine selbst "ausgeschlagen". Defekt erklaert den Preis, Angebot liegt exakt auf dem p25 der Referenz. |
| w126 - 500 SEL | 7.999 EUR | 250.000 km, zweizeilige Beschreibung ohne Zustandsangaben, Verkaeuferbewertung 0,57. Vergleichbares 500 SEL Angebot mit nur 66.000 km liegt bei 8.000 EUR, ein Abstand von 20 Prozent zum bestaetigten Markt ist damit nicht belegbar. |
| BMW E36 328 Coupé M-Paket | 9.200 EUR | Verkaeufer schreibt selbst "muss definitiv komplett restauriert werden": Servopumpe defekt, alle vier Kotfluegel und die Wagenheberaufnahmen zu machen, Lackierung faellig. 9.200 EUR sind dafuer nicht billig, sondern teuer. |
| BMW 318i Touring E30 | 3.750 EUR | Fahrzeugzustand laut Inserat "beschaedigt", Zahnriemen faellig, Schweller beidseitig geschweisst, abgemeldet ohne Probefahrtmoeglichkeit. Zustandsstufe 4, der Preis passt dazu. |
| Mercedes 300 CE W124 Coupé | 6.900 EUR | 238.000 km, Verkaeuferbewertung 0,41. Untere Kante des Haendlermarkts fuer den 300 CE liegt bei 7.990 EUR, damit kein belegbarer Abstand von 20 Prozent. |
| Mercedes-Benz E 250 W124 | 3.000 EUR | 500.000 km, mit Maengeln durch den TUEV gefallen, als beschaedigtes Fahrzeug eingestellt. Preis erklaert sich von selbst. |
| W124 300 Turbo Diesel | 6.000 EUR | Unfallschaden vorne links, nicht repariert, 468.000 km. Preis erklaert sich von selbst. |
| Mercedes-Benz 190 E W201 | 1.950 EUR | 450.000 km, TUEV abgelaufen, ungeklaertes Vibrieren ab 80 km/h, Schiebedach defekt, Klarlackabloesungen. Preis erklaert sich von selbst. |
| Rolex Oyster 41mm | 6.950 EUR | Titel nennt kein Modell und keine Referenz, "Rolex Oyster 41mm" kann Oyster Perpetual 41, Datejust 41 oder Air-King sein. Ein einziges Bild bei 6.950 EUR, Verkaeuferbewertung 0,45, Versand angeboten. Marktwert nicht bestimmbar, weil das Produkt nicht bestimmbar ist. |
| Tudor Black Bay GMT | 2.500 EUR | Ehrliche Anzeige, Full Set von 11/19, Revision 03/25 bei Tudor ueber Wempe, nur Abholung. Deutscher Gebrauchtmarkt aber bei 2.790 bis 3.947 EUR, konkretes Vergleichsangebot Full Set Bj. 2020 bei 3.140 EUR. Der Abstand liegt bei 10 bis 20 Prozent und damit unter der Schwelle. Knappster Fall des Laufs. |
| Leica Elmarit-M 2,8/21mm ASPH. 11135 | 1.090 EUR | Sauber dokumentierte Anzeige mit Seriennummer und 20 Bildern. MPB als vorgesehene Referenzquelle fuehrt das Objektiv gebraucht zu 1.319 bis 1.479 EUR. Die offengelegten Putzspuren auf der Frontlinse setzen das Exemplar ans untere Ende dieser Spanne, dort betraegt der Abstand 17 Prozent. Knapp verfehlt. |
| Jaeger-LeCoultre Reverso Squadra Full Set | 4.500 EUR | Guenstigstes Vergleichsangebot derselben Squadra Hometime in Stahl liegt bei 4.746 EUR, Abstand rund 5 Prozent. |
| Jaeger leCoultre Reverso Shadow | 4.390 EUR | Gewerblicher Haendler mit zwoelf Monaten Garantie. Die Referenzabfrage "Jaeger leCoultre Reverso" mischt Quarz-Classique und Manufakturmodelle ueber eine Preisspanne von 2.000 bis 30.000 EUR, das genaue Modell ist aus vier Bildern und drei Textzeilen nicht bestimmbar. |
| Jaeger-LeCoultre Atmos Classique | 1.800 EUR | Referenz nicht belastbar (Streuung 3,5), Konto erst seit 29.06.2026. |
| Rolex Lady Datejust 6917 Vintage | 2.750 EUR | Referenz nicht belastbar (Streuung 2,71), damit kein Median. Marktniveau fuer die 6917 liegt selbst bei 2.500 bis 3.500 EUR, das Angebot also im Markt. |
| Tag Heuer Carrera Chronograph | 1.499 EUR | Keine Referenznummer im Text, die Abfrage "Tag Heuer Carrera" mischt Quarz- und Manufakturchronographen. Zudem "keine Abwicklung ueber Kleinanzeigen, nur Bankueberweisung". |
| Omega Seamaster de Ville Cross dial | 950 EUR | Referenz nicht belastbar (Streuung 4,07). Vintage-Niveau fuer das Modell liegt bei 700 bis 1.200 EUR, das Angebot also im Markt. |
| Omega Constellation Pie Pan | 1.650 EUR | Referenz nicht belastbar (Streuung 2,79). |
| Longines Chronographe Full Set | 499 EUR | Kein Modellname, kein Kaliber, Zahlung per PayPal Friends verlangt. |
| Longines Conquest Classic | 600 EUR | PayPal Friends verlangt, dazu ausdruecklicher Haftungsausschluss fuer den Versandweg. |
| ASUS ROG Astral RTX 5080 | 620 EUR | 39 Prozent des Marktwerts bei ausdruecklich verlangtem PayPal Freunde. Siehe Abschnitt oben. |
| Sony PlayStation 5 Pro 2 TB | 479 EUR | Selbes Konto wie die RTX 5080, ebenfalls nur PayPal Freunde. Siehe Abschnitt oben. |
| Deckel FP1 Fraesmaschine | 2.300 EUR | Konto 15 Tage alt, keine Abholung angeboten, dafuer "Versand ab 7,69 EUR" fuer eine Konsolfraesmaschine mit rund einer Tonne Gewicht. |
| Drehbank Heidenreich und Harbeck | 1.300 EUR | Referenz nicht belastbar (Streuung 6,58), kein externer Vergleichswert fuer die konkrete Maschine auffindbar. |
| Riese & Müller Packster 70 automatic | 4.249 EUR | Gepflegtes Rad mit lueckenloser Wartung, aber Ausstellungsraeder desselben Modells werden bei 4.999 EUR gehandelt. Bei 7.000 km Laufleistung ist der Abstand von 20 Prozent nicht belegbar. |
| Vespa Sprint Roller Bj. 2019 | 1.650 EUR | Anzeige unterscheidet nicht zwischen Sprint 50 und Sprint 125, der Median mischt beide. Kein belastbarer Referenzwert fuer die konkrete Variante gefunden, deshalb keine Meldung statt einer Schaetzung. |
| Ducati Monster 900 i.e. | 1.400 EUR | Austauschmotor, ausgehaengte Rueckholfeder am Schalthebel, Marving-Anlage und offener Kupplungsdeckel. Wertmindernde Umbauten und Defekt erklaeren den Preis. |
| Simson Schwalbe 4gang | 2.100 EUR | Ohne Papiere. Nach Pflichtregel fuer Klassiker damit nicht billig, sondern richtig bepreist. |
| Simson Habicht | 2.000 EUR | Ein einziges Bild, Bewertung 0,75, angegebene Erstzulassung 2002 passt nicht zur Baureihe. |
| Cube Reaction Hybrid EXC 625 | 700 EUR | 14.000 km auf Akku und Antrieb. Preis erklaert sich von selbst. |
| Hasselblad 500 C | 800 EUR | Referenz nicht belastbar (Streuung 3,94), fuenf Textzeilen ohne Angabe zu Objektiv, Magazin und Sucher. Umfang des Angebots nicht bestimmbar. |
| Vitra Eames Soft Pad Chair Leder | 850 EUR | Gasfeder defekt, sichtbare Lederabnutzung. Defekt erklaert den Preis. |
| USM Haller Sideboard 3x2 reinweiss | 1.250 EUR | Gewerblicher Anbieter, der zum eigenen Haendlerpreis inklusive Rechnung und Mehrwertsteuer anbietet. Kein Fund, sondern ein normal kalkuliertes Haendlerangebot. |
| USM Haller Sideboard Rubinrot | 990 EUR | Verkaeuferbewertung 0,42, dazu passen die genannten Masse 75 x 35 x 105 cm nicht zur Bezeichnung Sideboard. |
| USM Haller Container / Nachttisch | 225 EUR | Plausibel guenstig, aber fuer diese Einzelkonfiguration mit einer Schublade kein konkretes Vergleichsangebot auffindbar. Ohne bestaetigten Referenzwert keine Meldung. |
| Knoll Antimott Sessel | 150 EUR | Vom Verkaeufer als "Grundlage fuer eine Restaurierung" angeboten, ungereinigt. Restaurierungsbedarf erklaert den Preis. |
| Fahrrad Cube Race One | 595 EUR | Einziger Kandidat des Laufs mit `unkenntnis_bonus`, deshalb nicht nach Anzeigenqualitaet bewertet. Referenz aber nicht belastbar (Streuung 4,45), und ein Cube Race One Hardtail kostet neu rund 900 EUR - bei 595 EUR gebraucht bleibt kein Abstand. |
| iPhone 17 | 590 EUR | Konto seit April 2026 ohne Bewertung, nur Versand. Bei Apple-Geraeten kommt die nicht pruefbare iCloud-Aktivierungssperre hinzu, die aus der Ferne nicht auszuschliessen ist. |

### Gruppenweise verworfen

- **63 Kandidaten** mit `referenz.belastbar: false` oder `referenz.streuung` groesser 2,5: Der Median
  hat verschiedene Produkte gemischt und zaehlt nach Schritt 2a nicht. Soweit sie oben nicht einzeln
  aufgefuehrt sind, gab es auch keinen externen Ansatzpunkt fuer eine eigene Marktwertbestaetigung.
- **37 iPhones der Watchlist `apple-mobil`** ausser dem oben genannten iPhone 17: Abstaende von 75
  bis 250 EUR bei Medianen zwischen 225 und 545 EUR. Der Gebrauchtmarkt fuer iPhone 12 bis 15 ist so
  dicht, dass diese Spannen innerhalb der normalen Streuung nach Speichergroesse, Akkugesundheit und
  Zustand liegen. Kein Kandidat traegt eine Ausstattungsangabe, die einen belegbaren Abstand von
  20 Prozent gegen ein konkret vergleichbares Geraet zuliesse.
- **15 MacBooks**: dasselbe Bild, dazu bei jedem einzelnen die nicht aus der Ferne pruefbare
  iCloud-Sperre und moegliche MDM-Registrierung.
- **Rund 40 Fahrraeder und E-Bikes der Watchlist `ebike-rad`**: Die Referenzabfragen sind fast
  durchgehend Markenabfragen ("Fahrrad Cube Race", "Canyon Mountainbike") ueber Rahmengroessen,
  Modelljahre und Ausstattungsstufen hinweg. Wo die Referenz belastbar war, lag der Abstand unter
  20 Prozent oder das Rad hatte einen offengelegten Schaden, etwa das Canyon Endurace AL 7 mit dem
  Zusatz "beschaedigt" im Titel.
- **Uebrige Kandidaten aus `design-sammeln`, `notverkaeufe`, `modellbau-sammler`,
  `konsolen-sweep`, `musikinstrumente` und `vintage-hifi`**: entweder Referenz nicht belastbar,
  oder Abstand unter 20 Prozent, oder Zustand beziehungsweise Vollstaendigkeit aus der Anzeige nicht
  bestimmbar. Bei den `notverkaeufe`-Kandidaten fehlt durchgaengig ein Kleinanzeigen-Median, und
  keiner der neun war ohne eigene Zustandsbesichtigung bewertbar.

## Anmerkung zur Priorisierung

Nach der Vorgabe wurden zuerst die Kandidaten mit dem groessten absoluten Abstand und die liquide
Ware geprueft. Auffaellig ist, dass die drei gemeldeten Funde alle aus `design-sammeln` kommen,
waehrend keine der 15 Uhren, keine der sieben Drohnen, keines der 53 Apple-Geraete und die einzige
Grafikkarte durchgekommen ist. Bei den liquiden Kategorien fielen die Kandidaten fast ausnahmslos
in eine von drei Gruppen: Zahlungsforderung ausserhalb der Plattform, Konto aus dem Juli 2026 mit
Versand ohne Abholung, oder ein Abstand von 10 bis 19 Prozent zum extern bestaetigten Markt. Genau
die Ware, die sich am schnellsten weiterverkaufen laesst, zieht die meisten Betrugsversuche an.
