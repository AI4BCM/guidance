# prepare-bia baseline (no skill loaded), run1: Codex, guidance at 3f263b8

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a0fe62-d253-74d1-98ee-4e336d05a584`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’ll read the three files and use them to draft a dispatch interview guide tailored to Site B.

# Site B dispatch interview guide

**Purpose:** Confirm how dispatch operates at Site B, assess the consequences of interruption, and identify recovery requirements and dependencies.

**Status:** Draft for validation. Site A’s approved activity list is a reference for questions; it does not establish Site B’s activities or dependencies. Site B’s organisation chart is undated and unapproved.

**Participants:** Dispatch lead, Site B, with input from the three shift leaders. Involve the warehouse lead and Site A QA representative for dependency questions. Confirm who at Site B will approve the findings.

**Suggested duration:** 75–90 minutes.

## 1. Confirm ownership and scope — 10 minutes

- Is the organisation chart current? Who owns dispatch, who deputises, and who makes decisions during an interruption?
- What does “dispatch” include at Site B: order preparation, picking, staging, loading, transport booking, documentation, or other steps?
- Where does the activity start and end? Which steps belong to warehouse, QA, or carriers?
- Does Site B dispatch chilled food? What products, customers, routes, and operating hours are in scope?
- How do responsibilities and staffing differ across the three shifts?

**Record:** Agreed activity description, boundaries, accountable owner, deputies, and any corrections to the organisation chart.

## 2. Understand normal operations and peaks — 10 minutes

- Walk through a recent order from receipt to departure. What must be available at each step?
- What are normal and peak daily volumes, customer cut-off times, and loading windows?
- Site A records peaks in weeks 49–52 and week 14. Does Site B have the same peaks, different ones, or none?
- What backlog can Site B hold safely? What limits arise from chilled storage, shelf life, dock capacity, or vehicle availability?
- Which orders or customers would receive priority if capacity fell?

**Request evidence:** Dispatch schedules, volume records, customer commitments, shift rosters, and relevant operating procedures.

## 3. Assess interruption impacts — 20 minutes

Use the **top-management-approved impact criteria, version 1.1**, without changing the thresholds:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | Under EUR 10k a day | One customer complains | None |
| 2 | EUR 10k–100k a day | A key account is late | A report to the food authority |
| 3 | Over EUR 100k a day | A key account is lost | The authority stops production |

Consider a complete dispatch stoppage first, then reduced capacity. Assess normal operations and peak periods separately where the consequences differ.

- What happens after each missed loading window or customer cut-off?
- When would each impact level first be reached? What evidence supports that timing?
- What financial loss occurs per day—for example, spoilage, penalties, lost sales, or additional transport costs? Identify assumptions and avoid double counting.
- Which key accounts become late, and when could an account be lost?
- Could an interruption cause a report to the food authority or an authority-imposed production stop? Ask QA to validate the circumstances and timing.
- What food safety, temperature-control, or traceability consequences arise? Record these explicitly even where the supplied criteria do not fully describe them.

Use operationally meaningful intervals; **2, 8, 24, 48, and 72 hours** are prompts, not agreed limits.

| Elapsed interruption | Operational consequence | Financial loss/day and level | Customer consequence and level | Regulatory consequence and level | Evidence / assumptions |
|---|---|---|---|---|---|
| | | | | | |

Record the dimensions separately. Confirm the approved method for combining scores and deciding which impact becomes unacceptable; do not invent one.

## 4. Confirm dependencies and alternatives — 15 minutes

Treat Site A’s recorded dependencies as questions to investigate:

- **QA:** The draft chart says QA is covered from Site A. Does Site B require QA release before dispatch? How are releases communicated and verified? What happens if Site A QA or its laboratory is unavailable?
- **Systems:** Does Site B use LogiStock or another warehouse system? What data, interfaces, devices, connectivity, and access are essential?
- **Site A transfer:** Site A records that manual export to Site B is possible. What is exported, who produces and receives it, and can Site B actually use it during an outage? Has this been tested?
- **Transport:** Does Site B use NordFrost? Are alternatives contracted, suitable for chilled goods, and available at peak times?
- **People and premises:** What minimum skills, staffing, dock access, chilled storage, power, and equipment are required?
- **Other sites:** Could another site take over dispatch? What spare capacity, approvals, transport changes, and system access would be needed?

For each dependency, capture its owner, required availability, failure consequence, alternative, activation time, capacity, and evidence of testing.

## 5. Establish recovery requirements — 15 minutes

- At what point does interruption become unacceptable, and why? Record the proposed **maximum tolerable period of disruption**.
- What **recovery time objective** would restore dispatch before that point?
- What minimum dispatch volume or service level must be restored, and which orders take priority?
- What resources and dependency recovery times are needed to achieve that level?
- If electronic records are lost, how much data loss is tolerable, and how would orders, releases, and shipment records be reconstructed?
- How long would backlog clearance take after restart?
- Which manual or alternative arrangements are practical, and what limits or validation steps apply?

Distinguish required recovery targets from demonstrated capability. Record gaps where current arrangements cannot meet the proposed targets.

## 6. Close and validate — 5 minutes

Read back the activity scope, impact timings, proposed recovery targets, critical dependencies, and unresolved assumptions.

| Open point / evidence needed | Responsible person | Due date | Validation or approval required |
|---|---|---|---|
| | | | |

Confirm the approval route with the Site B site manager and relevant BCM owner. Keep findings provisional until Site B-specific facts, QA conclusions, and recovery assumptions have been validated.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md'"`
- command_execution: `/bin/bash -lc 'cat site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat impact-criteria.md'`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md'`
