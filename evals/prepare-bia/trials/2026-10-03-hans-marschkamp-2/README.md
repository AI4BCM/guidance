# /prepare-bia real-work trial 2: Hans on Marschkamp, 2026-10-03

The same job as trial 1 (`../2026-10-02-hans-marschkamp`): the BIA interview with Sven Hollmann, Head of Chilling,
Storage & Dispatch, the same six Marschkamp files, after the owner's fit-and-tone change (`f0644bf`, borrowed from
nemo: impacts rated in full only for the top one or two activities; a take-in sheet of plain spoken questions,
conflicts first, fitted to the interview length). Clean Claude Code run with the eval flags; the estate clock relayed
each turn word for word in Buzz `#skills-trial-prepare-bia`; files unchanged after every turn; no relay error.

| Class | Trial 1 | Trial 2 |
|---|---|---|
| Questions | 8 | 9 |
| Sources | 8 | 8 |
| Data and safety | 9 | 9 |
| Fit | 4 | 7 |
| Tone | 4 | 8 |
| Overall | 7 | 8 |

## Turn 1

**Hans (as typed into the tool):**

> /prepare-bia bia interview with sven hollmann, head of chilling storage and dispatch. need the questions for him and what he should send me before  The files company-profile.md, org-and-roles.md, impact-criteria.md, dependency-register.json, supplier-sla.md and 25_04_15_prior-bia.md in this folder are attached.

**/prepare-bia:**

Before I open any of the six files, I need one answer from you. The skill's preflight requires this as its first step.

**What class of data do these files hold, and is this environment approved for it?**

From the file names, the material probably falls under the guidance's **high-sensitivity** class. That class covers BIA data, supplier weaknesses and contractual dependencies, personnel and contact details, and site detail. High-sensitivity material may only go into an approved corporate or private environment. Please confirm two things:

1. the class (high-sensitivity, or something lower if your own scheme classifies it differently), and
2. that this Claude Code environment on `brain` is approved for that class under your organisation's rules.

If it isn't approved for that class, I'll stop here.

Once you've answered, I'll send one message with up to three intake questions: what Sven knows that you don't, what you need back from the interview, and whether memory, connectors and web search are off. Then I'll draft his interview guide and the list of things to ask him to send you beforehand.

## Turn 2

**Hans (as typed into the tool):**

> high sensitivity, its the marschkamp demo set and this setup is approved for it. go

**/prepare-bia:**

I've read all six files. Before I draft, I have three intake questions (this is step 1 of the skill). The files already cover Sven's role, his deputy, the impact criteria and the prior cycle, so I won't ask about those.

1. **How long is the interview, and what do you need back from it?** Is this the 2026 method-based run that replaces the 2025 prose entry for chilled/frozen store and dispatch (BIA-2025-03)? That would mean full impact-over-time ratings against your current impact criteria (VA-BCM-04 v2.1, seven categories × six time horizons). Or do you only need an update on what changed?
2. **What do you know about Sven's area that isn't in these files?** For example, changes since March 2026, incidents, or the current state of the open actions on diesel monitoring (Ü-03) and the redundant compressor, which was due 30 Sep 2026. I'll list your answers as your own statements, not as sources, so they can shape the questions but never fill in a value.
3. **Are memory, past chats, project files, connectors and web search switched off for this session?** If any of them is on, I'll record it under Gaps.

If you skip a question, I'll write down the assumption I made instead and carry on. In the meantime, here is what I've noted while reading:

- **Missing version and date:** `dependency-register.json` has neither, so it will go under Gaps.
- **One conflict between sources:** the 2025 BIA says the standby generators' diesel level was "not monitored". The dependency register says "Diesel level monitored since PIR-2025-004". That will be one of the first questions for Sven.
- **No cross-site comparison:** the site profile describes a "single integrated site", so step 4 of the method (comparing registers across sites) doesn't apply.

## Turn 3

**Hans (as typed into the tool):**

> 90 min, full 2026 run replacing bia-2025-03, trucks and drivers in scope. no date yet, petke if he brings her. no idea on ü-03 or the compressor, ask him. 3 i dont know its a clean run, put it under gaps

**/prepare-bia:**

# BIA preparation: Chilling, Storage & Dispatch (Sven Hollmann), 2026 cycle

**Draft for the organiser, written only in this chat.** Every entry is "candidate, to confirm". MTPD, RTO and RPO are blank everywhere. The two things you asked for are the **pre-interview request to Sven** (§F) and the **take-in sheet** (§G). §A–§E are the guide and draft register they come from.

## Sources

- **SMF-01** Site Profile / Site Master File: v3.2, approved, valid from 01 Jan 2026 (`company-profile.md`)
- **VA-ORG-02** Organisation chart, key and emergency roles: v2.3, approved, valid from 01 Mar 2026 (`org-and-roles.md`)
- **VA-BCM-04** BIA rating scale (impact criteria): v2.1, approved, valid from 09 Mar 2026 (`impact-criteria.md`)
- **SLA-2024-KT/ABP/IT** Supplier SLA extracts: v2.3, approved, valid from 09 Mar 2026 (`supplier-sla.md`)
- **BIA-2025-Zyklus1** Prior-cycle BIA: v2.0, approved 07 Apr 2025, next review Q1 2026. It is the prior cycle that this run replaces, used for reference only (`25_04_15_prior-bia.md`)
- **DEP-REG** Dependency register: **no version, no date, no approval.** It is listed under Gaps and used only as a source of questions (`dependency-register.json`)

---

## A. Candidate activities

| ID | Candidate activity (question for Sven) | Source | MTPD | Interview | Confirmed on | Mark |
|---|---|---|---|---|---|---|
| A1 | Is chilled storage at +2 °C (6,800 pallet spaces), including the temperature evidence used for release, one of your activities? | SMF-01 §2, §3, §4; DEP-REG KA-01 | | | | candidate, to confirm |
| A2 | Is frozen storage at −22 °C (3,200 spaces), including intake from the blast freezer, one of your activities? | SMF-01 §3; DEP-REG KA-02 | | | | candidate, to confirm |
| A3 | Does carcass chilling after slaughter belong to you or to Slaughter? | DEP-REG AN-SCHLACHT-01 (consumer "kuehlung-lager-versand") vs KA-01 (consumer "schlachtung") | | | | candidate, to confirm |
| A4 | Picking, loading, dispatch weighing and dispatch documents | SMF-01 §2 ("picking, loading"); DEP-REG IT-ERP-01, IT-WAAGE-01 | | | | candidate, to confirm |
| A5 | Refrigerated transport: the 18 own reefer trucks with their drivers, plus contract trunking | SMF-01 §2, §4, §10; DEP-REG LF-SPED-01; organiser: "trucks and drivers in scope" | | | | candidate, to confirm |

**Full impact-over-time rating applies to A1 and A5.** The 2025 record singles these two out as the area's clocks: "Cold chain 0 h · Dispatch/transport 24 h" (BIA-2025-03). For A2, A3 and A4, ask only where they differ.

## B. Candidate resource requirements

### People, with the skills, authorities and mandates the work needs

| ID | Question for the owner | Act. | Source | Interview | Confirmed on | Mark |
|---|---|---|---|---|---|---|
| P1 | You lead the "Cold chain / storage / dispatch situation" in the crisis team, with Diana Petke as deputy. Who takes over if neither of you is available? | all | VA-ORG-02 §4 | | | candidate, to confirm |
| P2 | What is the minimum crew per dispatch shift (pickers, forklift drivers, loaders), and which skills or licences do they need? | A4 | not in the sources | | | candidate, to confirm |
| P3 | How many drivers do the 18 own reefer trucks need per day? Which licences and qualifications do they need? Do you use agency drivers? | A5 | SMF-01 §4 (fleet); headcount not in the sources | | | candidate, to confirm |
| P4 | Who has the mandate to block or release stock after a temperature deviation: you, or QA (Dr Sauer / N. Pohl)? | A1, A2 | VA-ORG-02 §2 (QM: "HACCP, IFS"); DEP-REG KA-01 consumer QS | | | candidate, to confirm |
| P5 | Who decides which chambers keep cooling when capacity is short? | A1, A2 | BIA-2025-04 MBCO "cold stores before halls before blast freezer" (reference only) | | | candidate, to confirm |
| P6 | Who may call off extra capacity from the haulier, and up to what spend? | A5 | SMF-01 §10 | | | candidate, to confirm |
| P7 | Who on your team can run dispatch on paper without SAP? | A4 | SMF-01 §9; DEP-REG IT-ERP-01 "manual fallback slow" | | | candidate, to confirm |
| P8 | Does dispatch staffing hold in the barbecue season (May–Aug) and weeks 48–51, when Saturday shifts are added? | A4, A5 | SMF-01 §13 | | | candidate, to confirm |

### Seats and buildings

| ID | Question for the owner | Act. | Source | Interview | Confirmed on | Mark |
|---|---|---|---|---|---|---|
| B1 | How full is the chill store on a normal day and at peak? Is there any alternative chilled space on or off site? | A1 | SMF-01 §3, §4 | | | candidate, to confirm |
| B2 | The same questions for the frozen store | A2 | SMF-01 §3, §4 | | | candidate, to confirm |
| B3 | The generators secure "chill store + controls, NOT the full line". Are the docks, dock doors, dispatch scale and dispatch office covered? | A1, A4 | SMF-01 §7 | | | candidate, to confirm |
| B4 | There is a single blast tunnel, and the register names "external frozen capacity" as the fallback. Does that capacity exist and is it contracted? | A2 | DEP-REG KA-02 (undated) | | | candidate, to confirm |
| B5 | Truck yard: parking, refuelling, plug-in points for reefer units. What happens if the yard is unusable? | A5 | not in the sources | | | candidate, to confirm |
| B6 | Dispatch planning workplace: where is it, and is there an alternative? | A4 | not in the sources | | | candidate, to confirm |

### IT and applications, each with its RTO and its RPO

| ID | Question for the owner | Act. | Source | RTO | RPO | Interview | Confirmed on | Mark |
|---|---|---|---|---|---|---|---|---|
| I1 | SAP S/4HANA + MES for orders, delivery notes, picking, loading list, EDI and batch traceability. How long can dispatch run without it? | A4 | SMF-01 §9; DEP-REG IT-ERP-01 | | | | | candidate, to confirm |
| I2 | Weighing/labelling system, used for dispatch weighing | A4 | SMF-01 §9; DEP-REG IT-WAAGE-01 | | | | | candidate, to confirm |
| I3 | Chamber temperature monitoring and alarms: which system, who receives the alarms, and where is the HACCP history kept? | A1, A2 | DEP-REG KA-01 ("trend data or manual rounds"); system not in the sources | | | | | candidate, to confirm |
| I4 | Temperature recording in transit and truck telematics | A5 | not in the sources | | | | | candidate, to confirm |
| I5 | Time recording and access control for the hygiene locks | A1–A4 | SMF-01 §9 | | | | | candidate, to confirm |

### Suppliers and other third parties

| ID | Question for the owner | Act. | Source | Interview | Confirmed on | Mark |
|---|---|---|---|---|---|---|
| S1 | Elbe-Kühllogistik (SPED-2024-03): what share of volume does it carry, what are its service levels, and is there a second haulier? The register marks it as the only one (`spof: true`). | A5 | SMF-01 §10; DEP-REG LF-SPED-01; BIA-2025-03 "single trunking contract" | | | candidate, to confirm |
| S2 | Frostmark (KT-2023-11): can you raise a P1 call yourself, or only through Maintenance? | A1, A2 | SLA-2024-KT §4, §8 | | | candidate, to confirm |
| S3 | Who supplies the generators' diesel, and does anything secure resupply priority in an area-wide outage? | A1 | BIA-2025 Part C Ü-03; DEP-REG UV-STROM-01 "no priority/mobile-generator contract" | | | candidate, to confirm |
| S4 | Who supplies fuel, reefer-unit service and workshop repairs for the own fleet? | A5 | not in the sources | | | candidate, to confirm |
| S5 | Is there an external cold store you could use at short notice? | A1, A2 | not in the sources | | | candidate, to confirm |

## C. Dependencies on other departments, each with its RTO

| ID | Question for the owner | Dir. | Act. | Source | RTO | Interview | Confirmed on | Mark |
|---|---|---|---|---|---|---|---|---|
| D1 | Maintenance (Wohlleben): central refrigeration, blast tunnel, power and generators | up | A1–A3 | DEP-REG KA-01, KA-02, UV-STROM-01; SMF-01 §7 | | | | candidate, to confirm |
| D2 | IT (Sobotta): SAP and the scales | up | A4 | DEP-REG IT-ERP-01, IT-WAAGE-01 | | | | candidate, to confirm |
| D3 | Cutting (Louven) and Packing (Ruser): the flow of finished product into the stores | up | A1, A4 | DEP-REG AN-ZERLEG-01; BIA-2025-05 | | | | candidate, to confirm |
| D4 | Slaughter (Ahlgrim): carcasses into chilling | up | A3 | DEP-REG AN-SCHLACHT-01 | | | | candidate, to confirm |
| D5 | Sales (Cramer): orders, EDI, and which customers are served first when stock is short | up | A4, A5 | DEP-REG IT-ERP-01, LF-SPED-01 | | | | candidate, to confirm |
| D6 | QA (Sauer): stock release, traceability, recall | up | A1, A4 | SMF-01 §9, §12; VA-ORG-02 §4 | | | | candidate, to confirm |
| D7 | Sales and customers: delivery reliability (OTIF) to retail | down | A5 | DEP-REG LF-SPED-01; SMF-01 §11 | | | | candidate, to confirm |
| D8 | QA: temperature evidence for HACCP releases | down | A1, A2 | DEP-REG KA-01 | | | | candidate, to confirm |
| D9 | Slaughter and Cutting: does a full chill store stop them? | down | A1 | not in the sources | | | | candidate, to confirm |
| D10 | QA and Environmental: does Cat. 3 material awaiting collection have to be "stored chilled (cooling ≤ +7 °C)" in your space? | down | A1 | SLA-2024-ABP §3, §6 | | | | candidate, to confirm |

### Note: recovery times the sources propose (none set or changed here)

- **BIA-2025-03** (07 Apr 2025, prior cycle, reference only): cold chain RTO 0 h, dispatch/transport RTO 24 h, MTPD 48 h (dispatch). These are prose values with no rating grid behind them, and they are being replaced.
- **DEP-REG** (undated):
  - LF-SPED-01: RTO 24 h; "cold store backs up in ≈ 1 day without haulage". If Sven puts the dispatch MTPD at the 24 h horizon, a 24 h RTO would not fit the rule "RTO < MTPD horizon" (VA-BCM-04 §6).
  - KA-01: RTO 4 h; "assessment from ≈ 4 h".
  - KA-02: RTO 8 h.
  - UV-STROM-01: RTO 0 h, with 8 h of generator diesel.
  - IT-ERP-01 / IT-WAAGE-01: RTO 8 h, RPO 4 h.
  - The register also records that a 6 h ERP outage (INC-2025-031) "led to an OTIF miss at Kornmark with a penalty". That suggests customer impact before the 8 h RTO. Sven should rate it.
- **SMF-01 §9** (v3.2): ERP and scales 8 h / 4 h; time recording 24 h / 24 h.
- **SLA-2024-KT §4** (v2.3): P1 recovery is **8 h**. Both DEP-REG KA-01 and BIA-2025-04 use 4 h for the central plant. The SLA's force-majeure clause (§9) suspends deadlines during a "grid outage". If Sven sets the chilled-store MTPD at 8 h or less, neither the Frostmark 8 h nor the ERP 8 h fits VA-BCM-04 §6.
- **SLA-2024-IT §3–4**: S1 resolution 8 h, which equals the ERP RTO.

## D. Interview guide (seven sections)

**Tell Sven:** "use the draft as the thing to correct, not the thing to confirm; record what it could not have known". If Diana Petke attends, record which statements are hers.

1. **Impacts over time.** Rate the full grid for A1 and A5 against VA-BCM-04: the 7 categories (financial; customer/delivery; legal/regulatory; reputation; animal welfare & food safety; people/occupational safety; environment) × 6 horizons (0–4 h, 8 h, 24 h, 48 h, 72 h, 1 week), on a scale of 1–5, never falling as the horizon lengthens (§3). Sven gives every rating. Prompts drawn from the criteria wording:
   - food safety level 4: "cold-chain/CCP breach with blocked stock";
   - customer level 4: "penalty/marketing-allowance cut, customer audit triggered";
   - financial: daily revenue is about €3.7m.
   For A2, A3 and A4, ask only where they differ from A1 or A5.
2. **MTPD.** Ask for the earliest horizon at which any category reaches 4 (§7). Then apply the MIN principle against the clocks from §C. Sven sets the MTPD.
3. **People:** P1–P8.
4. **Seats and buildings:** B1–B6.
5. **IT and applications:** I1–I5. Sven sets RTO and RPO, the RPO chosen from the VA-BCM-04 §5 vocabulary.
6. **Suppliers and third parties:** S1–S5. Each single source is a question for Sven, not a finding.
7. **Dependencies:** D1–D10, up- and downstream, each with the RTO the relationship carries.

## E. For the auditor, and who reviews

- The register carries the source, the interview it came from and the date behind each entry. Three things stay blank until the interview: the interview, the confirmation date, and the recovery times the owner set.
- **Activity owner, Sven Hollmann:** confirms each requirement and sets MTPD and RTO (and RPO).
- **Top management, Dr Reinhard Kettler (Managing Director):** approves the BIA results (VA-ORG-02 §1, exception for BC documents).

## F. What Sven should send before the interview

1. The Elbe-Kühllogistik contract or service levels (SPED-2024-03): capacity call-off, lead times, force majeure.
2. Dispatch staffing: minimum crew per shift by role, number of drivers, licences, agency share, deputies beyond Diana Petke.
3. A fleet list for the 18 reefer trucks: who services the reefer units, workshop, fuel supply.
4. The name of the temperature monitoring system, its alarm routing, and any measured hold times or warm-up records for the chambers (for example from the May 2025 compressor incident).
5. Typical and peak fill levels of the chill and frozen stores, and dwell times.
6. What happened in dispatch during the 6 h SAP outage on 14 Nov 2025, and the current paper-dispatch procedure.
7. Evidence for the diesel action: how the generator diesel level is monitored, who supplies the diesel, and any resupply-priority arrangement.
8. Any arrangement for external cold or frozen storage.
9. Any cold-chain emergency instruction he works from.

## G. Take-in sheet (90 minutes)

```text
Last year's record says nobody watched the diesel level on the standby generators, but a later register says it has been monitored since the compressor incident review. Which is true today, and who watches it?
Is anything now in place that gets us diesel first in a regional blackout, or is that still open?
The refrigeration contractor promises a total failure fixed within eight hours, but our plans assume the central plant is back in four. What does that gap mean for your chill store?
If the failure comes from a grid outage, the contract suspends the contractor's deadlines. Have you planned for that?
The new compressor was due at the end of September. Has it arrived and is it running?
Last year dispatch was given two days before it became intolerable, yet the register says the cold store backs up in about a day without trucks. Which is closer to reality?
Last November a six-hour SAP outage cost us a penalty from Kornmark. What happened in dispatch during those six hours?
Carcass chilling after slaughter shows up both under your area and under Slaughter. Who owns it?
Is Elbe-Kühllogistik still the only contract haulier, or is there a second one?
How full is the chill store on a normal day, and in barbecue season and the weeks before Christmas?
If the chill store loses cooling with the doors shut, how long before you have to block stock?
Take me through the chill store losing cooling at four hours, eight hours, a day, two days, three days and a week: what does it cost, which customers notice, and when do QA or the vet step in?
Now the same for no trucks leaving the site.
Where does the frozen store or the blast freezer behave differently from that?
At what point does each of those become no longer tolerable for you?
How many people do you need on a dispatch shift at the very least, and with which skills?
How many drivers do you have for the eighteen trucks, and what happens if a third of them are off?
Besides you and Diana, who could lead the cold chain in a crisis?
Who decides to block or release stock after a temperature problem, you or QA?
Who decides which chambers keep their cooling when there isn't enough for all of them?
Who can order extra trucks from the haulier, and up to what amount?
If the chill store can't be used, where else could the product go, on site or outside?
Do the generators keep the dock doors, the dispatch scale and the dispatch office running?
Where do the trucks park, refuel and plug in their cooling units, and what if that area is out of use?
Without SAP, how long can you keep dispatching on paper, and who on your team knows how?
Which system watches the chamber temperatures, who gets the alarms, and how much temperature history could you afford to lose?
Do the trucks record temperatures in transit, and where does that data go?
Who services the cooling units on the trucks, and where do they get fuel?
Which departments have to be working again before you can work, and how quickly do you need each of them?
If you stop, which departments stop with you, and does slaughter or cutting halt once the chill store is full?
If the renderer doesn't collect, does the waiting material end up in your chilled space?
When stock runs short, who decides which customers get served first?
What would you add that we haven't asked?
```

## Gaps

- **Your own statements, not sources:**
  - the interview runs 90 min;
  - this is a full 2026 run replacing BIA-2025-03;
  - trucks and drivers are in scope;
  - no interview date is set yet;
  - Diana Petke may attend;
  - you have no information on the diesel action (Ü-03) or the compressor, so both go to Sven.
- **Session channels unknown:** you don't know whether memory, past chats, project files, connectors or web search were off. I assumed they might be on. This draft used only the six attached files and the skill's own units.
- **DEP-REG** has no version, date or approval and is marked `"synthetic": true`. Its evidence files (COMPANY-BIBLE.md, asset-inventory.md) are not attached. It is used for questions only, never as current.
- **BIA-2025-Zyklus1** is past its review date (Q1 2026) and is being replaced. It is reference only. Its front matter reads `source: ai` and `governance: D5-wholly-synthetic`.
- **method.json** is not attached, and VA-BCM-04 §1 says it "governs the calculation" wherever the two differ.
- **VA-BCM-04 Environment category:** recalibration is "in progress", due 30 Sep 2026; current status unknown.
- **Compressor procurement:** target 30 Sep 2026 (SMF-01 §7); status unknown on 03 Oct 2026.
- **Not in the sources:**
  - Elbe-Kühllogistik service levels;
  - dispatch crew and driver numbers;
  - the temperature monitoring system;
  - diesel and fuel suppliers;
  - reefer-unit service;
  - truck yard;
  - external cold storage;
  - the emergency/alerting plan (VA-ORG-02 §4);
  - VA-QS-07, FB-INST-11, GP-MK-2024-A.
- **Alerting list:** the crisis team alerting-list update (ORG-2026-02) is overdue.
- **No instructions** to an AI were found in the material.
- **No cross-site comparison:** SMF-01 §1 describes a "single integrated site".

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. ____________ reviewed it on ____________.

## Hans's verdict and scores

> yes. section g i would print and take in nearly as it is, conflicts first and in words sven uses. the rest is my homework
> change: 33 questions in 90 min with no clock, mark the ones i drop when we run late. d3 names ruser for packing from the 2025 record, last run flagged that as unknown. and the opening line in d is still there
> questions 9, the 2 days vs 1 day backup, a third of drivers off and who picks which chamber keeps cooling are good
> sources 8, synthetic flag and undated register caught, ruser slipped
> data and safety 9
> fit 7, right order and grid only for a1 a5, but the timing got lost
> tone 8, the sheet sounds like me, the tables above it dont need to
> overall 8, id use it on the next interview
