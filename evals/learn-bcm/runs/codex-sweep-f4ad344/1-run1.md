# $learn-bcm case 1, run1: Codex, guidance at f4ad344

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1010d-462e-74e3-afd9-ed179d0267bb`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $learn-bcm

**Reply (verbatim):**

I’m using the learn-bcm skill and will check its preflight instructions before we begin.

What data sensitivity class will the material for this lesson contain? If you’re using only the skill’s public sources, say “public sources only.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/SKILL.md .agents/skills/learn-bcm/preflight.md'`

## Turn 2

**Request:** low

**Reply (verbatim):**

I’ll check the skill’s rules for low-sensitivity material, then we can choose a lesson topic.

Which part of business continuity management would you like to learn, and what do you already know about it? You can say “skip” to start with the basics.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'rg --files .agents/skills/learn-bcm'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/data-rules.md'`

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

Objective: learn what information a business impact analysis (BIA) asks for and why, starting from your experience of seeing a form once. I’ll use the skill’s shipped sources.

Sources for this lesson:

- *AI4BCM Glossary*, version 2026.11; publication year 2026, exact date not supplied.
- *AI4BCM Analysis: Business Impact and Risk*, version 2026.11; publication year 2026, exact date not supplied.
- *AI4BCM Workflow Design*, version 2026.11; publication year 2026, exact date not supplied.
- *NIST SP 800-34*, Revision 1, May 2010; shipped conversion retrieved 10 September 2026.

**Objective:** understand what information a BIA asks for before you fill in a form.

A **business impact analysis (BIA)** examines activities and the effects of their disruption. That is this guidance’s definition. ([Glossary, BIA](.agents/skills/learn-bcm/units/glossary.md))

The guidance’s interview follows this order: impacts over time, maximum tolerable period of disruption (MTPD), resource requirements, then dependencies. ([Workflow Design, “The BIA workflow, five stages”](.agents/skills/learn-bcm/units/workflow-design.md))

| What it asks about | What you describe | Source passage |
|---|---|---|
| **Impacts over time** | What happens when the activity is disrupted, and how the effects develop over time, using the agreed impact categories and time horizons. | Workflow Design, “The BIA workflow, five stages” |
| **MTPD** | How long the activity can be down before the impact becomes unacceptable. | Glossary, MTPD |
| **Resource requirements** | People—including skills and authority; seats and buildings; IT and applications; suppliers and other third parties. | [Analysis, “Method”](.agents/skills/learn-bcm/units/stages/analysis.md) |
| **Dependencies** | Upstream and downstream relationships with other departments. This guidance records these separately from resources. | Analysis, “Method” |

Recovery fields also distinguish **RTO**, the time frame for resuming at a specified minimum acceptable capacity within the MTPD, from **RPO**, the point to which information and data must be restored. These explanations use the guidance’s glossary wording. ([Glossary, RTO and RPO](.agents/skills/learn-bcm/units/glossary.md))

The activity owner confirms resource requirements and sets MTPD and RTO. AI-produced recovery fields remain empty. ([Analysis, “Minimum controls”; Workflow Design, “The BIA workflow, five stages”](.agents/skills/learn-bcm/units/stages/analysis.md))

**Read next:** *NIST SP 800-34 Rev. 1*, section **3.2.2, “Identify Resource Requirements”**, for its information-system-focused treatment of resources. [Open text](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf).

**Gaps:** exact publication dates for the three guidance units are not supplied. Your organisation’s form and impact criteria are **not in the sources** provided for this lesson.

**Where your organisation decides:** none.

Check this explanation against the cited passages yourself or with a colleague before acting on it, as the learn-bcm control requires.

**Self-test — question 1 of 3:** From memory, what does a BIA examine? Answer in your own words, or say “skip.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/glossary.md .agents/skills/learn-bcm/units/stages/analysis.md .agents/skills/learn-bcm/literature/README.md .a`
- command_execution: `/bin/bash -lc "cat .agents/skills/learn-bcm/units/workflow-design.md; rg -n '3.2|Business Impact|Date|date|Revision|May|2010|2011' .agents/skills/learn-bcm/lite`
- command_execution: `/bin/bash -lc "sed -n '1,18p' .agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md; rg -n '"'^#{1,5} .*3'"\\.2' .agents/skills/lear`

## Turn 4

**Request:** The effects of disruption on an activity over time: how the impacts grow until they become unacceptable, which gives the MTPD, and what people, buildings, IT and suppliers the activity needs to resume, plus its dependencies.

**Reply (verbatim):**

Correct. You identified the effects of disruption over time, MTPD, resource requirements and dependencies. Those match the [Glossary, “BIA” and “MTPD”](.agents/skills/learn-bcm/units/glossary.md) and [Analysis, “Method”](.agents/skills/learn-bcm/units/stages/analysis.md).

**Question 2 of 3:** From memory, what are the four resource requirement classes, and what does this guidance mean by dependencies?

**Tool calls (JSON events):**

- none

## Turn 5

**Request:** People, IT systems, data and the budget. Dependencies are just another name for the suppliers.

**Reply (verbatim):**

Partly correct: people and IT belong in the list. The four classes are:

- People, including skills and authority.
- Seats and buildings.
- IT and applications, with RTO and RPO.
- Suppliers and other third parties.

The misconception is mixing resources with dependencies. This guidance uses **dependencies** specifically for upstream and downstream relationships with other departments; suppliers belong in the resource classes. Data and budget are not separate classes in this four-class structure. ([Analysis, “Method”](.agents/skills/learn-bcm/units/stages/analysis.md))

**Question 3 of 3:** Who confirms resource requirements and sets MTPD and RTO, and how should AI-produced recovery fields be left?

**Tool calls (JSON events):**

- none

## Turn 6

**Request:** skip

**Reply (verbatim):**

Question 3: **skipped**.

The activity owner confirms resource requirements and sets MTPD and RTO. AI-produced recovery fields stay empty. ([Analysis, “Minimum controls”; Workflow Design, “The BIA workflow, five stages”](.agents/skills/learn-bcm/units/stages/analysis.md))

Your self-test record: question 1 correct; question 2 partly correct, with feedback given; question 3 skipped. Revisit the distinction between the four resource classes and dependencies on other departments.

Read next: *NIST SP 800-34 Rev. 1*, May 2010, **section 3.2.2, “Identify Resource Requirements”**. [Open text](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf).

**Where your organisation decides:** none.

You or a colleague should check the explanation against the cited sources before acting on it.

**Tool calls (JSON events):**

- none

## Turn 7

**Request:** Is our payroll a critical activity?

**Reply (verbatim):**

**Where your organisation decides**

“Is our payroll a critical activity?” remains unanswered for your BC manager. This lesson does not decide cases for your organisation.

The guidance calls for evidence of impacts over time against agreed impact categories, time horizons and thresholds. Your payroll evidence and those criteria are **not in the sources** provided here. ([Workflow Design, “The BIA workflow, five stages”](.agents/skills/learn-bcm/units/workflow-design.md))

**Tool calls (JSON events):**

- none
