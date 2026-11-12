# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [785d729] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001], [MIL-001] | [RC-002] |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | MIL-001 to MIL-005 | [RC-003] |
| [MIL-001] | Milestone | en | it | [PP-001] | [MIL-002] | [RC-004], [RC-010] |
| [MIL-002] | Milestone | en | it | [MIL-001] | [MIL-003] | [RC-005], [RC-011] |
| [MIL-003] | Milestone | en | it | [MIL-002] | [MIL-004] | [RC-006], [RC-012] |
| [MIL-004] | Milestone | en | it | [MIL-003] | [MIL-005] | [RC-007], [RC-013], [RC-014] |
| [MIL-005] | Milestone | en | it | [MIL-004] | - | [RC-008], [RC-009] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 to CN-008 | [SA-001], [MIL-001] to [MIL-005] | - | - | Gap (no views or tests yet; covered as code is written) |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | - | None found | - | Closed | - |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-data-cleaning-exploration.md
[MIL-003]: ../milestones/mil-003-visualisation.md
[MIL-004]: ../milestones/mil-004-notebook-readme-screenshots.md
[MIL-005]: ../milestones/mil-005-wiki-release.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[RC-007]: ./reviews/rc-007-mil-004.md
[RC-008]: ./reviews/rc-008-mil-005.md
[RC-009]: ./reviews/rc-009-mil-005-delta.md
[785d729]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/commit/785d7293943e70d627fd9536319355092051a847
[RC-010]: ./reviews/rc-010-mil-001-code.md
[RC-011]: ./reviews/rc-011-mil-002-code.md
[RC-012]: ./reviews/rc-012-mil-003-code.md
[RC-013]: ./reviews/rc-013-mil-004-delta.md
[RC-014]: ./reviews/rc-014-mil-004-code.md
