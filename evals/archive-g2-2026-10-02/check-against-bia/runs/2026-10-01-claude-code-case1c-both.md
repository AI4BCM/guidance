# check-against-bia case1c-both: Claude Code 2.1.284, 2026-10-01

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed; later turns with `--resume`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.


## Turn 1

**Request:** /check-against-bia check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. Attached: bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md, change-trunking-supplier.md

**Reply (verbatim):**

I've read the skill's preflight. Before I open any of the six attachments, I need one answer from you.

**1. What class of data do these files hold, and is this environment approved for it?**

Under the AI4BCM data rules, BIA data, recovery strategies, supplier dependencies and contract details, and contact lists all count as **high-sensitivity**. High-sensitivity data may only be processed in an approved enterprise, private or corporate environment. From the file names, at least `bia-extract-dispatch.md`, `requirements-register.md` and `change-trunking-supplier.md` look like they fall in that class.

Please confirm:
- the class of data in the attachments (for example "high: internal BIA and supplier detail", or "low: a fictional or anonymised training set"), and
- that this Claude Code environment is approved for that class. That means retention, access and connector settings have been checked under *Before you approve a tool* in `units/tools.md`.

If the environment isn't approved for this class, I'll stop here and won't read the files.

**2. Who reviews the output:** you, as the BCM manager who asked, check every quoted passage. Each plan owner and each BIA activity owner decides whether their document needs to change. A plan only changes with its owner's approval and a new version.

**3. What you'll get:** a draft in this chat with two separate blocks:
- **Against the BIA:** the chilled dispatch plan compared with the BIA extract and the requirements register.
- **What it reads as reopened by the January trunking carrier change:** searched across the six attached files only, ending with a **Coverage unknown** list of document types I can't see.

I won't edit, send or approve anything. I also won't set any recovery time objective (RTO), recovery point objective (RPO) or maximum tolerable period of disruption (MTPD) values; those stay with their owners.

Once you've answered, I'll read the files. If they leave anything open, I'll ask you up to three questions before writing the draft.


## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources read and their versions:**
- BIA v2, approved by top management 4 Feb 2026 (`bia-extract-dispatch.md`, extract for Site A chilled operations)
- Requirements register v5, 10 Feb 2026, approved by the BCM manager (`requirements-register.md`)
- Chilled dispatch recovery plan v3, 12 Mar 2026, approved (`plan-chilled-dispatch.md`)
- Chilled goods receipt recovery plan v2, 3 Mar 2026, approved (`plan-goods-receipt.md`)
- Quality release recovery plan v1, 20 Feb 2026, approved (`plan-quality-release.md`)
- Change notice on the chilled trunking carrier, dated 15 Sep 2026, status *planned* (`change-trunking-supplier.md`)

I didn't ask any intake questions: the attached files settled the scope. This is a draft for you to review. I haven't changed anything in any document.

---

## Block 1: Chilled dispatch plan against the BIA

The chilled dispatch plan (v3) was approved after BIA v2 and register v5, but it disagrees with them in three places. Every result below is **proposed, to confirm**. I don't suggest replacement values.

| # | Item | What the plan says (Head of Logistics) | What the BIA and register say | Result |
|---|---|---|---|---|
| 1 | **Recovery time** | Plan v3, §2, 12 Mar 2026: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA v2, B-A2, 4 Feb 2026 (activity owner Dispatch lead; BIA owner BCM manager): RTO "8 hours", MTPD "24 hours" | **Disagree.** The plan's time is 4 hours longer than the BIA's RTO. It is still inside the MTPD. Choosing which figure is right is up to the owners. |
| 2 | **Staffing** | Plan v3, §3: "A minimum of 3 pickers per shift travel to Site B." | BIA v2, B-A2: "at least 4 pickers per shift". Register v5, R-07, 10 Feb 2026 (owner Dispatch lead): "Chilled dispatch: at least 4 pickers per shift" | **Disagree.** The plan has one picker fewer than both the BIA and the register. |
| 3 | **Second carrier** | Plan v3, §5: "Backup carrier: KuehlTrans, by spot booking." | BIA v2, B-A2: "carrier: NordFrost, no second carrier recorded". Register v5, R-08 (no owner named): "one carrier, NordFrost; second carrier open" | **Disagree.** The plan names a backup carrier that neither the BIA nor the register records. |
| 4 | Main carrier | Plan v3, §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | BIA v2, B-A2: "carrier: NordFrost". Register v5, R-08: "one carrier, NordFrost" | Match. |
| 5 | Carrier escalation contact | Plan v3, §4: "Carrier escalation: NordFrost control room, 040 555 0900." | BIA v2, B-A2: "carrier escalation: NordFrost control room" | The name matches. The phone number is not in the BIA or register, so it can't be checked here. |
| 6 | Duty manager contact | Plan v3, §4: "Duty manager, Site A: 040 555 0172." | Not in the BIA or register | Can't be compared. |
| 7 | System | Plan v3, §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | BIA v2, B-A2: "warehouse system LogiStock". Register v5, R-09 (owner IT service owner): "LogiStock restored within 6 hours" | The system matches. The plan gives no restore time for LogiStock, so R-09 can't be checked against it. WI-14 wasn't attached. |
| 8 | Activation trigger | Plan v3, §1: "Loss of Hall 3 (chilled dispatch) for more than two hours." | Not in the BIA or register | Can't be compared. |

**Gaps for Block 1**
- Register R-08 has no owner. Nobody is named to confirm item 3.
- The plan says it is "approved" but doesn't say who approved it.
- The strategy approved at the design stage, which the plan is meant to carry out, wasn't attached. I can't check whether moving dispatch to Site B, or using KuehlTrans, is part of an approved strategy.
- Work instruction WI-14 wasn't attached.
- The BIA file is an extract. I've treated B-A1 to B-A3 as the whole of BIA v2 for Site A chilled operations; the extract doesn't confirm this.

---

## Block 2: What the January carrier change touches

The change: from 1 Jan 2027, "chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul", and "NordFrost's control room will no longer handle Site A loads from that date". (Change notice, 15 Sep 2026, status planned, raised by the Head of Procurement.)

I searched all three plans, all three BIA entries and all four register entries. Every line below is **proposed, to confirm**. No replacement value is given: the sources name no escalation contact for Polar Haul ("contact: to be confirmed").

| Document | Line touched (quoted) | Owner named in the sources |
|---|---|---|
| BIA v2, B-A1, 4 Feb 2026 | "carrier: NordFrost, inbound trunking from Site B" | Warehouse lead (activity); BCM manager (BIA) |
| BIA v2, B-A2, 4 Feb 2026 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Dispatch lead (activity); BCM manager (BIA) |
| Register v5, R-08, 10 Feb 2026 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | **None named** |
| Chilled dispatch plan v3, §4, 12 Mar 2026 | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Chilled dispatch plan v3, §5 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | Head of Logistics |
| Chilled goods receipt plan v2, §3, 3 Mar 2026 | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead (this action is carried out by the Dispatch lead) |

**Searched and not touched:** BIA B-A3; register R-06, R-07 and R-09; the whole quality release plan v1. The KuehlTrans line in chilled dispatch plan §5 isn't changed by the notice's wording, because the notice doesn't mention a backup carrier.

**Gaps for Block 2**
- R-08 has no owner.
- The change notice is planned, not yet in effect. I've used it only as the change being assessed, not as the current state.
- Before 1 Jan 2027, the sources don't name a Polar Haul control room or any other escalation route.

**Coverage unknown.** These kinds of documents weren't attached, so I couldn't search them for this change:
- contact lists, call trees and escalation routes that may hold the NordFrost control room number
- supplier contracts and agreements: NordFrost exit terms, the Polar Haul contract, KuehlTrans spot-booking terms
- the supplier or third-party register, and supplier risk assessments
- the risk register
- the approved recovery strategy from the design stage
- work instructions, including WI-14 and any carrier-booking procedures
- Site B plans and BIA entries (Site B is at the other end of the trunking)
- BIA entries outside this extract
- the incident or crisis management plan
- transport quality or temperature agreements
- the exercise schedule

---

**Next step:** use [`units/prompts/review.md`](units/prompts/review.md) on each flagged plan: the **chilled dispatch plan v3** (Blocks 1 and 2) and the **chilled goods receipt plan v2** (Block 2). Each plan owner and each BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version.

> Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
