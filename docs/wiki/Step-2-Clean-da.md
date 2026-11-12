[English](Step-2-Clean) · **Dansk** · [Bahasa Malaysia](Step-2-Clean-ms)

# Trin 2: Oprydning: ubrugte kolonner, manglende ratings og dubletter

**Spørgsmål:** Hvordan fjerner vi kolonner, vi ikke skal bruge, apps uden rating og dublerede rækker?

![Trin 2: Oprydning: ubrugte kolonner, manglende ratings og dubletter](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-2-clean.png)

## Hvad koden gør

`drop_unused_columns` fjerner `Last_Updated` og `Android_Ver` med `.drop(columns=...)`. `drop_missing_ratings` bruger `.dropna()`: lektionen rapporterer **9.367** rækker tilbage. `find_duplicates` bruger `.duplicated(subset=["App", "Type", "Price"], keep=False)` til at vise alle kopier; Instagram optræder 3 gange med forskelligt antal anmeldelser. `remove_duplicates` sorterer efter `Reviews` og beholder rækken med flest anmeldelser pr. App, Type og Price: der er **8.199** rækker tilbage. `clean_apps` kører alle trin i lektionens rækkefølge.

**Bemærk:** De nøjagtige værdier kommer fra kursets CSV-fil, som du selv lægger i `data/apps.csv`; lektionen rapporterer de tal, der er nævnt her.

## Hvad du lærte

- `.drop(columns=...)` fjerner kolonner; `.dropna()` fjerner rækker med manglende værdier.
- `.duplicated(subset=..., keep=False)` finder dubletter på en kombination af kolonner.
- Sortér først og brug derefter `.drop_duplicates(keep="first")` for at beholde den mest komplette række (den med flest anmeldelser).
- At sætte små, rene funktioner sammen til én pipeline (`clean_apps`), som er nem at teste.

Forrige: [Trin 1: Udforskning af de rå data](Step-1-Explore-da) · Næste: [Trin 3: Højest bedømte, største og mest anmeldte apps](Step-3-Ratings-Size-Reviews-da)
