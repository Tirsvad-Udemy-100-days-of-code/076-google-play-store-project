[English](Summary) · **Dansk** · [Bahasa Malaysia](Summary-ms)

# Hvad lektionen lærte

- At indlæse og udforske en CSV-fil: `pd.read_csv`, `.shape`, `.head()`, `.sample()`, `.info()` og `.isna()`.
- Oprydning: `.drop(columns=...)`, `.dropna()`, `.duplicated()` og `.drop_duplicates()`, og `.str.replace()` med `pd.to_numeric` til at gøre tekst til tal.
- At filtrere ekstreme værdier med en betingelse, for eksempel `Price < 250`, og tilføje en udregnet kolonne (`Revenue_Estimate = Installs * Price`).
- At tælle og rangere med `.value_counts()`, `.sort_values()` og `.head(n)`.
- At aggregere med `.groupby()`, `.agg()` og `pd.merge`, og dele indlejrede værdier op med `.str.split(";", expand=True).stack()`.
- Plotly Express-diagrammer: `px.pie` (og donut med `hole=`), `px.bar` (lodret, vandret og grupperet), `px.scatter` og `px.box`, med logaritmiske akser til værdier af meget forskellig størrelse.
- At aflæse medianer og spredning for at besvare forretningsspørgsmål om gratis og betalte apps.

Svar (som lektionen rapporterer dem): 10.841 rækker og 12 kolonner rå, 9.367 efter fjernelse af manglende ratings og 8.199 efter fjernelse af dubletter; 33 kategorier og 53 genrer; Family og Game er de mest konkurrenceprægede kategorier, Games og Tools de mest populære; Minecraft topper den estimerede omsætning med omkring 70 millioner dollars; gratis apps har en median på 500.000 installationer mod omkring 5.000 for betalte apps; medianprisen for en betalt app er 2,99 dollars; den mediane betalte fotoapp tjente omkring 20.000 dollars, så en antaget udviklingsomkostning på 30.000 dollars tjenes sjældent ind alene ved salg. De nøjagtige værdier kommer fra kursets CSV-fil, som du selv lægger i `data/apps.csv`.

Forrige: [Trin 9: Omsætning og pris for betalte apps](Step-9-Revenue-and-Price-da)
