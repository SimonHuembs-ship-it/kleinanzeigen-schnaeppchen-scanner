# Lauf 2026-08-16, morgens (07:05 Uhr MESZ)

`candidates.json` generiert: 2026-08-16T06:44:57+02:00 (20 min alt, klar innerhalb der
Vier-Stunden-Grenze aus Schritt 1). Zeitraum des Sammellaufs: 2026-08-16T01:25:50+02:00 bis
2026-08-16T06:25:50+02:00, gesichtet 52.394 Anzeigen.

- Kandidaten in `candidates.json`: 182
- davon schon in `deal_log.csv`: 0
- Referenz nicht belastbar (`belastbar: false`, Streuung > 2,5 oder `referenz: null`): 56 —
  Median als nicht vorhanden behandelt
- inhaltlich geprueft: 41 (sortiert nach absoluter Ersparnis und nach Liquiditaet der Ware,
  also zuerst Uhren, Drohnen, Apple-Geraete und Fahrzeuge; die uebrigen 141 sind Massenware
  aus `ebike-rad`, `apple-mobil` und `design-sammeln` mit gemischtem Median oder liegen unter
  300 Euro absoluter Ersparnis)
- `unkenntnis_bonus` in diesem Lauf: 3 Kandidaten, alle `ebike-rad`, alle ohne belastbare
  Referenz (siehe unten)
- gemeldete Funde: 2

## Funde

| Ware | Preis | bestaetigter Marktwert | Abstand | Ort |
|---|---|---|---|---|
| [E-Bike Specialized Turbo Vado 4.0, Bj. 2020, 1.588 km](https://www.kleinanzeigen.de/s-anzeige/e-bike-specialized-vado-turbo-4-0/3485561800-217-4136) | 950 € | 1.280 € unterste belegte Gebrauchtgrenze, 2.099 € generalueberholt beim Haendler (Neupreis 3.199 €) | −26 % auf die Untergrenze, −55 % auf den Haendlerpreis | Meissen |
| [DJI Mavic 3 Classic mit DJI RC, 3 Akkus und Ladestation](https://www.kleinanzeigen.de/s-anzeige/dji-mavic-3-classic-drohne-mit-fernsteuerung/3485341484-245-7585) | 700 € | 903,89 € und 949,95 €, beide nur mit RC-N1 (Neupreis 1.749 € mit DJI RC) | −23 % bis −26 % bei besserer Ausstattung | Oberaudorf |

Belege:

- **Specialized Turbo Vado 4.0** — Neupreis des Modelljahrs 2020 laut Specialized 3.199 €.
  Upway fuehrt zwei generalueberholte Turbo Vado 4.0 (Diamant und ST) ab 2.099 € mit einem
  Jahr Garantie; fuer den freien Gebrauchtmarkt ist ein Abschlag von bis zu 60 Prozent auf den
  Neupreis belegt, das sind rund 1.280 €. Gegen diese unterste belegte Grenze liegen 950 €
  noch 26 Prozent darunter, und das bei 1.588 km, Originalkaufbeleg, Ladegeraet und beiden
  Akkuschluesseln. Der Kleinanzeigen-Median von 2.790 € (n = 99, Streuung 2,22) mischt
  neuere Baujahre bei und wurde deshalb nicht als Massstab verwendet — in `deals.json` steht
  statt `ersparnis_eur` ein `referenz_hinweis` mit dem selbst bestaetigten Niveau.
  Verkaeuferprofil passt zur Leitidee: Konto seit 2017, Bewertung 0,98, nur Abholung, 14
  eigene Fotos, und die Anzeige nennt von sich aus die Bremsscheibenstaerken in Millimetern —
  Angaben, die nur jemand macht, der das Rad in der Hand hatte.
- **DJI Mavic 3 Classic** — zwei konkrete Haendlerangebote fuer dasselbe Modell: buyZOXS
  903,89 € im Zustand sehr gut und eBay.de 949,95 € geprueft, beide jeweils nur mit der
  einfacheren RC-N1-Fernsteuerung. Das Angebot hier enthaelt die DJI RC mit integriertem
  Display (laut UVP 150 € Aufpreis: 1.599 € mit RC-N1 gegen 1.749 € mit DJI RC), drei Akkus
  und eine Ladestation, ist also besser ausgestattet als beide Belege. Der
  Kleinanzeigen-Median von 1.000 € (n = 53, Streuung 1,23) deckt sich mit dem belegten
  Niveau und wurde nicht als alleiniger Beleg benutzt. Kein Pflicht-Warnflag aus Schritt 2e)
  betroffen; die Mavic 3 Classic traegt die C1-Klassifizierung, das EU-Klassenproblem der
  aelteren Legacy-Drohnen greift hier nicht.

## Verworfene Kandidaten

### Marktwert bestaetigt, aber weniger als 20 Prozent Abstand

| Ware | Preis | bestaetigter Marktwert | Grund |
|---|---|---|---|
| Jaeger-LeCoultre Grande Master Ultra Thin, 40 mm Stahl (3485510216) | 4.750 € | 5.278–6.451 € gebraucht (Chrono24, Ref. Q1358420) | −10 % bis −26 % gegen Haendlerpreise, im Mittel rund 17 %. Der Median von 11.925 € stammt aus der Suche "Jaeger LeCoultre Grande" und mischt Reverso Grande und Master Grande Tradition ein. Der Verkaeufer begruendet den Preis selbst mit dem Stahlband — er kennt den Wert. |
| Rolex Datejust 41 Ref. 126300, Bj. 2018, Full Set (3484932776) | 7.800 € | 7.900 € (eBay.de, 2018 Full Set) bis 11.075 € (Chrono24) | Das einzige wirklich gleichartige Angebot, Baujahr 2018 mit Full Set, liegt bei 7.900 €. Damit ist 7.800 € Markt, kein Fund. Median 12.695 € mischt Jubilee-, Zweifarben- und Diamantvarianten. |
| Tudor Black Bay Chrono 79360N, ca. 5 Jahre, Full Set (3485239081) | 3.450 € | 4.081–5.599 USD gebraucht (Chrono24), unterste Grenze rund 3.750 € | −8 % gegen den niedrigsten Beleg. Median 6.795 € mischt Sondermodelle wie Flamingo Blue ein. |
| Apple MacBook Pro 14", M5, 16/512 GB (3484865386) | 1.222 € | 1.449 € neu (Geizhals), 1.595,87 € neu (eBay.de) | −16 % gegenueber dem guenstigsten Neupreis. Der Median von 2.249 € ist veraltet und mischt M5-Pro- und M5-Max-Konfigurationen ein. |
| DJI Mini 5 Pro, Kauf 09/2025, komplett (3485261509) | 600 € | 850 € gebraucht, 968–990 € neu (im Lauf vom 15.08. zweifach belegt) | −29 % waere ausreichend, aber ein baugleiches Geraet mit mehr Zubehoer (Fly More Combo, RC 2, Care Refresh) wurde am 15.08. zu 650 € gemeldet und steht in `deal_log.csv`; hier ist nur ein Akku dabei, kein Koffer, keine Restgarantie. Kein zweiter Fund desselben Modells in derselben Woche. |
| DJI Mavic 2 Pro Fly More Combo (3485608432) | 300 € | ab 437,70 € gebraucht (Beleg aus dem Lauf vom 15.08.) | Abstand ausreichend, aber die Anzeige nennt eine "Drone hacks Lizenz" und einen Abwurfmechanismus: Firmware-Umbau und Anbauten mindern den Wert und erklaeren den Preis. |
| Valve Steam Deck OLED 512 GB, Rechnung 12/2025 (3485077094) | 360 € | 400–450 € gebraucht (Neupreis 569 €) | Rund 15 % Abstand, dazu Verkaeuferbewertung 0,67 und nur Versand. Zu schwach. |
| Riese & Mueller Swing Silent, Bj. 2023, 130 km (3440640599) | 2.500 € | 2.800–3.200 € gebraucht (Neupreis 3.999 €) | −15 % bis −22 %, und die Anzeige steht ausweislich der niedrigen Anzeigen-ID seit Wochen zum selben Festpreis, ohne Abnehmer. Kein Fehlpreis. |
| Rohloff Speedhub 500/14, 32 Loch, mit Schaltbox (3485171911) | 450 € | 500–800 € gebraucht, stark km-abhaengig | Die Anzeige nennt weder Laufleistung noch Serviceintervall; ohne diese Angaben ist der Wert einer gebrauchten Speedhub nicht bestimmbar. Kein Fund, nur 429 € nominale Ersparnis. |
| Honda Fireblade CBR 900RR, Bj. 1994, 55.000 km (3485301653) | 2.300 € | 2.500–4.000 € je nach Zustand | Der Preis liegt nur knapp unter dem 25-Prozent-Quartil des Medians (2.350 €), und die Anzeige nennt weder HU noch Zustand. Kein belegbarer Abstand. |
| USM Haller Sideboard oliv, 152 cm (3276454241) und drei weitere USM-Anzeigen desselben Anbieters | 470–1.300 € | Haendlerpreise fuer aufbereitete Lagerware | Gewerblicher Aufbereiter mit Textbaustein-Anzeige und Pulverbeschichtung ab Werkstatt; der Median von 1.670 € gilt deutlich groesseren Konfigurationen. Keine Fehlbepreisung. |
| Neumann BCM-104 (3485623795) | 500 € | 450–550 € gebraucht (Neupreis rund 700 €) | Preis ist Markt, dazu Verkaeuferbewertung 0,38 und nur Versand. `referenz: null`, eigener Wert recherchiert. |
| Surron Light Bee, Bj. 2023, 8.500 km, Notverkauf (3485612909) | 3.400 € | 2.800–3.800 € gebraucht | `referenz: null`. Preis liegt mitten im Markt, und das defekte Lenkkopflager ist bereits eingepreist. |

### Der niedrige Preis erklaert sich von selbst

| Ware | Preis | Grund |
|---|---|---|
| BMW E36 323i Touring (3484853465) | 1.999 € | Als "Beschaedigtes Fahrzeug" eingestellt, 300.000 km, teilweise geschweisst, bis auf den Fahrersitz ausgebaut, "zum Schlachten oder Fertigstellen". |
| BMW E36 328i Limousine (3485246408) | 4.499 € | "Beschaedigtes Fahrzeug", Schweller muss geschweisst werden. |
| Mercedes SL 300 R129, Bj. 1991 (3485175419) | 9.500 € | Verdeck oeffnet nicht und Zentralverriegelung defekt — bei einem R129 ist genau die Verdeckhydraulik der teure Punkt, der Abschlag ist korrekt. |
| BMW 318i E30, Bj. 1988 (3485550493) | 5.000 € | Steht seit acht Jahren in der Garage, braucht laut Anzeige eine grosse Inspektion, keine gueltige HU genannt. |
| Alle uebrigen Youngtimer (3485558050, 3485556823, 3485305853, 3484982809, 3485208173, 3485242352, 3485427567, 3485528615) | 1.999–5.800 € | Durchweg Laufleistungen jenseits 200.000 km, abgelaufene HU oder Roststellen, teils Median mit Streuung ueber 2,5 ("318is E30", 4,55). |
| Simson S51 Garagenfund (3484905826) | 1.650 € | Motor fest, keine Papiere, keine Plakette — nach Schritt 2e) ist ein Klassiker ohne Zulassungsbescheinigung Teil II richtig bepreist, nicht billig. |
| Simson Star 4-2/1 (3484948779) | 1.100 € | Laeuft nicht, nicht fahrbereit, keine Papiere. |
| Simson Schwalbe KR 51/2 (3485152653) | 1.700 € | Ohne Papiere, Vergaser und Tank muessen nach Standzeit gereinigt werden. |
| Simson S51 mit KBA-Papieren (3485196703) | 1.850 € | Gewerblicher Simson-Haendler, "sollte dennoch komplett restauriert werden". |
| Simson Schwalbe KR 51/1, Simson Star SR4, Simson S51 N, MZ 125 SM, Simson-Rahmen und -Motor (3485135407, 3485055878, 3485600123, 3485555420, 3484945979, 3485305416, 3485365715) | 550–2.250 € | Restaurationsobjekte, Ersatzteile oder ausdrueckliche Bastlerfahrzeuge; der Median gilt fahrbereiten, zugelassenen Mopeds. |
| Mafell Tischkreissaege (3485321607) | 300 € | Streuung 3,29, und die Anzeige nennt keinen Typ; ohne Modell kein Wert bestimmbar. |
| Thorens TD 160 Super mit SME-Tonarm (3485057480) | 430 € | Streuung 6,25, Median mischt Laufwerke mit und ohne Tonarm; kein eigener Beleg gefunden. |

### Verkaeufer- oder Zahlungsprofil

| Ware | Preis | Grund |
|---|---|---|
| Rolex GMT Master, "NEU ungetragen, Box, Papiere" (3485576618) | 10.500 € | Vier Woerter Beschreibung ohne Referenznummer. Ohne bestimmbares Modell — 16710, 126710BLRO oder 126710BLNR unterscheiden sich um fuenfstellige Betraege — laesst sich kein Marktwert bestaetigen. Konto erst seit 09/2024. |
| Rolex Oyster Perpetual Lady-Date Ref. 6916/0 (3485387315) | 4.200 € | Der Preis liegt **ueber** dem Gebrauchtniveau einer 26-mm-Lady-Date aus den Siebzigern; der Median von 7.899 € entstand aus der Suche "Rolex Oyster Perpetual" und mischt moderne OP 36 und OP 41 ein. Phantomersparnis. |
| Omega Speedmaster Professional, Ref. 145.022 ST 71 (3485011436) | 4.000 € | Konto 18 Tage alt, nur Versand, dazu eine handwerklich perfekte Datenblatt-Anzeige mit exakter Referenz und Werknummer — genau das Muster aus der Leitidee. |
| Brompton C Line 6-Gang, Sonderfarbe Soft Grey, 50 km (3485317421) | 549 € | Gebrauchte C Line 6-Gang liegen bei rund 1.600 €, neue 2026er ab 1.635 €. Ein Verkaeufer, der die seltene Sonderfarbe benennt, die Originalrechnung und den ersten Service auffuehrt, kennt den Wert und verschenkt ihn nicht bei 31 Prozent. Dazu eingestellt unter "Zubehoer" und nur Versand. |
| CUBE Stereo HPC One22 Fully, Carbon (3484905840) | 900 € | Nur Versand zu 23,99 € fuer ein voll gefedertes Carbon-MTB, Bewertung 0,73 und ein Beschreibungstext ohne einen einzigen konkreten Mangel. |
| DJI Mini 3 Pro (3485517323) | 280 € | Konto 48 Tage alt, keine Bewertung, nur Versand, Beschreibung aus einem Satz. |
| Junghans max bill Tischuhr (3485013480) | 520 € | Konto 281 Tage, Abstand ohnehin nur rund 300 €. |

### Referenz nicht belastbar, kein eigener Wert gefunden

- Alle drei Kandidaten mit `unkenntnis_bonus` liegen hier: "Mtb fully Cube" (3485498129,
  850 €, Streuung 2,64), "E-Bike Cube" (3484846086, 800 €, Streuung 3,67) und "Rennrad Cube"
  (3484886779, 390 €, Streuung 3,35). Keine der drei Anzeigen nennt ein Modell — beim
  Mountainbike steht nur "Cube Fully", beim Rennrad gar nichts. Ohne bestimmbares Produkt
  laesst sich kein Vergleichswert belegen. Ausdruecklich **nicht** wegen der schlechten
  Anzeigenqualitaet verworfen, sondern weil die Ware nicht identifizierbar ist.
- Cube Kathmandu (3485542833, 550 €, Zustand "Neu", Streuung 1,43): Die Anzeige besteht aus
  drei Zeilen und verweist auf die Bilder. Der Median von 2.199 € mischt die Hybrid-Pedelecs
  ein; ob hier ein Kathmandu Hybrid oder ein einfaches Kathmandu-Trekkingrad steht, ist aus
  den Textdaten nicht zu entscheiden. Kein geschaetzter Wert eingetragen.
- Walter Knoll Sofa, zweimal derselbe Anbieter (3301004163, 2931221071, je 1.400 €):
  Streuung 3,29 und 3,50, Median mischt Zwei- und Dreisitzer sowie Stoff- und Lederbezuege.
  Beide Anzeigen tragen ausserdem alte Anzeigen-IDs, stehen also seit Monaten.
- Der gesamte Gibson-Block (3485310221, 3485130062, 3484902361): Streuung 2,62 bis 2,86, der
  Median mischt Les Paul Standard, Studio, Tribute und Modern. Kein Ersatzwert recherchiert.
- Tag Heuer Professional Chronograph (3485466589, 400 €, Streuung 3,96) und Rolex-Submariner-
  Zifferblatt als Ersatzteil (3485224765, 1.000 €, Streuung 11,76): Beim Zifferblatt
  vergleicht der Median ein Einzelteil gegen komplette Uhren.

## Nicht einzeln recherchiert

141 Kandidaten. Davon 59 aus `ebike-rad` und 27 aus `design-sammeln`, deren Median nach
Punkt a) Rahmengroessen, Modelljahre und Konfigurationen mischt, sowie 22 aus `apple-mobil`:
Dort liegen alle Angebote bei 45 bis 55 Prozent des Medians bei sehr enger Streuung
(1,18 bis 1,60), also genau im Korridor, in dem auf Kleinanzeigen die Koederanzeigen fuer
iPhones liegen; die absolute Ersparnis betraegt hoechstens 250 €, und keines der Angebote
nennt Akkugesundheit oder Seriennummer. Nach zwei bestaetigten Funden und dem Abarbeiten
aller Kandidaten oberhalb von 300 Euro Ersparnis wurde die Pruefung beendet; die
Zehn-Funde-Grenze aus Schritt 3 wurde nicht erreicht.

---

# Lauf 2026-08-16, abends (19:05 Uhr MESZ)

`candidates.json` generiert: 2026-08-16T15:48:27+02:00, also 3 Stunden 16 Minuten alt und
damit innerhalb der Vier-Stunden-Grenze aus Schritt 1. Zeitraum des Sammellaufs:
2026-08-16T09:19:09+02:00 bis 2026-08-16T14:19:09+02:00, gesichtet 184.206 Anzeigen.

- Kandidaten in `candidates.json`: 182
- davon schon in `deal_log.csv`: 0 (die beiden Funde des Morgenlaufs sind aus der Sammlung
  gefallen)
- Referenz nicht belastbar (`belastbar: false`, Streuung > 2,5 oder `referenz: null`): 59 —
  Median als nicht vorhanden behandelt
- inhaltlich geprüft: 44 einzeln, sortiert nach absoluter Ersparnis und Liquidität der Ware
  (Fahrzeuge, Uhren, Apple, Drohnen zuerst), dazu 44 Apple- und Drohnen-Kandidaten als Gruppe;
  die restlichen 94 liegen unter 1.000 Euro absoluter Ersparnis und sind Massenware aus
  `ebike-rad` und `design-sammeln`, überwiegend ohne belastbaren Median
- `unkenntnis_bonus` in diesem Lauf: 1 Kandidat (siehe unten)
- gemeldete Funde: 1

## Funde

| Ware | Preis | bestätigter Marktwert | Abstand | Ort |
|---|---|---|---|---|
| [Ducati Monster 1000, EZ 09/2003, 24.000 km](https://www.kleinanzeigen.de/s-anzeige/ducati-monster-m-1000-/3434713449-305-25915) | 2.400 € | 3.780 € (66.200 km), 4.200 € (66.101 km), 3.850 € (32.000 km); motorradonline.de: Baureihe beginnt knapp unter 4.000 € | −38 % gegen das nächstliegende Vergleichsangebot | Berlin-Rummelsburg |

Beleg: Drei konkrete Gebrauchtangebote derselben Baureihe (luftgekühlte Monster 1000,
Baujahr 2003) liegen zwischen 3.780 und 4.200 Euro, sämtlich mit deutlich höherer
Laufleistung; die Gebrauchtberatung von motorradonline.de nennt für die 1000er-Monster einen
Einstieg knapp unter 4.000 Euro bei über 40.000 km. Dieses Exemplar hat 24.000 km und HU bis
11/2026. Die Anzeige nennt von sich aus Kratzer, Schürfstellen am Auspuff, angegriffenen Lack
am Tank, sechs Jahre alte Reifen und eine nachzuziehende Kette — optische Mängel, die den
Abstand von 38 Prozent nicht erklären. Verkäuferprofil: Konto seit 2012, Bewertung 0,96, nur
Abholung, kein Versand, keine Zahlungsaufforderung außerhalb der Plattform.
Pflichtwarnflag Motorrad/L-Twin: Desmo-Ventilservice ist der größte Kostenblock und wird in
der Anzeige nicht erwähnt — steht als `risiko` in der Mail. Anmerkung: Die Anzeigen-ID
(3434713449) ist deutlich älter als das Einstelldatum, die Anzeige wurde also reaktiviert und
läuft möglicherweise schon länger.

## Verworfene Kandidaten

Nach absoluter Ersparnis geordnet, jeweils mit Grund.

| Kandidat | Preis | Grund der Verwerfung |
|---|---|---|
| Minibagger Yanmar SV17, Bj. 2014, 3.010 Bh | 12.300 € | Marktwert selbst geprüft: 2014er SV17 mit ~3.200 Bh liegen bei 18.663 € und 19.000 €, das sind aber osteuropäische Exportangebote; ein deutsches Angebot mit nur 1.581 Bh steht bei 11.800 €. Gegen das deutsche Niveau ist der Preis marktgerecht, der Kleinanzeigen-Median von 24.978 € nicht haltbar. |
| Jaeger-LeCoultre Grande Master Ultra Thin, Stahl 40 mm | 4.750 € | Referenzgruppe falsch: Die Query „Jaeger LeCoultre Grande" mischt Master Grande Tradition und Grande Reverso ein. Eigene Prüfung des richtigen Modells (Master Grande Ultra Thin Q1358420, Stahl, 40 mm): gebraucht rund 4.400–5.100 €. Kein 20-Prozent-Abstand. |
| BMW 318i E30, Bj. 1988, 169.000 km | 5.000 € | Stand acht Jahre in der Garage, braucht laut Anzeige eine große Inspektion, keine HU angegeben — der Preis erklärt sich aus dem Standschaden. |
| 318is E30 original, Bj. 1990, 290.000 km | 5.800 € | Referenz nicht belastbar (Streuung 4,55) und „muss geschweißt und lackiert werden", als beschädigtes Fahrzeug eingestellt: korrekt bepreist. |
| BMW E36 328i Limousine, Bj. 1996 | 4.499 € | Als beschädigtes Fahrzeug eingestellt, Schweller muss geschweißt werden, Automatik, 185.878 km — Preis erklärt sich selbst. |
| Rolex GMT Master, „neu, ungetragen" | 10.500 € | Keine Referenznummer, dreizeilige Beschreibung, Konto seit 2024, Neuware weit unter Marktpreis: exakt das Fälschungs- bzw. Betrugsprofil. Modell nicht identifizierbar, damit kein Marktwert bestätigbar. |
| Rolex Submariner „gepflegt gebraucht" | 8.500 € | Ein Satz Beschreibung, keine Referenznummer, kein Baujahr. Zwischen 14060, 16610 und 116610 liegen mehrere tausend Euro — Marktwert nicht bestätigbar. |
| Rolex Oyster Perpetual Lady-Date Ref. 6916/0, Vintage | 4.200 € | Referenzgruppe mischt Herrenmodelle ein. Die 26-mm-Lady-Date 6916 in Stahl liegt gebraucht deutlich unter dem Angebotspreis; kein Abschlag, sondern ein Aufschlag. |
| BMW E36 Coupé 316/318, 302.000 km | 4.300 € | Türgriff defekt, Klimakompressor-Spannrolle defekt, nachlackierte Teile, Innenraum verschlissen — die Mängel erklären den Preis. |
| Tudor Black Bay Chrono 79360N | 3.450 € | Gebrauchtniveau der 79360N liegt in derselben Größenordnung wie der Angebotspreis; der Median von 6.795 € stammt aus Neu- und Händlerangeboten. Kein 20-Prozent-Abstand. |
| Mercedes 190er W201, Bj. 1989 | 2.400 € | Ausdrücklich als Bastlerfahrzeug verkauft, springt nach zehn Jahren Standzeit nicht mehr an, HU abgelaufen. |
| BMW E36 320i Cabrio M-Paket | 5.800 € | Konto jünger als drei Tage, ausdrücklich Bastlerfahrzeug (hintere Wagenheberaufnahmen für die HU fällig). |
| Mercedes W124 „halbfertiges Restaurationsprojekt" | 4.000 € | Zwei Zeilen Beschreibung, unfertiges Projekt, unter Ersatzteile eingestellt — kein bestimmbares Fahrzeug, kein bestimmbarer Wert. |
| Cube Litening Rennrad SRAM Red, Gr. 56 | 1.250 € | Referenz nicht belastbar (Streuung 5,01), Beschreibung ohne Modelljahr, Laufradsatz und Rahmengeneration; Litening-Modelle spannen 900 bis 4.000 €, Marktwert nicht bestätigbar. |
| Raymon E-Bike Trekking | 900 € | Referenz nicht belastbar (Streuung 2,87), generischer Werbetext ohne Modell, Motor, Akkugröße und Baujahr — nicht bewertbar. |
| Vespa Sprint 125, Bj. 2020 | 2.000 € | Verliert Öl, rechts stark verkratzt — der Preis ist die Reparatur. |
| Simson S51 Neuaufbau 12V Vape | 1.950 € | Sauber beschriebener Neuaufbau, aber Konto am selben Tag angelegt, Versand mit Käuferschutz und Reservierung gegen Anzahlung: In der meistbetrogenen Kategorie überhaupt ist das kein Fund, sondern ein Risiko. |
| Mercedes W124 200D, 308.000 km | 1.999 € | Durchrostung am Radlauf, diverse Roststellen, Reifen fällig — Preis erklärt sich selbst. |
| BMW E36 318i, Lichtmaschine defekt | 2.000 € | Springt nicht an, ausdrücklich Bastlerfahrzeug. |
| Gibson Les Paul Junior Billie Joe Armstrong Signature 2010 | 1.700 € | Referenz nicht belastbar (Streuung 3,24, Query nur „Gibson Les Paul 2010"); das Signature-Modell liegt gebraucht in der Größenordnung des Angebotspreises. |
| Rolex Lady Date 6916, gewerblicher Händler | 2.999 € | Gewerbliches Angebot mit Gewährleistung und Zertifikat zum marktüblichen Händlerpreis, kein Privatschnäppchen. |
| Mercedes W201 190E, Bj. 1989 | 3.500 € | Gewindefahrwerk und Sportlenkrad verbaut (wertmindernde Umbauten am Klassiker), steht länger, „müsste einmal durchgeschaut werden". |
| DUCATI Monster 1000 | 2.400 € | **gemeldet** |
| Rolex Datejust 26 mm | 3.800 € | p_ratio 0,69, unter 20 Prozent Abstand zum Median, keine Referenznummer. |
| Cube Kathmandu, Zustand „neu" | 550 € | Beschreibung verweist nur auf Bilder, keine Variante und kein Baujahr; Kathmandu reicht vom Trekkingrad bis zum Hybrid-E-Bike, Marktwert nicht bestimmbar. |
| Truma Aventa Compact 2. Generation, NEU | 725 € | „Versand (DHL) und PayPal FF bitte" — ausdrückliche Zahlung ohne Käuferschutz, Pflichtausschluss nach Schritt 2c. |
| Uhr Jäger-LeCoultre | 1.400 € | Referenz nicht belastbar (Streuung 5,34), Modell im Titel nicht benannt. |
| Walter Knoll Sofa, Leder braun | 1.400 € | Referenz nicht belastbar (Streuung 3,5), gewerblicher Anbieter, Modellreihe nicht benannt — kein bestimmbarer Vergleichswert. |
| Riese & Müller Swing Silent, Bosch | 2.500 € | Neupreis 3.999 € von 2023; gebrauchte Swing Silent liegen in derselben Spanne, kein 20-Prozent-Abstand. Zudem nur ein Bild. |
| Suzuki GSX-R 1100 W | 1.200 € | Referenz nicht belastbar (Streuung 2,67). |
| Walter Knoll DRIFT Sessel | 490 € | „Zahlung per PayPal Freunde" — Zahlung ohne Käuferschutz, Pflichtausschluss. |
| Tudor Black Bay Full Set Rot | 2.599 € | p_ratio 0,66, unter 20 Prozent Abstand. |
| Mtb fully Cube (`unkenntnis_bonus`) | 850 € | Nicht wegen der Anzeigenqualität verworfen: Das Verkäuferprofil (Konto seit 2018, Bewertung 0,97, nur Abholung, Mängel offengelegt) passt zur Leitidee. Es fehlt aber jede Modellangabe, jedes Baujahr und jede Ausstattungsangabe; Cube-Fullys spannen 600 bis 4.000 €, die Referenz ist nicht belastbar (Streuung 2,64). Ohne bestimmbares Produkt kein bestätigbarer Marktwert — geschätzt wird nicht. |
| Omega Seamaster 36 mm Full Set | 1.030 € | Keine Referenznummer, Quarz und Automatik liegen weit auseinander — nicht bestimmbar. |
| Brompton C Line 6-Gang, „50 km gelaufen" | 549 € | Nahezu neuwertiges Premium-Faltrad zu 30 Prozent des Marktwerts, ausschließlich Versand, exakte Modellbezeichnung, keine Mängel: das handwerklich gute Betrugsprofil aus der Leitidee, kein Fund. |
| USM Haller Sideboard offen, oliv | 495 € | Gewerblicher Aufbereiter, offenes Element ohne Türen und Auszüge; der Median mischt geschlossene Konfigurationen ein. Der Preis ist der Marktpreis für diese Konfiguration. |
| Tag Heuer Professional Chronograph | 400 € | Referenz nicht belastbar (Streuung 3,96), Modell nicht benannt, PayPal Freunde. |
| Tag Heuer Aquaracer 500 | 1.299 € | Kronenverschraubung nur noch eine Vierteldrehung — Defekt am Dichtsystem erklärt den Preis; zudem PayPal Freunde. |
| Honda Fireblade CBR 900RR, Bj. 1994 | 2.300 € | Fünf Zeilen Beschreibung ohne Zustandsangaben bei 55.000 km, kein 20-Prozent-Abstand zum belegbaren Niveau. |
| Glashütte Nomos Uhr, ungetragen | 870 € | Modell nicht benannt (Tangente, Club, Orion liegen weit auseinander), Gravur wurde entfernt — Wert nicht bestimmbar. |
| Neumann BCM-104 (`referenz: null`) | 500 € | Neupreis des BCM 104 liegt in derselben Größenordnung; Verkäuferbewertung 0,38, nur Versand. Kein Abstand. |
| Surron Light Bee (`referenz: null`) | 3.400 € | Lenkkopflager defekt, „Notverkauf"; mit Fox-40-Umbau liegt der Preis im Marktkorridor. |
| Haushaltsauflösung Berlin-Mahlsdorf (`referenz: null`) | 1.500 € | Konvolut ohne bestimmbaren Inhalt, kein bewertbarer Einzelgegenstand. |
| 20 alte Petroleumlampen (`referenz: null`) | 580 € | Konvolut, kein belastbarer Referenzwert für Sammlerlampen dieser Zusammenstellung recherchierbar. |
| 44 Kandidaten aus `apple-mobil`, `macbook` und `optik-drohnen` | 150–1.300 € | Sammelverwerfung: iPhones und MacBooks ohne Speichergröße, Zustandsangabe oder Modelljahr, durchweg bei rund 50 Prozent des Medians — das Muster für gesperrte, defekte oder nicht existente Geräte. Höchste Einzel-Ersparnis 639 €, keiner mit belastbarer Modellangabe. Pflichtwarnflag Apple (iCloud-Sperre, MDM) wäre bei jedem einzelnen zu setzen gewesen. |
| übrige 94 Kandidaten | < 1.000 € Ersparnis | Nach Prioritätsregel (größter absoluter Abstand, liquide Ware zuerst) nicht mehr geprüft: durchweg Fahrräder, USM-Regale und Kleinuhren mit gemischtem Median und Ersparnissen unter 1.000 €. |
