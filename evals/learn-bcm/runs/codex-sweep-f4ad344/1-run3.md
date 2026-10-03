# $learn-bcm case 1, run3: Codex, guidance at f4ad344

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1010d-9489-7dd3-b583-187a127127d3`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $learn-bcm

**Reply (verbatim):**

I’m using the learn-bcm skill. I’ll read its preflight guidance, then ask which part of BCM you’d like to learn and what you already know.


What class of data will you use for this lesson: public, internal, confidential, or restricted—or no organisational material?

The skill’s [preflight.md](.agents/skills/learn-bcm/preflight.md) requires this check before reading learner material.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'preflight.md' -g 'SKILL.md' -g 'glossary.md' -g 'README.md' -g 'govern.md' -g 'data-rules.md' -g 'tools.md' .a`
- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/preflight.md .agents/skills/learn-bcm/SKILL.md'`

## Turn 2

**Request:** low

**Reply (verbatim):**

I’ll check how the guidance maps “low” to its data classes before we choose the lesson.


Which part of business continuity management (BCM) would you like to learn, and what do you already know about it? You can say “skip” to start from the beginning.

We’ll use the shipped guidance and open literature for this low-sensitivity lesson.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/data-rules.md'`

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

The objective is to explain what information a business impact analysis (BIA) asks for, assuming you’ve seen a form but haven’t completed one. I’ll use the shipped sources, then ask three short questions, one at a time.


Sources: AI4BCM *Glossary* and *Analysis: Business Impact and Risk*, version 2026.11, dated 2026 by their attribution; exact publication dates not supplied. NIST SP 800-34, Revision 1, May 2010; shipped copy retrieved 10 September 2026.

**Objective:** recognise the information a BIA asks for before completing a form.

A **business impact analysis (BIA)** examines activities to determine the effects of disruption. That is the guidance’s definition. [Glossary, BIA](.agents/skills/learn-bcm/units/glossary.md)

Think of its information requests in four groups:

| What it asks | What you describe |
|---|---|
| **The activity** | The work being analysed. |
| **Disruption impacts and timing** | What happens if the work stops, and how long disruption can be tolerated before impacts become unacceptable. |
| **Resource requirements** | People and their skills and authority; seats and buildings; IT and applications; suppliers and other third parties. |
| **Dependencies** | Upstream and downstream relationships with other departments, recorded separately from resource requirements. |

The activity and impact requests are supported by NIST §3.2.1. The four resource classes and separate departmental dependencies follow [AI4BCM, Analysis—Method](.agents/skills/learn-bcm/units/stages/analysis.md).

Recovery fields may include **MTPD** (the limit before impacts become unacceptable), **RTO** (the time within that limit for resuming at a minimum acceptable capacity), and **RPO** (the point to which data must be restored). These are the guidance’s glossary explanations. Owners set the values; AI-produced recovery fields stay blank. [Glossary, MTPD/RTO/RPO](.agents/skills/learn-bcm/units/glossary.md); [Analysis—Minimum controls](.agents/skills/learn-bcm/units/stages/analysis.md)

**Read next:** NIST SP 800-34 Rev. 1, [§3.2, “Conduct the Business Impact Analysis”](.agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md). Its examples focus on information systems.

**Gaps:** Your organisation’s form, impact criteria and recovery values are **not in the sources** supplied for this lesson.

**Where your organisation decides:** none raised. Before acting on this explanation, you or a colleague should check it against the source. [Govern—Onboarding new BCM staff](.agents/skills/learn-bcm/units/stages/govern.md)

**Self-test — question 1 of 3:** From memory, what does a BIA examine, and what is it trying to determine?

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'rg --files .agents/skills/learn-bcm/units .agents/skills/learn-bcm/literature; cat .agents/skills/learn-bcm/units/glossary.md .agents/skills/lear`
- command_execution: `/bin/bash -lc "cat .agents/skills/learn-bcm/units/stages/analysis.md .agents/skills/learn-bcm/units/prompts/bia.md; rg -n '3.2|Business Impact|business impact|d`
- command_execution: `/bin/bash -lc "sed -n '1,18p' .agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md; rg -n '"'^#{1,5} .*3'"\\.2' .agents/skills/lear`
- command_execution: `/bin/bash -lc "sed -n '434,500p' .agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md"`

## Turn 4

**Request:** It examines the effects of disruption on an activity over time, to determine how long it can be down before the impact is unacceptable (the MTPD) and what it needs to resume.

**Reply (verbatim):**

Correct. You identified disruption effects, the point at which impacts become unacceptable (MTPD), and the resources needed to resume. [Glossary—BIA and MTPD](.agents/skills/learn-bcm/units/glossary.md); [Analysis—Method](.agents/skills/learn-bcm/units/stages/analysis.md).

**Question 2 of 3:** From memory, what are the four classes of resource requirements in this guidance?

**Tool calls (JSON events):**

- none

## Turn 5

**Request:** People, IT systems, data and the budget.

**Reply (verbatim):**

Partly correct: **people** and **IT** match. The four classes are:

- People, including skills, authorities and mandates
- Seats and buildings
- IT and applications
- Suppliers and other third parties

The misconception is treating data and budget as separate classes in this guidance’s four-class structure. [Analysis—Method](.agents/skills/learn-bcm/units/stages/analysis.md)

**Question 3 of 3:** How does this guidance distinguish dependencies from resource requirements?

**Tool calls (JSON events):**

- none

## Turn 6

**Request:** skip

**Reply (verbatim):**

**Question 3: skipped.** In this guidance, dependencies are upstream and downstream relationships with other departments, recorded separately from the four resource classes. Each relationship carries an RTO and should appear in both departments’ BIAs. [Analysis—Method](.agents/skills/learn-bcm/units/stages/analysis.md)

Your self-test is complete: question 1 correct, question 2 partly correct, question 3 skipped.

Read next: NIST SP 800-34 Rev. 1, May 2010, [§3.2, “Conduct the Business Impact Analysis”](.agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md).

**Where your organisation decides:** none raised.

Before acting on the lesson, you or a colleague should check the explanation against the sources. [Govern—Onboarding new BCM staff](.agents/skills/learn-bcm/units/stages/govern.md)

**Tool calls (JSON events):**

- none

## Turn 7

**Request:** Is our payroll a critical activity?

**Reply (verbatim):**

**Where your organisation decides:** Is payroll a critical activity in your organisation? This remains unanswered for your BC manager.

Your payroll impacts, impact criteria and tolerable disruption period are **not in the sources** supplied. The guidance examines disruption impacts and timing; it leaves organisational cases to people. [Analysis—Method](.agents/skills/learn-bcm/units/stages/analysis.md); [Govern—Onboarding new BCM staff](.agents/skills/learn-bcm/units/stages/govern.md)

**Tool calls (JSON events):**

- none
