# $prepare-bia case 1, run3: Codex, guidance at 836c32f

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff12-5ec4-7111-9c93-e3e0014bccc5`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide from the three attached files. I’ll first check the skill’s preflight and the source material.

The skill’s preflight requires your data classification before I access the attachments. I listed their filenames too early; I haven’t read their contents. Memory, past chats, other project files, connectors and web search are off.

What data classification do the three attachments hold?

What data classification do the three attachments hold?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first.” I need your answer before reading their contents and drafting the guide.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g '*.md' -g '"'!node_modules'"' -g '"'!vendor'"' ."`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md; cat .agents/skills/prepare-bia/preflight.md; cat .agents/skills/prepare-bia/units/prompts/bia.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read the three attachments now that you’ve confirmed their classification and this environment’s approval. The guide will stay in chat, with recovery fields blank for the activity owner to set.

Who will be interviewed for Site B dispatch, and what do they know that you still need to establish?

What do you need back from the interview beyond the guide—for example, corrected activity scope, confirmed requirements, or an interview record?

How long is the interview?

The Site A list provides dispatch details to test at Site B, but it does not rank activities by impact. The Site B organisation chart is an undated draft, so its staffing and QA arrangements need confirmation. I’ll use your intake answers to set the interview scope and timing.

Before I draft the guide, please confirm:

1. Who will be interviewed, and what do they know that you need to establish?
2. What should the interview produce—corrected activity scope, confirmed requirements, an interview record, or something else?
3. How long is the interview?

The [prepare-bia intake](.agents/skills/prepare-bia/units/prompts/bia.md) says “Wait for my answers.” These answers will shape the guide; recovery fields will remain blank.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md; cat impact-criteria.md; cat site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/keep-it-running.md; cat .agents/skills/prepare-bia/units/stages/analysis.md'`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on dispatch resources and peak weeks, using the Site B dispatch lead’s knowledge of shifts and carrier contacts. Since you left the interview length open, I’ll assume 45 minutes and mark questions to drop if time runs short. The Site A details will remain questions for Site B to correct.

**Sources**

- **site-a-activity-list.md**, “Site A: activity list (chilled food production)” — version 3, 12 March 2026; approved by the Site A site manager. Evidence about Site A; applicability to Site B remains unconfirmed.
- **impact-criteria.md**, “Impact criteria” — version 1.1, 4 February 2026; approved by top management.
- **site-b-org-chart.md**, “Site B: organisation structure” — no version or date; draft from HR. Listed under Gaps and used only to frame questions.

**Site B dispatch interview guide — draft**

Interviewee: Site B dispatch lead. Intended output: dispatch resource requirements and peak weeks. Assumed duration: 45 minutes.

Tell the activity owner: **“Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”**

Every Site B entry below is **candidate, to confirm**. A resource requirement enters the register only after the activity owner confirms it. Approval of a Site A source does not confirm the same requirement at Site B.

### 1. Impacts over time and peak weeks

| Candidate activity or impact question | Evidence |
|---|---|
| Does Site B carry out chilled dispatch, and what are its start and end points? | Site A activity list, A2, 12 March 2026 |
| Are weeks 49–52 and week 14 also dispatch peaks at Site B? Which weeks differ, and what changes in the resources needed? | Site A activity list, A2, “Peak weeks,” 12 March 2026 |
| As dispatch interruption continues, when would financial, customer or regulatory impacts move between the approved levels? What evidence supports each assessment? | Impact criteria, level table, 4 February 2026 |
| How do those impacts change during Site B’s peak weeks? | Site A activity list, A2, “Peak weeks”; Impact criteria, level table |

Use the approved criteria without assigning scores in advance:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

Source: *Impact criteria*, level table, 4 February 2026.

Ask the owner to identify the relevant interruption intervals, then assess all three impact categories at each interval. The sources contain neither an activity ranking nor assessed impacts over time. Dispatch receives the full discussion because it is the requested scope. If related activities emerge, ask where their impacts differ; do not assign them dispatch’s ratings.

### 2. MTPD

At what point would interruption of Site B dispatch become unacceptable, based on the impacts described? Does the limiting point change in peak weeks?

The activity owner sets MTPD. No recovery values are proposed in the attachments.

| Candidate activity | MTPD | Activity RTO | Interview reference | Confirmation date |
|---|---|---|---|---|
| Does chilled dispatch belong in Site B’s activity register? — **candidate, to confirm**; Site A activity list, A2, 12 March 2026 | | | | |

### 3. People

Discuss people **with the skills, authorities and mandates the work needs**.

| Candidate requirement question | Source |
|---|---|
| Is dispatch lead still the role accountable for dispatch at Site B? | Site A activity list, A2, “Owner (role),” 12 March 2026 |
| Does the draft’s arrangement of three shift leaders still apply? What shift pattern and minimum staffing does dispatch require in normal and peak weeks? | Site B organisation structure, dispatch reporting line; undated draft |
| What skills, authorities and mandates must the dispatch lead and shift leaders hold? Who can cover those requirements? | Site B organisation structure, dispatch reporting line; undated draft. Specific requirements: not in the sources |

Do not treat three shift leaders as the minimum staffing requirement or assume any individual is the sole person capable of performing the work.

### 4. Seats and buildings

| Candidate requirement question | Source |
|---|---|
| Which seats, buildings and physical dispatch facilities does Site B require, and how much capacity is needed during peak weeks? | Gaps — dispatch facilities and capacity are not in the sources |
| Site A records two dock doors for goods receipt: does this reveal any shared receipt/dispatch facility requirement at Site B, or is it irrelevant to dispatch here? | Site A activity list, A1, “Notes,” 12 March 2026 |

The two dock doors are recorded for **Site A goods receipt**; they are not a confirmed Site B dispatch requirement.

### 5. IT and applications

Discuss IT and applications **each with its RTO and its RPO**, to be set by the owner after identifying the requirement.

| Candidate requirement question | Source | RTO | RPO |
|---|---|---|---|
| Site A records LogiStock: is LogiStock still the one, and does Site B dispatch use it? What function and information does dispatch require from it? | Site A activity list, A2, “Notes,” 12 March 2026 | | |
| Is the recorded manual export to Site B still possible? What does it provide, and what does it fail to provide for dispatch? | Site A activity list, A2, “Notes,” 12 March 2026 | | |

### 6. Suppliers and other third parties

| Candidate requirement question | Source |
|---|---|
| Site A records NordFrost: is NordFrost still the one, and does it serve Site B dispatch? | Site A activity list, “Dependencies recorded,” 12 March 2026 |
| Who holds the current carrier contacts, and what service and capacity does dispatch need in normal and peak weeks? | Same dependency record; contact holders and Site B capacity: not in the sources |
| Site A records no second carrier: does Site B have another carrier, and what can that carrier actually cover? | Site A activity list, “Dependencies recorded,” 12 March 2026 |

A single carrier or contact remains a question for the owner; the draft does not establish sole dependence.

### 7. Dependencies on other departments

Record **up- and downstream relationships with other departments, each recorded with the RTO the relationship carries**.

| Candidate relationship question | Source | Relationship RTO |
|---|---|---|
| Does Site B dispatch require quality release from Site A before dispatch? What must QA provide, and when? | Site A activity list, A2–A3 and “Dependencies recorded,” 12 March 2026; Site B organisation structure, QA line, undated draft | |
| Does the Site A-only laboratory arrangement still apply to Site B’s release process? | Site A activity list, A3, “Notes,” 12 March 2026; Site B organisation structure, QA line, undated draft | |
| What does Site B dispatch receive from, and provide to, the warehouse department? | Site B organisation structure, warehouse reporting line, undated draft; actual relationship not in the sources | |
| Which other departmental inputs or outputs must be recorded? | Gaps — not in the sources | |

### Organiser’s take-in sheet

No direct contradiction is established by the attachments. Resolve differences between Site A’s approved record and Site B’s draft arrangements first.

**Cross-source differences — about 4 minutes**

Does Site B’s QA coverage from Site A mean the same release-before-dispatch dependency recorded at Site A?

Does the Site A-only laboratory arrangement still apply?

Does the draft showing three shift leaders still describe Site B?

**Impacts and peak weeks — about 10 minutes**

What exactly does Site B dispatch include?

Are weeks 49–52 and week 14 also your peak weeks?

What changes in those weeks?

As dispatch stays stopped, when do the financial, customer and regulatory impacts reach each approved level?

**MTPD — about 4 minutes**

When does the interruption become unacceptable, and which impact makes it so?

**People — about 6 minutes**

What is the shift pattern in normal and peak weeks?

How many people are needed, with which skills, authorities and mandates?

Who can cover those requirements?

**Seats and buildings — about 4 minutes**

Which workspaces and dispatch facilities are essential, and what capacity is needed?

Do the two receipt dock doors recorded at Site A tell us anything relevant here? **Drop first if late.**

**IT and applications — about 5 minutes**

Is LogiStock still the one, and do you use it here?

What information and functions must be available?

Is the manual export from Site A still possible? **Drop first if late.**

What RTO and RPO does each required application need?

**Suppliers — about 5 minutes**

Is NordFrost still the one for Site B?

Who holds the current carrier contacts?

What carrier capacity is needed during peak weeks?

Is another carrier available, and what can it cover?

**Departmental dependencies — about 5 minutes**

What must QA and the warehouse provide before dispatch can work?

What does dispatch provide to other departments?

What RTO does each relationship need?

**Corrections and close — about 2 minutes**

Which candidate requirements should be removed or corrected?

What did this draft miss?

### Gaps and handover

- **Organiser’s own statements, not sources:** the interviewee is the Site B dispatch lead, who knows the shift pattern and carrier contacts; the requested output is resources and peak weeks. These shape the scope and do not populate requirement values.
- **Interview length:** unanswered; 45 minutes is a planning assumption.
- **Site B organisation chart:** undated, unversioned HR draft; not established as current. Obtain its date, version and approved status, and resolve its arrangements with the owner.
- **Not in the sources:** Site B’s confirmed activity scope, peak weeks, staffing minimums, mandates, facilities, carrier arrangements, application requirements, assessed impacts and recovery values. Owner evidence is needed.
- **Source currency:** the two approved documents have dates and versions, but the attachments do not establish whether they have since been replaced.
- Memory, past chats, other project files, connectors and web search remained off.

For every eventual register entry, retain its source and source date, interview reference, confirmation date and confirmed/unconfirmed mark. Interview references, confirmation dates and owner-set recovery fields remain blank before the interview. Preserve the Site A documents’ approval status without transferring it to Site B candidates.

Put each cross-site conflict **“to the two owners, not to the model”**—including dispatch, QA or warehouse owners as applicable. The Site B activity owner confirms each requirement and sets MTPD, RTO and RPO. **Top management approves the BIA results.**

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
