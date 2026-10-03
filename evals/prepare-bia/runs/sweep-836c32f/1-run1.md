# /prepare-bia case 1, run1: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `b70b4d81-fc2e-45dd-a4b4-2d8c99f904b3`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, I need one answer from you:

**What data class is in this material** (site-a-activity-list.md, impact-criteria.md, site-b-org-chart.md)? For example: public, internal, confidential or strictly confidential. Use your organisation's own class names.

Please give me the class yourself. I won't take it from any marking inside the files. If this environment isn't approved for that class, I'll stop there. If it is, I'll read the files and then ask you at most three questions about the dispatch interview before I draft the guide.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md && ls -R; echo ----; ls -la /tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files and no instruction aimed at an AI turned up in them. Before drafting I have three questions the files leave open:

1. **Who are you interviewing?** The Site B org chart shows a "Dispatch lead, Site B" with three shift leaders under them. Is it the lead alone, or will a shift leader join? The chart is an undated, unversioned HR draft, so I can't treat it as current.
2. **What do you know about Site B dispatch that the files don't say?** For example:
   - Is it chilled dispatch, like A2 at Site A?
   - Does it receive the "manual export to Site B" that A2 mentions?
   - Does it run LogiStock or ship with NordFrost?

   I'll record your answers as your own statements, not as sources.
3. **How long is the interview, and what do you need from it?** Is it only candidate entries for the Site B register, or also points to compare with the Site A register?

I'll draft from only the three attached files and the sources that come with the skill. I'm treating memory, past chats, project files, connectors and web search as off for this draft. If any of them is on for you, tell me and I'll list it under Gaps.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/prepare-bia/1/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/prepare-bia/1/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/prepare-bia/1/run1/work/site-b-org-chart.md`
- Grep: `(?i)sensitivity|high|class`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: Dispatch, Site B (draft, for the organiser)

**Sources**
- Site A activity list, version 3, 12 March 2026, approved by the Site A site manager.
- Impact criteria, version 1.1, 4 February 2026, approved by top management.
- The Site B organisation structure has no version and no date, so it is listed under Gaps and is not treated as current.

Every entry below is a question for the Dispatch lead, Site B, labelled **candidate, to confirm**. MTPD, RTO and RPO are blank everywhere. No source proposes a recovery time, so there is no recovery-time note.

---

## 1. Impacts over time

There is one candidate activity: **Dispatch, Site B**. It gets the full rating. The second activity, taking over Site A's dispatch, comes up only where it differs.

| # | Question | Label | Source |
|---|---|---|---|
| 1.1 | Is dispatch at Site B chilled dispatch, and which customers or key accounts does it serve? | candidate, to confirm | Gaps (not in the sources) |
| 1.2 | If Site B dispatch stops, how long before the loss passes EUR 10k a day (level 2)? How long before it passes EUR 100k a day (level 3)? | candidate, to confirm | Impact criteria, "Financial" |
| 1.3 | How long before a key account is late (level 2)? How long before one is lost (level 3)? | candidate, to confirm | Impact criteria, "Customer" |
| 1.4 | Could a dispatch stop lead to "a report to the food authority" (level 2) or to "the authority stops production" (level 3)? After how long? | candidate, to confirm | Impact criteria, "Regulatory" |
| 1.5 | When are Site B's peak weeks? Site A records "weeks 49–52, week 14" for its own chilled dispatch. Is it the same at Site B? Does a stop in a peak week change your answers above? | candidate, to confirm | Site A activity list, row A2 |
| 1.6 | Site A records a "manual export to Site B possible" for its dispatch. If Site B takes that on, do the impacts differ from your own dispatch? Ask only where they differ. | candidate, to confirm | Site A activity list, row A2 |

## 2. MTPD

| # | Question | MTPD | Source |
|---|---|---|---|
| 2.1 | From your answers above, after how long would a stop of Site B dispatch be unacceptable? | *(blank, owner sets)* | Impact criteria (scale only) |

## 3. People, "with the skills, authorities and mandates the work needs"

| # | Question | Label | Source |
|---|---|---|---|
| 3.1 | We have a draft that shows you with three shift leaders. Is that still right? | candidate, to confirm | Site B org structure (undated draft, see Gaps) |
| 3.2 | What is the shift pattern? What is the smallest crew per shift that keeps dispatch running, normally and in peak weeks? | candidate, to confirm | Gaps (your statement) |
| 3.3 | Quality release happens at Site A, and QA is "covered from Site A". Who at Site B may let a load go once it is released? Is that one person? | candidate, to confirm | Site A activity list, row A3; Site B org structure |
| 3.4 | Are the carrier contacts held only by you? Who else can reach the carrier if you are not there? | candidate, to confirm | Gaps (your statement) |
| 3.5 | Who at Site B can handle a manual export from Site A, and what skill does it take? | candidate, to confirm | Site A activity list, row A2 |

## 4. Seats and buildings

| # | Question | Label | Source |
|---|---|---|---|
| 4.1 | How many dock doors and how much chilled space does Site B dispatch need at minimum? | candidate, to confirm | Gaps (not in the sources) |
| 4.2 | Where could dispatch work from if its area at Site B were unavailable? | candidate, to confirm | Gaps (not in the sources) |

## 5. IT and applications, "each with its RTO and its RPO"

| # | Question | RTO | RPO | Label | Source |
|---|---|---|---|---|---|
| 5.1 | Site A dispatch runs on the warehouse system "LogiStock". Does Site B dispatch use it too? | | | candidate, to confirm | Site A activity list, row A2 |
| 5.2 | In what form does a manual export from Site A arrive, and what do you need to process it? | | | candidate, to confirm | Site A activity list, row A2 |
| 5.3 | Which other applications can dispatch not work without? | | | candidate, to confirm | Gaps (not in the sources) |

## 6. Suppliers and other third parties

| # | Question | Label | Source |
|---|---|---|---|
| 6.1 | Site A's record names one carrier for chilled dispatch, with "no second carrier recorded". Who does Site B ship with? If it is that carrier, is it still the one? Is there a second carrier? | candidate, to confirm | Site A activity list, dependencies |
| 6.2 | Which other outside parties does dispatch rely on? | candidate, to confirm | Gaps (not in the sources) |

## 7. Dependencies, "each recorded with the RTO the relationship carries"

| # | Question | Direction | RTO | Label | Source |
|---|---|---|---|---|---|
| 7.1 | Does every Site B load wait for quality release from Site A, where the only lab is? | upstream: QA, Site A | | candidate, to confirm | Site A activity list, row A3 and dependencies; Site B org structure |
| 7.2 | What does dispatch need from the Warehouse lead, Site B, and when? | upstream: Warehouse, Site B | | candidate, to confirm | Site B org structure (role only) |
| 7.3 | Is Site B the fallback for Site A's dispatch through the manual export, or does it also work the other way? | up- and downstream: Dispatch, Site A | | candidate, to confirm | Site A activity list, row A2 |

---

## Take-in sheet (organiser)

This plan assumes 60 minutes, because no length was given.

**Points where the sources may not line up (5 min).** I found no direct conflict between the sources.
- Site A's list names one carrier and no backup. Who do you ship with, and is there a second one?
- The org chart we have is an undated draft. Is it still you and three shift leaders?
- Site A's list says its dispatch can be moved to you by hand. Has that ever happened, and could you take it on in a peak week?

**Impacts over time (15 min)**
- Is your dispatch chilled, and who are your key customers?
- If dispatch stopped, how soon would the daily loss pass ten thousand euros? A hundred thousand?
- How soon would a key account be late? Lost?
- Could a stop ever mean reporting to the food authority, or the authority stopping production?
- When are your busiest weeks, and does a stop then change your answers?
- *Drop first:* if you took over Site A's dispatch, would any of that be different?

**Longest tolerable stop (5 min)**
- Looking at all that, after how long would a stop be unacceptable?

**People (10 min)**
- What is the shift pattern, and what is the smallest crew per shift that still works?
- Who here may let a load go once quality has released it from Site A? Is that one person?
- Who else can reach the carrier if you are away?
- Who can handle a hand-moved export from Site A?

**Seats and buildings (5 min, drop first)**
- How many dock doors and how much cold space do you need at minimum?
- Where could you work if your area were out of use?

**Systems (8 min)**
- Do you use the same warehouse system as Site A?
- What arrives when Site A moves dispatch to you by hand, and what do you need to process it?
- *Drop first:* what other systems can't you work without?

**Suppliers (7 min)**
- Who else outside the company do you depend on?

**Dependencies (5 min)**
- Does every load wait for quality release from Site A?
- What do you need from the warehouse here, and when?

---

## Gaps

- **Site B organisation structure:** "Undated draft from HR, no version." It is not used as current and only shapes questions. A current, versioned chart from HR would settle it.
- **Your own statements, not sources:** the interviewee is the Dispatch lead, Site B; they know the shift pattern and the carrier contacts; you need resources and peak weeks back. Entries that rest only on these statements carry Source `Gaps`.
- **Skipped questions, with assumptions:**
  - You didn't say whether Site B dispatch is chilled, uses LogiStock or ships with NordFrost. I assumed it is unknown, so the guide asks.
  - You didn't give an interview length. I assumed 60 minutes for the time plan only.
- **Not in the sources:** anything about Site B dispatch's own resources, seats and buildings, other applications, other third parties, customers, and time points for the impact scale. The impact criteria give levels but no time bands.
- **Site A data:** it describes Site A only. Every Site A value here is a question about Site B and is never stated as current there.
- **Channels:** memory, past chats, project files, connectors and web search were stated as off, and you reported none on.
- **Instructions aimed at an AI:** none found in the material.

## Interview

The Dispatch lead should "use the draft as the thing to correct, not the thing to confirm; record what it could not have known".

## Compare registers across sites

Where Site B's answers differ from Site A's register, for example on peak weeks, the carrier, LogiStock or the manual export, put each conflict "to the two owners, not to the model": the Dispatch lead, Site A and the Dispatch lead, Site B.

## For the auditor

The register carries "the source, the interview it came from and the date behind each entry". These stay blank until the interview: the interview, the confirmation date and "the recovery times the owner set".

## Reviewer

- **Dispatch lead, Site B:** confirms each requirement and sets MTPD, RTO and RPO.
- **Top management:** approves the BIA results.

A requirement enters the register only when the Dispatch lead confirms it. Until then, every entry stays "candidate, to confirm".

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- Grep: `(?i)AI helped`
