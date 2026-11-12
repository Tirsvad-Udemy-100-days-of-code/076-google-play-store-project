# MIL-004 Notebook, Screenshots and README

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version; Go in RC-007 (autonomous, not independent) | [785d729] |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Tasks 2 and 3 name the real paths (notebooks/, presentation/export.py, scripts/make_screenshots.py); delta Go in RC-013 (autonomous, not independent) | pending |

---

## Purpose

Decide whether a participant can open the notebook, run the whole analysis on the course data and see every lecture step as a screenshot in the README.

## Deliverable

A Jupyter notebook that runs the analysis through the package, a script that exports every chart to PNG, one screenshot per lecture step under `docs/images/`, and a README that shows them.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The notebook runs top to bottom with the course CSV | `jupyter nbconvert --execute` exits 0 | Any cell fails |
| 2 | Every chart step has a PNG in `docs/images/` | File count equals the number of chart steps | A step has no image |
| 3 | The README shows each screenshot and passes `check-readme.sh` | Script exits 0 | Finding |
| 4 | opengrep finds no error-severity finding | Exit 0 | A finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | The notebook and screenshots use all chart functions |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3, O4 | [BC-001] Objectives |
| Success criteria 5 | [BC-001] Success Criteria |
| Concerns CN-005, CN-006 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in in autonomous mode) |

## Target Date

2026-11-17 — after [MIL-003]; leaves two days for the wiki.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Obtain the course CSV | The CSV comes from the course download. Downloading it needs the Product Owner's permission, given when the plan is accepted, or the Product Owner places it in `data/apps.csv`; the file stays untracked. Without it the dependent tasks stop and report. | No | |
| 2 | Build the Jupyter notebook | Create `notebooks/google_play_store.ipynb` that follows the lecture order and calls the package functions, with a markdown cell per step. | No | |
| 3 | Add the chart export script | Add `src/play_store/presentation/export.py`, `scripts/make_screenshots.py` and a command that writes each figure to PNG with kaleido (optional `docs` extra), one file per lecture step. | No | |
| 4 | Generate a screenshot for every lecture step | Run the export on the real data to produce the images in `docs/images/` for the pie, donut, bars, scatter, grouped bar and box plots; the exploration steps get a table image. | No | |
| 5 | Add the screenshots and run instructions to the README | Show each screenshot under its lecture step in `README.md` and explain how to run the notebook and the tests. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-003]: ./mil-003-visualisation.md
[785d729]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/commit/785d7293943e70d627fd9536319355092051a847
