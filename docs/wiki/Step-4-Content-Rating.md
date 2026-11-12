**English** · [Dansk](Step-4-Content-Rating-da) · [Bahasa Malaysia](Step-4-Content-Rating-ms)

# Step 4: Content rating: pie and donut charts

**Question:** How are the apps spread over the content ratings?

![Step 4: Content rating: pie and donut charts](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-6-content-rating-pie.png)

![Step 4: Content rating: pie and donut charts](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/raw/branch/main/docs/images/step-7-content-rating-donut.png)

## What the code does

`content_rating_counts` uses `.value_counts()` on `Content_Rating`. `content_rating_pie` draws the counts with `px.pie` (labels outside, `textinfo="percent+label"`). `content_rating_donut` is the same chart with `hole=DONUT_HOLE` (0.6) and the percentages inside the slices, which is the donut chart of the lecture.

**Note:** Exact values come from the course CSV that you supply as `data/apps.csv`; the lecture reports the numbers quoted here.

## What you gained

- `.value_counts()` turns a column into counts per category.
- `px.pie(values=..., names=...)` draws a pie chart; `hole=` turns it into a donut.
- `fig.update_traces(...)` controls the text position and what the labels show.

Previous: [Step-3-Ratings-Size-Reviews](Step-3-Ratings-Size-Reviews) · Next: [Step-5-Numbers-and-Revenue](Step-5-Numbers-and-Revenue)
