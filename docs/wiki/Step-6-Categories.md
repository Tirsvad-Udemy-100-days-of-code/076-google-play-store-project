**English** · [Dansk](Step-6-Categories-da) · [Bahasa Malaysia](Step-6-Categories-ms)

# Step 6: Categories: size, popularity and concentration

**Question:** Which categories have the most apps, which are the most downloaded, and where is the competition hardest?

![Step 6: Categories: size, popularity and concentration](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-8-top-categories-bar.png)

![Step 6: Categories: size, popularity and concentration](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-9-category-popularity-bar.png)

![Step 6: Categories: size, popularity and concentration](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-10-category-concentration-scatter.png)

## What the code does

The lecture reports **33** categories. `top_categories` takes `.value_counts()[:10]` of `Category` and `top10_categories_bar` draws it as a vertical bar chart. `category_installs` sums `Installs` per category with `.groupby()` and `category_popularity_bar` draws a horizontal bar chart (`orientation="h"`). `category_concentration` joins the number of apps and the installs with `pd.merge(..., left_index=True, right_index=True)`, and `category_concentration_scatter` draws a scatter plot with a log y-axis. Family and Game are the most competitive categories (most apps); Games and Tools are the most popular (most installs).

**Note:** Exact values come from the course CSV that you supply as `data/apps.csv`; the lecture reports the numbers quoted here.

## What you gained

- `.value_counts()[:n]` gives the n largest groups.
- `.groupby(...)[...].sum()` aggregates a column per category.
- `pd.merge` on the index combines two aggregated tables.
- `px.bar` (vertical and horizontal) and `px.scatter` with `size=` and `color=` show different sides of the same data.
- A log axis (`yaxis={"type": "log"}`) makes values of very different size readable.

Previous: [Step-5-Numbers-and-Revenue](Step-5-Numbers-and-Revenue) · Next: [Step-7-Genres](Step-7-Genres)
