**English** · [Dansk](Step-2-Clean-da) · [Bahasa Malaysia](Step-2-Clean-ms)

# Step 2: Cleaning: unused columns, missing ratings and duplicates

**Question:** How do we remove columns we do not need, apps without a rating and duplicate rows?

![Step 2: Cleaning: unused columns, missing ratings and duplicates](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-2-clean.png)

## What the code does

`drop_unused_columns` drops `Last_Updated` and `Android_Ver` with `.drop(columns=...)`. `drop_missing_ratings` uses `.dropna()`: the lecture reports **9,367** rows left. `find_duplicates` uses `.duplicated(subset=["App", "Type", "Price"], keep=False)` to show every copy; Instagram appears 3 times with different review counts. `remove_duplicates` sorts by `Reviews` and keeps the row with the most reviews per App, Type and Price: **8,199** rows are left. `clean_apps` runs all the steps in lecture order.

**Note:** Exact values come from the course CSV that you supply as `data/apps.csv`; the lecture reports the numbers quoted here.

## What you gained

- `.drop(columns=...)` removes columns; `.dropna()` removes rows with missing values.
- `.duplicated(subset=..., keep=False)` finds duplicates on a combination of columns.
- Sort first and then `.drop_duplicates(keep="first")` to keep the most complete row (the one with the most reviews).
- Chain small, pure functions into one pipeline (`clean_apps`) that is easy to test.

Previous: [Step-1-Explore](Step-1-Explore) · Next: [Step-3-Ratings-Size-Reviews](Step-3-Ratings-Size-Reviews)
