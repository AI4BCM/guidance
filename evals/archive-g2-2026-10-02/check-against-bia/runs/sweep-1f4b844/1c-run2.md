# /check-against-bia case 1c, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `74ed9a97-fbc0-4429-a5ec-2d0535c524db`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six attached files, I need one thing settled.

**What class of data do these files hold, and is this environment approved for it?**

From the file names, the set likely includes high-sensitivity material: BIA data, recovery strategies and requirements, and supplier dependencies (the trunking carrier change). Any contact lists inside the plans would add personal data. Under the AI4BCM data rules, that material may only be processed in an approved corporate or private environment.

Please tell me:
1. The classification of these files under your organisation's scheme (for example, confidential or internal).
2. Whether this Claude Code session is approved for that class.

If it is approved, I'll read the files and run the check. That means block 1 compares the chilled dispatch plan against the BIA, and block 2 lists what the January trunking carrier change reopens, followed by Coverage unknown. If it isn't approved, I'll stop here and won't open anything.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

From: BIA v2, approved by top management 4 Feb 2026 (extract: Site A, chilled operations) · requirements register v5, 10 Feb 2026 · chilled dispatch recovery plan v3, 12 Mar 2026 · chilled goods receipt recovery plan v2, 3 Mar 2026 · quality release recovery plan v1, 20 Feb 2026 · change notice "chilled trunking carrier", 15 Sep 2026 (status: planned).

**Reviewer:** you, as the BCM manager, check every quoted passage against its source. Each plan owner and each BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version. This is a draft in the chat, and I changed no file.

The files answered everything I would have asked, so I asked no intake questions. The assumptions this rests on are listed under Gaps.

---

## Block 1: Against the BIA, chilled dispatch plan v3

Every entry below is **proposed, to confirm**. I don't propose a replacement value for any of them, and I don't choose between the two recovery times.

| # | Item | Plan v3 says | BIA v2 / register v5 says | Owners to confirm |
|---|---|---|---|---|
| 1 | **Recovery time: disagrees** | §2, 12 Mar 2026: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA B-A2, 4 Feb 2026: RTO "8 hours" (MTPD "24 hours") | Plan: Head of Logistics · BIA B-A2: Dispatch lead |
| 2 | **Staffing: disagrees** | §3: "A minimum of 3 pickers per shift travel to Site B." | BIA B-A2: "at least 4 pickers per shift" · Register R-07, 10 Feb 2026: "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics · B-A2 and R-07: Dispatch lead |
| 3 | **Supplier: disagrees** | §5: "Backup carrier: KuehlTrans, by spot booking." | BIA B-A2: "carrier: NordFrost, no second carrier recorded" · Register R-08: "one carrier, NordFrost; second carrier open" | Plan: Head of Logistics · B-A2: Dispatch lead · R-08: **owner: not in the sources** |
| 4 | Main carrier: agrees | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | BIA B-A2: "carrier: NordFrost" | (none) |
| 5 | Carrier escalation: agrees | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | BIA B-A2: "carrier escalation: NordFrost control room" | The number itself is not in the BIA, so it can't be compared |
| 6 | **System recovery time: gap** | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." The plan sets no LogiStock restoration time. | Register R-09: "LogiStock restored within 6 hours" | Plan: Head of Logistics · R-09: IT service owner |
| 7 | Duty manager contact: no comparison | §4: "Duty manager, Site A: 040 555 0172." | Not in the sources (the BIA lists no contacts beyond the carrier escalation) | Plan: Head of Logistics |

**Gaps (block 1)**
- Register R-08 has an empty Owner field, so no owner is named for the carrier requirement.
- The plan owner ("Head of Logistics") is not the BIA activity owner for B-A2 ("Dispatch lead"). That isn't a disagreement, but disagreements 1–3 need both of them.
- The plan's contact numbers carry no date of verification of their own beyond the plan date of 12 Mar 2026.
- WI-14 is referenced but wasn't attached, so I couldn't check whether the manual export works without LogiStock in a way that is consistent with R-09.
- I asked no intake questions. The assumption is that BIA v2 is still the approved version and that no later plan or register version exists.

---

## Block 2: What it reopens, carrier change to Polar Haul from 1 Jan 2027

The change notice says: "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul… NordFrost's control room will no longer handle Site A loads from that date." (change notice, 15 Sep 2026, status "planned, approved by the procurement board", raised by Head of Procurement)

I searched only the six attached files. Every entry is **proposed, to confirm**, and none comes with a replacement value.

| Document | Section, date | Line it touches | Owner the sources name |
|---|---|---|---|
| Chilled dispatch plan v3 | §5, 12 Mar 2026 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | Head of Logistics |
| Chilled dispatch plan v3 | §4, 12 Mar 2026 | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Chilled goods receipt plan v2 | §3, 3 Mar 2026 | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead (the action falls to the dispatch lead) |
| BIA v2, B-A1 | 4 Feb 2026 | "carrier: NordFrost, inbound trunking from Site B" | Activity: Warehouse lead · BIA: BCM manager |
| BIA v2, B-A2 | 4 Feb 2026 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Activity: Dispatch lead · BIA: BCM manager |
| Register v5, R-08 | 10 Feb 2026 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | **Not in the sources** (Owner field empty) |

**Searched and not touched:**
- Quality release plan v1 names no carrier.
- BIA B-A3 is not affected.
- Register entries R-06, R-07 and R-09 are not affected.
- Chilled dispatch plan §5 "Backup carrier: KuehlTrans, by spot booking": the change doesn't mention KuehlTrans. Whether that backup arrangement still holds against a new main carrier is for the plan owner to decide.

**Gaps (block 2)**
- R-08 has no named owner.
- The change notice names no Polar Haul escalation contact or control room. The new value for every touched line is therefore "contact: to be confirmed" or "carrier: to be confirmed by owner".
- The change is planned, not yet in force, so I used it only as the trigger and never as the current state.

**Coverage unknown** (kinds of document the change could touch that weren't attached):
- contact lists and call trees, including duty and out-of-hours carrier numbers
- supplier contracts and SLAs: the NordFrost exit terms, the Polar Haul contract, and any KuehlTrans spot-booking arrangement
- work instructions, including WI-14 and any loading or booking instructions that name the carrier
- escalation routes and role or action cards drawn from the two touched plans
- Site B plans and documents, since Site B is the recovery location and the other end of the trunking
- the approved continuity strategy from the design stage, and supplier risk assessments
- system configuration, such as carrier master data in LogiStock or any transport booking tool
- exercise and test schedules that use NordFrost

---

**Next step:** run [`units/prompts/review.md`](units/prompts/review.md) on each flagged plan:
- **Chilled dispatch plan v3:** block 1, items 1, 2, 3 and 6, and block 2.
- **Chilled goods receipt plan v2:** block 2.

Parts of this document were drafted with AI support (check-against-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
