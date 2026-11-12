**English** · [Dansk](Step-8-Free-vs-Paid-da) · [Bahasa Malaysia](Step-8-Free-vs-Paid-ms)

# Step 8: Free versus paid apps

**Question:** Are there fewer paid apps, and how many downloads do paid apps give up?

![Step 8: Free versus paid apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-12-free-vs-paid-bar.png)

![Step 8: Free versus paid apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-13-installs-box.png)

## What the code does

`free_vs_paid_by_category` counts the apps per `Category` and `Type` with `.groupby(["Category", "Type"], as_index=False).agg({"App": "count"})`, and `free_vs_paid_bar` draws a grouped bar chart (`barmode="group"`) with a log y-axis. `installs_box` draws a notched box plot of `Installs` per `Type`. The lecture reports a median of **500,000** installs for free apps against about **5,000** for paid apps.

**Note:** Exact values come from the course CSV that you supply as `data/apps.csv`; the lecture reports the numbers quoted here.

## What you gained

- `.groupby([...], as_index=False).agg({...})` counts on two keys and keeps a flat table.
- `barmode="group"` puts bars side by side; `categoryorder` sorts the categories.
- A box plot (`px.box`, `notched=True`) shows the median and the spread, not just the average.
- Putting a price on an app costs many downloads.

Previous: [Step-7-Genres](Step-7-Genres) · Next: [Step-9-Revenue-and-Price](Step-9-Revenue-and-Price)
