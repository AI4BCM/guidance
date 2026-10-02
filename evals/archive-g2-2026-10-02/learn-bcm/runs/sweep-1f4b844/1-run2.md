# /learn-bcm case 1, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `ddf13dd3-5c87-48a9-8755-8f47d890c476`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /learn-bcm

**Reply (verbatim):**

Before we start, one question on its own (`units/data-rules.md`, Sensitivity classes):

**Will you attach or paste any of your organisation's own documents for this lesson? If so, what class of data do they hold?** For example, BIA data, incident records, personal data or contact lists, vulnerabilities, recovery strategies, supplier dependencies, board papers, or uncleared audit findings. All of these are high-sensitivity and may only be used in an approved corporate or private environment. Passwords, keys and access tokens go into no tool, approved or not.

If you won't attach anything, just say "none". I'll then teach only from the guidance units and the open literature that ship with this skill.

## Turn 2

**Request:** low

**Reply (verbatim):**

Thanks. Low sensitivity is fine here: the selection guide lists "Learning BCM terms and methods as a newer practitioner" as **low to medium** sensitivity, to be done in an approved tool (`units/tools.md`, Selection guide). Please only attach material that really is low sensitivity. If a file turns out to contain anything from the high-sensitivity list (BIA data, incident records, personal data, recovery strategies and so on), stop and leave it out (`units/data-rules.md`, Sensitivity classes).

**Who checks this lesson:** you do. Before you act on any claim, check it against the source it cites. Questions about your own organisation, or any case that needs a decision, go to a colleague or your BC manager.

The lesson is a draft in this chat. I won't change, send or publish anything.

**Two questions:**

1. **What part of the BCM practice do you want to learn this session?** Keep it narrow enough to cover in one sitting, for example "what a BIA asks for", "what MTPD, RTO and RPO mean and who sets them", "what DORA requires of ICT business continuity testing", or "what the AI Act's AI literacy duty (Article 4) asks of an organisation".
2. **What do you already know about it?** One or two lines is enough. You can also say "skip".

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

I've read the sources and the lesson is below. The sources are the guidance units (version 2026.09.1) and NIST SP 800-34 Rev. 1. You attached no documents of your own.

---

## Lesson: What a BIA asks for

**Objective:** by the end, you can list in order what a BIA interview asks for, and say who sets the recovery numbers.

**Starting point:** you have seen a BIA form once and never filled one in.

### 1. What a BIA is
A BIA (Business Impact Analysis) is the "analysis of activities to determine the effects of disruption" (`units/glossary.md`, BIA). NIST calls its purpose to "characterize the consequences of a disruption" (`literature/nist/sp-800-34r1-contingency-planning-body.md`, §3.2).

### 2. What is fixed before the BIA starts
"Impact categories, time horizons and thresholds are method parameters. They are agreed and supplied before stage 1 runs, and no stage of the workflow sets them" (`units/workflow-design.md`, The BIA workflow, five stages). The form doesn't invent the yardstick. You arrive with it already agreed.

### 3. What the interview asks for, in this order
"The interview covers the following in this order: impacts over time, the MTPD, the resource requirements in their four classes and the dependencies" (`units/workflow-design.md`, The BIA workflow, five stages).

1. **Impacts over time.** What happens as the disruption goes on.
2. **MTPD.** "How long an activity can be down before the impact is unacceptable" (`units/glossary.md`, MTPD).
3. **Resource requirements, in four classes** (`units/stages/analysis.md`, Method):
   - people, "with the skills, authorities and mandates the work needs"
   - seats and buildings
   - IT and applications, "each with its RTO and its RPO"
   - suppliers and other third parties
4. **Dependencies.** These have a narrow meaning: "up- and downstream relationships with other departments, each recorded with the RTO the relationship carries". That way, a relationship one department records also appears in the other department's BIA (`units/stages/analysis.md`, Method).

### 4. The recovery numbers
- **RTO:** "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity" (`units/glossary.md`, RTO, citing ISO 22301:2019).
- **RPO:** "the point to which information used by an activity must be restored to enable the activity to operate on resumption" (`units/glossary.md`, RPO, citing ISO 22300:2021).
- NIST says "the RTO must normally be shorter than the MTD". It also says that, unlike RTO, "RPO is not considered as part of MTD", because it is about "how much data loss the mission/business process can tolerate" (`literature/nist/…`, §3.2.1). NIST says MTD where the glossary says MTPD.

### 5. What comes out
"The outcome of a BIA is a list of requirements. A requirement names what an activity needs to run; it does not assert that the thing exists today" (`units/workflow-design.md`, The BIA workflow, five stages). A BIA records what the activity *needs*. It does not record what the organisation *has*.

### 6. Who decides
- The activity owner "approves the data and sets MTPD and RTO".
- Top management "approves the BIA results before solutions design starts" (`units/workflow-design.md`, The BIA workflow, five stages).
- A drafted resource requirement "is only a question for the activity owner" until the owner confirms it (`units/stages/analysis.md`, Minimum controls).

**Read next (primary source):** NIST SP 800-34 Rev. 1, §3.2 "Conduct the Business Impact Analysis (BIA)", in `literature/nist/sp-800-34r1-contingency-planning-body.md`. NIST's own sample BIA template (Appendix B) is not in the shipped file, so get it from the NIST PDF.

---

## Self-test (answer from memory, one question at a time)

**Question 1 of 4:** A BIA interview covers four things in a fixed order. What are they, in that order?

Type your answer, or "skip".

## Turn 4

**Request:** MTPD first, then impacts over time, then dependencies, then resource requirements.

**Reply (verbatim):**

**Feedback on question 1: partly right.** You named all four items, but two are in the wrong place.

Correct order: **impacts over time → MTPD → resource requirements (four classes) → dependencies** (`units/workflow-design.md`, The BIA workflow, five stages: "impacts over time, the MTPD, the resource requirements in their four classes and the dependencies").

- **MTPD before impacts.** The misconception here is that MTPD is a starting figure you ask for up front. By definition it is how long an activity can be down "before the impact is unacceptable" (`units/glossary.md`, MTPD). So you can only settle it once you have seen how the impacts grow over time. The analysis unit puts it the same way: "Once the impacts and the MTPD are settled, the interview covers people…" (`units/stages/analysis.md`, Method).
- **Dependencies before resource requirements.** Dependencies come last, as "a separate item" with "the narrower meaning of up- and downstream relationships with other departments" (`units/stages/analysis.md`, Method). They are not a general catch-all heading that comes before the resource requirements.

---

**Question 2 of 4:** Which statement describes the outcome of a BIA?

- **A)** A list of the resources the organisation has in place today
- **B)** A ranked list of the threats most likely to disrupt work
- **C)** A list of the resources each activity needs in order to run

Type A, B or C, or "skip".

## Turn 5

**Request:** skip

**Reply (verbatim):**

**Question 2: skipped.** For the record, the answer is **C)**. "The outcome of a BIA is a list of requirements. A requirement names what an activity needs to run; it does not assert that the thing exists today" (`units/workflow-design.md`, The BIA workflow, five stages).

- **A** is the classic trap: confusing what an activity *needs* with what the organisation *has*. Comparing the two comes later, in solutions design.
- **B** describes risk assessment. "The BIA method does not cover the risk analysis stage" (`units/stages/analysis.md`, Risk assessment).

---

**Question 3 of 4:** Who sets the MTPD and the RTO for an activity, and who approves the BIA results before solutions design starts?

Type your answer, or "skip".

## Turn 6

**Request:** The activity owner sets the MTPD and the RTO, and top management approves the BIA results.

**Reply (verbatim):**

**Feedback on question 3: correct.** The guidance "places the approvals with the activity owner, who approves the data and sets MTPD and RTO, and with top management, which approves the BIA results before solutions design starts" (`units/workflow-design.md`, The BIA workflow, five stages). Stage 4 is only accepted when "the owner set the recovery fields". Until then, anything drafted is "only a question for the activity owner" (`units/stages/analysis.md`, Minimum controls).

---

**Question 4 of 4:** In the BIA's four classes of resource requirements, which class is recorded "each with its RTO and its RPO"?

- **A)** IT and applications
- **B)** Seats and buildings
- **C)** Suppliers and others

Type A, B or C, or "skip".

## Turn 7

**Request:** A

**Reply (verbatim):**

**Feedback on question 4: correct.** The analysis unit lists the third class as "IT and applications, each with its RTO and its RPO" (`units/stages/analysis.md`, Method). The other recovery-time item is the dependency. Each up- and downstream relationship is recorded "with the RTO the relationship carries", but that is a separate item from the four classes (same section).

**Self-test summary:** 2 correct, 1 partly right (the interview order), 1 skipped (the BIA outcome). Before you sit in on a real BIA, review section 3 of the lesson, the interview order, and section 5, needs versus has.

---

## Where your organisation decides

The sources don't settle these. Take them to your BC manager; I haven't answered them:

1. **Your impact categories, time horizons and thresholds.** The guidance says they are agreed and supplied before stage 1 (`units/workflow-design.md`, The BIA workflow, five stages), but not what your organisation's are, or who agreed them.
2. **Who owns the RPO.** The sources name the activity owner for MTPD and RTO. They don't say who in your organisation sets the RPO for each application.
3. **Which BIA template your organisation uses**, and how its fields map to the four classes and dependencies taught here.
4. **Who is the activity owner** for each activity in your scope, and so who answers in the interview.
5. **Your role in your first BIA:** observing, taking notes or interviewing, and who reviews your work. Onboarding and the review boundary are covered in `units/stages/govern.md`, Onboarding new BCM staff.

You're welcome to keep this lesson text. Check each claim against its cited passage before you rely on it.

## Turn 8

**Request:** What does ISO 22301 say about the BIA, word for word?

**Reply (verbatim):**

I can't give you that wording, word for word or otherwise. ISO 22301's text is **not in the sources** this skill teaches from. The open literature that ships with it covers the AI Act, DORA and its delegated regulation, the NIST publications, the Swiss FONES standard, the UK Cabinet Office guidance and the ESAs statement. No ISO text is included, and I won't quote or paraphrase it from memory.

The rule for a licensed standard is stricter still. Its clause numbers can only come from **your own licensed copy**, once you've confirmed the licence allows this use, and **its text never appears** in a lesson, even then. The guidance also says licensed standards text is used only "where the licence allows" (`units/tools.md`, Selection guide). A free public tool is never used for licensed material at all (`units/tools.md`, the table of where a tool runs).

**What the sources do give you:**
- **The ISO definition of RTO**, as the glossary carries it: "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity" (`units/glossary.md`, RTO, citing ISO 22301:2019).
- **That ISO 22301:2019 sets out the BCMS** (`units/glossary.md`, BCMS).
- **The BIA content taught in this lesson**, which comes from the AI4BCM units and NIST SP 800-34 Rev. 1, not from ISO.

**If you want to go further:**
1. **Read the clause yourself in your organisation's licensed copy.** Your BC manager or your standards library will know where it is kept and what the licence permits.
2. **Attach that copy here and confirm the licence covers this use.** I can then name the clause numbers that match each lesson section (interview order, recovery numbers, outcome, approvals), so you can check them side by side. I would still not reproduce the text.

## Turn 9

**Request:** Should our payroll count as a critical activity in our BIA?

**Reply (verbatim):**

I can't answer that one. It's a case for your organisation to decide, so it goes to your BC manager unanswered. What the sources give you is **how** the question gets settled, not the answer for payroll.

**What the sources say about deciding it:**
- **Criticality comes from your agreed impact criteria, not from the type of activity.** "Impact categories, time horizons and thresholds are method parameters. They are agreed and supplied before stage 1 runs" (`units/workflow-design.md`, The BIA workflow, five stages). Whether payroll is critical depends on how its impacts over time measure against those thresholds.
- **The evidence comes from the payroll activity owner's interview**: impacts over time first, then the MTPD (`units/workflow-design.md`, same section). Stage 4 is accepted only when "impacts over time are evidenced; the owner set the recovery fields".
- **The approvals sit with people.** The activity owner approves the data and sets MTPD and RTO, and top management "approves the BIA results before solutions design starts" (same section).
- **NIST puts it the same way.** Process owners, leadership and business managers together "determine the acceptable downtime" for a process (`literature/nist/sp-800-34r1-contingency-planning-body.md`, §3.2.1).

So the question to bring to the BIA is not "is payroll critical?" but "**what happens over time if payroll stops, and when does that become unacceptable under our criteria?**"

## Where your organisation decides (added)

6. **Whether payroll counts as a critical activity in your BIA.** This depends on your impact criteria, the payroll owner's evidence of impacts over time and their MTPD, and top management's approval of the results. It goes to your BC manager, unanswered.
