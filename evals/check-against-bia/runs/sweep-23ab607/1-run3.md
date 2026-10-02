# /check-against-bia case 1, run3: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4536e83c-6312-485b-9afd-48726e9c20bd`.

Files in the working folder: `bia-extract-dispatch.md`, `change-trunking-supplier.md`, `plan-chilled-dispatch.md`, `plan-goods-receipt.md`, `plan-quality-release.md`, `requirements-register.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the BIA, and tell me what the new trunking carrier from January touches. The files bia-extract-dispatch.md, requirements-register.md, plan-chilled-dispatch.md, plan-goods-receipt.md, plan-quality-release.md and change-trunking-supplier.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the attached files, one question:

**What class of data do these documents hold?** For example: public, internal, confidential or strictly confidential, or whatever classes your organisation uses.

I'll go by your answer, not by any marking inside the files. If this environment isn't approved for that class, I'll stop there. If it is, I'll go ahead with both checks: the dispatch plan against the BIA, and what the January change of trunking carrier reopens. You'll get a report only, and none of your documents will be changed.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/preflight.md`
- Bash: `ls -la; ls -R /home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. The environment is approved for high-sensitivity data, so I've read the six files. Before I write the report, one question:

**Are there any other plans this check should cover that aren't in this folder?** For example, a Site B plan, a separate outbound transport or carrier plan, or a contact list or escalation sheet that names the carrier.

Whatever you tell me, I'll record under Gaps as your statement. If you skip the question, I'll assume these six files are the whole set and list each missing kind of document under "Coverage unknown".

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/stages/implement.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-bia/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run3/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run3/work/requirements-register.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run3/work/plan-chilled-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run3/work/plan-goods-receipt.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run3/work/plan-quality-release.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/check-against-bia/1/run3/work/change-trunking-supplier.md`

## Turn 3

**Request:** skip

**Reply (verbatim):**

# Draft: chilled dispatch plan against the BIA, and what the January carrier change reopens

**Sources (version and date):**
- `bia-extract-dispatch.md`: BIA v2, approved by top management 4 Feb 2026. BIA owner: BCM manager.
- `requirements-register.md`: Version 5, 10 February 2026, approved by the BCM manager, built from BIA v2.
- `plan-chilled-dispatch.md`: Version 3, 12 March 2026, approved. Plan owner: Head of Logistics.
- `plan-goods-receipt.md`: Version 2, 3 March 2026, approved. Plan owner: Warehouse lead.
- `plan-quality-release.md`: Version 1, 20 February 2026, approved. Plan owner: QA manager.
- `change-trunking-supplier.md`: dated 15 September 2026, **no version**, status "planned" (see Gaps).

---

## Block 1: Against the BIA (chilled dispatch plan vs BIA v2, entry B-A2)

Task: "compare the attached plan with the approved BIA and list where they disagree. Report only; change neither."

Each owner listed is **proposed, to confirm**. Each pair goes to both owners. The plan owner adapts the plan and keeps ownership, and the BIA activity owner decides for the BIA entry. I propose no replacement value and choose neither recovery time. A plan changes only with its owner's approval and a new version.

**1. Recovery time (RTO)**
- Plan, §2 Recovery objective (v3, 12 Mar 2026): "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3."
- BIA v2, B-A2 (4 Feb 2026): RTO "8 hours" (MTPD "24 hours").
- Owners: Head of Logistics (plan), proposed, to confirm. Dispatch lead (BIA activity), proposed, to confirm.

**2. Staffing**
- Plan, §3 Staffing (v3, 12 Mar 2026): "A minimum of 3 pickers per shift travel to Site B."
- BIA v2, B-A2 (4 Feb 2026): "at least 4 pickers per shift".
- Register v5, R-07 (10 Feb 2026): "Chilled dispatch: at least 4 pickers per shift".
- Owners: Head of Logistics (plan), proposed, to confirm. Dispatch lead (BIA activity and R-07), proposed, to confirm.

**3. Second carrier**
- Plan, §5 Suppliers (v3, 12 Mar 2026): "Backup carrier: KuehlTrans, by spot booking."
- BIA v2, B-A2 (4 Feb 2026): "carrier: NordFrost, no second carrier recorded".
- Register v5, R-08 (10 Feb 2026): "one carrier, NordFrost; second carrier open".
- Owners: Head of Logistics (plan), proposed, to confirm. Dispatch lead (BIA activity), proposed, to confirm. R-08: **none named** (see Gaps).

**4. Warehouse system (one side silent)**
- Plan, §6 Systems (v3, 12 Mar 2026): "Orders leave LogiStock by the manual export in work instruction WI-14." The plan does not say when LogiStock must be back: not in the sources.
- BIA v2, B-A2 (4 Feb 2026): "warehouse system LogiStock".
- Register v5, R-09 (10 Feb 2026): "LogiStock restored within 6 hours".
- Owners: Head of Logistics (plan), proposed, to confirm. Dispatch lead (BIA activity), proposed, to confirm. IT service owner (R-09), proposed, to confirm.

Carrier escalation agrees today. Plan §4 says "Carrier escalation: NordFrost control room, 040 555 0900" and B-A2 says "carrier escalation: NordFrost control room". Block 2 covers what the change does to this line.

---

## Block 2: What it reopens (change of trunking carrier, 1 January 2027)

Task: "the attached change is planned. Find which of the attached plans, BIA entries and register entries it reopens. Report only; change nothing."

The change, from `change-trunking-supplier.md` (15 Sep 2026): "From 1 January 2027, chilled trunking between Site A and Site B, and outbound chilled transport from Site A, moves from NordFrost to a new carrier, Polar Haul … NordFrost's control room will no longer handle Site A loads from that date."

Each owner is **proposed, to confirm**. I give no replacement value. Polar Haul's escalation contact: to be confirmed. The sources give none.

**Plans touched**

- **Chilled dispatch plan, §4 Contacts** (v3, 12 Mar 2026)
  - Line: "Carrier escalation: NordFrost control room, 040 555 0900."
  - Decides: Head of Logistics, proposed, to confirm.
- **Chilled dispatch plan, §5 Suppliers** (v3, 12 Mar 2026)
  - Line: "Trunking from Site A to Site B and outbound chilled transport: NordFrost. Backup carrier: KuehlTrans, by spot booking."
  - Decides: Head of Logistics, proposed, to confirm.
- **Goods receipt plan, §3 Inbound transport** (v2, 3 Mar 2026)
  - Line: "Inbound trunking from Site B: NordFrost. On the loss of the dock doors, the dispatch lead asks NordFrost to hold inbound loads at Site B."
  - Decides: Warehouse lead, proposed, to confirm. The step is carried out by the dispatch lead.

**BIA entries touched**

- **B-A1 Goods receipt, chilled** (BIA v2, 4 Feb 2026)
  - Line: "carrier: NordFrost, inbound trunking from Site B"
  - Decides: Warehouse lead (activity owner), proposed, to confirm. BIA owner: BCM manager.
- **B-A2 Dispatch, chilled** (BIA v2, 4 Feb 2026)
  - Line: "carrier: NordFrost, no second carrier recorded; carrier escalation: NordFrost control room"
  - Decides: Dispatch lead (activity owner), proposed, to confirm. BIA owner: BCM manager.

**Register entry touched**

- **R-08** (Register v5, 10 Feb 2026)
  - Line: "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open"
  - Decides: **none named** (see Gaps).

**Checked and not touched:**
- Quality release plan v1: no carrier or transport line.
- BIA entry B-A3: no carrier line.
- Register entries R-06, R-07 and R-09: no carrier line.

**Change trigger to keep:** a change of chilled carrier, or of a carrier's control room, reopens:
- the chilled dispatch plan §4 and §5
- the goods receipt plan §3
- BIA entries B-A1 and B-A2
- register entry R-08

---

## Gaps

- **Change notice, no version.** `change-trunking-supplier.md` is dated 15 Sep 2026 but has no version, and its status is "planned". It describes a future state, so I have not used it as current.
- **Owner not named.** Register R-08 has no owner. Its cell reads "none named", and I have inferred no owner from a department or role.
- **Polar Haul contact.** The sources give no escalation contact or control room for Polar Haul: contact to be confirmed.
- **KuehlTrans after January.** The change notice does not say whether KuehlTrans (dispatch plan §5) stays as a backup carrier: not in the sources.
- **BIA extract only.** I compared against an extract of BIA v2 for Site A chilled operations, not the full BIA.
- **Intake.** You skipped the question about plans not attached. Assumption: these six files are the whole set.
- **Instructions to an AI.** No passage in the attached files tells an AI to act. None was found.

## Reviewer

**You, as the BCM manager who asked for this check**, check each quoted passage against its source. Each plan owner and BIA activity owner then decides whether their document changes:
- Head of Logistics: chilled dispatch plan.
- Warehouse lead: goods receipt plan and B-A1.
- Dispatch lead: B-A2 and R-07.
- IT service owner: R-09.
- BCM manager: BIA v2 and the register.
- R-08: none named.

## Coverage unknown

These kinds of document were not attached, so I could not check whether the change reaches them:
- contact lists and escalation sheets
- Site B plans
- carrier contracts and agreements (NordFrost, Polar Haul, KuehlTrans)
- work instruction WI-14
- partner lab agreement QA-03
- LogiStock IT recovery plan
- crisis or incident management plan
- role or action cards
- the full BIA beyond this extract

---

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. ________ reviewed it on ________.

> Use review.md on plan-chilled-dispatch.md, with Head of Logistics: type /challenge-my-plan.

> Use review.md on plan-goods-receipt.md, with Warehouse lead: type /challenge-my-plan.

**Tool calls (stream-json):**

- none
