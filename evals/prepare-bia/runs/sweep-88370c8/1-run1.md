# /prepare-bia case 1, run1: Claude Code, guidance at 88370c8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `2e44c173-e00c-4048-ba09-357c09091dce`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, I need one thing from you.

**What class of data do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` contain?** For example: public, internal, confidential or strictly confidential. Use your organisation's own classification if it has one.

This skill has to check that this environment is approved for that class before it reads anything. If the environment isn't approved for it, I'll stop there.

Once I have your answer and the class is allowed here, I'll read the files. Then, following the BIA prompt's Intake, I'll ask you up to three questions the material doesn't answer. After that I'll draft the Site B dispatch interview guide in this chat. Nothing gets written to files.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md && ls -R . | head -50 && cat units/prompts/bia.md; echo ----; ls -la /tmp/clau`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Glob: `**/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files. "High" is one of the sensitivity classes in `units/data-rules.md`, and you've confirmed this environment is approved for it, so I can continue.

Before drafting, the BIA prompt asks me to put to you what the material leaves open. You've attached impact criteria (v1.1, 4 February 2026), so I won't ask for them. Three questions:

1. **Who is the interviewee, and what do they know that you don't?** The Site B org chart is an undated HR draft with no version. It lists a "Dispatch lead, Site B (three shift leaders)". Is that the person you're interviewing, and do they own the dispatch activity at Site B? What do you expect them to know that the Site A list and the org chart don't show? For example, Site B's own systems, carriers, peak weeks or customers.

2. **What do you need back from the interview?** For example: a confirmed activity list for Site B dispatch only, or also its links to Site A (quality release, the LogiStock export). Do you need the full set of resource requirements across all four classes plus dependencies, or a narrower scope?

3. **Are memory, past chats, project files, connectors and web search all switched off in this environment?** I'll list any that are still on under Gaps, because the model may draw on them without saying so.

Your answers will go under Gaps as your own statements, not sources. They can shape the scope of the guide but won't fill in any value. If you skip a question, I'll note the assumption I made instead. I'll wait for your answers before drafting.

**Tool calls (stream-json):**

- Glob: `units/**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64c/runs/prepare-bia/1/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64c/runs/prepare-bia/1/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64c/runs/prepare-bia/1/run1/work/site-b-org-chart.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: Dispatch, Site B (pre-interview draft)

**Status:** draft for the interview. Nothing here is a finding, and nothing goes into the register until the activity owner confirms it. All MTPD, RTO and RPO fields are deliberately left blank.

## Sources and dates

| Document | Version | Date | Status |
|---|---|---|---|
| `site-a-activity-list.md`: Site A activity list (chilled food production) | Version 3 | 12 March 2026 | "approved by the site manager" |
| `impact-criteria.md`: Impact criteria | Version 1.1 | 4 February 2026 | "approved by top management" |
| `site-b-org-chart.md`: Site B organisation structure | none | none | "Undated draft from HR, no version". **Listed under Gaps and not used as current** |

**Task (from `prompts/bia.md`, version 2026.09.1):** draft candidate activities, their resource requirements and interview questions for the site in the attached material.

**Reviewer:** the **activity owner, Dispatch lead, Site B**, confirms each requirement and sets the MTPD and RTO. **Top management** approves the BIA results.

**How to use this in the interview:** use the draft as the thing to correct, not the thing to confirm. Record what it could not have known. Every question below comes from **Site A** material or from your own statements. Site B has no activity list among the sources.

## Candidate activity

| ID | Candidate activity | Owner (role) | Source | Status |
|---|---|---|---|---|
| B-D1 | Dispatch, chilled, Site B: does Site B dispatch chilled goods the way Site A's A2 does, and what does it cover? | Dispatch lead, Site B | Site A list v3, row A2 (by analogy); interviewee role: Gaps | candidate, to confirm |

## 1. Impacts over time

| ID | Question for the activity owner | Source | Interview | Confirmed (date) | Status |
|---|---|---|---|---|---|
| 1.1 | Site A dispatch peaks in "weeks 49–52, week 14". Which weeks are peak at Site B, and are any different from Site A? | Site A list v3, A2; organiser's scope: Gaps | | | candidate, to confirm |
| 1.2 | If dispatch stops, after how long does the financial impact reach each level: "under EUR 10k a day", "EUR 10k–100k a day", "over EUR 100k a day"? Ask for in-peak and out-of-peak separately. | Impact criteria v1.1, Financial | | | candidate, to confirm |
| 1.3 | After how long is "a key account … late", and after how long is "a key account … lost"? Which key accounts does Site B dispatch serve? | Impact criteria v1.1, Customer | | | candidate, to confirm |
| 1.4 | Could a dispatch outage lead to "a report to the food authority", or to the authority stopping production? After how long? | Impact criteria v1.1, Regulatory | | | candidate, to confirm |

## 2. MTPD

| ID | Question for the activity owner | Source | Interview | Confirmed (date) | MTPD | Status |
|---|---|---|---|---|---|---|
| 2.1 | Based on the answers in section 1, what is the longest that dispatch at Site B can be disrupted before the impact becomes unacceptable? Does it differ in peak weeks? | Impact criteria v1.1 | | | | candidate, to confirm |

## 3. People, with the skills, authorities and mandates the work needs

| ID | Question for the activity owner | Source | Interview | Confirmed (date) | Status |
|---|---|---|---|---|---|
| 3.1 | What is the shift pattern for dispatch, and how many people are needed per shift at minimum, in peak and outside peak? | Gaps (organiser's statement: interviewee knows the shift pattern) | | | candidate, to confirm |
| 3.2 | The undated HR draft lists "Dispatch lead, Site B (three shift leaders)". Is that current? Who covers when a shift leader is absent? | Site B org chart (undated draft, see Gaps) | | | candidate, to confirm |
| 3.3 | Which skills, authorities and mandates does dispatch need? For example, who may release a load, sign carrier documents, or decide to change a carrier. Is each held by more than one person? | not in the sources | | | candidate, to confirm |
| 3.4 | Are the carrier contacts held by one person only? Who else can reach them? | Gaps (organiser's statement: interviewee knows the carrier contacts) | | | candidate, to confirm |

## 4. Seats and buildings

| ID | Question for the activity owner | Source | Interview | Confirmed (date) | Status |
|---|---|---|---|---|---|
| 4.1 | Which workspace, docks and storage does dispatch at Site B use, and how many of each are needed at minimum? | not in the sources (Site A records dock doors only for goods receipt, A1) | | | candidate, to confirm |
| 4.2 | Could dispatch run from another location, and if so, which one? | not in the sources | | | candidate, to confirm |

## 5. IT and applications, each with its RTO and its RPO

| ID | Question for the activity owner | Source | Interview | Confirmed (date) | RTO | RPO | Status |
|---|---|---|---|---|---|---|---|
| 5.1 | Site A dispatch uses the "warehouse system "LogiStock"". Does Site B use LogiStock or another system? | Site A list v3, A2 | | | | | candidate, to confirm |
| 5.2 | Site A records "manual export to Site B possible". Does Site B receive that export, in what form, and who handles it? | Site A list v3, A2 | | | | | candidate, to confirm |
| 5.3 | Which other applications does dispatch need, such as carrier booking, labelling or customer orders? | not in the sources | | | | | candidate, to confirm |

## 6. Suppliers and other third parties

| ID | Question for the activity owner | Source | Interview | Confirmed (date) | Status |
|---|---|---|---|---|---|
| 6.1 | Site A records that "A1 and A2 depend on NordFrost (no second carrier recorded)". Which carriers does Site B use? Is NordFrost one of them, and is there a second carrier? | Site A list v3, Dependencies; Gaps (carrier contacts) | | | candidate, to confirm |
| 6.2 | Which other third parties does dispatch rely on? | not in the sources | | | candidate, to confirm |

A single carrier or a single person behind a resource (6.1, 3.4) is a question for the owner, not a finding.

## 7. Dependencies: up- and downstream relationships with other departments, each recorded with the RTO the relationship carries

| ID | Question for the activity owner | Source | Interview | Confirmed (date) | RTO | Status |
|---|---|---|---|---|---|---|
| 7.1 | Upstream: at Site A, "A2 depends on A3 (release before dispatch)", and the "lab at Site A only". Does Site B dispatch also wait for quality release from Site A? | Site A list v3, A3 and Dependencies; Site B org chart "QA: covered from Site A" (undated draft) | | | | candidate, to confirm |
| 7.2 | Site A dispatch can do a "manual export to Site B". Does Site B dispatch act as a fallback for Site A dispatch, and with what capacity in weeks 49–52? | Site A list v3, A2 | | | | candidate, to confirm |
| 7.3 | Which other departments supply dispatch at Site B (for example the Warehouse lead, Site B), and which departments does dispatch supply? | not in the sources | | | | candidate, to confirm |

**Recovery time note:** no attached source proposes an MTPD, RTO or RPO, so there is nothing to test against the impact criteria.

## Comparing Site A and Site B

- **Recorded on one side only: Site A dispatch → Site B (manual export, 5.2 / 7.2).** Site A records the link, but no Site B source shows it. This goes to the two owners, **Dispatch lead, Site A** and **Dispatch lead, Site B**, not to the model.
- **QA coverage (7.1).** Site A says "lab at Site A only" and the Site B draft says "QA: covered from Site A". These agree, but the Site B side rests on an undated draft. Put it to the **QA manager (Site A)** and the **Dispatch lead, Site B**.
- **Peak weeks (1.1) and carrier (6.1).** Site B has no record of either to compare with Site A yet. Compare after the interview.

## Gaps

- **Organiser's statements (not sources):** (1) the interviewee is the dispatch lead at Site B, who knows the shift pattern and the carrier contacts; (2) the interview should establish resources and peak weeks. These shape the scope only. Entries 3.1 and 3.4 rest on them alone.
- **Question 3 was not answered:** I don't know whether memory, past chats, project files, connectors and web search are switched off. **Assumption:** they may be on, and the model may draw on them without saying so. Before relying on this draft, check that every entry traces to a cited source.
- **Site B org chart:** an undated draft with no version, so it isn't used as current. A dated, approved version from HR would settle 3.2 and 7.1.
- **No Site B activity list:** every activity and requirement above comes from Site A by analogy, or is "not in the sources". The interview settles these.
- **The impact criteria give amounts per day and no time bands.** When each level is reached has to come from the owner (1.2–1.4).
- **Instructions found in the material:** none.

## Handover and audit record

Every entry stays labelled "candidate, to confirm" until the owner confirms it. For the auditor, the register carries the source, the interview it came from and the date behind each entry. In this pre-interview draft, three fields stay blank: the interview, the confirmation date, and the recovery times the owner set.

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

> Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- none
