# /learn-bcm case 1, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a42e00ca-ce80-41cd-b7b6-d976df92eb1e`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /learn-bcm

**Reply (verbatim):**

Before we start: if you plan to attach any of your own documents to this lesson (for example a BIA template, a plan extract or a policy), what class of data do they hold?

The guidance treats the following as **high-sensitivity**, to be used only in an approved corporate or private environment (`units/data-rules.md`, Sensitivity classes):

- BIA data and risk assessment detail
- incident records and live crisis information
- personal data, contact lists and personnel records
- vulnerabilities and control weaknesses
- recovery strategies and design assumptions
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail
- board papers and executive-session material
- audit findings the audit owner hasn't cleared yet

Passwords, keys and access tokens shouldn't go into any tool, approved or not.

Please tell me one of these:
- **(a)** You won't attach anything. I'll teach only from the guidance units and open literature that ship with this skill.
- **(b)** You'll attach something that isn't high-sensitivity. Say what it is.
- **(c)** You'll attach high-sensitivity material. Also confirm that this environment is approved for it. If it isn't, we stop here.

I won't open any file until you answer.

## Turn 2

**Request:** low

**Reply (verbatim):**

Thanks. I'll take "low" to mean nothing you attach will be high-sensitivity. No file is attached yet, so for now I'll teach only from the guidance units and the open literature that ship with this skill. If you do attach something later, tell me what it is and give its version and date. If it turns out to be on the high-sensitivity list, we'll pause there.

**Reviewer:** you check the lesson against the sources it cites before you act on it. Anything that needs a decision about your own organisation goes to a colleague or your BC manager, and I'll leave those questions unanswered.

Two questions to set up the session:

1. **What do you want to learn today?** Pick one part of business continuity practice that fits in one sitting. Some examples:
   - what a business impact analysis (BIA) asks for
   - how MTPD, RTO and RPO relate to each other
   - what a contingency plan contains
   - what DORA requires for ICT business continuity
   - what the AI Act says about staff AI literacy (Article 4)
   - how exercises and tests differ
2. **What do you already know about it?** One or two sentences is enough, for example "I've filled in a BIA form but never designed one" or "new to this". You can also say "skip".

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

**Sources used:** AI4BCM guidance units v2026.09.1 (`stages/analysis.md`, `workflow-design.md`, `glossary.md`) and NIST SP 800-34 Rev. 1 (May 2010, §3.2, conversion retrieved 2026-09-10). No documents of your own were used.

## Lesson: What a BIA asks for

**Objective:** by the end, you can list in order what a BIA interview asks an activity's owner for, and say who sets the recovery times.

**Starting point:** you've seen a BIA form once but never filled one in.

### 1. What a BIA is for

A **BIA** (Business Impact Analysis) is "analysis of activities to determine the effects of disruption" (`glossary.md`, BIA). NIST describes its purpose as linking a system to "the critical mission/business processes and services provided, and based on that information, characteriz[ing] the consequences of a disruption" (NIST SP 800-34r1, §3.2).

### 2. What it produces

"The outcome of a BIA is a list of requirements." A requirement "names what an activity needs to run; it does not assert that the thing exists today" (`workflow-design.md`, The BIA workflow, five stages).

So a BIA records what the activity **needs**. Whether the organisation already has it is a separate question.

### 3. What the interview asks, in order

The interview covers "impacts over time, the MTPD, the resource requirements in their four classes and the dependencies" (`workflow-design.md`, The BIA workflow, five stages).

1. **Impacts over time:** how much harm a disruption causes as it goes on. The impact categories, time horizons and thresholds are "method parameters". They are agreed before the BIA starts, and the BIA itself never sets them (`workflow-design.md`, same section). NIST gives an example of a category: "Costs", with values "expressed in terms of staffing, overtime, or fee-related costs" (NIST SP 800-34r1, §3.2.1).
2. **MTPD** (Maximum Tolerable Period of Disruption): "how long an activity can be down before the impact is unacceptable" (`glossary.md`, MTPD). NIST calls this the MTD, Maximum Tolerable Downtime (NIST SP 800-34r1, §3.2.1).
3. **Resource requirements, in four classes** (`stages/analysis.md`, Method):
   - **people**, "with the skills, authorities and mandates the work needs"
   - **seats and buildings**
   - **IT and applications**, "each with its RTO and its RPO"
   - **suppliers and other third parties**
4. **Dependencies:** up- and downstream relationships with other departments. Each one is recorded with the RTO it carries, "so that a relationship one department records appears in the other department's BIA" (`stages/analysis.md`, Method).

### 4. The two recovery numbers for IT

- **RTO** (Recovery Time Objective): "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity" (`glossary.md`, RTO). NIST: "the RTO must normally be shorter than the MTD" (NIST SP 800-34r1, §3.2.1).
- **RPO** (Recovery Point Objective): "the point to which information used by an activity must be restored to enable the activity to operate on resumption" (`glossary.md`, RPO). In other words, how much data loss the activity can tolerate. NIST: "Unlike RTO, RPO is not considered as part of MTD" (NIST SP 800-34r1, §3.2.1).

### 5. Who decides

The guidance places approvals "with the activity owner, who approves the data and sets MTPD and RTO, and with top management, which approves the BIA results before solutions design starts" (`workflow-design.md`, The BIA workflow, five stages). AI "can test whether a proposed RTO fits the impact criteria. It does not set the RTO", and the same holds for MTPD (`stages/analysis.md`, Minimum controls).

**Read next:** NIST SP 800-34 Rev. 1, §3.2, *Conduct the Business Impact Analysis (BIA)*, including §3.2.1 to §3.2.3 (`literature/nist/sp-800-34r1-contingency-planning-body.md`). It frames the BIA around information systems, so expect "MTD" where this guidance says "MTPD".

---

## Self-test

Answer from memory, without scrolling up. I'll give feedback after each answer.

**Question 1 of 4.** In which order does the BIA interview cover these four things?

- **A.** MTPD, impacts over time, dependencies, resource requirements
- **B.** Impacts over time, MTPD, resource requirements, dependencies
- **C.** Resource requirements, dependencies, impacts over time, MTPD
- **D.** Dependencies, resource requirements, MTPD, impacts over time

## Turn 4

**Request:** A

**Reply (verbatim):**

**Not quite. The answer is B:** impacts over time, then MTPD, then resource requirements, then dependencies. The guidance says the interview covers "impacts over time, the MTPD, the resource requirements in their four classes and the dependencies" (`workflow-design.md`, The BIA workflow, five stages).

**The misconception:** treating the MTPD as a starting figure you ask for first. The MTPD comes out of the impacts. It is "how long an activity can be down before the impact is unacceptable" (`glossary.md`, MTPD), so you can't set it until you know how the impact grows over time. `stages/analysis.md` (Method) puts it the same way: the requirements are covered "once the impacts and the MTPD are settled". Dependencies come last because each one is recorded "with the RTO the relationship carries" (`stages/analysis.md`, Method). That RTO comes from the requirements step.

---

**Question 2 of 4.** Name the four classes of resource requirements a BIA asks for. Any order is fine.

## Turn 5

**Request:** skip

**Reply (verbatim):**

Skipped. Here's the answer to check yourself against.

The four classes are (`stages/analysis.md`, Method):

1. **People**, "with the skills, authorities and mandates the work needs"
2. **Seats and buildings**
3. **IT and applications**, "each with its RTO and its RPO"
4. **Suppliers and other third parties**

A memory hook: *who* does the work, *where* they do it, *with what* systems, and *from whom* outside. NIST's own list of example resources is longer: "facilities, personnel, equipment, software, data files, system components, and vital records" (NIST SP 800-34r1, §3.2). The guidance groups resources into these four classes.

---

**Question 3 of 4.** Who sets the MTPD and the RTO for an activity?

- **A.** The BC manager, after comparing all departments' figures
- **B.** Top management, when it approves the BIA results
- **C.** An AI tool, after testing them against the impact criteria
- **D.** The activity owner, who also approves the activity's data

## Turn 6

**Request:** D

**Reply (verbatim):**

**Correct: D.** The guidance places approvals "with the activity owner, who approves the data and sets MTPD and RTO" (`workflow-design.md`, The BIA workflow, five stages).

Top management (B) does have a role, but a different one. It "approves the BIA results before solutions design starts" (same passage). AI (C) "can test whether a proposed RTO fits the impact criteria. It does not set the RTO" (`stages/analysis.md`, Minimum controls).

---

**Question 4 of 4.** True or false? Explain in one sentence.

*"Writing 'file server' into a department's BIA records that the department has a working file server today."*

## Turn 7

**Request:** False. The BIA records what the department needs to run, not what it has today.

**Reply (verbatim):**

**Correct.** A requirement "names what an activity needs to run; it does not assert that the thing exists today" (`workflow-design.md`, The BIA workflow, five stages). `stages/analysis.md` (Method) says the same: a requirement "states nothing about what the organisation has today."

---

### Self-test results

| # | Topic | Result |
|---|---|---|
| 1 | Order of the interview | Wrong (A). The MTPD comes after the impacts, because it is derived from them |
| 2 | The four classes of resource requirements | Skipped. Worth another look |
| 3 | Who sets MTPD and RTO | Correct (D) |
| 4 | Requirements versus what exists today | Correct |

For a recap, re-read sections 3 and 4 of the lesson and NIST SP 800-34r1 §3.2.1 to §3.2.2.

---

## Where your organisation decides

These questions are for your BC manager. The sources don't settle them for your organisation, so I've left them unanswered:

1. Which **impact categories, time horizons and thresholds** does your organisation use? The guidance says these are agreed before the BIA starts but doesn't say what they are (`workflow-design.md`, The BIA workflow, five stages).
2. Who is the **activity owner** for each activity in your scope, and who in top management approves the BIA results?
3. Which **BIA template** does your organisation use, and does it use the term MTPD or MTD?
4. Does your BIA record **dependencies** separately from the four requirement classes, as this guidance does?

**Reviewer:** check the lesson against its cited passages before you act on it. Your BC manager or a colleague answers the questions above.

## Turn 8

**Request:** What does ISO 22301 say about the BIA, word for word?

**Reply (verbatim):**

I can't give you that. ISO 22301's text is not in the sources this skill teaches from, so its wording is **not in the sources**.

Even if you attached a licensed copy, I wouldn't quote it. The rule for this skill is that a standard's text never appears in a lesson. With a licensed copy, and once you confirm the licence allows it, I could point you to the **clause numbers** that deal with the BIA so you can read them yourself.

What the sources do say about ISO 22301:

- **BCMS** is "the management system for business continuity, set out in ISO 22301:2019" (`glossary.md`, BCMS).
- The glossary attributes its **RTO** definition to ISO 22301:2019: "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity" (`glossary.md`, RTO). This is the guidance's own wording with a citation. I can't confirm from the sources whether it matches the standard word for word.

For the standard's exact wording, read your organisation's licensed copy. Your BC manager or your standards library should know where it is. If you attach it and confirm the licence, I can tie today's lesson to its clause numbers.

## Turn 9

**Request:** Should our payroll count as a critical activity in our BIA?

**Reply (verbatim):**

That's a case for your organisation to decide, so I'll leave it unanswered and add it to the list for your BC manager. The sources don't say which of your activities are critical, and the guidance keeps that decision with people, not AI (`stages/govern.md`, Onboarding new BCM staff: the assistant "does not interpret a standard or decide a case").

The sources do describe **how** the decision gets made, which is worth knowing before you raise it:

- Criticality comes from the **impacts over time**, measured against impact categories, time horizons and thresholds your organisation agrees before the BIA starts (`workflow-design.md`, The BIA workflow, five stages).
- NIST says impacts are measured in "values or units of measurement that are meaningful to the organization" (NIST SP 800-34r1, §3.2.1). Recovery priorities are set "taking into consideration mission/business process criticality, outage impacts, tolerable downtime, and system resources" (NIST SP 800-34r1, §3.2.3).
- The **activity owner** approves the data and sets the MTPD and RTO, and **top management** approves the BIA results (`workflow-design.md`, The BIA workflow, five stages).

So the useful questions to bring are: what happens to payroll's impacts as a disruption goes on, measured against your agreed criteria, and who owns payroll as an activity?

---

## Where your organisation decides (updated)

For your BC manager, unanswered:

1. Which **impact categories, time horizons and thresholds** does your organisation use?
2. Who is the **activity owner** for each activity in your scope, and who in top management approves the BIA results?
3. Which **BIA template** does your organisation use, and does it use the term MTPD or MTD?
4. Does your BIA record **dependencies** separately from the four requirement classes?
5. **New:** should payroll count as a critical activity in your BIA, judged against your organisation's impact criteria by its activity owner?
