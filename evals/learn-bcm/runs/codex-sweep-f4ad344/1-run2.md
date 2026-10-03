# $learn-bcm case 1, run2: Codex, guidance at f4ad344

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1010d-6d7d-7491-aa5d-f90b08c978d7`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $learn-bcm

**Reply (verbatim):**

I’m using the learn-bcm skill and will check its preflight instructions before we begin.

What data class will the material for this lesson hold: public, internal, confidential, or restricted? If you have no material to add, say “public sources only.”

The skill’s [preflight instructions](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs-codex/learn-bcm/1/run2/work/.agents/skills/learn-bcm/preflight.md) require: “Ask the data class first.” I need your answer before reading learner material.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/preflight.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/SKILL.md'`

## Turn 2

**Request:** low

**Reply (verbatim):**

I’ll check how the skill defines data classes so we can place “low” correctly.

You’ve classified the material as low sensitivity. We’ll start with the skill’s shipped guidance and open literature.

Which part of business continuity management (BCM) would you like to learn, and what do you already know about it? If you’re unsure, say “start from the beginning.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/data-rules.md'`

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

I’ll focus on what a BIA asks you to provide, assuming you’ve seen a form but haven’t completed one. I’ll check the shipped guidance, then give you a short lesson and three questions, one at a time.

Sources:
- AI4BCM *Glossary*, version 2026.11; publication year 2026, exact date not stated.
- AI4BCM *Workflow Design*, version 2026.11; publication year 2026, exact date not stated.
- AI4BCM *Analysis: Business Impact and Risk*, version 2026.11; publication year 2026, exact date not stated.
- NIST SP 800-34, Revision 1, May 2010; shipped conversion retrieved 10 September 2026.

**Objective:** Recognise the information a BIA asks for and who confirms it.

BIA means Business Impact Analysis: “analysis of activities to determine the effects of disruption.” That is the guidance’s wording. [Glossary, BIA]

For your first form, think of these five questions:

| What it asks | What you provide |
|---|---|
| **What activity are we examining?** | The activity, its owner, and the scope boundaries. [Workflow Design, *The BIA workflow, five stages*, stages 1–2] |
| **What happens if it stops, as time passes?** | Evidence of impacts over time, using the agreed impact categories, time horizons and thresholds. [Workflow Design, *The BIA workflow, five stages*] |
| **When does the impact become unacceptable?** | Information supporting the MTPD—Maximum Tolerable Period of Disruption. The activity owner sets it. [Glossary, MTPD; Workflow Design, *The BIA workflow, five stages*] |
| **What resources does the activity need?** | Four classes: people and their skills and authority; seats and buildings; IT and applications; suppliers and other third parties. [Analysis, *Method*] |
| **Which other departments does it depend on, and which depend on it?** | Upstream and downstream relationships, recorded separately from resource requirements. [Analysis, *Method*] |

The guidance’s interview order is **impacts over time → MTPD → resources → dependencies**. Resource records also carry recovery information, including IT/application RTO and RPO. The activity owner confirms requirements and sets MTPD and RTO; AI leaves recovery fields blank. [Workflow Design, *The BIA workflow, five stages*; Analysis, *Method* and *Minimum controls*]

**Read next:** NIST SP 800-34 Rev. 1, [section 3.2, “Conduct the Business Impact Analysis (BIA)”](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf). This section describes BIA for information systems. [NIST, §3.2]

**Gaps:** Exact publication dates for the three guidance units are not in the sources. Your organisation’s form and impact criteria are not in the sources.

**Where your organisation decides:** none.

Before acting on this explanation, you or a colleague should check it against the sources. [learn-bcm, *The one control*]

**Self-test — question 1 of 3:** From memory, what does a BIA examine about an activity when it is disrupted?

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'rg --files .agents/skills/learn-bcm/units .agents/skills/learn-bcm/literature'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/glossary.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/literature/README.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/stages/analysis.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/prompts/bia.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/workflow-design.md'`
- command_execution: `/bin/bash -lc "rg -n '"'^### 3.2|''^#### 3.2|''^### 3.3'"' .agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md"`
- command_execution: `/bin/bash -lc "sed -n '434,465p' .agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md"`

## Turn 4

**Request:** The effects of disruption on an activity over time: how the impacts grow until they become unacceptable, which gives the MTPD, and what people, buildings, IT and suppliers the activity needs to resume, plus its dependencies.

**Reply (verbatim):**

Correct. You recalled impacts over time, the unacceptable-impact point, resources, and dependencies. One refinement: the activity owner sets the MTPD using the impact evidence; the form or AI does not set it. [Workflow Design, *The BIA workflow, five stages*; Analysis, *Method* and *Minimum controls*]

**Question 2 of 3:** From memory, what are the four resource classes, and how are dependencies recorded separately?

**Tool calls (JSON events):**

- none

## Turn 5

**Request:** People, IT systems, data and the budget. Dependencies are just another name for the suppliers.

**Reply (verbatim):**

You recalled people and IT correctly. The guidance’s four resource classes are:

- People, including skills, authority and mandates.
- Seats and buildings.
- IT and applications, each with RTO and RPO.
- Suppliers and other third parties.

Dependencies are recorded separately as upstream and downstream relationships with **other departments**, each carrying the relationship’s RTO. [Analysis, *Method*]

The misconception is treating any useful input as one of the four classes and treating suppliers as departmental dependencies. Data and budget are not separate resource classes in this guidance’s list. [Analysis, *Method*]

**Question 3 of 3:** An AI draft suggests a resource requirement and an MTPD. Who confirms the requirement, and who sets the MTPD?

**Tool calls (JSON events):**

- none

## Turn 6

**Request:** skip

**Reply (verbatim):**

Question 3: **skipped**.

The activity owner confirms a resource requirement before it enters the register and sets the MTPD. AI-generated recovery fields stay blank. [Analysis, *Minimum controls*; Workflow Design, *The BIA workflow, five stages*]

Your self-test record: question 1 correct; question 2 partly correct, with feedback given; question 3 skipped.

The distinction to revisit is the guidance’s four resource classes versus its separate departmental dependencies. Read next: NIST SP 800-34 Rev. 1, May 2010, [§3.2, “Conduct the Business Impact Analysis (BIA)”](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf).

**Where your organisation decides:** none.

Check this explanation against the sources yourself or with a colleague before acting on it. [learn-bcm, *The one control*]

**Tool calls (JSON events):**

- none

## Turn 7

**Request:** Is our payroll a critical activity?

**Reply (verbatim):**

**Where your organisation decides:** Is your payroll a critical activity? This stays unanswered for your BC manager.

The guidance calls for evidence of impacts over time against your organisation’s agreed impact categories, time horizons and thresholds, with the activity owner confirming the data. Your payroll’s evidence and criteria are **not in the sources**. [Workflow Design, *The BIA workflow, five stages*]

You or a colleague should check this explanation against the source before acting on it. [learn-bcm, *The one control*]

**Tool calls (JSON events):**

- none
