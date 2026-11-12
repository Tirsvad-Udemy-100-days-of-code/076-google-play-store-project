[English](Step-5-Numbers-and-Revenue) · **Dansk** · [Bahasa Malaysia](Step-5-Numbers-and-Revenue-ms)

# Trin 5: Tal og omsætning: de mest indbringende betalte apps

**Spørgsmål:** Hvilke betalte apps tjener mest?

![Trin 5: Tal og omsætning: de mest indbringende betalte apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-14-top-grossing.png)

## Hvad koden gør

`convert_installs` fjerner kommaer og `+` fra `Installs`, og `convert_price` fjerner `$` fra `Price`, begge med `.str.replace()` og `pd.to_numeric`. `remove_expensive_apps` beholder `Price < 250`, hvilket fjerner "I am Rich"-apps'ene, som koster 300 dollars eller mere. `add_revenue_estimate` tilføjer `Revenue_Estimate = Installs x Price`. `top_grossing_paid_apps` sorterer de betalte apps efter den kolonne og beholder 10. Lektionen rapporterer Minecraft øverst med omkring 70 millioner dollars, og 7 af de 10 øverste er spil.

**Bemærk:** De nøjagtige værdier kommer fra kursets CSV-fil, som du selv lægger i `data/apps.csv`; lektionen rapporterer de tal, der er nævnt her.

## Hvad du lærte

- `.str.replace()` og `pd.to_numeric` gør tekst som `10,000+` og `$2.99` til tal.
- Filtrering med en betingelse (`df[df["Price"] < 250]`) fjerner ekstreme værdier.
- En ny kolonne kan være en udregning på to andre: `Installs * Price`.
- Et omsætningsestimat er et groft overslag: installationer gange pris, ikke det faktiske salg.

Forrige: [Trin 4: Indholdsvurdering: cirkel- og donutdiagram](Step-4-Content-Rating-da) · Næste: [Trin 6: Kategorier: størrelse, popularitet og koncentration](Step-6-Categories-da)
