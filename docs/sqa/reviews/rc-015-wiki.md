# SQA Review Record: Wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [QC-WIKI-001], [MIL-005] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [04d9840] |

---

## Artifact Under Review

- Instance reviewed: the wiki in `docs/wiki/` (task 1 to 4 of [MIL-005])
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | docs/wiki/_Sidebar.md exists and is published. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Sidebar starts with the bold title and has one English page list, Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All 12 English pages are listed; all 36 published pages answer HTTP 200 on the host. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | No related wikis, so no Related section exists. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages is the last sidebar section with English, Dansk and Bahasa Melayu linking to the three Home pages. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list is not repeated per language. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is maintained by hand in the repository; no generator belongs to the project. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English and Danish (PO language is English, Danish and Malay are extra). |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | 12 pages in each of en, da and ms. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Each page starts with the language line with the current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Files are Page.md, Page-da.md and Page-ms.md. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Commands, file names, IDs and function names are English in all three languages. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | After the merge of the wiki and of MIL-004: 36 pages and 16 screenshot URLs checked with HTTP 200 on git.tirsystem.com; sidebar Languages section present. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | Optional: no change to layout rules. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | docs/wiki is flat: 37 files, no subfolder. |

## Overall Verdict

Go — no Mandatory criterion fails and criterion 14 was checked on the published wiki. The Danish and Malay text was written by the AI and has not been read by a native speaker; S01 can challenge this stand-in review in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read the Danish and Malay pages for wording | S01 | 2026-11-19 |

---

[MIL-005]: ../../milestones/mil-005-wiki-release.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[04d9840]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/076-google-play-store-project/commit/04d9840682cb2d612885c4bd696bf1572197b362
