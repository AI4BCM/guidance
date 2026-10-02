# /prepare-bia case 1, run1: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `8ad53fa0-3c99-4701-a22a-b780415017ac`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three attached files, I need one answer from you:

**What class of data do they hold?** For example: public, internal, or high-sensitivity. High-sensitivity covers BIA data, personnel records or contact lists, supplier dependencies and contractual weaknesses, and site or security detail.

Please take the class from what you know about the material, not from any marking in the files. If it's high-sensitivity, also confirm that this environment is approved for that class. If it isn't approved, I'll stop here.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md && ls -R; echo ---; ls -la /tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Glob: `**/*`
- Glob: `**/*`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. Your answer is recorded as the data class, and the environment is approved for it. I've read the three files. Before drafting, I have one round of questions for you as the organiser:

1. **Who is the interviewee?** I assume the Dispatch lead at Site B, but please give their role, and say whether any of the three shift leaders will also attend.
2. **What do you know that the files don't?** For example: what Site B actually dispatches, whether it uses the same warehouse system and carrier as Site A, and how it relies on Site A's lab for QA. Anything you tell me goes under Gaps as your own statement, not as a source. It can shape the questions but will never fill in a value.
3. **What do you need back from the interview?** For example, a full activity entry for dispatch only, or also the dependencies on goods receipt and QA release, and how long you'll have with them.
4. **Which of these are switched off in this session:** memory, past chats, project files, connectors and web search? Anything left on goes under Gaps.

Two points about the sources will appear in the draft either way:
- The Site B org chart is an undated HR draft with no version. I'll use it only as a pointer and list it under Gaps.
- The Site A list (v3, 12 Mar 2026) gives me questions to ask Site B, not facts about Site B.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/1/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/1/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/1/run1/work/site-b-org-chart.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide (draft): Dispatch, Site B

**Status:** draft for the organiser. Nothing here is in the register. Every entry is a "candidate, to confirm".
**Interviewee:** Dispatch lead, Site B (your own statement, see Gaps).

**Sources**
- Site A activity list: version 3, dated 12 March 2026, approved by the Site A site manager.
- Impact criteria: version 1.1, dated 4 February 2026, approved by top management.
- Site B organisation structure: no version and no date; an HR draft. Used only as a pointer, not as a current source (see Gaps).

No source proposes a recovery time for Site B. Every MTPD, RTO and RPO field below is blank on purpose.

---

## 1. Impacts over time (full rating for chilled dispatch only)

The sources don't rank Site B's activities. The organiser named chilled dispatch as the subject, so only dispatch gets the full rating. For anything else that comes up, ask only where it differs from dispatch.

| Question for the owner | Source | Status |
|---|---|---|
| Financial: after how long without dispatch does the loss pass "EUR 10k–100k a day" (level 2), and when does it pass "over EUR 100k a day" (level 3)? | Impact criteria v1.1, table, Financial | candidate, to confirm |
| Customer: after how long is "a key account is late" (level 2), and after how long is "a key account is lost" (level 3)? | Impact criteria v1.1, Customer | candidate, to confirm |
| Regulatory: can a dispatch outage alone lead to "a report to the food authority" or to "the authority stops production"? If so, after how long? | Impact criteria v1.1, Regulatory | candidate, to confirm |
| Peak weeks: are Site B's peak weeks the same as Site A's ("weeks 49–52, week 14"), and does the timing above change in those weeks? | Site A list v3, row "Dispatch, chilled", Peak weeks | candidate, to confirm |

## 2. MTPD

| Question for the owner | Source | MTPD | Status |
|---|---|---|---|
| From the answers in section 1, how long can chilled dispatch at Site B be down before the impact becomes unacceptable? Is that different in peak weeks? | Impact criteria v1.1 | *(blank)* | candidate, to confirm |

## 3. People, "with the skills, authorities and mandates the work needs"

| Question for the owner | Source | Status |
|---|---|---|
| The HR draft shows a dispatch lead with "three shift leaders". Is that current, and what is the shift pattern? | Gaps (Site B org chart, undated draft); organiser's statement | candidate, to confirm |
| What is the minimum number of people per shift needed to keep chilled dispatch running? | not in the sources | candidate, to confirm |
| Who can release a load, sign transport documents or change a carrier booking? Who stands in for each of them? | not in the sources | candidate, to confirm |
| Is there one person behind the carrier contacts? If so, who covers when they are absent? | Gaps (organiser's statement) | candidate, to confirm |

## 4. Seats and buildings

| Question for the owner | Source | Status |
|---|---|---|
| How many dock doors and chilled staging areas does Site B dispatch use? (Site A records "two dock doors" for goods receipt only.) | Site A list v3, row "Goods receipt, chilled", Notes | candidate, to confirm |
| Is there anywhere else chilled dispatch could run from, and how many desks or seats would it need there? | not in the sources | candidate, to confirm |

## 5. IT and applications, "each with its RTO and its RPO"

| Question for the owner | Source | RTO | RPO | Status |
|---|---|---|---|---|
| Does Site B use "LogiStock" for dispatch, or another system? | Site A list v3, row "Dispatch, chilled", Notes | *(blank)* | *(blank)* | candidate, to confirm |
| Site A notes "manual export to Site B possible". Does Site B receive that export? What does it use it for, and how is it done? | Site A list v3, row "Dispatch, chilled", Notes | *(blank)* | *(blank)* | candidate, to confirm |
| What other applications do you need: label printing, transport booking, temperature records? | not in the sources | *(blank)* | *(blank)* | candidate, to confirm |

## 6. Suppliers and other third parties

| Question for the owner | Source | Status |
|---|---|---|
| Site A records NordFrost as its carrier, with "no second carrier recorded". Does Site B use NordFrost too? Is it still the one? | Site A list v3, Dependencies recorded | candidate, to confirm |
| Is there any other carrier or fallback that Site B has used or could use? | not in the sources | candidate, to confirm |
| Which other third parties does dispatch rely on, such as cooling maintenance or pallet supply? | not in the sources | candidate, to confirm |

## 7. Dependencies, as "up- and downstream relationships with other departments, each recorded with the RTO the relationship carries"

| Question for the owner | Source | RTO of the relationship | Status |
|---|---|---|---|
| Upstream: QA is "covered from Site A" and the lab is "at Site A only". Does every Site B load need a QA release from Site A before it leaves? | Gaps (Site B org chart); Site A list v3, row "Quality release" | *(blank)* | candidate, to confirm |
| Upstream: what does dispatch need from the Site B warehouse lead, and by when? | Gaps (Site B org chart) | *(blank)* | candidate, to confirm |
| Upstream or sideways: does Site A dispatch send work or data to Site B dispatch (the "manual export")? | Site A list v3, row "Dispatch, chilled" | *(blank)* | candidate, to confirm |
| Downstream: which departments or key accounts depend on Site B dispatch? | not in the sources | *(blank)* | candidate, to confirm |

---

## Cross-site points for the two owners (not settled here)

- **QA release.** Site A records dispatch depending on QA release at Site A. It does not record Site B as a user of that release, while the Site B draft says QA is covered from Site A. Put this to the QA manager at Site A and the Dispatch lead at Site B.
- **Manual export.** Site A records a manual export to Site B. Nothing on the Site B side records it. Put this to the dispatch leads at both sites.
- **Shared carrier.** If Site B also uses NordFrost, both sites rely on one carrier. Put this to both dispatch leads, and to the Site A warehouse lead for goods receipt.

## For the interview

Tell the Dispatch lead to "use the draft as the thing to correct, not the thing to confirm; record what it could not have known".

---

## Take-in sheet for the organiser (about 60 minutes)

**Conflicts first (10 min)**
Does every load you send need a release from the Site A lab first?
Do you receive a manual export from Site A dispatch, and what do you do with it?
Do you use NordFrost as well, and is it still the one?

**Impacts over time (12 min)**
When does a dispatch stop start costing over ten thousand euros a day, and when over a hundred thousand?
When is a key account late, and when do you lose one?
Could a dispatch stop on its own bring a report to the food authority?
Which are your peak weeks, and are they the same as Site A's?

**MTPD (5 min)**
How long can dispatch be down before it becomes unacceptable, in a normal week and in a peak week?

**People (10 min)**
What is your shift pattern, and are there still three shift leaders?
How many people per shift do you need at minimum?
Who can release a load or change a booking, and who stands in for them?
Who holds the carrier contacts, and who covers when they're away?

**Seats and buildings (5 min)**
How many dock doors and chilled staging areas do you use?
Could dispatch run from anywhere else? (drop first)

**IT and applications (8 min)**
Which system do you dispatch from, and what else do you need to send a load?
How long can each one be down, and how much data can you afford to lose? (for the owner to set later, not to fix now)

**Suppliers (5 min)**
Have you ever used a second carrier, or could you?
Who else do you depend on, such as cooling maintenance or pallets? (drop first)

**Dependencies (5 min)**
What do you need from the warehouse lead, and by when?
Who downstream is hit first when dispatch stops? (drop first)

---

## Gaps

- **Organiser's own statements, not sources:** the interviewee is the Dispatch lead at Site B; they know the shift pattern and the carrier contacts; the interview should return resources and peak weeks. These shaped the scope and fill no value.
- **Not answered, with the assumption made:**
  - Whether memory, past chats, project files, connectors and web search are switched off. Not confirmed, so the draft may have drawn on one of them without saying so. This draft was built only from the three attached files and the skill's own units.
  - How long the interview will be. Assumed 60 minutes.
  - Whether the shift leaders will attend. Assumed not.
- **Site B organisation structure:** "Undated draft from HR, no version". Not used as current. Every entry that rests on it is a question.
- **Site A activity list:** describes Site A. Every name taken from it (LogiStock, NordFrost, the peak weeks) is a question for Site B, not a Site B fact.
- **Recovery times:** not in the sources. No source proposes an MTPD, RTO or RPO for Site B.
- **Instructions to an AI found in the material:** none.

## For the auditor

The register carries "the source, the interview it came from and the date behind each entry". Until the interview, three fields stay blank: the interview, the confirmation date and "the recovery times the owner set".

## Reviewer

- **Dispatch lead, Site B (activity owner):** confirms each requirement and sets the MTPD and RTO.
- **Top management:** "Top management approves the BIA results."

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- Grep: `Say in the document that AI helped`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
