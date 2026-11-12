[English](Step-6-Categories) · **Dansk** · [Bahasa Malaysia](Step-6-Categories-ms)

# Trin 6: Kategorier: størrelse, popularitet og koncentration

**Spørgsmål:** Hvilke kategorier har flest apps, hvilke hentes mest, og hvor er konkurrencen hårdest?

![Trin 6: Kategorier: størrelse, popularitet og koncentration](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-8-top-categories-bar.png)

![Trin 6: Kategorier: størrelse, popularitet og koncentration](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-9-category-popularity-bar.png)

![Trin 6: Kategorier: størrelse, popularitet og koncentration](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-10-category-concentration-scatter.png)

## Hvad koden gør

Lektionen rapporterer **33** kategorier. `top_categories` tager `.value_counts()[:10]` af `Category`, og `top10_categories_bar` tegner det som et lodret søjlediagram. `category_installs` summerer `Installs` pr. kategori med `.groupby()`, og `category_popularity_bar` tegner et vandret søjlediagram (`orientation="h"`). `category_concentration` samler antallet af apps og installationerne med `pd.merge(..., left_index=True, right_index=True)`, og `category_concentration_scatter` tegner et spredningsdiagram med logaritmisk y-akse. Family og Game er de mest konkurrenceprægede kategorier (flest apps); Games og Tools er de mest populære (flest installationer).

**Bemærk:** De nøjagtige værdier kommer fra kursets CSV-fil, som du selv lægger i `data/apps.csv`; lektionen rapporterer de tal, der er nævnt her.

## Hvad du lærte

- `.value_counts()[:n]` giver de n største grupper.
- `.groupby(...)[...].sum()` aggregerer en kolonne pr. kategori.
- `pd.merge` på indekset kombinerer to aggregerede tabeller.
- `px.bar` (lodret og vandret) og `px.scatter` med `size=` og `color=` viser forskellige sider af de samme data.
- En logaritmisk akse (`yaxis={"type": "log"}`) gør værdier af meget forskellig størrelse læsbare.

Forrige: [Trin 5: Tal og omsætning: de mest indbringende betalte apps](Step-5-Numbers-and-Revenue-da) · Næste: [Trin 7: Genrer: opdeling af indlejrede værdier](Step-7-Genres-da)
