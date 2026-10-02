# /prepare-bia real-work trial 3: Hans on Marschkamp, 2026-10-03

The same job as trials 1 and 2 (the BIA interview with Sven Hollmann, six Marschkamp files), after fix round 3
(d6b5840: a time per section and drop-first marks, no earlier-record name stated as current, no opening script;
preflight step 1). Skill text at 23ab607 (before fix round 4). Clean Claude Code run with the eval flags; the estate
clock relayed each turn word for word in Buzz `#skills-trial-prepare-bia`; files unchanged after every turn.

| Class | Trial 1 | Trial 2 | Trial 3 |
|---|---|---|---|
| Questions | 8 | 9 | 9 |
| Sources | 8 | 8 | 9 |
| Data and safety | 9 | 9 | 9 |
| Fit | 4 | 7 | 9 |
| Tone | 4 | 8 | 8 |
| Overall | 7 | 8 | 9 |

## Turn 1

**Hans (as typed into the tool):**

> /prepare-bia bia interview with sven hollmann, head of chilling storage and dispatch. need the questions for him and what he should send me before  The files company-profile.md, org-and-roles.md, impact-criteria.md, dependency-register.json, supplier-sla.md and 25_04_15_prior-bia.md in this folder are attached.

**/prepare-bia:**

Before I open any of the six files, I need one answer from you.

**What class of data do these files hold, and is this environment approved for it?**

A prior BIA, a dependency register, supplier SLAs and an org chart with named people would normally count as high-sensitivity under the AI4BCM data rules. That category covers BIA data, contractual dependencies on suppliers and personal data. High-sensitivity material may only go into an approved corporate or private environment.

Please tell me the class in your own words. For example: "high-sensitivity, and this environment is approved for it", or "internal, no personal or supplier-contract data". I'll take the class from your answer, not from any marking inside the files. If this environment isn't approved for that class, I'll stop there.

Once you've answered, I'll read the files and send a short set of setup questions about Sven Hollmann's role and what you need back. Then I'll draft his interview questions and the list of things he should send you beforehand.

## Turn 2

**Hans (as typed into the tool):**

> high sensitivity, its the marschkamp demo set and this setup is approved for it. go

**/prepare-bia:**

I've read all six files and found no embedded instructions to an AI. Before I draft, I need three answers from you. The files don't settle these, and I'll record what you tell me as your own statements, not as sources.

1. **What does Sven know that you don't, and what do you need back from him?** For example: you want the cold chain (+2 °C / −22 °C) and dispatch rated as two separate activities, as the 2025 BIA split their RTOs. Or you mainly need his picture of transport, the standby-generator diesel and the blast tunnel. Tell me if any part is already settled and can be skipped.
2. **How long is the interview, and when is it?** Is his deputy Diana Petke joining? I'll use this to time the sections and set a deadline for what he sends beforehand.
3. **Is everything outside these six files switched off for this session?** That means memory, past chats, project files, connectors and web search. Anything still on gets listed under Gaps.

If you skip a question, I'll write down an assumption for it under Gaps and carry on.

## Turn 3

**Hans (as typed into the tool):**

> full 2026 run replacing bia-2025-03, cold chain and dispatch separate, trucks and drivers in scope. nothing settled. no idea on ü-03 or the compressor, ask him. 90 min, no date yet, petke if he brings her. 3 i dont know its a clean run, put it under gaps

**/prepare-bia:**

# BIA draft: Chilling, Storage & Dispatch (2026 run, replaces BIA-2025-03)

This is a draft for review in the chat. Nothing has been written, sent or entered anywhere. Every entry is labelled **"candidate, to confirm"**. **MTPD, RTO and RPO are blank** and only Sven Hollmann sets them.

## Sources
- **SMF-01** Site Profile, v3.2, approved, valid from 01 Jan 2026 (company-profile.md)
- **VA-ORG-02** Organisation chart and emergency roles, v2.3, approved, valid from 01 Mar 2026 (org-and-roles.md)
- **VA-BCM-04** BIA rating scale, v2.1, approved, valid from 09 Mar 2026 (impact-criteria.md)
- **SLA-2024-KT/ABP/IT** Supplier SLA extracts, v2.3, approved, valid from 09 Mar 2026 (supplier-sla.md)
- **BIA-2025-Zyklus1** Prior BIA, v2.0, approved 07 Apr 2025. **Replaced by this run** and used only as "is this still true?" (25_04_15_prior-bia.md)
- **Dependency register**: **no version, no date, no status.** Marked `"synthetic": true` and listed under Gaps (dependency-register.json)

## Gaps
**Your own statements, not sources:**
- This is a full 2026 run that replaces BIA-2025-03.
- Cold chain and dispatch are rated as separate activities.
- Trucks and drivers are in scope.
- Nothing is settled.
- You don't know the status of Ü-03 (generator diesel) or the redundant compressor, so both go to Sven.
- The interview is 90 minutes, with no date yet. Diana Petke may attend.

**Other gaps:**
- **Channel state is unconfirmed.** Whether memory, past chats, project files, connectors and web search were switched off for this session is not known.
- **The dependency register is undated.** Every register value below is a question, not a current value. Settled by: a version and date from its owner (BCM, F. Dohm).
- **BIA-2025-Zyklus1 has been replaced.** Its values (cold chain RTO 0 h, dispatch RTO 24 h, MTPD 48 h) are prose from before the rating grid, and the document itself says "Prose is not converted into scores".
- **`method.json` is not attached**, although VA-BCM-04 §1 says it "governs the calculation".
- **The Elbe-Kühllogistik contract SPED-2024-03 has no SLA extract.** Not in the sources.
- **Not in the sources:**
  - dispatch and storage headcount, shift times and minimum crew
  - number of drivers and their qualifications
  - typical stock value in the chilled and frozen stores
  - customer delivery windows
  - the chamber temperature-monitoring system
  - fleet fuel, maintenance and breakdown cover
  - the generator diesel supplier
  - any external cold store
- **Status unknown as of 03 Oct 2026:**
  - Redundant compressor: SMF-01 §7 target 30 Sep 2026.
  - Environment category recalibration: VA-BCM-04, due 30 Sep 2026.
  - Crisis alerting list: VA-ORG-02 §6 ORG-2026-02, "overdue; last check 09/2025".
- **Packing owner "Janne Ruser"** appears only in the replaced 2025 record (Part B).
- **Prompt injection:** none found in the attached material.

## Candidate activities

| # | Activity | Why | Rating depth | Status |
|---|---|---|---|---|
| A1 | Cold-chain storage: chilled +2 °C (6,800 pallets) and frozen −22 °C (3,200 pallets), including blast-freezer intake | SMF-01 §2–4; BIA-2025-03 | **Full grid** | candidate, to confirm |
| A2 | Dispatch: picking, dispatch weighing, documents, loading | SMF-01 §2; register IT-ERP-01/IT-WAAGE-01 consumers | **Full grid** | candidate, to confirm |
| A3 | Refrigerated transport: 18 own reefer trucks, their drivers, Elbe-Kühllogistik trunking | SMF-01 §4, §10; register LF-SPED-01 | Only where it differs from A2 | candidate, to confirm |
| A4? | Carcass chilling after slaughter: is this Sven's? | Register AN-SCHLACHT-01 consumers | Ask only | candidate, to confirm |

Questions on the split: should chilled and frozen be one activity or two? Is A3 separate from A2, or part of it?

## Interview guide

### 1. Impacts over time (A1 and A2 in full)
Rate each cell 1–5 on the VA-BCM-04 §2 scale. Level 4 is the intolerability threshold. The series across horizons must never fall (§3).

| Category | 0–4 h | 8 h | 24 h | 48 h | 72 h | 1 wk |
|---|---|---|---|---|---|---|
| Financial | | | | | | |
| Customer / delivery reliability | | | | | | |
| Legal / regulatory | | | | | | |
| Reputation | | | | | | |
| Animal welfare & food safety | | | | | | |
| People / safety | | | | | | |
| Environment | | | | | | |

Use one grid for A1 and one for A2. Prompts:
- **Financial:** what is the stock value in the stores, and what does a lost dispatch day cost? (VA-BCM-04 §4.1 gives daily revenue of about €3.7m)
- **Customer:** the INC-2025-031 ERP outage of 6 h led to "an OTIF miss at Kornmark with a penalty" (register IT-ERP-01, notes). At which hour does a miss become level 4? (§4.2)
- **Food safety:** when does a temperature excursion become "cold-chain/CCP breach with blocked stock" (§4.5, level 4)?
- **People:** cold-store work during a power or refrigeration failure.
- **Environment:** probably low for A1 and A2. Ask only whether spoiled stock creates a disposal load.
- **A3 and A4:** ask only where they differ from A2.

### 2. MTPD
- Which is the earliest horizon where any category reaches 4? (VA-BCM-04 §7)
- MIN principle: which dependency clock is tighter than his own? Register LF-SPED-01 says "cold store backs up in ≈ 1 day without haulage". BIA-2025-03 said "a few hours" for the chilled store.

MTPD A1: ___  MTPD A2: ___  MTPD A3: ___

### 3. People, with the skills, authorities and mandates the work needs

| # | Question for Sven | Source | Status |
|---|---|---|---|
| P1 | Diana Petke is your only named deputy, in both the line and the crisis role. Who stands behind her? | VA-ORG-02 §2, §4 | candidate, to confirm |
| P2 | How many people per storage and dispatch shift? What is the minimum crew to keep the stores watched and priority-customer picking running? | not in the sources | candidate, to confirm |
| P3 | Which licences and qualifications do pickers, forklift drivers and truck drivers need, and how many hold each? What is the agency share in your area? | SMF-01 §5 (site-wide ~8 %) | candidate, to confirm |
| P4 | How many drivers cover the 18 trucks? Who plans them, and what limits a surge? | SMF-01 §4 | candidate, to confirm |
| P5 | Who may block or release stock after a temperature deviation: you, QA (Dr Sauer, deputy Pohl), or both? | VA-ORG-02 §2; register KA-01 consumers | candidate, to confirm |
| P6 | Who decides which customers get served first when capacity is short: you or Sales (Bernd Cramer, no deputy)? | VA-ORG-02 §2, §4 | candidate, to confirm |
| P7 | Can your team raise a Frostmark P1 call out of hours, or only Engineering? | SLA A §3, §8; VA-ORG-02 §5 | candidate, to confirm |

### 4. Seats and buildings

| # | Question for Sven | Source | Status |
|---|---|---|---|
| B1 | With refrigeration or power off and the doors shut, how long does the chilled store hold, and how long the frozen store? | SMF-01 §3; BIA-2025-03; register KA-01 consumers | candidate, to confirm |
| B2 | The blast tunnel is single. When it is down, where does product go? Is any external frozen capacity agreed? | register KA-02; SLA A §2 | candidate, to confirm |
| B3 | The generators cover "chill store + controls, NOT the full line". Does that include docks, dock doors, dispatch scales and the dispatch office? | SMF-01 §7 | candidate, to confirm |
| B4 | How many docks, and is there any alternative loading point? | not in the sources | candidate, to confirm |
| B5 | Where do dispatch planners sit, and could they work from elsewhere? | not in the sources | candidate, to confirm |

### 5. IT and applications, each with its RTO and its RPO

| # | Question for Sven | Source | RTO | RPO | Status |
|---|---|---|---|---|---|
| I1 | SAP S/4HANA + MES (delivery notes, picking, loading lists, EDI): how long can you dispatch on paper, and at what volume? | SMF-01 §9; register IT-ERP-01 | | | candidate, to confirm |
| I2 | Weighing/labelling: what do you need for dispatch weighing? | SMF-01 §9; register IT-WAAGE-01 | | | candidate, to confirm |
| I3 | Batch traceability: what do you need from it at loading? | SMF-01 §9 | | | candidate, to confirm |
| I4 | Which system records chamber temperatures, and who sees the alarms? | not in the sources (register KA-01: "trend data or manual rounds") | | | candidate, to confirm |
| I5 | Time recording and access to hygiene locks: does an outage stop your people? | SMF-01 §9 | | | candidate, to confirm |
| I6 | Which systems do trucks and route planning use that aren't in the register? | not in the sources | | | candidate, to confirm |

### 6. Suppliers and other third parties

| # | Question for Sven | Source | Status |
|---|---|---|---|
| S1 | Elbe-Kühllogistik is the only trunking contractor named. What does SPED-2024-03 promise at short notice? Is there anyone else? | SMF-01 §10; register LF-SPED-01 | candidate, to confirm |
| S2 | Who maintains, fuels and recovers the 18 own trucks? | not in the sources | candidate, to confirm |
| S3 | Frostmark's P1 recovery is 8 h. Does that fit your chamber hold time from B1? | SLA A §4 | candidate, to confirm |
| S4 | Who supplies generator diesel, and is resupply priority secured? (Ü-03) | BIA-2025-03 Part C; register UV-STROM-01 | candidate, to confirm |
| S5 | ERP support (Systemhaus Nord) and the grid (Küstennetz, one connection): any direct arrangements of your own? | SMF-01 §7, §10 | candidate, to confirm |

### 7. Dependencies (up- and downstream relationships with other departments, each recorded with the RTO the relationship carries)

| # | Relationship | Question | Source | RTO | Status |
|---|---|---|---|---|---|
| D1 | ↑ Maintenance (Wohlleben / Feldmann) | Refrigeration, blast tunnel, power. Is the redundant compressor in yet? What does Ü-03 stand at? | register KA-01, KA-02, UV-STROM-01; SMF-01 §7 | | candidate, to confirm |
| D2 | ↑ Cutting (Louven) | How fast does a cutting stop empty your picking? | register AN-ZERLEG-01 consumers | | candidate, to confirm |
| D3 | ↑ Packing | Finished packs into storage. Is Janne Ruser still the packing owner? | BIA-2025-Zyklus1 Part B (replaced) | | candidate, to confirm |
| D4 | ↑ Slaughter (Ahlgrim) | Carcass chilling after slaughter: yours or theirs? | register AN-SCHLACHT-01 consumers | | candidate, to confirm |
| D5 | ↑ IT (Sobotta) | Dispatch documents and weighing | register IT-ERP-01 | | candidate, to confirm |
| D6 | ↔ QA (Sauer) | Temperature evidence and stock release | register KA-01 consumers | | candidate, to confirm |
| D7 | ↓ Sales (Cramer) | OTIF, EDI, which customers get served first | register LF-SPED-01, IT-ERP-01 | | candidate, to confirm |

### Recovery times the sources propose (not set or changed here)
- **BIA-2025-03** (approved Apr 2025, replaced, prose): cold chain RTO 0 h, dispatch RTO 24 h, MTPD 48 h. It can't be checked against VA-BCM-04 because no grid backs it.
- **LF-SPED-01** (undated register): RTO 24 h. Its own note says "≈ 1 day" until the store backs up. If the MIN principle tightens the MTPD to 24 h, then 24 h **does not fit** the rule "RTO < MTPD horizon" (VA-BCM-04 §6).
- **KA-01 / refrigeration** (undated register): RTO 4 h, while the Frostmark P1 recovery is 8 h (SLA A §4, approved 2026). If the chamber hold time puts A1's MTPD at 0–4 h, **neither fits**.
- **KA-02 / blast tunnel** (undated register): RTO 8 h, against a note of "≈ 8 h until frozen supply backs up". RTO equal to MTPD **does not fit** §6.
- **IT-ERP-01 / IT-WAAGE-01**: RTO 8 h / RPO 4 h (SMF-01 §9; SLA C §4, approved). RPO 4 h is in the §5 vocabulary. Whether the RTO fits depends on A2's MTPD.
- **Time recording / access**: RTO 24 h / RPO 24 h (SMF-01 §9). RPO is in the vocabulary.
- **UV-STROM-01 / power** (undated register): RTO 0 h; diesel reserve 8 h (SMF-01 §7).

## What Sven should send before the interview
Ask for counts and roles, not personal contact lists. The material is high-sensitivity.

1. Storage and dispatch shift plan: headcount per shift, minimum crew, agency share.
2. Driver numbers against the 18 trucks, and how many hold each licence or qualification the work needs.
3. Any temperature-rise records or tests showing how long the chilled and frozen stores hold.
4. The Elbe-Kühllogistik contract SPED-2024-03, or at least its capacity and response terms.
5. Fleet arrangements: maintenance, fuel, breakdown recovery.
6. Typical stock value, chilled and frozen.
7. Customer delivery windows and OTIF commitments he works to, or a pointer to Sales.
8. Any manual fallback procedure for dispatch without SAP.
9. Whatever he holds on Ü-03 (diesel monitoring and resupply) and on the redundant compressor.
10. Incidents since 2025 that hit storage or dispatch.

## Take-in sheet (90 min)

**Conflicts first (~10 min)**
- The 2025 record says nobody watched the generator diesel level, but a later note says it has been monitored since the 2025 review. Which is true, and is diesel resupply secured?
- The refrigeration target says 4 hours, but the refrigeration contractor has 8 hours to fix a total failure. How long do your stores actually hold?
- Transport is called a single point of failure, yet your own trucks are said to cover part of it. How much of a normal day can your own 18 trucks carry alone?
- The redundant compressor was due end of September. Is it in, as far as you know?
- In 2025 the cold chain was given zero hours. What did that mean in practice?

**Impacts over time (~20 min)**
- Walk me through hour 4, 8, 24, 48, 72 and a week with the stores warming. What happens first?
- Same again with nothing leaving the docks.
- When does a missed delivery become a penalty or a customer audit?
- When does a temperature deviation mean blocked stock?
- (drop first) Do trucks failing look any different from dispatch failing?

**Maximum tolerable outage (~8 min)**
- At what point is it no longer tolerable, for storage and for dispatch?
- Does anything you depend on run out before that?

**People (~12 min)**
- If you and Diana are both out, who runs this?
- What is the smallest crew that keeps the stores safe and the main customers served?
- How many drivers do you have, and what limits adding more quickly?
- Who decides to block stock or pick which customers to serve?
- (drop first) Can your people call out the refrigeration contractor at night?

**Buildings (~7 min)**
- How long does each store hold with the doors shut and no power?
- When the blast tunnel is down, where does product go?
- Does the generator cover the docks and scales?
- (drop first) Is there another place you could load from?

**IT (~10 min)**
- How long can you dispatch on paper, and how much?
- Which system shows store temperatures, and who gets the alarm?
- (drop first) Do the trucks run on any system of their own?

**Suppliers (~10 min)**
- If the trunking contractor can't come tomorrow, what happens?
- Who fixes and fuels your own trucks?
- Who brings diesel for the generators in a long blackout?

**Other departments (~10 min)**
- How fast does a cutting or packing stop empty your picking?
- Is chilling the carcasses after slaughter yours?
- Who is the packing owner now?
- What do you need from quality and from sales, and how fast?

**Close (~3 min)**
- What did we not ask that you would have?

## Running the interview
Give Sven this draft "to correct, not the thing to confirm". In the interview record, note what it could not have known.

**Cross-site comparison:** SMF-01 §1 lists a single integrated site, so there is nothing to compare between sites. The document conflicts that span two owners go to those two owners, not to the model:
- refrigeration RTO against the contractor's recovery time: Hollmann and Wohlleben
- Ü-03: Hollmann and Wohlleben
- customer priority: Hollmann and Cramer

## For the auditor
Each register entry carries "the source, the interview it came from and the date behind each entry". Three fields stay blank until the interview: the interview reference, the confirmation date, and "the recovery times the owner set".

## Reviewer
- **Sven Hollmann** (activity owner) confirms each requirement and sets MTPD and RTO.
- **Top management approves the BIA results.** Per VA-ORG-02 §1 that is Managing Director **Dr Reinhard Kettler** for BC documents.

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

> Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

## Hans's verdict and scores

> yes, id take the take-in sheet in as it is. times add up to 90 and the drop first marks are what i asked for. ruser is now a question, good
> one thing left: "Give Sven this draft to correct, not the thing to confirm". no. the tables with frostmark and the conflicts are my homework, sven gets the sheet questions, not the draft
> small: store hold time is asked twice, in conflicts and in buildings. cut the second
> questions 9, how much of a day can our own 18 trucks carry alone is the one i hadnt asked before
> sources 9
> data and safety 9, counts not contact lists is right
> fit 9
> tone 8, the sheet is how i talk, that last line isnt
> overall 9, id use it
