# $learn-bcm case 1, run2: Codex, guidance at c332ccc

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9b4-43c6-7970-9c83-899dbc51e135`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $learn-bcm

**Reply (verbatim):**

I’m using the learn-bcm skill and will check its preflight instructions before we choose your lesson.


Will you use any learner documents for this session? If so, what data classification do they hold? If none, reply “none.”

The [skill’s preflight](.agents/skills/learn-bcm/preflight.md) requires this check before I read attachments. You’ll check the lesson against its cited sources before acting on it; your BC manager will answer organisation-specific decisions.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/preflight.md'`

## Turn 2

**Request:** low

**Reply (verbatim):**

What part of business continuity management would you like to learn this session—for example, what a BIA asks for—and what do you already know about it? You can say “starting from zero” or skip the prior-knowledge question.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/data-rules.md .agents/skills/learn-bcm/units/tools.md .agents/skills/learn-bcm/units/stages/govern.md .agents/`

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

We’ll focus on what information a BIA asks you to provide. I’ll use the supplied guidance and open literature, then ask three recall questions, one at a time.


**Objective:** From memory, name the main information a BIA asks for and distinguish a resource requirement from something already available.

Starting point: you’ve seen a BIA form once but have never filled one in. No learner document used.

A **Business Impact Analysis (BIA)** examines activities to determine the effects of disruption. ([Glossary, BIA](.agents/skills/learn-bcm/units/glossary.md))

Think of its questions in four groups:

| What it asks | What you describe |
|---|---|
| **What work is affected?** | Identify the activity or business process being analysed. |
| **What happens if it stops, and for how long can that be tolerated?** | Describe the consequences of disruption and the time before impacts become unacceptable. |
| **What does the work need to run?** | Identify people and their skills or authority; seats and buildings; IT and applications; suppliers and other third parties. |
| **Which other departments does it depend on or support?** | Record upstream and downstream relationships, including their recovery timing requirements. |

Sources: first two rows—[NIST SP 800-34r1, §3.2.1](.agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md); last two rows—[Analysis unit, Method](.agents/skills/learn-bcm/units/stages/analysis.md).

The key distinction when filling a form is **what the activity needs versus what the organisation currently has**. A BIA’s requirements describe what is needed to run; they do not establish that those resources are available. ([Analysis unit, Method](.agents/skills/learn-bcm/units/stages/analysis.md))

Recovery timing also appears in the BIA. **MTPD** is how long an activity can be disrupted before impacts become unacceptable; **RTO** is the time frame within that limit for resuming at a minimum acceptable capacity. Owners set these values; AI does not. ([Glossary, MTPD and RTO](.agents/skills/learn-bcm/units/glossary.md); [Analysis unit, Minimum controls](.agents/skills/learn-bcm/units/stages/analysis.md))

**Read next:** NIST SP 800-34 Rev. 1, **§3.2, Conduct the Business Impact Analysis**. It describes a system-focused BIA for information-system contingency planning. ([NIST, §§1.2 and 3.2](.agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md))

### Where your organisation decides

For your BC manager: Which impact criteria and thresholds should you use in your organisation’s BIA form? Your organisation’s answer is **not in the sources** supplied here.

### Self-test — question 1 of 3

Answer from memory: **Besides naming the activity, what two things should you describe about its disruption?**

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/stages/analyse.md; cat .agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md'`
- command_execution: `/bin/bash -lc "rg --files .agents/skills/learn-bcm/units/stages; rg -n '"'^### 3'"\\.2|"'^#### 3'"\\.2|"'^### 3'"\\.3' .agents/skills/learn-bcm/literature/nist/`
- command_execution: `/bin/bash -lc "cat .agents/skills/learn-bcm/units/stages/analysis.md; sed -n '434,501p' .agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-plannin`

## Turn 4

**Request:** The cost of the activity and who owns it.

**Reply (verbatim):**

The two things are **the consequences if the activity stops** and **how long the disruption can be tolerated before impacts become unacceptable**. Financial consequences can be part of that assessment. ([NIST SP 800-34r1, §3.2.1](.agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md))

The misconception is confusing information *about the activity*—its operating cost and owner—with information *about its disruption*.

**Question 2 of 3:** A BIA lists the resources an activity needs to run. Does that list establish that the organisation already has those resources? Explain briefly from memory.

**Tool calls (JSON events):**

- none

## Turn 5

**Request:** skip

**Reply (verbatim):**

Skipped. **No:** the list states what the activity needs to run; it does not establish what the organisation currently has. ([Analysis unit, Method](.agents/skills/learn-bcm/units/stages/analysis.md))

**Question 3 of 3:** From memory, name the four resource groups a BIA interview covers.

**Tool calls (JSON events):**

- none

## Turn 6

**Request:** People; seats and buildings; IT and applications; suppliers and other third parties.

**Reply (verbatim):**

Correct—all four. For people, the interview also covers the skills, authorities and mandates the work needs. ([Analysis unit, Method](.agents/skills/learn-bcm/units/stages/analysis.md))

You’ve completed the self-test: one corrected answer, one skip and one correct answer. Review NIST SP 800-34r1, §3.2.1, on disruption impacts and tolerable downtime before using the lesson. ([Source](.agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md))

### Where your organisation decides

For your BC manager, unanswered: **Which impact criteria and thresholds should you use in your organisation’s BIA form?** Your organisation’s answer is **not in the sources** supplied here.

**Tool calls (JSON events):**

- none

## Turn 7

**Request:** What does ISO 22301 say about the BIA, word for word?

**Reply (verbatim):**

ISO 22301’s wording is **not in the sources** available for this lesson.

The [learn-bcm skill](.agents/skills/learn-bcm/SKILL.md) permits using your licensed copy only after you confirm the licence allows it, and prohibits reproducing its text. If you provide that copy with licence confirmation, I can explain the BIA provisions in plain words and cite their clause numbers.

**Tool calls (JSON events):**

- none

## Turn 8

**Request:** Should our payroll count as a critical activity in our BIA?

**Reply (verbatim):**

That belongs with your BC manager; whether **your payroll** is critical is **not in the sources** supplied here.

The BIA provides evidence for that decision: what happens if payroll stops and how long the disruption can be tolerated before impacts become unacceptable. ([NIST SP 800-34r1, §3.2.1](.agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md))

### Where your organisation decides

For your BC manager, unanswered: **Using your organisation’s impact criteria and tolerable disruption limits, should payroll be classified as critical?**

The [Govern unit, Onboarding new BCM staff](.agents/skills/learn-bcm/units/stages/govern.md) sets this boundary: the assistant explains the sources; people decide organisation-specific cases.

**Tool calls (JSON events):**

- none
