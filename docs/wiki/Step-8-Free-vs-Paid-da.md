[English](Step-8-Free-vs-Paid) · **Dansk** · [Bahasa Malaysia](Step-8-Free-vs-Paid-ms)

# Trin 8: Gratis mod betalte apps

**Spørgsmål:** Er der færre betalte apps, og hvor mange downloads mister betalte apps?

![Trin 8: Gratis mod betalte apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-12-free-vs-paid-bar.png)

![Trin 8: Gratis mod betalte apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-13-installs-box.png)

## Hvad koden gør

`free_vs_paid_by_category` tæller apps pr. `Category` og `Type` med `.groupby(["Category", "Type"], as_index=False).agg({"App": "count"})`, og `free_vs_paid_bar` tegner et grupperet søjlediagram (`barmode="group"`) med logaritmisk y-akse. `installs_box` tegner et boksplot med hak af `Installs` pr. `Type`. Lektionen rapporterer en median på **500.000** installationer for gratis apps mod omkring **5.000** for betalte apps.

**Bemærk:** De nøjagtige værdier kommer fra kursets CSV-fil, som du selv lægger i `data/apps.csv`; lektionen rapporterer de tal, der er nævnt her.

## Hvad du lærte

- `.groupby([...], as_index=False).agg({...})` tæller på to nøgler og bevarer en flad tabel.
- `barmode="group"` sætter søjler side om side; `categoryorder` sorterer kategorierne.
- Et boksplot (`px.box`, `notched=True`) viser medianen og spredningen, ikke kun gennemsnittet.
- At sætte en pris på en app koster mange downloads.

Forrige: [Trin 7: Genrer: opdeling af indlejrede værdier](Step-7-Genres-da) · Næste: [Trin 9: Omsætning og pris for betalte apps](Step-9-Revenue-and-Price-da)
