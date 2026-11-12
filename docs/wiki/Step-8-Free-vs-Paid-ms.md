[English](Step-8-Free-vs-Paid) · [Dansk](Step-8-Free-vs-Paid-da) · **Bahasa Malaysia**

# Langkah 8: Apl percuma berbanding apl berbayar

**Soalan:** Adakah apl berbayar lebih sedikit, dan berapa banyak muat turun yang hilang bagi apl berbayar?

![Langkah 8: Apl percuma berbanding apl berbayar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-12-free-vs-paid-bar.png)

![Langkah 8: Apl percuma berbanding apl berbayar](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-13-installs-box.png)

## Apa yang kod lakukan

`free_vs_paid_by_category` mengira apl bagi setiap `Category` dan `Type` dengan `.groupby(["Category", "Type"], as_index=False).agg({"App": "count"})`, dan `free_vs_paid_bar` melukis carta bar berkumpulan (`barmode="group"`) dengan paksi-y logaritma. `installs_box` melukis plot kotak bertakuk bagi `Installs` setiap `Type`. Kuliah melaporkan median **500,000** pemasangan bagi apl percuma berbanding kira-kira **5,000** bagi apl berbayar.

**Nota:** Nilai tepat datang daripada CSV kursus yang anda sediakan sebagai `data/apps.csv`; kuliah melaporkan nombor yang disebut di sini.

## Apa yang anda perolehi

- `.groupby([...], as_index=False).agg({...})` mengira pada dua kunci dan mengekalkan jadual rata.
- `barmode="group"` meletakkan bar bersebelahan; `categoryorder` menyusun kategori.
- Plot kotak (`px.box`, `notched=True`) menunjukkan median dan serakan, bukan sekadar purata.
- Meletakkan harga pada apl menyebabkan banyak muat turun hilang.

Sebelumnya: [Step-7-Genres](Step-7-Genres-ms) · Seterusnya: [Step-9-Revenue-and-Price](Step-9-Revenue-and-Price-ms)
