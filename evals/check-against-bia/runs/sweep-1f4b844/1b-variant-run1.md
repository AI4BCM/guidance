# /check-against-bia case 1b-variant, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `afa892b8-9f28-4b41-98e1-2de99070d097`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `requirements-register.md`.
Variant of 1b: only the change notice, the BIA and the register attached.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia New contract trunking supplier from january, what does it touch? The files change-trunking-supplier.md, bia-extract-dispatch.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attachments, I need one answer from you.

**What class of data do these files hold, and is this environment approved for it?**

From the file names, they likely include BIA data (`bia-extract-dispatch.md`) and supplier contract dependencies (`change-trunking-supplier.md`). Under the AI4BCM data rules (`units/data-rules.md`, Sensitivity classes), both are **high-sensitivity**. High-sensitivity data may only be used in an enterprise, private or purpose-built BCM environment that your organisation has approved for it (`units/tools.md`, Selection guide, Implement and Analyse rows). That approval covers retention, deletion, access control and logging.

Please confirm one of these:

1. **High-sensitivity, and this environment is approved for high-sensitivity BCM data.** I'll read the files and continue.
2. **Lower class**, for example anonymised or fictional training material. Tell me which, and I'll continue.
3. **High-sensitivity, but you're not sure this environment is approved.** I'll stop here, and nothing will have been read.

Once that's settled, I'll read the attachments and ask only about what they leave unclear. The BCM manager who asked reviews the output. Each plan owner and each BIA activity owner decides whether their document changes. I'll only write a draft in the chat and won't edit any file.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files. Nothing in them tries to instruct an AI. This is a **change** (block 2 only, since no plan was given for comparison). I'll check it against BIA v2 (Site A extract, approved 4 Feb 2026) and requirements register v5 (approved 10 Feb 2026).

Before I write the draft, I have two questions the attachments leave open:

1. **Which plans and other documents should I search?** You attached the BIA extract and the register, but no continuity plans. That means no Site A chilled dispatch plan, goods receipt plan, escalation or contact list, or NordFrost contract summary. If you attach the ones that could name NordFrost or its control room, I'll search them. If not, block 2 will cover only the BIA and register entries and will say "plans: coverage unknown, none attached".

2. **Is there more of BIA v2 to search than the Site A extract?** The change also moves the trunking between Site A and Site B. Site B activities that depend on that trunking would sit in a part of BIA v2 I don't have. Should I treat Site B as out of scope, or will you attach that extract? If not, I'll list it under Coverage unknown.

If you skip either question, I'll proceed on the stated assumption and record it under Gaps. Your answers can shape the scope, but they won't fill any value. Choosing replacement carriers, contacts or owners stays with the document owners.

## Turn 3

**Request:** None to hand.

**Reply (verbatim):**

# What the Polar Haul carrier change touches (draft)

Sources:
- Change notice "chilled trunking carrier", dated 15 Sep 2026, status "planned". It has no version number (see Gaps).
- BIA extract for Site A chilled operations, from BIA v2, approved 4 Feb 2026.
- Requirements register for Site A, v5, approved 10 Feb 2026.

**Reviewer:** you, as BCM manager, check each quoted passage. The Warehouse lead and the Dispatch lead each decide whether their BIA entry changes, and so does whoever is named owner of R-08. I have changed nothing.

## Block 2: What it reopens

The change, quoted from the change notice (15 Sep 2026): *"From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."*

| # | Entry | Line the change touches (quoted) | Why it's touched | Owner named in the source | Status |
|---|---|---|---|---|---|
| 1 | BIA v2, B-A1 Goods receipt, chilled | "carrier: NordFrost, inbound trunking from Site B" | The Site B to Site A trunking moves to another carrier from 1 Jan 2027 | Warehouse lead | proposed, to confirm |
| 2 | BIA v2, B-A2 Dispatch, chilled (carrier) | "carrier: NordFrost, no second carrier recorded" | Outbound chilled transport from Site A moves to another carrier from 1 Jan 2027 | Dispatch lead | proposed, to confirm |
| 3 | BIA v2, B-A2 Dispatch, chilled (escalation) | "carrier escalation: NordFrost control room" | The notice says NordFrost's control room "will no longer handle Site A loads from that date". The escalation route would point to a party that no longer handles the loads | Dispatch lead | proposed, to confirm |
| 4 | Register v5, R-08 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | It names NordFrost as the single carrier for both flows the change moves. Whether "second carrier open" is still open is for the owner to judge | **not in the sources** (owner blank) | proposed, to confirm |

I'm proposing no replacement values. "Carrier", "carrier escalation" and the R-08 wording are all **to be confirmed** by their owners.

**Searched, and the change doesn't touch them:**
- BIA v2, B-A3 Quality release. It names no carrier.
- Register R-06 (B-A3), R-07 (pickers for B-A2) and R-09 (LogiStock for B-A2). None of them names a carrier or an escalation route.

**Gaps**
- **R-08 has no named owner.** The register's Owner column is blank for it. Someone has to own the decision on the carrier line before this entry can be reopened.
- **The change notice has no version number.** It is dated 15 Sep 2026, has status "planned, approved by the procurement board" and was raised by the Head of Procurement. Because it is planned, not in effect, the BIA and register lines above stay correct until 31 Dec 2026. They become out of date from 1 Jan 2027.
- **What you told me:** "None to hand." No plans or other documents were attached, and no Site B BIA extract. My assumption is that Site B entries are outside this search, so they are listed under Coverage unknown below.
- **Plans:** coverage unknown, none attached.

**Coverage unknown.** These kinds of document could also name NordFrost, its control room, or the Site A to Site B trunking. None of them was attached:
- continuity plans for Site A chilled goods receipt and dispatch, including action cards
- escalation routes and contact lists that hold NordFrost control room details
- supplier contracts and SLAs: the NordFrost exit terms and the Polar Haul contract
- the BIA v2 entries and plans for Site B, which depend on the same trunking
- the supplier register or third-party list, and supplier risk records
- the continuity strategy from the design stage, where the single carrier or "second carrier open" may have been decided
- exercise schedules or scenarios that use NordFrost

---

*Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

**Next step:** no plan was attached, so none is flagged yet. When you find the Site A chilled plans, contact lists or escalation routes that name NordFrost, run each one through `units/prompts/review.md` with its owner before the 1 January 2027 changeover.
