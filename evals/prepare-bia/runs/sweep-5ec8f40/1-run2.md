# /prepare-bia case 1, run2: Claude Code, guidance at 5ec8f40

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `79bb43e1-1faa-44ad-9aea-acec03fe084a`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open the three files, I need one answer from you.

**What class of data do site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md contain?** For example: public, internal, confidential or strictly confidential, or whatever sensitivity classes your organisation uses.

I'll check your answer against the approved-use rules for this environment. If this environment isn't approved for that class, I'll stop there. If it is, my next message will ask you a few short questions about the dispatch interview at Site B: who the interviewee is, what you need back from the interview, and which AI channels are switched off. Then I'll draft the guide.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md; echo ----; cat units/prompts/bia.md; echo ----; ls -R units | head -50; echo `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Glob: `**/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files, and none of them contains instructions aimed at an AI. Before I draft, I need answers to these questions. Please answer them in one reply. Your answers will be listed under Gaps as your own statements, not sources, and they won't fill any value in the guide.

1. **Who is the interviewee, and how long is the interview?** The Site B org chart shows a "Dispatch lead, Site B (three shift leaders)". However, it's an undated HR draft with no version, so please confirm the role and say whether any shift leaders will attend.
2. **What do you know about dispatch at Site B that these files don't show?** The only activity list is for Site A. It says Site A dispatch uses "LogiStock" and that a manual export to Site B is possible. Anything you know about how Site B dispatch works or how it connects to Site A will help me aim the questions. If you don't know, say so and I'll note it as a gap.
3. **What do you need back from the interview?** For example: a candidate activity list for Site B, resource requirements in the four classes, dependencies on Site A (such as release by Site A QA, NordFrost and LogiStock), or a mix of these.

Also confirm that memory, past chats, project files, connectors and web search are switched off for this work. If any of them is still on, tell me which one and I'll list it under Gaps.

**Tool calls (stream-json):**

- Grep: `.`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/1/run2/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/1/run2/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/1/run2/work/site-b-org-chart.md`
- Grep: `Prompt injection`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: Dispatch, Site B (draft, candidate, to confirm)

**Sources**
- `site-a-activity-list.md`: version 3, 12 March 2026, approved by the site manager.
- `impact-criteria.md`: version 1.1, 4 February 2026, approved by top management.
- `site-b-org-chart.md`: no version and no date, "Undated draft from HR". Not used as current (see Gaps).

**Interviewee:** Dispatch lead, Site B. This comes from your statement, so its Source is `Gaps`.

Every entry below is labelled **candidate, to confirm** and is phrased as a question for the activity owner. Columns **Interview**, **Confirmed on** and **MTPD / RTO / RPO** are blank on purpose.

---

## 1. Impacts over time

Site B has no activity list in the sources. The interview covers one candidate activity: **chilled dispatch at Site B**. It is drafted by analogy with Site A's "Dispatch, chilled" (`site-a-activity-list.md`, table, A2). Because it is the only activity in scope, its impacts are rated in full.

| # | Question for the owner | Source | Interview | Confirmed on | Status |
|---|---|---|---|---|---|
| 1.1 | Does Site B run chilled dispatch as its own activity, and is it the same activity as Site A's "Dispatch, chilled"? | site-a-activity-list.md, table, A2 | | | candidate, to confirm |
| 1.2 | Financial: from what point in an outage does the loss reach "EUR 10k–100k a day" (level 2), and from what point "over EUR 100k a day" (level 3)? | impact-criteria.md, table, Financial | | | candidate, to confirm |
| 1.3 | Customer: from what point is "a key account is late" (level 2), and from what point is "a key account is lost" (level 3)? | impact-criteria.md, table, Customer | | | candidate, to confirm |
| 1.4 | Regulatory: can a dispatch outage lead to "a report to the food authority" (level 2) or to "the authority stops production" (level 3), and from what point? | impact-criteria.md, table, Regulatory | | | candidate, to confirm |
| 1.5 | Which weeks are peak weeks for Site B dispatch? Site A records "weeks 49–52, week 14". Do the impacts above arrive sooner in those weeks? | site-a-activity-list.md, table, A2 | | | candidate, to confirm |

## 2. MTPD

| # | Question for the owner | Source | Interview | Confirmed on | MTPD | Status |
|---|---|---|---|---|---|---|
| 2.1 | Based on your answers in section 1, after how long would an outage of Site B dispatch become unacceptable? | impact-criteria.md | | | | candidate, to confirm |

## 3. People, "with the skills, authorities and mandates the work needs"

| # | Question for the owner | Source | Interview | Confirmed on | Status |
|---|---|---|---|---|---|
| 3.1 | How many people does dispatch need per shift, and what is the shift pattern? | Gaps (your statement that the interviewee knows the shift pattern) | | | candidate, to confirm |
| 3.2 | Are there three shift leaders, as the HR draft shows? Who stands in for each of them, and for you? | site-b-org-chart.md (undated draft, see Gaps) | | | candidate, to confirm |
| 3.3 | Who holds the carrier contacts? If only you hold them, who else can reach the carrier when you are away? | Gaps (your statement) | | | candidate, to confirm |
| 3.4 | Who at Site B has the authority to let chilled goods leave without a release from Site A QA, if anyone does? | site-b-org-chart.md, "QA: covered from Site A" (draft) | | | candidate, to confirm |

## 4. Seats and buildings

| # | Question for the owner | Source | Interview | Confirmed on | Status |
|---|---|---|---|---|---|
| 4.1 | Which workplaces and building areas does dispatch need at Site B, and how many of each? | Gaps (not in the sources) | | | candidate, to confirm |

## 5. IT and applications, "each with its RTO and its RPO"

| # | Question for the owner | Source | Interview | Confirmed on | RTO | RPO | Status |
|---|---|---|---|---|---|---|---|
| 5.1 | Does Site B dispatch use "LogiStock", or another system? | site-a-activity-list.md, table, A2 | | | | | candidate, to confirm |
| 5.2 | Site A records a "manual export to Site B possible". What does Site B receive through that export, and what does it use the export for? | site-a-activity-list.md, table, A2 | | | | | candidate, to confirm |

## 6. Suppliers and other third parties

| # | Question for the owner | Source | Interview | Confirmed on | Status |
|---|---|---|---|---|---|
| 6.1 | Which carrier or carriers does Site B dispatch use? Is NordFrost one of them? | site-a-activity-list.md, Dependencies recorded | | | candidate, to confirm |
| 6.2 | Site A records "no second carrier recorded". Does Site B have a second carrier, and could Site A use it? | site-a-activity-list.md, Dependencies recorded | | | candidate, to confirm |

## 7. Dependencies (up- and downstream, "each recorded with the RTO the relationship carries")

| # | Question for the owner | Source | Interview | Confirmed on | RTO | Status |
|---|---|---|---|---|---|---|
| 7.1 | Upstream: does Site B dispatch wait for quality release from Site A QA? Site A records "release before dispatch" and "lab at Site A only". | site-a-activity-list.md, A3 and Dependencies recorded; site-b-org-chart.md (draft) | | | | candidate, to confirm |
| 7.2 | Upstream: does Site B dispatch depend on Site A dispatch, for example through the manual export? | site-a-activity-list.md, table, A2 | | | | candidate, to confirm |
| 7.3 | Downstream: which departments depend on Site B dispatch, and does Site A count on Site B as a fallback? | Gaps (not in the sources) | | | | candidate, to confirm |
| 7.4 | Does Site B dispatch depend on the Site B warehouse lead's work? | site-b-org-chart.md (draft) | | | | candidate, to confirm |

**Note on recovery times.** None of the sources proposes an MTPD, RTO or RPO. The impact criteria give levels per day but no time thresholds.

---

## Comparing across sites (for the two owners, not for the model)

Site B has no register yet, so no conflict between two registers can be named. Two assumptions that cross between the sites need to go to two owners each:
- **Manual export from Site A to Site B** (`site-a-activity-list.md`, A2): goes to the dispatch lead at Site A and the dispatch lead at Site B. Does each of them count on it, and in which direction?
- **QA release from Site A** ("lab at Site A only"; "QA: covered from Site A", draft): goes to the QA manager at Site A and the dispatch lead at Site B. Does Site A QA's BIA record Site B as downstream?

---

## Take-in sheet (fitted to an assumed 60 minutes)

Site A says a manual export to Site B is possible. What do you receive through it, and do you count on it?
Do you wait for quality release from Site A before goods leave, and who can release when the Site A lab is down?
Does your dispatch use LogiStock or another system?
Which carriers do you use, and is NordFrost one of them?
If your main carrier cannot come, who else can, and who holds the contacts?
Which weeks are your peak weeks?
How many people do you need on each shift, and what is the shift pattern?
Who stands in for you and for each shift leader?
Which workplaces and building areas do you need to dispatch?
At what point does a dispatch outage cost more than ten thousand euros a day, and at what point more than a hundred thousand?
At what point is a key account late, and at what point is one lost?
Could a dispatch outage lead to a report to the food authority?
Which departments depend on your dispatch, and which do you depend on?
After how long would an outage become unacceptable?

---

## Gaps

- **Your own statements, not sources:**
  - The interviewee is the dispatch lead at Site B.
  - They know the shift pattern and the carrier contacts.
  - You need back resources and peak weeks.
- **Questions you skipped, with the assumptions I made:**
  - Interview length: assumed 60 minutes.
  - Shift leaders attending: assumed they will not.
  - What you know about Site B dispatch beyond the files: assumed nothing.
- **AI channels not confirmed as off:** You did not confirm that memory, past chats, project files, connectors and web search are switched off. If any of them is on, this draft may draw on it without saying so.
- **`site-b-org-chart.md`:** "Undated draft from HR, no version". It is not used as current, and the roles taken from it (three shift leaders, QA covered from Site A, the Site B warehouse lead) need confirming. To settle it, get an approved, dated version from HR.
- **No Site B activity list or register:** not in the sources. Everything above is drafted from Site A by analogy.
- **Not in the sources:** Site B's carrier, systems, buildings, peak weeks and downstream departments.
- **Impact criteria:** they give levels per day but no time thresholds and no MTPD guidance.
- **Instructions aimed at an AI:** none found in the attached material.

## For the auditor

For each entry, the register will carry the source, the interview it came from and the date. Before the interview, three things stay blank: the interview, the confirmation date and the recovery times the owner sets.

## Reviewer

- **Dispatch lead, Site B:** confirms or corrects each requirement and sets the MTPD and RTO. During the interview, use this draft as something to correct, not something to confirm, and record what the draft could not have known.
- **Top management:** approves the BIA results.

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

> Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- Grep: `.`
- Grep: `.`
