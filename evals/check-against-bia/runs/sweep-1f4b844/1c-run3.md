# /check-against-bia case 1c, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `824eb983-fbf1-4a17-8385-795946729e72`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files, I need to settle one thing. This question comes first and on its own.

**What class of data do these files hold, and is this environment approved for that class?**

A BIA extract, a requirements register, recovery plans and a supplier change usually count as **high sensitivity** under the guidance's data rules (`units/data-rules.md`, Sensitivity classes). That class covers BIA data, recovery strategies, contact lists and personal data, and supplier weaknesses and contractual dependencies. High-sensitivity work may only run in an approved enterprise, private or purpose-built BCM environment (`units/tools.md`, Selection guide, rows for Analyse and Implement).

Please confirm one of these:

1. **High sensitivity, and this Claude Code session is approved for it.** I'll read the files and run the check.
2. **Lower sensitivity** (for example fictional, anonymised or training material). Tell me the class and I'll go ahead.
3. **High sensitivity, and this environment is not approved for it.** I'll stop here, and you can run the check in an approved environment.

Once you confirm, here's what happens:
- **Who reviews:** you, as the BCM manager who asked, check every quoted passage. Each plan owner and each BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version.
- **What you get:** a draft in this chat and nothing else. I won't edit, send or approve anything. MTPD, RTO and RPO values stay with their owners.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources compared**
- Compared against BIA v2 (extract: Site A, chilled operations), approved 4 Feb 2026
- Requirements register: Site A, version 5, 10 Feb 2026
- From the chilled dispatch plan v3, 12 Mar 2026 (approved)
- From the chilled goods receipt plan v2, 3 Mar 2026 (approved)
- From the quality release plan v1, 20 Feb 2026 (approved)
- From the change notice "chilled trunking carrier", dated 15 Sep 2026. It has no version number (see Gaps in block 2).

**Input:** both a plan (chilled dispatch) and a change (trunking carrier). Block 1 checks the plan against the BIA; block 2 shows what the change reopens. I didn't ask any intake questions because the attachments answered what the check needed.

**Reviewer:** you, as BCM manager, check every quoted passage. Each plan owner and each BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version. All findings below are **proposed, to confirm**. I don't propose a replacement value or pick between recovery times.

---

## Block 1: Against the BIA (chilled dispatch plan v3)

### Disagreements

| # | Item | Plan passage | BIA / register passage | Owners the sources name | Status |
|---|---|---|---|---|---|
| 1 | **Recovery time** | Dispatch plan v3, §2, 12 Mar 2026: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA v2, B-A2, 4 Feb 2026: RTO "8 hours" (MTPD "24 hours") | Plan: Head of Logistics. BIA activity: Dispatch lead. BIA: BCM manager | proposed, to confirm |
| 2 | **Resource requirement: pickers** | Dispatch plan v3, §3, 12 Mar 2026: "A minimum of 3 pickers per shift travel to Site B." | BIA v2, B-A2, 4 Feb 2026: "at least 4 pickers per shift". Register v5, R-07, 10 Feb 2026: "Chilled dispatch: at least 4 pickers per shift" | Plan: Head of Logistics. B-A2 and R-07: Dispatch lead | proposed, to confirm |
| 3 | **Supplier: second carrier** | Dispatch plan v3, §5, 12 Mar 2026: "Backup carrier: KuehlTrans, by spot booking." | BIA v2, B-A2, 4 Feb 2026: "no second carrier recorded". Register v5, R-08, 10 Feb 2026: "second carrier open" | Plan: Head of Logistics. B-A2: Dispatch lead. R-08: **no owner named** | proposed, to confirm |

### Items that agree

| Item | Plan passage | BIA passage |
|---|---|---|
| Supplier: main carrier | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | B-A2: "carrier: NordFrost" |
| Contact: carrier escalation (route) | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | B-A2: "carrier escalation: NordFrost control room" |

### Items with no comparison possible (recorded gaps)

| Item | Plan passage | Why I couldn't compare |
|---|---|---|
| Carrier escalation **number** | §4: "040 555 0900" | Not in the sources. The BIA names the route but gives no number. No contact list was attached. |
| Contact: duty manager | §4: "Duty manager, Site A: 040 555 0172." | Not in the sources. The BIA and the register hold no contacts. |
| Resource: warehouse system LogiStock | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | B-A2 lists "warehouse system LogiStock" and R-09 says "LogiStock restored within 6 hours" (owner: IT service owner). The plan states no LogiStock recovery time, so the 6 hours has nothing to compare against. WI-14 was not attached. |
| Recovery location Site B | §1: "Recovery option: move chilled dispatch to Site B." | The BIA records no recovery location for B-A2, and no approved strategy was attached (the approved strategy is what the plan carries out). |

### Gaps
- Register R-08 has **no named owner**: "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" with the owner column empty.
- The approved recovery strategy (design stage) was not attached: not in the sources.
- Work instruction WI-14 was not attached: not in the sources.
- No document's status is draft, replaced or undated. The BIA is the approved v2.

---

## Block 2: What it reopens (change to Polar Haul from 1 Jan 2027)

The change notice (15 Sep 2026) says: "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul … NordFrost's control room will no longer handle Site A loads from that date."

I searched all three plans, all three BIA entries and all four register entries.

### Touched (proposed, to confirm; no replacement value given)

| Document | Line quoted | Owner the sources name |
|---|---|---|
| Dispatch plan v3, §4, 12 Mar 2026 | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Dispatch plan v3, §5, 12 Mar 2026 | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics |
| Goods receipt plan v2, §3, 3 Mar 2026 | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead (the action is assigned to the dispatch lead) |
| BIA v2, B-A1, 4 Feb 2026 | "carrier: NordFrost, inbound trunking from Site B" | Activity: Warehouse lead. BIA: BCM manager |
| BIA v2, B-A2, 4 Feb 2026 | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Activity: Dispatch lead. BIA: BCM manager |
| Register v5, R-08, 10 Feb 2026 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | **No owner named** |

### Searched, not touched
- Quality release plan v1 (§1–3): no carrier or transport line.
- BIA v2, B-A3: no carrier dependency.
- Register R-06, R-07 and R-09: no carrier line.

### Gaps
- The change notice has a date and a status ("planned, approved by the procurement board") but **no version number**. Its owner is the Head of Procurement. Because the change is planned and not yet in effect, I treated it as a proposed change, not as the current state.
- The change notice gives no Polar Haul escalation contact: contact: to be confirmed.
- The change notice doesn't say whether KuehlTrans stays as backup or whether Polar Haul covers that role: not in the sources.
- The notice covers "outbound chilled transport from Site A". It doesn't say which carrier runs outbound loads when dispatch has moved to Site B (dispatch plan §1): not in the sources.
- R-08 has no named owner.

### Coverage unknown
These kinds of document could be affected by the change but weren't in the attached set:
- Contact lists and call trees, which may hold the NordFrost control room number
- Supplier contracts: the new Polar Haul contract, the end of the NordFrost contract, and any KuehlTrans spot arrangement
- The supplier register and risk register (carrier dependency and concentration)
- Work instructions, including WI-14 and any carrier booking instructions
- Action cards and role cards that come from the dispatch or goods receipt plans
- Site B plans and BIA entries outside this Site A extract
- The approved recovery strategy from the design stage
- System interfaces, for example any LogiStock link to the carrier
- The exercise and test schedule

---

**Next step:** use `units/prompts/review.md` on each flagged plan:
- **Chilled dispatch plan v3**: block 1 items 1–3, and §4 and §5 from block 2
- **Chilled goods receipt plan v2**: §3 from block 2

> Parts of this document were drafted with AI support (/check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
