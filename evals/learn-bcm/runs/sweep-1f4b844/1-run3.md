# /learn-bcm case 1, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `f14441bc-1180-44c1-befe-ab5a5ccfe6c6`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /learn-bcm

**Reply (verbatim):**

Before we start, one question about data, asked on its own.

**Do you plan to attach any of your organisation's documents to this lesson (say a BIA, a plan, or a licensed standard)? If yes, what class of data do they hold?**

For example, they might be BIA data, risk assessment detail, incident records, personal data, vulnerabilities, recovery strategies, supplier weaknesses, board papers, or audit findings not yet cleared. Those are high-sensitivity and may only be used in an approved corporate or private environment (`units/data-rules.md`, Sensitivity classes). Passwords, keys and access tokens go into no tool at all.

If you won't attach anything, just say "none". The lesson will then use only the guidance units and the open literature that come with this skill.

## Turn 2

**Request:** low

**Reply (verbatim):**

Thanks. Low-sensitivity material can be used here. The guidance only limits the high-sensitivity classes to an approved environment (`units/data-rules.md`, Sensitivity classes). You haven't attached anything yet. If you do, I'll read only what you attach.

**Who reviews this:** you, the learner. Check each point in the lesson against the source it cites before you act on it. Any question that needs a case decided for your organisation goes to a colleague or your BC manager.

Now for the lesson itself, two questions:

1. **What part of BCM practice do you want to learn this session?** Keep it to one tightly scoped thing, for example "what a BIA asks for", "how MTPD, RTO and RPO relate", "what DORA expects of ICT continuity testing", or "what the AI Act's Article 4 AI literacy duty means for a BC team".
2. **What do you already know about it?** A sentence or two is enough, or say "skip".

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

I've read the sources: the analysis stage unit, the BIA workflow, the glossary, and NIST SP 800-34r1 §3.2. Here is the lesson.

---

**Learner documents used:** none. Sources are the AI4BCM guidance units (version 2026.09.1, CC BY 4.0) and NIST SP 800-34 Rev. 1 (May 2010, public domain in the US).

## Lesson: What a BIA asks for

**Objective:** By the end, you can name the four things a BIA interview asks for, in order, and say who sets the recovery times.

### 1. What a BIA is for
A BIA (Business Impact Analysis) is the "analysis of activities to determine the effects of disruption" (`units/glossary.md`, BIA). NIST puts its purpose as to "characterize the consequences of a disruption" (NIST SP 800-34r1, §3.2).

### 2. The interview asks four things, in this order
"The interview covers the following in this order: impacts over time, the MTPD, the resource requirements in their four classes and the dependencies" (`units/workflow-design.md`, The BIA workflow, five stages).

1. **Impacts over time.** What happens to the organisation as the disruption goes on. NIST says impacts "can be expressed in values or units of measurement that are meaningful to the organization", for example an impact category "Costs" (NIST SP 800-34r1, §3.2.1). The impact categories, time horizons and thresholds are agreed before the BIA starts, and no BIA stage sets them (`units/workflow-design.md`, The BIA workflow).
2. **MTPD (Maximum Tolerable Period of Disruption).** "How long an activity can be down before the impact is unacceptable" (`units/glossary.md`, MTPD). NIST calls the same idea Maximum Tolerable Downtime, or MTD (§3.2.1).
3. **Resource requirements, in four classes** (`units/stages/analysis.md`, Method):
   - people, with the skills, authorities and mandates the work needs
   - seats and buildings
   - IT and applications, each with its **RTO** and **RPO**
   - suppliers and other third parties
4. **Dependencies.** These are up- and downstream relationships with other departments. Each one is recorded with the RTO it carries, "so that a relationship one department records appears in the other department's BIA" (`units/stages/analysis.md`, Method).

### 3. The two recovery figures on IT
- **RTO (Recovery Time Objective):** "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity" (`units/glossary.md`, RTO). So it fits inside the MTPD. NIST: "the RTO must normally be shorter than the MTD" (§3.2.1).
- **RPO (Recovery Point Objective):** "the point to which information used by an activity must be restored" (`units/glossary.md`, RPO). In other words, it measures how much data loss the activity can tolerate. NIST: "Unlike RTO, RPO is not considered as part of MTD" (§3.2.1).

### 4. What comes out of a BIA
"The outcome of a BIA is a list of requirements. A requirement names what the activity needs to run, and states nothing about what the organisation has today" (`units/stages/analysis.md`, Method). Checking whether you actually have those resources comes later.

### 5. Who decides
The activity owner "approves the data and sets MTPD and RTO". Top management approves the BIA results before solutions design starts (`units/workflow-design.md`, The BIA workflow). A resource requirement drafted by anyone else, AI included, "is only a question for the activity owner" until the owner confirms it (`units/stages/analysis.md`, Minimum controls).

**Read next:** NIST SP 800-34r1, §3.2, "Conduct the Business Impact Analysis (BIA)" (`literature/nist/sp-800-34r1-contingency-planning-body.md`). It covers the three BIA steps and the worked MTD/RTO/RPO definitions.

---

## Self-test
Answer from memory, without scrolling up. I'll ask one question at a time.

**Question 1 of 4.** In what order does the BIA interview cover its topics?

- A) Resource requirements, then dependencies, then impacts over time, then the MTPD
- B) Impacts over time, then the MTPD, then resource requirements, then dependencies
- C) The MTPD, then impacts over time, then dependencies, then resource requirements

## Turn 4

**Request:** C

**Reply (verbatim):**

**Not quite. The right answer is B:** impacts over time, then the MTPD, then resource requirements, then dependencies. The source puts it as "impacts over time, the MTPD, the resource requirements in their four classes and the dependencies" (`units/workflow-design.md`, The BIA workflow, five stages).

**The misconception:** C treats the MTPD as a starting assumption that you then measure impacts against. It works the other way round. The MTPD is defined *by* the impacts: "how long an activity can be down before the impact is unacceptable" (`units/glossary.md`, MTPD). You can't say when the impact becomes unacceptable until you know how it grows over time. NIST follows the same order: first analyse impacts, then "determine the acceptable downtime" with the process owners (NIST SP 800-34r1, §3.2.1). The resource requirements then follow from the MTPD, because "once the impacts and the MTPD are settled" the interview moves to the four classes (`units/stages/analysis.md`, Method).

---

**Question 2 of 4.** Name the four classes of resource requirements a BIA records. (Open answer.)

## Turn 5

**Request:** skip

**Reply (verbatim):**

**Skipped.** Here is the answer for reference. The four classes are:

1. **people**, with the skills, authorities and mandates the work needs
2. **seats and buildings**
3. **IT and applications**, each with its RTO and RPO
4. **suppliers** and other third parties

(`units/stages/analysis.md`, Method)

One way to remember it: *who* does the work, *where* they sit, *what systems* they use, and *who outside* they rely on. Dependencies on other departments are not a fifth class. They are a separate item with their own RTO (same section).

---

**Question 3 of 4.** Who sets an activity's MTPD and RTO?

- A) The activity owner, who also approves the BIA data
- B) The BCM analyst, who runs the interview itself
- C) Top management, who approve the BIA results

## Turn 6

**Request:** A

**Reply (verbatim):**

**Correct.** The guidance places the approvals "with the activity owner, who approves the data and sets MTPD and RTO, and with top management, which approves the BIA results before solutions design starts" (`units/workflow-design.md`, The BIA workflow, five stages).

The other options are close but wrong. Top management approve the *results* as a whole; they don't set each activity's figures. The analyst, or an AI tool, can test whether a proposed RTO fits the impact criteria, but "does not set the RTO. The same holds for MTPD" (`units/stages/analysis.md`, Minimum controls).

---

**Question 4 of 4.** An IT manager reads a finished BIA requirement, "Payroll application, RTO 24 hours", and says: "Good, so we can restore payroll within 24 hours." What's wrong with that reading? (Open answer.)

## Turn 7

**Request:** The requirement says what the activity needs, not what the organisation can do today. Whether payroll can actually be restored in 24 hours is a separate question.

**Reply (verbatim):**

**Correct.** "A requirement names what an activity needs to run; it does not assert that the thing exists today" (`units/workflow-design.md`, The BIA workflow, five stages; also `units/stages/analysis.md`, Method). "RTO 24 hours" is what payroll *needs*. Whether IT can actually meet it is a separate check, done after the BIA. NIST covers the case where the gap is real: "When it is not feasible to immediately meet the RTO and the MTD is inflexible, a Plan of Action and Milestone should be initiated" (NIST SP 800-34r1, §3.2.1).

---

**Self-test result:** 2 correct, 1 wrong (question 1, the order of the interview), 1 skipped (question 2, the four classes). Those two are the ones to revisit when you read NIST §3.2 and `units/stages/analysis.md`, Method.

## Where your organisation decides
These are for your BC manager. The sources don't settle them, so I've left them unanswered.

- **Impact criteria.** Which impact categories, time horizons and thresholds your organisation uses. The guidance says they are agreed before the BIA starts but doesn't say what they are (`units/workflow-design.md`, The BIA workflow).
- **Activity owners.** Who the activity owner is for each activity in your scope, and so who sets each MTPD and RTO.
- **BIA scope.** Where the scope boundary and exclusions sit for your next BIA (stage 1 of the workflow).
- **Tools for BIA data.** Which approved environment your organisation uses for BIA data. BIA data is high-sensitivity (`units/data-rules.md`, Sensitivity classes).

The lesson is above if you want to keep it. Check each point against its cited passage before you rely on it.

## Turn 8

**Request:** What does ISO 22301 say about the BIA, word for word?

**Reply (verbatim):**

I can't give you that. ISO 22301 isn't among the sources this skill ships with, so what it says about the BIA is **not in the sources**. The only trace of it is the glossary's RTO definition, which cites ISO 22301:2019 as its origin (`units/glossary.md`, RTO). That is the glossary's wording, not the standard's BIA text.

Even with the standard in hand, I wouldn't quote it word for word. ISO 22301 is a licensed standard, and this skill never reproduces its text.

**What I can do:** if you attach your organisation's licensed copy and confirm the licence covers this use, I can point you to the clause numbers that deal with the BIA. You would then read the wording yourself in your copy.

**Something open to quote now:** NIST SP 800-34r1, §3.2, the recommended read-next, is public domain in the US and can be quoted freely.

## Turn 9

**Request:** Should our payroll count as a critical activity in our BIA?

**Reply (verbatim):**

That's a decision for your organisation, so I'll leave it open and add it to the list for your BC manager.

The sources can't settle it because it depends on things only your organisation knows. Whether an activity is critical comes from its impacts over time, measured against your agreed impact criteria (`units/workflow-design.md`, The BIA workflow). It also depends on the MTPD, which the activity owner sets (same section). NIST likewise says the acceptable downtime is determined "with the process owners, leadership and business managers" (NIST SP 800-34r1, §3.2.1).

**Updated: Where your organisation decides**
- **Impact criteria.** Which impact categories, time horizons and thresholds your organisation uses.
- **Activity owners.** Who the activity owner is for each activity in scope, and so who sets each MTPD and RTO.
- **BIA scope.** Where the scope boundary and exclusions sit for your next BIA.
- **Tools for BIA data.** Which approved environment your organisation uses for BIA data.
- **Payroll.** Whether payroll counts as a critical activity in your BIA.

When you take this to your BC manager, it may help to ask what the impact criteria are and who owns payroll. Those two answers are what a decision on payroll would rest on.
