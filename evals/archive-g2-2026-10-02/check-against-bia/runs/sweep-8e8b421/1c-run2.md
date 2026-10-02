# /check-against-bia case 1c, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `11df7852-34d9-45a6-841e-da532d2e35f6`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six attachments, I need to know one thing about them.

**What class of data do they hold, and is this environment approved for it?**

BIA extracts, recovery requirements, supplier dependencies and contact lists in plans are usually **high-sensitivity** data under the AI4BCM data rules (`units/data-rules.md`, Sensitivity classes). For an Implement-stage check like this one, the selection guide (`units/tools.md`) says high-sensitivity data may only go into an approved enterprise or private environment.

Please confirm one of these:

1. **High-sensitivity, and this Claude Code environment is approved for it** by your organisation. I'll read the files and go ahead.
2. **Lower sensitivity:** for example, the files are anonymised, fictional or training material. Tell me which, and I'll go ahead.
3. **High-sensitivity, and this environment is not approved.** I'll stop here and not open the files. You can run the skill again in an approved environment.

Once you answer, I'll read the six files. If anything is still unclear after that, I'll ask at most three intake questions. Then I'll write the draft in two parts:
1. **Against the BIA:** the chilled-dispatch plan compared with the BIA and the requirements register.
2. **What it reopens:** what the January trunking carrier change touches across the plans, BIA and register you attached, with a list of the document types I couldn't check.

**Reviewer:** you, as the BCM manager, check every quoted passage. Each plan owner and each BIA activity owner decides whether their own document changes. I won't edit any file.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources (version and date):**
- Compared against BIA v2, approved by top management 4 Feb 2026 (extract: Site A, chilled operations)
- Requirements register v5, 10 Feb 2026, approved by the BCM manager, built from BIA v2
- Chilled dispatch recovery plan v3, 12 Mar 2026, approved
- Chilled goods receipt recovery plan v2, 3 Mar 2026, approved
- Quality release recovery plan v1, 20 Feb 2026, approved
- Change notice "chilled trunking carrier", dated 15 Sep 2026, planned and approved by the procurement board. **It has no version number**, so it is listed under Gaps.

The attachments answered everything I would have asked, so I asked no intake questions. None of the files contains instructions aimed at an AI.

---

## Block 1: Against the BIA (chilled dispatch plan v3)

Every row is **proposed, to confirm**. Neither value is chosen and no replacement is proposed.

| # | Item | Plan passage (Head of Logistics) | BIA / register passage | Owners the sources name | Result |
|---|---|---|---|---|---|
| 1 | Recovery time | Plan v3, 12 Mar 2026, §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA v2, 4 Feb 2026, B-A2: MTPD "24 hours", RTO "8 hours" | Plan: Head of Logistics. BIA activity: Dispatch lead. BIA: BCM manager | **Disagree** |
| 2 | Staffing | Plan v3, §3: "A minimum of 3 pickers per shift travel to Site B." | BIA v2, B-A2: "at least 4 pickers per shift". Register v5, 10 Feb 2026, R-07: "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics. B-A2 and R-07: Dispatch lead | **Disagree** |
| 3 | Supplier (second carrier) | Plan v3, §5: "Backup carrier: KuehlTrans, by spot booking." | BIA v2, B-A2: "carrier: NordFrost, no second carrier recorded". Register v5, R-08: "one carrier, NordFrost; second carrier open" | Plan: Head of Logistics. B-A2: Dispatch lead. R-08: **no owner named** | **Disagree** |
| 4 | Supplier (main carrier) | Plan v3, §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | BIA v2, B-A2: "carrier: NordFrost". Register v5, R-08: "one carrier, NordFrost" | As in row 3 | Agree |
| 5 | Contact (carrier escalation) | Plan v3, §4: "Carrier escalation: NordFrost control room, 040 555 0900." | BIA v2, B-A2: "carrier escalation: NordFrost control room" | Plan: Head of Logistics. B-A2: Dispatch lead | Party agrees. The BIA gives no number, so the number can't be compared. |
| 6 | Contact (duty manager) | Plan v3, §4: "Duty manager, Site A: 040 555 0172." | Not in the sources (the BIA and register name no duty manager) | Plan: Head of Logistics | No comparison possible |
| 7 | System resource | Plan v3, §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | BIA v2, B-A2: "warehouse system LogiStock". Register v5, R-09: "LogiStock restored within 6 hours" | Plan: Head of Logistics. R-09: IT service owner | The plan has the system and a workaround. **The plan sets no restore time**, so R-09's "6 hours" has nothing to compare against. Recorded as a gap, not a disagreement. |

**Gaps (block 1)**
- R-08 names no owner, so nobody is named to answer row 3 on the register side.
- The plan dates the contacts in §4 only by the plan date (12 Mar 2026). The sources don't give a separate date for when the contact data was checked.
- WI-14 is not attached, so I couldn't check the manual export against the BIA.
- I saw only an extract of BIA v2. Entries outside Site A chilled operations were not checked.
- The plan's scope ("more than two hours") and recovery option ("move chilled dispatch to Site B") don't appear in the BIA extract, so there was nothing to compare them with. The approved strategy document is not attached.

---

## Block 2: What it reopens (new trunking carrier from 1 Jan 2027)

The change notice, dated 15 Sep 2026, says chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves "from NordFrost to a new carrier, Polar Haul" from 1 January 2027. It also says "NordFrost's control room will no longer handle Site A loads from that date."

I searched only the attached set. Every row is **proposed, to confirm**, with no replacement value.

| Document and section, with date | Line touched | Owner the sources name |
|---|---|---|
| BIA v2, 4 Feb 2026, B-A1 (Goods receipt, chilled) | "carrier: NordFrost, inbound trunking from Site B" | Activity: Warehouse lead. BIA: BCM manager |
| BIA v2, 4 Feb 2026, B-A2 (Dispatch, chilled) | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Activity: Dispatch lead. BIA: BCM manager |
| Register v5, 10 Feb 2026, R-08 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | **No owner named** |
| Dispatch plan v3, 12 Mar 2026, §4 Contacts | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Dispatch plan v3, 12 Mar 2026, §5 Suppliers | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics |
| Goods receipt plan v2, 3 Mar 2026, §3 Inbound transport | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead. The action itself sits with the dispatch lead. |

- **Searched, nothing touched:** BIA B-A3, register R-06, R-07 and R-09, and the quality release plan v1 (§1–§3). None of them names NordFrost, a carrier or trunking.
- **Carrier escalation contact after 1 Jan 2027:** to be confirmed. It is not in the sources.
- **KuehlTrans after the change:** not in the sources. The change notice doesn't mention it as a backup carrier.

**Gaps (block 2)**
- The change notice has no version number. It is a planned change (approved by the procurement board, raised by the Head of Procurement), so it is not used as current state anywhere above.
- R-08 names no owner.

**Coverage unknown.** The change could touch these kinds of documents, but none were attached:
- Contact lists, call-out trees and escalation routes outside the plans
- Supplier contracts: the NordFrost exit terms and the Polar Haul contract, including any recovery or control-room obligations
- The supplier register and the risk register, including supplier concentration
- The rest of the BIA (Site B entries and other sites that NordFrost serves)
- Site B's own plans, since dispatch recovers to Site B
- Work instructions, including WI-14
- The approved recovery strategy from the design stage
- Any agreement with KuehlTrans
- The partner-lab agreement QA-03, in case it relies on chilled transport
- The incident and crisis management plan
- The exercise schedule

---

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next steps.** As BCM manager, you check each quoted passage. Each plan owner and BIA activity owner decides whether their document changes, and any change to a plan needs the owner's approval and a new version.

For each flagged plan, run [`units/prompts/review.md`](units/prompts/review.md):
- **Chilled dispatch plan v3** (Head of Logistics): blocks 1 and 2
- **Chilled goods receipt plan v2** (Warehouse lead): block 2

I haven't changed or sent any file.
