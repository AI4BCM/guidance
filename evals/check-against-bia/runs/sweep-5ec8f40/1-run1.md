# /check-against-bia case 1, run1: Claude Code, guidance at 5ec8f40

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `75bc6b8a-8f62-42d7-a511-c71eb8458e1b`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the attached files, I need one answer.

**What class of data do these documents hold?** For example: public, internal, confidential, or strictly confidential / personal data. Mention anything specific too, such as named staff contact details, supplier contract terms or site security details.

I'll only read the BIA extract, register, three plans and the change notice once I know this environment is approved for that class. If it isn't, I'll stop there.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia && cat preflight.md && ls -R units | head -50 && cat units/stages/implement.md`
- Bash: `ls -la && for f in bia-extract-dispatch.md requirements-register.md plan-chilled-dispatch.md plan-goods-receipt.md plan-quality-release.md change-trunking-suppl`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/stages/implement.md`
- Glob: `*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The material is in. One question before I draft. The prompt tells me to ask only about what the files leave open:

**Are there other plans, contact lists or escalation routes the January carrier change could touch that aren't attached?** For example: an outbound transport plan, a Site B plan, a crisis contact list, a carrier-loss plan, or the WI-14 work instruction. If there are, attach them or tell me they exist. If not, I'll mark every kind of document not attached as "coverage unknown".

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/1/run1/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/1/run1/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/1/run1/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/1/run1/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/1/run1/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/check-against-bia/1/run1/work/change-trunking-supplier.md`

## Turn 3

**Request:** skip

**Reply (verbatim):**

# Check against the BIA: chilled dispatch, and the January trunking carrier change

**Draft only.** I have changed no plan, BIA entry or register entry. A live plan changes only with its owner's approval and a new version.

**Sources**
- BIA extract, Site A chilled operations: v2, approved by top management on 4 Feb 2026. BIA owner: BCM manager.
- Requirements register, Site A: version 5, 10 February 2026, approved by the BCM manager.
- Chilled dispatch recovery plan: version 3, 12 March 2026, approved. Plan owner: Head of Logistics.
- Chilled goods receipt recovery plan: version 2, 3 March 2026, approved. Plan owner: Warehouse lead.
- Quality release recovery plan: version 1, 20 February 2026, approved. Plan owner: QA manager.
- Change notice, chilled trunking carrier: dated 15 September 2026, no version. Status: planned. See Gaps.

---

## Block 1: Against the BIA (chilled dispatch plan v3 vs BIA v2, B-A2)

This is a report only; I changed neither document. Each disagreement goes to the two owners named. I propose no replacement value and choose neither recovery time.

| # | Topic | Chilled dispatch plan, v3, 12 Mar 2026 | BIA v2, 4 Feb 2026 (and register v5, 10 Feb 2026) | Owners, proposed, to confirm |
|---|---|---|---|---|
| 1 | Recovery time | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | B-A2, RTO column: "8 hours" | Plan: Head of Logistics. BIA activity B-A2: Dispatch lead |
| 2 | Resource: pickers | §3: "A minimum of 3 pickers per shift travel to Site B." | B-A2: "at least 4 pickers per shift". Register R-07: "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics. B-A2: Dispatch lead. R-07: Dispatch lead |
| 3 | Supplier: second carrier | §5: "Backup carrier: KuehlTrans, by spot booking." | B-A2: "carrier: NordFrost, no second carrier recorded". Register R-08: "one carrier, NordFrost; second carrier open" | Plan: Head of Logistics. B-A2: Dispatch lead. R-08: none named (see Gaps) |

**Lines that agree or where one side is silent (not disagreements):**
- **Carrier escalation:** plan §4 has "Carrier escalation: NordFrost control room, 040 555 0900". B-A2 has "carrier escalation: NordFrost control room". The route matches. The BIA gives no number: not in the sources.
- **Systems:** plan §6 has "Orders leave LogiStock by the manual export in work instruction WI-14". Register R-09 has "LogiStock restored within 6 hours". The plan states no LogiStock recovery time: not in the sources.
- **Duty manager contact:** plan §4 has "Duty manager, Site A: 040 555 0172". The BIA and register don't cover it: not in the sources.

---

## Block 2: What the January carrier change reopens

**The change**, from the change notice dated 15 Sep 2026: "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."

This is a report only, over the attached set; I changed nothing and give no replacement values.

| Document, section, date | Line touched (quoted) | Owner, proposed, to confirm |
|---|---|---|
| Chilled dispatch plan v3, §4 Contacts, 12 Mar 2026 | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Chilled dispatch plan v3, §5 Suppliers, 12 Mar 2026 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics |
| Chilled goods receipt plan v2, §3 Inbound transport, 3 Mar 2026 | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead |
| BIA v2, B-A1 Goods receipt, chilled, 4 Feb 2026 | "carrier: NordFrost, inbound trunking from Site B" | Activity owner: Warehouse lead. BIA owner: BCM manager |
| BIA v2, B-A2 Dispatch, chilled, 4 Feb 2026 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Activity owner: Dispatch lead. BIA owner: BCM manager |
| Register v5, R-08, 10 Feb 2026 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | none named (see Gaps) |

**Not touched in the attached set:**
- the quality release plan v1, which has no carrier, trunking or carrier contact line
- BIA B-A3
- register entries R-06, R-07 and R-09

**For future triggers:** any change of chilled trunking or outbound carrier should reopen:
- chilled dispatch plan §4 and §5
- goods receipt plan §3
- BIA B-A1 and B-A2
- register R-08

---

## Gaps

- **Intake:** I asked whether any plans, contact lists or escalation routes were missing from the attachments. You skipped the question. I assumed the six files are the whole set, so every other kind of document is listed under Coverage unknown.
- **Change notice:** it has a date (15 September 2026) but no version number. Its status is "planned, approved by the procurement board". I treated it as a planned change, not current fact. The notice says "Raised by: Head of Procurement" and names no owner: none named.
- **Register R-08:** the Owner cell is blank, so the owner is none named. I have not inferred one from a department or role.
- **Polar Haul escalation route:** the change notice gives no Polar Haul control room or escalation route. Contact: to be confirmed.
- **KuehlTrans after 1 January 2027:** the change notice doesn't say whether the plan's backup carrier line still holds: not in the sources.
- **Goods receipt plan §3:** this goods receipt plan gives the hold request to "the dispatch lead". Whether that hand-off still applies under Polar Haul is not in the sources.
- **Planted text:** none of the attached files contains a passage telling an AI to act.

## Reviewer

The BCM manager who asked for this checks each quoted passage against the source documents. Each plan owner and BIA activity owner then decides whether their document changes. A plan changes only with its owner's approval and a new version.

- **Plan owners:**
  - Head of Logistics (chilled dispatch)
  - Warehouse lead (goods receipt)
- **BIA activity owners:**
  - Dispatch lead (B-A2)
  - Warehouse lead (B-A1)
- **BIA owner:** BCM manager
- **Register R-08 owner:** none named

## Coverage unknown

These kinds of document were not attached, so I can't say whether the change touches them:
- contact lists and crisis or escalation directories
- Site B plans
- work instruction WI-14
- carrier contracts and the supplier register
- the IT recovery plan for LogiStock
- the approved recovery strategy from the design stage
- role or action cards drawn from these plans

---

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Use review.md on the Site A chilled dispatch recovery plan, with Head of Logistics: type /challenge-my-plan.

> Use review.md on the Site A chilled goods receipt recovery plan, with Warehouse lead: type /challenge-my-plan.

**Tool calls (stream-json):**

- Grep: `AI helped`
