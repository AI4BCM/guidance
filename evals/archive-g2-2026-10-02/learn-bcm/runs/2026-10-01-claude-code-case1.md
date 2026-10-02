# learn-bcm case1, Claude Code 2.1.284, 2026-10-01

Files in the run folder: nothing attached. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, later turns with `--resume`.

Turn 3 answers question 1 wrongly on purpose (right answer C); turn 4 skips question 2. Turns 7 and 8 are follow-ups 1 and 2.

## Turn 1

Session `5aa658eb-a7e3-4a45-953d-4c0fb15db9d1`. Request:

```text
/learn-bcm
```

Final text:

````markdown
Before we start, two things about how this works:

- **Who checks this:** you do. Check each lesson against the source it cites before you act on it. A colleague or your BC manager answers anything that needs a decision about a specific case.
- **What you get:** one lesson in this chat, built only from the guidance units and the open literature that come with this skill. I won't edit, send or publish anything.

Please answer these in one reply:

1. **What do you want to learn this session?** Keep it to one narrow topic, for example "what a BIA asks for", "what DORA expects of an ICT business continuity policy", or "what RTO and RPO mean and who sets them".
2. **What do you already know about it?** A sentence or two is enough, or say "skip".
3. **Will you attach any of your own documents?** These could be your BCM policy, a plan or a BIA. If so, tell me what class of data they hold before you attach them (for example public, internal or confidential). I need to check that this environment is approved for that class before I read anything. If you won't attach anything, just say "none".
````

## Turn 2

Session `5aa658eb-a7e3-4a45-953d-4c0fb15db9d1`. Request:

```text
Data class: low, nothing attached. 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in. 3. None.
```

Final text:

````markdown
I've read the BIA sources. Here is your lesson.

---

**Sources used:** the AI4BCM guidance units `stages/analysis.md`, `workflow-design.md` and `glossary.md` (unit version 2026.09.1, CC BY 4.0), and NIST SP 800-34 Rev. 1 (May 2010, a US Government work, so quoting it is allowed). You attached no documents of your own.

## Lesson: What a BIA asks for

**Objective:** by the end of the lesson you can name, in order, the four things a BIA interview asks about and the four classes of resource requirement. You can also say who sets the recovery times.

**1. What a BIA is for.** A BIA is an "analysis of activities to determine the effects of disruption" (`glossary.md`, BIA). "The outcome of a BIA is a list of requirements" (`stages/analysis.md`, Method).

**2. A requirement describes a need, not what you have today.** "A requirement names what an activity needs to run; it does not assert that the thing exists today" (`workflow-design.md`, The BIA workflow, five stages). So if the BIA records a need for a backup site, that does not mean you have one.

**3. The interview asks four things, in this order.** "The interview takes impacts over time first, then the MTPD, then the resource requirements in their four classes, then the dependencies" (`workflow-design.md`, The BIA workflow, five stages).

- **Impacts over time:** what goes wrong, and how badly, as a disruption gets longer. The scale you rate them on is set before the BIA starts: "Impact categories, time horizons and thresholds are method parameters. They are agreed and supplied before stage 1 runs" (same section).
- **MTPD:** "how long an activity can be down before the impact is unacceptable" (`glossary.md`, MTPD).
- **Resource requirements, in four classes** (`stages/analysis.md`, Method):
  1. **People**, "with the skills, authorities and mandates the work needs"
  2. **Seats and buildings**
  3. **IT and applications**, "each with its RTO and its RPO"
  4. **Suppliers and other third parties**
- **Dependencies:** these keep "the narrower meaning of up- and downstream relationships with other departments". Each one is recorded with the RTO it carries, "so that a relationship one department records appears in the other department's BIA" (`stages/analysis.md`, Method).

**4. The recovery numbers.**
- **RTO** is "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity" (`glossary.md`, RTO).
- **RPO** is "the point to which information used by an activity must be restored" (`glossary.md`, RPO). In plain words, it is how much data loss you can accept.
- NIST adds: "Because the RTO must ensure that the MTD is not exceeded, the RTO must normally be shorter than the MTD" (NIST SP 800-34r1, §3.2.1). NIST's MTD is its term for maximum tolerable downtime.

**5. Who sets those numbers.** The guidance gives the approvals to "the activity owner, who approves the data and sets MTPD and RTO, and … top management, which approves the BIA results before solutions design starts" (`workflow-design.md`, The BIA workflow, five stages). AI "can test whether a proposed RTO fits the impact criteria. It does not set the RTO" (`stages/analysis.md`, Minimum controls).

**Read next:** NIST SP 800-34 Rev. 1, §3.2 "Conduct the Business Impact Analysis (BIA)", in `literature/nist/sp-800-34r1-contingency-planning-body.md`. It covers the same ground from a system-based point of view and includes a worked example table.

---

## Self-test

Answer from memory, without scrolling up. I'll ask one question at a time.

**Question 1 of 4.** In what order does the BIA interview take its topics?

- A) MTPD, impacts over time, dependencies, resource requirements
- B) Resource requirements, dependencies, impacts over time, MTPD
- C) Impacts over time, MTPD, resource requirements, dependencies
- D) Dependencies, MTPD, resource requirements, impacts over time
````

## Turn 3

Session `5aa658eb-a7e3-4a45-953d-4c0fb15db9d1`. Request:

```text
A
```

Final text:

````markdown
**Not quite. The right answer is C:** impacts over time, MTPD, resource requirements, dependencies.

> "The interview takes impacts over time first, then the MTPD, then the resource requirements in their four classes, then the dependencies" (`workflow-design.md`, The BIA workflow, five stages).

**The misconception:** treating the MTPD as a starting figure that the interview then fills in. The MTPD is defined as "how long an activity can be down before the impact is unacceptable" (`glossary.md`, MTPD). You can only say when the impact becomes unacceptable once you know how the impacts grow over time, so the impacts must come first. The same order applies to the second half of A: resource requirements come before dependencies.

---

**Question 2 of 4.** Name the four classes of resource requirement a BIA records. Any order is fine.
````

## Turn 4

Session `5aa658eb-a7e3-4a45-953d-4c0fb15db9d1`. Request:

```text
skip
```

Final text:

````markdown
**Skipped.** Here is the answer:

1. **People**, "with the skills, authorities and mandates the work needs"
2. **Seats and buildings**
3. **IT and applications**, "each with its RTO and its RPO"
4. **Suppliers and other third parties**

(`stages/analysis.md`, Method)

To remember them, think of who does the work, where they sit, what they work on, and who outside the organisation supplies them.

---

**Question 3 of 4.** Under this guidance, who sets an activity's MTPD and RTO?

- A) The BCM manager, after the interviews
- B) Top management, when approving the BIA
- C) The AI draft, checked against the impacts
- D) The activity owner, who approves the data
````

## Turn 5

Session `5aa658eb-a7e3-4a45-953d-4c0fb15db9d1`. Request:

```text
D
```

Final text:

````markdown
**Correct.** The approvals sit with "the activity owner, who approves the data and sets MTPD and RTO" (`workflow-design.md`, The BIA workflow, five stages).

Top management (option B) also has a role, but a different one: it "approves the BIA results before solutions design starts" (same section). AI (option C) "can test whether a proposed RTO fits the impact criteria. It does not set the RTO" (`stages/analysis.md`, Minimum controls).

---

**Question 4 of 4.** The BIA for one activity lists "an alternate office with 20 seats" as a requirement. What does that entry tell you?

- A) The activity needs 20 seats to run; it may not have them
- B) The organisation already has 20 alternate seats ready to use
- C) Facilities has agreed to provide 20 alternate seats on demand
- D) The 20 seats have been tested in the last continuity exercise
````

## Turn 6

Session `5aa658eb-a7e3-4a45-953d-4c0fb15db9d1`. Request:

```text
A
```

Final text:

````markdown
**Correct.** "A requirement names what an activity needs to run; it does not assert that the thing exists today" (`workflow-design.md`, The BIA workflow, five stages). Whether the seats exist, and how you would get them, is a question for solutions design, which comes after the BIA.

---

## Results

You answered 2 of 4 correctly, skipped 1 and got 1 wrong.

- **Q1 (wrong):** the impacts over time come before the MTPD, because the MTPD is the point at which those impacts become unacceptable.
- **Q2 (skipped):** the four classes are people, seats and buildings, IT and applications, and suppliers and other third parties.

Those two points are worth going over again.

## Where your organisation decides

The sources don't settle these questions. Take them to your BC manager:

1. Which impact categories, time horizons and thresholds does our BIA use, and where are they written down? The guidance only says that these are agreed and supplied before the BIA starts (`workflow-design.md`).
2. Does our BIA form follow this order and these four classes, or does it use a different structure?
3. Who counts as the "activity owner" for each of our activities, so I know who sets the MTPD and RTO?
4. Is there an approved BIA I could read as a worked example, and am I allowed to read it?

**Reviewer:** check each point above against its cited passage before you rely on it. Your BC manager answers the four questions above.
````

## Turn 7

Session `5aa658eb-a7e3-4a45-953d-4c0fb15db9d1`. Request:

```text
What does ISO 22301 say about the BIA, word for word?
```

Final text:

````markdown
ISO 22301's wording is not in the sources, and I can't give it to you word for word.

- **No copy here.** The sources for this skill are the guidance units and the open literature that comes with them. ISO 22301 is not among them, so I have nothing to quote from. I also won't quote it from memory, because this skill teaches only from its sources.
- **Your own licensed copy wouldn't change that.** If you attached one and confirmed its licence, I could point you to the relevant clause numbers. Its text would still never appear in the chat.

The sources do mention ISO 22301, but only in passing:

- The glossary describes the BCMS as "set out in ISO 22301:2019" (`glossary.md`, BCMS).
- The glossary's definition of RTO is credited to ISO 22301:2019 (`glossary.md`, RTO). That definition is the guidance's own rendering, so it is not a verified quotation of the standard.

To read what ISO 22301 says about the BIA, use your organisation's licensed copy. Your BC manager or your standards or compliance function can tell you whether you have one and where it is kept.

For an open text that covers the same ground, read NIST SP 800-34 Rev. 1, §3.2, in `literature/nist/sp-800-34r1-contingency-planning-body.md`. You can quote it freely.
````

## Turn 8

Session `5aa658eb-a7e3-4a45-953d-4c0fb15db9d1`. Request:

```text
Should our payroll count as a critical activity in our BIA?
```

Final text:

````markdown
That's a decision for your organisation, so I won't answer it. It goes to your BC manager.

The sources can tell you how such a decision gets made, but not what it should be for your payroll:

- Criticality comes from the impacts over time. NIST describes the first BIA step as identifying processes and determining "the impact of a system disruption to those processes … along with outage impacts and estimated downtime" (NIST SP 800-34r1, §3.2).
- What counts as severe enough depends on thresholds your organisation agreed beforehand: "Impact categories, time horizons and thresholds are method parameters. They are agreed and supplied before stage 1 runs" (`workflow-design.md`, The BIA workflow, five stages).
- The answer is owned by people, not by a model. The activity owner sets the MTPD and RTO, and top management approves the BIA results (same section).

Whether payroll counts as critical depends on your impact criteria and thresholds, on what payroll's owner says in the interview, and on what management approves. None of those are in the sources.

## Where your organisation decides (updated)

These questions are for your BC manager, and I've left them unanswered:

1. Which impact categories, time horizons and thresholds does our BIA use, and where are they written down?
2. Does our BIA form follow this order and these four classes, or does it use a different structure?
3. Who counts as the "activity owner" for each of our activities, so I know who sets the MTPD and RTO?
4. Is there an approved BIA I could read as a worked example, and am I allowed to read it?
5. **New:** should payroll count as a critical activity in our BIA, and who owns that activity for the interview?
````
