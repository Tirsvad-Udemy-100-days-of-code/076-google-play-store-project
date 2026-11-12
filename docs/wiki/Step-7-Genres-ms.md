[English](Step-7-Genres) · [Dansk](Step-7-Genres-da) · **Bahasa Malaysia**

# Langkah 7: Genre: memisahkan nilai bersarang

**Soalan:** Genre manakah yang mempunyai apl paling banyak?

![Langkah 7: Genre: memisahkan nilai bersarang](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-11-top-genres-bar.png)

## Apa yang kod lakukan

Kuliah melaporkan **53** genre, tetapi `.value_counts()` biasa menemui **114** nilai, kerana sesetengah apl mempunyai beberapa genre yang disambung dengan koma bertitik (contohnya `Action;Action & Adventure`). `count_genres` membetulkannya dengan `df["Genres"].str.split(";", expand=True).stack()` kemudian `.value_counts()`: apl dengan beberapa genre dikira sekali dalam setiap satu. `top_genres_bar` melukis 15 genre terbesar dengan skala warna.

**Nota:** Nilai tepat datang daripada CSV kursus yang anda sediakan sebagai `data/apps.csv`; kuliah melaporkan nombor yang disebut di sini.

## Apa yang anda perolehi

- `.str.split(";", expand=True)` memecahkan satu lajur kepada beberapa lajur.
- `.stack()` meletakkan lajur itu semula ke dalam satu Series panjang yang boleh dikira.
- Semak apa yang sebenarnya terkandung dalam lajur sebelum mengira: nilai bersarang memberi jumlah yang salah.
- `color=` dan `color_continuous_scale=` mewarnakan bar mengikut nilainya.

Sebelumnya: [Step-6-Categories](Step-6-Categories-ms) · Seterusnya: [Step-8-Free-vs-Paid](Step-8-Free-vs-Paid-ms)
