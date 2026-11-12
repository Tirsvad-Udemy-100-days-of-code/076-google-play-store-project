[English](Step-1-Explore) · **Dansk** · [Bahasa Malaysia](Step-1-Explore-ms)

# Trin 1: Udforskning af de rå data

**Spørgsmål:** Hvordan ser den skrabede Google Play Store-fil ud, og hvor stor er den?

![Trin 1: Udforskning af de rå data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-1-explore.png)

## Hvad koden gør

`load_apps` (i `play_store.infrastructure.data`) læser `data/apps.csv` med `pd.read_csv`. Det første blik bruger `.shape`, `.head()`, `.sample()` og `.info()`. Lektionen rapporterer **10.841** rækker og **12** kolonner i den rå fil, med manglende værdier i nogle kolonner og én kolonne (`Rating`), der ikke er udfyldt for alle apps.

**Bemærk:** De nøjagtige værdier kommer fra kursets CSV-fil, som du selv lægger i `data/apps.csv`; lektionen rapporterer de tal, der er nævnt her.

## Hvad du lærte

- At indlæse en CSV-fil i en DataFrame med `pd.read_csv`.
- `.shape` giver rækker og kolonner; `.head()` og `.sample()` viser nogle få rækker.
- `.info()` og `.isna()` viser datatyper og hvor der mangler værdier, før oprydningen begynder.

Forrige: [Kom godt i gang](Getting-Started-da) · Næste: [Trin 2: Oprydning: ubrugte kolonner, manglende ratings og dubletter](Step-2-Clean-da)
