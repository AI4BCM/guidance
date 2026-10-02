# /check-against-bia case 1b-variant, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `fdb37923-5088-452f-be35-dff0cef274d8`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `requirements-register.md`.
Variant of 1b: only the change notice, the BIA and the register attached.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia New contract trunking supplier from january, what does it touch? The files change-trunking-supplier.md, bia-extract-dispatch.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attachments I need one answer, because it decides whether I can work on them here at all.

**What class of data do `change-trunking-supplier.md`, `bia-extract-dispatch.md` and `requirements-register.md` hold, and is this environment approved for that class?**

The guidance (`units/data-rules.md`, Sensitivity classes) treats the following as **high sensitivity**, allowed only in an approved corporate or private environment:
- BIA data and risk assessment detail
- supplier weaknesses and contractual dependencies
- contact lists and personal data
- recovery strategies and design assumptions

From the file names, a BIA extract for dispatch and a supplier contract change probably fall in that class. The selection guide in `units/tools.md` puts this kind of comparison in an enterprise, private or purpose-built BCM environment only.

Please confirm one of these:
1. **High sensitivity, and this Claude Code environment is approved for high-sensitivity BCM data** (retention, access and contract checks done under *Before you approve a tool*). I'll read the files and continue.
2. **Lower sensitivity** (for example anonymised or fictional data). Tell me which class and I'll continue.
3. **High sensitivity, and this environment is not approved, or you don't know.** I'll stop here and won't open the files.

Once you answer, I'll read the attachments and ask any remaining intake questions. The draft will go to you as BCM manager to check each quoted passage. The plan and BIA activity owners decide whether their documents change.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read all three files. Here is what they are:

- **Change notice: chilled trunking carrier.** Dated 15 Sep 2026, status "planned, approved by the procurement board". It has no version number.
- **BIA extract: Site A, chilled operations.** BIA v2, approved 4 Feb 2026.
- **Requirements register: Site A.** v5, 10 Feb 2026, approved.

Three questions before I write the draft. Your answers can change what I search, but they won't supply any value in the draft.

1. **Plans and other documents to search.** You didn't attach any continuity plans, such as a chilled dispatch plan, a goods receipt plan or a Site A recovery plan. You also didn't attach a carrier escalation or contact list, or the NordFrost or Polar Haul contracts. Can you attach any of them? If not, block 2 will cover only the BIA and register entries, and it will say "plans: coverage unknown, none attached".
2. **Direction of trunking.** The notice says "chilled trunking between Site A and Site B". BIA entry B-A1 relies on "inbound trunking from Site B". Do you want me to treat the change as covering both directions, and so reopening B-A1? Or do you know it covers Site A → Site B only?
3. **Version of the notice.** The notice has a date but no version. Is the 15 September 2026 notice the current one, or has a later version replaced it? Either way, I'll list the missing version under Gaps.

If you skip a question, I'll make these assumptions and record them under Gaps:
1. No plans are available.
2. The change covers both directions.
3. The 15 Sep notice is current.

## Turn 3

**Request:** None to hand.

**Reply (verbatim):**

**Sources read:**
- **Change notice:** "Change notice: chilled trunking carrier", dated 15 Sep 2026. It has no version number (see Gaps).
- **BIA:** compared against BIA v2, approved 4 Feb 2026. Only the "Site A, chilled operations" extract was attached.
- **Requirements register:** Site A, v5, 10 Feb 2026, approved by the BCM manager.

**Reviewer:** you, as BCM manager, check every quoted passage against its source. Each BIA activity owner, and the register entry's owner once someone is named, decides whether their entry changes. I changed nothing.

---

**Block 1: Against the BIA.** Not run. No plan was attached, so there is nothing to compare against the BIA.

---

**Block 2: What it reopens**

The change, quoted from the change notice (dated 15 Sep 2026):
> "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

| # | Document, entry, date | Line it touches (quoted) | Owner the sources name | Status |
|---|---|---|---|---|
| 1 | BIA v2, B-A2 Dispatch, chilled, 4 Feb 2026 | "carrier: NordFrost, no second carrier recorded" | Dispatch lead (activity owner); BCM manager (BIA owner) | proposed, to confirm |
| 2 | BIA v2, B-A2 Dispatch, chilled, 4 Feb 2026 | "carrier escalation: NordFrost control room" | Dispatch lead; BCM manager | proposed, to confirm |
| 3 | BIA v2, B-A1 Goods receipt, chilled, 4 Feb 2026 | "carrier: NordFrost, inbound trunking from Site B" | Warehouse lead (activity owner); BCM manager (BIA owner) | proposed, to confirm. Depends on assumption A1 under Gaps. |
| 4 | Requirements register v5, R-08, 10 Feb 2026 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | **None.** The Owner cell is empty. | proposed, to confirm |

There is no replacement value for any of these lines:
- **Carrier:** to be confirmed.
- **Carrier escalation route:** to be confirmed.
- **Second carrier:** to be confirmed.

**Searched and not touched by the change's wording:**
- BIA v2, B-A3 Quality release, and register R-06. Neither names a carrier.
- R-07 ("at least 4 pickers per shift") and R-09 ("LogiStock restored within 6 hours"). Both cite B-A2 as their source, but neither names a carrier.

**Plans: coverage unknown, none attached.**

**Coverage unknown.** The change could also touch these kinds of document, none of which was in the attached set:
- Continuity plans that use chilled dispatch, goods receipt or trunking, for example a Site A recovery plan or a dispatch plan.
- Carrier escalation and contact lists, and out-of-hours call-out lists that name the NordFrost control room.
- Supplier contracts and service levels: the NordFrost exit terms and the new Polar Haul contract.
- The supplier or third-party register and the risk register entries for chilled transport.
- BIA entries at Site B that depend on the same trunking.
- Action cards drawn from any of the plans above.

**Gaps**
- **Change notice has no version number.** It is dated 15 Sep 2026 with status "planned, approved by the procurement board", and the change takes effect on 1 Jan 2027. I didn't treat it as the current state. The BIA and register lines above remain current until their owners decide otherwise.
- **R-08 has no named owner.** It is the only touched entry without one.
- **Your statement:** you have no plans, contact lists or contracts to hand. I took this from your intake answer, not from a source.
- **Assumption A1 (question skipped):** I read "trunking between Site A and Site B" as covering both directions, so B-A1's "inbound trunking from Site B" is touched. If the change covers Site A → Site B only, row 3 drops out.
- **Assumption A2 (question skipped):** I treated the 15 Sep 2026 notice as current, with no later version.
- **Not in the sources:**
  - Polar Haul's escalation route or control room.
  - Whether NordFrost stays on in any role, for example as a second carrier.
  - Whether the Polar Haul contract supports B-A2's RTO of "8 hours" and B-A1's RTO of "12 hours". I compared no values here. The RTOs belong to their owners.
- **No instructions addressed to an AI** were found in any of the three attachments.

Parts of this document were drafted with AI support (check-against-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** no plans were attached, so none is flagged yet. When the plans that use chilled dispatch, goods receipt or trunking turn up, run `units/prompts/review.md` on each one with its owner.
