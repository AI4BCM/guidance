# check-against-bia case1b-variant-no-plans: Claude Code 2.1.284, 2026-10-01

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed; later turns with `--resume`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `requirements-register.md`.


## Turn 1

**Request:** /check-against-bia new contract trunking supplier from january, what does it touch. Attached: change-trunking-supplier.md, bia-extract-dispatch.md, requirements-register.md

**Reply (verbatim):**

Before I open any of the three files, I need one answer from you. This check always starts with it.

**What class of data do these files hold, and is this environment approved for that class?**

A BIA extract counts as high-sensitivity data. A change about a trunking supplier contract is likely to carry contractual dependencies on that supplier, which is high-sensitivity too. Under the AI4BCM data rules (`units/data-rules.md`, Sensitivity classes), that kind of data may only go into an approved corporate or private environment. If this session is not approved for it, tell me and I'll stop without reading anything.

**Reviewer:** you, as the BCM manager who asked, check every quoted passage. The owner of each plan and each BIA activity decides whether their document changes. A plan only changes with its owner's approval and a new version. What I return is a draft in this chat. I won't edit, send or approve anything.

**Plans are missing from the set.** The file names show a change description, a BIA extract and the requirements register, but no continuity plans. If you want the check to cover the plans the new supplier could affect, attach them along with your answer. These might be the dispatch continuity plan, a telephony or ICT recovery plan, contact lists, escalation routes or the supplier contract. If you don't, the "What it reopens" section will cover only the BIA and register entries and will say "plans: coverage unknown, none attached".

Once you've confirmed the classification, I'll read the files. I may then ask up to three questions that the files leave open.


## Turn 2

**Request:** high, and this environment is approved for high. None to hand: no plans or other documents to attach.

**Reply (verbatim):**

From change notice dated 15 Sep 2026 (no version number; status "planned, approved by the procurement board")
Compared against BIA v2, approved 4 Feb 2026
Compared against requirements register v5, 10 Feb 2026 (approved by the BCM manager)

**Input:** a change only, with no plan attached. Block 1 (Against the BIA) does not apply, so this reply is block 2 only. I asked no further intake questions: the one thing the files leave open is R-08's missing owner, and an answer from you could not fill that in.

---

## What it reopens

The change, quoted from the change notice dated 15 Sep 2026: "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

| Document and entry | Line the change touches (quoted) | What it touches | Owner the sources name | Status |
|---|---|---|---|---|
| BIA v2, 4 Feb 2026, B-A1 Goods receipt, chilled | "carrier: NordFrost, inbound trunking from Site B" | The named carrier for Site B to Site A trunking | Warehouse lead (activity); BCM manager (BIA) | proposed, to confirm |
| BIA v2, 4 Feb 2026, B-A2 Dispatch, chilled | "carrier: NordFrost, no second carrier recorded" | The named carrier for outbound chilled transport | Dispatch lead (activity); BCM manager (BIA) | proposed, to confirm |
| BIA v2, 4 Feb 2026, B-A2 Dispatch, chilled | "carrier escalation: NordFrost control room" | The escalation route: the notice says that control room "will no longer handle Site A loads" from 1 Jan 2027 | Dispatch lead (activity); BCM manager (BIA) | proposed, to confirm |
| Requirements register v5, 10 Feb 2026, R-08 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | The named single carrier, and the open second-carrier item | **none named** (see Gaps) | proposed, to confirm |

I propose no replacement values. Each affected line reads "carrier: to be confirmed" and "carrier escalation: to be confirmed" until its owner decides. The notice names Polar Haul but gives no escalation route for it ("not in the sources"). It also doesn't say whether NordFrost stays on as a second carrier, so the change neither settles nor reopens R-08's "second carrier open" ("not in the sources").

**Searched and not touched, as far as the sources go:**
- **BIA v2, B-A3 Quality release:** its resources ("lab at Site A; one qualified releaser per shift") name no carrier.
- **Register R-06** ("One qualified releaser per shift, all year") and **R-07** ("Chilled dispatch: at least 4 pickers per shift"): no carrier dependency.
- **Register R-09** ("LogiStock restored within 6 hours"): the notice says nothing about Polar Haul and LogiStock ("not in the sources").
- **MTPD and RTO for B-A1 and B-A2:** the change does not alter these values. Their owners decide whether the new carrier affects them.

### Gaps

- **R-08 has no named owner.** The Owner column is empty. Somebody has to own the decision on this entry before it can be closed.
- **The change notice has a date but no version number.** It is a planned change, not yet in effect. I used it as the description of the change, not as current fact.
- **Your answers at intake** (your statements, not sources): the data is high-sensitivity and this environment is approved for that class; you have no plans or other documents to attach. Assumption: no plan in the set names NordFrost, because no plan was searched.
- I found no instructions aimed at an AI in any of the three files.

### Coverage unknown

- **plans: coverage unknown, none attached.** This covers continuity or recovery plans for chilled goods receipt and chilled dispatch at Site A, and any transport or logistics recovery procedures.
- **Contact lists and escalation routes:** any list that names the NordFrost control room.
- **Supplier contracts:** NordFrost's contract and exit terms, and the new Polar Haul contract and its service levels.
- **Supplier or third-party register:** wherever NordFrost is recorded as a critical supplier.
- **Risk register or risk assessments:** for example single-carrier risk and the transition at 1 Jan 2027.
- **Site B BIA entries:** the trunking runs both ways, and the extract covers Site A only.
- **Exercise and test schedules:** any scenario built around NordFrost.

---

**Reviewer:** you, as BCM manager, check each quoted passage against the source files. The Warehouse lead and the Dispatch lead decide whether B-A1 and B-A2 change. R-08 needs an owner to be named first. Nothing has been edited; any change needs its owner's approval and a new version.

**Next step:** no plans were attached, so I flagged none. When you find a plan that names NordFrost or its control room, run [`units/prompts/review.md`](units/prompts/review.md) on that plan.

> Parts of this document were drafted with AI support (/check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
