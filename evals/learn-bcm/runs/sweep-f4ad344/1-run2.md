# /learn-bcm case 1, run2: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `12782b30-9987-48cb-9c37-7350221bfa98`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /learn-bcm

**Reply (verbatim):**

Before we start, I need to ask one thing.

**What class of data is in the material you plan to bring to this lesson?** For example:

- **None.** You only want to learn from this guidance's units and the open literature that ships with the skill.
- **Internal, low-sensitivity.** For example, a published policy or a general framework document.
- **High-sensitivity.** For example, BIA data, risk assessment detail, incident records, personal data or contact lists, vulnerabilities, recovery strategies, supplier weaknesses, board papers, or uncleared audit findings. That material may only be used in an approved corporate or private environment, so please also tell me whether this environment is approved for it.

Please don't share any passwords, keys or access tokens. They don't belong in any tool.

Once you've answered, I'll ask which part of BCM you'd like to learn.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/preflight.md`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** low

**Reply (verbatim):**

Thanks. Low-sensitivity material is fine to use here.

**Which part of business continuity management would you like to learn, and what do you already know about it?** For example, you might pick a term like MTPD, RTO or RPO, a structure like the BIA or the BCMS lifecycle, or an expected output like a BC plan or an exercise report. If you have a low-sensitivity document you'd like to use as the worked example, such as a published policy, mention it now, along with its version and date if it has them.

If you'd rather not choose, say "skip" and I'll start from the beginning.

**Tool calls (stream-json):**

- none

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

I've read the guidance's units and the open literature on BIA. Here's your lesson.

**Objective:** by the end of this lesson you can name what a BIA asks for, in the order the interview asks for it, and who supplies each answer.

**Sources used** (no learner document attached):
- AI4BCM guidance, `units/glossary.md`, version 2026.11
- `units/workflow-design.md`, "The BIA workflow, five stages", AI4BCM guidance 2026.11
- `units/stages/analysis.md`, "Method", version 2026.11
- `units/prompts/bia.md`, version 2026.11, dated 2026-09
- NIST SP 800-34 Rev. 1, May 2010, section 3.2 (shipped conversion, retrieved 2026-09-10)

---

## What a BIA asks for

**What a BIA is.** The glossary defines it as "analysis of activities to determine the effects of disruption" (`glossary.md`, BIA). The unit of analysis is an **activity**, not a system or a building.

**The BIA asks four things, in this order.** The guidance gives a fixed order: "impacts over time, the MTPD, the resource requirements in their four classes and the dependencies" (`workflow-design.md`, The BIA workflow).

1. **Impacts over time.** This asks what happens, and how badly, as a disruption runs on. You measure it against **impact categories, time horizons and thresholds**. These are "method parameters" that are "agreed and supplied before stage 1 runs, and no stage of the workflow sets them" (`workflow-design.md`). So the form you once saw probably had a grid of categories against time bands, and you don't invent that grid. It comes to you.
2. **MTPD.** This is "how long an activity can be down before the impact is unacceptable" (`glossary.md`, MTPD). It comes out of step 1: it's the point where the impact over time crosses the threshold.
3. **Resource requirements, in four classes** (`analysis.md`, Method):
   - **people**, "with the skills, authorities and mandates the work needs"
   - **seats and buildings**
   - **IT and applications**, "each with its RTO and its RPO"
   - **suppliers and other third parties**
4. **Dependencies.** These keep "the narrower meaning of up- and downstream relationships with other departments, each recorded with the RTO the relationship carries", so that "a relationship one department records appears in the other department's BIA" (`analysis.md`, Method).

**Two recovery terms you'll meet in the IT row:**
- **RTO:** "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity". This is the guidance's wording, citing ISO 22301:2019 (`glossary.md`, RTO).
- **RPO:** "the point to which information and data used by an activity is restored to enable the activity to operate on resumption". This is the guidance's wording, citing ISO 22300:2025 (`glossary.md`, RPO).

The standards' own clause text is not in the sources. I don't have your licensed copy.

**Who fills in what.** The activity owner "approves the data and sets MTPD and RTO", and top management "approves the BIA results before solutions design starts" (`workflow-design.md`). A drafted requirement "is only a question for the activity owner" (`analysis.md`, Minimum controls). So when you fill in a form, you gather and record the answers. You don't decide them.

**Where the BIA sits.** It's one of five stages: scope, structured interview, conversion to the template, listing the requirements, and consolidation and handover (`workflow-design.md`, table). The form you saw is the stage 3 "standardised template".

**Not in the sources:** what your organisation's form looks like, and which impact categories and thresholds it uses.

---

## Read next

**NIST SP 800-34 Rev. 1, section 3.2, "Conduct the Business Impact Analysis (BIA)"**, especially 3.2.1. It's in the shipped literature as `literature/nist/sp-800-34r1-contingency-planning-body.md`, and the PDF at nvlpubs.nist.gov is the authoritative version. It covers the same ground from the IT-system side. It calls the MTPD "Maximum Tolerable Downtime (MTD)" and explains why "the RTO must normally be shorter than the MTD".

---

## Self-test (question 1 of 4)

Answer from memory, without scrolling up. You can also say "skip".

**Q1. In what order does the BIA interview cover its four topics?**

---

## Where your organisation decides

None yet.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm; find . -type f | sort; wc -l units/glossary.md literature/README.md`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/glossary.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/literature/README.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/stages/analysis.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/prompts/bia.md`
- Grep: `(?i)business impact analysis|^#+ `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `(?i)BIA`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/workflow-design.md`

## Turn 4

**Request:** Impacts over time, then the MTPD, then the resource requirements in their four classes, then the dependencies.

**Reply (verbatim):**

**Correct.** That's the order `workflow-design.md` (The BIA workflow) gives: "impacts over time, the MTPD, the resource requirements in their four classes and the dependencies."

The order matters because each answer builds on the one before. The MTPD comes from where the impacts cross the threshold, and `analysis.md` (Method) starts the resource questions only "once the impacts and the MTPD are settled".

---

## Self-test (question 2 of 4)

**Q2. Which of these is *not* one of the four classes of resource requirements?**

- A) People, with the skills, authorities and mandates the work needs
- B) Dependencies on other departments, up- and downstream
- C) Seats and buildings
- D) Suppliers and other third parties

**Tool calls (stream-json):**

- none

## Turn 5

**Request:** A. People.

**Reply (verbatim):**

**Not quite. The answer is B, dependencies.**

People are the first of the four classes. `analysis.md` (Method) lists them as "people, with the skills, authorities and mandates the work needs; then seats and buildings; then IT and applications … then suppliers and other third parties."

**The likely misconception:** treating "resources" as only things, such as buildings, systems or contracts, so that people seem to belong somewhere else. In a BIA, people are a resource like any other. That includes their mandates: who is *authorised* to do the work, not just who knows how.

**Why dependencies aren't in the list:** they are "a separate item", kept to the narrower meaning of "up- and downstream relationships with other departments" (`analysis.md`, Method). That's also why they come fourth and last in the interview.

---

## Self-test (question 3 of 4)

**Q3. Who sets the MTPD and the RTO for an activity?**

- A) The BCM practitioner who fills in the form
- B) Top management
- C) The activity owner
- D) The IT department, for the IT and applications row

**Tool calls (stream-json):**

- none

## Turn 6

**Request:** skip

**Reply (verbatim):**

**Q3: skipped.**

Here is the answer so you have it. It's **C, the activity owner**, who "approves the data and sets MTPD and RTO" (`workflow-design.md`, The BIA workflow).

The other options each have a different role:
- **A, the practitioner,** gathers and records the answers. A requirement they draft "is only a question for the activity owner" (`analysis.md`, Minimum controls).
- **B, top management,** "approves the BIA results before solutions design starts" (`workflow-design.md`). That means approving the results, not setting each activity's figures.
- **D, the IT department:** in this guidance the IT and applications row carries an RTO and RPO, but the sources don't give IT the decision on them. The owner sets the RTO.

---

## Self-test (question 4 of 4)

**Q4. Impact categories, time horizons and thresholds: where do they come from?**

- A) They are agreed and supplied before the BIA's first stage runs
- B) The activity owner sets them during the interview
- C) The practitioner chooses them when converting the interview to the template
- D) They are set at the consolidation stage, so they fit every department

**Tool calls (stream-json):**

- none

## Turn 7

**Request:** A

**Reply (verbatim):**

**Correct.** Impact categories, time horizons and thresholds are "method parameters. They are agreed and supplied before stage 1 runs, and no stage of the workflow sets them" (`workflow-design.md`, The BIA workflow).

That's why the grid on the form you saw would already have been filled in with categories and time bands before anyone was interviewed. You measure against it; you don't build it during the BIA.

---

## How you did

| Question | Result |
|---|---|
| Q1: the interview order | correct |
| Q2: the four classes | wrong (A); answer B, dependencies are a separate item |
| Q3: who sets MTPD and RTO | skipped; answer C, the activity owner |
| Q4: where the impact criteria come from | correct |

**Worth going over again:** the four classes of resource requirements (people; seats and buildings; IT and applications; suppliers), and who decides what in a BIA.

**Read next:** NIST SP 800-34 Rev. 1, section 3.2.1. It explains the MTD/RTO/RPO relationship from the IT side.

**Before you act on any of this,** check it yourself or with a colleague against the cited sections. That's the control this lesson works under.

## Where your organisation decides

None.

**Tool calls (stream-json):**

- none

## Turn 8

**Request:** Is our payroll a critical activity?

**Reply (verbatim):**

I can't answer that one. Whether your payroll is a critical activity is a decision for your organisation, so I've put it under **Where your organisation decides** for your BC manager.

Here is what the sources say about how that kind of decision gets made, without applying it to your payroll:

- **The term itself.** A definition of "critical activity" is not in the sources. The glossary's RA entry refers to "prioritised activities" (`glossary.md`, RA) but doesn't define them.
- **What a priority rests on.** It rests on impacts over time, measured against impact categories, time horizons and thresholds that are "agreed and supplied before stage 1 runs" (`workflow-design.md`, The BIA workflow). NIST describes the same idea as determining "recovery criticality" from outage impacts and tolerable downtime (NIST SP 800-34 Rev. 1, section 3.2.1).
- **Who decides.** The activity owner "approves the data and sets MTPD and RTO", and top management "approves the BIA results" (`workflow-design.md`).

A useful way to put the question to your BC manager: *has payroll been through our BIA, and what MTPD did its owner set?*

## Where your organisation decides

- Is our payroll a critical activity? This is for your BC manager. It's unanswered here.

**Tool calls (stream-json):**

- none
