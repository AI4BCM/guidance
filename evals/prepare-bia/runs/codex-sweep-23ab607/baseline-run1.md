# prepare-bia baseline (no skill loaded), run1: Codex, guidance at 23ab607

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a0feee-d424-7df2-b732-19732d95aed0`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’ll read the three files and use them to draft a Site B dispatch interview guide, with questions tied to the impact criteria and the site’s responsibilities.

# Site B dispatch interview guide — draft

**Purpose:** Identify Site B’s dispatch activities, how disruption affects them over time, and the resources and recovery arrangements they need.

**Interviewees:** Dispatch lead, Site B, with input from the three shift leaders. Seek follow-up evidence from the warehouse lead, QA at Site A and the Site B manager.

**Suggested duration:** 60–75 minutes.

**Source status:** Site A’s activity list is approved for Site A; use it as a prompt, not as evidence of Site B’s arrangements. The impact criteria are approved by top management. Site B’s organisation chart is an undated, unversioned HR draft; confirm roles and reporting lines during the interview.

## 1. Confirm scope and responsibilities — 10 minutes

- What does Site B dispatch handle: products, customers, destinations and operating hours?
- Walk through dispatch from receipt of an order to carrier handover. Where does dispatch responsibility start and end?
- Which steps are separate activities with different owners, dependencies or recovery needs?
- Who owns dispatch, who provides cover, and what do the three shift leaders each control?
- Which decisions require the warehouse lead, QA or site manager?
- Does the draft organisation chart accurately reflect current responsibilities?

**Record:** Activity names, boundaries, accountable owners, deputies, shift coverage and corrections to the organisation chart.

## 2. Establish normal operations and peak demand — 10 minutes

- What are normal and peak daily volumes, staffing levels and dispatch cut-off times?
- Which customers or orders have priority, and why?
- What storage capacity is available if goods cannot leave? When would congestion, temperature control or shelf life become a constraint?
- Site A records peaks in weeks 49–52 and week 14. Do these apply to Site B? What other peaks matter?
- How does disruption on one shift affect later shifts?

**Request evidence:** Volume reports, shift schedules, customer delivery requirements and storage-capacity information.

## 3. Identify dependencies and failure points — 15 minutes

Use these Site A arrangements as questions to verify, rather than assumptions:

| Site A reference | Questions for Site B |
|---|---|
| Dispatch uses LogiStock | What systems does Site B use? Which functions, data, devices and access rights are essential? |
| Manual export to Site B is possible | What does this export support at Site B? Who initiates it, how current is the data, and has the process been tested? |
| QA release is required before dispatch; the lab is at Site A | How does Site B obtain and verify release? What happens if Site A’s QA staff, lab or communication links are unavailable? Who may authorise release? |
| NordFrost is the recorded carrier; no second carrier is recorded | Which carriers serve Site B? What capacity is committed, and are alternatives contracted and available during peaks? |
| Site A has two dock doors | How many usable loading points does Site B have? What happens if one or all become unavailable? |

Also ask:

- Which warehouse activities, people, facilities, utilities and external services must be available?
- Are there single points of failure or dependencies shared with Site A?
- Which dependencies have workable substitutes, and what limits their use?

**Record:** Dependency, provider or owner, failure effect, substitute, activation time, capacity and supporting evidence.

## 4. Assess impacts over time — 15 minutes

Consider a **complete dispatch stoppage** and **reduced dispatch capacity**, starting at a demanding but credible time. Assess normal and peak periods separately where results differ.

Suggested checkpoints are 2, 4, 8, 24, 48 and 72 hours; adjust them to actual shifts, delivery deadlines and product constraints.

Apply the approved criteria:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | Under EUR 10k a day | One customer complains | None |
| 2 | EUR 10k–100k a day | A key account is late | A report to the food authority |
| 3 | Over EUR 100k a day | A key account is lost | The authority stops production |

At each checkpoint ask:

- What happens, and when does it first happen?
- What daily financial loss results, and how is it estimated? Record cumulative loss separately.
- Which customers are affected? When would a key account become late or potentially be lost?
- What specific circumstances would require an authority report or lead to a production stop? Confirm these with QA.
- What backlog, spoilage, storage or food-safety consequences develop?

Score each impact category separately. Record assumptions, evidence and uncertainty. The supplied criteria do **not** define an overall scoring rule or the threshold for an unacceptable impact; flag those for confirmation.

## 5. Define recovery needs and validate workarounds — 10 minutes

- When would continued disruption become unacceptable, and why?
- What recovery time objective is needed to restore an agreed minimum dispatch service before that point?
- What is that minimum service: volume, priority orders, operating hours and required controls?
- What staff, systems, data, equipment, space, QA support and carrier capacity are needed?
- How much data loss or delay can dispatch tolerate?
- What workarounds exist, how quickly can they start, and how long can they operate?
- Could Site A support Site B, or Site B support Site A? Confirm capacity, authorisation and constraints.
- How long would clearing the backlog and returning to normal take?

Treat recovery objectives and workaround capacity as **proposals pending validation**, not approved commitments.

## 6. Close and capture actions — 5 minutes

Read back the activity scope, earliest significant impacts, proposed recovery requirements and unresolved dependencies. Agree evidence requests, action owners and due dates.

Use this record for each identified activity:

| Field | Interview finding |
|---|---|
| Activity, scope, owner and deputy | |
| Normal and peak demand | |
| Impacts by elapsed time and category | |
| Point at which disruption becomes unacceptable, with rationale | |
| Proposed recovery time and minimum service | |
| Data recovery requirement | |
| Essential dependencies and resources | |
| Workarounds, capacity and test evidence | |
| Assumptions and open questions | |
| Follow-up owner and due date | |

Have the dispatch lead validate the factual record, QA validate release and regulatory findings, and the Site B manager confirm ownership and recovery proposals through the applicable BCM approval process.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g '*.md'"`
- command_execution: `/bin/bash -lc 'cat impact-criteria.md'`
- command_execution: `/bin/bash -lc 'cat site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md'`
