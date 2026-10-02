# /prepare-bia case 1, run1: Claude Code, guidance at 3f263b8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `081b4239-ed83-4df5-85b8-a8bbad0356c7`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, I need one answer.

**What class of data do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` hold?** For example: public, internal, confidential or restricted, or your organisation's own label. An org chart often contains personal data such as names and roles, so please mention that too.

If this environment isn't approved for that class, I'll stop there. If it is, I'll read the files and write the Site B dispatch interview guide as a draft in this chat. I won't create, write or send anything.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md && ls -R units 2>/dev/null | head -50; echo ---; cat units/prompts/bia.md; ech`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Glob: `*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The data class is high and you've confirmed this environment is approved for it, so I've read the three files. Before I draft anything I need three answers. The interview prompt allows at most three questions, and I'll list your answers under Gaps as your own statements. They can shape the scope of the guide but won't be used as values or sources.

1. **Who is the interviewee, and what do they know that you don't?** The Site B org chart is an undated HR draft with no version. It shows a "Dispatch lead, Site B (three shift leaders)". Is that the person you're interviewing, or is it one of the shift leaders? What do you expect them to know that isn't written down, such as Site B's own warehouse system, carriers, peak weeks or how quality release works at Site B?
2. **What do you need back from this interview?** For example: confirmed candidate dispatch activities and their resource requirements, a date for a later session where the owner sets MTPD and RTO, or an answer on how Site B depends on Site A. Site A's list says "manual export to Site B possible" and "QA: covered from Site A".
3. **Are memory, past chats, project files, connectors and web search switched off for this work?** If any of them is on, the model may draw on it without saying so. I'll record any that stays on under Gaps.

I'll draft the guide once you've answered. If you skip a question, I'll write down the assumption I made instead.

**Tool calls (stream-json):**

- Glob: `units/**/*`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/1/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/1/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/1/run1/work/site-b-org-chart.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/workflow-design.md`
- Glob: `*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/SKILL.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: Dispatch, Site B (draft before the interview)

**Status:** draft. Every entry is marked "candidate, to confirm". Nothing here goes into the register until the activity owner confirms it.
**Interviewee:** the Dispatch lead at Site B. You named this person, and the undated HR draft shows the same role.
**Reviewers:** the activity owner (Dispatch lead, Site B) confirms each requirement and sets the MTPD and RTO. Top management approves the BIA results.

## Sources and dates

- `site-a-activity-list.md`: version 3, 12 March 2026, approved by the site manager.
- `impact-criteria.md`: version 1.1, 4 February 2026, approved by top management.
- `site-b-org-chart.md`: no version and no date, a draft from HR. It is listed under Gaps and not treated as current. I used it only to word questions.
- Method documents that come with the skill: `units/prompts/bia.md` 2026.09.1 (2026-09), `units/stages/analysis.md` 2026.09.1, `units/workflow-design.md` 2026.09.1.

## How to run the interview

Use the draft as the thing to correct, not the thing to confirm, and record what it could not have known. The draft knows nothing about Site B's shift pattern or carrier contacts, so expect to fill those in.

---

## Candidate activity

| ID | Question for the owner | Source | Mark |
|---|---|---|---|
| B-D1 | Site A lists the activity "Dispatch, chilled". Is dispatch at Site B the same activity? Does it handle chilled goods? What does your team do that isn't on Site A's list? | `site-a-activity-list.md`, A2 | candidate, to confirm |

## 1. Impacts over time

The impact criteria set levels but no time horizons. The interviewer records the time points the owner names. The impact level at each time point is left blank for the owner.

| ID | Question for the owner | Source | Mark | Interview | Confirmed on |
|---|---|---|---|---|---|
| 1.1 | If dispatch at Site B stops, how long until the loss is between EUR 10k and 100k a day (level 2)? How long until it is over EUR 100k a day (level 3)? | `impact-criteria.md`, Financial | candidate, to confirm | (empty) | (empty) |
| 1.2 | How long until a key account is late (level 2)? How long until one is lost (level 3)? | `impact-criteria.md`, Customer | candidate, to confirm | (empty) | (empty) |
| 1.3 | Could a stop lead to "a report to the food authority" (level 2)? Could it lead to "the authority stops production" (level 3)? | `impact-criteria.md`, Regulatory | candidate, to confirm | (empty) | (empty) |
| 1.4 | Site A's dispatch peaks in "weeks 49–52, week 14". Which weeks are Site B's peak weeks? Do the impacts above come sooner in those weeks? | `site-a-activity-list.md`, A2; you asked for peak weeks | candidate, to confirm | (empty) | (empty) |

## 2. MTPD

| ID | Question for the owner | Source | Mark | MTPD (the owner sets it) |
|---|---|---|---|---|
| 2.1 | Looking at your answers in section 1, after how long would a stop of dispatch at Site B become unacceptable? | `impact-criteria.md`; `units/stages/analysis.md`, Method | candidate, to confirm | (empty) |

## 3. People, with the skills, authorities and mandates the work needs

| ID | Question for the owner | Source | Mark | Interview | Confirmed on |
|---|---|---|---|---|---|
| 3.1 | The HR draft shows you with "three shift leaders". Is that current? What is the shift pattern? | `site-b-org-chart.md` (undated draft); your statement | candidate, to confirm | (empty) | (empty) |
| 3.2 | How many people does dispatch need per shift at the minimum, normally, and in peak weeks? | not in the sources | candidate, to confirm | (empty) | (empty) |
| 3.3 | Which skills does the work need, including using the warehouse system? Who in each shift has them? | `site-a-activity-list.md`, A2 ("LogiStock") | candidate, to confirm | (empty) | (empty) |
| 3.4 | Who has the authority to dispatch, to switch to the manual export, and to book or change a carrier? | `site-a-activity-list.md`, A2 and the dependencies line | candidate, to confirm | (empty) | (empty) |
| 3.5 | You hold the carrier contacts. Who else holds them, and where are they written down? Who stands in for you in each shift? | your statement | candidate, to confirm | (empty) | (empty) |

## 4. Seats and buildings

None of the sources describes Site B's buildings.

| ID | Question for the owner | Source | Mark | Interview | Confirmed on |
|---|---|---|---|---|---|
| 4.1 | Which building, loading area and office seats does dispatch at Site B use? | not in the sources | candidate, to confirm | (empty) | (empty) |
| 4.2 | Site A records "two dock doors" for goods receipt. How many dock doors does dispatch at Site B use? Can goods leave another way if those doors are unavailable? | `site-a-activity-list.md`, A1 | candidate, to confirm | (empty) | (empty) |
| 4.3 | Does dispatch need a chilled area at Site B? | `site-a-activity-list.md`, A2 ("chilled") | candidate, to confirm | (empty) | (empty) |

## 5. IT and applications, each with its RTO and its RPO

| ID | Question for the owner | Source | Mark | Interview | Confirmed on | RTO | RPO |
|---|---|---|---|---|---|---|---|
| 5.1 | Site A's dispatch uses "LogiStock". Does Site B use LogiStock, another system, or both? | `site-a-activity-list.md`, A2 | candidate, to confirm | (empty) | (empty) | (empty) | (empty) |
| 5.2 | Site A records "manual export to Site B possible". What does Site B receive, in what form, and what does dispatch do with it? | `site-a-activity-list.md`, A2 | candidate, to confirm | (empty) | (empty) | (empty) | (empty) |
| 5.3 | Which system or channel do you use to reach the carriers? | your statement (carrier contacts) | candidate, to confirm | (empty) | (empty) | (empty) | (empty) |

## 6. Suppliers and other third parties

| ID | Question for the owner | Source | Mark | Interview | Confirmed on |
|---|---|---|---|---|---|
| 6.1 | Which carriers does dispatch at Site B use? For Site A, NordFrost is recorded for A1 and A2 with "no second carrier recorded". Does Site B use NordFrost? Is there a second carrier? | `site-a-activity-list.md`, A1, A2 and the dependencies line | candidate, to confirm | (empty) | (empty) |
| 6.2 | Which other third parties does dispatch at Site B rely on? | not in the sources | candidate, to confirm | (empty) | (empty) |

## 7. Dependencies

These are up- and downstream relationships with other departments. Each is recorded with the RTO the relationship carries.

| ID | Question for the owner | Source | Mark | Interview | Confirmed on | RTO of the relationship |
|---|---|---|---|---|---|---|
| 7.1 | Upstream: quality release at Site A (A3). Site A records "A2 depends on A3 (release before dispatch)" and "lab at Site A only". The HR draft says "QA: covered from Site A". Does dispatch at Site B have to wait for a release from Site A? | `site-a-activity-list.md`, A3 and the dependencies line; `site-b-org-chart.md` (undated draft) | candidate, to confirm | (empty) | (empty) | (empty) |
| 7.2 | Dispatch at Site A (A2), where Site A records "manual export to Site B possible". Which way does this relationship run, and when is it used? | `site-a-activity-list.md`, A2 | candidate, to confirm | (empty) | (empty) | (empty) |
| 7.3 | Upstream: the warehouse at Site B, under the Warehouse lead, Site B. What does dispatch need from the warehouse? | `site-b-org-chart.md` (undated draft) | candidate, to confirm | (empty) | (empty) | (empty) |
| 7.4 | Downstream: which departments or customers receive from dispatch at Site B? | not in the sources | candidate, to confirm | (empty) | (empty) | (empty) |

**Recovery times proposed by the sources:** none. No attached source proposes an MTPD, RTO or RPO.

---

## Points to put to the owners at both sites

No register for Site B was attached. This compares Site A's activity list with the Site B org chart. Each point goes to the two owners named, not to the model.

- **C1, quality coverage.** The Site B draft says "QA: covered from Site A". Site A's list records a dependency on A3 only for A2, and nothing for Site B. Put this to the QA manager at Site A and the Dispatch lead at Site B.
- **C2, manual export.** Site A records "manual export to Site B possible" under A2. Site B's material says nothing about it. Put this to the Dispatch lead at Site A and the Dispatch lead at Site B.
- **C3, carrier.** This is a possible shared supplier, not yet a conflict. If Site B confirms NordFrost, then the carrier Site A relies on, with "no second carrier recorded", serves both sites. Put this to the Dispatch lead and Warehouse lead at Site A and the Dispatch lead at Site B.

## Gaps

- **Your own statements (not sources).** You said the interviewee is the Dispatch lead at Site B, who knows the shift pattern and the carrier contacts. You need back resources and peak weeks. These shaped the scope of the guide. They did not fill any values.
- **Question 3 was skipped**, so I am assuming memory, past chats, project files, connectors and web search may still be switched on. If any of them is on, the model may draw on it without saying so. In this session I read only the three attached files and the method documents that come with the skill.
- **`site-b-org-chart.md`** is an undated draft with no version, so it isn't used as current. HR's current approved chart would settle this.
- **The impact criteria have no time horizons.** Only the financial levels are stated per day. Time horizons are a method parameter and need to be agreed before the interview, not set in it.
- **Missing about Site B.** There is no activity list or register for Site B. Its systems, carriers, buildings, peak weeks and downstream recipients are "not in the sources".
- **Instructions inside the documents:** none found.

## For the auditor

Each register entry carries its source, the interview it came from, and the date. In this draft, three fields are left blank for every entry: the interview, the confirmation date, and the recovery times the owner set. Every entry stays marked "candidate, to confirm" when it is handed on.

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

> Parts of this document were drafted with AI support (prepare-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- none
