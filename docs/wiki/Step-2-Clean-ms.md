[English](Step-2-Clean) · [Dansk](Step-2-Clean-da) · **Bahasa Malaysia**

# Langkah 2: Pembersihan: lajur tidak digunakan, penilaian hilang dan pendua

**Soalan:** Bagaimanakah kita membuang lajur yang tidak diperlukan, apl tanpa penilaian dan baris pendua?

![Langkah 2: Pembersihan: lajur tidak digunakan, penilaian hilang dan pendua](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-2-clean.png)

## Apa yang kod lakukan

`drop_unused_columns` membuang `Last_Updated` dan `Android_Ver` dengan `.drop(columns=...)`. `drop_missing_ratings` menggunakan `.dropna()`: kuliah melaporkan **9,367** baris tinggal. `find_duplicates` menggunakan `.duplicated(subset=["App", "Type", "Price"], keep=False)` untuk menunjukkan setiap salinan; Instagram muncul 3 kali dengan bilangan ulasan yang berbeza. `remove_duplicates` menyusun mengikut `Reviews` dan mengekalkan baris dengan ulasan paling banyak bagi setiap App, Type dan Price: **8,199** baris tinggal. `clean_apps` menjalankan semua langkah mengikut susunan kuliah.

**Nota:** Nilai tepat datang daripada CSV kursus yang anda sediakan sebagai `data/apps.csv`; kuliah melaporkan nombor yang disebut di sini.

## Apa yang anda perolehi

- `.drop(columns=...)` membuang lajur; `.dropna()` membuang baris yang mempunyai nilai hilang.
- `.duplicated(subset=..., keep=False)` mencari pendua pada gabungan lajur.
- Susun dahulu, kemudian `.drop_duplicates(keep="first")` untuk mengekalkan baris yang paling lengkap (yang mempunyai ulasan paling banyak).
- Menyambung fungsi kecil yang tulen menjadi satu saluran paip (`clean_apps`) yang mudah diuji.

Sebelumnya: [Step-1-Explore](Step-1-Explore-ms) · Seterusnya: [Step-3-Ratings-Size-Reviews](Step-3-Ratings-Size-Reviews-ms)
