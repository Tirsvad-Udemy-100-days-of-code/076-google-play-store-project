**English** · [Dansk](Step-5-Numbers-and-Revenue-da) · [Bahasa Malaysia](Step-5-Numbers-and-Revenue-ms)

# Step 5: Numbers and revenue: the top grossing paid apps

**Question:** Which paid apps earn the most?

![Step 5: Numbers and revenue: the top grossing paid apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-14-top-grossing.png)

## What the code does

`convert_installs` removes the commas and the `+` from `Installs` and `convert_price` removes the `$` from `Price`, both with `.str.replace()` and `pd.to_numeric`. `remove_expensive_apps` keeps `Price < 250`, which removes the "I am Rich" apps that cost $300 or more. `add_revenue_estimate` adds `Revenue_Estimate = Installs x Price`. `top_grossing_paid_apps` sorts the paid apps by that column and keeps 10. The lecture reports Minecraft on top with about $70 million, and 7 of the top 10 are games.

**Note:** Exact values come from the course CSV that you supply as `data/apps.csv`; the lecture reports the numbers quoted here.

## What you gained

- `.str.replace()` and `pd.to_numeric` turn text such as `10,000+` and `$2.99` into numbers.
- Filtering with a condition (`df[df["Price"] < 250]`) removes outliers.
- A new column can be a calculation on two others: `Installs * Price`.
- A revenue estimate is a ballpark: installs times price, not real sales.

Previous: [Step-4-Content-Rating](Step-4-Content-Rating) · Next: [Step-6-Categories](Step-6-Categories)
