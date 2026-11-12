[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Bermula

Keperluan: Python 3.13 atau lebih baharu. Kebergantungan masa jalan: `pandas` dan `plotly`. Tambahan: `dev` (pytest, pytest-cov, ruff), `notebook` (jupyterlab, nbconvert, nbclient, ipykernel) dan `docs` (kaleido, untuk tangkapan skrin).

Cipta dan gunakan `.venv` tempatan (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev,notebook,docs]"
```

Linux dan macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev,notebook,docs]"
```

CSV Google Play Store yang dikikis tiada dalam repositori. Simpan fail daripada kursus sebagai `data/apps.csv` (cipta folder `data` jika belum ada).

```text
data/apps.csv
```

Jalankan ujian, buku nota, tangkapan skrin dan imbasan keselamatan (`opengrep`):

```bash
python -m pytest
jupyter lab notebooks/google_play_store.ipynb
python scripts/make_screenshots.py
bash scripts/scan.sh
```

**Apa yang anda perolehi:** persediaan yang boleh diulang (satu persekitaran maya bagi setiap projek), pakej yang dipasang dalam mod boleh sunting, ujian yang membuktikan setiap jawapan, dan imbasan yang memeriksa kod untuk masalah keselamatan.

Seterusnya: [Step-1-Explore](Step-1-Explore-ms)
