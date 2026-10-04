# /check-against-bia case 1, run3: Claude Code, guidance at 07b8232

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `225be3d6-37b4-4cfa-8a09-6f4f622fdb87`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the attached files: what data class do the dispatch plan, the BIA extract, the register and the trunking change notice hold (for example public, internal, confidential or restricted)? I'll check that this environment is approved for that class before I read them.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/stages/implement.md`
- Glob: `*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Draft: Site A chilled dispatch against BIA v2, and what the trunking carrier change reopens.** Report only. Nothing has been changed, written or sent.

**Sources**
- BIA extract, Site A chilled operations: BIA v2, approved by top management on 4 Feb 2026. BIA owner: BCM manager.
- Requirements register, Site A: version 5, 10 Feb 2026, approved by the BCM manager.
- Chilled dispatch recovery plan: version 3, 12 Mar 2026, approved. Plan owner: Head of Logistics.
- Chilled goods receipt recovery plan: version 2, 3 Mar 2026, approved. Plan owner: Warehouse lead.
- Quality release recovery plan: version 1, 20 Feb 2026, approved. Plan owner: QA manager.
- Change notice, chilled trunking carrier: dated 15 Sep 2026, **no version**, status "planned". See Gaps.

---

## 1. Against the BIA

Each line below quotes both passages. Owners are "proposed, to confirm". I propose no replacement value and choose neither recovery time.

**Chilled dispatch plan v3 (12 Mar 2026) against BIA v2, B-A2 (4 Feb 2026)**

| # | Topic | Plan says | BIA / register says | Owners (proposed, to confirm) |
|---|---|---|---|---|
| 1.1 | Recovery time | Plan §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA B-A2, RTO column: "8 hours" | Head of Logistics (plan); Dispatch lead (B-A2) |
| 1.2 | Staffing | Plan §3: "A minimum of 3 pickers per shift travel to Site B." | BIA B-A2: "at least 4 pickers per shift". Register R-07 (v5, 10 Feb 2026): "Chilled dispatch: at least 4 pickers per shift" | Head of Logistics (plan); Dispatch lead (B-A2, R-07) |
| 1.3 | Second carrier | Plan §5: "Backup carrier: KuehlTrans, by spot booking." | BIA B-A2: "carrier: NordFrost, no second carrier recorded". Register R-08: "one carrier, NordFrost; second carrier open" | Head of Logistics (plan); Dispatch lead (B-A2); R-08: none named |
| 1.4 | LogiStock recovery | Plan §6 names only the fallback: "Orders leave LogiStock by the manual export in work instruction WI-14." A LogiStock recovery time is not in the plan. | BIA B-A2 lists "warehouse system LogiStock" with no time. Register R-09: "LogiStock restored within 6 hours" | Head of Logistics (plan); Dispatch lead (B-A2); IT service owner (R-09) |

The carrier escalation route matches. Plan §4 says "NordFrost control room" and BIA B-A2 says "carrier escalation: NordFrost control room". The number "040 555 0900" is not in the BIA.

**Where the related plans contradict each other**

| # | Topic | Passage A | Passage B | Owners (proposed, to confirm) |
|---|---|---|---|---|
| 1.5 | Action given to the dispatch lead | Goods receipt plan v2 §3 (3 Mar 2026): "the dispatch lead asks NordFrost to hold inbound loads at Site B." | The dispatch plan v3 holds no such action: not in the sources. | Warehouse lead (goods receipt plan); Head of Logistics (dispatch plan) |
| 1.6 | Backup carrier for trunking between the sites | Dispatch plan v3 §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Goods receipt plan v2 §3: "Inbound trunking from Site B: NordFrost." A backup carrier is not in the sources. | Head of Logistics; Warehouse lead |

The quality release plan v1 agrees with BIA B-A3 on "24 hours" and with R-06 on "One qualified releaser per shift". Each disagreement goes to its two owners. Each plan owner and BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version.

---

## 2. What it reopens: Polar Haul from 1 January 2027

The change notice (15 Sep 2026, §1) says: "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul… NordFrost's control room will no longer handle Site A loads from that date."

This is the list of changes that reopen which plan. Each line is quoted as the source holds it, owners are "proposed, to confirm", and I give no replacement value.

| Document | Entry | Line it holds now | Owner (proposed, to confirm) |
|---|---|---|---|
| Chilled dispatch plan v3, 12 Mar 2026 | §4 Contacts | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Chilled dispatch plan v3, 12 Mar 2026 | §5 Suppliers | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics |
| Goods receipt plan v2, 3 Mar 2026 | §3 Inbound transport | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead |
| BIA v2, 4 Feb 2026 | B-A1 Goods receipt | "carrier: NordFrost, inbound trunking from Site B" | Warehouse lead (activity); BCM manager (BIA) |
| BIA v2, 4 Feb 2026 | B-A2 Dispatch | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Dispatch lead (activity); BCM manager (BIA) |
| Register v5, 10 Feb 2026 | R-08 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | none named (see Gaps) |

Missing values:
- Polar Haul escalation contact: to be confirmed. It is not in the sources.
- Whether KuehlTrans stays the backup carrier: not in the sources.

**Not touched in the attached material:**
- Quality release plan v1: no line names a carrier.
- BIA B-A3.
- Register R-06, R-07 and R-09.

---

## Gaps

- **Change notice:** dated 15 Sep 2026, but it has no version number. Its status is "planned, approved by the procurement board", raised by the Head of Procurement. It takes effect on 1 Jan 2027, so it is not used as current. Until then the sources still say NordFrost.
- **Register R-08 has no owner:** "none named". It is not inferred from any role.
- **R-09 traceability:** R-08 and R-09 cite "BIA v2, B-A2". The "6 hours" in R-09 does not appear in the BIA extract, which lists LogiStock with no time. Only an extract of BIA v2 is attached.
- **Your statements, not sources:** "high" data class, and this environment is approved for high.
- **Intake questions not asked.** My assumption is that the three attached plans are the related plans in scope. Other documents are listed under Coverage unknown.
- **Text telling an AI to act:** none found in the attached files.

## Reviewer

The BCM manager who asked checks each quoted passage. Each plan owner and BIA activity owner decides whether their document changes:
- Head of Logistics: dispatch plan
- Warehouse lead: goods receipt plan and B-A1
- Dispatch lead: B-A2 and R-07
- BCM manager: BIA and register
- IT service owner: R-09
- R-08: none named

## Coverage unknown

These kinds of document were not attached, so I can't say whether the change touches them:
- contact lists and call trees
- escalation routes and role or action cards
- Site B plans
- carrier contracts or SLAs with NordFrost, KuehlTrans and Polar Haul
- work instruction WI-14
- the crisis or incident management plan
- the IT / LogiStock recovery plan

---

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Use review.md on the chilled dispatch recovery plan, with the Head of Logistics: type /challenge-my-plan.

> Use review.md on the chilled goods receipt recovery plan, with the Warehouse lead: type /challenge-my-plan.

**Tool calls (stream-json):**

- Grep: `(?i)high|Sensitivity classes|Prompt injection`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run3/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run3/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run3/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run3/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run3/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run3/work/change-trunking-supplier.md`
- Grep: `(?i)AI helped`
