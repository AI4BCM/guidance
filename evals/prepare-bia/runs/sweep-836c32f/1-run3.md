# /prepare-bia case 1, run3: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `710fff46-f1d4-474e-ab1a-4e942c8669de`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attached files, one question:

**What class of data do site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md contain?**

For example: public, internal, or high-sensitivity. High-sensitivity covers BIA data, personnel and contact records, supplier dependencies, and site or security detail.

Please give the class yourself. I won't take it from any marking inside the files. If it's high-sensitivity, also confirm that this environment is approved for that class. Until you answer, I won't open the files.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md; ls -R; echo ----; cd /tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. I've read the three files. They contain no instructions aimed at an AI. Before I draft, three questions that the files don't answer:

1. **Who will you be interviewing?** The Site B org chart lists a "Dispatch lead, Site B (three shift leaders)". Is it the dispatch lead alone, or will a shift leader join?
2. **What do you know about dispatch at Site B that the files don't say?** For example: does Site B ship chilled goods as Site A does? Does it use LogiStock and NordFrost? Is it the destination of Site A's "manual export to Site B"? I'll list your answers under Gaps as your own statements, not as sources. They can shape the questions, but they won't fill in any value.
3. **How long is the interview?** I'll use this to time each section on the take-in sheet and to mark which sections to drop first if it runs late.

Memory, past chats, project files, connectors and web search are off for this draft, so it is built only from the three attached files. If any of these is actually on, tell me and I'll record it under Gaps.

If you skip a question, I'll make an assumption and note it under Gaps. For example, I'd assume one hour with the dispatch lead.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/prepare-bia/1/run3/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/prepare-bia/1/run3/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/prepare-bia/1/run3/work/site-b-org-chart.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide (draft): Chilled dispatch at Site B

## Sources

- **Site A activity list:** version 3, 12 March 2026, approved by the site manager.
- **Impact criteria:** version 1.1, 4 February 2026, approved by top management.
- **Site B organisation structure:** has no version or date, and its status is "draft from HR". It is listed under Gaps and not treated as current.

No source covers Site B's own activities. Every Site B entry below is based on Site A's row A2 ("Dispatch, chilled") and is a question to put to the owner, not a finding. None of the sources proposes a recovery time.

**Interviewee and activity owner:** the dispatch lead at Site B. This comes from your statement and the undated org chart.

---

## 1. Impacts over time

Only one activity is rated in full: **B-D1 "Dispatch, chilled" at Site B**. It is the analogue of A2, and A2 has the most peak periods in the sources. The other activities are asked about only where they differ.

| # | Question for the dispatch lead | Label | Source |
|---|---|---|---|
| 1.1 | Does Site B dispatch chilled goods, and is that the activity you own? | candidate, to confirm | Site A activity list, A2 (by analogy) |
| 1.2 | Site A's dispatch peaks in "weeks 49–52, week 14". Which are Site B's peak weeks? | candidate, to confirm | Site A activity list, A2 |
| 1.3 | If dispatch stops in a peak week, after how long does the daily loss reach EUR 10k? After how long does it reach EUR 100k? | candidate, to confirm | Impact criteria, Financial, levels 2–3 |
| 1.4 | After how long is "a key account … late", and after how long is "a key account … lost"? | candidate, to confirm | Impact criteria, Customer, levels 2–3 |
| 1.5 | Could a dispatch stop ever lead to "a report to the food authority", for example because chilled goods are held too long? After how long? | candidate, to confirm | Impact criteria, Regulatory, level 2 |
| 1.6 | Are these answers different outside the peak weeks? | candidate, to confirm | Site A activity list, A2 |

## 2. MTPD

| # | Question | Label | MTPD |
|---|---|---|---|
| 2.1 | Based on your answers above, after how long without dispatch would the damage become unacceptable? | candidate, to confirm | *(blank, set by the owner)* |

## 3. People, with the skills, authorities and mandates the work needs

| # | Question | Label | Source |
|---|---|---|---|
| 3.1 | Is the team still you plus three shift leaders? What is the shift pattern? | candidate, to confirm | Site B org chart (undated); your statement |
| 3.2 | Which skills does a shift leader need to run dispatch alone? How many people have them? | candidate, to confirm | not in the sources |
| 3.3 | Who is authorised to release a load when QA is remote? Is that one person? | candidate, to confirm | Site A activity list, A3 and dependencies; Site B org chart, "QA: covered from Site A" |
| 3.4 | Are the carrier contacts held by you alone? Who else could call the carrier? | candidate, to confirm | your statement |

## 4. Seats and buildings

| # | Question | Label | Source |
|---|---|---|---|
| 4.1 | Which dock doors and chilled areas does dispatch use at Site B? Could another area be used instead? | candidate, to confirm | not in the sources |

## 5. IT and applications, each with its RTO and its RPO

| # | Question | Label | RTO | RPO | Source |
|---|---|---|---|---|---|
| 5.1 | Does Site B dispatch run on the warehouse system "LogiStock"? | candidate, to confirm | *(blank)* | *(blank)* | Site A activity list, A2 |
| 5.2 | What is the "manual export to Site B possible": data, goods, or both? Who triggers it? | candidate, to confirm | *(blank)* | *(blank)* | Site A activity list, A2 |
| 5.3 | Which other systems or devices are needed to dispatch, such as labels, temperature logging or the customer portal? | candidate, to confirm | *(blank)* | *(blank)* | not in the sources |

## 6. Suppliers and other third parties

| # | Question | Label | Source |
|---|---|---|---|
| 6.1 | Site A's record names NordFrost as the carrier, with "no second carrier recorded". Does Site B use NordFrost? If it does, is NordFrost still the one? | candidate, to confirm | Site A activity list, A1, A2 and dependencies |
| 6.2 | If the single carrier fails, can another carrier be called, and by whom? | candidate, to confirm | Site A activity list, dependencies |
| 6.3 | Are there other third parties dispatch cannot work without, such as packaging, pallets or temperature-monitoring services? | candidate, to confirm | not in the sources |

## 7. Dependencies (up- and downstream, each with the RTO the relationship carries)

| # | Question | Direction | Label | RTO | Source |
|---|---|---|---|---|---|
| 7.1 | Does Site B dispatch wait for quality release from Site A, where the "lab at Site A only" is? | upstream: QA, Site A | candidate, to confirm | *(blank)* | Site A activity list, A3 and dependencies; Site B org chart |
| 7.2 | Does dispatch depend on the Site B warehouse lead's team for picking or receipt? | upstream: Warehouse, Site B | candidate, to confirm | *(blank)* | Site B org chart (undated) |
| 7.3 | Does Site B receive goods or data from Site A's dispatch through the manual export? | upstream: Dispatch, Site A | candidate, to confirm | *(blank)* | Site A activity list, A2 |
| 7.4 | Which departments depend on Site B dispatch? | downstream | candidate, to confirm | *(blank)* | not in the sources |

---

## Take-in sheet for the organiser

Planned for 60 minutes. Sections marked *(drop first)* are the ones to cut if time runs short.

**Unclear points (5 min).** The sources don't contradict each other, but these are unclear:
- Is the team still you plus three shift leaders? The org chart showing it has no date.
- What does "manual export to Site B" mean: goods, data, or both?
- Does Site B use NordFrost, the same single carrier as Site A?

**Peak weeks and impacts (12 min)**
- Which are your peak weeks? Site A's are weeks 49 to 52 and week 14.
- If dispatch stops in a peak week, when does the daily loss pass ten thousand euros, and when does it pass a hundred thousand?
- When is a key account late, and when is it lost?
- Could a stop ever mean a report to the food authority?
- Is any of this different outside the peak weeks?

**Longest tolerable stop (5 min)**
- After how long would the damage become unacceptable?

**People (10 min)**
- What is the shift pattern?
- What does a shift leader need to know to run dispatch alone?
- Who can release a load when QA is at Site A?
- Who besides you has the carrier contacts?

**Carriers and other suppliers (10 min)**
- Which carrier do you use? Is it still the same one?
- If that carrier fails, who can you call, and who makes the call?
- Who else can't you dispatch without?

**Systems (8 min)**
- Which systems do you need to dispatch?
- How long can each be down?
- How much data could you lose?

**Other departments (7 min)**
- Who do you wait on?
- Who waits on you?
- How long can each of them wait?

**Docks and space (3 min)** *(drop first)*
- Which docks and chilled areas do you use?
- Is there anywhere else you could use?

---

## Running the interview

Tell the dispatch lead to use the draft as something to correct, not something to confirm, and to record anything it could not have known. Anything the lead adds that isn't in the draft gets its own entry, marked "stated by dispatch lead, Site B, to confirm".

## After the interview: comparing the sites

Some answers may conflict with Site A's record, for example on the carrier, on LogiStock or on the manual export. Put each conflict to the two owners, the dispatch lead at Site A and the dispatch lead at Site B, not to the model.

## Gaps

- **Your statements (not sources):**
  - The interviewee is the dispatch lead at Site B.
  - They know the shift pattern and the carrier contacts.
  - You need back the resources and the peak weeks.

  Your statements shaped the scope only. Entries 3.1 and 3.4 rely partly on them.
- **Assumptions for questions you skipped:**
  - Interview length was not given, so I assumed 60 minutes.
  - You gave nothing about Site B beyond the files, so I assumed there is nothing further.
- **Site B organisation structure:** undated HR draft with no version. Not used as current. The roles in it are only questions.
- **Site B activity list:** not in the sources. Everything about Site B is by analogy with Site A's row A2.
- **Impact criteria:** they have no time axis. When each level is reached is not in the sources and is left to the owner.
- **Dock layout, other systems, other third parties and downstream departments:** not in the sources.
- **Channels:** memory, past chats, project files, connectors and web search are off. You did not report any of them as on.
- **Instructions aimed at an AI in the files:** none found.

## For the auditor

The register carries the source, the interview it came from and the date behind each entry. The following stay blank until after the interview:
- the interview itself
- the date the owner confirmed each entry
- the recovery times the owner set

Every entry above is a "candidate, to confirm". No source shows any entry as already confirmed.

## Reviewer

- **The dispatch lead at Site B** (activity owner) confirms each requirement and sets the MTPD and the RTOs.
- **Top management** approves the BIA results.

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

> Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- none
