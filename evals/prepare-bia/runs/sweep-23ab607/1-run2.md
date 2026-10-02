# /prepare-bia case 1, run2: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `2ef3d87f-086b-4018-a771-9bbf5454f98b`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files: what class of data do they hold (for example public, internal, confidential or strictly confidential)?

I'll go by your answer, not by any marking inside the files, and I'll check that this environment is approved for that class before I read them.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && ls -R | head -50 && cat preflight.md; echo ----; ls -la /tmp/claude-1001/-opt-brain/8e671d9c-30`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Glob: `**/*`
- Glob: `**/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The class is high and you've confirmed this environment is approved for it, so I've read the three files. Before I draft, I have three questions. Your answers will go under Gaps as your own statements, not sources, and won't fill any value in the guide:

1. **Who is the interviewee, and what do they know that you don't?** Is it the Dispatch lead at Site B, one of the three shift leaders, or someone else?
2. **What do you need back from this interview?** For example: confirmed dispatch resources only, the Site A–B dependencies (including the manual export from LogiStock), the impact ratings, or all of these.
3. **Are memory, past chats, project files, connectors and web search all switched off for this work?** If any is on, tell me which and it will go under Gaps.

These are the sources I'll use:
- `site-a-activity-list.md`: version 3, 12 March 2026, approved
- `impact-criteria.md`: version 1.1, 4 February 2026, approved by top management
- `site-b-org-chart.md`: undated draft with no version. It goes under Gaps and won't be treated as current.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/1/run2/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/1/run2/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/1/run2/work/site-b-org-chart.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide (draft): Dispatch, Site B

**Sources**
- `site-a-activity-list.md`: version 3, 12 March 2026, approved by the site manager (owner: BCM manager, Site A)
- `impact-criteria.md`: version 1.1, 4 February 2026, approved by top management
- `site-b-org-chart.md`: no version and no date, a draft from HR. It is listed under Gaps and not used as current.

**Interviewee:** Dispatch lead, Site B (organiser's statement, see Gaps)
**Activity owner who confirms each entry:** Dispatch lead, Site B
**Candidate activity:** Dispatch, chilled, Site B. This is modelled on Site A's activity A2. It is "candidate, to confirm".

Every entry below is a question for the activity owner, labelled "candidate, to confirm". The MTPD, RTO and RPO fields are left empty on purpose.

---

## 1. Impacts over time

This is the only activity in scope, so it gets the full rating. The Site A list doesn't rank activities. Use the approved impact criteria and let the owner pick the time points.

| # | Question for the owner | Source | Status |
|---|---|---|---|
| 1.1 | If chilled dispatch at Site B stops, how long until the financial impact reaches level 2 ("EUR 10k–100k a day")? How long until level 3 ("over EUR 100k a day")? | impact-criteria.md, table | candidate, to confirm |
| 1.2 | How long until "a key account is late"? How long until "a key account is lost"? | impact-criteria.md, table | candidate, to confirm |
| 1.3 | Does a stop in dispatch ever lead to "a report to the food authority", or to "the authority stops production"? After how long? | impact-criteria.md, table | candidate, to confirm |
| 1.4 | Site A peaks in weeks 49–52 and week 14. Which weeks are Site B's peaks? Do the answers to 1.1–1.3 change in those weeks? | site-a-activity-list.md, A2 | candidate, to confirm |

## 2. MTPD

| # | Question for the owner | Source | Status | MTPD |
|---|---|---|---|---|
| 2.1 | From your answers in section 1, after how long would a stop in dispatch become unacceptable? Is that the same in the peak weeks? | impact-criteria.md | candidate, to confirm | |

## 3. People, "with the skills, authorities and mandates the work needs"

| # | Question for the owner | Source | Status |
|---|---|---|---|
| 3.1 | The HR draft shows three shift leaders under you. Is that still correct? What shift pattern do they work? | site-b-org-chart.md (undated draft); Gaps | candidate, to confirm |
| 3.2 | What is the minimum number of people per shift for chilled dispatch, normally and in the peak weeks? | not in the sources | candidate, to confirm |
| 3.3 | Who may release a load for dispatch when you are absent? Does a shift leader hold that mandate? | not in the sources | candidate, to confirm |
| 3.4 | At Site A, quality release must happen before dispatch. Who at Site B can confirm that a load has been released, and with what authority? | site-a-activity-list.md, dependencies | candidate, to confirm |
| 3.5 | Is any task held by one person only? For example: carrier booking, LogiStock entries, or the manual export. | site-a-activity-list.md, A2; Gaps | candidate, to confirm |

## 4. Seats and buildings

| # | Question for the owner | Source | Status |
|---|---|---|---|
| 4.1 | Site A records two dock doors for chilled goods receipt. How many dock doors, and which chilled areas, does dispatch at Site B need, at a minimum and in the peak weeks? | site-a-activity-list.md, A1 | candidate, to confirm |
| 4.2 | Which desks or workplaces do the shift leaders and you need to plan and book dispatch? | not in the sources | candidate, to confirm |
| 4.3 | Could dispatch at Site B be run from another site? Could Site A's dispatch be run from Site B? | site-a-activity-list.md, A2 ("manual export to Site B possible") | candidate, to confirm |

## 5. IT and applications, "each with its RTO and its RPO"

| # | Question for the owner | Source | Status | RTO | RPO |
|---|---|---|---|---|---|
| 5.1 | Site A dispatch uses the warehouse system "LogiStock". Does Site B dispatch use LogiStock too, or another system? | site-a-activity-list.md, A2 | candidate, to confirm | | |
| 5.2 | Site A records "manual export to Site B possible". What gets exported, by whom, and do you receive and use it at Site B? | site-a-activity-list.md, A2 | candidate, to confirm | | |
| 5.3 | Without the system, can you dispatch on paper? For how long, and in which weeks? | not in the sources | candidate, to confirm | | |
| 5.4 | Which other applications or devices does dispatch need? For example: carrier booking, labels, temperature records. | not in the sources | candidate, to confirm | | |

## 6. Suppliers and other third parties

| # | Question for the owner | Source | Status |
|---|---|---|---|
| 6.1 | Site A dispatch depends on the carrier NordFrost, and no second carrier is recorded. Which carrier or carriers does Site B use? Is NordFrost still the one? | site-a-activity-list.md, A1/A2, dependencies | candidate, to confirm |
| 6.2 | Which carrier contacts do you hold? Is there a second carrier who could take chilled loads, and how quickly? | Gaps (organiser's statement) | candidate, to confirm |
| 6.3 | Which other third parties does dispatch need? For example: packaging, cooling service, pallet supply. | not in the sources | candidate, to confirm |

## 7. Dependencies: "up- and downstream relationships with other departments, each recorded with the RTO the relationship carries"

| # | Question for the owner | Direction | Source | Status | RTO |
|---|---|---|---|---|---|
| 7.1 | The HR draft shows QA for Site B as "covered from Site A", and Site A records "lab at Site A only". Does every Site B load wait for a release from Site A QA? How long can you wait? | upstream | site-b-org-chart.md (draft); site-a-activity-list.md, A3 | candidate, to confirm | |
| 7.2 | What do you need from the Site B warehouse (warehouse lead) before you can dispatch? | upstream | site-b-org-chart.md (draft) | candidate, to confirm | |
| 7.3 | Does Site A dispatch rely on Site B, through the manual export, as a fallback? Does Site B rely on Site A? | up- or downstream | site-a-activity-list.md, A2 | candidate, to confirm | |
| 7.4 | Which departments rely on Site B dispatch? For example: sales, customer service for key accounts. | downstream | not in the sources | candidate, to confirm | |

**Recovery times in the sources:** no source proposes an MTPD, RTO or RPO.

---

## Cross-site points, for the two owners

These go to the Dispatch lead at Site A and the Dispatch lead at Site B together, not to the model:
- whether dispatch at both sites relies on NordFrost as the only carrier
- what the "manual export to Site B" means in practice, and who relies on whom
- whether Site B dispatch is bound to Site A QA release and the Site A lab

I found no direct contradiction between the attached sources. These are points where they touch and only the two owners can settle them.

---

## Organiser's take-in sheet

**Points between the sites (about 10 min)**
Does Site B also use NordFrost, and is NordFrost still the one?
Is there a second carrier you could call for chilled loads?
What does the manual export from Site A's system mean for you, and do you use it?
Does every load here wait for a release from Site A's quality team?

**Impacts over time (about 10 min)**
If dispatch stops, how long before it costs between ten and a hundred thousand euros a day, and how long before more?
How long before a key account is late, and how long before one is lost?
Could a stop in dispatch ever involve the food authority?
Which weeks are your peak weeks, and is it worse then?

**Maximum tolerable stop (about 5 min)**
After how long would a stop become unacceptable, and is that shorter in the peak weeks?

**People (about 10 min)**
Are there still three shift leaders, and what shift pattern do they work?
How many people per shift do you need at a minimum, normally and in the peak weeks?
Who may release a load when you are not there?
Is any task held by only one person? *(drop first if late)*

**Seats and buildings (about 5 min)**
How many dock doors and which chilled areas do you need at a minimum?
Could dispatch run from another site? *(drop first if late)*
Which desks or workplaces do you need for planning? *(drop first if late)*

**IT and applications (about 10 min)**
Which system do you dispatch from?
Can you dispatch on paper, and for how long?
What else do you need, such as labels, booking or temperature records? *(drop first if late)*

**Suppliers (about 5 min)**
Which carrier contacts do you hold, and how fast can a second carrier take over?
Who else do you need, such as packaging or cooling service? *(drop first if late)*

**Dependencies (about 5 min)**
What do you need from the warehouse before you can dispatch?
Who relies on dispatch here, inside the company? *(drop first if late)*

**Before you close:** what does this guide miss that only you know?

---

## Interview

Tell the owner to "use the draft as the thing to correct, not the thing to confirm; record what it could not have known".

## Gaps

- **Organiser's statements, not sources:**
  - The interviewee is the Dispatch lead, Site B.
  - They know the shift pattern and the carrier contacts.
  - What you need back is resources and peak weeks.

  These shaped the scope only. Entries that rest on them alone (3.1 shift pattern, 6.2 carrier contacts) have Source `Gaps`.
- **Channels (question 3, not answered):** it's not confirmed that memory, past chats, project files, connectors and web search are off. The assumption is that one or more may have been on. I used only the three attached files and the skill's own sources, but a reader can't tell that from the output alone. Settle it by confirming the settings before relying on the draft.
- **`site-b-org-chart.md`:** undated draft, no version, from HR. The three shift leaders, the warehouse lead and "QA: covered from Site A" are used only as questions, not as current facts. Settle it with an approved, dated Site B structure, or the owner's answer to 3.1 and 7.1.
- **Site B activities:** no Site B activity list is attached. "Dispatch, chilled, Site B" is modelled on Site A's activity A2. Site A's A4 (payroll, head office) is outside this interview.
- **Not in the sources:** Site B peak weeks, staffing minimums, dock doors, systems, carriers, and downstream departments.
- **Instructions to an AI found in the material:** none found.

## For the auditor

The register carries "the source, the interview it came from and the date behind each entry". Before the interview these fields stay blank:
- the interview: ______
- the confirmation date: ______
- "the recovery times the owner set": ______

## Reviewer

- The activity owner, Dispatch lead, Site B, confirms each requirement and sets the MTPD and RTO.
- "Top management approves the BIA results."

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

> Parts of this document were drafted with AI support (prepare-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- none
