# prepare-bia baseline (no skill loaded), run1: Codex, guidance at 88370c8

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a0fe7a-256f-7840-b5ab-6aa3ad336193`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’ll read the three files and use them to draft a Site B dispatch interview guide aligned with the impact criteria.

# Site B dispatch interview guide

**Purpose:** Establish how dispatch operates at Site B, assess the impact of an interruption over time, and identify recovery requirements and dependencies.

**Status:** Draft for validation with Site B. Site A’s approved activity list is a reference for questions; it does not establish Site B’s activities or dependencies.

**Interview lead:** BCM interviewer  
**Proposed participants:** Site B dispatch lead and representatives of the three shifts. Involve the warehouse lead, Site A QA representative and Site B site manager for relevant questions and validation. Confirm these roles: the Site B organisation chart is undated, unversioned and marked draft.  
**Suggested duration:** 75–90 minutes.

## 1. Confirm scope and ownership — 10 minutes

- What does “dispatch” cover at Site B? Walk through a shipment from receipt of the order to carrier handover and dispatch confirmation.
- Which products, customers and destinations are served? Does Site B handle chilled goods?
- Where do warehouse, dispatch and QA responsibilities start and end?
- Who owns dispatch, who acts as deputy, and who can authorise recovery decisions on each shift?
- Are there distinct dispatch activities with different deadlines or recovery needs that should be assessed separately?

**Capture:** Agreed activity boundaries, outputs, accountable owner, deputies, operating hours and shift differences.

## 2. Understand demand and deadlines — 10 minutes

- What are normal and peak dispatch volumes, shipment values and staffing levels?
- Which customer cut-offs, loading slots or delivery windows are binding? What happens when one is missed?
- What are Site B’s peak periods? Site A records weeks 49–52 and week 14 for dispatch; do these apply here?
- How much backlog can accumulate before storage capacity, product shelf life or delivery commitments become limiting?
- Does an interruption outside operating hours still affect the next dispatch window?

**Request evidence:** Volume reports, dispatch schedules, customer service commitments and peak staffing plans.

## 3. Assess interruption impacts over time — 20 minutes

**Scenario:** Dispatch at Site B stops completely while other activities initially remain available. Assess a normal period and a peak period separately, then consider partial capacity where it changes the result.

Use proposed checkpoints of **2, 4, 8, 24, 48 and 72 hours**, extending them or adding specific cut-offs as needed. These are interview prompts, not approved recovery targets.

Apply the approved impact criteria:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | Under EUR 10k a day | One customer complains | None |
| 2 | EUR 10k–100k a day | A key account is late | A report to the food authority |
| 3 | Over EUR 100k a day | A key account is lost | The authority stops production |

At each checkpoint, ask:

- What consequences occur, and when do they first occur?
- What is the estimated financial impact **per day**, and what supports that estimate? Record cumulative losses separately.
- Which customers are affected? When would a key account become late or potentially be lost?
- What circumstances could require a report to the food authority or cause the authority to stop production? Validate with QA.
- Would delayed dispatch cause spoilage, temperature-control problems, congestion or an upstream production stoppage?
- Which consequences become unacceptable to Site B, and why?

**Capture using this worksheet:**

| Elapsed time / missed cut-off | Operational consequence | Financial impact/day and level | Customer impact and level | Regulatory impact and level | Evidence / assumptions |
|---|---|---|---|---|---|

Record each impact dimension separately. The supplied criteria do not specify how to combine levels or which level defines an unacceptable impact; flag those decisions for validation.

## 4. Identify dependencies and alternatives — 15 minutes

- **QA:** The draft organisation chart says Site B is covered from Site A. What release or approval is required before dispatch? How is it communicated, including outside normal hours? What happens if Site A QA is unavailable?
- **Systems and data:** Which applications, interfaces and records support orders, stock, release status, labels and dispatch confirmation? Site A uses LogiStock; does Site B?
- **Site-to-site support:** Site A records that manual export to Site B is possible. What exactly is exported, how would Site B use it, and has this been tested? Does it help restore Site B dispatch?
- **Transport:** Which carriers does Site B use? Is NordFrost involved? Are alternatives contracted, available and suitable for the goods?
- **People and facilities:** What minimum skills, staffing, loading equipment, dock capacity, storage, power and communications are required?
- **Workarounds:** Can dispatch run manually or from another location? What capacity, duration, controls and constraints apply?

For each dependency, record its owner, availability requirement, single points of failure, alternative arrangements and evidence of testing. Site A’s lab, carrier and release dependencies are prompts to investigate, not confirmed Site B dependencies.

## 5. Establish recovery requirements — 15 minutes

- What is the **maximum tolerable period of disruption** before impacts become unacceptable? Link the answer to the impact assessment.
- What **recovery time objective** would restore dispatch early enough to avoid those impacts, allowing time for restart and backlog clearance?
- What minimum acceptable service must be restored—such as shipments per hour, percentage of normal capacity or priority customers?
- In what order should shipments resume, and who authorises prioritisation?
- How much data loss, if any, is tolerable? Which order, stock, QA and shipment records must be recovered or reconciled?
- How long would restarting and clearing the backlog take at the proposed recovery capacity?
- Are the proposed targets achievable with current resources and arrangements? What gaps remain?

Distinguish **required recovery targets** from **demonstrated current capability**. Treat untested workarounds as assumptions.

## 6. Close and validate — 5 minutes

Read back the agreed scope, earliest unacceptable impacts, proposed recovery targets, minimum service level and critical dependencies.

Record:

- Interview date, participants and roles.
- Evidence reviewed and outstanding requests.
- Unconfirmed assumptions, with an owner and due date for each.
- Recovery capability gaps and follow-up actions.
- The person responsible for validating the Site B assessment and confirming ownership.

**Expected output:** A draft Site B dispatch BIA record with evidence-based impact timing, proposed recovery requirements, dependencies and clearly assigned validation actions.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g '*.md'"`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md'`
- command_execution: `/bin/bash -lc 'cat site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat impact-criteria.md'`
