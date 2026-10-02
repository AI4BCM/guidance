# /check-against-bia case 1c, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `9dcbe169-b917-4490-b72a-76d77077f013`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files, I need one answer from you.

**What class of data do these files hold, and is this environment approved for that class?**

Going by the file names, they likely contain BIA data (recovery times and resource requirements), recovery strategies, supplier dependencies and contract details for the trunking carrier, and possibly contact lists with personal data. The AI4BCM data rules (`units/data-rules.md`) class all of these as **high sensitivity**. High-sensitivity data may only be handled in an approved enterprise, private or corporate environment (`units/tools.md`, Selection guide, Implement and Analyse rows).

Please confirm one of these:
- The files are high sensitivity, and this Claude Code environment is approved for that class under your organisation's AI and information-classification rules. I'll go ahead.
- They're a lower class, such as anonymised or fictional material. Tell me which class.
- This environment isn't approved for them. In that case I'll stop here and won't read the files.

Until you answer, I won't open any of the files.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

# Dispatch plan checked against the BIA, and what the January trunking change reopens: draft for review

**Sources (versions and dates)**
- Compared against BIA v2, approved by top management on 4 Feb 2026. This is the extract for Site A chilled operations, owned by the BCM manager.
- Requirements register v5, 10 Feb 2026, approved by the BCM manager and built from BIA v2.
- From the chilled dispatch recovery plan v3, 12 Mar 2026, approved. Owner: Head of Logistics.
- From the chilled goods receipt recovery plan v2, 3 Mar 2026, approved. Owner: Warehouse lead.
- From the quality release recovery plan v1, 20 Feb 2026, approved. Owner: QA manager.
- From the change notice on the chilled trunking carrier, dated 15 Sep 2026. Status: planned, approved by the procurement board. Raised by the Head of Procurement.

**Reviewer:** you, as the BCM manager who asked, check each quoted passage. Each plan owner and each BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version. This draft changes nothing.

---

## Block 1: The dispatch plan against the BIA

This compares the chilled dispatch plan v3 with BIA v2, entry B-A2, and with the register v5. Every entry is **proposed, to confirm**. No replacement value is proposed, and neither recovery time is chosen.

| # | Item | Plan says (Head of Logistics) | BIA / register says | Result |
|---|---|---|---|---|
| 1 | **Recovery time** | Plan v3 §2, 12 Mar 2026: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA v2 B-A2, 4 Feb 2026: RTO "8 hours" (MTPD "24 hours"). Activity owner: Dispatch lead. | **Disagree.** The plan's 12 hours is longer than the BIA's 8-hour RTO. Put it to the Head of Logistics and the Dispatch lead. |
| 2 | **Resource: pickers** | Plan v3 §3, 12 Mar 2026: "A minimum of 3 pickers per shift travel to Site B." | BIA v2 B-A2, 4 Feb 2026: "at least 4 pickers per shift". Register v5 R-07, 10 Feb 2026: "Chilled dispatch: at least 4 pickers per shift". Owner: Dispatch lead. | **Disagree.** The plan has 3 pickers per shift where the BIA and the register have 4. Put it to the Head of Logistics and the Dispatch lead. |
| 3 | **Supplier: backup carrier** | Plan v3 §5, 12 Mar 2026: "Backup carrier: KuehlTrans, by spot booking." | BIA v2 B-A2, 4 Feb 2026: "carrier: NordFrost, no second carrier recorded". Register v5 R-08, 10 Feb 2026: "one carrier, NordFrost; second carrier open". **R-08 has no owner named.** | **Disagree.** The plan names a backup carrier that the BIA and the register don't record. Put it to the Head of Logistics, the Dispatch lead and the R-08 owner (not named, so to be confirmed). |
| 4 | Supplier: main carrier | Plan v3 §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | BIA v2 B-A2: "carrier: NordFrost". Register v5 R-08: "one carrier, NordFrost". | **Agree.** (Block 2 shows this changes on 1 Jan 2027.) |
| 5 | Contact: carrier escalation | Plan v3 §4: "Carrier escalation: NordFrost control room, 040 555 0900." | BIA v2 B-A2: "carrier escalation: NordFrost control room". | **Agree** on who to call. The BIA gives no number, so the number can't be compared: not in the sources. |
| 6 | Contact: duty manager | Plan v3 §4: "Duty manager, Site A: 040 555 0172." | Not in the sources (BIA v2 B-A2 holds no duty manager contact). | **Gap:** can't be compared. |
| 7 | Resource: warehouse system | Plan v3 §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | BIA v2 B-A2: "warehouse system LogiStock". Register v5 R-09: "LogiStock restored within 6 hours". Owner: IT service owner. | **Gap:** the plan states no recovery time for LogiStock, so R-09's 6 hours can't be compared. WI-14 wasn't attached. |

**Gaps (block 1)**
- Register v5 R-08 has no named owner.
- The plan doesn't say whether LogiStock must be available for the WI-14 manual export, and it gives no LogiStock recovery time.
- The BIA has no duty manager contact and no carrier escalation number, so the numbers in plan §4 can't be checked against it.
- BIA v2 is marked approved, so no unapproved BIA was used.

---

## Block 2: What the trunking carrier change reopens

The change notice (15 Sep 2026, planned) says that from 1 Jan 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, "moves from NordFrost to a new carrier, Polar Haul". It also says "NordFrost's control room will no longer handle Site A loads from that date." I searched only the attached set. Every entry is **proposed, to confirm**, with no replacement value.

| Document and section (date) | Line the change touches | Owner the sources name |
|---|---|---|
| Dispatch plan v3 §5 (12 Mar 2026) | "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | Head of Logistics |
| Dispatch plan v3 §4 (12 Mar 2026) | "Carrier escalation: NordFrost control room, 040 555 0900." The replacement escalation contact is not yet known. | Head of Logistics |
| Dispatch plan v3 §1 (12 Mar 2026), touched indirectly | "Recovery option: move chilled dispatch to Site B." This option depends on trunking from Site A to Site B, which moves to Polar Haul. | Head of Logistics |
| Goods receipt plan v2 §3 (3 Mar 2026) | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead |
| BIA v2 B-A1 (4 Feb 2026) | "carrier: NordFrost, inbound trunking from Site B" | Warehouse lead (activity); BCM manager (BIA) |
| BIA v2 B-A2 (4 Feb 2026) | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Dispatch lead (activity); BCM manager (BIA) |
| Register v5 R-08 (10 Feb 2026) | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | **No owner named** |

**Searched, not touched:** quality release plan v1 (no carrier or trunking line), BIA v2 B-A3, and register R-06, R-07 and R-09.

**Gaps (block 2)**
- Register R-08 has no named owner.
- The change notice is planned, not in effect. It was used only as the description of the change, not as the current state.
- The sources don't give a Polar Haul escalation contact (contact: to be confirmed).
- The sources don't say whether the KuehlTrans spot-booking backup in dispatch plan §5 still applies after the change.
- No intake questions were asked: the attachments answered everything that shapes the scope.
- None of the attached files contains text addressed to an AI.

**Coverage unknown.** The change could touch these kinds of document, but none was attached:
- contact lists and call trees that may hold the NordFrost control room number
- supplier contracts: the NordFrost contract and its end date, the Polar Haul contract, and any KuehlTrans spot-booking arrangement
- the supplier or third-party register and the risk register
- work instruction WI-14 and any LogiStock interfaces to the carrier
- Site B plans and any outbound or customer delivery plans
- role and action cards drawn from the dispatch or goods receipt plans
- the incident or crisis management plan
- the exercise schedule
- BIA entries outside this Site A chilled extract

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** run `units/prompts/review.md` on each plan this draft flags:
- the **chilled dispatch plan v3**, for three disagreements with the BIA and register (recovery time, pickers, backup carrier) and the carrier change
- the **chilled goods receipt plan v2**, for the carrier change
