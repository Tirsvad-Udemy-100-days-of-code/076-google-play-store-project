[English](Step-7-Genres) · **Dansk** · [Bahasa Malaysia](Step-7-Genres-ms)

# Trin 7: Genrer: opdeling af indlejrede værdier

**Spørgsmål:** Hvilke genrer har flest apps?

![Trin 7: Genrer: opdeling af indlejrede værdier](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-11-top-genres-bar.png)

## Hvad koden gør

Lektionen rapporterer **53** genrer, men et almindeligt `.value_counts()` finder **114** værdier, fordi nogle apps har flere genrer sat sammen med semikolon (for eksempel `Action;Action & Adventure`). `count_genres` løser det med `df["Genres"].str.split(";", expand=True).stack()` og derefter `.value_counts()`: en app med flere genrer tæller med én gang i hver. `top_genres_bar` tegner de 15 største genrer med en farveskala.

**Bemærk:** De nøjagtige værdier kommer fra kursets CSV-fil, som du selv lægger i `data/apps.csv`; lektionen rapporterer de tal, der er nævnt her.

## Hvad du lærte

- `.str.split(";", expand=True)` deler én kolonne op i flere.
- `.stack()` samler de kolonner igen i én lang Series, der kan tælles.
- Tjek, hvad en kolonne virkelig indeholder, før du tæller: indlejrede værdier giver et forkert antal.
- `color=` og `color_continuous_scale=` farver søjlerne efter deres værdi.

Forrige: [Trin 6: Kategorier: størrelse, popularitet og koncentration](Step-6-Categories-da) · Næste: [Trin 8: Gratis mod betalte apps](Step-8-Free-vs-Paid-da)
