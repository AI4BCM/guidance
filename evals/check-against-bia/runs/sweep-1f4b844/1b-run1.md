# /check-against-bia case 1b, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `98405639-9ccd-43c0-a543-7ab0f1ec7b15`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia New contract trunking supplier from january, what does it touch? The files change-trunking-supplier.md, bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md and plan-quality-release.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files, I need to settle one thing. The preflight asks this question by itself, before anything else.

**What class of data do these files hold, and is this environment approved for it?**

A BIA extract, a requirements register, recovery plans and a supplier change usually fall into the **high-sensitivity** class (`units/data-rules.md`, Sensitivity classes). That class covers BIA data, recovery strategies, supplier dependencies and contractual dependencies, plus contact lists if the plans name people. High-sensitivity material can only be processed in an approved enterprise, private or purpose-built BCM environment (`units/tools.md`, Selection guide, Implement and Analyse rows).

Please confirm one of these:
- **High sensitivity, and this Claude Code environment is approved for it.** I'll read the files and run the check.
- **Lower class**, for example fictional or training data. Tell me which, and I'll go ahead.
- **High sensitivity, but this environment isn't approved, or you're not sure.** I'll stop here and you can run the check in an approved environment.

Once that's settled, here's what happens next. The BCM manager who asked will check each quoted passage. Each plan owner and BIA activity owner will decide whether their document changes. The result is a draft in this chat only, and none of your files will be edited.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read all six files. I'm treating this as a **change** check: the change notice from 15 Sep 2026 is the subject, and I'll search the BIA v2 extract, requirements register v5 and the three plans for what it touches.

Before I write the draft, two things the files leave open:

1. **Does the change cover the inbound leg too?** The notice says "chilled trunking between Site A and Site B, and outbound chilled transport from Site A". It doesn't say whether that includes **inbound** trunking from Site B into Site A. That inbound leg is what B-A1 and the goods receipt plan rely on ("Inbound trunking from Site B: NordFrost"). Do you want me to read it as covering both directions, or only Site A → Site B and outbound?
2. **Is this the whole set to search, or do you have more?** Possible extras are a contact list or escalation directory, the NordFrost or Polar Haul contracts, work instruction WI-14, the approved recovery strategy, or a KuehlTrans spot-booking arrangement. If they stay out, I'll list each one under **Coverage unknown**.

If you skip a question, I'll say what I assumed under Gaps. For question 1, I'd assume both directions are affected and flag that as an assumption. Your answers can change the scope of the check but won't fill in any values.

## Turn 3

**Request:** skip

**Reply (verbatim):**

**Draft. Nothing has been edited, sent or approved.**

- Change: "Change notice: chilled trunking carrier", dated 15 Sep 2026, status "planned, approved by the procurement board". It has no version number (see Gaps).
- Compared against BIA v2, approved 4 Feb 2026 (extract: Site A, chilled operations).
- Requirements register v5, 10 Feb 2026, approved.
- Chilled dispatch recovery plan v3, 12 Mar 2026, approved.
- Chilled goods receipt recovery plan v2, 3 Mar 2026, approved.
- Quality release recovery plan v1, 20 Feb 2026, approved.

**Reviewer:** the BCM manager checks each quoted passage below. Each plan owner and BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version.

Block 1 (Against the BIA) was not run because the input is a change only.

---

## Block 2: What it reopens

**The change** (change notice, 15 Sep 2026): "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

### Plans

| # | Document, section, date | Line the change touches | Owner the sources name | Status |
|---|---|---|---|---|
| P1 | Chilled dispatch plan v3, §4 Contacts, 12 Mar 2026 | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics | proposed, to confirm |
| P2 | Chilled dispatch plan v3, §5 Suppliers, 12 Mar 2026 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics | proposed, to confirm |
| P3 | Goods receipt plan v2, §3 Inbound transport, 3 Mar 2026 | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead | proposed, to confirm. Rests on the assumption that the inbound leg is in scope (Gaps 1) |

The quality release plan v1 (§1 to §3) was searched and the change touches no line in it.

### BIA entries (BIA v2, approved 4 Feb 2026; BIA owner: BCM manager)

| # | Entry | Line the change touches | Activity owner | Status |
|---|---|---|---|---|
| B1 | B-A2 Dispatch, chilled, Resources and dependencies | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Dispatch lead | proposed, to confirm |
| B2 | B-A1 Goods receipt, chilled, Resources and dependencies | "carrier: NordFrost, inbound trunking from Site B" | Warehouse lead | proposed, to confirm. Rests on the assumption that the inbound leg is in scope (Gaps 1) |

B-A3 Quality release was searched and the change touches no line in it.

### Register entries (requirements register v5, 10 Feb 2026)

| # | Ref | Line the change touches | Owner the sources name | Status |
|---|---|---|---|---|
| R1 | R-08 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" (Source: "BIA v2, B-A1, B-A2") | **None named.** Owner: to be confirmed (Gaps 2) | proposed, to confirm |

R-06, R-07 and R-09 were searched and the change touches none of them.

None of the lines above has a replacement value. Two examples: the carrier escalation contact (to be confirmed) and the carrier for each leg (to be confirmed by each owner).

### Gaps

1. **Intake question 1 was skipped; I assumed both directions.** The change says "between Site A and Site B", which I read as covering inbound trunking from Site B as well. P3 and B2 rest on that reading. If only Site A → Site B and outbound move, P3 and B2 may drop out.
2. **Intake question 2 was skipped; I assumed these six files are the whole set.** Everything outside them is under Coverage unknown.
3. **R-08 has no named owner.** The Owner column is blank in register v5.
4. **The change notice has no version number.** It carries only a date (15 Sep 2026) and the status "planned, approved by the procurement board". I treated it as a planned change, not as current fact. It says "Raised by: Head of Procurement".
5. **The change notice is silent on these points (not in the sources):**
   - Polar Haul's escalation route or control room.
   - Whether a second or backup carrier is part of the new contract.
   - Whether the KuehlTrans spot-booking backup (P2) stays in place.
   - Whether Polar Haul's service covers the plan's relocation of chilled dispatch to Site B. The chilled dispatch plan v3, §1, says: "Recovery option: move chilled dispatch to Site B."
6. **No passage addressed to an AI was found** in any attached file.

### Coverage unknown

These kinds of document could be touched by the change but are not in the attached set:

- contact lists and escalation directories, including any copy of the NordFrost control room number
- the NordFrost contract (exit or notice terms) and the new Polar Haul contract or SLA
- any KuehlTrans spot-booking arrangement
- the supplier register or supplier risk records for chilled carriers
- the approved recovery strategy from the design stage, for the relocation to Site B
- Site B plans, for dispatch and receiving
- action cards and role cards taken from the two plans flagged above
- risk register entries on carrier dependency
- the exercise or test schedule, if a carrier escalation test is planned
- work instruction WI-14 and any carrier booking interface with LogiStock

---

**Next step:** use [`units/prompts/review.md`](units/prompts/review.md) on each flagged plan:
- the **chilled dispatch plan v3** (Head of Logistics), for P1 and P2
- the **chilled goods receipt plan v2** (Warehouse lead), for P3, once Gaps 1 is settled

Parts of this document were drafted with AI support (/check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
