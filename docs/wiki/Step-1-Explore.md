**English** · [Dansk](Step-1-Explore-da) · [Bahasa Malaysia](Step-1-Explore-ms)

# Step 1: Exploring the raw data

**Question:** What does the scraped Google Play Store file look like, and how big is it?

![Step 1: Exploring the raw data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-1-explore.png)

## What the code does

`load_apps` (in `play_store.infrastructure.data`) reads `data/apps.csv` with `pd.read_csv`. The first look uses `.shape`, `.head()`, `.sample()` and `.info()`. The lecture reports **10,841** rows and **12** columns in the raw file, with missing values in some columns and one column (`Rating`) that is not filled for every app.

**Note:** Exact values come from the course CSV that you supply as `data/apps.csv`; the lecture reports the numbers quoted here.

## What you gained

- Loading a CSV into a DataFrame with `pd.read_csv`.
- `.shape` gives rows and columns; `.head()` and `.sample()` show a few rows.
- `.info()` and `.isna()` show data types and where values are missing, before any cleaning starts.

Previous: [Getting-Started](Getting-Started) · Next: [Step-2-Clean](Step-2-Clean)
