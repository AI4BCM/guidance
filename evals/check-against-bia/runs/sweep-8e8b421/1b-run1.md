# /check-against-bia case 1b, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `bb4ff244-9b72-4540-8813-67beb93d29fc`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia New contract trunking supplier from january, what does it touch? The files change-trunking-supplier.md, bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md and plan-quality-release.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files, I need one answer from you.

**What class of data do these attachments hold, and is this environment approved for it?**

From their names, the files probably include BIA data, recovery plans and supplier/contract dependencies. Under the AI4BCM data rules (`units/data-rules.md`, Sensitivity classes), all three of those are **high-sensitivity**. High-sensitivity data may only be used in an approved corporate or private environment. They may also hold contact lists or personal data, which are high-sensitivity too.

Please tell me:
- the class of data the six files hold (for example, high-sensitivity BIA, plan and supplier data, or a test or anonymised set), and
- whether this Claude Code environment is approved for that class.

If it isn't approved for that class, I'll stop here and you can run the check in an approved tool. If it is, I'll read the files and run the change check.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. I've read all six files. Before I write the check, I have three questions the files don't answer. Your answers only set the scope. Any name or number you give me won't be used as a replacement value.

1. **Direction of trunking.** The change notice says Polar Haul takes over "chilled trunking between Site A and Site B". Does that include **inbound** trunking from Site B into Site A? That's the NordFrost dependency in the goods receipt plan and BIA entry B-A1. Or does it only cover outbound from Site A?
2. **Backup carrier.** Does anything you know of, such as the new contract, change the **KuehlTrans** spot-booking backup in the chilled dispatch plan? Or do I treat it as outside the change notice?
3. **Other documents.** Do you have any of these to attach: a contact or escalation list, the NordFrost or Polar Haul contract or SLA, Site B plans, or work instructions such as WI-14? If not, I'll list each kind under **Coverage unknown**.

If you'd rather skip these, I'll assume both directions are in scope, treat KuehlTrans as unchanged, and search only the six files you attached. I'll record each of those as an assumption under Gaps.

## Turn 3

**Request:** skip

**Reply (verbatim):**

**Sources read**
- Change notice "chilled trunking carrier", dated 15 Sep 2026, status "planned, approved by the procurement board". It has **no version number**.
- BIA v2, approved 4 Feb 2026 (extract: Site A, chilled operations)
- Requirements register v5, 10 Feb 2026, approved
- Chilled dispatch recovery plan v3, 12 Mar 2026, approved
- Chilled goods receipt recovery plan v2, 3 Mar 2026, approved
- Quality release recovery plan v1, 20 Feb 2026, approved

**Reviewer:** the BCM manager checks each quoted passage below against its source. Each plan owner and BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version. This draft changes nothing.

---

## Block 2: What the change reopens

**The change:** *"From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."* (Change notice, 15 Sep 2026)

All seven entries below are still accurate until 31 Dec 2026. They go out of date on 1 Jan 2027.

| # | Document, section, date | Line the change touches (quoted) | Owner named in the sources | Status |
|---|---|---|---|---|
| 1 | Chilled dispatch plan v3, §4 Contacts, 12 Mar 2026 | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics (plan owner) | proposed, to confirm. Contact: to be confirmed |
| 2 | Chilled dispatch plan v3, §5 Suppliers, 12 Mar 2026 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | Head of Logistics | proposed, to confirm. Carrier: to be confirmed |
| 3 | Goods receipt plan v2, §3 Inbound transport, 3 Mar 2026 | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead (plan owner) | proposed, to confirm (relies on assumption A1). Carrier and hold-loads contact: to be confirmed |
| 4 | BIA v2, entry B-A1 Goods receipt, chilled, 4 Feb 2026 | "carrier: NordFrost, inbound trunking from Site B" | Warehouse lead (activity owner); BCM manager (BIA owner) | proposed, to confirm (relies on assumption A1) |
| 5 | BIA v2, entry B-A2 Dispatch, chilled, 4 Feb 2026 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Dispatch lead (activity owner); BCM manager (BIA owner) | proposed, to confirm |
| 6 | Requirements register v5, R-08, 10 Feb 2026 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | **No owner named** (see Gaps) | proposed, to confirm |
| 7 | Chilled dispatch plan v3, §1 Scope, 12 Mar 2026 | "Recovery option: move chilled dispatch to Site B." | Head of Logistics | proposed, to confirm. This line doesn't name a carrier, but the option depends on the Site A to Site B trunking that §5 assigns to NordFrost |

**Searched and not touched by the change:**
- Chilled dispatch plan v3: §2, §3 and §6 (LogiStock, WI-14). §5 says "Backup carrier: KuehlTrans, by spot booking", which I left untouched under assumption A2.
- Goods receipt plan v2: §1 and §2.
- Quality release plan v1: all sections. It names no carrier.
- BIA v2: entry B-A3.
- Requirements register v5: R-06, R-07 and R-09.

### Gaps
- **R-08 has no named owner.** The Owner column is empty, so nobody is named to decide on entry 6.
- **The change notice has no version number.** It is dated 15 Sep 2026 and its status is "planned". I treated it as the change under review, not as a current source for any value.
- **I only saw a BIA extract** (Site A, chilled operations). BIA entries outside it, for Site A or Site B, weren't searched.
- Entry 3 assigns the hold-loads request to the dispatch lead, inside the warehouse lead's plan. Both owners may need to confirm it.
- No passage in the attachments addressed an AI or gave instructions.
- **Assumptions from the skipped intake questions:**
  - A1: Polar Haul also takes over inbound trunking from Site B into Site A.
  - A2: The change doesn't affect the KuehlTrans spot-booking backup.
  - A3: Only the six attached files were searched.

### Coverage unknown
The change could touch these kinds of documents, but none were attached:
- contact and escalation lists, and call trees
- supplier contracts and SLAs (the NordFrost exit and the Polar Haul contract)
- the KuehlTrans spot-booking arrangement
- Site B recovery plans and Site B BIA entries
- work instructions for transport and loading, including any that cover carrier booking or hold requests
- role and action cards drawn from the dispatch or goods receipt plans
- risk register entries for single-carrier dependency
- exercise and test schedules that use NordFrost scenarios
- crisis communication templates that name the carrier

---

Parts of this document were drafted with AI support (check-against-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** the two flagged plans are the **chilled dispatch plan v3** (entries 1, 2 and 7) and the **goods receipt plan v2** (entry 3). For each of them, use [`units/prompts/review.md`](units/prompts/review.md) with its owner. Unless R-08 gets an owner first, nobody is named to decide on that entry.

I also noticed that the chilled dispatch plan disagrees with BIA v2 on points unrelated to this change:
- **Pickers:** the plan says "3 pickers per shift"; the BIA says "at least 4".
- **Recovery time:** the plan says "within 12 hours"; the BIA sets an RTO of "8 hours".
- **Backup carrier:** the plan names KuehlTrans; the BIA says "no second carrier recorded".

This run didn't check those. A plan check (block 1) of that plan would cover them.
