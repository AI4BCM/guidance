# /check-against-bia case 1b-variant, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `887b5064-4d89-49c7-9090-44794c50801c`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `requirements-register.md`.
Variant of 1b: only the change notice, the BIA and the register attached.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia New contract trunking supplier from january, what does it touch? The files change-trunking-supplier.md, bia-extract-dispatch.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

Before I open the three files, I need to know what class of data they hold.

**What sensitivity class is in `change-trunking-supplier.md`, `bia-extract-dispatch.md` and `requirements-register.md`?**

Under the AI4BCM data rules, these count as high-sensitivity, and they may only be handled in an approved corporate or private environment:
- BIA data and risk assessment detail
- supplier weaknesses and contractual dependencies
- contact lists or personal data
- recovery strategies and design assumptions
- security-related architecture or site detail

From the file names, I'd expect the BIA extract and the supplier change to fall in this class. Please confirm the class, and tell me whether this environment is approved to hold it. If it isn't, I'll stop here and won't read the files.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files. This is **a change only**: the carrier change notice dated 15 Sep 2026. I'll check it against BIA v2 (approved 4 Feb 2026) and requirements register v5 (10 Feb 2026). The BCM manager will check each passage I quote. Each BIA activity owner and register owner decides whether their entry changes.

Three questions before I write the draft:

1. **Which plans or other documents should I search?** No continuity plans are attached, such as a Site A dispatch plan, a goods receipt plan or a transport recovery plan. No carrier contact or escalation lists, supplier contracts or supplier register are attached either. If you attach them, I'll search them. If not, the draft lists only the BIA and register entries and says "plans: coverage unknown, none attached".
2. **Are BIA v2 and register v5 still the current approved versions?** I'm checking whether a newer version is in draft or already approved.
3. **Does the BIA extract cover every Site A activity that names NordFrost, or only the chilled ones?** It covers only chilled operations (B-A1 to B-A3). If other Site A activities rely on NordFrost, I'll list them under **Coverage unknown** unless you attach those entries.

Your answers can change the scope of the check, but I won't use them to fill in any value.

## Turn 3

**Request:** None to hand.

**Reply (verbatim):**

**Sources read:**
- Change notice "chilled trunking carrier", dated 15 Sep 2026, status "planned, approved by the procurement board". It has no version number (see Gaps).
- Compared against BIA v2, approved by top management on 4 Feb 2026. Only the extract "Site A, chilled operations" was attached.
- Requirements register Site A v5, 10 Feb 2026, approved by the BCM manager.

**Reviewer:** you, as BCM manager, check each quoted passage below. The Warehouse lead and the Dispatch lead each decide whether their BIA entry changes. The register entry has no named owner (see Gaps). A plan changes only with its owner's approval and a new version.

---

## Block 2: What it reopens

**The change:** "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date." (Change notice, 15 Sep 2026)

| Document, entry, date | Line the change touches (quoted) | What it touches | Owner named in the sources | Status |
|---|---|---|---|---|
| BIA v2, B-A1 "Goods receipt, chilled", 4 Feb 2026 | "carrier: NordFrost, inbound trunking from Site B" | Supplier: names the carrier being replaced on trunking between Site A and Site B | Warehouse lead (activity owner); BCM manager (BIA owner) | proposed, to confirm |
| BIA v2, B-A2 "Dispatch, chilled", 4 Feb 2026 | "carrier: NordFrost, no second carrier recorded" | Supplier: names the carrier being replaced on outbound chilled transport | Dispatch lead (activity owner); BCM manager (BIA owner) | proposed, to confirm |
| BIA v2, B-A2 "Dispatch, chilled", 4 Feb 2026 | "carrier escalation: NordFrost control room" | Contact or escalation: the change notice says this control room "will no longer handle Site A loads" from 1 Jan 2027 | Dispatch lead (activity owner); BCM manager (BIA owner) | proposed, to confirm |
| Register v5, R-08, 10 Feb 2026 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | Supplier requirement: names the carrier being replaced. The entry is built from "BIA v2, B-A1, B-A2" | **no owner named** | proposed, to confirm |

I propose no replacement values. Whether the new carrier, an escalation route or a second carrier belongs in these entries is for their owners to decide.

**Searched, not touched by the change text:**
- BIA v2, B-A3 "Quality release": no carrier or transport in the entry.
- R-06: releaser per shift.
- R-07: "Chilled dispatch: at least 4 pickers per shift". It is built from B-A2 but concerns staffing only.
- R-09: "LogiStock restored within 6 hours".

**Coverage unknown:**
- **Plans: coverage unknown, none attached.** This includes any Site A dispatch, goods receipt or transport recovery plan, and their action cards.
- **Carrier contact and escalation lists.** Any list holding the NordFrost control room number.
- **Supplier contracts.** The NordFrost exit terms and the Polar Haul contract.
- **Supplier register or supplier continuity assessments** for NordFrost and Polar Haul.
- **BIA entries outside the chilled extract.** This covers other Site A activities, and Site B activities that depend on the same trunking from the other end.
- **Risk register entries** on the single-carrier dependency.
- **Exercise and test schedules** that use NordFrost as a scenario or participant.

**Gaps:**
- **R-08 has no named owner.** Its Owner column is empty: "| R-08 | … | BIA v2, B-A1, B-A2 | |".
- **The change notice has no version number.** It is dated 15 Sep 2026, and its status is "planned" with effect from 1 Jan 2027. I used it as the description of a planned change, not as the current state. The BIA and register entries above stay current until their owners decide.
- **The change notice is silent on two points.** Polar Haul's escalation route or control room contact, and whether a second carrier is arranged, are "not in the sources".
- **Your intake answer: "None to hand"** (your own statement, not a source). I took it to mean no plans, contact lists or contracts are available to attach.
- **Assumption for skipped question 2:** BIA v2 and register v5 are the current approved versions, as their headers state.
- **Assumption for skipped question 3:** the BIA extract covers chilled operations only, so other Site A or Site B entries that may name NordFrost were not searched.
- No instructions addressed to an AI were found in the attached text.

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** no plans were attached, so I couldn't flag any. Once the Site A plans and carrier contact lists are found, review each plan that names NordFrost or its control room with [`units/prompts/review.md`](units/prompts/review.md). That should happen before 1 Jan 2027.
