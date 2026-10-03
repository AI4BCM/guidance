# /prepare-bia case 1, run2: Claude Code, guidance at 4dc1660

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `57ee80ea-7764-4d1a-8fa0-89299cd92727`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three attached files, one question:

**What class of data do site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md hold?** For example: public, internal, confidential or restricted, using your organisation's own scheme.

I need your answer because the class decides whether this environment can be used for the material at all. I'll go by what you tell me, not by any marking inside the files. Until you answer, I won't open, list, search or read them. Once you've answered, I'll ask up to three short questions about the interview and then write the draft.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia; cat preflight.md; echo ----; cat units/prompts/bia.md; echo ----; ls -R units | head -50; echo --`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Glob: `*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. The material is high-sensitivity and you've said this environment is approved for that class, so I've read the three attached files.

For this draft I use only those three files and the skill's own sources. Memory, past chats, project files, connectors and web search are off; if any of them is on in your setup, tell me and I'll record it under Gaps.

The files leave three things open:

1. **Who is the interview with?** The Site B org chart lists a Dispatch lead with three shift leaders under them, but it doesn't name anyone. Will it be the Dispatch lead alone, or one or more shift leaders as well?
2. **What do you need back from the interview?** For example, confirmed resource requirements for dispatch only, or also the dependencies on QA release at Site A and on goods receipt. Anything else, such as a first view of the MTPD?
3. **How long does it run?** I'll use this to set the rough time for each section and to mark which sections to drop first if it runs late.

I'll record your answers under Gaps as your own statements, not as sources. They can shape the scope but won't fill any value. If you skip a question, I'll state the assumption I made instead.

**Tool calls (stream-json):**

- Glob: `units/**/*.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/1/run2/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/1/run2/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/1/run2/work/site-b-org-chart.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: chilled dispatch at Site B (draft)

**Sources**
- `site-a-activity-list.md`: version 3, 12 March 2026, approved by the Site A site manager. It describes Site A only, so here it only suggests questions for Site B.
- `impact-criteria.md`: version 1.1, 4 February 2026, approved by top management.
- `site-b-org-chart.md`: no version and no date, a draft from HR. It is listed under Gaps and not used as current.

**Status of every entry: candidate, to confirm.** None of the sources shows a Site B entry as confirmed. MTPD, RTO and RPO are left empty everywhere, including each dependency's RTO.

**For the dispatch lead:** use this draft as the thing to correct, not the thing to confirm. Record what it could not have known.

## Candidate activity

| # | Question for the activity owner | Label | Source |
|---|---|---|---|
| D1 | Does Site B run chilled dispatch as its own activity, and are you its owner? | candidate, to confirm | site-a-activity-list.md, row A2; site-b-org-chart.md (draft, see Gaps) |
| D2 | Does Site B dispatch handle anything Site A's list doesn't show, for example loads that arrive by "manual export to Site B" from Site A? | candidate, to confirm | site-a-activity-list.md, row A2 Notes |

Impacts over time are rated in full only for D1. The sources rank nothing higher for Site B, and D1 is the scope you set. D2 gets questions only where it differs from D1.

## 1. Impacts over time

The impact criteria give the financial level per day. The customer and regulatory levels have no time attached.

| Checkpoint (organiser may adjust) | Financial (level 1–3) | Customer (level 1–3) | Regulatory (level 1–3) |
|---|---|---|---|
| first shift lost | | | |
| first day lost | | | |
| three days lost | | | |
| one week lost | | | |

The checkpoints are only the shape of the interview. They are not values. The owner fills every cell. Source: impact-criteria.md, table.

| # | Question | Label | Source |
|---|---|---|---|
| I1 | Are Site B's dispatch peak weeks the same as Site A's ("weeks 49–52, week 14")? If not, which weeks? | candidate, to confirm | site-a-activity-list.md, row A2 Peak weeks; organiser's scope (Gaps) |
| I2 | In a peak week, at which point does a stoppage reach each level: "a key account is late", "a key account is lost", over EUR 100k a day? | candidate, to confirm | impact-criteria.md, table |
| I3 | Can a dispatch stoppage lead to "a report to the food authority" or worse? At which point? | candidate, to confirm | impact-criteria.md, Regulatory column |
| I4 | For loads arriving by manual export from Site A: does a stoppage hit differently from D1? Ask only if it does. | candidate, to confirm | site-a-activity-list.md, row A2 Notes |

## 2. MTPD

| Activity | MTPD | Source |
|---|---|---|
| D1 Chilled dispatch, Site B | *(left empty; the owner sets it)* | — |

Question M1: from the impact ratings above, after how long would a stoppage become unacceptable?

## 3. People, with the skills, authorities and mandates the work needs

| # | Question | Label | Source |
|---|---|---|---|
| P1 | Does the draft org chart still hold: a dispatch lead with three shift leaders? How many staff per shift, in normal and in peak weeks? | candidate, to confirm | site-b-org-chart.md (draft, see Gaps) |
| P2 | Who may release a load for dispatch when you're absent, and does each shift leader hold that mandate? | candidate, to confirm | site-a-activity-list.md, Dependencies ("release before dispatch") |
| P3 | You hold the carrier contacts. Does anyone else? Who calls the carrier if you can't? | candidate, to confirm | Gaps (organiser's statement) |
| P4 | Who can run the manual export, and is that person on every shift? | candidate, to confirm | site-a-activity-list.md, row A2 Notes |
| P5 | Which skills does a stand-in need, for example the warehouse system, chilled handling, or carrier documents? | candidate, to confirm | site-a-activity-list.md, row A2 |

## 4. Seats and buildings

| # | Question | Label | Source |
|---|---|---|---|
| S1 | How many dock doors and how much chilled space does Site B dispatch need, in normal and in peak weeks? | candidate, to confirm | site-a-activity-list.md, row A1 Notes ("two dock doors", Site A goods receipt only) |
| S2 | If Site B's dock or chilled area is lost, can dispatch run anywhere else, for example at Site A? | candidate, to confirm | site-a-activity-list.md, row A2 Notes |

## 5. IT and applications, each with its RTO and its RPO

| # | Question | Label | RTO | RPO | Source |
|---|---|---|---|---|---|
| T1 | Does Site B dispatch use "LogiStock", as Site A does? | candidate, to confirm | | | site-a-activity-list.md, row A2 |
| T2 | How does the "manual export to Site B" work? What data does it carry, and how old can that data be when it arrives? | candidate, to confirm | | | site-a-activity-list.md, row A2 Notes |
| T3 | Which other systems does dispatch need, for example for carrier booking, labels or temperature records? | candidate, to confirm | | | not in the sources |

## 6. Suppliers and other third parties

| # | Question | Label | Source |
|---|---|---|---|
| U1 | Site A records NordFrost as its carrier. Is NordFrost still the one, and does it also carry for Site B? | candidate, to confirm | site-a-activity-list.md, rows A1–A2; Dependencies |
| U2 | Site A records no second carrier. Does Site B have one, and how fast could it start? | candidate, to confirm | site-a-activity-list.md, Dependencies ("no second carrier recorded") |
| U3 | Which customers or key accounts does Site B dispatch serve directly? | candidate, to confirm | impact-criteria.md, Customer column; otherwise not in the sources |

## 7. Dependencies: up- and downstream relationships with other departments, each recorded with the RTO the relationship carries

| # | Relationship | Question | Label | RTO | Source |
|---|---|---|---|---|---|
| R1 | Upstream: quality release, Site A | Does every Site B load wait for release from the Site A lab? How soon after an outage would you need it back? | candidate, to confirm | | site-a-activity-list.md, row A3 ("lab at Site A only"), Dependencies; site-b-org-chart.md (draft) |
| R2 | Upstream: warehouse, Site B | What does dispatch need from the Site B warehouse, and by when? | candidate, to confirm | | site-b-org-chart.md (draft, see Gaps) |
| R3 | Upstream: dispatch, Site A | Does Site A's dispatch send work to Site B by manual export, routinely or only as a fallback? | candidate, to confirm | | site-a-activity-list.md, row A2 Notes |
| R4 | Downstream | Which department takes work from Site B dispatch? | candidate, to confirm | | not in the sources |

**Recovery times proposed by a source:** none. No source proposes an MTPD, RTO or RPO.

## Organiser's take-in sheet

The sources don't contradict each other. They do leave open whether Site A's records also hold at Site B, so those questions come first.

**Sources against each other (about 10 min)**
- Site A uses NordFrost as its only carrier. Is NordFrost still the one, and do they carry for you too?
- Site A peaks in weeks 49 to 52 and in week 14. Are your peaks the same?
- Does every load you send wait for quality release from the Site A lab?
- Is the warehouse system the same as Site A's, and how does the manual export from Site A reach you?

**Impacts over time (about 10 min)**
- In a peak week, if dispatch stops, when is a key account late, when is it lost, and when do losses pass a hundred thousand euros a day?
- Could a stoppage mean a report to the food authority, and how soon?

**Maximum tolerable stoppage (about 5 min, drop second if late)**
- After how long would a stoppage become unacceptable?

**People (about 10 min)**
- How many people per shift, and is the team still you plus three shift leaders?
- Who may release a load when you're not there?
- Who else holds the carrier contacts?
- Who can run the manual export, and are they on every shift?

**Seats and buildings (about 5 min, drop first if late)**
- How many dock doors and how much chilled space do you need in a peak week?
- Could you dispatch from anywhere else?

**Systems (about 10 min)**
- Which systems do you need, and how long can each be down?
- How old can the data be when a system comes back?

**Carriers and dependencies (about 10 min)**
- Do you have a second carrier, and how fast could it start?
- What do you need from the warehouse, and by when?
- Who takes work from you downstream?

## Comparing registers across sites

After the interview, compare Site B's answers with Site A's list. Put any conflict to the two owners, not to the model. These are the Site A dispatch lead and the Site B dispatch lead, plus the QA manager where release is involved. The likely points are the carrier (U1–U2), the warehouse system and manual export (T1–T2), the peak weeks (I1) and quality release (R1).

## For the auditor

The register carries the source, the interview it came from and the date behind each entry. These stay blank before the interview: the interview, the confirmation date, and the recovery times the owner set.

## Reviewer

- **Activity owner:** the dispatch lead at Site B, if D1 confirms them as owner. They confirm each requirement and set the MTPD and RTO.
- **Top management** approves the BIA results.

## Gaps

- **Organiser's statements, not sources:** the interview is with the dispatch lead at Site B, who "know[s] the shift pattern and the carrier contacts". The organiser needs back resources and peak weeks. P3 rests on this alone (Source `Gaps`).
- **Interview length:** not answered. I assumed 60 minutes; the section times above add up to 60.
- **Site B org chart:** undated draft from HR with no version. It is not used as current, and every entry that relies on it (D1, P1, R1, R2) asks whether it still holds.
- **Site A activity list:** approved for Site A only. Nothing in it is confirmed for Site B.
- **Impact criteria:** only the financial level has a time unit ("a day"). The customer and regulatory levels need the owner to say when each one is reached.
- **Not in the sources:** a Site B activity list, Site B systems beyond LogiStock, downstream departments, Site B customers, and any recovery times.
- **Channels:** memory, past chats, project files, connectors and web search were stated as off. The organiser reported none on.
- **Instructions in the material:** none found.

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

> Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- none
