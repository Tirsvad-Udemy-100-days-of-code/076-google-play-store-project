# MIL-001 Project Setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version; Go in RC-004 (autonomous, not independent) | pending |

---

## Purpose

Decide whether the repository is ready to receive code: the Python project configuration, the local environment instructions, the ignore rules, the security scan and the description on the git host are in place.

## Deliverable

A repository skeleton with `pyproject.toml`, `src/` and `tests/` folders, a Python `.gitignore`, a README built from the framework template with `.venv` instructions, a local opengrep script, and a repository description with topics on Gitea.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e .[dev]` and `python -m pytest` succeed in a fresh `.venv` on Python 3.13 or newer | Both exit 0 | Either fails |
| 2 | `.env` and the data folder are ignored by git | `git check-ignore .env data/apps.csv` lists both | Either is not ignored |
| 3 | The README follows the framework template and passes `check-readme.sh` | Script exits 0 | Script reports a finding |
| 4 | The opengrep scan of the repository runs | Exit 0 and no error-severity finding | A finding or a failed run |
| 5 | The Gitea repository has a description and at least five topics | API returns both | Description or topics empty |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None (first gateway after the accepted baseline) | The baseline documents are accepted before this gateway starts |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O5 | [BC-001] Objectives |
| Success criteria 4 and 7 | [BC-001] Success Criteria |
| Concerns CN-003, CN-005, CN-007, CN-008 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in in autonomous mode) |

## Target Date

2026-11-13 — inside the one-week window of the Business Case (2026-11-12 to 2026-11-19).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml and the src/tests layout | Create `pyproject.toml` (requires-python >=3.13, runtime dependencies pandas and plotly only, optional extras `dev`, `notebook` and `docs`) and the `src/play_store/` package and `tests/` folders, following the clean-architecture folder structure. Keeps the runtime dependency list minimal for S03. | No | |
| 2 | Add the Python .gitignore | Add a Python `.gitignore` that also ignores `.env`, `.venv/`, the `data/` folder holding the course CSV, and notebook checkpoints, so secrets and the non-redistributable data set never reach the repository. | No | |
| 3 | Document the local .venv and pip upgrade | Write the README Setup section with the commands to create and activate `.venv` (Windows and POSIX), run `python -m pip install --upgrade pip` and install the project with its extras. Course participants can then run the project on a clean clone. | No | |
| 4 | Write the README from the framework template | Build `README.md` from `framework/templates/README-template.md` with overview, requirements, setup, run, tests, license and links; the screenshots are added later in MIL-004. | No | |
| 5 | Add pytest configuration and a smoke test | Configure pytest and coverage in `pyproject.toml` and add one smoke test that imports the package, so the test command works before any feature exists. | No | |
| 6 | Add the local opengrep scan | Add a script that runs `~/.opengrep/cli/latest/opengrep.exe` over the repository and document that it runs before every push to Gitea. | No | |
| 7 | Set the repository description and topics | Use the Gitea API with the repository token from the untracked `.env` (never imported by the project) to set a description and topics such as python, pandas, plotly, data-visualization, google-play-store, udemy, 100-days-of-code, jupyter. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
