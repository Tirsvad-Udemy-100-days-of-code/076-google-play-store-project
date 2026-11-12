**English** · [Dansk](Step-9-Revenue-and-Price-da) · [Bahasa Malaysia](Step-9-Revenue-and-Price-ms)

# Step 9: Revenue and price of paid apps

**Question:** How much can a paid app earn, and what should it cost?

![Step 9: Revenue and price of paid apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-15-paid-revenue-box.png)

![Step 9: Revenue and price of paid apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-16-paid-price-box.png)

## What the code does

`paid_apps` keeps the rows where `Type` is `Paid`. `paid_revenue_box` draws a box plot of `Revenue_Estimate` per category with a log y-axis, and `paid_price_box` draws the `Price` per category. `median_paid_price` returns the median price of the paid apps: the lecture reports **$2.99**, with Medical at about $5.49 and Personalisation at about $1.49. The median paid photography app earned about **$20,000**, so an assumed $30,000 development cost is rarely recovered by sales alone.

**Note:** Exact values come from the course CSV that you supply as `data/apps.csv`; the lecture reports the numbers quoted here.

## What you gained

- `paid_apps` filters first, so every chart that follows is about paid apps only.
- The median is a better guide than the average when prices and revenues are very skewed.
- Box plots per category (`px.box`) compare the spread of many groups in one chart.
- The numbers can answer a business question: does a paid app pay for its development?

Previous: [Step-8-Free-vs-Paid](Step-8-Free-vs-Paid) · Next: [Summary](Summary)
