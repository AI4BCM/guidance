# /learn-bcm case 1, run1: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `dd40b557-f196-444d-b46f-cb5c529f9490`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /learn-bcm

**Reply (verbatim):**

Before we start: what class of data will the material you bring to this lesson hold? For example public, internal, confidential, or restricted, in your organisation's own terms. If you won't attach any of your organisation's documents, just say so.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/preflight.md`

## Turn 2

**Request:** low

**Reply (verbatim):**

Thanks. I'll treat the material as low sensitivity. Please don't attach BIA data, incident records, personal data, recovery strategies or anything else on the high-sensitivity list in `units/data-rules.md` ("Sensitivity classes") unless this environment is approved for it.

**Which part of BCM do you want to learn, and what do you already know about it?** For example: BIA, MTPD/RTO/RPO, risk assessment, BC strategies, plans and exercising, or governance and policy. One or two sentences on your background is enough.

If you'd rather skip this, I'll note it as skipped and start from the beginning.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/data-rules.md`

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

I'm writing your lesson from the guidance's analysis and workflow units now.

---

**Objective:** by the end you can name what a BIA asks for, in the order the interview asks it, and say who supplies each answer.

**Sources used**
- AI4BCM guidance units, version 2026.11: `units/glossary.md`, `units/workflow-design.md`, `units/stages/analysis.md`
- `units/prompts/bia.md`, version 2026.11, dated 2026-09
- No documents from you are attached.

## What a BIA asks for

**What it is.** The glossary defines a BIA as "Business Impact Analysis; analysis of activities to determine the effects of disruption." (`glossary.md`, BIA). The unit of analysis is the **activity**, not the IT system.

**The questions come in a fixed order.** "The interview covers the following in this order: impacts over time, the MTPD, the resource requirements in their four classes and the dependencies." (`workflow-design.md`, The BIA workflow, five stages)

1. **Impacts over time.** What happens if the activity stops, and how that gets worse after hours, days or weeks. The scales you rate against are set before the BIA starts: "Impact categories, time horizons and thresholds are method parameters. They are agreed and supplied before stage 1 runs" (same section). The form gives you the categories. You don't invent them during the interview.
2. **The MTPD**, "how long an activity can be down before the impact is unacceptable." (`glossary.md`, MTPD)
3. **Resource requirements, in four classes**, asked "once the impacts and the MTPD are settled": "people, with the skills, authorities and mandates the work needs; then seats and buildings; then IT and applications, each with its RTO and its RPO; then suppliers and other third parties." (`stages/analysis.md`, Method)
   - RTO is "the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity" (`glossary.md`, RTO, this guidance's wording, citing ISO 22301:2019).
   - RPO is "the point to which information and data used by an activity is restored to enable the activity to operate on resumption" (`glossary.md`, RPO, this guidance's wording, citing ISO 22300:2025).
4. **Dependencies.** These are kept separate from suppliers. They mean "up- and downstream relationships with other departments, each recorded with the RTO the relationship carries, so that a relationship one department records appears in the other department's BIA." (`stages/analysis.md`, Method)

**Who fills in the numbers.** The approvals sit "with the activity owner, who approves the data and sets MTPD and RTO, and with top management, which approves the BIA results before solutions design starts." (`workflow-design.md`, The BIA workflow, five stages). On a form, the recovery fields belong to the owner. The analyst asks for them but doesn't set them.

**Gaps**
- ISO 22301's own clause text on the BIA: not in the sources. No licensed copy is attached, so no clause text is recited here.
- What your organisation's form asks for: not in the sources. No form is attached.

## Read next

**NIST SP 800-34 Rev. 1 (May 2010), section 3.2, "Conduct the Business Impact Analysis (BIA)"**, subsections 3.2.1 to 3.2.3. The file is `literature/nist/sp-800-34r1-contingency-planning-body.md`, retrieved 2026-09-10. It covers the same ground from an IT-system angle and uses "MTD" where this guidance uses MTPD. Noticing that difference is useful practice.

## Self-test: question 1 of 4

Answer from memory, without scrolling up.

> **Q1.** A BIA interview covers four things in a fixed order. Name them, in that order.

---

**Where your organisation decides:** none yet.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm; ls -R units literature | head -50; cat literature/README.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/glossary.md`
- Glob: `**/*.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/stages/analysis.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/prompts/bia.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/literature/README.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/units/workflow-design.md`
- Grep: `Business Impact Analysis|^#+ .*3\.2|Maximum Tolerable Downtime|Identify outage impacts`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md`

## Turn 4

**Request:** Impacts over time, then the MTPD, then the resource requirements in their four classes, then the dependencies.

**Reply (verbatim):**

**Q1: correct.** You have all four, in the right order. The passage is `workflow-design.md`, The BIA workflow, five stages: "The interview covers the following in this order: impacts over time, the MTPD, the resource requirements in their four classes and the dependencies."

The order matters for a reason. The MTPD comes from the impacts, so impacts are asked first. Only "once the impacts and the MTPD are settled" do you go on to the resources (`stages/analysis.md`, Method).

## Self-test: question 2 of 4

> **Q2.** In a BIA, who sets the MTPD and the RTO for an activity?
>
> A. The BCM analyst who runs the interview
> B. Top management, when it approves the BIA report
> C. The activity owner
> D. The IT department, since it runs the recovery

Answer with a letter, plus a few words on why if you like.

**Tool calls (stream-json):**

- none

## Turn 5

**Request:** A. The analyst, since they run the interview and fill in the form.

**Reply (verbatim):**

**Q2: not right. The answer is C, the activity owner.**

The passage is `workflow-design.md`, The BIA workflow, five stages: the approvals sit "with the activity owner, who approves the data and sets MTPD and RTO, and with top management, which approves the BIA results before solutions design starts." The stage-4 gate makes the same point: "the owner set the recovery fields".

**The misconception:** treating the person who writes on the form as the person who decides. The analyst runs the interview and records the answers. The owner supplies the values. The analysis unit puts it this way: "a resource requirement drafted by AI is only a question for the activity owner. It goes into the register only when the owner confirms it." (`stages/analysis.md`, Minimum controls). In this guidance, anything the analyst drafts is a question for the owner, not an answer.

The other options:
- **B:** top management approves the *results* as a whole but doesn't set the values.
- **D:** IT isn't named in the sources as setting them.

## Self-test: question 3 of 4

> **Q3.** Resource requirements come in four classes, asked in a set order. Name the four classes, in order.

**Tool calls (stream-json):**

- none

## Turn 6

**Request:** skip

**Reply (verbatim):**

**Q3: skipped.** Here is the answer so you have it.

The passage is `stages/analysis.md`, Method: "people, with the skills, authorities and mandates the work needs; then seats and buildings; then IT and applications, each with its RTO and its RPO; then suppliers and other third parties."

So the order is:
1. People, with their skills, authorities and mandates
2. Seats and buildings
3. IT and applications, each with an RTO and an RPO
4. Suppliers and other third parties

One way to remember it: who does the work, where they sit, what they work on, and who outside the organisation they rely on.

## Self-test: question 4 of 4

> **Q4.** Your activity needs monthly figures from the Finance department to finish its work. Where does this go in the BIA?
>
> A. Under dependencies, recorded with the RTO the relationship carries
> B. Under suppliers and other third parties
> C. Under people, since Finance staff produce the figures
> D. Nowhere. Only external parties belong in a BIA

**Tool calls (stream-json):**

- none

## Turn 7

**Request:** A

**Reply (verbatim):**

**Q4: correct.** The passage is `stages/analysis.md`, Method: "Dependencies are a separate item and keep the narrower meaning of up- and downstream relationships with other departments, each recorded with the RTO the relationship carries, so that a relationship one department records appears in the other department's BIA." Finance is another department, so the link is a dependency, not a supplier. Finance's own BIA should show the same link from its side.

## Results

| Q | Topic | Result |
|---|---|---|
| 1 | Interview order | correct |
| 2 | Who sets MTPD and RTO | wrong: the analyst records the values, the activity owner sets them |
| 3 | The four resource classes | skipped |
| 4 | Dependency or supplier | correct |

**Worth revisiting:** Q2 and Q3. For Q2, reread `workflow-design.md`, The BIA workflow, five stages. For Q3, reread `stages/analysis.md`, Method. Then read **NIST SP 800-34 Rev. 1, section 3.2**.

**Before you act on this:** check this explanation against the cited sections yourself, or ask a colleague to.

**Where your organisation decides:** none. If you want to know how your own BIA form sets its impact categories, time horizons and thresholds, take that to your BC manager.

**Tool calls (stream-json):**

- none

## Turn 8

**Request:** Is our payroll a critical activity?

**Reply (verbatim):**

I can't answer that one. Whether payroll is critical in your organisation is a case to decide, and that decision belongs to your organisation, not to this lesson.

What the sources do say is how such a question gets answered:
- **Impacts are rated against agreed criteria.** "Impact categories, time horizons and thresholds are method parameters. They are agreed and supplied before stage 1 runs" (`workflow-design.md`, The BIA workflow, five stages).
- **The owner supplies the values.** The activity owner "approves the data and sets MTPD and RTO" (same section).
- **Top management approves the results**, "before solutions design starts" (same section).

So the answer for payroll comes from your organisation's own impact criteria, from what the payroll owner says in the interview, and from management's approval of the BIA results. Where payroll sits in your current BIA is not in the sources.

**Where your organisation decides**
- "Is our payroll a critical activity?" This is left unanswered for your BC manager. They can show you how payroll is rated in your current approved BIA, and against which criteria.

**Tool calls (stream-json):**

- none
