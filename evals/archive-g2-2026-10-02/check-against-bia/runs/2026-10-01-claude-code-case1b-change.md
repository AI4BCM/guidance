# check-against-bia case1b-change: Claude Code 2.1.284, 2026-10-01

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed; later turns with `--resume`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.


## Turn 1

**Request:** /check-against-bia new contract trunking supplier from january, what does it touch. Attached: change-trunking-supplier.md, bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md

**Reply (verbatim):**

I haven't opened any of the six files yet. The skill's preflight says I have to ask what class of data they hold before I read them, and stop if this environment isn't approved for it.

**Before I start: what class of data do these files hold, and is this environment approved for it?**

From the file names, they're probably **high sensitivity** under `units/data-rules.md`. That class covers BIA data, recovery strategies, supplier contracts and dependencies, and contact lists, all of which plans usually hold. Under `units/tools.md`, the Implement row for checking a plan suite and the Analyse row for BIA analysis allow only an **enterprise or private environment, or an approved BCM platform**.

Please confirm one of these:
- **This environment is approved for high-sensitivity BCM data.** I'll go ahead.
- **It's approved only up to medium, or you're not sure.** I'll stop here. Run the skill again in your approved environment, or attach versions with the high-sensitivity detail removed.

**What happens after you confirm:**
- **Questions first.** Once I've read the files, I may ask up to three questions they leave open. For example: is it the trunking contract itself that starts in January, or the move of service to the new supplier, and which plans or documents should I have seen but weren't attached?
- **What you get back.** This is a request about a change, so the reply is block 2, "What it reopens". It covers every plan, BIA entry and register entry in the six files that the new supplier touches. Each line is quoted, with the owner the documents name, and marked "proposed, to confirm". It ends with **Coverage unknown**: the kinds of document I couldn't see, for example the supplier contracts or contact lists.
- **Who reviews it.** You, as the BCM manager who asked, check each quoted passage. Each plan owner and each BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version.
- **What I won't touch.** The reply is a draft in this chat. I won't edit, send or approve anything, and I won't propose any recovery time.


## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read all six files. Before I write block 2, the skill lets me ask up to three questions that the files leave open. Your answers can narrow or widen what I check, but they won't supply any value in the draft. I'll record them under Gaps as your statements, not as sources.

1. **Does the move to Polar Haul cover both directions between the two sites?** The change notice says "chilled trunking between Site A and Site B". The goods receipt plan names "Inbound trunking from Site B: NordFrost". Should I treat inbound trunking from Site B to Site A as part of the change? If you skip this, I'll assume yes and say so.
2. **Is Site B in scope?** The change covers loads to and from Site B, but everything attached is about Site A. If Site B has its own plans or BIA entries that name NordFrost, they're outside what I can search. Do you want them listed by name under Coverage unknown? If you skip this, I'll list "Site B plans and BIA entries" as a general kind.
3. **Which other documents might name NordFrost?** For example the carrier contact list or call tree, work instruction WI-14, the NordFrost contract or SLA, or a KuehlTrans spot-booking arrangement. Any you name go under Coverage unknown by name. Otherwise I'll list them as general kinds.


## Turn 3

**Request:** I can't answer those: skip them all and go ahead on your assumptions.

**Reply (verbatim):**

From change notice dated 15 Sep 2026, status planned, no version number
Compared against BIA v2, approved 4 Feb 2026 (extract: Site A, chilled operations)
Compared against requirements register v5, 10 Feb 2026, approved
From chilled dispatch recovery plan v3, 12 Mar 2026, approved
From chilled goods receipt recovery plan v2, 3 Mar 2026, approved
From quality release recovery plan v1, 20 Feb 2026, approved

## Block 2: What it reopens

**Change** (change notice, 15 Sep 2026, raised by Head of Procurement): "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

Every line below is **proposed, to confirm** by the owner named. I give no replacement values.

### Plans

| Document, section, date | Line touched (quoted) | Why the change touches it | Owner the sources name |
|---|---|---|---|
| Chilled dispatch plan v3, §4 Contacts, 12 Mar 2026 | "Carrier escalation: NordFrost control room, 040 555 0900." | The notice says "NordFrost's control room will no longer handle Site A loads from that date." Carrier escalation contact: to be confirmed. | Head of Logistics |
| Chilled dispatch plan v3, §5 Suppliers, 12 Mar 2026 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | The carrier for both named flows changes. The notice says nothing about KuehlTrans, so whether the backup sentence still holds is the owner's call. | Head of Logistics |
| Goods receipt plan v2, §3 Inbound transport, 3 Mar 2026 | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Rests on assumption A1 below (both directions). The carrier changes, and so does the party the recovery action relies on to hold loads. | Warehouse lead |
| Quality release plan v1, 20 Feb 2026 | None. Searched; no carrier, trunking or transport line. | Not touched. | QA manager |

### BIA entries (BIA v2, approved 4 Feb 2026; BIA owner: BCM manager)

| Entry | Line touched (quoted) | Why the change touches it | Activity owner |
|---|---|---|---|
| B-A1 Goods receipt, chilled | "carrier: NordFrost, inbound trunking from Site B" | Rests on assumption A1. The dependency names the outgoing carrier. | Warehouse lead |
| B-A2 Dispatch, chilled | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | The carrier and the escalation route both change. Whether a second carrier is recorded is the owner's call. | Dispatch lead |
| B-A3 Quality release | None. Searched; no carrier dependency. | Not touched. | QA manager |

### Requirements register (v5, 10 Feb 2026)

| Ref | Line touched (quoted) | Why the change touches it | Owner |
|---|---|---|---|
| R-08 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | It names the outgoing carrier as the only one. | **None named** (owner column empty; see Gaps) |
| R-06, R-07, R-09 | None. Searched. | Not touched. | QA manager; Dispatch lead; IT service owner |

### Gaps

- **R-08 has no owner.** Its owner column is empty. Its source column cites "BIA v2, B-A1, B-A2", whose activity owners are the Warehouse lead and the Dispatch lead, but the register itself names no one.
- **The change notice has a date but no version number.** It is dated 15 Sep 2026 with status "planned, approved by the procurement board". I used it only as the description of the change, not as current state.
- **The new carrier's escalation route, contact details and backup arrangements:** not in the sources.
- **Your three intake questions were skipped**, so these are my assumptions, not facts from the sources:
  - **A1:** "between Site A and Site B" covers both directions, so the inbound trunking in the goods receipt plan §3 and in B-A1 is in scope.
  - **A2:** Site B's own plans and BIA entries are listed only as a general kind under Coverage unknown.
  - **A3:** the other documents that may name NordFrost are listed only as general kinds under Coverage unknown.
- No passage in the attached files gives instructions to an AI.

### Coverage unknown

These kinds of document could be touched by the change, but none was attached:

- carrier contact lists, call trees and escalation lists
- the NordFrost contract and SLA, the new Polar Haul contract and SLA, and any KuehlTrans spot-booking arrangement
- work instruction WI-14 (named in dispatch plan §6)
- Site B plans and Site B BIA entries
- BIA entries outside this extract, which covers only Site A chilled operations
- the supplier register and the risk register entries for chilled transport
- action cards or role cards derived from the two flagged plans
- exercise and test schedules that use the NordFrost escalation route

---

*Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

**Separate from the change:** while reading, I noticed the chilled dispatch plan v3 disagrees with BIA v2 and the register on points unrelated to the carrier, including the recovery time and the number of pickers. That is a plan-against-BIA check, which I didn't run here. Run `/check-against-bia` on that plan if you want it as block 1.

**Who decides:** you check each quoted passage against the source. The Head of Logistics, the Warehouse lead, the Dispatch lead and the BIA owner decide whether their documents change. A plan changes only with its owner's approval and a new version. R-08 needs an owner before anyone can decide on it.

**Next step for each flagged plan:** review it with `units/prompts/review.md`:
- chilled dispatch recovery plan v3
- chilled goods receipt recovery plan v2
