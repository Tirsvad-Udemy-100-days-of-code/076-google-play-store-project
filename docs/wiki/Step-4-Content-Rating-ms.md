[English](Step-4-Content-Rating) · [Dansk](Step-4-Content-Rating-da) · **Bahasa Malaysia**

# Langkah 4: Penarafan kandungan: carta pai dan donat

**Soalan:** Bagaimanakah apl diagihkan mengikut penarafan kandungan?

![Langkah 4: Penarafan kandungan: carta pai dan donat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-6-content-rating-pie.png)

![Langkah 4: Penarafan kandungan: carta pai dan donat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-7-content-rating-donut.png)

## Apa yang kod lakukan

`content_rating_counts` menggunakan `.value_counts()` pada `Content_Rating`. `content_rating_pie` melukis kiraan dengan `px.pie` (label di luar, `textinfo="percent+label"`). `content_rating_donut` ialah carta yang sama dengan `hole=DONUT_HOLE` (0.6) dan peratusan di dalam kepingan, iaitu carta donat dalam kuliah.

**Nota:** Nilai tepat datang daripada CSV kursus yang anda sediakan sebagai `data/apps.csv`; kuliah melaporkan nombor yang disebut di sini.

## Apa yang anda perolehi

- `.value_counts()` menukar satu lajur kepada kiraan bagi setiap kategori.
- `px.pie(values=..., names=...)` melukis carta pai; `hole=` menjadikannya carta donat.
- `fig.update_traces(...)` mengawal kedudukan teks dan apa yang ditunjukkan oleh label.

Sebelumnya: [Step-3-Ratings-Size-Reviews](Step-3-Ratings-Size-Reviews-ms) · Seterusnya: [Step-5-Numbers-and-Revenue](Step-5-Numbers-and-Revenue-ms)
