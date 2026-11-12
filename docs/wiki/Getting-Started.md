**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

Requirements: Python 3.13 or newer. Runtime dependencies: `pandas` and `plotly`. Extras: `dev` (pytest, pytest-cov, ruff), `notebook` (jupyterlab, nbconvert, nbclient, ipykernel) and `docs` (kaleido, for the screenshots).

Create and use a local `.venv` (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev,notebook,docs]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev,notebook,docs]"
```

The scraped Google Play Store CSV is not in the repository. Save the file from the course as `data/apps.csv` (create the `data` folder if it does not exist).

```text
data/apps.csv
```

Run the tests, the notebook, the screenshots and the security scan (`opengrep`):

```bash
python -m pytest
jupyter lab notebooks/google_play_store.ipynb
python scripts/make_screenshots.py
bash scripts/scan.sh
```

**What you gain:** a repeatable set-up (a virtual environment per project), a package you install in editable mode, tests that prove each answer, and a scan that checks the code for security problems.

Next: [Step-1-Explore](Step-1-Explore)
