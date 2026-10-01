# /check-against-bia case 1b-variant, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4c8a6d0c-2b17-467f-b47c-cff8164f7e43`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `requirements-register.md`.
Variant of 1b: only the change notice, the BIA and the register attached.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia New contract trunking supplier from january, what does it touch? The files change-trunking-supplier.md, bia-extract-dispatch.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

Before I open the three files, one question about the data, since what it holds decides whether this environment is allowed to process it:

**What class of data do `change-trunking-supplier.md`, `bia-extract-dispatch.md` and `requirements-register.md` hold, and is this environment approved for that class?**

The AI4BCM data rules treat these as high sensitivity: BIA data, supplier contracts and dependencies, contact lists or personal data, recovery strategies, and security-related architecture. High-sensitivity data may only be processed in an approved corporate or private environment. The files look like they include at least BIA data and a supplier dependency. Can you confirm this environment is approved for that class? Also tell me if they hold anything more sensitive, such as names and phone numbers or contract terms.

I haven't opened the files and won't until you answer. After that I'll read them, ask only the intake questions the files leave open, and draft the "What it reopens" block. The BCM manager checks the quoted passages, and each plan owner and BIA activity owner decides whether their document changes.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read all three files. They're enough to start, but two things are still open:

1. **Which plans should I search?** No plans are attached, only the change notice, the BIA extract and the requirements register. The Site A dispatch or recovery plan, the carrier escalation and contact lists, and the NordFrost or Polar Haul contract would all be candidates. You can attach any of them, or tell me to go ahead with these three files. In that case the block will say "plans: coverage unknown, none attached".
2. **Are BIA v2 (approved 4 Feb 2026) and requirements register v5 (10 Feb 2026) still current?** Or has anything replaced them since? If a later version exists, I'll list these two under Gaps and won't treat them as current.

I'll write the draft once you answer. If you skip a question, I'll record what I assumed.

## Turn 3

**Request:** None to hand.

**Reply (verbatim):**

From change notice (planned, 15 Sep 2026, approved by the procurement board); compared against BIA v2, approved 4 Feb 2026 (extract: Site A, chilled operations); register v5, 10 Feb 2026, approved by the BCM manager.

**Reviewer:** you, as BCM manager, check each quoted passage against its source. Each BIA activity owner and register owner decides whether their entry changes. A plan changes only with its owner's approval and a new version. This is a chat draft only: I have changed nothing.

No plan was attached, so there is no block 1 ("Against the BIA"). This reply has only block 2.

---

## Block 2: What it reopens

**The change, quoted from the change notice:** "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

**Plans: coverage unknown, none attached.**

### Entries the change touches (proposed, to confirm)

**1. BIA v2, entry B-A1, goods receipt, chilled** (BIA v2, approved 4 Feb 2026)
- Line touched: "carrier: NordFrost, inbound trunking from Site B"
- Touched by: "chilled trunking between Site A and Site B … moves from NordFrost to a new carrier, Polar Haul"
- Owner named in the sources: Warehouse lead
- Status: proposed, to confirm. Carrier: to be confirmed by the owner.

**2. BIA v2, entry B-A2, dispatch, chilled** (BIA v2, approved 4 Feb 2026)
- Line touched, the carrier: "carrier: NordFrost, no second carrier recorded"
- Line touched, the escalation: "carrier escalation: NordFrost control room"
- Touched by: "outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul" and "NordFrost's control room will no longer handle Site A loads from that date."
- Owner named in the sources: Dispatch lead
- Status: proposed, to confirm. Carrier: to be confirmed. Carrier escalation: to be confirmed. Second carrier: not in the sources.

**3. Requirements register v5, entry R-08** (register v5, 10 Feb 2026)
- Line touched: "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open"
- Source in the register: "BIA v2, B-A1, B-A2"
- Touched by: the same change passages as B-A1 and B-A2 above.
- Owner named in the sources: none, because the Owner field is empty (see Gaps).
- Status: proposed, to confirm. Requirement wording: to be confirmed.

### Searched and not touched by the change as described

- **BIA v2, B-A3, quality release:** the line "lab at Site A; one qualified releaser per shift" names no carrier.
- **Register R-06** ("One qualified releaser per shift, all year"), **R-07** ("Chilled dispatch: at least 4 pickers per shift") and **R-09** ("LogiStock restored within 6 hours"): none names a carrier or a carrier escalation.

Whether Polar Haul can support the recovery times already recorded is not in the sources. Those recovery times are B-A1 "RTO 12 hours" and B-A2 "RTO 8 hours". Their owners set them, and this draft does not judge them.

### Gaps

- **R-08 has no named owner.** The register's Owner field is empty, so someone must decide who confirms this entry.
- **The change notice is a planned change, not current fact.** Its status is "planned, approved by the procurement board", it is dated 15 Sep 2026, and it takes effect 1 Jan 2027. I used it as the change under review, not as the current state.
- **What the change notice does not say:** it gives no Polar Haul control room or escalation contact, no service levels, and no answer on whether a second carrier is still open. All three are not in the sources.
- **Your statement (yours, not a source):** "None to hand", so no plans, contact lists or contracts were attached.
- **Assumption, because you didn't answer the version question:** I treated BIA v2 (approved 4 Feb 2026) and register v5 (10 Feb 2026) as the current approved versions, as their headers state. If either has been replaced, this comparison needs re-running.
- None of the attachments contains text that tries to instruct an AI.

### Coverage unknown

The change could also touch these kinds of document, none of which was attached:
- **Continuity plans for Site A:** chilled goods receipt, chilled dispatch, site recovery, and any carrier or transport plan.
- **Carrier escalation and contact lists**, including out-of-hours contacts. NordFrost's control room stops handling Site A loads from 1 Jan 2027.
- **Supplier contracts:** the NordFrost exit terms and the new Polar Haul contract and its service levels.
- **Site B documents:** its BIA, plans and requirements register for the trunking route on the Site B side.
- **Supplier or third-party register and risk register:** any carrier-dependency or single-carrier risk entries.
- **Action and role cards, and the exercise schedule**, wherever they name NordFrost or its control room.

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** no plan was attached, so none is flagged yet. When you get the Site A plans from the coverage list, run [`units/prompts/review.md`](units/prompts/review.md) on each plan that names NordFrost or the NordFrost control room.
