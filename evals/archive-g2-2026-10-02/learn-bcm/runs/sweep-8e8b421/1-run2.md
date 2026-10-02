# /learn-bcm case 1, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `b1401c17-08e4-44e0-97e4-03a9eb9c0ef3`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /learn-bcm

**Reply (verbatim):**

Before we start, one question on its own:

**Will you attach any of your own documents to this lesson (for example a plan, a BIA or a policy)? If so, what class of data do they hold (for example public, internal, confidential or strictly confidential)?**

I won't open any file until you've answered, and I'll stop if this environment isn't approved for that class. If you won't attach anything, just say "no documents". The lesson will then use only the guidance units and the open literature that come with this skill.

## Turn 2

**Request:** low

**Reply (verbatim):**

Thanks. Low-sensitivity material is fine here. Nothing is attached yet, so I haven't opened any file of yours. If you do attach one later, please keep out anything on the high-sensitivity list: BIA data, incident records, personal data, recovery strategies and similar (`units/data-rules.md`, Sensitivity classes).

**Reviewer:** you, the learner, check the lesson against the sources it cites before acting on it. A colleague or your BC manager answers anything that needs a case decided.

Now two questions:

1. **What part of the practice do you want to learn this session?** Keep it narrow, for example "what a BIA asks for", "the difference between RTO and RPO" or "what DORA requires for ICT continuity testing".
2. **What do you already know about it?** One line is enough, or say "skip".

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

I've read the BIA sources. The main one is the analysis stage unit, backed by the workflow unit, the glossary and NIST SP 800-34r1 §3.2. Here is your lesson.

*No learner documents used. Sources: AI4BCM units v2026.09.1; NIST SP 800-34 Rev. 1 (May 2010).*

**Your starting point:** you've seen a BIA form but never filled one in.

## Objective
By the end you can list, in order, what a BIA interview asks for, and say who sets the recovery times.

## What a BIA asks for

**1. What it is for.** A BIA is the "analysis of activities to determine the effects of disruption" (`units/glossary.md`, BIA). NIST puts its purpose as follows: to "characterize the consequences of a disruption" and so set contingency requirements and priorities (`literature/nist/sp-800-34r1…`, §3.2).

**2. What it produces.** "The outcome of a BIA is a list of requirements." A requirement "names what the activity needs to run, and states nothing about what the organisation has today" (`units/stages/analysis.md`, Method). A BIA doesn't check whether you already have a backup site. It records that the activity needs one.

**3. What the interview asks, in order** (`units/workflow-design.md`, The BIA workflow, five stages; `units/stages/analysis.md`, Method):

1. **Impacts over time.** What happens to the organisation as a disruption goes on.
2. **The MTPD.** "How long an activity can be down before the impact is unacceptable" (`units/glossary.md`, MTPD).
3. **Resource requirements, in four classes:**
   - **people**, "with the skills, authorities and mandates the work needs"
   - **seats and buildings**
   - **IT and applications**, "each with its RTO and its RPO"
   - **suppliers and other third parties**
4. **Dependencies.** These are up- and downstream links with other departments, each recorded with the RTO it carries. A link one department records then also shows up in the other department's BIA (`units/stages/analysis.md`, Method).

**4. The three time measures** (`units/glossary.md`):
- **MTPD:** the outer limit for the activity.
- **RTO:** "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity."
- **RPO:** the point to which the activity's information "must be restored."

NIST says the RTO "must normally be shorter than" the maximum tolerable downtime. It also says "RPO is not considered as part of MTD", because the RPO is about "how much data loss" can be tolerated (§3.2.1).

**5. Who decides what.** Impact categories, time horizons and thresholds are "agreed and supplied before stage 1 runs" (`units/workflow-design.md`, five stages). The activity owner "approves the data and sets MTPD and RTO". Top management "approves the BIA results before solutions design starts" (same section). An AI-drafted requirement "is only a question for the activity owner" (`units/stages/analysis.md`, Minimum controls).

**Read next:** NIST SP 800-34 Rev. 1, §3.2 "Conduct the Business Impact Analysis (BIA)", subsections 3.2.1 to 3.2.3 (`literature/nist/sp-800-34r1-contingency-planning-body.md`).

---

## Self-test
Answer from memory, without scrolling up. I'll give feedback after each answer.

**Question 1 of 4.** Which of these best describes one entry in a BIA's list of requirements?

- A) What the activity needs to run, whether or not it exists today
- B) What the organisation already has in place to run the activity
- C) What the risk owner has accepted as the residual risk for it

## Turn 4

**Request:** B

**Reply (verbatim):**

**Not quite. The right answer is A.**

A requirement "names what the activity needs to run, and states nothing about what the organisation has today" (`units/stages/analysis.md`, Method). The workflow unit says the same: a requirement "does not assert that the thing exists today" (`units/workflow-design.md`, The BIA workflow, five stages).

**The mix-up behind B:** treating the BIA as an inventory of what you have now. The BIA records what the activity *needs*. Comparing that need with what actually exists comes later, at solutions design, after top management approves the BIA results (same section). If you fill in a BIA with what you have today, you never see a gap, because the requirement always matches the current setup.

(C mixes up the BIA with risk assessment. Accepting risk belongs to the risk owner, a separate step: `units/stages/analysis.md`, Risk assessment.)

---

**Question 2 of 4.** From memory: name the **four classes** of resource requirements, in the order the interview covers them.

## Turn 5

**Request:** skip

**Reply (verbatim):**

Skipped. Here's the answer, so you have it:

1. **People**, "with the skills, authorities and mandates the work needs"
2. **Seats and buildings**
3. **IT and applications**, "each with its RTO and its RPO"
4. **Suppliers and other third parties**

(`units/stages/analysis.md`, Method)

The interview gets to these only "once the impacts and the MTPD are settled". Dependencies on other departments come after the four classes as a separate item (same section). To remember the order, think of it as working outwards: the people doing the work, the place they sit, the systems they use, then the outside parties they rely on.

---

**Question 3 of 4.** Which statement about RTO and RPO matches the sources?

- A) RPO sits within the MTPD and RTO measures how much data can be lost
- B) RTO and RPO are both set by the AI draft and confirmed by the BC team
- C) RTO sits within the MTPD and RPO measures how much data can be lost

## Turn 6

**Request:** C

**Reply (verbatim):**

**Correct: C.**

The RTO is "the time frame within the MTPD for resuming disrupted activities" (`units/glossary.md`, RTO). NIST adds that "the RTO must normally be shorter than the MTD" (`literature/nist/sp-800-34r1…`, §3.2.1). The RPO is different: "RPO is not considered as part of MTD. Rather, it is a factor of how much data loss the mission/business process can tolerate" (same section).

A swaps the two. B is wrong on two counts, which leads into the next question.

---

**Question 4 of 4.** From memory: **who sets the MTPD and the RTO** for an activity, and **who approves the BIA results** before solutions design starts?

## Turn 7

**Request:** The activity owner sets the MTPD and the RTO; top management approves the BIA results.

**Reply (verbatim):**

**Correct on both.**

The workflow unit puts the approvals "with the activity owner, who approves the data and sets MTPD and RTO, and with top management, which approves the BIA results before solutions design starts" (`units/workflow-design.md`, The BIA workflow, five stages). The analysis unit adds that AI "can test whether a proposed RTO fits the impact criteria. It does not set the RTO. The same holds for MTPD" (`units/stages/analysis.md`, Minimum controls). That is why option B in question 3 was wrong.

---

**Self-test result:** 2 correct (Q3, Q4), 1 wrong (Q1), 1 skipped (Q2).

Q1 and Q2 are worth revisiting. The point to hold onto from Q1 is that a requirement is what the activity *needs*, not what exists today. The four classes from Q2 are people, seats and buildings, IT and applications, then suppliers and third parties.

## Where your organisation decides
The sources leave these to your organisation. Take them to your BC manager:

- **Your impact categories, time horizons and thresholds.** The sources say they are "agreed and supplied before stage 1 runs" (`units/workflow-design.md`), but not what yours are.
- **Who counts as the "activity owner"** for each activity in your organisation's scope.
- **Your organisation's BIA template.** Which fields the form you've seen contains, and how they map to the interview order in this lesson.
- **Who signs for "top management"** when your BIA results are approved.

Before you act on anything here, check it against the cited passages. NIST SP 800-34r1 §3.2 is the next thing to read.

## Turn 8

**Request:** What does ISO 22301 say about the BIA, word for word?

**Reply (verbatim):**

I can't give you that. ISO 22301's wording is **not in the sources** for this lesson. The literature that ships with this skill includes no ISO text, and I teach only from those sources, not from memory.

Even with your own licensed copy, the rules would stay the same:

- **Its text never appears here.** ISO standards are copyrighted, so I wouldn't quote them word for word even from a licensed copy.
- **Clause numbers** would come only from your licensed copy, and only once you've confirmed the licence. Without that copy, I can't point you to a clause either.

What you can do:

- **Read it directly.** If your organisation holds a licence, your BC manager or document controller can tell you where the copy is kept. The governance unit allows "licensed standards text only where the licence permits" (`units/stages/govern.md`, Onboarding new BCM staff).
- **Use the open texts meanwhile.** NIST SP 800-34r1 §3.2 is free to read, and it covers the same ground as this lesson: processes and criticality, resource requirements, recovery priorities.

If your organisation's BIA method follows ISO 22301, how it applies that standard is a question for your BC manager.

## Turn 9

**Request:** Should our payroll count as a critical activity in our BIA?

**Reply (verbatim):**

I won't answer that one. Whether payroll counts as critical is a decision about your own organisation, and it goes to your BC manager.

Here is what the sources say about *how* that decision gets made. None of it settles the answer for payroll:

- Criticality comes from **impacts over time**, measured against impact categories, time horizons and thresholds your organisation agreed beforehand (`units/workflow-design.md`, The BIA workflow, five stages).
- The **activity owner** approves the data and sets the MTPD (same section), and **top management** approves the BIA results.
- NIST's example measures impact "in values or units of measurement that are meaningful to the organization", such as costs (`literature/nist/sp-800-34r1…`, §3.2.1).

So the answer depends on your thresholds and on what the payroll owner reports in the interview. The sources hold neither.

## Where your organisation decides (updated)
- Your impact categories, time horizons and thresholds.
- Who counts as the "activity owner" for each activity.
- Your organisation's BIA template and how its fields map to the interview order.
- Who signs for "top management" when the BIA results are approved.
- **New: whether payroll counts as a critical activity.** This is a case to decide, for the BC manager with the payroll activity owner.
