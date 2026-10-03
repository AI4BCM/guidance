# prepare-bia baseline (no skill loaded), run1: Codex, guidance at 4dc1660

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a0ff3d-e0d6-7d23-a798-de9674218f4b`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’ll read the three files and use them to draft a dispatch interview guide tailored to Site B.

# Site B dispatch interview guide

**Purpose:** Confirm how dispatch operates at Site B, assess the effects of disruption using the approved impact criteria, and identify recovery needs and dependencies.

**Suggested duration:** 60–75 minutes  
**Primary interviewee:** Dispatch lead, Site B  
**Contributors:** Shift leaders; warehouse lead and Site A QA representative for relevant interfaces. Confirm who approves Site B’s findings with the site manager.

## 1. Preparation and opening — 5 minutes

Use the attached documents with these qualifications:

| Source | How to use it |
|---|---|
| **Site A activity list**, v3, 12 March 2026; approved by Site A’s site manager | Prompts for comparison. Its activities, systems, carriers and peak periods are not confirmed for Site B. |
| **Impact criteria**, v1.1, 4 February 2026; approved by top management | Apply these criteria to Site B’s disruption impacts. |
| **Site B organisation chart**, undated, unversioned HR draft | Starting point for identifying interviewees and responsibilities; validate during the interview. |

Opening statement:

> “We want to understand Site B’s dispatch activities, how disruption affects them over time, and what is needed to restore an acceptable service. We will use Site A’s information as prompts and record Site B’s answers separately. Please distinguish confirmed facts from estimates and flag evidence we should obtain.”

Confirm:

- Are the dispatch lead and three shift leaders shown in the draft chart current?
- Who owns dispatch, acts as deputy, and authorises operational exceptions?
- Who can validate the impact estimates and approve recovery requirements?

## 2. Establish Site B’s dispatch scope — 10 minutes

Ask the interviewee to walk through a recent shipment, from receipt of the dispatch instruction to carrier handover and confirmation.

- What triggers dispatch, and when is the activity considered complete?
- Which steps does dispatch own? Where do warehouse, QA, carriers or other teams take over?
- Does Site B handle chilled food? What products, customers and destinations are covered?
- Are there separate dispatch activities with different deadlines, impacts or recovery needs?
- What are normal and peak volumes, shift patterns and shipment cut-off times?
- Which weeks or events create peaks? Site A lists weeks 49–52 and week 14; do these apply here?
- What backlog can be absorbed, and how quickly can it be cleared?

**Capture:** Agreed activity description, boundaries, accountable owner, operating hours, volumes and critical deadlines.

## 3. Assess disruption impacts over time — 20 minutes

Scenario:

> “Assume Site B cannot dispatch from the start of a normal operating shift. Assess the consequences as the interruption continues, then consider whether peak demand changes the result.”

Suggested checkpoints are **4 hours, 8 hours, 24 hours, 48 hours and 72 hours**. Adjust these to actual shipment cut-offs, shelf-life limits and other critical deadlines; extend the assessment if necessary.

Apply the approved criteria:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | Under EUR 10k a day | One customer complains | None |
| 2 | EUR 10k–100k a day | A key account is late | A report to the food authority |
| 3 | Over EUR 100k a day | A key account is lost | The authority stops production |

At each checkpoint, ask:

- What happens operationally? When do missed shipments, storage constraints or product losses begin?
- What is the financial impact **per day**? What supports the estimate—for example, lost margin, spoilage, penalties or extra transport costs?
- Which customers are affected? When would a key account become late or be at risk of being lost?
- What circumstances would require a food-authority report or lead to an authority stopping production? Obtain QA validation.
- How do these consequences change at peak demand?
- Which consequence first makes continued interruption unacceptable, and why?

Record financial, customer and regulatory levels separately. The supplied criteria do not define an overall scoring rule or an automatic threshold for unacceptable impact; flag these for confirmation.

| Elapsed interruption | Consequences and evidence | Financial EUR/day and level | Customer level | Regulatory level | Assumptions / validation needed |
|---|---|---|---|---|---|
| Relevant checkpoint | | | | | |

## 4. Establish recovery requirements — 10 minutes

- What is the **maximum tolerable period of disruption**: the point beyond which the consequences become unacceptable?
- What **recovery time objective** is needed to restore dispatch before that point?
- What minimum acceptable service must be restored—for example, shipments per shift, priority customers or product groups?
- What staff, equipment, information and capacity are required to deliver that service?
- How long would restoring service and clearing the backlog take?
- If dispatch records are lost, how much data loss is tolerable, and how could records be reconstructed?

Record recovery requirements separately from current recovery capability. Capture any gap, supporting rationale and owner responsible for validating it.

## 5. Confirm dependencies and workarounds — 15 minutes

| Topic | Interview prompts |
|---|---|
| **QA and release** | The draft chart says QA is covered from Site A. Does Site B require Site A release before dispatch? Who provides cover outside normal hours? What happens if Site A or its lab is unavailable? |
| **Systems and data** | Which systems support orders, stock, release status, labels and dispatch confirmation? Does Site B use LogiStock? What access, connectivity and records are essential? |
| **Transfers between sites** | Site A records a possible manual export to Site B. What does that export contain, who initiates it, and can Site B use it? Has the process been tested? |
| **Carrier** | Which carriers serve Site B? Site A records NordFrost with no second carrier; does this apply here? What alternatives have confirmed availability and capacity? |
| **Facilities and equipment** | Which loading areas, chilled storage, power supplies, handling equipment and temperature controls are essential? What constraints limit dispatch during disruption? |
| **People** | What minimum staffing and skills are needed per shift? Are there deputies and trained substitutes for critical tasks? |
| **Alternative arrangements** | Can dispatch move to another site or operate manually? What capacity, transport, QA checks, traceability controls and authorisations would be required? |

For each workaround, distinguish **suggested**, **documented** and **tested** capability. Record activation time, sustainable capacity, operating limits and evidence.

## 6. Close and validate — 5 minutes

Read back the proposed findings:

- Dispatch scope and ownership.
- Impact progression and first unacceptable consequence.
- Maximum tolerable disruption, recovery target and minimum service.
- Critical dependencies and feasible workarounds.
- Uncertainties, evidence requests and capability gaps.

Assign an owner and due date to each follow-up. Request relevant shipment and volume records, customer deadlines, QA procedures, carrier arrangements, system recovery information and workaround test results.

**Interview output:** A draft Site B dispatch BIA record for validation, with Site B facts, estimates and unresolved assumptions clearly identified.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g '*.md'"`
- command_execution: `/bin/bash -lc 'cat site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md'`
- command_execution: `/bin/bash -lc 'cat impact-criteria.md'`
