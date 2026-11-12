[English](Step-1-Explore) · [Dansk](Step-1-Explore-da) · **Bahasa Malaysia**

# Langkah 1: Meneroka data mentah

**Soalan:** Bagaimanakah rupa fail Google Play Store yang dikikis, dan sebesar mana ia?

![Langkah 1: Meneroka data mentah](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-1-explore.png)

## Apa yang kod lakukan

`load_apps` (dalam `play_store.infrastructure.data`) membaca `data/apps.csv` dengan `pd.read_csv`. Pandangan pertama menggunakan `.shape`, `.head()`, `.sample()` dan `.info()`. Kuliah melaporkan **10,841** baris dan **12** lajur dalam fail mentah, dengan nilai yang hilang dalam beberapa lajur dan satu lajur (`Rating`) yang tidak diisi untuk setiap apl.

**Nota:** Nilai tepat datang daripada CSV kursus yang anda sediakan sebagai `data/apps.csv`; kuliah melaporkan nombor yang disebut di sini.

## Apa yang anda perolehi

- Memuatkan CSV ke dalam DataFrame dengan `pd.read_csv`.
- `.shape` memberi bilangan baris dan lajur; `.head()` dan `.sample()` menunjukkan beberapa baris.
- `.info()` dan `.isna()` menunjukkan jenis data dan di mana nilai hilang, sebelum pembersihan bermula.

Sebelumnya: [Getting-Started](Getting-Started-ms) · Seterusnya: [Step-2-Clean](Step-2-Clean-ms)
