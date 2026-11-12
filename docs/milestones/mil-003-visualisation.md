# MIL-003 Visualisation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version; Go in RC-006 (autonomous, not independent) | pending |

---

## Purpose

Decide whether the six market questions of the assignment are answered by tested Plotly chart builders.

## Deliverable

Functions in `src/play_store/` that return Plotly figures for every chart in the lecture (pie, donut, vertical, horizontal and grouped bars, scatter, box plots), with tests that check the figure type, data and layout settings.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every chart function returns a `plotly.graph_objects.Figure` and has a test | All tests pass | Missing test or failure |
| 2 | Coverage of `src/` | At least 90% | Below 90% |
| 3 | Chart settings from the lecture are asserted (donut hole 0.6, log y-axis, group mode, category order, colour scale) | Assertions present and passing | A setting is not tested |
| 4 | `qc-programming-python` review has verdict Go | RC record says Go | No-Go or no record |
| 5 | opengrep finds no error-severity finding | Exit 0 | A finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The charts consume the cleaned data frame |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2 | [BC-001] Objectives |
| Success criteria 1 and 2 | [BC-001] Success Criteria |
| Concerns CN-001, CN-004 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in in autonomous mode) |

## Target Date

2026-11-15 — after [MIL-002] and inside the Business Case window.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Content rating pie and donut charts | Implement `content_rating_pie` and `content_rating_donut` from `value_counts` of Content_Rating (donut with `hole=0.6`), answering the content rating distribution step. | No | |
| 2 | Category bar charts | Implement `top10_categories_bar` (vertical) and `category_popularity_bar` (horizontal, sorted by installs), answering how competitive and how popular each category is. | No | |
| 3 | Category concentration scatter plot | Implement `category_concentration_scatter` by merging app counts and installs per category, using size, hover name, colour and a log y-axis. | No | |
| 4 | Genres bar chart with .stack() | Implement `count_genres` (split on semicolon and `.stack()`) and `top_genres_bar` with the Agsunset colour scale and no colour axis. | No | |
| 5 | Free versus paid grouped bar chart | Implement `free_vs_paid_by_category` data and `free_vs_paid_bar` (group mode, total descending, log axis). | No | |
| 6 | Installs box plot for free versus paid | Implement `installs_box` (notched, all points, log axis) to show the downloads given up by charging. | No | |
| 7 | Revenue and price box plots per category | Implement `paid_revenue_box` (min ascending), `paid_price_box` (max descending) and `median_paid_price`, answering what to charge and whether paid apps recoup development cost. | No | |
| 8 | Review the code against qc-programming-python | Run the Python checklist over the new code and tests and record the `RC-*` before the pull request. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-002]: ./mil-002-data-cleaning-exploration.md
