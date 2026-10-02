# /check-against-bia case 1b, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `9525bb4f-261f-474c-8e94-536bfb9e2903`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia New contract trunking supplier from january, what does it touch? The files change-trunking-supplier.md, bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md and plan-quality-release.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files: **what class of data do they hold, and is this environment approved for it?**

From the file names, they look like a BIA extract, a requirements register, three continuity plans and a supplier change. Under the AI4BCM sensitivity classes (`units/data-rules.md`), several of those are **high-sensitivity**:

- BIA data and risk assessment detail
- recovery strategies and design assumptions
- supplier weaknesses and contractual dependencies
- contact lists and personal data, which plans often contain

High-sensitivity material may only go into an approved corporate or private environment. Please tell me:

1. Which class the attachments fall into (high-sensitivity, or something lower such as internal or public).
2. Whether this Claude Code session is approved by your organisation for that class.

If they're high-sensitivity and this environment isn't approved for it, I'll stop here and won't open them. If it is approved, I'll read the six files and run the change check (Task choice 3), with no plan-vs-BIA block unless you want one too. The check covers what the trunking supplier change reopens in the attached plans, BIA entry and register, with each line quoted and its owner named. It also gives a **Coverage unknown** list for document types not attached, such as contracts and contact lists.

**Reviewer:** you, as the BCM manager who asked, check each quoted passage. Each plan owner and BIA activity owner decides whether their document changes. I'll write nothing to any file.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

from change notice "chilled trunking carrier", dated 15 Sep 2026, no version, status planned
compared against BIA v2, approved 4 Feb 2026 (extract: Site A, chilled operations)
compared against requirements register v5, 10 Feb 2026, approved
from plan "Site A: chilled dispatch recovery plan" v3, 12 Mar 2026, approved
from plan "Site A: chilled goods receipt recovery plan" v2, 3 Mar 2026, approved
from plan "Site A: quality release recovery plan" v1, 20 Feb 2026, approved

**Input:** a change only, checked against the BIA, the register and the three attached plans. The files answered everything I needed, so I had no intake questions. I wrote no "Against the BIA" block because you only asked what the change touches.

## Block 2: What it reopens

**The change**, quoted from the change notice dated 15 Sep 2026: *"From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."*

It touches 6 lines across 5 documents. Every line is marked **proposed, to confirm**. No replacement value is proposed.

| # | Document, section, date | Line touched (quoted) | Why the change reaches it | Owner the sources name |
|---|---|---|---|---|
| 1 | BIA v2, entry B-A1 (Goods receipt, chilled), 4 Feb 2026 | "carrier: NordFrost, inbound trunking from Site B" | Trunking between Site A and Site B moves to Polar Haul | Activity owner: Warehouse lead. BIA owner: BCM manager |
| 2 | BIA v2, entry B-A2 (Dispatch, chilled), 4 Feb 2026 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Carrier and escalation route both change. NordFrost's control room "will no longer handle Site A loads" | Activity owner: Dispatch lead. BIA owner: BCM manager |
| 3 | Requirements register v5, R-08, 10 Feb 2026 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | The named single carrier changes | **No owner named** (see Gaps) |
| 4 | Chilled dispatch plan v3, §4 Contacts, 12 Mar 2026 | "Carrier escalation: NordFrost control room, 040 555 0900." | After 1 Jan 2027 this escalation contact will not handle Site A loads | Plan owner: Head of Logistics |
| 5 | Chilled dispatch plan v3, §5 Suppliers, 12 Mar 2026 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | The primary carrier changes. Whether the KuehlTrans backup still stands is not in the sources | Plan owner: Head of Logistics |
| 6 | Goods receipt plan v2, §3 Inbound transport, 3 Mar 2026 | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Both the carrier and a recovery action rely on NordFrost | Plan owner: Warehouse lead |

**Searched, no reference to the carrier or the change:**
- BIA B-A3, Quality release
- Register entries R-06, R-07 and R-09
- Quality release plan v1, all sections
- Chilled dispatch plan v3: §2, §3 and §6 (§1 is covered under Gaps)
- Goods receipt plan v2: §1 and §2

**Timing:** until 31 Dec 2026, the NordFrost lines above match the change notice. They go out of date on 1 Jan 2027.

### Gaps

- **R-08 has no named owner.** The register's Owner cell is blank, so nobody is named to confirm this entry.
- **The change notice has no version number.** It is dated 15 Sep 2026 with status "planned, approved by the procurement board". I treated it as the planned change, not as something already in effect.
- **Outbound transport from Site B during recovery: not in the sources.** Dispatch plan §1 moves "chilled dispatch to Site B". The change notice covers "outbound chilled transport from Site A" and trunking between the sites. It doesn't say which carrier takes outbound loads from Site B while that plan is invoked.
- **Polar Haul's escalation route or control room: not in the sources.**
- **The KuehlTrans backup and the change: not in the sources.** Nothing says whether the backup is affected. Separately, BIA B-A2 says "no second carrier recorded" while dispatch plan §5 names KuehlTrans. That predates this change and is a plan-vs-BIA question for block 1, so I haven't ranked it here.
- **Holding loads at Site B: not in the sources.** Nothing says whether Polar Haul will hold inbound loads at Site B as goods receipt plan §3 expects NordFrost to.
- **No embedded instructions** were found in any attachment.

### Coverage unknown

These kinds of document could be touched by the change but weren't attached, so I couldn't search them:
- **Supplier contracts:** NordFrost's exit and transition terms, and the Polar Haul contract or SLA.
- **Site A contact lists and call trees** that hold the NordFrost control room number.
- **Escalation routes** kept outside the plans.
- **Action cards and role cards** for the dispatch lead and warehouse lead.
- **Work instruction WI-14**, the LogiStock manual export, and any carrier interface in LogiStock.
- **Site B plans and Site B BIA entries.** The trunking runs to and from Site B.
- **The full Site A BIA.** Only the extract was attached.
- **The continuity strategy** from the design stage that chose the carrier arrangement.
- **The risk register and supplier risk assessments.**
- **The exercise and test schedule** for the affected plans.

**Reviewer:** you, as the BCM manager, check each quoted passage. The Dispatch lead and Warehouse lead (BIA activity owners), the Head of Logistics and Warehouse lead (plan owners), and you as BIA and register owner each decide whether their document changes. A plan changes only with its owner's approval and a new version. I changed nothing.

Parts of this document were drafted with AI support (check-against-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** use `units/prompts/review.md` on each flagged plan: the chilled dispatch plan v3 and the chilled goods receipt plan v2. If you want the plan-vs-BIA comparison as well, run this skill on those plans. It would cover the KuehlTrans point above.
