# /check-against-bia case 1c, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `3bf0973c-44cf-4de8-a44e-c015cd5c6c8c`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files, I need to know what class of data they hold.

BIA data, recovery strategies, contact lists, personal data, and supplier weaknesses or contractual dependencies all count as **high-sensitivity**. Under the AI4BCM data rules (`units/data-rules.md`, Sensitivity classes), that kind of data may only be processed in an approved corporate or private environment. A BIA extract, three continuity plans and a supplier change will very likely include some of it.

**What class of data do these files hold, and is this Claude Code environment approved for that class?**

- If they're high-sensitivity and this environment is approved for it, I'll go ahead.
- If they're high-sensitivity and this environment isn't approved, I'll stop here and won't open them.
- If they're lower-sensitivity, for example redacted, synthetic or training copies, tell me and I'll go ahead.

Once you've answered, I'll read the files. I'll only ask the skill's own intake questions (at most three) if the documents leave something open.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Draft: not approved. I haven't changed any document.**

Documents compared:
- Dispatch plan: Site A chilled dispatch recovery plan v3, 12 March 2026, approved
- BIA: BIA v2, approved by top management 4 Feb 2026 (extract for Site A chilled operations)
- Requirements register: Site A v5, 10 February 2026, approved by the BCM manager
- Goods receipt plan: Site A chilled goods receipt recovery plan v2, 3 March 2026, approved
- Quality release plan: Site A quality release recovery plan v1, 20 February 2026, approved
- Change notice: chilled trunking carrier, dated 15 September 2026. Status: planned, approved by the procurement board.

**Reviewer:** you, as the BCM manager, check each quoted passage against its source. Each plan owner and each BIA activity owner decides whether their document changes. A plan only changes with its owner's approval and a new version.

**Intake:** I didn't ask any intake questions. The files and your request covered the scope, and the gaps below are for the document owners to fill, not for you to answer.

---

## Block 1: Dispatch plan against the BIA

The dispatch plan (v3) was checked against BIA v2, entry B-A2, and register v5. All findings are **proposed, to confirm**. I don't propose a replacement value and I don't pick either recovery time.

| # | Type | Dispatch plan v3, 12 Mar 2026 (owner: Head of Logistics) | BIA v2, 4 Feb 2026 / Register v5, 10 Feb 2026 | Result |
|---|---|---|---|---|
| 1 | Recovery time | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA B-A2, RTO column: "8 hours" (MTPD "24 hours"). Activity owner: Dispatch lead | **Disagree.** The plan allows 12 hours, the BIA RTO is 8 hours. |
| 2 | Resource requirement | §3: "A minimum of 3 pickers per shift travel to Site B." | BIA B-A2: "at least 4 pickers per shift". Register R-07: "Chilled dispatch: at least 4 pickers per shift" (owner: Dispatch lead) | **Disagree.** The plan has 3 pickers per shift, the BIA and register have 4. |
| 3 | Supplier (backup carrier) | §5: "Backup carrier: KuehlTrans, by spot booking." | BIA B-A2: "carrier: NordFrost, no second carrier recorded". Register R-08: "one carrier, NordFrost; second carrier open" (no owner named) | **Disagree.** The plan names a backup carrier. The BIA records none and the register lists a second carrier as open. |
| 4 | Supplier (primary carrier) | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | BIA B-A2: "carrier: NordFrost". Register R-08: "one carrier, NordFrost" | Agree |
| 5 | Contact (carrier escalation) | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | BIA B-A2: "carrier escalation: NordFrost control room" | Agree on the role. The BIA has no phone number to compare: "contact: to be confirmed". |
| 6 | Contact (duty manager) | §4: "Duty manager, Site A: 040 555 0172." | Not in the sources | No comparison possible: "contact: to be confirmed" |
| 7 | Resource (system) | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | BIA B-A2: "warehouse system LogiStock". Register R-09: "LogiStock restored within 6 hours" (owner: IT service owner) | Agree that LogiStock is a dependency. The plan gives no LogiStock recovery time, so I can't compare it with R-09's 6 hours. WI-14 wasn't attached. |

**Gaps, block 1**
- R-08 has no named owner, so there's no register owner to put finding 3 to.
- I only had an *extract* of BIA v2. Other parts of BIA v2, for example any Site B entries, are not in the sources.
- The plan's recovery option ("move chilled dispatch to Site B", §1) is a strategy choice. The approved strategy document wasn't attached, so I couldn't check whether Site B is the approved option.
- The plan's activation threshold ("more than two hours", §1) has no matching BIA value to compare: not in the sources.
- The contact numbers in §4 carry only the plan's own date (12 Mar 2026). No contact list with its own date was attached.
- I didn't use the change notice (15 Sep 2026, planned) as current in this block.

---

## Block 2: What the January carrier change reopens

Change notice, 15 Sep 2026: from **1 January 2027**, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to Polar Haul. "NordFrost's control room will no longer handle Site A loads from that date."

I searched only the six attached documents. Every entry below is **proposed, to confirm**, with no replacement value.

| Document | Section / entry | Line affected | Owner the sources name |
|---|---|---|---|
| Dispatch plan v3, 12 Mar 2026 | §4 Contacts | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Dispatch plan v3, 12 Mar 2026 | §5 Suppliers | "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | Head of Logistics |
| Dispatch plan v3, 12 Mar 2026 | §5 Suppliers | "Backup carrier: KuehlTrans, by spot booking." The notice says nothing about this backup, so it isn't clear whether the line is affected. | Head of Logistics |
| Dispatch plan v3, 12 Mar 2026 | §1 Scope | "Recovery option: move chilled dispatch to Site B." This option depends on the Site A–B trunking that is changing carrier. | Head of Logistics |
| Goods receipt plan v2, 3 Mar 2026 | §3 Inbound transport | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." | Warehouse lead |
| BIA v2, 4 Feb 2026 | B-A1 Goods receipt, chilled | "carrier: NordFrost, inbound trunking from Site B" | Activity owner: Warehouse lead. BIA owner: BCM manager |
| BIA v2, 4 Feb 2026 | B-A2 Dispatch, chilled | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Activity owner: Dispatch lead. BIA owner: BCM manager |
| Register v5, 10 Feb 2026 | R-08 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" | **None named** |

**Searched and not affected in the attached text:** quality release plan v1 (no carrier mentioned), BIA B-A3, and register entries R-06, R-07 and R-09.

**Gaps, block 2**
- R-08 has no named owner.
- The change notice has status "planned" and is dated 15 Sep 2026. I treated it as the change under review, not as current fact.
- The notice gives no Polar Haul escalation contact: "contact: to be confirmed".
- The goods receipt plan §3 gives an action to the *dispatch lead*, but the plan's owner is the Warehouse lead. When that line is reopened, both may need to confirm it.

**Coverage unknown.** These kinds of document could be affected by the change, but none were attached:
- contact lists and escalation lists, which may carry the NordFrost control room number
- supplier contracts: the NordFrost contract ending, and the new Polar Haul contract with any recovery or capacity terms for Site B relocation
- the supplier or third-party register and any supplier risk assessment
- the KuehlTrans spot-booking arrangement
- work instructions, including WI-14
- role or action cards drawn from the dispatch and goods receipt plans
- Site B plans and BIA entries
- the crisis or incident management plan
- the full BIA v2 beyond this extract
- the risk register
- the exercise schedule

> Parts of this document were drafted with AI support (check-against-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** run `units/prompts/review.md` on each plan flagged above:
- **Dispatch plan v3:** blocks 1 and 2. Its owner is the Head of Logistics.
- **Goods receipt plan v2:** block 2. Its owner is the Warehouse lead.
