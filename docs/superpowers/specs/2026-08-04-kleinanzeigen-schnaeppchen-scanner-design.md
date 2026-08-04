# Kleinanzeigen Schnäppchen-Scanner: Design

Stand: 4. August 2026

## 1. Ziel

Jeden Morgen um 7 Uhr eine E-Mail mit Angeboten von kleinanzeigen.de, die deutlich
unter Marktwert liegen und von seriösen Verkäufern stammen. Kein Kleinanzeigen-Login,
damit kein Konto gesperrt werden kann. Preisrahmen offen: ein günstiger Porsche 992
gehört genauso hinein wie ein Dometic MS-50 Tempomat.

Kommt an einem Tag nichts über die Schwelle, kommt keine Mail. Ein leerer Posteingang
ist ein gültiges Ergebnis.

### Die Leitidee

Der Scanner sucht nicht nach guten Anzeigen, sondern nach schlechten Anzeigen von
ehrlichen Leuten.

Das ist kein Wortspiel, sondern das zentrale Rechercheergebnis. Betrugsanzeigen sind
handwerklich **besser** als echte Schnäppchen: scharfe freigestellte Katalogfotos,
exakte Modellbezeichnung mit Spezifikationen, keine Mängel genannt, Versand angeboten.
Wer dagegen den Wert seines geerbten Objektivs nicht kennt, fotografiert unscharf im
Wohnzimmer, schreibt den Modellnamen falsch, erwähnt den Kratzer und will nur Abholung.

Genau dieses Profil ist gleichzeitig das schnäppchenreichste und das betrugssicherste,
denn mit reiner Abholung lässt sich nicht betrügen. Der Scanner bürstet die üblichen
Qualitätsheuristiken deshalb bewusst gegen den Strich.

## 2. Verifizierte Grundlagen

Alle Werte am 4. August 2026 gemessen, nicht angenommen.

### Datenquelle

Die Mobile-JSON-API unter `api.kleinanzeigen.de`, angesprochen über das PyPI-Paket
`kleinanzeigen-api` (Version 0.4.0). Kein Login. Die Basic-Auth-Zugangsdaten sind
App-Verteilwerte aus dem Android-Client, keine persönlichen Geheimnisse, und über
Umgebungsvariablen austauschbar.

| Eigenschaft | Messwert |
|---|---|
| Frische | neueste Anzeige 4 bis 13 Sekunden alt |
| Seitengröße | maximal 100, darüber stillschweigend gedeckelt |
| Offset-Decke | 10.000 pro Query, danach leere Liste ohne Fehler |
| Ergebnis-Cache | rund 2 Minuten pro exakter Query |
| Durchsatz ungedrosselt | 3,8 Requests pro Sekunde ohne einen einzigen 429 |
| Anzeigenaufkommen | rund 11 neue Anzeigen pro Sekunde site-weit |

### Verfügbare Felder pro Anzeige

Aus der Suche: `id`, `title`, `description`, `price`, `price_type`, `url`, `city`,
`zip_code`, `latitude`, `longitude`, `posted`, `poster_type`, `category_id`, `images`,
`attributes`.

Zusätzlich aus dem Detailabruf: `user-since-date-time` (Registrierungsdatum),
`user-rating` (averageRating 0 bis 1), `userBadges` (rating, friendliness, reliability
mit Level 0 bis 3), `contact-name`, `user-id`, `seller-account-type`, `shipping-options`.

`shipping-options` ist verifiziert entweder `null` (nur Abholung) oder eine Liste wie
`[HERMES_001, HERMES_002, DHL_001]`. Das ist die maschinelle Grundlage der wichtigsten
Filterregel.

### GitHub Actions als Laufzeitumgebung

Am 4. August 2026 verifiziert: Ein Runner in Azure West-US-2 (IP 52.156.141.245,
AS8075 Microsoft Corporation) erreicht die API ohne Einschränkung. 25 Treffer,
Detailabruf inklusive Verkäuferdaten erfolgreich. Weder eine deutsche IP noch ein
Proxy ist nötig.

Das beweist Erreichbarkeit, nicht Dauerbetrieb unter Last. Deshalb Abschnitt 10.

### Zwei Fallen, die ohne echte Daten übersehen worden wären

**Gesuche verseuchen jede Trefferliste.** Kleinanzeigen mischt Gesuche und
Händler-Ankauf ungefiltert unter die Angebote. Eine reale Anzeige lautet
`Suche Porsche 911 TURBO Ankauf 993 964 930 996 997 991 G Modell`. Solche Inserate
enthalten sämtliche Typcodes auf einmal und matchen deshalb jede denkbare Suche.

**Markenfilter allein sind wertlos.** Eine Suche nach "Porsche" liefert überwiegend
Cayenne, Macan, Panamera, Taycan, Boxster und Cayman. Positives Modell-Matching ist Pflicht.

## 3. Architektur

Drei Stufen, bewusst getrennt.

```
06:15  Stufe 1  Sammler     GitHub Action, Python
                            Rohdaten holen, deterministisch filtern,
                            Referenzpreise rechnen, Seriosität scoren
                            -> candidates.json, commit, push

07:00  Stufe 2  Gutachter   Claude-Routine im geklonten Repo
                            candidates.json lesen, inhaltlich urteilen
                            -> email_output.html, deal_log.csv, commit, push

on push Stufe 3 Versand     GitHub Action, Resend
                            Mail an den Empfänger
```

Die Trennung hat drei Gründe. Erstens macht Python das Mengengeschäft über
zehntausende Anzeigen deterministisch und kostenlos, während Claude nur dort urteilt,
wo Urteilsvermögen gebraucht wird. Zweitens ist der teure Schritt dadurch auf 20 bis
40 Kandidaten begrenzt. Drittens braucht die Routine-Sandbox keinen Netzzugriff auf
Kleinanzeigen, weil sie die Daten aus dem Repo liest.

## 4. Stufe 1: der Sammler

### 4.1 Zwei Suchverfahren

**Kategorie-Sweep für breite Ziele.** Über die undokumentierten Parameter `modAfter`
und `modBefore` werden Zeitfenster der letzten 24 Stunden abgefahren. Diese Parameter
sind über `search_metadata` auffindbar und verifiziert wirksam, werden vom Client aber
nicht durchgereicht, also direkt über `api._get(f"{API_HOST}/api/ads.json", params=...)`
ansprechen.

Regeln für den Sweep:

- Fenster so schneiden, dass `numFound` je Fenster unter 10.000 bleibt
- 30 Prozent Überlappung zwischen aufeinanderfolgenden Fenstern
- `size=100`
- Dedupe über `ad_id`, nicht über Position

Der Grund für Überlappung und Dedupe ist gemessen: Ein naiver Zehn-Seiten-Scan lieferte
1.000 Slots, aber nur **796 eindeutige Anzeigen**, und es fehlten nachweislich Anzeigen,
deren Zeitstempel mitten im gescannten Fenster lag. Der Index ist vollständig, die
Paginierung ist es nicht. Tiefes Blättern darf niemals als Vollscan gelten.

Der Sweep ist **tippfehlerimmun**, weil überhaupt keine Suchbegriffe im Spiel sind.
"Porshe 911 Carerra" landet genauso im Netz wie die korrekte Schreibweise.

**Keyword-Suche für schmale Ziele.** Bei Nischen mit wenigen Anzeigen pro Tag wäre ein
Sweep Verschwendung. Stattdessen die korrekte Schreibweise plus fünf bis acht
Falschschreibungen als eigene Suchen. Weil der Ergebnis-Cache an der exakten Query
hängt, sind Varianten ohnehin eigene Cache-Einträge und damit frisch.

### 4.2 Vorfilter, in dieser Reihenfolge

Alles hier ist deterministisch und kostet keinen zusätzlichen Request.

1. **Nur Angebote.** `ad_type == "OFFERED"`, zusätzlich Titel verwerfen bei
   `/^\s*(suche|ankauf|kaufe|gesucht)\b/i` oder `/\b(suche|ankauf)\b.*\b(ankauf|suche)\b/i`.
2. **Emoji und Trennzeichen strippen** vor jedem Matching. Reale Titel enthalten
   `⭐️‼️`, `|`, `/`, `#`, `*`.
3. **Modell-Matching** gegen die `muster` des Watchlist-Eintrags, case-insensitive.
   Wortstellung ist frei, Titel werden bei rund 65 Zeichen hart abgeschnitten, also
   niemals auf das Titelende matchen.
4. **Ausschlussliste** des Watchlist-Eintrags.
5. **Fälschungen verwerfen:**
   `/\b(nachmache|nachbau|replika|replica|clone|klon|kopie|fake|1\s*:\s*1|wie\s+original|kein[e]?\s+original)/i`
6. **Fantasieprodukte verwerfen.** Belegter Realfall: "Apple MacBook Neo 13 Zoll
   A18 Pro" für 325 Euro. Das Produkt existiert nicht, der A18 Pro ist ein
   iPhone-Chip. Für Apple, Leica und andere Marken mit klarer Modellpalette prüft der
   Scanner gegen eine Whitelist echter Modellnamen und flaggt alles außerhalb als
   Betrug, nicht als Schnäppchen.
7. **Dedupe** gegen `seen_ads.csv`. Wichtig: `posted` ist das Reaktivierungsdatum, nicht
   das Ersteinstelldatum. Rund 2 Prozent der Treffer in Datumssortierung sind gebumpte
   Altanzeigen. Die ID ist der einzige verlässliche Anker.

### 4.3 Referenzpreis

Für jeden verbliebenen Treffer eine Suche nach der Modellbezeichnung, aufgebaut aus
`referenz_query` des Watchlist-Eintrags plus den unterscheidenden `attributes` des
Treffers (Speichergröße, Baujahr, Variante).

- Median und 25. Perzentil aus mindestens **8** Vergleichsanzeigen
- `p_ratio = price / median`
- Weniger als 8 Vergleichsanzeigen: kein `p_ratio`, Treffer geht mit dem Flag
  `referenz: fehlt` an Stufe 2 weiter statt still zu verschwinden

Validiert: Für eine iPhone-15-Pro-Max-Anzeige zu 600 Euro ergaben 50 Vergleichsanzeigen
einen Median von exakt 600 Euro. Der Treffer wurde korrekt als kein Schnäppchen erkannt.

**Das Schnäppchenfenster hat eine Untergrenze.** Das ist eine Korrektur gegenüber der
naheliegenden Annahme "je billiger desto besser":

| `p_ratio` | Behandlung |
|---|---|
| über 0.80 | verwerfen, kein Schnäppchen |
| 0.45 bis 0.80 | **das eigentliche Fenster**, hier liegen die echten Funde |
| 0.25 bis 0.45 | nur mit außergewöhnlich vielen grünen Flaggen, sonst verwerfen |
| unter 0.25 | verwerfen, statistisch Betrug oder Totalschaden. Dieselbe Grenze taucht in 4.4 als harter Ausschluss auf, die strengere Regel gewinnt |

Ein Inserat unter rund 50 Prozent Marktwert ist statistisch eher Betrug, Motorschaden
oder Totalschaden als ein Fund. Diese Grenze ist für Fahrzeuge belegt und lässt sich
auf Elektronik übertragen, wo "zu billig" das häufigste Betrugssignal ist.

**Angebotspreise sind keine Transaktionspreise.** Bei Fahrzeugen liegen Angebotspreise
8 bis 15 Prozent über den tatsächlich erzielten Preisen, bei Verbrennern 5 bis 12 Prozent.
Der Referenzmedian wird deshalb bei Fahrzeugen um 10 Prozent nach unten korrigiert, sonst
wirkt praktisch jedes Inserat wie ein Schnäppchen.

**Aufmerksamkeitspreise hart filtern.** `1 €`, `123 €` und ähnliche Lockpreise sind ein
verbreiteter Trick, um in Preissortierungen oben zu stehen. Ohne diesen Filter besteht
die Trefferliste überwiegend daraus.

### 4.4 Detailabruf und Seriositäts-Scoring

Erst jetzt `get_ad` pro Kandidat, denn dieser Schritt kostet einen Request.

**Harte Ausschlüsse.** Trifft eine dieser Regeln, wird die Anzeige verworfen und nicht
gescort.

| Regel | Prüfausdruck auf Titel plus Beschreibung |
|---|---|
| Messenger-Wechsel | `/\b(whats\s*app|wa\.me|telegram|t\.me|signal|viber|threema)\b/i` |
| Externer Link | `/\b(?:https?:\/\/|www\.)(?!(?:www\.)?kleinanzeigen\.de)[a-z0-9.-]+\.[a-z]{2,}/i` |
| Zahlung ohne Schutz | `/\b(freunde\s*(und|&|\+)\s*familie|f\s*&\s*f|western\s*union|money\s*gram|paysafe|bitcoin|krypto|usdt|amazon[- ]?gutschein)/i` |
| Fake-Treuhand | `/\b(treuhand(service|konto)?|escrow|kleinanzeigen[- ]?(liefer|versand)service)/i` |
| Auslandslegende | `/\b(bin\|befinde\s*mich\|arbeite)\s+(derzeit\|momentan\|gerade)?\s*(im\|in)\s+ausland\b/i`, `/\b(bohrinsel|auslandseinsatz|stationiert)\b/i` |
| Spedition holt ab | `/\b(spedition|logistikpartner)\b.{0,60}\b(holt\s+ab|übernimmt|organisiert)\b/i` |
| Vorab-Gebühren | `/\b(zollgebühren|einfuhrumsatzsteuer|transportversicherung|kaution)\b.{0,80}\b(vorab|im\s*voraus|zuerst)\b/i` |
| KI-Prompt-Rest | `/^\s*(natürlich|gerne|klar)\s*[,!]\s/i`, `/\bhier\s+ist\s+(die\|eine)\s+(fertige\s+)?(verkaufs)?anzeige\b/i` |

Die KI-Regel stammt aus einem Realfund: Eine Corsair-RAM-Anzeige unter halbem
Marktpreis begann wörtlich mit "Natürlich, hier ist die fertige Verkaufsanzeige für".

**Die Kill-Regel.** Unabhängig von jedem Score:

> Kein Abholung möglich **und** kein Käuferschutz **und** `p_ratio < 0.70`: verwerfen.

Diese eine Zeile schneidet praktisch den gesamten Vorkasse-Betrug weg. Sie kostet die
Untermenge legitimer Fernverkäufe ohne Plattformzahlung, was für einen privaten
Schnäppchenscanner ein guter Tausch ist.

**Punkteskala.** Start bei 50, geklemmt auf 0 bis 100.

Rote Flaggen: Konto jünger als 3 Tage (−30), 3 bis 30 Tage (−18), 30 bis 180 Tage (−8).
Takeover-Signatur, also Konto älter als 540 Tage bei ausschließlich frischen Anzeigen und
mindestens 3 Anzeigen (−35). Bewertung unter 0,70 (−25), zwischen 0,70 und 0,85 (−10).
Kein Käuferschutz trotz angebotenem Versand (−30). Abholung ausgeschlossen (−30).
Abholort faktisch unerreichbar, etwa Inseln (−25). Vorkasse gefordert (−25). Preis
zwischen 25 und 45 Prozent des Marktwerts (−20). Höchstens ein Bild bei über 200 Euro
(−12). Zeitdruckformeln (−12). Gewerbetext auf Privatprofil (−12).

Grüne Flaggen: Konto älter als 730 Tage (+12). Historie über mindestens 3 verschiedene
Monate gestreut (+15). Bewertung ab 0,90 zusammen mit Zuverlässigkeits-Level 2 (+15).
Abholung möglich und beworben (+20). Käuferschutz verfügbar (+18). Mängel offengelegt,
etwa Kratzer oder Gebrauchsspuren (+15). Legitime Preisbegründung wie Umzug, Nachlass,
Sammlungsauflösung (+15). Mindestens vier Realfotos (+12). Detailtiefe mit Angaben wie
Akkukapazität, Betriebsstunden oder Kaufdatum (+12).

**Warum Kontoalter und Bewertung schwach gewichtet sind.** Aus dem
Kleinanzeigen-Hilfecenter: Das höchste Zuverlässigkeits-Abzeichen (Level 3) verlangt
sechs Bewertungen aus maximal zehn berücksichtigten. Level 2 verlangt drei. Bewerten
darf man sich, sobald zwei Nachrichten gewechselt wurden und 24 Stunden vergangen sind,
**ganz ohne Kauf**. Sechs abgesprochene Kontaktpaare ergeben also das höchste Abzeichen
der Plattform. Dazu sind gekaperte Alt-Konten mit guter Bewertung der dokumentierte
Standardvektor für Vorkassebetrug.

Konsequenz: Kontoalter ist kein Gütesiegel, sondern ein **Konsistenzanker**. Nicht
"wie alt ist das Konto", sondern "passt die Anzeigenhistorie zum Kontoalter". Ein Konto
von 2016, dessen sämtliche zwölf Anzeigen von heute stammen, ist gefährlicher als ein
zwei Wochen altes Konto mit drei plausiblen Möbelanzeigen.

Intern heißt das Ergebnis deshalb nie "seriös", sondern "keine roten Flaggen".

### 4.5 Der Unkenntnis-Bonus

Trifft diese Kombination zu, wird der Kandidat hochpriorisiert, obwohl er nach
klassischen Qualitätsmaßstäben schlecht aussieht:

```
p_ratio < 0.60
und Abholung möglich
und kein Versand angeboten
und höchstens 3 Bilder
und (Tippfehler im Modellnamen oder auffallend generischer Titel)
und Kontoalter über 365 Tage
und höchstens 5 Anzeigen des Kontos
und kein harter Ausschluss
```

Für Betrüger ist diese Konstellation unattraktiv, weil ohne Versand kein Geld ohne
Übergabe fließt. Für den Käufer ist sie der sichere Hafen.

### 4.6 Entwarnung gegen Fehlalarme

Haushaltsauflösung und Kontoübernahme sehen zunächst identisch aus, nämlich viele
Anzeigen, alle frisch. Unterscheidung:

```
haushaltsaufloesung_wahrscheinlich =
    anzahl_anzeigen >= 5
    und median(preise_des_users) < 80
    und anteil_abholung > 0.8
    und anzahl_verschiedener_staedte == 1
```

Trifft das zu, werden Takeover-Signatur und Kategorie-Bruch neutralisiert.

Ein weiteres Kaufsignal steht nur im Website-HTML, nicht in der API: der durchgestrichene
Altpreis bei reduzierten Anzeigen, im Format `330 € VB 420 €`. Das bedeutet, der
Verkäufer hat bereits nachgegeben und ist verhandlungsbereit. Abrufbar per `curl` mit
Browser-User-Agent, Preis-Container
`aditem-main--middle--price-shipping--price"[^>]*>(.*?)</p>`. Optionaler Anreicherungs-
schritt für die Top-Kandidaten, kein Pflichtbestandteil.

### 4.7 Externe Marktreferenzen für Stufe 2

Der Kleinanzeigen-Median ist die Standardreferenz, aber bei hochpreisigen Kategorien
gibt es bessere Anker. Stufe 2 zieht sie per Websuche heran, wenn der Kandidatenwert
über 1.000 Euro liegt.

| Kategorie | Referenz | Warum |
|---|---|---|
| Porsche 911 | 911finder.de / MarqueScope | Mediane je exakter Generation plus Standzeit, aus tatsächlichen Verkäufen |
| Tesla | AutoScout24 25-Prozent-Quartil | Median verzerrt durch Neuwagen-nahe Angebote |
| Youngtimer | classic-analytics **Zustand 3** | Zustand 2 ist auf Kleinanzeigen praktisch nie realistisch |
| HiFi und Studio | hifishark.com | aggregiert über 40 Marktplätze inklusive Kleinanzeigen, Median plus Spanne |
| Leica | usedlenstracker.com, usedcameratracker.com | liefert fertige Deal-Fair-High-Schwellen plus Verkaufsgeschwindigkeit |
| Kameras allgemein | MPB.com | reale Händlerpreise nach Zustandsstufe |
| Games und Konsolen | pricecharting.com | USD, eBay-basiert, als Obergrenze lesen |
| Apple und IT | Refurbished-Händler als Anker, Ankaufspreise als Untergrenze | kein Aggregator vorhanden |

Für Fahrzeuge und Klassiker gilt: Bezugsgröße ist immer die **exakte Generation**, nie
ein Markendurchschnitt. Bei Porsche liegt die Spreizung zwischen 74.900 und 167.838 Euro
innerhalb derselben Modellbezeichnung, ein Aggregat wäre wertlos.

### 4.8 Kategoriespezifische Pflichtregeln

Diese Regeln haben in der Recherche jeweils einen konkreten Realfall hinter sich. Ohne
sie produziert der Scanner teure Fehltreffer.

**Fahrzeuge allgemein.** Gesuche und Händler-Ankauf zuerst filtern, siehe 4.2. Bei
Klassikern ist die Papierlage wichtiger als die Technik: In 4 von 26 Simson-Titeln stand
`mit KBA Papieren` oder `inkl. Gutachten` im Titel, wofür der Verkäufer bei 1.700 bis
3.000 Euro Marktwert knappe Titelzeichen opfert. Ein Inserat ohne Zulassungsbescheinigung
Teil II ist nicht billig, sondern richtig bepreist.

**Tesla.** Kilometerstand gegen die Akkugarantiegrenze prüfen, denn die liegt bei
Model 3 und Model Y mit Heckantrieb bei 160.000 Kilometern. Ein günstiges Fahrzeug bei
155.000 Kilometern ist korrekt bepreist, nicht unterbewertet. "FSD im Wert von 7.500 Euro
inklusive" ist **kein** Wertaufschlag, sondern ein Prüfpunkt: Tesla hat gekaufte Optionen
in Gebrauchtwagen schon per Fernupdate deaktiviert. Premium Konnektivität ist ein Abo für
9,99 Euro im Monat und niemals im Fahrzeug enthalten.

**Porsche 991 und 992.** Zylinderlaufbahnschäden gehören an 996 und 997.1, nicht an
991 oder 992. Wer dort danach filtert, filtert am Problem vorbei. Die realen Kostenrisiken
sind Wasserpumpe (1.500 bis 2.500 Euro, vor allem Modelljahr 2017), Wastegate und
Turbolader (5.000 bis 7.000 Euro pro Seite) und PDK-Mechatronik (10.000 bis 15.000 Euro).

**Youngtimer.** Die höchsten Wertzuwächse liegen nicht bei den Ikonen, sondern bei
ehemaligen Alltagsautos im Bereich 2.000 bis 6.000 Euro, deren Bestand durch Verschrottung
kollabiert ist: Honda CRX plus 260 Prozent, BMW 325i Baur plus 245 Prozent, Volvo 850 T5
plus 228 Prozent seit 2020. Umgekehrt sind billige Oberklasse-Youngtimer **Wertfallen**:
W140 S 320 in Zustand 3 kostet 7.100 Euro, Audi A8 4.2 nur 5.400 Euro, und beide fressen
das Vielfache an Steuergeräte-Reparaturen. Ein naiver Scanner spuckt genau diese Fahrzeuge
als Top-Treffer aus, deshalb gehören sie auf die Ausschlussliste.

Der beste Filterhebel bei Klassikern ist Zustandsnoten-Arbitrage: Zustand 3 ist
definitionsgemäß rostfrei. Ein als "Bastler" inseriertes, tatsächlich rostfreies Fahrzeug
ist der eigentliche Fund, während ein als "Zustand 3" beworbenes Fahrzeug mit Rostbildern
um etwa Faktor 2 fehlbewertet ist.

**Grafikkarten.** Umgeflashte RTX 3090, die als 4090 verkauft werden, sind 2026 ein
Massenphänomen, inklusive gefälschtem Die-Label auf abgeschliffenem Chip. Ein Techniker
fand unter vier eingeschickten 4090 drei Fälschungen. Prüfpunkte für die Handlungs-
empfehlung: GPU-Z zeigt bei Manipulation ein `[FAKE]`-Präfix, der QR-Code sitzt auf echten
4090 exakt in der linken unteren Ecke des Substrats. Eine 4090 deutlich unter 1.700 Euro
bekommt ein Pflicht-Warnflag.

**Konsolen.** Nintendo sperrt Accounts bei gebraucht erworbenen Switch-2-Spielen, wenn
unerlaubte Vervielfältigung erkannt wird. Reale Sperrfälle sind dokumentiert. Jede
Switch-2-Anzeige mit Spielen bekommt ein Pflicht-Warnflag.

**AirPods.** Höchstes Fälschungsrisiko im ganzen Datensatz. Ein dokumentierter Fake trug
eine echte, aber gestohlene Seriennummer und bestand die Apple-Prüfung. Unter 50 Euro ist
ein Warnsignal, kein Kaufsignal.

**Enterprise-Netzwerktechnik.** Cisco und Juniper gehören auf die Ausschlussliste, nicht
auf die Zielliste: Smart Licensing macht die Hardware für Zweitkäufer weitgehend wertlos,
und Verkäufer legen das praktisch nie offen. Threadripper-Pro-CPUs aus OEM-Systemen von
Lenovo oder Dell sind per Vendor-Lock ans Herstellerboard gebunden. Rack-Server älterer
Generationen sind in Deutschland illiquide, weil getestete Refurbished-Ware mit Garantie
bei 580 Euro liegt.

**NAS und Server mit Platten.** Wert primär nach verbauten Festplatten und RAM bewerten,
nicht nach Gehäusemodell, denn die Speicherkrise hat die Komponentenpreise entkoppelt.
Ein DS220+ inklusive zweier 6-TB-Platten für 250 Euro lag unter dem reinen Plattenwert.
Zusätzlich ein DSGVO-Hinweis in der Handlungsempfehlung, weil Gebrauchtgeräte regelmäßig
mit fremden Daten verkauft werden.

### 4.9 Die drei stärksten Fundmuster

Diese Muster bekommen im Ranking Vorrang, weil sie in der Recherche die größten
Wertabstände zeigten.

**Generischer Titel bei Spezialware.** "Alte Stereoanlage Dachboden", "Fotoausrüstung
Nachlass", "Tonstudio Auflösung", "Gaming PC komplett". Der stärkste Einzelbefund: Ein
Neumann KM84 ist ein unscheinbares kleines Stäbchenmikrofon und kostet 2.650 bis 2.980
Euro das Stück. Aus Nachlässen sowie Kirchen- und Schulauflösungen wird sowas regelmäßig
auf 100 bis 200 Euro taxiert. Ebenso: die im Komplett-PC versteckte Grafikkarte, bei der
der Gesamtpreis unter dem Kartenwert liegt.

**Modellverwechslung innerhalb einer Familie.** Die Revox PR99 ist die professionelle
Ausführung der optisch ähnlichen B77 und kostet 1.500 bis 4.590 statt 576 Euro. Wer
"Revox Tonbandgerät" schreibt und sich am A77-Niveau orientiert, unterbepreist um Faktor
3 bis 5. Gleiches Muster: Leica R statt M, Zeiss ZM statt Leica M.

**Systematische Fehlbepreisung durch Marktverschiebung.** Wer Grafikkarte, RAM oder SSD
nach dem Preisgefühl von 2024 einstellt, liegt 2026 massiv unter Markt, weil die
Speicherknappheit die Preise gedreht hat. Die RTX 5090 kostete im August 2025 noch 2.249
Euro und liegt jetzt bei mindestens 4.250 Euro. Gebrauchte GPUs, RAM, SSDs, NAS und
Konsolen sind derzeit im Wert steigende Güter.

### 4.10 Ausgabe

`candidates.json`, sortiert nach absoluter Ersparnis, maximal 40 Einträge:

```json
{
  "generiert": "2026-08-05T06:31:12+02:00",
  "zeitraum": {"von": "2026-08-04T07:00:00+02:00", "bis": "2026-08-05T06:15:00+02:00"},
  "statistik": {
    "gesichtet": 61240, "nach_modellmatch": 812, "nach_vorfilter": 430,
    "nach_preisschwelle": 96, "nach_scoring": 31, "requests": 1840,
    "laufzeit_sekunden": 1120
  },
  "kandidaten": [
    {
      "id": "3476253175",
      "watchlist_id": "porsche-911-992",
      "titel": "Porshe 911 Carrera 991.2 aus Nachlass",
      "url": "https://www.kleinanzeigen.de/s-anzeige/...",
      "preis": 58000,
      "preis_typ": "NEGOTIABLE",
      "referenz": {"median": 92000, "p25": 84000, "n": 23, "query": "Porsche 911 991.2 Carrera"},
      "p_ratio": 0.63,
      "ersparnis_eur": 34000,
      "ort": "Uelzen", "plz": "29525",
      "eingestellt": "2026-08-04T18:22:10+02:00",
      "bilder": ["https://img.kleinanzeigen.de/..."],
      "beschreibung": "...",
      "attribute": {"Kilometerstand": "78000", "Erstzulassung": "2018"},
      "verkaeufer": {
        "id": "52527555", "typ": "PRIVATE", "name": "M. Hadler",
        "konto_seit": "2014-03-02", "konto_alter_tage": 4538,
        "bewertung": 0.94, "abzeichen": {"reliability": 2, "friendliness": 2},
        "anzahl_anzeigen": 3, "historie_monate": 7
      },
      "uebergabe": {"abholung": true, "versand": false, "kaeuferschutz": false},
      "score": 84,
      "signale": {
        "gruen": ["Abholung beworben", "Konto seit 2014, Historie gestreut",
                  "Mängel offengelegt", "Nachlass als Preisbegründung"],
        "rot": [],
        "unkenntnis_bonus": true,
        "tippfehler_im_titel": "Porshe"
      }
    }
  ]
}
```

## 5. watchlist.yaml

Ein Eintrag pro Jagdziel. Der Sammler entscheidet anhand von `verfahren`, ob gesweept
oder gesucht wird.

```yaml
- id: porsche-911-992
  aktiv: true
  verfahren: sweep
  kategorie: 216
  preis_min: 15000
  preis_max: 150000
  muster:
    - '\b911\b'
    - '\b99[12](\.\d)?\b'
    - '\bcarrera\b'
    - '\bgt3\b'
  tippfehler: [porshe, porche, posche, porsche911, "911er"]
  ausschluss: [cayenne, macan, panamera, taycan, boxster, cayman, "modellauto",
               "1:18", "1:43", teppich, felgen, schlüsselanhänger]
  referenz_query: "Porsche 911 {typcode} {variante}"
  schwelle: 0.70

- id: dometic-tempomat
  aktiv: true
  verfahren: keyword
  begriffe: ["Dometic MagicSpeed", "MS-50 Tempomat", "AP60B", "MagicSpeed MS50"]
  tippfehler: ["Magic Speed MS 50", "Dometic Tempomat", "Waeco MS-50", "MS50 Tempomat"]
  ausschluss: [gesucht, defekt]
  preis_max: 900
  referenz_query: "Dometic MagicSpeed MS-50"
  schwelle: 0.65
```

### Start-Watchlist

Aus der Recherche, mit belegten Preisbändern. Alle Zahlen sind Gebrauchtpreise auf
Kleinanzeigen im August 2026, nicht Neupreise.

**Fahrzeuge** (Sweep über Kategorie 216, Motorräder 305, Wohnmobile 220): Porsche 911 in
den Baureihen 991 und 992, Tesla Model 3 und Model Y, Mercedes W124, Simson. Empirisch
belegte Suchmuster: `Tesla 3 LR AWD` (das Wort "Model" fällt weg), echter Tippfehler
`Tesla Model Y Performenc`, `Endoskopie gemacht` als Qualitätssignal bei 996 und 997.
Bei Klassikern schlägt die Papierlage die Technik: In 4 von 26 Simson-Titeln stand
`mit KBA Papieren` oder `inkl. Gutachten` im Titel, wofür der Verkäufer bei 1.700 bis
3.000 Euro Marktwert wertvolle Titelzeichen opfert. `Sammlungsauflösung` ist ein
Schnäppchensignal, `Tuning`, `Cross` und `130ccm` bei Klassikern das Gegenteil.

**Consumer-Elektronik** (Sweep über 173 Handy, 278 Notebooks, 245 Foto, 172 Audio,
279 Konsolen): AirPods Max Generation 1 (225 bis 350 Euro, Schwelle rund 200), Apple
Watch Ultra 1 (250 bis 339), iPad Pro M4 11 Zoll 256 GB (699 bis 850, Schwelle 650),
13 Zoll (800 bis 970, Schwelle 780). Achtung bei "Mac Pro": Die Suche liefert praktisch
ausschließlich MacBook Pro, der Begriff braucht zwingend einen Negativausschluss auf
"MacBook".

**IT und Homelab**: RTX 3090 (850 bis 1.500, Schwerpunkt 999 bis 1.250, Schwelle 850,
Nachfragetreiber ist lokale KI-Inferenz, nicht Gaming). Nvidia Tesla P40 24 GB (290 bis
379), V100 32 GB (850). Kepler-Karten wie K80 sind wegen fehlendem CUDA-Support wertlos.
Ubiquiti UDM-Pro (330) und UDM-SE (379), alles vor der UDM-Generation ist kein Ziel.
Synology nur die Plus-Serie, und dort **primär nach verbauten Platten und RAM bewerten**,
nicht nach Gehäusemodell: Ein DS220+ inklusive zweier 6-TB-Platten für 250 Euro lag
unter dem reinen Plattenwert. Threadripper Pro aus OEM-Systemen von Lenovo oder Dell
sind per Vendor-Lock an das Herstellerboard gebunden, deshalb ist `kein Lock` im Titel
ein Pflicht-Prüfpunkt.

**Retro und Nische**: Sony PVM-Studiomonitore. Unrestauriert 200 bis 350 Euro,
restauriert bis 1.400 Euro, der größte erkennbare Wertabstand im gesamten Datensatz.
Signale: Zollangabe (20 Zoll deutlich über 14 Zoll), `800 Lines` oder `600 TV-Lines`
im Titel, Mehrfachposten aus Studioauflösungen. Dometic MagicSpeed AP60B und MS-50.

**HiFi und Studio**, die Kategorie mit den größten relativen Fehlbepreisungen, weil
Erben und Auflöser die Modellhierarchien nicht kennen: Revox PR99 (1.500 bis 4.590 Euro,
optisch fast identisch zur B77 bei 576), Studer A807 (Median 3.050), Neumann KM84 (2.650
bis 2.980 pro Stück), Neumann U87 (2.000 bis 4.331), AKG C414 (Median 700), Technics
SL-1200 MK2 (Median 750, Schwelle 400), Thorens TD 124 (Median 490), Linn Sondek LP12
(komplett 1.800 bis 4.250), Klipschorn (Median 5.634, Schwelle 3.000), Nakamichi Dragon
(Median 2.294), Quad ESL 57 (Median 1.020). Zwei Besonderheiten: Bei Plattenspielern
steckt der Wert oft im Tonabnehmer, nicht im Laufwerk. Und Braun-Geräte von Dieter Rams
kosten im HiFi-Kanal ein Viertel dessen, was der Design- und Interior-Kanal zahlt, also
generische Suchbegriffe wie "weiße Musiktruhe" statt Modellnamen.

**Kameras**: Leica über usedlenstracker mit fertigen Schwellen (Summicron-M 50 unter
1.140 Dollar ist ein Deal, Leica Q2 verkauft sich in 6 Tagen). Besonders ergiebig ist
der Suchbegriff `Leitz`, historisch korrekt und umgangssprachlich für "altes Leica-Zeug".
Zeiss ZM als strukturell unterbewertete Alternative zu Leica M. Konvolute aus Nachlässen
sind der größte Hebel, weil Erben Einzelwerte nicht kennen.

**Notverkäufe kategorieübergreifend** (Keyword, ohne festes Produkt): Notverkauf,
Haushaltsauflösung, Nachlass, Sammlungsauflösung, wegen Umzug, Wohnungsauflösung,
höre mit dem Hobby auf. Hier bewertet Stufe 2, ob der Gegenstand überhaupt wertvoll ist.

Die Liste ist Startpunkt, nicht Endzustand. Sie wird nach den ersten Läufen anhand der
Trefferqualität nachgezogen.

## 6. Stufe 2: der Gutachter

Die Routine läuft im geklonten Repo und folgt `prompt.md` als einziger Wahrheit, genau
wie DACH Exit Scanner und Berlin Funding Scanner.

Ablauf:

1. `candidates.json` und `deal_log.csv` lesen. Alles, was schon gemeldet wurde, fällt raus.
2. Pro Kandidat prüfen:
   - **Ist die Referenzgruppe wirklich vergleichbar?** Ein 256-GB-Gerät gegen
     512-GB-Anzeigen zu vergleichen erzeugt Phantomersparnisse. Speichergröße, Baujahr,
     Zustand und Zubehörumfang gegenprüfen.
   - **Betrugsplausibilität im Fließtext.** Die Regex aus Stufe 1 sind grob. Claude liest
     den Text und erkennt, was kein Muster fängt.
   - **Produktexistenz.** Gibt es das genannte Modell überhaupt?
   - **Externe Marktwertprüfung** bei Fahrzeugen und hochpreisigen Nischenteilen per
     Websuche. mobile.de und AutoScout24 antworten auf direkten Abruf mit 403, deshalb
     Websuche statt Fetch.
   - Bei `referenz: fehlt` den Marktwert selbst recherchieren.
3. Verdikt je Kandidat: melden oder verwerfen, mit einem Satz Begründung.
4. Für gemeldete Deals je einen Satz Handlungsempfehlung: was fragen, worauf achten,
   welches Risiko bleibt.
5. Neue Deals an `deal_log.csv` anhängen, `runs/JJJJ-MM-TT/run_results.md` schreiben.
6. **Kein gemeldeter Deal: kein Commit, kein Push, keine Mail.** Lauf beendet.
7. Sonst `email_output.html` erzeugen, alles committen und pushen.

## 7. Stufe 3: die Mail

Kartenlayout, ein Fund pro Karte, sortiert nach absoluter Ersparnis. Alles Inline-CSS,
damit es in Mail-Clients hält.

Kopf: "Kleinanzeigen Schnäppchen, 5. August 2026" in dunklem Navy, darunter eine rote
Linie und die explizite Zeitraumangabe "Zeitraum: 4. August 2026, 07:00 Uhr bis
5. August 2026, 06:15 Uhr", damit erkennbar ist, welche Periode abgedeckt ist. Danach
"3 neue Funde".

Pro Karte: Vorschaubild links, rechts Titel als Link auf die Anzeige, Preis groß,
darunter Median-Marktwert und Ersparnis in Euro und Prozent. Zeile mit Ort, Übergabeart
und Einstellzeitpunkt. Zeile zum Verkäufer: Konto seit Jahr, Bewertung, Abzeichen,
Anzahl Anzeigen. Darunter ein Satz warum das ein Deal ist, ein Satz Risikohinweis, und
die Handlungsempfehlung.

Ist der Unkenntnis-Bonus gesetzt, bekommt die Karte eine sichtbare Markierung, denn das
ist die wertvollste Fundklasse.

## 8. Repo-Struktur

```
prompt.md                          Anweisung für die Routine, source of truth
watchlist.yaml                     Jagdziele
requirements.txt
scanner/
  __init__.py
  fetch.py                         Zeitfenster-Sweeps und Keyword-Suchen
  filter.py                        Gesuche, Fälschungen, Modell-Matching
  reference.py                     Referenzpreis-Median
  score.py                         Seriositäts-Scoring
  main.py                          Ablaufsteuerung, schreibt candidates.json
tests/                             Tests gegen aufgezeichnete API-Antworten
candidates.json                    Ergebnis von Stufe 1
seen_ads.csv                       ad_id, erste_sichtung
deal_log.csv                       datum,ad_id,titel,preis,median,ersparnis,url,watchlist_id
email_output.html                  von Stufe 2 erzeugt
runs/JJJJ-MM-TT/scan.md            Laufprotokoll Stufe 1
runs/JJJJ-MM-TT/run_results.md     Laufprotokoll Stufe 2
docs/superpowers/specs/            dieses Dokument
.github/workflows/scan.yml         Cron
.github/workflows/send-email.yml   Resend auf Push
.github/workflows/connectivity-check.yml   manueller Erreichbarkeitstest
```

Tests laufen gegen aufgezeichnete API-Antworten, nicht gegen die Live-API. Damit sind
Filter- und Scoring-Logik prüfbar, ohne bei jedem Testlauf Kleinanzeigen zu belasten.

### Secrets

`RESEND_API_KEY` als Repository-Secret. `KLEINANZEIGEN_BASIC_USER` und
`KLEINANZEIGEN_BASIC_PW` optional vorbereitet, damit bei rotierten Zugangsdaten nur ein
Secret getauscht werden muss statt Code geändert.

## 9. Zeitplan

| Zeit (Berlin) | Was |
|---|---|
| 06:15 | `scan.yml`, Cron `15 4 * * *` in UTC |
| 07:00 | Routine, Stufe 2 |
| direkt danach | `send-email.yml` auf Push |

Der Cron steht in UTC. Im Winter läuft der Scan dadurch um 05:15 statt 06:15, was
unkritisch ist, weil bis 07:00 genug Puffer bleibt.

## 10. Betrieb, Kosten, Überwachung

**Requests.** Grob 1.500 bis 2.500 pro Tag. Bei gedrosselter Rate rund 20 bis 30 Minuten
Laufzeit. Das passt in die 2.000 Freiminuten für private Repos, ist aber der Stellhebel,
an dem nach dem ersten echten Lauf nachjustiert wird. Enge Preisbänder in den großen
Kategorien sparen am meisten: Ein ungefilterter Autos-Sweep über 24 Stunden umfasst
84.873 Anzeigen, mit `min_price` deutlich weniger.

**Resend.** Eine Mail pro Tag, weit im Gratiskontingent.

**Überwachung.** Das ist kein Nice-to-have, denn es gibt zwei stille Ausfallpfade, die
für den Client identisch aussehen. Der Job schlägt fehl bei:

- HTTP 401 oder 403, was auf rotierte Zugangsdaten oder eine ASN-Sperre hindeutet
- leerer Ergebnismenge bei einer Query, die am Vortag Treffer hatte
- weniger als der Hälfte der Vortagsmenge an gesichteten Anzeigen

Der eingebaute Backoff des Pakets ist schwach, nach drei Versuchen und rund 4,5 Sekunden
fliegt eine Exception. Für einen echten Rate-Limit-Ban reicht das nicht, deshalb einen
eigenen Backoff mit deutlich längeren Wartezeiten davorsetzen.

**Fallback, falls die Erreichbarkeit kippt.** Scrappa, 10 Dollar für 33.000 Requests,
zwölf Monate gültig, dedizierte Kleinanzeigen-Endpunkte. Alternativ ein
Residential-Proxy ab 0,49 Dollar pro Gigabyte. Beides ändert nur `fetch.py`.

**Rechtlicher Rahmen.** Automatisierter Zugriff widerspricht den Kleinanzeigen-AGB.
Ohne Login, mit Rate-Limit, ohne Weitergabe der Daten und in dieser Größenordnung ist
das privater Kleinstverbrauch. Bewusste Entscheidung, hier festgehalten.

## 11. Risiken

| Risiko | Wirkung | Gegenmaßnahme |
|---|---|---|
| Zugangsdaten rotiert | 401 sofort, kein Retry | über Secrets austauschbar, Alarm auf 401 |
| ASN-Sperre für Azure | Scan fällt aus | Alarm, Umstieg auf Scrappa oder Proxy |
| Referenzgruppe unpassend | Phantomersparnis in der Mail | Mindestens 8 Vergleiche, Plausibilitätsprüfung durch Stufe 2 |
| Zu viele Fehlalarme | Mail wird ignoriert | Schwellen nach den ersten Läufen empirisch nachziehen |
| Zu wenige Treffer | Scanner wirkt tot | Laufprotokoll zeigt je Filterstufe, wo die Anzeigen hängenbleiben |
| Actions-Minuten überschritten | Scan stoppt Ende des Monats | Laufzeit im Protokoll mitschreiben, Preisbänder verengen |

Es existiert keine öffentliche Statistik zum Anteil betrügerischer Inserate auf
Kleinanzeigen. Weder Plattform noch BKA weisen das aus. Jede Kalibrierung der
Schwellwerte muss deshalb empirisch am eigenen Datenstrom erfolgen.

## 12. Bewusst nicht im Umfang

Kein Kleinanzeigen-Login, kein automatisches Anschreiben von Verkäufern, kein
automatisches Kaufen oder Bieten. Keine Bild-Rückwärtssuche in Version 1, obwohl sie
gegen kopierte Inserate hilft, denn sie kostet einen externen Dienst. Keine
Preishistorie über Zeit. Keine Weboberfläche. Keine anderen Plattformen.

## 13. Offene Punkte vor der Umsetzung

1. Empfängeradresse für die Mail und Absenderdomain für Resend.
2. Ist `RESEND_API_KEY` aus den bestehenden Scannern wiederverwendbar oder braucht es
   einen eigenen Schlüssel?
3. Die Tippfehlerlisten sind bislang konstruiert (QWERTZ-Nachbarschaft, deutsch-englische
   Orthografie-Interferenz, Buchstabendreher) und nur an Stichproben von rund 27 Titeln
   je Kategorie geprüft. Diese Stichprobe widerlegt Annahmen zuverlässig, belegt aber
   keine Häufigkeiten: Die vermutete Schreibweise "Modell 3" für Tesla kam in 27 echten
   Titeln kein einziges Mal vor, dafür fand sich der reale Tippfehler
   `Tesla Model Y Performenc`. Für die Produktivkalibrierung braucht es mehrere hundert
   Titel je Kategorie. Das ist ein Auswertungslauf gegen echte Daten, kein Blocker für
   die Umsetzung.
