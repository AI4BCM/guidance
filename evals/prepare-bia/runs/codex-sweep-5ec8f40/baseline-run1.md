# prepare-bia baseline (no skill loaded), run1: Codex, guidance at 5ec8f40

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a0fec4-a024-78d0-b0d3-9ffe073fe4bd`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’ll read the three files and use them to draft a dispatch interview guide tailored to Site B.

**Site B dispatch interview guide — draft for validation**

Purpose: establish how dispatch operates at Site B, how disruption affects the business over time, and what is needed to restore a minimum acceptable service.

Interview the **Dispatch lead, Site B**, with input from the three shift leaders. Involve the Warehouse lead and the QA representative from Site A for relevant dependencies. Confirm who owns and approves the completed assessment.

The approved Site A activity list is a starting point for questions. Its systems, carriers, peak periods and workarounds have **not been confirmed for Site B**. Site B’s organisation chart is an undated, unversioned HR draft; verify roles and reporting lines during the interview.

1. **Confirm the activity and its boundaries**

   - What does Site B dispatch do, from receipt of an order or dispatch instruction through handover to the carrier?
   - Which products, customers and destinations are covered? Is all dispatch chilled?
   - Where do warehouse responsibilities end and dispatch responsibilities begin?
   - Who owns dispatch, who acts as deputy, and what decisions can each shift leader make?
   - Which steps require QA release? Who provides that release, and how is it communicated and recorded?

   **Record:** activity description, scope, accountable owner, deputy and key handoffs.

2. **Establish normal service and peak demand**

   - What volumes are dispatched per shift and day? What are the customer and carrier cut-off times?
   - Which customers or orders take priority, and why?
   - When does demand peak? Site A records weeks 49–52 and week 14 for dispatch; do these periods also apply to Site B?
   - What minimum staffing, skills, equipment and dock capacity are needed on each shift?
   - How much backlog can be absorbed, and how quickly can it be cleared after service resumes?

   **Record:** normal and peak volumes, deadlines, capacity constraints and minimum acceptable service, expressed in measurable terms.

3. **Assess the consequences of interruption over time**

   Consider dispatch being unavailable while other activities initially continue. Then explore partial loss of capacity and interruption during a peak period.

   Use time points that reflect Site B’s operating cycle—for example, the next dispatch cut-off, end of shift, 24 hours, 48 hours and subsequent days. These are interview prompts, not approved recovery targets.

   At each point, ask:

   - What financial loss arises per day, and what supports the estimate? Distinguish delayed revenue from permanent loss, spoilage, penalties and extra costs; avoid double counting.
   - Which customers are affected? When would a key account receive a late delivery or be lost?
   - Could disruption trigger a report to the food authority or an authority decision to stop production? What specific circumstances would cause this?
   - What happens to chilled stock, storage capacity, temperature control, traceability and upstream production?
   - When does the impact become unacceptable, and who has authority to validate that judgement?

   Apply the approved impact criteria:

   | Level | Financial | Customer | Regulatory |
   |---|---|---|---|
   | 1 | Under EUR 10k a day | One customer complains | None |
   | 2 | EUR 10k–100k a day | A key account is late | A report to the food authority |
   | 3 | Over EUR 100k a day | A key account is lost | The authority stops production |

   Record each category separately with evidence and uncertainty. Confirm boundary treatment at EUR 10k and EUR 100k and the rule for combining categories; the supplied criteria do not specify an overall scoring method. Capture food safety and operational consequences even where the table does not classify them directly.

4. **Identify dependencies and failure points**

   - **QA:** The draft chart says Site B is covered from Site A. Which dispatch steps depend on that support? Site A’s list places the lab only at Site A; does Site B require its results? What happens if release staff, the lab or communications are unavailable?
   - **Systems and data:** Which systems does Site B use? Site A uses LogiStock; does Site B also use it? What order, stock, release, label and shipment data are essential?
   - **Transport:** Which carriers serve Site B? Site A records NordFrost with no second carrier recorded; confirm Site B’s arrangements and any approved alternatives.
   - **People and facilities:** What skills, access, refrigeration, power, docks, handling equipment and communications are essential?
   - **Other activities:** Which activities supply dispatch, and which activities stop or become constrained when dispatch fails?

   **Record:** dependency, owner/contact, time until its loss affects dispatch, available substitute and evidence of availability.

5. **Test workarounds and recovery needs**

   - Can dispatch operate manually? For how long and at what capacity?
   - Site A records “manual export to Site B possible.” What is exported, in which direction, and can Site B receive and use it? Has this been tested?
   - Can another site, dock, shift or carrier take over? What capacity and activation time are confirmed?
   - How would manual operations preserve QA release, temperature control and traceability?
   - What must be restored first, and what is the minimum service required at that point?
   - What recovery time is needed before impacts become unacceptable, allowing time to clear backlog?
   - How much data loss can be tolerated, and how would missing records be reconstructed?

   **Record:** proposed recovery time, tolerable data loss where applicable, minimum resources, recovery sequence and workaround limitations. Treat untested alternatives as assumptions.

6. **Close and validate**

   Read back the activity scope, earliest unacceptable impacts, proposed recovery needs and critical dependencies. Separate confirmed facts from estimates and unresolved assumptions.

   Capture the assessment using this worksheet:

   | Disruption duration / missed deadline | Financial impact per day and level | Customer impact and level | Regulatory impact and level | Evidence / assumptions |
   |---|---|---|---|---|
   | To be completed in interview | | | | |

   Assign an owner and due date to each follow-up. Request supporting dispatch volumes, cut-off schedules, carrier agreements, QA procedures and workaround test records. Confirm the approval route with Site B management and record the guide’s date, version, interview participants and validation status.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g '*.md'"`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md'`
- command_execution: `/bin/bash -lc 'cat impact-criteria.md'`
- command_execution: `/bin/bash -lc 'cat site-b-org-chart.md'`
