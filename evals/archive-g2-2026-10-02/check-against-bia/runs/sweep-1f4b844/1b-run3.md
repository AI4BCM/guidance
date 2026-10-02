# /check-against-bia case 1b, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `fb31d330-2dce-485d-8025-8153b869e485`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia New contract trunking supplier from january, what does it touch? The files change-trunking-supplier.md, bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md and plan-quality-release.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the six files, I need to know how sensitive they are. This check has to start with that question.

**What class of data do these files hold, and is this environment approved for it?**

Under the guidance's sensitivity classes (`units/data-rules.md`), several things in this set would count as **high** sensitivity:

- **BIA data:** `bia-extract-dispatch.md`.
- **Supplier dependencies and contract terms:** the trunking supplier change and any supplier details in the register.
- **Recovery strategies and requirements:** the requirements register and the three plans.
- **Contact lists and personal data:** any named people or phone numbers in the plans.

For this kind of work, the tool selection guide allows high-sensitivity data only in an approved enterprise or private environment, or on a purpose-built BCM platform (`units/tools.md`). Please confirm one of these:

1. These files are high sensitivity, and this Claude Code session runs in an environment your organisation has approved for that. I'll go ahead.
2. They are lower sensitivity, for example fictional, training or anonymised material. Tell me the class and I'll go ahead.
3. They are high sensitivity and this environment isn't approved for it. I'll stop and read nothing.

Once you answer, I'll read the files. After that I'll ask only what they leave open, then return a draft in the chat. It will cover the plans, BIA entries and register entries the January supplier change reopens, and any kinds of documents I couldn't see. I won't edit any file.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read all six files. They're enough for the check, but three things are still open. Answer whichever you can, and say "skip" for the rest. I'll record your answers as your own statements, not as sources. They can change what I search, but they won't fill in any value.

1. **Other documents to search.** I have only the three Site A plans, the BIA extract and the register. Could the change also touch any of these?
   - contact or call-out lists, or escalation routes
   - the NordFrost or Polar Haul contracts
   - work instruction WI-14
   - the KuehlTrans spot-booking arrangement
   - any Site B plans

   If you can attach any of them, I'll search them too. If not, I'll list each one as "coverage unknown".
2. **Inbound direction.** The notice says "chilled trunking between Site A and Site B". Does that include inbound trunking from Site B to Site A? The goods-receipt plan v2 §3 depends on that leg. If you skip this, I'll assume "between" means both directions and flag that as an assumption.
3. **Other parts of the same change.** Does the procurement change cover anything beyond the carrier swap? For example, does it end, keep or replace the KuehlTrans backup by spot booking, or add Polar Haul as a second carrier rather than a straight replacement? If you skip this, I'll assume a straight replacement, as the notice describes, and flag that too.

## Turn 3

**Request:** skip

**Reply (verbatim):**

# Draft: what the January carrier change reopens

**What this draft is based on**
- Change notice "chilled trunking carrier", dated 15 Sep 2026, planned and approved by the procurement board. It has no version number.
- BIA extract for Site A chilled operations, from BIA v2, approved 4 Feb 2026.
- Requirements register Site A, v5, 10 Feb 2026, approved.
- Chilled dispatch recovery plan v3, 12 Mar 2026, approved.
- Chilled goods receipt recovery plan v2, 3 Mar 2026, approved.
- Quality release recovery plan v1, 20 Feb 2026, approved.

**Reviewer:** you, as the BCM manager who asked, check each quoted passage against its source. Each plan owner and each BIA activity owner decides whether their document changes. A plan changes only with its owner's approval and a new version. I have changed no file.

Only a change was attached, with no plan sent for checking, so there is no "Against the BIA" section. The whole draft is the "What it reopens" check.

---

## What it reopens

The change, quoted from the notice dated 15 Sep 2026: *"From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul, under a new contract. NordFrost's control room will no longer handle Site A loads from that date."*

Every row below is **proposed, to confirm**. No replacement values are given.

### Plans

| Document | Section | Line touched (quoted) | Owner named in the source |
|---|---|---|---|
| Chilled dispatch plan v3, 12 Mar 2026 | §4 Contacts | "Carrier escalation: NordFrost control room, 040 555 0900." | Head of Logistics |
| Chilled dispatch plan v3, 12 Mar 2026 | §5 Suppliers | "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking." | Head of Logistics |
| Chilled dispatch plan v3, 12 Mar 2026 | §1 Scope | "Recovery option: move chilled dispatch to Site B." This recovery option depends on the Site A to Site B trunking leg that is moving to the new carrier. | Head of Logistics |
| Goods receipt plan v2, 3 Mar 2026 | §3 Inbound transport | "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B." This row assumes "between Site A and Site B" covers the inbound direction (see Gaps). | Warehouse lead |
| Quality release plan v1, 20 Feb 2026 | All sections searched | No carrier, trunking or NordFrost line. Nothing touched in the attached text. | QA manager |

### BIA entries (BIA v2, approved 4 Feb 2026; the BIA's owner is the BCM manager)

| Entry | Line touched (quoted) | Activity owner |
|---|---|---|
| B-A1 Goods receipt, chilled | "carrier: NordFrost, inbound trunking from Site B" | Warehouse lead |
| B-A2 Dispatch, chilled | "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room" | Dispatch lead |
| B-A3 Quality release | Searched. No carrier dependency. Not touched. | QA manager |

### Register entries (register v5, 10 Feb 2026)

| Ref | Line touched (quoted) | Owner named in the source |
|---|---|---|
| R-08 | "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open" (source: "BIA v2, B-A1, B-A2") | **None named.** Listed under Gaps. |
| R-06, R-07, R-09 | Searched. No carrier dependency. Not touched. | QA manager, Dispatch lead, IT service owner |

### Gaps
- **R-08 has no owner.** The register's Owner cell for R-08 is blank. This is the requirement most directly affected by the change.
- **The change notice has no version number.** It has a date (15 Sep 2026) and a status ("planned, approved by the procurement board"), and it was raised by the Head of Procurement. Because it is a planned change, it is used here only as the trigger, not as current state.
- **Your skipped intake questions became three assumptions.** You answered "skip", so I worked on these assumptions:
  - "Between Site A and Site B" covers both directions, so the inbound leg in goods receipt §3 and B-A1 is included.
  - Polar Haul is a straight replacement for NordFrost. Whether the KuehlTrans spot-booking backup continues is not in the sources.
  - No further documents were available to search.
- **The BIA was only an extract.** It covers Site A chilled operations. Other BIA entries that rely on NordFrost, such as Site B activities, were not seen.
- **Polar Haul's escalation arrangements are not in the sources.** That covers its control room and contact route.
- **No instructions to an AI were found** in any of the attached files.

### Coverage unknown
These are kinds of document the change could touch that were not attached:
- contact lists, call-out lists and escalation routes that name the NordFrost control room
- supplier contracts and agreements: NordFrost (including exit terms and the notice period up to 1 Jan 2027), Polar Haul, and the KuehlTrans spot-booking arrangement
- the supplier register and the risk register, including entries on carrier concentration or single-carrier risk
- Site B recovery plans and Site B BIA entries
- the parts of the full BIA v2 beyond this extract
- work instructions that hand loads to the carrier. WI-14 is cited in dispatch plan §6, but its content was not attached.
- role or action cards based on the dispatch or goods receipt plans
- the incident management and crisis communication plans, and exercise schedules that use NordFrost in a scenario

---

**Next step:** run [`units/prompts/review.md`](units/prompts/review.md) on each flagged plan: the **chilled dispatch plan v3** (Head of Logistics) and the **goods receipt plan v2** (Warehouse lead).

*Outside this check:* I also spotted some places where the chilled dispatch plan v3 and BIA v2 may disagree, separate from the carrier change. They concern recovery time, picker numbers and a backup carrier the BIA doesn't record. I didn't check them here. If you'd like, I can run the plan-against-BIA check on that plan.

> Parts of this document were drafted with AI support (check-against-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
