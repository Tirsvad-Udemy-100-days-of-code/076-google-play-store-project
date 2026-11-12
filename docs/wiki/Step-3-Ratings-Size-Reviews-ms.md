[English](Step-3-Ratings-Size-Reviews) · [Dansk](Step-3-Ratings-Size-Reviews-da) · **Bahasa Malaysia**

# Langkah 3: Apl berating tertinggi, terbesar dan paling banyak diulas

**Soalan:** Apl manakah yang dinilai paling tinggi, yang terbesar, dan yang mempunyai ulasan paling banyak?

![Langkah 3: Apl berating tertinggi, terbesar dan paling banyak diulas](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-3-highest-rated.png)

![Langkah 3: Apl berating tertinggi, terbesar dan paling banyak diulas](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-4-largest-apps.png)

![Langkah 3: Apl berating tertinggi, terbesar dan paling banyak diulas](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-5-most-reviewed.png)

## Apa yang kod lakukan

`highest_rated`, `largest_apps` dan `most_reviewed` semuanya menggunakan `.sort_values(..., ascending=False).head(n)` pada `Rating`, `Size_MBs` dan `Reviews` (5, 5 dan 50 apl). Kuliah mendapati bahawa apl 5 bintang sempurna mempunyai sedikit ulasan, jadi penilaian sahaja tidak banyak bermakna. Play Store menghadkan saiz apl kepada 100 MB, yang menerangkan mengapa apl terbesar berhenti di situ. Antara 50 apl paling banyak diulas tiada apl berbayar.

**Nota:** Nilai tepat datang daripada CSV kursus yang anda sediakan sebagai `data/apps.csv`; kuliah melaporkan nombor yang disebut di sini.

## Apa yang anda perolehi

- `.sort_values()` bersama `.head(n)` ialah cara membina senarai n teratas.
- Penilaian tinggi dengan sedikit ulasan tidak boleh dipercayai: lihat juga bilangan ulasan.
- Peraturan platform (had 100 MB) kelihatan sebagai siling dalam data.
- Apl paling popular adalah percuma.

Sebelumnya: [Step-2-Clean](Step-2-Clean-ms) · Seterusnya: [Step-4-Content-Rating](Step-4-Content-Rating-ms)
