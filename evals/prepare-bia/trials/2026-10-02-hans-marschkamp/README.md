# /prepare-bia real-work trial: Hans on Marschkamp, 2026-10-02

Hans (seat `hans`, the BCM-user persona: 25 years in BC, sceptical of AI) prepared a BIA interview with Sven Hollmann,
Head of Chilling, Storage & Dispatch at Marschkamp (synthetic demo company), with `/prepare-bia` at skills/2026.11
`94748ab`+ (skill text as at `88370c8`). The skill ran in a clean Claude Code run with the eval flags (no MCP, no
memory, Read/Glob/Grep only); the estate clock relayed each turn word for word in Buzz `#skills-trial-prepare-bia`.
Attached: company-profile.md, org-and-roles.md, impact-criteria.md, dependency-register.json, supplier-sla.md,
25_04_15_prior-bia.md (read live from marschkamp via bia-file). One sentence naming the six files as attached was
added to Hans's first message, as in the eval cases. Files unchanged after every turn.

**Relay error (coordinator):** Hans's data-class answer reached the tool twice (turn 3); the tool read the repeat
as "skip" and drafted on its stated assumptions, listed under Gaps. Hans's intake answers then went through as
turn 4 and the tool revised the draft. Disclosed to Hans in the channel.

## Turn 1

**Hans (as typed into the tool):**

> /prepare-bia bia interview with sven hollmann, head of chilling storage and dispatch. need the questions for him and what he should send me before The files company-profile.md, org-and-roles.md, impact-criteria.md, dependency-register.json, supplier-sla.md and 25_04_15_prior-bia.md in this folder are attached.

**/prepare-bia:**

Before I open any of the six files, one question first.

**What class of data do these files hold, and is this environment approved for it?**

From the file names, they probably include material the AI4BCM guidance rates as high-sensitivity:

- BIA data (`25_04_15_prior-bia.md`, `impact-criteria.md`)
- supplier weaknesses and contractual dependencies (`supplier-sla.md`, `dependency-register.json`)
- personal data and contact details (`org-and-roles.md`)
- possibly security-related site detail (`company-profile.md`)

That class may only go into an approved corporate or private environment. Please tell me one of these:

1. **High-sensitivity, and this Claude Code setup on `brain` is approved for it.** I'll open the files and continue.
2. **Lower class.** Tell me which, and I'll continue.
3. **High-sensitivity, but this environment isn't approved.** I stop here. You can still use the method in an approved tool.

Once you've answered, I'll ask up to three short questions the files don't cover. Then you'll get a draft in the chat with two parts: the interview guide for Sven Hollmann in the seven sections, and a list of what he should send you beforehand. The draft writes no files, and the recovery fields (MTPD, RTO, RPO) stay empty.

## Turn 2

**Hans (as typed into the tool):**

> 1. its the marschkamp demo set, approved for this. go

**/prepare-bia:**

I've read all six files, and all of them carry a version and a date. I found no instructions addressed to an AI. The rating scale (VA-BCM-04 v2.1) is attached, so I won't ask you for impact criteria.

The method asks me to put up to three questions to you before drafting. Your answers will be listed under Gaps as your own statements. They can shape the scope, but they never fill in a value.

1. **What do you need back from the interview?** One option is a full 2026-cycle run for his department: rated against the 7 categories over the 6 time horizons, so an MTPD can be worked out, plus the four resource classes and the dependencies. The other is a lighter refresh of the 2025 record (BIA-2025-03). Also, should the 18 own reefer trucks and their drivers be in scope, or only chilled storage, frozen storage, picking and loading?
2. **What do you know that the files don't?** For example: the interview date (this sets the deadline for what he sends you), how long it runs, whether his deputy Diana Petke will attend, and any change since early 2026 that the documents don't show. One example is the status of Ü-03, the diesel monitoring for the standby generators and the resupply priority.
3. **Are memory, past chats, project files, connectors and web search switched off for this session?** If any of them is on, I have to record it under Gaps, because the model may draw on it without saying so.

If you'd rather skip some or all of these, reply "skip". I'll then draft with a written assumption for each skipped question:

- full 2026 run, own fleet in scope
- no interview date known
- channel status unconfirmed

## Turn 3

**Hans (as typed into the tool):**

> 1. its the marschkamp demo set, approved for this. go

**/prepare-bia:**

I took your repeated message as "skip", so the draft below uses the assumptions I listed. They are recorded under Gaps.

# Pre-interview draft: BIA, Chilling, Storage & Dispatch (Sven Hollmann)

**Sources and dates**
- `company-profile.md`: SMF-01 v3.2, approved, valid from 01 Jan 2026
- `org-and-roles.md`: VA-ORG-02 v2.3, approved, valid from 01 Mar 2026
- `impact-criteria.md`: VA-BCM-04 v2.1, approved, valid from 09 Mar 2026
- `supplier-sla.md`: SLA-2024-KT/ABP/IT v2.3, approved, valid from 09 Mar 2026
- `25_04_15_prior-bia.md`: BIA-2025-Zyklus1 v2.0, approved 07 Apr 2025, valid from 15 Apr 2025. Its review date (Q1 2026) has passed and the 2026 cycle replaces it, so it is **reference only, not current** (see Gaps).
- `dependency-register.json`: **no version, no date**. I used it only to frame questions, never as a current value (see Gaps).

Short references below: SMF, ORG, CRIT, SLA, BIA-25, DEP (the dependency register, undated).

## 1. Candidate activities and resource requirements

Every entry is labelled **candidate, to confirm**. MTPD, RTO and RPO stay blank; Sven sets them.

**Activities**

| # | Candidate activity (question for S. Hollmann) | Source | MTPD |
|---|---|---|---|
| A1 | Is chilled storage at +2 °C (6,800 pallet spaces) one of your activities, as it stands? | SMF §2, §3, §4 | |
| A2 | Is frozen storage at −22 °C (3,200 pallet spaces), including intake from the blast freezer (KA-02), yours? | SMF §3; SLA A.2; DEP KA-02 | |
| A3 | Is "carcass chilling after slaughter" yours or Slaughter's? Only the undated register assigns it to your department. | DEP AN-SCHLACHT-01 | |
| A4 | Picking and loading at the docks: is this one activity or two? | SMF §2, §3 | |
| A5 | Outbound refrigerated transport (18 own reefer trucks plus contract trunking): is this yours end to end? | SMF §2, §4, §10 | |

**Resource requirements**

| # | Act. | Class | Candidate requirement (question) | Source | RTO | RPO |
|---|---|---|---|---|---|---|
| R1 | A1–A5 | People | What minimum crew per shift do storage, picking and loading need, and with which skills (forklift, cold-store work)? | Gaps (not in the sources) | | |
| R2 | A1–A5 | People | Who besides you and Diana Petke may block or release stock after a temperature excursion, and sign dispatch documents? | ORG §2, §4; CRIT §4.5 level 4 ("blocked stock") | | |
| R3 | A5 | People | How many drivers do the 18 own trucks need per day, and who stands in for them? | SMF §4 (fleet); driver numbers: Gaps | | |
| R4 | all | People | You lead the "cold chain / storage / dispatch situation" in a crisis (ext. -130). Is that mandate current, and are your contact details on the alerting list? That list's update is overdue. | ORG §4; ORG §6 ORG-2026-02 | | |
| R5 | A1, A2 | Seats & buildings | Which chambers are on the standby generators? The profile says they secure "chill store + controls, NOT the full line". | SMF §7 (Power) | | |
| R6 | A4 | Seats & buildings | Are the docks, doors and dock levellers on a standby circuit, or does loading stop when the grid fails? | SMF §7; Gaps | | |
| R7 | A1, A2 | Seats & buildings | Is there any off-site cold or frozen capacity you could move stock to? | DEP KA-02 ("external frozen capacity"); otherwise Gaps | | |
| R8 | A4, A5 | IT | SAP S/4HANA + MES for delivery notes, picking and the loading list: what does your manual fallback cover, and for how long? | SMF §9; DEP IT-ERP-01 | | |
| R9 | A4 | IT | Weighing and labelling system, used for dispatch weighing | SMF §9; DEP IT-WAAGE-01 | | |
| R10 | A4, A5 | IT | Batch traceability, needed to release goods for dispatch | SMF §9 | | |
| R11 | A1–A5 | IT | Do you run a warehouse system, temperature monitoring and alarms, telematics or tour planning outside SAP? | Gaps (not in the sources) | | |
| R12 | all | IT | Time recording and access control at the hygiene locks | SMF §9 | | |
| R13 | A5 | Suppliers | Elbe-Kühllogistik (SPED-2024-03) is the only contract haulier named. Is there a second one? | SMF §10; BIA-25-03 ("single trunking contract") | | |
| R14 | A1, A2 | Suppliers | Frostmark (KT-2023-11) for the refrigeration plant (KA-01) and blast freezer (KA-02). Do you know the escalation path? | SLA A.4, A.8 | | |
| R15 | A1, A2 | Suppliers | Grid supply (Küstennetz) and diesel resupply for the standby generators. Who supplies the diesel, and is there a priority agreement? | SMF §7; BIA-25 Part C Ü-03 | | |
| R16 | A4, A5 | Suppliers | Systemhaus Nord IT (IT-2022-04) for SAP and weighing | SLA C | | |

**Dependencies on other departments**

The RTO stays blank, and so does any date by which a dependency must be restored.

| # | Direction | Candidate dependency (question) | Source | RTO |
|---|---|---|---|---|
| D1 | Upstream | Maintenance (Wohlleben): refrigeration plant, blast freezer, power | DEP KA-01, KA-02; SMF §7 | |
| D2 | Upstream | Cutting (Louven) and Packing: who owns Packing today? Janne Ruser appears only in the 2025 BIA. | SMF §2; BIA-25-05; DEP AN-ZERLEG-01 | |
| D3 | Upstream | Slaughter (Ahlgrim): carcasses into chilling | DEP AN-SCHLACHT-01 | |
| D4 | Upstream | IT (Sobotta): SAP, weighing, traceability | SMF §9 | |
| D5 | Downstream | QA (Sauer): chamber temperature evidence for HACCP releases | DEP KA-01 (consumer "qs"); CRIT §4.5 | |
| D6 | Downstream | Sales (Cramer): on-time-in-full (OTIF) delivery to retail; Kornmark is 27% of revenue | SMF §11; DEP LF-SPED-01 | |
| D7 | Lateral | If NTV fails to collect animal by-products, Category 3 material "must be stored chilled (cooling ≤ +7 °C)". Whose chilled space takes it? | SLA B.3 | |

**Recovery times the sources propose (not set, not changed)**
- **BIA-25-03** (approved 2025, reference only): "Cold chain 0 h · Dispatch/transport 24 h", MTPD "48 h (dispatch)". 48 h is one of the time horizons in CRIT §3. These values came from prose, not from a rating grid, so I can't check them against the level-4 threshold.
- **Refrigeration plant (KA-01)**: register 4 h (DEP, undated) and BIA-25-04 4 h, against **Frostmark's P1 recovery time of 8 h** (SLA A.4). In addition, "force majeure (including grid outage …) suspends the deadlines" (SLA A.9).
- **Blast freezer (KA-02)**: 8 h (DEP, undated). **Haulage (LF-SPED-01)**: 24 h (DEP, undated); "cold store backs up in ≈ 1 day".
- **SAP/MES**: RTO 8 h, RPO 4 h (SMF §9; SLA C.4). The RPO is in the CRIT §5 vocabulary. But a 6 h outage (INC-2025-031) already caused a Kornmark OTIF miss with a penalty (DEP IT-ERP-01).
- **NTV**: "replacement collection within 24 h" (SLA B.5).
- **Fit with the impact criteria**: not decidable until Sven rates his own grid. Under the MIN principle, these upstream clocks can tighten his MTPD (CRIT §7).

## 2. Interview guide for Sven Hollmann

**Opening, to say to him:** "Use the draft as the thing to correct, not the thing to confirm; record what it could not have known."

1. **Impacts over time.** For each of A1–A5, take the loss of the activity and rate all 7 categories in CRIT §4 at each horizon: 0–4 h, 8 h, 24 h, 48 h, 72 h, 1 week.
   - How long does a full chill store hold temperature with the doors shut? The frozen store? The 2025 record says only "a few hours" and "holds longer".
   - From which point is stock blocked, and from which point is it written off?
   - When does a retail OTIF miss start, and when do penalties from several customers start? Do the peak periods (May–August; weeks 48–51) change the answer?
   - Check that each series only rises (CRIT §3).
2. **MTPD.** At which horizon does the worst category first reach level 4? Do any upstream clocks (D1–D4, D7) arrive earlier?
3. **People, "with the skills, authorities and mandates the work needs".** Minimum crew per shift (R1). Who holds the release and blocking authority (R2), and who covers for it at night or on weekends? Drivers (R3). Your crisis role and whether Diana Petke is fully briefed (R4). What happens if the person who knows the chamber alarms is absent?
4. **Seats and buildings.** Which chambers, docks and controls run on the standby generators (R5, R6)? Which chamber gets priority? Is there off-site capacity (R7)? Is the Category 3 interim cooling space (D7) yours?
5. **IT and applications, "each with its RTO and its RPO".** SAP/MES, weighing and traceability (R8–R10), plus any systems the sources don't name (R11). How long can you dispatch on paper? Is a rebuilt order state 4 h old acceptable to you? What did INC-2025-031 show?
6. **Suppliers and other third parties.** Elbe-Kühllogistik is the only contract haulier named (R13): who else could take loads, and at what notice? Frostmark (R14). Diesel resupply and its priority during a wide-area grid outage (R15, Ü-03). Systemhaus Nord IT (R16). Each single supplier named here is a question for Sven, not a finding.
7. **Dependencies, each recorded with the RTO the relationship carries.**
   - Upstream: D1 Maintenance, D2 Cutting and Packing, D3 Slaughter, D4 IT.
   - Downstream: D5 QA, D6 Sales.
   - Lateral: D7 animal by-products.
   - For each one, ask: by when must it be back for your activity to hold, and by when must you deliver for theirs?

## 3. What Sven should send before the interview

1. A chamber and zone list: which chambers are on the generators, typical and peak occupancy, and the share held for A-customers.
2. Temperature trend or alarm records from past outages, including the chambers during INC-2025-014 (03 May 2025). This is the evidence for how long the store holds temperature.
3. Status of **Ü-03**: is the generator diesel level monitored, and who resupplies it with what priority? Evidence, if he has it.
4. The shift and staffing plan for storage, dispatch and drivers, with the key roles and deputies (headcount only, no personal data needed).
5. **The contract or SLA with Elbe-Kühllogistik (SPED-2024-03)**, which the SLA extracts don't contain, plus any other haulier or external cold-store agreements.
6. His manual dispatch procedure for an SAP outage, and the lessons learned from INC-2025-031.
7. The delivery windows and OTIF terms he works to for Kornmark, Frischwert, MetroLine and export (with Sales if needed).
8. A list of every system he uses beyond SAP/MES (warehouse system, temperature monitoring, telematics, EDI).
9. Anything in his area that has changed since the 2025 record (BIA-2025-03).

## 4. Conflicts to put to the two owners (single site, so no conflicts between sites)

This is one integrated site (SMF §1), so the method's comparison of registers across sites has nothing to compare. These conflicts are between sources at that one site:

- **Refrigeration plant recovery, 4 h vs Frostmark's 8 h P1 time**: to Hollmann and Wohlleben.
- **Generator diesel monitoring**: "not monitored" (BIA-25-03, Ü-03 open) against "Diesel level monitored since PIR-2025-004" (DEP UV-STROM-01). To Hollmann and Wohlleben, who both own Ü-03.
- **SAP RTO of 8 h against a 6 h outage that already drew a Kornmark penalty**: to Hollmann and Sobotta, with Cramer.
- **Redundant compressor**: target date 30 Sep 2026 (SMF §7), two days ago, status unknown. To Wohlleben, for Hollmann.
- **Category 3 chilled interim storage**: to Hollmann and Sauer/Templin.

## Gaps

- **Your answers (own statements, not sources):** you skipped the intake questions. My assumptions:
  - a full 2026-method run, with the own fleet in scope;
  - no interview date known, so the send-before deadline is open;
  - status of memory, past chats, project files and connectors not confirmed by you (the model may draw on any of them without saying so); this session read only the six files and the skill's units, and used no web search.
- **DEP has no version and no date.** It is not used as current; settle it with a dated, approved version. It cites `COMPANY-BIBLE.md` and `asset-inventory.md`, which weren't attached.
- **BIA-2025-Zyklus1**: review date (Q1 2026) passed, replaced by the 2026 cycle. Its metadata reads `source: ai`, so the prior record may itself have been AI-drafted.
- **CRIT** says `method.json` "governs the calculation" where the two differ. It wasn't attached.
- **The Environment category calibration** was due to be aligned with the discharge permit by 30 Sep 2026, owner Templin. Status not in the sources.
- **Referenced but not attached**: FB-INST-11, VA-QS-07, the emergency/alerting plan, GP-MK-2024-A, SPED-2024-03.
- **Not in the sources**: dispatch and warehouse staffing; how long the frozen store holds temperature; systems outside SAP; the diesel supplier; who manages the haulage contract while the Head of Purchasing post is vacant; the current owner of Packing.

## Reviewer and audit fields

- **Activity owner:** Sven Hollmann (deputy Diana Petke). He confirms each requirement and sets MTPD and RTO.
- **Top management approves the BIA results:** Dr Reinhard Kettler, Managing Director. BC and BIA documents go to him, not to the Plant Manager (ORG §1).
- **Each register entry carries** "the source, the interview it came from and the date behind each entry". In this draft the interview, the confirmation date and "the recovery times the owner set" are blank.

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

## Turn 4

**Hans (as typed into the tool):**

> full 2026 run, trucks and drivers in scope. no date yet, plan 90 min, petke if he brings her. no idea on ü-03, ask him. 3 i dont know its a clean run, put it under gaps

**/prepare-bia:**

I've added your answers to the draft as your own statements, not as sources. Only the parts below change; everything else in the draft stays as it was.

## Changes to section 2: interview guide, timed for 90 minutes

| Time | Section | Note |
|---|---|---|
| 0–5 | Opening | "Use the draft as the thing to correct, not the thing to confirm; record what it could not have known." |
| 5–30 | 1. Impacts over time | Activities A1–A5 against 7 categories and 6 horizons. This is the biggest block; don't cut it. |
| 30–40 | 2. MTPD | |
| 40–52 | 3. People | Includes trucks and drivers (A5, R3). If Diana Petke attends, put R2 and R4 to her as well: who covers the release and blocking authority, and is she briefed for the crisis role? |
| 52–60 | 4. Seats and buildings | **Ask him about Ü-03 here**: is the diesel for the standby generators monitored, and is there a resupply priority? You have no information on it, so his answer is the first source. |
| 60–70 | 5. IT and applications | |
| 70–78 | 6. Suppliers and third parties | Haulage (Elbe-Kühllogistik and the own fleet); diesel resupply (Ü-03, follow-up). |
| 78–88 | 7. Dependencies | |
| 88–90 | Close | Agree what he still owes you, and the date by which he confirms the record. |

If time runs short, sections 6 and 7 can go to a 30-minute follow-up. Sections 1 and 2 can't.

## Changes to section 3: what he should send

- **Deadline:** not set, because there's no interview date yet. Give him one when you fix the date.
- **Item 3, Ü-03:** ask him for whatever evidence he has. You have nothing on it.

## Gaps (this section replaces the earlier one)

- **Your statements (own statements, not sources):**
  - Scope: a full 2026-method run, with trucks and drivers in scope.
  - The interview has no date yet; you plan 90 minutes.
  - Diana Petke attends only if Sven brings her.
  - You have no information on Ü-03; Sven is to be asked.
  - You don't know whether memory, past chats, project files or connectors are on, and you describe this as "a clean run". **That status stays unconfirmed:** the model may draw on any channel that is on without saying so. This session read only the six files and the skill's units, and used no web search.
- **DEP has no version and no date.** It is not used as current; settle it with a dated, approved version. It cites `COMPANY-BIBLE.md` and `asset-inventory.md`, which weren't attached.
- **BIA-2025-Zyklus1**: review date (Q1 2026) passed, replaced by the 2026 cycle. Its metadata reads `source: ai`, so the prior record may itself have been AI-drafted.
- **CRIT** says `method.json` "governs the calculation" where the two differ. It wasn't attached.
- **The Environment category calibration** was due to be aligned with the discharge permit by 30 Sep 2026, owner Templin. Status not in the sources.
- **Ü-03 (generator diesel monitoring and resupply priority):** the sources contradict each other (BIA-25-03 against DEP UV-STROM-01), and you have no information. Settled by Sven's answer plus Wohlleben's.
- **Referenced but not attached**: FB-INST-11, VA-QS-07, the emergency/alerting plan, GP-MK-2024-A, SPED-2024-03.
- **Not in the sources**: dispatch, warehouse and driver staffing; how long the frozen store holds temperature; systems outside SAP; the diesel supplier; who manages the haulage contract while the Head of Purchasing post is vacant; the current owner of Packing.

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

## Hans's verdict

> better, the timing helps and ü-03 sits in the right place. id take it in
> but 25 min for 5 activities x 7 categories x 6 horizons is still 200 ratings, wont happen. rate chill and frozen store fully, the rest only where it changes
> put the section 4 conflicts in the first 10 min, frostmark 8h vs our 4h and the cat 3 chilled space are the best questions in there. and the opening line goes, i dont talk to sven like that
