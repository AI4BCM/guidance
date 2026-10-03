# /learn-bcm case 1, run3: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `fb631a7e-2c74-4c16-897a-e227b8b7e339`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /learn-bcm

**Reply (verbatim):**

Before we start: what class of data will the material you bring to this session hold — for example public, internal, confidential or restricted (as your organisation labels it)? If you don't plan to attach any documents of your own, just say "none", and we'll work only from this guidance's units and the open literature that ship with it.

I won't open any attached file until you've answered.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/preflight.md`

## Turn 2

**Request:** low

**Reply (verbatim):**

Thanks — I'll treat your material as **low sensitivity**. That's fine for this environment. The high-sensitivity list in `units/data-rules.md` (Sensitivity classes), which covers things like BIA data, incident records, personal data and recovery strategies, is for an "approved corporate or private environment only". If anything you attach later falls into one of those categories, tell me before you share it.

Now, which part of BCM would you like to learn, and what do you already know about it? A term (e.g. MTPD, RTO, RPO), a structure (e.g. the BIA, the BC policy, the exercise programme) or an expected output are all fine. One sitting covers one part.

If you'd rather skip this, say "skip". I'll note that and start from the beginning of the glossary.

**Tool calls (stream-json):**

- Grep: `Sensitivity classes`

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

I've read the guidance units and the open NIST text on BIAs, and the lesson is below.

---

## Lesson: what a BIA asks for

**Sources** (all shipped with this skill; you attached no documents)
- `units/glossary.md`, version 2026.11
- `units/stages/analysis.md`, version 2026.11
- `units/workflow-design.md`, version 2026.11
- `units/prompts/bia.md`, version 2026.11, dated 2026-09
- NIST SP 800-34 Rev. 1, chapters 1–5 (open literature, shelf 2)

**Objective:** by the end, you can name what a BIA form asks for, in the order the interview asks it, and who fills in the numbers.

### 1. What a BIA is
A BIA is "analysis of activities to determine the effects of disruption" (`glossary.md`, BIA).

### 2. What it asks for, in order
The interview covers "impacts over time, the MTPD, the resource requirements in their four classes and the dependencies" (`workflow-design.md`, The BIA workflow, five stages).

1. **Impacts over time.** These are the effects of disruption as time passes. The scales are fixed before the interview: "Impact categories, time horizons and thresholds are method parameters. They are agreed and supplied before stage 1 runs" (same section). On a form, these are the columns that are already printed on it.
2. **MTPD.** This is "how long an activity can be down before the impact is unacceptable" (`glossary.md`, MTPD).
3. **Resource requirements, in four classes** (`analysis.md`, Method):
   - "people, with the skills, authorities and mandates the work needs"
   - "seats and buildings"
   - "IT and applications, each with its RTO and its RPO"
   - "suppliers and other third parties"
4. **Dependencies.** These are "up- and downstream relationships with other departments, each recorded with the RTO the relationship carries", so that "a relationship one department records appears in the other department's BIA" (`analysis.md`, Method).

### 3. The numbers on the form
- **RTO** is "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity" (`glossary.md`, RTO, citing ISO 22301:2019). So the RTO falls inside the MTPD.
- **RPO** is "the point to which information and data used by an activity is restored to enable the activity to operate on resumption" (`glossary.md`, RPO, citing ISO 22300:2025).
- **Who sets them:** "the activity owner, who approves the data and sets MTPD and RTO", and "top management, which approves the BIA results before solutions design starts" (`workflow-design.md`, five stages). Whoever runs the interview doesn't set the numbers. Nor does an AI: "Recovery fields stay empty in anything AI produces" (`analysis.md`, Minimum controls).

### 4. Where the form goes next
The workflow runs in five stages: scope, structured interview, conversion to the "standardised template", listing the requirements, and consolidation and handover (`workflow-design.md`). So the form you saw is most likely the stage 3 template, filled in from an interview record.

### Gaps
- What ISO 22301 itself requires of a BIA is **not in the sources**. The standard's text doesn't ship with this skill (`literature/README.md`, Licences), so I quote no clause.
- No instructions aimed at an AI were found in the material used.

### Read next
**NIST SP 800-34 Rev. 1, section 3.2 "Conduct the Business Impact Analysis (BIA)"**, especially 3.2.1. It's an open text, and it describes the same ideas from an IT-system angle. Note that it uses the term "Maximum Tolerable Downtime (MTD)" where this guidance says MTPD.

### Where your organisation decides
None so far.

---

## Self-test: question 1 of 4

Answer from memory, without scrolling up:

**Name the four classes of resource requirement that a BIA interview covers.**

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm; ls -R units literature | head -50; grep -n -i "BIA\|business impact" units/glossary.md | head -40`
- Glob: `**/*.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/glossary.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/literature/README.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/stages/analysis.md`
- Grep: `Business Impact Analysis|BIA`
- Grep: `Onboarding`
- Grep: `Business Impact Analysis|BIA|^#`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/prompts/bia.md`
- Grep: `BIA|interview|template|stage`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/workflow-design.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md`

## Turn 4

**Request:** People, with their skills and mandates; seats and buildings; IT and applications, each with its RTO and RPO; suppliers and other third parties.

**Reply (verbatim):**

**Correct.** That matches `analysis.md` (Method) almost word for word: "people, with the skills, authorities and mandates the work needs; then seats and buildings; then IT and applications, each with its RTO and its RPO; then suppliers and other third parties."

You left out one word, **authorities**. The people class also covers what people are authorised to do, not just their skills and mandates. In a real BIA, that's where you'd record someone like a payment signatory.

---

## Question 2 of 4

**In what order does the BIA interview cover its topics?**

A. Resource requirements → dependencies → impacts over time → MTPD
B. Impacts over time → MTPD → resource requirements → dependencies
C. MTPD → impacts over time → dependencies → resource requirements
D. Dependencies → resource requirements → MTPD → impacts over time

Answer with a letter.

**Tool calls (stream-json):**

- none

## Turn 5

**Request:** A

**Reply (verbatim):**

**Not quite. The answer is B:** impacts over time → MTPD → resource requirements → dependencies (`workflow-design.md`, The BIA workflow, five stages).

**The misconception:** treating a BIA as an inventory that starts by listing what the activity uses. A BIA starts from **consequences** instead. `analysis.md` (Method) sets the order: "Once the impacts and the MTPD are settled, the interview covers people…" and then the other classes. The reasoning is that the MTPD comes from how impacts grow over time ("how long an activity can be down before the impact is unacceptable", `glossary.md`). Resources are then recorded with recovery times that have to fit inside that limit. If you start with resources, you have no time limit to measure them against.

---

## Question 3 of 4

**Who sets the MTPD and the RTO for an activity?**

A. The BCM practitioner who runs the interview
B. Top management, when it approves the BIA report
C. The activity owner
D. The IT department, based on what its systems can recover

Answer with a letter.

**Tool calls (stream-json):**

- none

## Turn 6

**Request:** skip

**Reply (verbatim):**

**Skipped, recorded as skipped.**

For reference, the answer is **C, the activity owner**. The source is `workflow-design.md` (five stages): "the activity owner, who approves the data and sets MTPD and RTO". Top management (B) comes in afterwards and "approves the BIA results before solutions design starts". That's an approval of the whole result, not setting the individual numbers. The interviewer (A) records what the owner says. IT (D) appears nowhere in the sources as the one who sets these numbers.

---

## Question 4 of 4

**How does the RTO relate to the MTPD?**

A. The RTO lies within the MTPD
B. The RTO is always exactly half the MTPD
C. The RTO lies beyond the MTPD, as a safety margin
D. The two are unrelated; one is for IT and one is for the business

Answer with a letter.

**Tool calls (stream-json):**

- none

## Turn 7

**Request:** A

**Reply (verbatim):**

**Correct.** The RTO is "the time frame **within the MTPD** for resuming disrupted activities at a specified minimum acceptable capacity" (`glossary.md`, RTO, citing ISO 22301:2019). The open NIST text says the same in its own terms: "the RTO must normally be shorter than the MTD" (NIST SP 800-34 Rev. 1, section 3.2.1).

---

## Your results

| # | Question | Result |
|---|---|---|
| 1 | Four classes of resource requirement | Correct (you left out "authorities" in the people class) |
| 2 | Order of the interview | Wrong: you started from resources, but a BIA starts from impacts |
| 3 | Who sets the MTPD and RTO | Skipped (answer: the activity owner) |
| 4 | RTO vs. MTPD | Correct |

**Worth going over again:** the order of the interview, and who owns the numbers. Both come down to the same idea: a BIA starts from the effects of disruption, and the activity owner decides what is tolerable.

**Read next:** NIST SP 800-34 Rev. 1, **section 3.2** (especially 3.2.1 on MTD, RTO and RPO).

**Check before you rely on this:** compare the lesson against the cited sections yourself, or ask a colleague to. Your organisation's own BIA template may use different terms or a different order. If it does, your BC manager can tell you which one applies.

**Where your organisation decides:** none.

**Tool calls (stream-json):**

- none

## Turn 8

**Request:** Is our payroll a critical activity?

**Reply (verbatim):**

I can't answer that one. Whether payroll counts as critical in your organisation is a decision about your own case, not something the sources can settle. I've added it below for your BC manager.

What the sources do say is **how** that question gets answered:

- It comes out of the BIA, by assessing "impacts over time" against your organisation's impact categories, time horizons and thresholds. These "are agreed and supplied before stage 1 runs, and no stage of the workflow sets them" (`workflow-design.md`, five stages).
- The activity owner, here whoever owns payroll, "approves the data and sets MTPD and RTO", and top management "approves the BIA results" (same section).
- Your organisation's impact criteria and payroll's BIA record are **not in the sources**.

So the people to ask are the payroll activity owner and your BC manager. The record to look at is payroll's approved BIA entry, if there is one.

**Where your organisation decides**
- Is payroll a critical activity in our organisation? *(For your BC manager. It depends on our impact criteria and the payroll owner's BIA input.)*

**Tool calls (stream-json):**

- none
