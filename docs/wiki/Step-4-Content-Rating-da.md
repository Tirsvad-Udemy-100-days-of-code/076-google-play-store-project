[English](Step-4-Content-Rating) · **Dansk** · [Bahasa Malaysia](Step-4-Content-Rating-ms)

# Trin 4: Indholdsvurdering: cirkel- og donutdiagram

**Spørgsmål:** Hvordan fordeler apps'ene sig over indholdsvurderingerne?

![Trin 4: Indholdsvurdering: cirkel- og donutdiagram](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-6-content-rating-pie.png)

![Trin 4: Indholdsvurdering: cirkel- og donutdiagram](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-7-content-rating-donut.png)

## Hvad koden gør

`content_rating_counts` bruger `.value_counts()` på `Content_Rating`. `content_rating_pie` tegner tallene med `px.pie` (tekst udenfor, `textinfo="percent+label"`). `content_rating_donut` er det samme diagram med `hole=DONUT_HOLE` (0,6) og procenterne inde i udsnittene, som er lektionens donutdiagram.

**Bemærk:** De nøjagtige værdier kommer fra kursets CSV-fil, som du selv lægger i `data/apps.csv`; lektionen rapporterer de tal, der er nævnt her.

## Hvad du lærte

- `.value_counts()` gør en kolonne om til antal pr. kategori.
- `px.pie(values=..., names=...)` tegner et cirkeldiagram; `hole=` gør det til et donutdiagram.
- `fig.update_traces(...)` styrer tekstens placering og hvad etiketterne viser.

Forrige: [Trin 3: Højest bedømte, største og mest anmeldte apps](Step-3-Ratings-Size-Reviews-da) · Næste: [Trin 5: Tal og omsætning: de mest indbringende betalte apps](Step-5-Numbers-and-Revenue-da)
