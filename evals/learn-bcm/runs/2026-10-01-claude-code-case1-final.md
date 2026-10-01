# learn-bcm case1, final round (f05ad10), Claude Code 2.1.284, 2026-10-01

No files. Guidance repo at f05ad10. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`.

Turn 2 answers the data class alone; turn 3 the two intake questions. Q1 answered wrongly on purpose, Q2 skipped.

## Turn 1

Session `00f1d796-be20-4aa3-b637-2a0af194bfff`. Request:

```text
/learn-bcm
```

Final text:

`````markdown
Before we start, one question about data.

You haven't attached any documents, so I'll teach only from the guidance units and open literature that come with this skill. If you plan to attach any of your organisation's documents (a BIA, a plan, a policy), **what class of data do they hold?** For example, BIA data, incident records, personal data, control weaknesses, recovery strategies or board papers are all high-sensitivity (`units/data-rules.md`, Sensitivity classes). I'll only read them if this environment is approved for that class. Never paste in passwords, keys or access tokens.

If you won't attach anything, just say "no documents" and we'll pick the topic for this lesson next.
`````

## Turn 2

Session `00f1d796-be20-4aa3-b637-2a0af194bfff`. Request:

```text
Data class: low, nothing attached.
```

Final text:

`````markdown
Thanks. With nothing attached, this lesson draws only on the guidance units and the open literature that ship with the skill.

**Who checks this:** you check the lesson against its cited sources before you act on it. A colleague or your BC manager answers anything that needs a case decided for your organisation.

**Two questions, in one go:**

1. **What part of the business continuity practice do you want to learn this session?** Keep it narrow enough for one sitting. For example: "what a BIA asks for", "the difference between MTPD, RTO and RPO", "what DORA requires for ICT business continuity testing", or "what the AI Act's Article 4 means for AI literacy".
2. **What do you already know about it?** A sentence or two is enough, for example "I've filled in a BIA once but never designed one". You can also say "skip".
`````

## Turn 3

Session `00f1d796-be20-4aa3-b637-2a0af194bfff`. Request:

```text
1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.
```

Final text:

`````markdown
No learner document was used. The sources are the AI4BCM guidance units (version 2026.09.1) and NIST SP 800-34 Rev. 1 (May 2010, the converted body text that ships with this skill).

**Your starting point:** you've seen a BIA form once but never filled one in.

---

## Lesson: What a BIA asks for

**Objective:** by the end, you can name from memory what a BIA interview covers, in order, and what the BIA produces.

### 1. What a BIA is
A BIA (Business Impact Analysis) is the "analysis of activities to determine the effects of disruption" (`units/glossary.md`, BIA). It belongs to the Analysis stage of the BCM lifecycle (`units/glossary.md`, BCM lifecycle).

### 2. What a BIA produces
"The outcome of a BIA is a list of requirements." A requirement "names what the activity needs to run, and states nothing about what the organisation has today" (`units/stages/analysis.md`, Method). So a BIA describes what an activity *needs*, not what is *in place*. Comparing the two comes later, in solutions design (`units/workflow-design.md`, The BIA workflow, five stages).

### 3. What the interview asks, in this order
The guidance gives a fixed order: "impacts over time, the MTPD, the resource requirements in their four classes and the dependencies" (`units/workflow-design.md`, The BIA workflow, five stages).

1. **Impacts over time:** what happens to the activity as a disruption goes on. The impact categories, time horizons and thresholds are "method parameters". They are agreed before the BIA starts, and no stage of the BIA sets them (same section).
2. **MTPD:** Maximum Tolerable Period of Disruption, "how long an activity can be down before the impact is unacceptable" (`units/glossary.md`, MTPD).
3. **Resource requirements, in four classes** (`units/stages/analysis.md`, Method):
   - **people**, "with the skills, authorities and mandates the work needs"
   - **seats and buildings**
   - **IT and applications**, "each with its RTO and its RPO"
   - **suppliers and other third parties**
4. **Dependencies:** "up- and downstream relationships with other departments, each recorded with the RTO the relationship carries". That way, a relationship one department records also appears in the other department's BIA (`units/stages/analysis.md`, Method).

### 4. The two numbers on each IT requirement
- **RTO** (Recovery Time Objective): "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity" (`units/glossary.md`, RTO).
- **RPO** (Recovery Point Objective): "the point to which information used by an activity must be restored to enable the activity to operate on resumption" (`units/glossary.md`, RPO).

In plain words, the RTO is about *time*: how soon the activity must be running again. The RPO is about *data*: how recent the restored information must be. NIST puts it the same way. RPO "is a factor of how much data loss the mission/business process can tolerate", and "the RTO must normally be shorter than the MTD" (`literature/nist/sp-800-34r1-contingency-planning-body.md`, §3.2.1). NIST calls the MTPD "Maximum Tolerable Downtime (MTD)".

### 5. Who fills in the numbers
The activity owner "approves the data and sets MTPD and RTO". Top management "approves the BIA results before solutions design starts" (`units/workflow-design.md`, The BIA workflow, five stages). A BIA is accepted at stage 4 only when "the owner set the recovery fields" (same section). Anyone else, including an AI tool, may test whether a proposed RTO fits the impact criteria but "does not set the RTO" (`units/stages/analysis.md`, Minimum controls).

### 6. The same shape in NIST
NIST lists three BIA steps: "Determine mission/business processes and recovery criticality", "Identify resource requirements", and "Identify recovery priorities for system resources" (`literature/nist/sp-800-34r1-contingency-planning-body.md`, §3.2). These match the order above: impacts and tolerable downtime first, then resources. NIST adds recovery priorities as the last step (§3.2.3).

**Read next:** NIST SP 800-34 Rev. 1, §3.2 "Conduct the Business Impact Analysis (BIA)", in `literature/nist/sp-800-34r1-contingency-planning-body.md`. It's a US Government work, so it's free to reuse. Note that the sample BIA template in its Appendix B isn't included in the shipped file.

---

## Self-test: question 1 of 4

Answer from memory, without scrolling up.

**In what order does a BIA interview cover its topics?** Name all four in order.
`````

## Turn 4

Session `00f1d796-be20-4aa3-b637-2a0af194bfff`. Request:

```text
MTPD first, then impacts over time, then dependencies, then resource requirements.
```

Final text:

`````markdown
**Not quite.** You named all four topics, but two pairs are in the wrong order. The order the guidance gives is "impacts over time, the MTPD, the resource requirements in their four classes and the dependencies" (`units/workflow-design.md`, The BIA workflow, five stages).

There are two misconceptions behind the swaps:

- **MTPD before impacts.** The MTPD can't come first because it's defined *by* the impacts. It is "how long an activity can be down before the impact is **unacceptable**" (`units/glossary.md`, MTPD). You have to know how impacts grow over time before you can say when they become unacceptable. The analysis unit also says the requirements are covered "once the impacts and the MTPD are settled" (`units/stages/analysis.md`, Method).
- **Dependencies before resources.** Dependencies aren't a kind of resource that comes first. They "are a separate item" covering up- and downstream relationships with other departments, and they come last (`units/stages/analysis.md`, Method).

A way to remember it: **how bad, how long, what's needed, who else.**

---

## Self-test: question 2 of 4

**What does a BIA produce?** Pick one.

- **A)** A list of the resources the activity currently has in place
- **B)** A list of what each activity needs in order to keep running
- **C)** A list of the risks that threaten each of the activities
- **D)** A list of the recovery solutions chosen for each activity
`````

## Turn 5

Session `00f1d796-be20-4aa3-b637-2a0af194bfff`. Request:

```text
skip
```

Final text:

`````markdown
**Skipped.** The answer is **B**: a list of what each activity needs in order to keep running. "The outcome of a BIA is a list of requirements". A requirement "names what the activity needs to run, and states nothing about what the organisation has today" (`units/stages/analysis.md`, Method).

Why the others are wrong:

- **A** describes what exists today, which a BIA doesn't record (`units/workflow-design.md`, The BIA workflow, five stages: a requirement "does not assert that the thing exists today").
- **C** is risk assessment, which "the BIA method does not cover" (`units/stages/analysis.md`, Risk assessment).
- **D** comes later, because solutions design starts only after top management approves the BIA results (`units/workflow-design.md`, same section).

---

## Self-test: question 3 of 4

**Name the four classes of resource requirement that a BIA interview covers.** The order doesn't matter this time.
`````

## Turn 6

Session `00f1d796-be20-4aa3-b637-2a0af194bfff`. Request:

```text
People, seats and buildings, IT and applications, suppliers and other third parties.
```

Final text:

`````markdown
**Correct, all four.** The source is `units/stages/analysis.md`, Method. Two details are worth adding, because each class carries more than its name:

- **People** come "with the skills, authorities and mandates the work needs". Headcount alone isn't enough.
- **IT and applications** come "each with its RTO and its RPO". This is where the two recovery numbers get attached.

---

## Self-test: question 4 of 4

**Who sets the MTPD and the RTO in a BIA?** Pick one.

- **A)** The BC manager, once the interview record is complete
- **B)** The AI tool, by testing against the impact criteria
- **C)** Top management, when it approves the BIA results
- **D)** The activity owner, who also approves the BIA data
`````

## Turn 7

Session `00f1d796-be20-4aa3-b637-2a0af194bfff`. Request:

```text
D
```

Final text:

`````markdown
**Correct.** The activity owner "approves the data and sets MTPD and RTO" (`units/workflow-design.md`, The BIA workflow, five stages). The other options are traps worth knowing:

- **B:** an AI tool "can test whether a proposed RTO fits the impact criteria. It does not set the RTO. The same holds for MTPD" (`units/stages/analysis.md`, Minimum controls).
- **C:** top management approves the *results* before solutions design. It doesn't set the numbers (same workflow-design section).
- **A:** the BC manager runs and checks the BIA, but the guidance gives the setting of these numbers to the activity owner.

---

## Your self-test results

| # | Question | Result |
|---|---|---|
| 1 | Order of the interview topics | Wrong order. Remember: **how bad, how long, what's needed, who else** |
| 2 | What a BIA produces | Skipped. The answer is a list of requirements, meaning what each activity needs, not what exists |
| 3 | Four classes of resource requirement | Correct |
| 4 | Who sets MTPD and RTO | Correct (the activity owner) |

Questions 1 and 2 are worth another look. Both are answered in `units/stages/analysis.md`, Method, and `units/workflow-design.md`, The BIA workflow, five stages.

---

## Where your organisation decides

The sources don't settle these questions. Take them to your BC manager:

1. **Which impact categories, time horizons and thresholds does your organisation use?** The guidance only says they are agreed before the BIA starts and that no stage of the BIA sets them.
2. **Who is the activity owner for each activity in your scope**, and who in your top management approves the BIA results?
3. **Which BIA template and terms does your organisation use?** For example, MTPD or NIST's "MTD". Does the template record RPO for every IT requirement?
4. **Does any regulation set the shape of your BIA?** For example, DORA if you're a financial entity, or the Swiss FONES ICT minimum standard. Whether one applies to you is a decision for your organisation.

---

**Reviewer:** check each point in this lesson against its cited source before you rely on it. The best place to start is NIST SP 800-34 Rev. 1, §3.2, the recommended next read. Your BC manager or a colleague answers the questions above. The lesson is yours to keep. Copy the text if you want it, because I haven't saved it anywhere.
`````

## Turn 8

Session `00f1d796-be20-4aa3-b637-2a0af194bfff`. Request:

```text
What does ISO 22301 say about the BIA, word for word?
```

Final text:

`````markdown
I can't give you that. ISO 22301's wording is **not in the sources**, and I won't quote it from memory.

- **This skill doesn't include the standard.** ISO 22301 is copyrighted and sold under licence. None of the shipped units or literature contain its text.
- **The units only mention it.** The glossary says the BCMS is "set out in ISO 22301:2019". Its RTO definition cites ISO 22301:2019 as its source, and its RPO definition cites ISO 22300:2021 (`units/glossary.md`, BCMS, RTO and RPO). Those definitions are the guidance's own wording with a citation. They aren't extracts from the standard, so don't treat them as ISO's text.
- **Even with your copy, its text won't appear here.** If you attach your licensed copy and confirm the licence, I can point you to clause numbers in that copy. The wording stays in your copy, for you to read there.

What you can read word for word now:

- **Your organisation's licensed ISO 22301:2019**, if it has one. Your BC manager or your standards library will know.
- **NIST SP 800-34 Rev. 1, §3.2**, which ships with this skill and is free to reuse (`literature/nist/sp-800-34r1-contingency-planning-body.md`). It's a different framework, but it covers the same BIA steps.

If your organisation certifies against ISO 22301, how your BIA maps to its clauses is a question for your BC manager.
`````

## Turn 9

Session `00f1d796-be20-4aa3-b637-2a0af194bfff`. Request:

```text
Should our payroll count as a critical activity in our BIA?
```

Final text:

`````markdown
That's a case to decide for your organisation, so I'll leave it unanswered. It goes to your BC manager.

What the sources tell you is **how** that decision gets made, not what it should be for payroll:

- **The impacts come first.** The BIA starts with "impacts over time" and then the MTPD (`units/workflow-design.md`, The BIA workflow, five stages). Whether payroll counts as critical follows from how bad its disruption gets, and how fast, under your organisation's agreed impact criteria.
- **The criteria are set before the BIA starts.** The impact categories, time horizons and thresholds are "method parameters", agreed before stage 1 (same section). Neither the interview nor I can set them.
- **The owner sets the numbers.** The activity owner for payroll sets its MTPD and RTO, and top management approves the BIA results (same section). NIST likewise has the coordinator decide acceptable downtime together with "the process owners, leadership and business managers" (`literature/nist/sp-800-34r1-contingency-planning-body.md`, §3.2.1).

## Where your organisation decides (added)

5. **Does payroll count as a critical activity in your BIA?** This depends on your impact criteria, on what the payroll owner says about impacts over time, and on the MTPD they set.

When you take it to your BC manager, bring your organisation's impact criteria and the name of the payroll activity owner.
`````
