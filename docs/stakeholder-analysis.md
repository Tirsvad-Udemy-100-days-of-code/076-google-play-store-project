# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version; Go in RC-002 (autonomous, not independent) | [785d729] |

---

## Purpose

This analysis names the people the Google Play Store Analysis project serves, how much power and interest each has, and what each needs, so that owners and reviewers elsewhere can cite stable IDs. It uses the power/interest grid and maps concerns to FURPS+.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad (personal) | HIGH | HIGH | Manage Closely | Finish Day 76 with clean, reviewed, public work |
| S02 | Udemy course participants | Fellow learners who share and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and run instructions in the README |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no heavy runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, accepts the plan and owns every review; interest is the learning goal.
- **Keep Informed (S02):** cannot change the project but depends on its readability and on the instructions to run it; informed through the README and the wiki.
- **Monitor (S03):** no say in the project and only passing interest; served by a good description, topics and README.
- **Keep Satisfied:** no stakeholder.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every lecture step is reproduced and checked, not just run once | Functionality |
| CN-002 | S01 | Work is reviewed and traceable before it is pushed | Supportability |
| CN-003 | S01 | Secrets in `.env` never reach the repository or the project code | Functionality (security) |
| CN-004 | S02 | Function names and step order follow the assignment | Usability |
| CN-005 | S02 | Instructions to create a `.venv`, install and run work on a clean clone | Usability |
| CN-006 | S02 | Each chart step is explained, in a language the participant reads | Usability |
| CN-007 | S03 | Repository description, topics and README tell what the project is | Usability |
| CN-008 | S03 | No runtime dependencies beyond the analysis libraries | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat with S01 | At plan acceptance and at the end of the run | Plan dry run; run summary with every stand-in decision | All milestones |
| CR-002 | Pull request on Gitea | One per milestone | Change, review record, closed issues | All milestones |
| CR-003 | README and wiki | At the documentation milestones | Run instructions, screenshots, explanations in en, da, ms | MIL-004, MIL-005 |
| CR-004 | Repository description and topics | Once | Short description and topic list | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no runtime dependencies; the assignment needs pandas and Plotly | S03, S01 | Runtime dependencies are limited to pandas and plotly; Jupyter, pytest, coverage and image export are optional extras, so a viewer installs nothing to read the repository |
| S02 wants the assignment's names; clean-code conventions prefer other names | S02, S01 | Public functions keep the assignment's names (`snake_case` as in the lecture); internal helpers follow the conventions |
| S01 wants fast delivery; S02 and S03 want three-language documentation | S01, S02 | The wiki is a separate milestone after the code; English first, then Danish and Malay with the same page set |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002, CN-003 | O1, O2, O3 ([BC-001]) |
| S02 | CN-004, CN-005, CN-006 | O1, O3, O4 ([BC-001]) |
| S03 | CN-007, CN-008 | O5 ([BC-001]) |

## Sign-Off

Product Owner: S01. Reviewed in autonomous mode by the AI as stand-in for S01; not independent.

---

[BC-001]: ./business-case.md
[785d729]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/commit/785d7293943e70d627fd9536319355092051a847
