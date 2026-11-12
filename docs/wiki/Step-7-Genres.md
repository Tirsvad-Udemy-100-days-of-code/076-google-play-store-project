**English** · [Dansk](Step-7-Genres-da) · [Bahasa Malaysia](Step-7-Genres-ms)

# Step 7: Genres: splitting nested values

**Question:** Which genres have the most apps?

![Step 7: Genres: splitting nested values](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-11-top-genres-bar.png)

## What the code does

The lecture reports **53** genres, but a plain `.value_counts()` finds **114** values, because some apps have several genres joined with a semicolon (for example `Action;Action & Adventure`). `count_genres` fixes this with `df["Genres"].str.split(";", expand=True).stack()` and then `.value_counts()`: an app with several genres counts once in each. `top_genres_bar` draws the 15 biggest genres with a colour scale.

**Note:** Exact values come from the course CSV that you supply as `data/apps.csv`; the lecture reports the numbers quoted here.

## What you gained

- `.str.split(";", expand=True)` splits one column into several.
- `.stack()` puts those columns back into one long Series that can be counted.
- Check what a column really contains before you count it: nested values give the wrong total.
- `color=` and `color_continuous_scale=` colour the bars by their value.

Previous: [Step-6-Categories](Step-6-Categories) · Next: [Step-8-Free-vs-Paid](Step-8-Free-vs-Paid)
