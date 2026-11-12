**English** · [Dansk](Step-3-Ratings-Size-Reviews-da) · [Bahasa Malaysia](Step-3-Ratings-Size-Reviews-ms)

# Step 3: Highest rated, largest and most reviewed apps

**Question:** Which apps are rated highest, which are the largest, and which have the most reviews?

![Step 3: Highest rated, largest and most reviewed apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-3-highest-rated.png)

![Step 3: Highest rated, largest and most reviewed apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-4-largest-apps.png)

![Step 3: Highest rated, largest and most reviewed apps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-5-most-reviewed.png)

## What the code does

`highest_rated`, `largest_apps` and `most_reviewed` all use `.sort_values(..., ascending=False).head(n)` on `Rating`, `Size_MBs` and `Reviews` (5, 5 and 50 apps). The lecture finds that the perfect 5-star apps have few reviews, so a rating alone says little. The Play Store limits app size to 100 MB, which explains why the largest apps stop there. Among the 50 most reviewed apps there is no paid app.

**Note:** Exact values come from the course CSV that you supply as `data/apps.csv`; the lecture reports the numbers quoted here.

## What you gained

- `.sort_values()` plus `.head(n)` is the way to build a top-n list.
- A high rating with few reviews is not reliable: look at the number of reviews too.
- Platform rules (the 100 MB size limit) show up as a ceiling in the data.
- The most popular apps are free.

Previous: [Step-2-Clean](Step-2-Clean) · Next: [Step-4-Content-Rating](Step-4-Content-Rating)
