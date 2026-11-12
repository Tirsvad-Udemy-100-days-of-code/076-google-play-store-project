[English](Step-9-Revenue-and-Price) · [Dansk](Step-9-Revenue-and-Price-da) · **Bahasa Malaysia**

# Langkah 9: Hasil dan harga apl berbayar

**Soalan:** Berapa banyak yang boleh diperoleh oleh apl berbayar, dan berapakah harga yang sesuai?

![Langkah 9: Hasil dan harga apl berbayar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-15-paid-revenue-box.png)

![Langkah 9: Hasil dan harga apl berbayar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-16-paid-price-box.png)

## Apa yang kod lakukan

`paid_apps` mengekalkan baris di mana `Type` ialah `Paid`. `paid_revenue_box` melukis plot kotak `Revenue_Estimate` bagi setiap kategori dengan paksi-y logaritma, dan `paid_price_box` melukis `Price` bagi setiap kategori. `median_paid_price` mengembalikan harga median apl berbayar: kuliah melaporkan **$2.99**, dengan Medical kira-kira $5.49 dan Personalisation kira-kira $1.49. Apl fotografi berbayar median memperoleh kira-kira **$20,000**, jadi kos pembangunan yang diandaikan $30,000 jarang diperoleh balik melalui jualan sahaja.

**Nota:** Nilai tepat datang daripada CSV kursus yang anda sediakan sebagai `data/apps.csv`; kuliah melaporkan nombor yang disebut di sini.

## Apa yang anda perolehi

- `paid_apps` menapis dahulu, jadi semua carta seterusnya hanya tentang apl berbayar.
- Median ialah panduan yang lebih baik daripada purata apabila harga dan hasil sangat tidak simetri.
- Plot kotak bagi setiap kategori (`px.box`) membandingkan serakan banyak kumpulan dalam satu carta.
- Nombor boleh menjawab soalan perniagaan: adakah apl berbayar menampung kos pembangunannya?

Sebelumnya: [Step-8-Free-vs-Paid](Step-8-Free-vs-Paid-ms) · Seterusnya: [Summary](Summary-ms)
