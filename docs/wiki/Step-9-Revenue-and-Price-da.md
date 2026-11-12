[English](Step-9-Revenue-and-Price) · **Dansk** · [Bahasa Malaysia](Step-9-Revenue-and-Price-ms)

# Trin 9: Omsætning og pris for betalte apps

**Spørgsmål:** Hvor meget kan en betalt app tjene, og hvad bør den koste?

![Trin 9: Omsætning og pris for betalte apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-15-paid-revenue-box.png)

![Trin 9: Omsætning og pris for betalte apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-16-paid-price-box.png)

## Hvad koden gør

`paid_apps` beholder rækkerne, hvor `Type` er `Paid`. `paid_revenue_box` tegner et boksplot af `Revenue_Estimate` pr. kategori med logaritmisk y-akse, og `paid_price_box` tegner `Price` pr. kategori. `median_paid_price` returnerer medianprisen for de betalte apps: lektionen rapporterer **2,99 dollars**, hvor Medical ligger omkring 5,49 dollars og Personalisation omkring 1,49 dollars. Den mediane betalte fotoapp tjente omkring **20.000 dollars**, så en antaget udviklingsomkostning på 30.000 dollars tjenes sjældent ind alene ved salg.

**Bemærk:** De nøjagtige værdier kommer fra kursets CSV-fil, som du selv lægger i `data/apps.csv`; lektionen rapporterer de tal, der er nævnt her.

## Hvad du lærte

- `paid_apps` filtrerer først, så alle følgende diagrammer kun handler om betalte apps.
- Medianen er en bedre rettesnor end gennemsnittet, når priser og omsætning er meget skæve.
- Boksplot pr. kategori (`px.box`) sammenligner spredningen i mange grupper i ét diagram.
- Tallene kan besvare et forretningsspørgsmål: betaler en betalt app sin udvikling?

Forrige: [Trin 8: Gratis mod betalte apps](Step-8-Free-vs-Paid-da) · Næste: [Opsummering](Summary-da)
