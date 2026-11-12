[English](Step-3-Ratings-Size-Reviews) · **Dansk** · [Bahasa Malaysia](Step-3-Ratings-Size-Reviews-ms)

# Trin 3: Højest bedømte, største og mest anmeldte apps

**Spørgsmål:** Hvilke apps har den højeste rating, hvilke er de største, og hvilke har flest anmeldelser?

![Trin 3: Højest bedømte, største og mest anmeldte apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-3-highest-rated.png)

![Trin 3: Højest bedømte, største og mest anmeldte apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-4-largest-apps.png)

![Trin 3: Højest bedømte, største og mest anmeldte apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-5-most-reviewed.png)

## Hvad koden gør

`highest_rated`, `largest_apps` og `most_reviewed` bruger alle `.sort_values(..., ascending=False).head(n)` på `Rating`, `Size_MBs` og `Reviews` (5, 5 og 50 apps). Lektionen finder, at apps med perfekte 5 stjerner har få anmeldelser, så en rating alene siger lidt. Play Store begrænser app-størrelsen til 100 MB, hvilket forklarer, hvorfor de største apps stopper dér. Blandt de 50 mest anmeldte apps er der ingen betalt app.

**Bemærk:** De nøjagtige værdier kommer fra kursets CSV-fil, som du selv lægger i `data/apps.csv`; lektionen rapporterer de tal, der er nævnt her.

## Hvad du lærte

- `.sort_values()` sammen med `.head(n)` er vejen til en top-n-liste.
- En høj rating med få anmeldelser er ikke pålidelig: se også på antallet af anmeldelser.
- Platformens regler (grænsen på 100 MB) viser sig som et loft i data.
- De mest populære apps er gratis.

Forrige: [Trin 2: Oprydning: ubrugte kolonner, manglende ratings og dubletter](Step-2-Clean-da) · Næste: [Trin 4: Indholdsvurdering: cirkel- og donutdiagram](Step-4-Content-Rating-da)
