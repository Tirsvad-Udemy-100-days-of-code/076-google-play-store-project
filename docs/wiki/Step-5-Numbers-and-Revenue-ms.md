[English](Step-5-Numbers-and-Revenue) · [Dansk](Step-5-Numbers-and-Revenue-da) · **Bahasa Malaysia**

# Langkah 5: Nombor dan hasil: apl berbayar paling menguntungkan

**Soalan:** Apl berbayar manakah yang memperoleh paling banyak?

![Langkah 5: Nombor dan hasil: apl berbayar paling menguntungkan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-14-top-grossing.png)

## Apa yang kod lakukan

`convert_installs` membuang koma dan `+` daripada `Installs` dan `convert_price` membuang `$` daripada `Price`, kedua-duanya dengan `.str.replace()` dan `pd.to_numeric`. `remove_expensive_apps` mengekalkan `Price < 250`, yang membuang apl "I am Rich" berharga $300 atau lebih. `add_revenue_estimate` menambah `Revenue_Estimate = Installs x Price`. `top_grossing_paid_apps` menyusun apl berbayar mengikut lajur itu dan mengekalkan 10. Kuliah melaporkan Minecraft di tempat teratas dengan kira-kira $70 juta, dan 7 daripada 10 teratas ialah permainan.

**Nota:** Nilai tepat datang daripada CSV kursus yang anda sediakan sebagai `data/apps.csv`; kuliah melaporkan nombor yang disebut di sini.

## Apa yang anda perolehi

- `.str.replace()` dan `pd.to_numeric` menukar teks seperti `10,000+` dan `$2.99` kepada nombor.
- Menapis dengan satu syarat (`df[df["Price"] < 250]`) membuang nilai ekstrem.
- Lajur baharu boleh menjadi pengiraan daripada dua lajur lain: `Installs * Price`.
- Anggaran hasil ialah angka kasar: pemasangan darab harga, bukan jualan sebenar.

Sebelumnya: [Step-4-Content-Rating](Step-4-Content-Rating-ms) · Seterusnya: [Step-6-Categories](Step-6-Categories-ms)
