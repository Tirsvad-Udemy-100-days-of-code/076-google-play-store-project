[English](Summary) · [Dansk](Summary-da) · **Bahasa Malaysia**

# Apa yang diajar oleh kuliah

- Memuatkan dan meneroka CSV: `pd.read_csv`, `.shape`, `.head()`, `.sample()`, `.info()` dan `.isna()`.
- Pembersihan: `.drop(columns=...)`, `.dropna()`, `.duplicated()` dan `.drop_duplicates()`, serta `.str.replace()` dengan `pd.to_numeric` untuk menukar teks kepada nombor.
- Menapis nilai ekstrem dengan satu syarat, seperti `Price < 250`, dan menambah lajur terkira (`Revenue_Estimate = Installs * Price`).
- Mengira dan menyusun dengan `.value_counts()`, `.sort_values()` dan `.head(n)`.
- Mengagregat dengan `.groupby()`, `.agg()` dan `pd.merge`, serta memisahkan nilai bersarang dengan `.str.split(";", expand=True).stack()`.
- Carta Plotly Express: `px.pie` (dan donat dengan `hole=`), `px.bar` (menegak, mendatar dan berkumpulan), `px.scatter` dan `px.box`, dengan paksi logaritma untuk nilai yang sangat berbeza saiz.
- Membaca median dan serakan untuk menjawab soalan perniagaan tentang apl percuma dan berbayar.

Jawapan (seperti yang dilaporkan oleh kuliah): 10,841 baris dan 12 lajur mentah, 9,367 selepas membuang penilaian yang hilang dan 8,199 selepas membuang pendua; 33 kategori dan 53 genre; Family dan Game ialah kategori paling bersaing, Games dan Tools paling popular; Minecraft mendahului anggaran hasil pada kira-kira $70 juta; apl percuma mempunyai median 500,000 pemasangan berbanding kira-kira 5,000 bagi apl berbayar; harga berbayar median ialah $2.99; apl fotografi berbayar median memperoleh kira-kira $20,000, jadi kos pembangunan yang diandaikan $30,000 jarang diperoleh balik melalui jualan sahaja. Nilai tepat datang daripada CSV kursus yang anda sediakan sebagai `data/apps.csv`.

Sebelumnya: [Step-9-Revenue-and-Price](Step-9-Revenue-and-Price-ms)
