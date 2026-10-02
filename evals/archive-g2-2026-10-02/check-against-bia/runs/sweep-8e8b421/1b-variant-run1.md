# /check-against-bia case 1b-variant, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `f299c8c3-285f-4418-a286-693cdf473227`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `requirements-register.md`.
Variant of 1b: only the change notice, the BIA and the register attached.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia New contract trunking supplier from january, what does it touch? The files change-trunking-supplier.md, bia-extract-dispatch.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, I need one answer from you. This question doesn't count toward the skill's intake questions.

**What class of data do these files hold, and is this environment approved for it?**

From their names, the files probably hold some of the following, which the AI4BCM data rules (`units/data-rules.md`, Sensitivity classes) treat as **high-sensitivity**:
- BIA data: the dispatch BIA extract
- supplier contractual dependencies: the trunking supplier change
- possibly contact or personal data in the register or the change description

High-sensitivity data may only go into an approved corporate or private environment. Please confirm one of these:

1. **This Claude Code environment is approved for high-sensitivity BCM data.** I'll then read the three files and run the check.
2. **The files hold nothing high-sensitivity** (for example, they're anonymised or test material). Tell me the class and I'll go ahead.
3. **Neither.** I'll stop, and you can run this skill in an approved environment instead.

Once you've answered, the BCM manager (you) checks every passage I quote. Each plan owner and each BIA activity owner decides whether their document changes. I'll return a draft in the chat and won't edit anything.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read all three files:

- **Change notice**, dated 15 Sep 2026, planned
- **BIA extract**, v2, approved 4 Feb 2026
- **Requirements register**, v5, 10 Feb 2026

This is a **change only**, so I'll check it against the BIA and the register. No plans are attached, so before I write anything I have three intake questions. Your answers will set the scope; they won't fill in any value.

1. **Plans to search.** Are there plans or related documents you want included? For example, the Site A dispatch or chilled operations plan, a carrier or transport failure plan, the escalation or contact list with the NordFrost control room, or the NordFrost or Polar Haul contract. If you don't attach any, the report will say "plans: coverage unknown, none attached" and cover only the BIA and register entries.
2. **Current versions.** Are BIA v2 (approved 4 Feb 2026) and register v5 (10 Feb 2026) still the current approved versions? Or is a later draft or version in progress that I should treat as not current?
3. **Scope at Site B.** The change covers trunking "between Site A and Site B" and outbound transport from Site A. Should I limit this to Site A's entries, which are all that's attached? Or do you also want Site B's BIA and register named as coverage unknown?

If you skip a question, I'll record my assumption under Gaps:
1. No plans are attached.
2. The attached versions are current.
3. Site A only, with Site B listed as coverage unknown.

## Turn 3

**Request:** None to hand.

**Reply (verbatim):**

Compared against **BIA v2, approved 4 Feb 2026** (extract: Site A, chilled operations)
Compared against **Requirements register v5, 10 Feb 2026** (approved by the BCM manager; built from BIA v2)
Change from the **Change notice: chilled trunking carrier, dated 15 Sep 2026** (status: planned, approved by the procurement board)

**Reviewer:** you, as BCM manager, check each quoted passage. Each BIA activity owner and register owner decides whether their entry changes. A plan changes only with its owner's approval and a new version.

## Block 2: What it reopens

The change, as the notice words it: *"From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."*

**Plans:** coverage unknown, none attached.

| Entry | Line it touches (quoted) | Why | Owner named in the source | Status |
|---|---|---|---|---|
| **BIA v2, B-A1** Goods receipt, chilled (4 Feb 2026) | "carrier: NordFrost, inbound trunking from Site B" | Trunking between Site A and Site B moves to Polar Haul | Warehouse lead | proposed, to confirm |
| **BIA v2, B-A2** Dispatch, chilled (4 Feb 2026) | "carrier: NordFrost, no second carrier recorded" | Outbound chilled transport from Site A moves to Polar Haul | Dispatch lead | proposed, to confirm |
| **BIA v2, B-A2** Dispatch, chilled (4 Feb 2026) | "carrier escalation: NordFrost control room" | "NordFrost's control room will no longer handle Site A loads from that date." | Dispatch lead | proposed, to confirm |
| **Register v5, R-08** (10 Feb 2026) | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | Both parts of this requirement move to Polar Haul. Its sources are BIA v2, B-A1 and B-A2. | **none named** | proposed, to confirm |

I've proposed no replacement values. The change notice doesn't name a new carrier escalation route, so that stays "carrier escalation: to be confirmed". The notice doesn't say whether a second carrier is planned: not in the sources.

**Searched and not touched:**
- **BIA B-A3** (Quality release)
- **R-06** (releaser per shift)
- **R-07** ("at least 4 pickers per shift", from B-A2)
- **R-09** ("LogiStock restored within 6 hours", from B-A2)

None of these mentions a carrier. The change doesn't affect any MTPD or RTO line. Whether the new carrier can meet B-A1's 12-hour RTO and B-A2's 8-hour RTO is not in the sources, and only the activity owners can settle it.

### Gaps
- **R-08 has no named owner.** The register's Owner field for this entry is blank.
- **The change notice is a planned change**, dated 15 Sep 2026, and takes effect 1 Jan 2027. Until then, NordFrost is still the carrier on record in both BIA v2 and register v5.
- **My statements, not sources:**
  - Your answer: "None to hand" (no plans or other documents to attach).
  - You didn't answer the version question. I assumed BIA v2 and register v5 are the current approved versions.
  - You didn't answer the Site B question. I assumed Site A only, with Site B listed below.

### Coverage unknown
These are kinds of document the change could touch that weren't attached:
- **Continuity plans**: for example the Site A chilled dispatch or goods-receipt plans, and any transport or carrier failure plan
- **Contact lists and escalation routes**: wherever the NordFrost control room is listed
- **Supplier contracts and supplier assessments**: the NordFrost exit terms and the new Polar Haul contract
- **Site B's BIA and requirements register**: the other end of the trunking
- **Risk register entries**: carrier or single-supplier dependency
- **Action cards**: for any role that calls the carrier

Parts of this document were drafted with AI support (/check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Next step:** no plans were attached, so none is flagged yet. When you find the plans listed under Coverage unknown, run [`units/prompts/review.md`](units/prompts/review.md) on each one that names NordFrost or its control room.
