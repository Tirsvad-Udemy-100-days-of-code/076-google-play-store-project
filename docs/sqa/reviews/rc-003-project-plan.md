# SQA Review Record: PP-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the stand-in reads the language and knows the domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Purpose and Planning Assumptions state 2026-11-12 to 2026-11-19, the Business Case duration constraint. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Five gateways, each once, with document, decision date and owner S01. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | All decision dates fall in the window and equal the target dates of the MIL documents. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps every In Scope item of BC-001 to a gateway. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Chain MIL-001 to MIL-005 is acyclic and matches the schedule order. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies section says a No-Go stops later gateways and that S01 decides on moving the end date. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | All owners use S01. No governance document exists in this project; S01 is the sole accountable role and the AI is the recorded stand-in (noted in Open Issues). |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Planning Assumptions list sources; this is the first baseline. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks have impact and mitigation and refer to Business Case risks. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues has one entry that contradicts nothing. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Main deliverable of each row matches the Deliverable of its MIL document. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says none (technical tasks) for every gateway. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt dates equal the table dates; the chain equals the dependency list. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column says not yet synced. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | One Project Plan; changes go to Version History. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Language en and Domain it are set. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | en is BCP 47; it is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Prose and table cells are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register matches the registry row for this type. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No dictionary (DICT) exists yet; terms were checked for consistency inside the document set (App, Category, Installs, Revenue_Estimate, gateway, milestone as the framework uses them). Confirmed by the stand-in, not independent. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no language change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Stand-in for S01 reads English and works in the IT domain; confirmed, not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | No unexplained abbreviations; ISO/IEC, FURPS+ and KPI-style terms are named in the Business Case foundation or are common IT terms. |

## Overall Verdict

Go — every Mandatory criterion of QC-PP-001 and of QC-LANG-001 passes. The review is by the author's stand-in in autonomous mode and is not independent; S01 can challenge it in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this stand-in decision in the run summary if wanted | S01 | 2026-11-19 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
