**English** · [Dansk](Summary-da) · [Bahasa Malaysia](Summary-ms)

# What the lecture taught

- Loading and exploring a CSV: `pd.read_csv`, `.shape`, `.head()`, `.sample()`, `.info()` and `.isna()`.
- Cleaning: `.drop(columns=...)`, `.dropna()`, `.duplicated()` and `.drop_duplicates()`, and `.str.replace()` with `pd.to_numeric` to turn text into numbers.
- Filtering outliers with a condition, such as `Price < 250`, and adding a calculated column (`Revenue_Estimate = Installs * Price`).
- Counting and ranking with `.value_counts()`, `.sort_values()` and `.head(n)`.
- Aggregating with `.groupby()`, `.agg()` and `pd.merge`, and splitting nested values with `.str.split(";", expand=True).stack()`.
- Plotly Express charts: `px.pie` (and the donut with `hole=`), `px.bar` (vertical, horizontal and grouped), `px.scatter` and `px.box`, with log axes for values of very different size.
- Reading medians and spreads to answer business questions about free and paid apps.

Answers (as the lecture reports them): 10,841 rows and 12 columns raw, 9,367 after dropping missing ratings and 8,199 after removing duplicates; 33 categories and 53 genres; Family and Game are the most competitive categories, Games and Tools the most popular; Minecraft tops the estimated revenue at about $70 million; free apps have a median of 500,000 installs against about 5,000 for paid apps; the median paid price is $2.99; the median paid photography app earned about $20,000, so an assumed $30,000 development cost is rarely recovered by sales alone. Exact values come from the course CSV that you supply as `data/apps.csv`.

Previous: [Step-9-Revenue-and-Price](Step-9-Revenue-and-Price)
