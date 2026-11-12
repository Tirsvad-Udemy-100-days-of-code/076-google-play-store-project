[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom godt i gang

Krav: Python 3.13 eller nyere. Afhængigheder ved kørsel: `pandas` og `plotly`. Tilvalg: `dev` (pytest, pytest-cov, ruff), `notebook` (jupyterlab, nbconvert, nbclient, ipykernel) og `docs` (kaleido, til skærmbillederne).

Opret og brug et lokalt `.venv` (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev,notebook,docs]"
```

Linux og macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev,notebook,docs]"
```

Den skrabede Google Play Store-CSV ligger ikke i repositoriet. Gem filen fra kurset som `data/apps.csv` (opret mappen `data`, hvis den ikke findes).

```text
data/apps.csv
```

Kør testene, notebooken, skærmbillederne og sikkerhedsscanningen (`opengrep`):

```bash
python -m pytest
jupyter lab notebooks/google_play_store.ipynb
python scripts/make_screenshots.py
bash scripts/scan.sh
```

**Hvad du får ud af det:** en gentagelig opsætning (et virtuelt miljø pr. projekt), en pakke, du installerer i redigerbar tilstand, tests, der beviser hvert svar, og en scanning, der kontrollerer koden for sikkerhedsproblemer.

Næste: [Trin 1: Udforskning af de rå data](Step-1-Explore-da)
