# MIL-005 Wiki and Release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version; Go in RC-008 (autonomous, not independent) | [785d729] |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Task 1 adds Getting-Started page with Windows and Linux guides, as S01 asked in chat; delta Go in RC-009 (autonomous, not independent) | [785d729] |

---

## Purpose

Decide whether the project is ready to be public: the wiki explains what each lecture step teaches, in three languages, with screenshots, and the first release is tagged.

## Deliverable

Wiki pages in `docs/wiki/` in English, Danish (`-da`) and Bahasa Malaysia (`-ms`) with the same page set, a sidebar, and the pages published to the Gitea wiki; release v1.0.0.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The three languages have the same page set | File lists match after removing the suffix | A page is missing in a language |
| 2 | Every lecture-step page has its screenshot | Image link present on each page | A page without image |
| 3 | The wiki passes review against `QC-WIKI-001` with verdict Go | RC record says Go | No-Go |
| 4 | The Gitea wiki shows Home and the language links | Page fetched from the host | Missing |
| 5 | opengrep and the full test suite pass before the final push | Exit 0 | Failure |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] | The wiki uses the screenshots and the README text |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O4, O5 | [BC-001] Objectives |
| Success criteria 5 and 6 | [BC-001] Success Criteria |
| Concerns CN-006, CN-007 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in in autonomous mode) |

## Target Date

2026-11-19 — last day of the Business Case window.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the English wiki | Create `Home.md`, `_Sidebar.md`, `Summary.md`, a `Getting-Started.md` page with a Windows (PowerShell) and a Linux/macOS guide to create the `.venv`, upgrade pip, install and run the notebook and tests (modelled on the Getting-Started page of the sibling Lego analysis wiki), and one page per lecture step (cleaning, exploration, content rating, categories, genres, free versus paid, box plots) that says what the step teaches and shows its screenshot. | No | |
| 2 | Write the Danish wiki | Translate every English page to `*-da.md` with the same page set and the language line at the top. | No | |
| 3 | Write the Bahasa Malaysia wiki | Translate every English page to `*-ms.md` with the same page set and the language line at the top. | No | |
| 4 | Publish the wiki to Gitea | Push the pages to the repository wiki using the wiki token from the untracked `.env`, and check Home and the language links on the host. | No | |
| 5 | Tag and release v1.0.0 | Create the v1.0.0 tag and Gitea release with notes, using the release token from `.env`, after the final tests and opengrep scan. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-004]: ./mil-004-notebook-readme-screenshots.md
[785d729]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/commit/785d7293943e70d627fd9536319355092051a847
