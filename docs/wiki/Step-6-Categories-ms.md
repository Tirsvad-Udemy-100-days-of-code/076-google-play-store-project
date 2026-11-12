[English](Step-6-Categories) · [Dansk](Step-6-Categories-da) · **Bahasa Malaysia**

# Langkah 6: Kategori: saiz, populariti dan penumpuan

**Soalan:** Kategori manakah yang mempunyai apl paling banyak, yang paling banyak dimuat turun, dan di manakah persaingan paling sengit?

![Langkah 6: Kategori: saiz, populariti dan penumpuan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-8-top-categories-bar.png)

![Langkah 6: Kategori: saiz, populariti dan penumpuan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-9-category-popularity-bar.png)

![Langkah 6: Kategori: saiz, populariti dan penumpuan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-10-category-concentration-scatter.png)

## Apa yang kod lakukan

Kuliah melaporkan **33** kategori. `top_categories` mengambil `.value_counts()[:10]` bagi `Category` dan `top10_categories_bar` melukisnya sebagai carta bar menegak. `category_installs` menjumlahkan `Installs` bagi setiap kategori dengan `.groupby()` dan `category_popularity_bar` melukis carta bar mendatar (`orientation="h"`). `category_concentration` menggabungkan bilangan apl dan pemasangan dengan `pd.merge(..., left_index=True, right_index=True)`, dan `category_concentration_scatter` melukis carta serakan dengan paksi-y logaritma. Family dan Game ialah kategori paling bersaing (apl paling banyak); Games dan Tools paling popular (pemasangan paling banyak).

**Nota:** Nilai tepat datang daripada CSV kursus yang anda sediakan sebagai `data/apps.csv`; kuliah melaporkan nombor yang disebut di sini.

## Apa yang anda perolehi

- `.value_counts()[:n]` memberikan n kumpulan terbesar.
- `.groupby(...)[...].sum()` mengagregat satu lajur bagi setiap kategori.
- `pd.merge` pada indeks menggabungkan dua jadual yang telah diagregat.
- `px.bar` (menegak dan mendatar) dan `px.scatter` dengan `size=` dan `color=` menunjukkan sisi berbeza data yang sama.
- Paksi logaritma (`yaxis={"type": "log"}`) menjadikan nilai yang sangat berbeza saiz mudah dibaca.

Sebelumnya: [Step-5-Numbers-and-Revenue](Step-5-Numbers-and-Revenue-ms) · Seterusnya: [Step-7-Genres](Step-7-Genres-ms)
