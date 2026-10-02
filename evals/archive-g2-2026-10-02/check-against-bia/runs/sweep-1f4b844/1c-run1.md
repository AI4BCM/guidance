# /check-against-bia case 1c, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `fab744cc-7fe4-4984-a237-8e7f2a96746b`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files, I need to know what kind of data they hold.

**What sensitivity class do these files fall under, and is this Claude Code environment approved for that class?**

From the file names, they probably include:
- **BIA data** (`bia-extract-dispatch.md`, `requirements-register.md`)
- **Recovery strategies and plan detail** (the three `plan-*.md` files)
- **Supplier dependencies and maybe contract terms** (`change-trunking-supplier.md`)
- possibly **contact lists or personal data** inside the plans

The AI4BCM data rules (`units/data-rules.md`) treat all of these as **high sensitivity**. That means they can only be worked on in an approved corporate or private environment, such as an enterprise licence with retention and access settings your organisation has signed off (`units/tools.md`, Selection guide, Implement row).

Please confirm one of these:
1. **Approved:** this environment is approved for high-sensitivity BCM data. I'll then read the files and run the check.
2. **Lower class:** the files are anonymised, fictional or training material. Tell me which class they actually are.
3. **Not approved:** I'll stop here, and you can run this check in an approved environment.

Once that's settled, here's what to expect. A **BCM manager** (presumably you, since you asked) checks every quoted passage. The plan owners and BIA activity owners each decide whether their own document changes. I'll return a draft in this chat and won't edit any of the files.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources read**
- Compared against **BIA v2** (Site A chilled operations extract), approved 4 Feb 2026
- **Requirements register v5**, 10 Feb 2026, approved
- **Chilled dispatch recovery plan v3**, 12 Mar 2026, approved
- **Chilled goods receipt recovery plan v2**, 3 Mar 2026, approved
- **Quality release recovery plan v1**, 20 Feb 2026, approved
- **Change notice "chilled trunking carrier"**, dated 15 Sep 2026, status planned. It has no version number, so it is also listed under Gaps.

**Reviewer:** you, as BCM manager, check each quoted passage below. Each plan owner and each BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version. This is a draft in chat only: I edited none of the files.

I asked no intake questions because the attachments and your request settle the scope. My assumptions are listed under Gaps.

---

## Block 1: Against the BIA (chilled dispatch plan v3)

Every row is **proposed, to confirm**. I propose no replacement values and pick neither side.

| # | Item | Plan v3 says | BIA v2 / register v5 says | Result | Owners to decide |
|---|---|---|---|---|---|
| 1 | **Recovery time** | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | B-A2: RTO "8 hours" (MTPD "24 hours") | **Disagree.** The plan's time is longer than the BIA RTO. | Head of Logistics (plan); Dispatch lead (B-A2) |
| 2 | **Staffing** | §3: "A minimum of 3 pickers per shift travel to Site B." | B-A2: "at least 4 pickers per shift"; R-07: "Chilled dispatch: at least 4 pickers per shift" | **Disagree** | Head of Logistics; Dispatch lead (B-A2 and R-07) |
| 3 | **Backup carrier** | §5: "Backup carrier: KuehlTrans, by spot booking." | B-A2: "carrier: NordFrost, no second carrier recorded"; R-08: "one carrier, NordFrost; second carrier open" | **Disagree.** The plan names a backup carrier; the BIA and register record none. | Head of Logistics; Dispatch lead (B-A2); R-08 has no owner (see Gaps) |
| 4 | Main carrier | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | B-A2: "carrier: NordFrost"; R-08: "one carrier, NordFrost" | Agree | n/a |
| 5 | Carrier escalation contact | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | B-A2: "carrier escalation: NordFrost control room" | The name agrees. The phone number is not in the BIA, so I can't check it. | Head of Logistics |
| 6 | Duty manager contact | §4: "Duty manager, Site A: 040 555 0172." | Not in the sources | Can't compare | Head of Logistics |
| 7 | System | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | B-A2: "warehouse system LogiStock"; R-09: "LogiStock restored within 6 hours" | The system name agrees. The plan gives no LogiStock restore time, so it can't be compared with R-09's 6 hours. WI-14 is not attached. | Head of Logistics; IT service owner (R-09) |
| 8 | Recovery location | §1: "move chilled dispatch to Site B" | Not in the sources | Can't compare | Head of Logistics; Dispatch lead |

**Gaps (block 1)**
- R-08 has no named owner. Its Owner cell is empty.
- The plan's activation threshold, §1 "for more than two hours", has nothing in the BIA to compare against.
- WI-14 and the contact list are not attached, so neither phone number could be checked.
- The plan doesn't say which BIA version it was built from.
- Assumptions, since I asked no questions:
  - BIA v2 is still the current approved BIA.
  - The extract shows all of B-A1 to B-A3.

---

## Block 2: What it reopens (Polar Haul from 1 Jan 2027)

The change notice says: "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul … NordFrost's control room will no longer handle Site A loads from that date."

I searched all five attached documents. Every row is **proposed, to confirm**, with no replacement values.

| Document | Line touched (quoted) | Why | Owner |
|---|---|---|---|
| Chilled dispatch plan v3, §4 (12 Mar 2026) | "Carrier escalation: NordFrost control room, 040 555 0900." | This escalation route stops working from 1 Jan 2027. | Head of Logistics |
| Chilled dispatch plan v3, §5 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | The named carrier changes. The notice doesn't say whether the KuehlTrans backup still applies. | Head of Logistics |
| Goods receipt plan v2, §3 (3 Mar 2026) | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | The carrier changes, and so does the party asked to hold loads. | Warehouse lead |
| BIA v2, B-A1 (4 Feb 2026) | "carrier: NordFrost, inbound trunking from Site B" | Recorded dependency | Warehouse lead |
| BIA v2, B-A2 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Recorded dependency and escalation route | Dispatch lead |
| Register v5, R-08 (10 Feb 2026) | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | The requirement names the outgoing carrier. | **No owner named** |

These were searched and are **not touched**:
- Quality release plan v1, all sections
- BIA B-A3
- Register entries R-06, R-07 and R-09

**Gaps (block 2)**
- R-08 has no named owner.
- The change notice has no version number. Its status is "planned, approved by the procurement board", so I treated it as a planned change, not current fact, until 1 Jan 2027.
- The notice doesn't cover the following ("not in the sources"):
  - Polar Haul's escalation contact or control room
  - whether a second or backup carrier is arranged
  - whether NordFrost keeps any other Site A role

**Coverage unknown:** these kinds of document could be touched but were not attached:
- contact lists and call trees, including the NordFrost control room number
- supplier contracts and SLAs for NordFrost (exit), Polar Haul (new) and the KuehlTrans spot booking
- the supplier or third-party register
- work instructions, including WI-14 and any carrier booking instructions
- role or action cards for the dispatch lead and the duty manager
- Site B plans and BIA entries, since the trunking runs between the two sites
- the rest of the BIA beyond this extract
- the risk register's supplier entries
- the exercise and test schedule

---

**Next step:** run [`units/prompts/review.md`](units/prompts/review.md) on each flagged plan:
- **chilled dispatch plan v3** (blocks 1 and 2), with the Head of Logistics
- **goods receipt plan v2** (block 2), with the Warehouse lead

> Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
