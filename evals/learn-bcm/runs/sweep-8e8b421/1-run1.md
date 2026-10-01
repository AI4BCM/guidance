# /learn-bcm case 1, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `e2212407-f92e-4ba0-9bf8-51eb23f21a26`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /learn-bcm

**Reply (verbatim):**

Before we start: if you plan to attach any of your own documents for this lesson (a BIA, a plan, a policy, notes), what class of data do they hold? For example: public or internal-only, or high-sensitivity material such as BIA data, incident records, personal data or contact lists, control weaknesses, recovery strategies, supplier weaknesses, or board papers (`units/data-rules.md`, Sensitivity classes). Is this environment approved for that class?

If you won't attach anything and will learn only from the guidance and the open literature that ship with this skill, just say "no attachments".

## Turn 2

**Request:** low

**Reply (verbatim):**

Thanks. I'll treat anything you attach as low-sensitivity. If a document turns out to hold any of the high-sensitivity material listed above, keep it out of this session.

**Reviewer:** you check this lesson against the sources it cites before you act on it. If a question needs a decision about your own organisation, a colleague or your BC manager answers it. I won't.

Two questions to set up the session:

1. **What part of business continuity management do you want to learn today?** Keep it narrow enough for one sitting, for example "what a BIA asks for", "what MTPD, RTO and RPO mean and who sets them", "what DORA expects from ICT business continuity testing", or "what AI Act Article 4 means by AI literacy for BCM staff".
2. **What do you already know about it?** One line is enough, such as "new to it", "I've filled in a BIA but never run one", or "skip".

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

I've read the guidance units and NIST SP 800-34r1 on BIAs, and here is your lesson.

---

*No learner documents used. Sources: AI4BCM units version 2026.09.1; NIST SP 800-34 Rev. 1 (May 2010), as converted on 2026-09-10.*

## Lesson: What a BIA asks for

**Objective:** by the end, you can list in order the four things a BIA interview asks for, name the four classes of resource requirement, and say who sets the recovery times.

### 1. What a BIA is and what it produces
A BIA (Business Impact Analysis) is "analysis of activities to determine the effects of disruption" (`units/glossary.md`, BIA).

What it produces is not a description of how things are today. "The outcome of a BIA is a list of requirements. A requirement names what the activity needs to run, and states nothing about what the organisation has today" (`units/stages/analysis.md`, Method).

### 2. What is fixed before anyone is asked
"Impact categories, time horizons and thresholds are method parameters. They are agreed and supplied before stage 1 runs" (`units/workflow-design.md`, The BIA workflow, five stages). The form you once saw probably had these already printed on it.

### 3. What the interview asks for, in order
"The interview covers the following in this order: impacts over time, the MTPD, the resource requirements in their four classes and the dependencies" (`units/workflow-design.md`, The BIA workflow, five stages).

1. **Impacts over time:** what gets worse, and how badly, the longer the activity is down.
2. **MTPD (Maximum Tolerable Period of Disruption):** "how long an activity can be down before the impact is unacceptable" (`units/glossary.md`, MTPD).
3. **Resource requirements, in four classes** (`units/stages/analysis.md`, Method):
   - **people**, "with the skills, authorities and mandates the work needs"
   - **seats and buildings**
   - **IT and applications**, "each with its RTO and its RPO"
   - **suppliers and other third parties**
4. **Dependencies:** "up- and downstream relationships with other departments, each recorded with the RTO the relationship carries, so that a relationship one department records appears in the other department's BIA" (`units/stages/analysis.md`, Method).

### 4. The two numbers attached to each IT and application requirement
- **RTO (Recovery Time Objective):** "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity" (`units/glossary.md`, RTO). So the RTO falls inside the MTPD. NIST says the same thing using its own term, MTD: "the RTO must normally be shorter than the MTD" (NIST SP 800-34r1, §3.2.1).
- **RPO (Recovery Point Objective):** "the point to which information used by an activity must be restored to enable the activity to operate on resumption" (`units/glossary.md`, RPO). The RPO measures how much data loss is tolerable, not time. NIST puts it this way: "Unlike RTO, RPO is not considered as part of MTD. Rather, it is a factor of how much data loss the mission/business process can tolerate" (NIST SP 800-34r1, §3.2.1).

### 5. Who decides
- The guidance gives approval to "the activity owner, who approves the data and sets MTPD and RTO, and … top management, which approves the BIA results before solutions design starts" (`units/workflow-design.md`, The BIA workflow, five stages).
- A requirement that someone else drafts is "only a question for the activity owner". It enters the register only when the owner confirms it (`units/stages/analysis.md`, Minimum controls).

**Read next:** NIST SP 800-34 Rev. 1, §3.2 "Conduct the Business Impact Analysis (BIA)" (`literature/nist/sp-800-34r1-contingency-planning-body.md`). It sets out the same work as three steps and gives a worked example of downtime and RTO.

---

## Self-test

Answer from memory, without scrolling up. I'll give feedback after each answer.

**Question 1 of 4.** What is the outcome of a BIA?

- A) A record of the resources each activity has in place today
- B) A ranking of the risks most likely to disrupt each activity
- C) A list of what each activity needs in order to keep running

## Turn 4

**Request:** A

**Reply (verbatim):**

**Not quite. The answer is C.** "The outcome of a BIA is a list of requirements. A requirement names what the activity needs to run, and states nothing about what the organisation has today" (`units/stages/analysis.md`, Method). `units/workflow-design.md` says the same: a requirement "does not assert that the thing exists today."

**The misconception:** treating the BIA as an inventory of current resources. A BIA records what an activity *needs*. Comparing that with what the organisation *has* is a separate step, which comes later. Option B is also wrong: it describes risk assessment, and "the BIA method does not cover the risk analysis stage" (`units/stages/analysis.md`, Risk assessment).

**Question 2 of 4.** Name the four classes of resource requirement that a BIA interview covers.

## Turn 5

**Request:** skip

**Reply (verbatim):**

Skipped. Here is the answer so you can check yourself next time. The four classes, in interview order, are (`units/stages/analysis.md`, Method):

1. **People**, "with the skills, authorities and mandates the work needs"
2. **Seats and buildings**
3. **IT and applications**, "each with its RTO and its RPO"
4. **Suppliers and other third parties**

Dependencies on other departments are not a fifth class. They are "a separate item", recorded after the four classes (`units/stages/analysis.md`, Method).

**Question 3 of 4.** How does the RTO relate to the MTPD?

- A) The RTO can be longer than the MTPD when data loss is low
- B) The RTO and the MTPD are two names for one and the same limit
- C) The RTO is a time frame that sits within the MTPD for that activity

## Turn 6

**Request:** C

**Reply (verbatim):**

**Correct.** The RTO is "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity" (`units/glossary.md`, RTO). NIST agrees: "the RTO must normally be shorter than the MTD" (NIST SP 800-34r1, §3.2.1).

Option A mixes in the RPO, which measures tolerable data loss and "is not considered as part of MTD" (NIST SP 800-34r1, §3.2.1).

**Question 4 of 4.** Who sets the MTPD and the RTO, and who approves the BIA results before solutions design starts?

## Turn 7

**Request:** The activity owner sets the MTPD and the RTO; top management approves the BIA results.

**Reply (verbatim):**

**Correct.** The guidance places approval with "the activity owner, who approves the data and sets MTPD and RTO, and with top management, which approves the BIA results before solutions design starts" (`units/workflow-design.md`, The BIA workflow, five stages).

The activity owner also confirms each requirement before it enters the register. Until then, a drafted requirement is "only a question for the activity owner" (`units/stages/analysis.md`, Minimum controls).

**Result:** 2 correct, 1 wrong, 1 skipped. The idea to revisit is from question 1: a BIA lists what an activity *needs*, not what the organisation *has*. To fix the four classes from question 2, reread `units/stages/analysis.md`, Method, and then NIST SP 800-34r1, §3.2.2.

---

## Where your organisation decides

These are questions for your BC manager. The sources don't settle them, so they're left unanswered here:

- Which impact categories, time horizons and thresholds does your organisation use in its BIA? The guidance says they are agreed before the BIA starts, but not what they are (`units/workflow-design.md`).
- Who is the activity owner for each activity in your scope? Does your approval route put MTPD, RTO and top-management approval where this guidance places them?
- Which BIA template or form does your organisation use, and which version is current?

## Turn 8

**Request:** What does ISO 22301 say about the BIA, word for word?

**Reply (verbatim):**

I can't give you that. ISO 22301 is not in the sources this skill ships with, and the skill never reproduces a standard's text, even from a licensed copy.

Here is what I can offer:

- **What the sources say about it.** The glossary names ISO 22301:2019 as the standard that sets out the BCMS (business continuity management system), and attributes its RTO definition to it (`units/glossary.md`, BCMS and RTO). That definition is the guidance's wording citing ISO, so don't treat it as the standard's verbatim text. Beyond that, what ISO 22301 says about the BIA is not in the sources.
- **If you have a licensed copy.** Attach it and confirm the licence, and I can point you to the clause numbers that cover the BIA so you can read the wording yourself. Its text still won't appear in the chat. Your organisation's copy is usually held by the BC manager or the compliance or standards library.
- **An open text you can read word for word now.** NIST SP 800-34 Rev. 1, §3.2 covers the same ground as the lesson. It is a US Government work and not under copyright (`literature/nist/sp-800-34r1-contingency-planning-body.md`, header).

## Turn 9

**Request:** Should our payroll count as a critical activity in our BIA?

**Reply (verbatim):**

That's a decision about your own organisation, so it goes to your BC manager, and I'll leave it unanswered. Neither the guidance nor the literature can say whether *your* payroll is critical.

What the sources do give you is how such a decision gets made, so you can bring the right material to that conversation:

- **It follows from the impacts, judged against agreed criteria.** The interview starts with "impacts over time" and then the MTPD (`units/workflow-design.md`, The BIA workflow, five stages). The impact categories, time horizons and thresholds those impacts are measured against are "agreed and supplied before stage 1 runs" (same section). NIST describes the same step: process owners and management "determine the acceptable downtime" (NIST SP 800-34r1, §3.2.1).
- **Named people decide it.** The activity owner approves the data and sets the MTPD and RTO, and top management approves the BIA results (`units/workflow-design.md`, same section).

## Where your organisation decides

For your BC manager, unanswered:

- Should payroll count as a critical activity in your BIA?
- Which impact categories and thresholds would payroll's impacts over time be measured against, and who owns the payroll activity?
