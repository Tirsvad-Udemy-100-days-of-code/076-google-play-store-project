# SQA Review Record: MIL-003 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [0b07b81] |

---

## Artifact Under Review

- Instance reviewed: [MIL-003] (its Python code: src/play_store/application/aggregations.py, presentation/charts.py, domain/rules.py, tests)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | snake_case modules and functions, UPPER_SNAKE constants; ruff passes the E/F/I/UP/B rule set. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names follow the assignment (drop_unused_columns, remove_duplicates, ...); no unexplained abbreviations. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` exit 0; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function is annotated including return types; reviewed by reading the sources. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; missing file raises FileNotFoundError with guidance. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtins shadowed. |
| 7 | Files, locks and connections are managed with context managers | Pass | File reading goes through pandas.read_csv; no raw handles are kept open. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules and functions have docstrings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print and no logging calls; nothing is logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | The tasks are plain technical tasks with no Design Class Diagram; the planned functions are listed in the milestone Tasks. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | pytest tests named for behaviour, independent of order and network; coverage is 100% (gate 90%). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | N-A | Optional: no type checker is configured for this project. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Dependencies are declared in pyproject.toml with lower bounds; none unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Constants (columns, price limit, defaults) are defined once in `domain/rules.py` where code exists. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | Domain imports nothing; application imports domain; asserted by tests/unit/test_architecture.py where code exists. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Small single-purpose pure functions; no class hierarchies. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | domain, application, infrastructure and presentation packages under src; tests/unit and tests/integration. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Names are English, lower case, with only letters, digits and underscores. |

## Overall Verdict

Go — no Mandatory criterion fails. Reviewed by reading all sources; 54 tests, 100% coverage, ruff and opengrep clean; every lecture chart setting is asserted. Stand-in review, not independent; S01 can challenge it in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this stand-in decision in the run summary if wanted | S01 | 2026-11-19 |

---

[MIL-003]: ../../milestones/mil-003-visualisation.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[0b07b81]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/commit/0b07b81c7d29d2060a6615904900460fceb08a83
