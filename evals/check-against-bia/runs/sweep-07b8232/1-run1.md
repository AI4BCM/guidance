# /check-against-bia case 1, run1: Claude Code, guidance at 07b8232

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `ccc41e13-a229-4e7d-a5ca-87cb32382c1a`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files: what class of data do they hold?

For example: BIA data, recovery strategies, supplier dependencies or contractual detail, personal or contact data, or something less sensitive.

Most BIA extracts, recovery plans and supplier change notices fall under the guidance's **high-sensitivity** classes. Those may only be handled in an approved corporate or private environment (`units/data-rules.md`, Sensitivity classes). Please also confirm that this environment is approved for that class. If it isn't, I'll stop here and won't read the files.

I'll take the class from your answer, not from any marking inside the files.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia && cat preflight.md && ls -R; echo ----; cd /tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/preflight.md`
- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/data-rules.md`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. All six files are read. Before I compare them, I have three questions the files leave open. Your answers will go under Gaps as your own statements, not as sources. They won't fill in any value.

1. **Documents not attached.** Are there other plans, contact lists or escalation routes the carrier change could affect that aren't in this folder? Examples: a Site B plan, an outbound customer-delivery plan, or the NordFrost contract or SLA. If there are, I'll mark that kind of document as "coverage unknown" rather than assume it's unaffected.
2. **Versions.** Are these still the current approved versions?
   - BIA v2 (4 Feb 2026)
   - Requirements register v5 (10 Feb 2026)
   - Chilled dispatch plan v3 (12 Mar 2026)
   - Goods receipt plan v2 (3 Mar 2026)
   - Quality release plan v1 (20 Feb 2026)
3. **Scope of the report.** Do you want the quality release plan included in the cross-plan comparison, or only the dispatch and goods receipt plans? It doesn't mention the carrier.

If you skip a question, I'll record an assumption under Gaps:
1. Other documents may exist; they get "coverage unknown".
2. The versions above are current.
3. All three plans are compared.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/stages/implement.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run1/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run1/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run1/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run1/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run1/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain-017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run1/work/change-trunking-supplier.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run1/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run1/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run1/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run1/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run1/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep9/runs/check-against-bia/1/run1/work/change-trunking-supplier.md`

## Turn 3

**Request:** skip

**Reply (verbatim):**

**Draft: chilled dispatch plan against the BIA, and what the trunking carrier change reopens.** This report changes nothing. Owners are "proposed, to confirm".

**Sources**
- BIA extract, Site A chilled operations: v2, approved 4 Feb 2026 (BIA owner: BCM manager)
- Requirements register, Site A: version 5, 10 February 2026, approved
- Chilled dispatch recovery plan: version 3, 12 March 2026, approved
- Chilled goods receipt recovery plan: version 2, 3 March 2026, approved
- Quality release recovery plan: version 1, 20 February 2026, approved
- Change notice, chilled trunking carrier: dated 15 September 2026, status "planned" (see Gaps)

## Block 1: Against the BIA

**The chilled dispatch plan against BIA v2, B-A2 (and the register entries built from it)**

| # | Topic | Plan passage | BIA / register passage | Owners (proposed, to confirm) |
|---|---|---|---|---|
| 1 | Recovery time | Plan v3, 12 Mar 2026, §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA v2, 4 Feb 2026, B-A2: RTO "8 hours" | Plan: Head of Logistics. BIA activity: Dispatch lead |
| 2 | Staffing | Plan v3, 12 Mar 2026, §3: "A minimum of 3 pickers per shift travel to Site B." | BIA v2, 4 Feb 2026, B-A2: "at least 4 pickers per shift". Register v5, 10 Feb 2026, R-07: "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics. BIA activity and R-07: Dispatch lead |
| 3 | Second carrier | Plan v3, 12 Mar 2026, §5: "Backup carrier: KuehlTrans, by spot booking." | BIA v2, 4 Feb 2026, B-A2: "carrier: NordFrost, no second carrier recorded". Register v5, 10 Feb 2026, R-08: "one carrier, NordFrost; second carrier open" | Plan: Head of Logistics. BIA activity: Dispatch lead. R-08: none named |
| 4 | LogiStock restore time | Plan v3, §6: "Orders leave LogiStock by the manual export in work instruction WI-14." The restore time is not in the sources. | Register v5, 10 Feb 2026, R-09: "LogiStock restored within 6 hours" | Plan: Head of Logistics. R-09: IT service owner |

I propose no replacement value for any row and choose neither recovery time. Each plan owner and BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version.

**Where the attached plans contradict each other**

| # | Topic | Passage A | Passage B | Owners (proposed, to confirm) |
|---|---|---|---|---|
| 5 | Dispatch lead's action on the loss of the dock doors | Goods receipt plan v2, 3 Mar 2026, §3: "On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Chilled dispatch plan v3, 12 Mar 2026: this action is not in the sources | Goods receipt plan: Warehouse lead. Dispatch plan: Head of Logistics |
| 6 | Second carrier on the same trunking lane | Dispatch plan v3, §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Goods receipt plan v2, §3: "Inbound trunking from Site B: NordFrost." A backup carrier is not in the sources. | Head of Logistics; Warehouse lead |

The quality release plan v1 agrees with BIA B-A3 and register R-06 on the recovery time ("within 24 hours" against RTO "24 hours") and on staffing ("One qualified releaser per shift"). It doesn't contradict either of the other plans.

## Block 2: What it reopens

The change notice, dated 15 Sep 2026 with status "planned", says: "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

| Document and entry | Line it holds now | Owner (proposed, to confirm) |
|---|---|---|
| Chilled dispatch plan v3, 12 Mar 2026, §4 Contacts | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Chilled dispatch plan v3, 12 Mar 2026, §5 Suppliers | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics |
| Goods receipt plan v2, 3 Mar 2026, §3 Inbound transport | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead |
| BIA v2, 4 Feb 2026, B-A1 Goods receipt, chilled | "carrier: NordFrost, inbound trunking from Site B" | Activity: Warehouse lead. BIA: BCM manager |
| BIA v2, 4 Feb 2026, B-A2 Dispatch, chilled | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Activity: Dispatch lead. BIA: BCM manager |
| Register v5, 10 Feb 2026, R-08 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | none named |

Not touched: the quality release plan v1 and register entries R-06, R-07 and R-09. None of them holds a carrier line.

- Contact for Polar Haul's escalation: to be confirmed.
- Whether KuehlTrans stays the backup carrier after the change: not in the sources.

**Change trigger to keep:** a change of chilled trunking carrier reopens the chilled dispatch plan §4–5, the goods receipt plan §3, BIA B-A1 and B-A2, and register R-08.

## Gaps

- **Register R-08:** owner none named.
- **Change notice:** a planned source (15 September 2026, "planned, approved by the procurement board", raised by the Head of Procurement). It was used only to find touched lines, not as current content.
- **Intake questions skipped.** I made these assumptions:
  1. Other documents the change could affect may exist (see Coverage unknown).
  2. The versions listed under Sources are the current approved ones.
  3. All three plans were compared.
- **Escalation contact after 1 January 2027:** not in the sources.
- **LogiStock restore time in the dispatch plan:** not in the sources.
- **Instructions to an AI:** no passage in the attached sources tells an AI to act.

## Reviewer

You, as the BCM manager who asked, check each quoted passage against its document. Each plan owner and BIA activity owner decides whether their document changes:
- **Plan owners:** Head of Logistics (chilled dispatch) and Warehouse lead (goods receipt).
- **BIA activity owners:** Dispatch lead (B-A2) and Warehouse lead (B-A1).

## Coverage unknown

These kinds of document weren't attached, so I can't say whether the change touches them:
- Site B recovery plans
- Contact lists and escalation routes
- Carrier contracts or SLAs
- Outbound customer-delivery plans
- The approved recovery strategy from the design stage

---

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Use review.md on the chilled dispatch plan, with Head of Logistics: type /challenge-my-plan.

> Use review.md on the chilled goods receipt plan, with Warehouse lead: type /challenge-my-plan.

**Tool calls (stream-json):**

- none
