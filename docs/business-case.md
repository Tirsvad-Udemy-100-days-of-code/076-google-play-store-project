# Google Play Store Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version; Go in RC-001 (autonomous, not independent) | pending |

---

## Executive Summary

The Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" sets, on Day 76, an analysis of Google Play Store data: clean a scraped data set of about 10,800 Android apps and answer six market questions (category competition, category popularity, the cost of charging for an app, a sensible price, the highest-earning paid apps, and whether paid apps recoup development cost) with Plotly charts. This project turns the assignment into a clean, tested, documented Python repository that other course participants can read and run, and that GitHub visitors can browse for ideas. Recommendation: proceed.

## Methodological and Standards Foundation

The documents follow the SQA and QC framework mounted at `framework/` (Larman, *Applying UML and Patterns*, for the analysis artifacts). Quality is judged against ISO/IEC 25010:2023 characteristics through the framework's QC checklists. Code follows the `coding-conventions` skill for Python and the layering of the `clean-architecture` skill. Each lecture step is documented in a wiki in English, Danish and Bahasa Malaysia.

## Problem Statement

- The course delivers the assignment as an unstructured Google Colab notebook: cells depend on hidden execution order, nothing is tested, and the data set and dependencies are not pinned.
- Participants who compare solutions cannot easily run another person's notebook, and cannot see what each step teaches.
- A repository that is only a notebook gives GitHub visitors no explanation of the result or of the method.

## Business Opportunity

A repository that keeps the assignment's function names and step order, but adds a runnable package, tests, screenshots of every chart and a three-language wiki, becomes a reusable reference. It also serves as a portfolio piece that shows the data-cleaning and visualisation skills of the Product Owner.

## Objectives

1. **O1** Reproduce every lecture step of Day 76 (cleaning, exploration, pie and donut, bar, scatter, grouped bar, box charts) as importable Python functions with the names used in the assignment.
2. **O2** Verify the cleaning and aggregation logic with automated tests that run without the real data set.
3. **O3** Provide a Jupyter notebook that runs the whole analysis end to end.
4. **O4** Document each lecture step with a screenshot in the README and in the wiki, and explain in the wiki what the step teaches, in English, Danish and Bahasa Malaysia.
5. **O5** Describe the repository on the git host with a description, topics and a README that gives set-up, run and test instructions.

## Scope

### In Scope

- Python package under `src/` with the Day 76 steps; tests under `tests/`; documents under `docs/`.
- `pyproject.toml`, a local `.venv` workflow and a Python `.gitignore`.
- A Jupyter notebook that uses the package.
- Screenshots of every chart, generated from the course data set.
- README from the framework template; wiki pages in en, da and ms.
- Repository description and topics on the git host.
- A static analysis run with opengrep before every push.

### Out of Scope

- Redistributing the course data set or the course notebook (the Product Owner supplies the CSV locally; see Assumptions).
- A web application, an API or a database.
- Scraping the Google Play Store, or any data other than the course file.
- Machine learning or forecasting.
- Any use of the tokens in `.env`: they are for the Product Owner's tooling only and are never imported, tested or read by the project.

## Expected Benefits

### Tangible Benefits

- A runnable repository with passing tests and a one-command set-up.
- A screenshot for every chart step, with explanations in three languages.

### Intangible Benefits

- Better understanding of pandas cleaning and Plotly charting.
- A clear, reviewable example of plan-first delivery with the SQA and QC framework.

## Strategic Alignment

The project supports the Product Owner's learning goal of finishing the 100 Days of Code bootcamp with public, reviewable work (S01), and the course community's habit of sharing and comparing solutions (S02, S03).

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Lecture steps implemented as functions | 100% of the Day 76 steps listed in the milestone tasks | Task rows closed; function names match the assignment |
| 2 | Automated tests pass | 0 failures, line coverage of `src/` at least 90% | `python -m pytest --cov` |
| 3 | Static analysis | 0 findings of severity error before each push | opengrep run |
| 4 | Set-up from a clean clone | `pip install -e .[dev]` and `pytest` succeed on Python 3.13 or newer | README steps run in a fresh `.venv` |
| 5 | Screenshots | One per chart step in README and in each wiki language | File count and page check |
| 6 | Wiki languages | 3 languages with the same page set | Page lists of en, da and ms are equal |
| 7 | Runtime dependencies | Only pandas and plotly | `[project] dependencies` in `pyproject.toml` |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The course data set is not freely redistributable | Licence problem if committed | The CSV is ignored by git; the README explains where to place it; tests use a small synthetic fixture |
| The signed course download link expires or is refused | The real charts and screenshots cannot be produced | Tests do not depend on it; the Product Owner supplies the file; the dependent tasks wait for it |
| Chart-to-PNG export needs extra tools (kaleido, a browser) | Screenshots cannot be generated automatically | Keep export in an optional `docs` extra; fall back to browser screenshots |
| Translations contain errors | Misleading wiki text | English is authoritative; Danish and Malay follow it page by page and the page sets are compared |
| Secrets in `.env` leak into the repository | Credential compromise | `.env` is in `.gitignore`; the project never reads it; opengrep scan before every push |

## Assumptions

- The Product Owner (S01) is also the developer and the reviewer; in autonomous mode the AI acts as stand-in reviewer and the review records say so.
- The data set is the "Google Play Store" CSV from the course, with the columns named in the lecture; it is supplied by S01 or downloaded with S01's permission.
- The data was scraped around 2017/2018 and is a sample, not the whole store.
- Course participants (S02) and visitors (S03) cannot be interviewed within this project; their needs are taken from the assignment text.
- The git host is Gitea at git.tirsystem.com and accepts the tokens in the Product Owner's `.env`.

## Constraints

- Python 3.13 or newer; a `venv` for the environment; configuration in `pyproject.toml`.
- Folder structure `src/`, `tests/`, `docs/`.
- Runtime dependencies limited to what the assignment needs (pandas, plotly).
- One branch and one pull request per milestone; no commits on `main`.
- Duration: one week, 2026-11-12 to 2026-11-19.
- GUI or end-to-end tests, if any, run in a container, never on the host desktop.

## Cost–Benefit Assessment

Qualitative, because this is a personal learning project with no revenue and no budget; money is not the measure.

| Costs | Benefits |
| --- | --- |
| About one week of S01's attention for review and the data supply | A public, tested reference solution |
| AI effort for implementation, tests and translation | Reusable documentation in three languages |
| Hosting on the existing Gitea instance (no extra cost) | A worked example of the framework |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| [S01][SA-001] | Product Owner, developer and reviewer; wants public, reviewed work |
| [S02][SA-001] | Course participants; want readable, runnable code with the assignment's names |
| [S03][SA-001] | GitHub viewers; want a clear description, topics and README |

## Recommendation

Proceed — the assignment is small, the outcome is useful to three audiences and the risks have mitigations.

---

[SA-001]: ./stakeholder-analysis.md
