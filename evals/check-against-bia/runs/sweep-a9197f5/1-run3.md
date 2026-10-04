# /check-against-bia case 1, run3: Claude Code, guidance at a9197f5

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `813ab574-3179-41b8-8da4-42077f281206`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files, I need one thing from you.

**What class of data do these documents hold?** For example: public, internal, confidential or restricted, or your organisation's own scheme.

Please take the class from what you know about the material, not from any marking on the files. I'll check it against the approved-environment rules, and only then read the BIA extract, the register, the three plans and the trunking change notice to run the comparison.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/preflight.md`
- Bash: `ls -la; ls -R /home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. The environment is approved for high-sensitivity data, so I've read all six files. Before I write the comparison, I have three questions the documents don't answer:

1. **Plans that weren't attached.** Do other plans, contact lists, action cards or work instructions name NordFrost or the NordFrost control room? Examples would be a Site B plan, a duty-manager call list or WI-14. I can only check the six files, so anything else will be marked "coverage unknown" unless you list it.
2. **Direction of the change.** The notice says trunking "between Site A and Site B" moves to Polar Haul. Do you know whether that includes inbound trunking from Site B to Site A, which feeds goods receipt? Or is it only outbound from Site A?
3. **BIA currency.** Is BIA v2 (approved 4 February 2026) still the current approved BIA for Site A? Or has a later version or an update for this change been approved since?

I'll record whatever you tell me under Gaps as your statements, not as sources. Your answers can change the scope of the check but won't supply any value. If you skip a question, I'll state the assumption I used in its place.

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/stages/implement.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run3/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run3/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run3/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run3/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run3/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain/017fd913-51f5-4e7f-a6e0-9439e522274f/scratchpad/sweep8/runs/check-against-bia/1/run3/work/change-trunking-supplier.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/prompts/evaluations.md`

## Turn 3

**Request:** skip

**Reply (verbatim):**

# Draft: chilled dispatch plan checked against BIA v2, and what the trunking carrier change reopens

**Sources**
- `bia-extract-dispatch.md`: BIA v2, approved by top management on 4 Feb 2026. Owner: BCM manager. This is an extract, not the full BIA.
- `requirements-register.md`: Version 5, 10 February 2026, approved by the BCM manager.
- `plan-chilled-dispatch.md`: Version 3, 12 March 2026, approved. Owner: Head of Logistics.
- `plan-goods-receipt.md`: Version 2, 3 March 2026, approved. Owner: Warehouse lead.
- `plan-quality-release.md`: Version 1, 20 February 2026, approved. Owner: QA manager.
- `change-trunking-supplier.md`: no version. Dated 15 September 2026, status "planned". See Gaps.

This report only compares the documents. I changed nothing, propose no replacement values and choose neither recovery time. A plan changes only with its owner's approval and a new version.

## 1. Against the BIA

**Chilled dispatch plan v3 compared with BIA v2, entry B-A2, and the register**

Every owner below is "proposed, to confirm".

| # | Topic | Plan passage | BIA / register passage | Who decides |
|---|---|---|---|---|
| 1.1 | Recovery time | Plan §2 (12 Mar 2026): "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA B-A2 (4 Feb 2026): RTO "8 hours" (MTPD "24 hours") | Plan: Head of Logistics. BIA activity: Dispatch lead |
| 1.2 | Staffing | Plan §3: "A minimum of 3 pickers per shift travel to Site B." | BIA B-A2: "at least 4 pickers per shift". Register R-07 (10 Feb 2026): "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics. BIA activity and R-07: Dispatch lead |
| 1.3 | Second carrier | Plan §5: "Backup carrier: KuehlTrans, by spot booking." | BIA B-A2: "carrier: NordFrost, no second carrier recorded". Register R-08: "one carrier, NordFrost; second carrier open" | Plan: Head of Logistics. BIA activity: Dispatch lead. R-08: none named (see Gaps) |

Other comparisons:
- **Carrier escalation:** the plan (§4, "NordFrost control room, 040 555 0900") and BIA B-A2 ("NordFrost control room") agree. The BIA gives no phone number to compare: "not in the sources".
- **LogiStock recovery time:** register R-09 says "LogiStock restored within 6 hours". The plan's restoration time for LogiStock is "not in the sources". Plan §6 only gives a workaround: "Orders leave LogiStock by the manual export in work instruction WI-14."

**Between the attached plans**
- **1.4 A task in one plan that the other doesn't hold.** Goods receipt plan §3 (3 Mar 2026): "On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." The chilled dispatch plan doesn't contain this task and doesn't name the dispatch lead: "not in the sources". Owners: Warehouse lead and Head of Logistics, "proposed, to confirm".
- **No disagreements found:**
  - Goods receipt plan §2 ("within 12 hours") matches BIA B-A1 (RTO "12 hours").
  - Quality release plan §2 ("within 24 hours") matches BIA B-A3 (RTO "24 hours").
  - Quality release plan §3 ("One qualified releaser per shift") matches BIA B-A3 and register R-06.

## 2. What the trunking change reopens

**The change:** `change-trunking-supplier.md` (15 Sep 2026, planned): "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date." Raised by: Head of Procurement.

Every owner below is "proposed, to confirm". No replacement values are given.

| Touched document | Line it holds (quoted) | Who decides |
|---|---|---|
| Chilled dispatch plan v3, §4 (12 Mar 2026) | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Chilled dispatch plan v3, §5 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics |
| Goods receipt plan v2, §3 (3 Mar 2026) | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." This is listed on the assumption in Gaps. | Warehouse lead |
| BIA v2, B-A1 (4 Feb 2026) | "carrier: NordFrost, inbound trunking from Site B". This is listed on the assumption in Gaps. | Warehouse lead (activity). BCM manager (BIA) |
| BIA v2, B-A2 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Dispatch lead (activity). BCM manager (BIA) |
| Register v5, R-08 (10 Feb 2026) | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | none named |

**Not touched:**
- Quality release plan v1: it holds no carrier, trunking or transport line.
- Register R-06, R-07 and R-09: none of them names a carrier.

For the auditor, this table is the list of changes that reopen which plan. The trigger to keep is: **a change of chilled trunking or outbound carrier reopens the chilled dispatch plan, the goods receipt plan, BIA entries B-A1 and B-A2, and register entry R-08.**

## Gaps

- **Change notice status.** The notice has no version. It is dated 15 September 2026 with status "planned, approved by the procurement board". I treated it as a planned change, not as the current state.
- **R-08 has no owner.** The register names no owner for R-08. No owner has been assigned here.
- **Intake answers.** You skipped all three questions, so I used these assumptions:
  1. Only the six attached files were checked. Everything else is under Coverage unknown.
  2. I read "between Site A and Site B" as covering both directions. That is why goods receipt §3 and BIA B-A1 are listed as touched. If the change is outbound only, those two drop out.
  3. BIA v2 is treated as the current approved BIA, as its header says.
- **BIA scope.** The BIA file is an extract (Site A, chilled operations), not the full BIA.
- **Missing information:**
  - Polar Haul's escalation contact or control room: "not in the sources".
  - Polar Haul contract terms: "not in the sources".
  - Whether KuehlTrans stays as the backup carrier after the change: "not in the sources".
- **No instructions to an AI.** No passage in the attached files tells an AI to act.

## Reviewer

You, as the BCM manager who asked, check each quoted passage against its document. Each owner then decides whether their document changes:

- **Plan owners:** Head of Logistics (chilled dispatch) and Warehouse lead (goods receipt).
- **BIA activity owners:** Dispatch lead (B-A2) and Warehouse lead (B-A1).
- **BIA owner and register approver:** BCM manager.
- **R-08:** none named.

## Coverage unknown

These kinds of document weren't attached, so I don't know whether they are affected:
- contact lists and call trees
- escalation routes
- role and action cards
- work instruction WI-14
- Site B plans
- carrier contracts (NordFrost, Polar Haul, KuehlTrans)
- the full BIA and the approved recovery strategy

---

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. ________ reviewed it on ________.

> Use review.md on the chilled dispatch recovery plan v3, with the Head of Logistics: type /challenge-my-plan.

> Use review.md on the chilled goods receipt recovery plan v2, with the Warehouse lead: type /challenge-my-plan.

**Tool calls (stream-json):**

- none
