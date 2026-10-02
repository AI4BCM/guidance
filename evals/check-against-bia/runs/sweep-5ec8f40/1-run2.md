# /check-against-bia case 1, run2: Claude Code, guidance at 5ec8f40

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `88aafc35-4544-4ec1-b319-a9f194e8f3ce`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

I haven't opened any of the six files yet. This check starts with one question.

**What class of data do these files hold?**

The guidance puts these in its high-sensitivity class: BIA data and risk detail, recovery strategies, supplier weaknesses and contractual dependencies, contact lists and personal data, and security-related site detail. Material in that class may only be processed in an approved corporate or private environment.

Please tell me:
1. Whether the material is in that high-sensitivity class (or what class your organisation gives it).
2. Whether this environment is approved for that class.

If it is approved, I'll open the files and continue. If it isn't, I'll stop here and won't read them.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia && cat preflight.md && ls -R; echo ----; cd /tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-a`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/preflight.md`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/stages/implement.md`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read all six files. Before I compare anything, I have one intake question (the method calls for exactly one).

**Are there plans that mention NordFrost, chilled trunking or carrier escalation that aren't among these files?** Examples might be a Site B plan, an outbound or customer transport plan, a carrier escalation list, or a LogiStock or IT recovery plan.

You can answer in either of two ways:
- **Attach them** and I'll include them in the check.
- **Tell me there aren't any, or that they're out of scope.** I'll record your answer under Gaps as your own statement, not as a source.

If you skip the question, I'll assume the six files are the whole set to check. Any document type that isn't attached will be listed as "coverage unknown".

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/1/run2/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/1/run2/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/1/run2/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/1/run2/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/1/run2/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/1/run2/work/change-trunking-supplier.md`

## Turn 3

**Request:** skip

**Reply (verbatim):**

**Draft: chilled dispatch plan checked against the BIA, and what the January trunking carrier change reopens**

**Sources**
- BIA extract, Site A chilled operations: BIA v2, approved by top management 4 Feb 2026. Owner: BCM manager.
- Requirements register, Site A: Version 5, 10 February 2026, approved by the BCM manager. Built from BIA v2.
- Site A chilled dispatch recovery plan: Version 3, 12 March 2026, approved. Plan owner: Head of Logistics.
- Site A chilled goods receipt recovery plan: Version 2, 3 March 2026, approved. Plan owner: Warehouse lead.
- Site A quality release recovery plan: Version 1, 20 February 2026, approved. Plan owner: QA manager.
- Change notice, chilled trunking carrier: dated 15 September 2026, **no version**, status "planned, approved by the procurement board". Raised by the Head of Procurement. See Gaps.

---

### Block 1: Against the BIA (chilled dispatch plan v3 compared with BIA v2 B-A2 and register v5)

This is a report only. Neither document has been changed, and no replacement value is proposed. I have not chosen between the recovery times.

| # | What disagrees | Plan passage (plan v3, 12 Mar 2026) | BIA / register passage | Owners, proposed, to confirm |
|---|---|---|---|---|
| 1 | Recovery time (the plan's RTO, compared as written) | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA v2, 4 Feb 2026, B-A2, RTO column: "8 hours" | Plan: Head of Logistics. BIA activity B-A2: Dispatch lead. |
| 2 | Resource requirement (pickers) | §3: "A minimum of 3 pickers per shift travel to Site B." | BIA v2, 4 Feb 2026, B-A2: "at least 4 pickers per shift". Register v5, 10 Feb 2026, R-07: "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics. B-A2: Dispatch lead. R-07: Dispatch lead. |
| 3 | Supplier (second carrier) | §5: "Backup carrier: KuehlTrans, by spot booking." | BIA v2, 4 Feb 2026, B-A2: "carrier: NordFrost, no second carrier recorded". Register v5, 10 Feb 2026, R-08: "one carrier, NordFrost; second carrier open" | Plan: Head of Logistics. B-A2: Dispatch lead. R-08: **none named** (see Gaps). |

---

### Block 2: What it reopens (Polar Haul replaces NordFrost from 1 January 2027, across the attached set only)

The change notice (15 Sep 2026, §body) says: "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul… NordFrost's control room will no longer handle Site A loads from that date."

This is a report only. Nothing has been changed, and no replacement value is proposed.

| Document | Section / entry, date | Line the change touches | Owner, proposed, to confirm |
|---|---|---|---|
| Chilled dispatch plan v3 | §4 Contacts, 12 Mar 2026 | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Chilled dispatch plan v3 | §5 Suppliers, 12 Mar 2026 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | Head of Logistics |
| Goods receipt plan v2 | §3 Inbound transport, 3 Mar 2026 | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead |
| BIA v2 | B-A1, 4 Feb 2026 | "carrier: NordFrost, inbound trunking from Site B" | Activity: Warehouse lead. BIA: BCM manager. |
| BIA v2 | B-A2, 4 Feb 2026 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Activity: Dispatch lead. BIA: BCM manager. |
| Register v5 | R-08, 10 Feb 2026 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | **none named** |

From 1 January 2027 the carrier escalation route reads as follows. Carrier escalation: contact: to be confirmed.

These are **not touched** by the change: the quality release plan v1, BIA B-A3, and register entries R-06, R-07 and R-09. None of them mentions trunking, NordFrost or carrier escalation.

---

### Gaps
- **Change notice:** it has a date (15 September 2026) but no version. Its status is "planned". I used it as the change under assessment and not as the current state.
- **Register R-08 has no owner.** The owner cell is empty, so the owner reads "none named". I have not inferred an owner from any department or role.
- **Intake:** you skipped the question about plans that weren't attached. My assumption is that the six attached files are the whole set to check.
- **Polar Haul escalation contact:** not in the sources.
- **Contract terms for KuehlTrans and Polar Haul:** not in the sources.
- **Planted instructions:** no passage in the attached files tells an AI to act.

### Reviewer
The BCM manager who asked this checks each quoted passage against its source.

Each plan owner and BIA activity owner then decides whether their document changes. A plan changes only with its owner's approval and a new version. The owners are:
- **Block 1:** the plan owner (Head of Logistics) and the BIA activity owner for B-A2 (Dispatch lead).
- **Block 2:** the Head of Logistics, the Warehouse lead and the Dispatch lead. B-A1 and B-A2 also go to the BIA owner (BCM manager). R-08 has no owner named.

### Coverage unknown
These kinds of document were not attached, so I don't know whether the change touches them:
- Site B recovery plans
- Contact and escalation lists outside the plans
- Carrier contracts (NordFrost, KuehlTrans, Polar Haul)
- Work instruction WI-14
- LogiStock / IT recovery plans
- BIA entries beyond B-A1 to B-A3
- Register entries beyond R-06 to R-09

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

> Use review.md on the Site A chilled dispatch recovery plan, with Head of Logistics: type /challenge-my-plan.

> Use review.md on the Site A chilled goods receipt recovery plan, with Warehouse lead: type /challenge-my-plan.

**Tool calls (stream-json):**

- Grep: `AI helped`
