# /check-against-bia case 1b, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `3f1615d5-3b0b-411a-87ef-666d4668598d`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia New contract trunking supplier from january, what does it touch? The files change-trunking-supplier.md, bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md and plan-quality-release.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files, I need to know one thing first.

**What class of data do these attachments hold, and is this Claude Code session an approved environment for that class?**

From the file names, they probably include a BIA extract, a requirements register, recovery plans and a supplier contract change. The guidance this skill follows (`units/data-rules.md`, Sensitivity classes) rates all of those as **high-sensitivity**:

- BIA data
- recovery strategies
- contact lists
- supplier contractual dependencies

High-sensitivity data may only go into an approved corporate or private environment.

Please confirm one of these:

1. **Yes:** these files are high-sensitivity, and this environment is approved for that class. I'll then read the files and run the check.
2. **No, or not sure:** I'll stop here. Please check with information security or your data owner which tool is approved before going further.
3. **Lower class:** the files are actually a lower class (for example, sanitised or test data). Tell me which class, and I'll go ahead on that basis.

Once that's settled, the BCM manager who asked (you) checks every passage I quote. Each plan owner and each BIA activity owner decides whether their own document changes. What I give you will be a draft in the chat, and I won't edit any of the files.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources read**
- Change notice "Chilled trunking carrier", dated 15 Sep 2026, status "planned, approved by the procurement board". It has no version number (see Gaps).
- Checked against BIA v2 (extract: Site A, chilled operations), approved 4 Feb 2026.
- Requirements register: Site A v5, 10 Feb 2026.
- Plan: chilled dispatch v3, 12 Mar 2026.
- Plan: chilled goods receipt v2, 3 Mar 2026.
- Plan: quality release v1, 20 Feb 2026.

**Input:** a change, checked against the three attached plans, the BIA extract and the register. **Reviewer:** you, as BCM manager, check each quoted passage. Each plan owner and BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version. This is a draft: I changed nothing.

---

## Block 2: What it reopens

**The change**, from the change notice of 15 Sep 2026:
> "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

The change covers trunking in both directions between the sites, so it reaches inbound goods receipt as well as dispatch.

### BIA entries (BIA v2, approved 4 Feb 2026; BIA owner: BCM manager)

| Entry | Line touched (quoted) | Why it's touched | Activity owner | Status |
|---|---|---|---|---|
| B-A1 Goods receipt, chilled | "carrier: NordFrost, inbound trunking from Site B" | The carrier named is the one being replaced | Warehouse lead | proposed, to confirm |
| B-A2 Dispatch, chilled | "carrier: NordFrost, no second carrier recorded" | The carrier named is the one being replaced | Dispatch lead | proposed, to confirm |
| B-A2 Dispatch, chilled | "carrier escalation: NordFrost control room" | The change says this control room "will no longer handle Site A loads" | Dispatch lead | proposed, to confirm |

I searched B-A3 (quality release). It does not mention the carrier.

### Register entries (register v5, 10 Feb 2026)

| Ref | Line touched (quoted) | Owner | Status |
|---|---|---|---|
| R-08 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | **None named** (see Gaps) | proposed, to confirm |

I searched R-06, R-07 and R-09. None mentions the carrier.

### Plans

| Plan | Section and line touched (quoted) | Why it's touched | Plan owner | Status |
|---|---|---|---|---|
| Chilled dispatch v3, 12 Mar 2026 | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | The escalation route stops working for Site A loads from 1 Jan 2027 | Head of Logistics | proposed, to confirm |
| Chilled dispatch v3 | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | The carrier named is the one being replaced | Head of Logistics | proposed, to confirm |
| Chilled dispatch v3 | §1: "Recovery option: move chilled dispatch to Site B." | This recovery option uses the Site A to Site B trunking that §5 assigns to NordFrost. The owner judges whether it still holds with the new carrier | Head of Logistics | proposed, to confirm |
| Goods receipt v2, 3 Mar 2026 | §3: "Inbound trunking from Site B: NordFrost." | The carrier named is the one being replaced | Warehouse lead | proposed, to confirm |
| Goods receipt v2 | §3: "the dispatch lead asks NordFrost to hold inbound loads at Site B." | The recovery step is addressed to the outgoing carrier. The person who performs it (dispatch lead) is not the plan owner | Warehouse lead (step performed by the dispatch lead) | proposed, to confirm |

I searched the quality release plan v1. It does not mention a carrier or transport.

I propose no replacement value. The Polar Haul escalation contact is labelled "contact: to be confirmed", because it is not in the sources.

### Gaps
- **The change notice has no version number.** It is dated 15 Sep 2026 and its status is "planned", so I treated it as a proposed change, not current fact.
- **R-08 has no named owner.** The Owner column is blank.
- The Polar Haul control room or escalation contact is not in the sources.
- The sources do not say whether the backup carrier KuehlTrans (dispatch plan §5: "Backup carrier: KuehlTrans, by spot booking") is affected.
- The sources do not say whether NordFrost stays available in any role after 1 Jan 2027, for example as a fallback.
- The change notice does not say whether the new contract adds a second carrier. It describes a move from one carrier to another.
- I asked no intake questions because the attachments answered what the check needed. No answers of yours are used as sources.
- I found no embedded instructions to an AI in the attachments.

### Coverage unknown
The change could touch these kinds of documents, but none were attached:
- **Contact lists, call trees and escalation lists.** The NordFrost control-room number 040 555 0900 may appear outside the dispatch plan.
- **Supplier contracts:** the NordFrost contract (exit terms, end date), the new Polar Haul contract (service levels, control-room cover, recovery commitments) and the KuehlTrans spot-booking arrangement.
- **Supplier register and third-party or supplier risk records.**
- **Risk register entries** about the single-carrier dependency.
- **Approved continuity strategy (design stage)** where it assumes the NordFrost trunking.
- **BIA entries outside this extract**, for example Site B activities that receive or send the same trunking.
- **Site B plans**, which hold inbound loads and take over chilled dispatch.
- **Work instructions, action cards and role cards** derived from the two flagged plans.
- **Carrier-facing system links**, if any. The sources do not say whether booking or order transfer to the carrier runs through LogiStock.
- **Exercise and test schedule**, for testing the reopened plans with the new carrier.

---

**Outside this check:** while searching I noticed that dispatch plan v3 differs from BIA v2 in ways unrelated to the carrier change:
- **Recovery time:** the plan has "within 12 hours"; B-A2 has an RTO of "8 hours".
- **Pickers:** the plan has "A minimum of 3 pickers"; B-A2 and R-07 have "at least 4 pickers per shift".
- **Second carrier:** the plan has "Backup carrier: KuehlTrans"; B-A2 has "no second carrier recorded".

Checking a plan against the BIA (block 1) is a separate run. Ask if you want it.

**Next step:** run [`units/prompts/review.md`](units/prompts/review.md) on each flagged plan: **chilled dispatch v3** (Head of Logistics) and **chilled goods receipt v2** (Warehouse lead). The change takes effect on 1 Jan 2027, three months from today.

> Parts of this document were drafted with AI support (check-against-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
