# /check-against-bia case 1b, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `efaa34c7-48a8-4904-8678-26da9ab6c660`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia New contract trunking supplier from january, what does it touch? The files change-trunking-supplier.md, bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md and plan-quality-release.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files: what class of data do they hold, and is this environment approved for it?

The file names point to a BIA extract, a requirements register, three recovery plans and a supplier contract change. Under the AI4BCM data rules (`units/data-rules.md`, Sensitivity classes), that material is usually **high-sensitivity**. That class covers BIA data, recovery strategies, contact lists and supplier contractual dependencies. High-sensitivity material may only be handled in an approved corporate or private environment.

Please confirm one of these:
- **High-sensitivity, and this Claude Code environment is approved for it** by your information security function. I'll go ahead and read the files.
- **High-sensitivity, but this environment isn't approved, or you're not sure.** I'll stop here, and you can run the check in an approved environment.
- **Lower class** (for example sanitised or test data). Tell me the class and I'll go ahead.

Also, if any of the files contains passwords, keys or access tokens, remove them before I read it.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources read:**
- Change notice "chilled trunking carrier", dated 15 Sep 2026, status planned (approved by the procurement board)
- Compared against BIA v2 (Site A chilled operations extract), approved 4 Feb 2026
- Requirements register Site A v5, 10 Feb 2026, approved
- Chilled dispatch recovery plan v3, 12 Mar 2026, approved
- Chilled goods receipt recovery plan v2, 3 Mar 2026, approved
- Quality release recovery plan v1, 20 Feb 2026, approved

**Reviewer:** you, as BCM manager, check each quoted passage below against its source. Each plan owner and BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version. I have changed nothing.

---

## What it reopens

**The change**, from the change notice dated 15 Sep 2026: "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

The change reopens **two plans, two BIA entries and one register entry**. Everything below is proposed, to confirm, and gives no replacement values.

| # | Document, section, date | Line the change touches (quoted) | Owner the sources name | Status |
|---|---|---|---|---|
| 1 | BIA v2, entry B-A2 (Dispatch, chilled), 4 Feb 2026 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Activity owner: Dispatch lead. BIA owner: BCM manager | Proposed, to confirm |
| 2 | BIA v2, entry B-A1 (Goods receipt, chilled), 4 Feb 2026 | "carrier: NordFrost, inbound trunking from Site B" | Activity owner: Warehouse lead. BIA owner: BCM manager | Proposed, to confirm |
| 3 | Requirements register v5, R-08, 10 Feb 2026 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | **No owner named** (see Gaps) | Proposed, to confirm |
| 4 | Chilled dispatch plan v3, §4 Contacts, 12 Mar 2026 | "Carrier escalation: NordFrost control room, 040 555 0900." | Plan owner: Head of Logistics | Proposed, to confirm. The change notice says this control room "will no longer handle Site A loads" from 1 Jan 2027. Carrier escalation contact: to be confirmed |
| 5 | Chilled dispatch plan v3, §5 Suppliers, 12 Mar 2026 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Plan owner: Head of Logistics | Proposed, to confirm. Whether the KuehlTrans backup continues is not in the sources |
| 6 | Chilled goods receipt plan v2, §3 Inbound transport, 3 Mar 2026 | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Plan owner: Warehouse lead | Proposed, to confirm. The step is carried out by the dispatch lead, a role outside this plan's ownership |

**Searched with nothing found:**
- **BIA B-A3:** no carrier or transport mentioned.
- **Register R-06, R-07, R-09:** no carrier mentioned.
- **Quality release plan v1, §§1–3:** no carrier or transport mentioned. Whether samples travel to the partner lab under QA-03 by carrier is not in the sources.
- **Chilled dispatch plan v3, §§1–3 and §6:** no carrier named. §1, though, moves dispatch to Site B, and the plan does not say which carrier serves Site B after the move. That is a question for the Head of Logistics, not a confirmed touch.

**Gaps**
- **R-08 has no owner.** Its Owner column is blank, so nobody is named to confirm a change to it.
- **The change notice is planned, not current.** It was approved by the procurement board on 15 Sep 2026 and takes effect 1 Jan 2027. Until then, every NordFrost line above is still the approved content.
- **The change notice gives no Polar Haul control room, escalation contact or contract reference.** Not in the sources.
- **The change notice doesn't mention KuehlTrans or a second carrier.** So the register's "second carrier open" and the plan's backup line can't be settled from these sources.
- **Intake:** I asked no questions, because the attached set answered the scope.
- **Instructions aimed at an AI:** none found in the attached files.

**Coverage unknown.** These kinds of document could hold NordFrost lines but were not attached:
- Supplier contracts: the NordFrost exit or notice terms, the Polar Haul contract and SLA, any KuehlTrans spot-booking arrangement
- Contact lists, call trees and escalation directories holding the NordFrost control room number
- Work instructions and role or action cards, for example transport booking and hold-load steps. WI-14 was not attached either.
- Site B's plans and BIA entries, which cover the other end of the trunking
- The rest of the BIA beyond the Site A chilled extract
- The approved recovery strategy from the design stage, plus the risk register and supplier risk assessments
- Exercise and test schedules that use NordFrost in scenarios

*Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

**Outside this check:** while searching, I saw that the chilled dispatch plan v3 also differs from BIA B-A2 on three points:
- **Recovery time:** "within 12 hours" against an RTO of "8 hours"
- **Pickers per shift:** "3 pickers" against "at least 4 pickers"
- **Second carrier:** "Backup carrier: KuehlTrans" against "no second carrier recorded"

These are plan-against-BIA disagreements, not effects of the carrier change. If you attach that plan as the plan to check, I can run the plan check on it separately.

**Next step:** run `units/prompts/review.md` on each flagged plan: the chilled dispatch plan v3 (Head of Logistics) and the chilled goods receipt plan v2 (Warehouse lead).
