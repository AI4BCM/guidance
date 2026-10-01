# /learn-bcm case 1, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `7c664625-9814-40a6-91b4-3ff2eed38cf2`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /learn-bcm

**Reply (verbatim):**

Before we start, one question about data.

If you plan to attach any of your own documents for this lesson (a policy, BIA template, plan extract, or anything similar), what class of data do they hold? For example:

- **Low:** public or generic material that says nothing about your organisation
- **Medium:** internal but not sensitive, such as an approved policy or awareness content
- **High:** BIA data, risk detail, incident records, personal data or contact lists, vulnerabilities, recovery strategies, supplier weaknesses, board papers, or audit findings not yet cleared (`units/data-rules.md`, Sensitivity classes)

Also, is this environment approved by your organisation for that class? If you won't attach anything and only want to learn from the guidance and the open literature that come with this skill, just say "no attachments".

## Turn 2

**Request:** low

**Reply (verbatim):**

Low-sensitivity material is fine here (`units/tools.md`, Selection guide: learning BCM terms and methods is "low to medium"). If you attach a document, say so and I'll read it before we begin. Keep passwords, keys and access tokens out of the chat (`units/data-rules.md`).

**Reviewer:** you check the lesson against the sources it cites before you act on it. Any question that needs a decision about your own organisation goes to your BC manager, or to a colleague they name.

**What would you like to learn this session?** Pick one part of the practice that fits in a single sitting, for example:

- what a BIA asks for
- how MTPD, RTO and RPO relate to each other
- what DORA asks of an ICT business continuity policy
- what makes a good exercise or test

**What do you already know about it?** A sentence is enough, such as "new to it", "I've sat in BIA interviews but never led one", or "skip".

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

I've read the analysis stage unit, the BIA workflow, the glossary and the BIA section of NIST SP 800-34r1. The lesson is below, and the first self-test question follows it.

No learner document was used. The sources are the AI4BCM units, version 2026.09.1, and NIST SP 800-34 Rev. 1 (May 2010, Chapters 1–5).

# Lesson: What a BIA asks for

**Objective:** by the end, you can list the four things a BIA interview covers, in order, and name the four classes of resource requirement.

**Your starting point:** you've seen a BIA form once and never filled one in.

### 1. What a BIA is for
- A BIA is the "analysis of activities to determine the effects of disruption" (`units/glossary.md`, BIA).
- NIST puts its purpose like this: to "characterize the consequences of a disruption" and to use the results "to determine contingency planning requirements and priorities" (NIST SP 800-34r1, §3.2).

### 2. What it produces
- "The outcome of a BIA is a list of requirements. A requirement names what an activity needs to run; it does not assert that the thing exists today" (`units/workflow-design.md`, The BIA workflow, five stages).
- So a BIA says "this activity needs X". Whether you have X today is a separate question.

### 3. What the interview asks, in this order
"The interview covers the following in this order: impacts over time, the MTPD, the resource requirements in their four classes and the dependencies" (`units/workflow-design.md`, same section).

1. **Impacts over time:** how bad the disruption gets as it goes on.
2. **MTPD (Maximum Tolerable Period of Disruption):** "how long an activity can be down before the impact is unacceptable" (`units/glossary.md`, MTPD).
3. **Resource requirements, in four classes** (`units/stages/analysis.md`, Method):
   - **people**, "with the skills, authorities and mandates the work needs"
   - **seats and buildings**
   - **IT and applications**, "each with its RTO and its RPO"
   - **suppliers and other third parties**
4. **Dependencies:** "up- and downstream relationships with other departments, each recorded with the RTO the relationship carries". That way a relationship one department records also appears in the other department's BIA (`units/stages/analysis.md`, Method).

### 4. The recovery numbers
- **RTO (Recovery Time Objective):** "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity" (`units/glossary.md`, RTO).
- **RPO (Recovery Point Objective):** "the point to which information used by an activity must be restored to enable the activity to operate on resumption" (`units/glossary.md`, RPO).
- NIST adds two points (§3.2.1):
  - "the RTO must normally be shorter than the MTD"
  - "Unlike RTO, RPO is not considered as part of MTD", because RPO is about "how much data loss the mission/business process can tolerate"
- NIST uses the term "Maximum Tolerable Downtime (MTD)" for the downtime threshold (§3.2.1).

### 5. Who decides what
- Impact categories, time horizons and thresholds "are agreed and supplied before stage 1 runs" (`units/workflow-design.md`, The BIA workflow).
- The activity owner "approves the data and sets MTPD and RTO", and top management "approves the BIA results before solutions design starts" (same section).
- An AI-drafted requirement "is only a question for the activity owner" (`units/stages/analysis.md`, Minimum controls).

**Read next:** NIST SP 800-34r1, §3.2 "Conduct the Business Impact Analysis (BIA)", in `literature/nist/sp-800-34r1-contingency-planning-body.md`. It walks through the same steps for an information system. The sample BIA template (Appendix B) is not in the shipped file, so get it from the NIST PDF.

---

## Self-test

Answer from memory, without scrolling back up. Type "skip" to pass on a question.

**Question 1 of 4.** In what order does the BIA interview cover these topics?

- A) MTPD → impacts over time → dependencies → resource requirements
- B) impacts over time → MTPD → resource requirements → dependencies
- C) resource requirements → impacts over time → MTPD → dependencies
- D) impacts over time → resource requirements → dependencies → MTPD

## Turn 4

**Request:** A

**Reply (verbatim):**

**Not quite. The right answer is B:** impacts over time → MTPD → resource requirements → dependencies. The source says: "The interview covers the following in this order: impacts over time, the MTPD, the resource requirements in their four classes and the dependencies" (`units/workflow-design.md`, The BIA workflow, five stages).

**The misconception behind A** is that the MTPD is a starting figure you set first and then explain. The MTPD comes out of the impacts. It is "how long an activity can be down before the impact is unacceptable" (`units/glossary.md`, MTPD), so you can't say when the impact turns unacceptable until you've described how it grows over time. The analysis unit makes the same point: the requirements are covered "once the impacts and the MTPD are settled" (`units/stages/analysis.md`, Method). Dependencies come last, after the resource requirements.

---

**Question 2 of 4.** A colleague says: "Our BIA lists a backup data centre, so we have one." What does a BIA requirement actually tell you? Answer in your own words.

## Turn 5

**Request:** skip

**Reply (verbatim):**

Skipped. Here's the answer for reference:

**A BIA requirement tells you what the activity needs in order to run. It does not tell you what the organisation has today.** "A requirement names what an activity needs to run; it does not assert that the thing exists today" (`units/workflow-design.md`, The BIA workflow, five stages). The analysis unit says the same: a requirement "states nothing about what the organisation has today" (`units/stages/analysis.md`, Method).

So the colleague's reasoning doesn't hold. A backup data centre in the BIA shows that the activity needs one. Whether one exists is a separate question.

---

**Question 3 of 4.** Name the four classes of resource requirement a BIA covers. Order isn't scored this time.

## Turn 6

**Request:** People, seats and buildings, IT and applications, and suppliers and other third parties.

**Reply (verbatim):**

**Correct, all four.** The source adds detail to two of them (`units/stages/analysis.md`, Method):

- **People** come "with the skills, authorities and mandates the work needs". A name on a list isn't enough; the person also needs the authority to act.
- **IT and applications** come "each with its RTO and its RPO".

Seats and buildings, and suppliers and other third parties, are named without more detail. Dependencies on other departments are a separate item, not a fifth class.

---

**Question 4 of 4.** An AI tool has drafted a BIA for a department and proposed an RTO of 4 hours for its billing application. Who sets the RTO?

- A) The AI tool, if its proposal fits the impact criteria
- B) The BC manager, after reviewing the draft BIA
- C) Top management, when it approves the BIA results
- D) The activity owner, who also approves the data

## Turn 7

**Request:** D

**Reply (verbatim):**

**Correct.** The activity owner "approves the data and sets MTPD and RTO" (`units/workflow-design.md`, The BIA workflow, five stages). Why the other options are wrong:

- **A:** "AI can test whether a proposed RTO fits the impact criteria. It does not set the RTO" (`units/stages/analysis.md`, Minimum controls).
- **B:** the BC manager checks each stage's result against its gate, but the sources don't give them the job of setting recovery times.
- **C:** top management approves the BIA results "before solutions design starts". It approves the results; it doesn't set each RTO (`units/workflow-design.md`).

---

## Self-test results

| # | Topic | Result |
|---|---|---|
| 1 | Order of the interview | Wrong: the MTPD comes from the impacts, so impacts come first |
| 2 | What a requirement says | Skipped: a requirement is what the activity needs, not what exists |
| 3 | Four classes of resource requirement | Correct |
| 4 | Who sets the RTO | Correct |

You got two right, one wrong and skipped one. Questions 1 and 2 are worth reviewing. Both are in `units/workflow-design.md`, The BIA workflow, five stages.

---

## Where your organisation decides

These questions go to your BC manager. The sources don't answer them for your organisation, so they're left open here:

1. What are your organisation's impact categories, time horizons and thresholds? The sources say only that they are "agreed and supplied before stage 1 runs" (`units/workflow-design.md`).
2. Which BIA template or form does your organisation use, and how do its fields map onto the four classes and the dependencies?
3. Who counts as the "activity owner" for each activity in your organisation, and who in top management approves the BIA results?
4. Are there regulations that shape your BIA, and if so which ones? For example, the DORA delegated regulation 2024/1774 refers to the BIA in its Articles 25 and 26, but whether it applies to you is a question for your organisation.

If you'd like a next session, natural follow-ups would be "how MTPD, RTO and RPO relate" (NIST SP 800-34r1, §3.2.1) or "the five stages of the BIA workflow" (`units/workflow-design.md`).

## Turn 8

**Request:** What does ISO 22301 say about the BIA, word for word?

**Reply (verbatim):**

I can't give you that. The ISO 22301 text isn't among the sources that ship with this skill, so the answer is **"not in the sources"**. I won't reconstruct it from memory either, because this skill teaches only from its sources and quoting a standard from memory risks wording that isn't really in it.

Here is what is possible:

- **The closest thing the sources hold** is the glossary's RTO definition, which it attributes to ISO 22301:2019 (`units/glossary.md`, RTO). The lesson quoted that one line. Nothing else in the sources says what ISO 22301 says about the BIA.
- **If you have a licensed copy**, you can attach it and confirm that your licence covers this use. I could then point you to the relevant clause numbers. I still wouldn't reproduce the standard's text in the chat; you'd read the wording in your own copy.
- **For open text on the BIA you can read in full**, NIST SP 800-34r1 §3.2 is the one I named for reading next, and it's public domain.

Whether your organisation holds an ISO 22301 licence, and who may use it, is a question for your BC manager.

## Turn 9

**Request:** Should our payroll count as a critical activity in our BIA?

**Reply (verbatim):**

I can't answer that. Whether payroll is critical is a decision for your organisation, and none of the sources settle it. It goes under **Where your organisation decides**, for your BC manager:

5. Should payroll count as a critical activity in our BIA?

The sources do say how such a question gets settled, which may help when you raise it:

- **It depends on agreed criteria, not opinion.** Impact categories, time horizons and thresholds "are agreed and supplied before stage 1 runs, and no stage of the workflow sets them" (`units/workflow-design.md`, The BIA workflow, five stages). Whether payroll is critical comes from measuring its impacts against those criteria.
- **The evidence comes from the interview.** The interview starts with "impacts over time" and then the MTPD (`units/workflow-design.md`). How quickly a payroll disruption becomes unacceptable is what the payroll owner would describe there.
- **Named people decide, not a tool or a lesson.** The activity owner "approves the data and sets MTPD and RTO", and top management "approves the BIA results" (`units/workflow-design.md`).

A good way to take it to your BC manager: "What are our impact criteria, and has payroll been assessed against them?"
