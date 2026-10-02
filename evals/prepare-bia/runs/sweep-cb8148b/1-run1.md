# /prepare-bia case 1, run1: Claude Code, guidance at cb8148b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `693b1617-6dca-4a3b-b7f0-33e61efa3d56`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I need one answer before I open the three attached files: **what class of data do they hold?**

AI4BCM's data rules treat these as high-sensitivity, to be handled only in an approved corporate or private environment:

- BIA data and risk assessment detail
- personal data, contact lists and personnel records (an org chart usually counts)
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail
- vulnerabilities and control weaknesses, or recovery strategies and design assumptions

So, do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` hold any of these? If they do, is this Claude Code environment approved by your organisation for high-sensitivity data?

If it isn't approved for what the files hold, I'll stop here and won't read them. If it is, I'll draft the Site B dispatch interview guide and change nothing else.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md && ls -R; echo ---; ls -la /tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Glob: `**/*`
- Glob: `**/*`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. I've read the three attached files and the skill's sources. Before I draft anything, the BIA prompt asks me to put up to three questions that the material leaves open. Your answers will be listed under Gaps as your own statements, not as sources. They can shape the scope of the guide but won't fill any value.

1. **Who is the interviewee, and what do they know that you don't?** The only Site B source is an undated HR draft org chart with no version. It shows a "Dispatch lead, Site B (three shift leaders)". Is that the person you're interviewing, or will a shift leader or the site manager join? Do you know anything about Site B dispatch that the Site A list doesn't cover, such as whether it handles chilled goods, which warehouse system it uses, or which carriers?

2. **What do you need back from the interview?** For example, chilled dispatch only or all dispatch at Site B; whether to cover the peak weeks; and whether Site A's note "manual export to Site B possible" should be tested from Site B's side.

3. **Which of these channels are switched off for this work: memory, past chats, project files, connectors, web search?** I'll read only the three attached files and the skill's own sources. But any channel that stays on goes under Gaps, because the model may draw on it without saying so.

The impact criteria are attached (v1.1, 4 Feb 2026, approved by top management), so I won't ask about them. If you skip a question, I'll write down the assumption I made in its place.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/1/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/1/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/1/run1/work/site-b-org-chart.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Grep: `Say in the document that AI helped`
- Grep: `version`
- Grep: `five stages|Top management|top management`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: Dispatch, Site B (pre-interview draft)

**Status:** draft for the interview. Every entry is "candidate, to confirm". MTPD, RTO and RPO are blank on purpose.

## Sources

| Document | Version | Date | Status |
|---|---|---|---|
| `site-a-activity-list.md` (Site A: activity list, chilled food production) | 3 | 12 March 2026 | approved by the site manager |
| `impact-criteria.md` (Impact criteria) | 1.1 | 4 February 2026 | approved by top management |
| `site-b-org-chart.md` (Site B: organisation structure) | none | none | "Undated draft from HR, no version". Listed under Gaps and not used as current |
| `units/prompts/bia.md` (skill source) | 2026.09.1 | 2026-09 | shipped with the skill |
| `units/stages/analysis.md` (skill source) | 2026.09.1 | no date given | shipped with the skill |

## Who does what

- **Activity owner: Dispatch lead, Site B** (the organiser's statement; see Gaps). They confirm or correct each requirement below, and they set the MTPD and the RTO. A requirement goes into the register only when they confirm it.
- **Top management** approves the BIA results.
- **Interviewer:** use this draft as the thing to correct, not the thing to confirm. Record what it could not have known, such as the shift pattern, the carrier arrangements and anything Site B does that Site A does not.

## Candidate activity

| # | Candidate activity | Owner (role) | Source | Label |
|---|---|---|---|---|
| B-D1 | Dispatch at Site B. Is it chilled dispatch, as at Site A ("Dispatch, chilled"), or does it cover other goods as well? | Dispatch lead, Site B | site-a-activity-list v3, row A2; organiser's statement | candidate, to confirm |

## 1. Impacts over time

Use the approved impact criteria (v1.1). Ask for each impact type separately.

| # | Question for the Dispatch lead, Site B | Source | Label |
|---|---|---|---|
| 1.1 | If dispatch at Site B stops, how does the financial impact grow over time? When does it go past "EUR 10k–100k a day" (level 2), and when past "over EUR 100k a day" (level 3)? | impact-criteria v1.1, Financial | candidate, to confirm |
| 1.2 | When would "a key account is late" (level 2) happen, and when "a key account is lost" (level 3)? Which accounts does Site B dispatch serve? | impact-criteria v1.1, Customer | candidate, to confirm |
| 1.3 | Could a stop in dispatch lead to "a report to the food authority" (level 2) or to "the authority stops production" (level 3)? If so, how? | impact-criteria v1.1, Regulatory | candidate, to confirm |
| 1.4 | **Peak weeks:** Site A records "weeks 49–52, week 14" for chilled dispatch. Which weeks are Site B's peaks? Do the impacts in 1.1 to 1.3 come sooner in those weeks? | site-a-activity-list v3, row A2; organiser's statement | candidate, to confirm |

## 2. MTPD

| # | Question | MTPD | Label |
|---|---|---|---|
| 2.1 | Given the answers in section 1, after how long would a stop in dispatch at Site B become unacceptable? The owner sets this value; this draft does not. | *(blank)* | candidate, to confirm |

## 3. People, with the skills, authorities and mandates the work needs

| # | Question | Source | Label |
|---|---|---|---|
| 3.1 | The HR draft shows "Dispatch lead, Site B (three shift leaders)". Is that the current team? What is the shift pattern, and how many people does each shift need at minimum, in normal weeks and in peak weeks? | site-b-org-chart (undated draft); organiser's statement | candidate, to confirm |
| 3.2 | Which skills does dispatch need, and how many people on each shift have them? | not in the sources | candidate, to confirm |
| 3.3 | Who has the authority to release a load, change a carrier or switch to a manual workaround? Is that authority held by one person or by several? | not in the sources | candidate, to confirm |
| 3.4 | Who holds the carrier contacts? Do the contacts depend on one person, and are they written down somewhere the shift leaders can reach? | organiser's statement | candidate, to confirm |

## 4. Seats and buildings

| # | Question | Source | Label |
|---|---|---|---|
| 4.1 | Which building, dock and chilled storage area does dispatch at Site B work from? How many dock doors does it use? (Site A records "two dock doors" for goods receipt only.) | site-a-activity-list v3, row A1 | candidate, to confirm |
| 4.2 | Which workplaces, such as an office or shift desk, does dispatch need? Could the work be done from another location, and with what? | not in the sources | candidate, to confirm |

## 5. IT and applications, each with its RTO and its RPO

| # | Question | RTO | RPO | Source | Label |
|---|---|---|---|---|---|
| 5.1 | Does Site B use the warehouse system "LogiStock", as Site A does, or a system of its own? | *(blank)* | *(blank)* | site-a-activity-list v3, row A2 | candidate, to confirm |
| 5.2 | Site A notes "manual export to Site B possible". What arrives at Site B, in what format and through which channel? Can Site B work from it? | *(blank)* | *(blank)* | site-a-activity-list v3, row A2 | candidate, to confirm |
| 5.3 | Which other applications does dispatch use, such as carrier booking, labels or temperature records? | *(blank)* | *(blank)* | not in the sources | candidate, to confirm |

## 6. Suppliers and other third parties

| # | Question | Source | Label |
|---|---|---|---|
| 6.1 | Which carriers does Site B dispatch use? Is NordFrost one of them? Site A records "carrier NordFrost" with "no second carrier recorded". | site-a-activity-list v3, row A1 and Dependencies | candidate, to confirm |
| 6.2 | If the main carrier cannot collect, what happens? Is there another carrier, a contract or a contact for that case? This is a question for the owner, not a finding. | site-a-activity-list v3, Dependencies | candidate, to confirm |
| 6.3 | Which other third parties does dispatch need, such as packaging or temperature monitoring? | not in the sources | candidate, to confirm |

## 7. Dependencies (up- and downstream, with other departments)

| # | Question | Direction | RTO | Source | Label |
|---|---|---|---|---|---|
| 7.1 | The HR draft has QA at Site B "covered from Site A", and Site A records "lab at Site A only" and "release before dispatch". Does dispatch at Site B wait for quality release from the QA manager at Site A? | upstream | *(blank)* | site-b-org-chart (undated draft); site-a-activity-list v3, rows A2–A3 and Dependencies | candidate, to confirm |
| 7.2 | Does dispatch at Site B depend on Site A's dispatch, or does Site A depend on Site B (the "manual export to Site B")? | up- or downstream | *(blank)* | site-a-activity-list v3, row A2 | candidate, to confirm |
| 7.3 | Does dispatch depend on the Warehouse lead, Site B, for example for picking or goods receipt? | upstream | *(blank)* | site-b-org-chart (undated draft) | candidate, to confirm |
| 7.4 | Which departments or customers receive from dispatch at Site B? | downstream | *(blank)* | not in the sources | candidate, to confirm |

**Recovery times proposed by a source:** none of the sources proposes an MTPD, RTO or RPO.

## Comparison across sites: conflicts for the two owners

These go to the two owners named in each row. The model does not settle them.

| # | Point | Owners |
|---|---|---|
| C1 | Site A's dependencies list only "A2 depends on A3" for quality release. If Site B dispatch also waits on Site A QA (7.1), that dependency is not in Site A's register. | QA manager, Site A, and Dispatch lead, Site B |
| C2 | Site A counts on "manual export to Site B possible" as a fallback. Site B's side of it, whether it has capacity and can take over, is not recorded anywhere (5.2, 7.2). | Dispatch lead, Site A, and Dispatch lead, Site B |
| C3 | If Site B also uses NordFrost (6.1), both sites rely on one carrier with no second carrier recorded. | Dispatch lead, Site A, and Dispatch lead, Site B |

## Gaps

- **Site B org chart:** "Undated draft from HR, no version". Not used as current; it serves only to prompt questions. A dated, versioned HR structure would settle it.
- **Organiser's statements, not sources:**
  - "The dispatch lead at Site B; they know the shift pattern and the carrier contacts."
  - "Resources and peak weeks."
- **Question 3 skipped (memory, past chats, project files, connectors, web search):** I assumed none was confirmed off. The model may draw on any channel left on without saying so. For this draft I read only the three attached files and the skill's sources, and I used no web search.
- **Site B activity list or register:** not in the sources. Every Site B entry above is drawn from Site A material or from the organiser's statements.
- **Whether Site B handles chilled goods:** not in the sources.
- **Carrier contacts** are personal data. Record them in the approved register, not in this guide.
- No instructions to an AI were found in the attached files.

## For the auditor

Each register entry will carry the source, the interview it came from and the date behind it. In this pre-interview draft three fields stay blank:

| Field | Value |
|---|---|
| Interview | |
| Date the owner confirmed | |
| Recovery times the owner set (MTPD / RTO / RPO) | |

Hand the register on with every entry still labelled "candidate, to confirm" until its owner confirms it, so the next stage can see which entries were drafted and never challenged.

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

I haven't written any file or published the guide anywhere, given the data class. If you want it saved, give me a path inside your approved environment and I'll write it there as a `.md` file.

**Tool calls (stream-json):**

- none
