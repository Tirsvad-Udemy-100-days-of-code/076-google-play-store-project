# MIL-002 Data Cleaning and Exploration

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version; Go in RC-005 (autonomous, not independent) | pending |

---

## Purpose

Decide whether the data layer is correct: the data set loads, is cleaned as the lecture describes, and the exploration questions are answered by tested functions.

## Deliverable

The package `src/play_store/` with functions for loading, cleaning, converting and exploring the Google Play Store data, and tests in `tests/` that run on a small synthetic fixture.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every function listed in the tasks exists and has a test | All tests pass | A function has no test or a test fails |
| 2 | Coverage of `src/` | At least 90% | Below 90% |
| 3 | The python review checklist `qc-programming-python` is reviewed with verdict Go | RC record says Go | No-Go or no record |
| 4 | opengrep finds no error-severity finding | Exit 0 | A finding |
| 5 | With the real CSV (when supplied) the clean data set has 8,199 rows, as the lecture states | Row count equals 8,199 | A different count; the difference is explained in the PR |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Needs the package layout, test setup and ignore rules |

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

2026-11-14 — inside the Business Case window and after [MIL-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create the synthetic test fixture | Build a small in-memory data frame with the same columns as the course CSV and with NaN ratings, duplicate apps (like Instagram), prices with a dollar sign, installs with commas and a "I am Rich" outlier, so tests never need the real data set. | No | |
| 2 | Load the data and inspect it | Implement `load_apps(path)` returning the raw data frame, with a clear error that tells the user where to place the CSV when the file is missing. Covers the "How many rows and columns, show a sample" step. | No | |
| 3 | Drop unused columns and NaN ratings | Implement `drop_unused_columns` (Last_Updated, Android_Ver) and `drop_missing_ratings`, producing `df_apps_clean`. Covers the "Removing NaN values" lecture step. | No | |
| 4 | Remove duplicates | Implement `find_duplicates` and `remove_duplicates` that identify duplicates on App, Type and Price and keep the entry with the most reviews, as the lecture does for Instagram. | No | |
| 5 | Convert Installs and Price to numbers | Implement `convert_installs` and `convert_price` that strip commas, plus signs and dollar signs and use `pd.to_numeric`. Covers "Numeric type conversions". | No | |
| 6 | Filter junk prices and add Revenue_Estimate | Implement `remove_expensive_apps` (price below 250) and `add_revenue_estimate` (price times installs), plus `top_grossing_paid_apps`. Covers the "I am Rich" step. | No | |
| 7 | Preliminary exploration functions | Implement `highest_rated`, `largest_apps` and `most_reviewed` using `sort_values`, answering the rating, size and review challenges. | No | |
| 8 | Review the code against qc-programming-python | Run the Python checklist over the package and tests and record the `RC-*` before the pull request. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-001]: ./mil-001-project-setup.md
