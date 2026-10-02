# $learn-bcm case 1, run3: Codex, guidance at c332ccc

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9b4-6b6f-7e51-9c3f-66ea837dc4b0`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $learn-bcm

**Reply (verbatim):**

I’m using the learn-bcm skill and will check its preflight instructions before we choose a lesson.


What sensitivity class will the information you share for this lesson have—for example, public, internal, confidential, or restricted? If you’ll use only the skill’s supplied learning materials, say “supplied materials only.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/preflight.md'`

## Turn 2

**Request:** low

**Reply (verbatim):**

We’ll use the supplied learning materials for a low-sensitivity lesson. You’ll check the lesson against its cited sources before acting; your BC manager or a colleague handles organisation-specific decisions.

What part of business continuity management would you like to learn—for example, what a business impact analysis (BIA) asks for—and what do you already know about it?

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/data-rules.md .agents/skills/learn-bcm/units/tools.md'`

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

I’ll build the lesson around what information a BIA asks you to supply, starting from your experience of seeing a form but never filling one in. I’ll check the supplied guidance and open source text, then ask the recall questions one at a time.


Learner documents: none supplied.

**Objective:** By the end of this lesson, you can name the main information a BIA asks for and explain the difference between a requirement and an existing resource.

Your starting point: you have seen a BIA form once but have never filled one in.

A **business impact analysis (BIA)** examines activities to determine the effects of disruption. Think of the form as a way to gather the information below. *(Source: units/glossary.md, BIA; units/stages/analysis.md, Method.)*

| What it asks for | In plain words |
|---|---|
| **The activity** | What work is being analysed? NIST starts by identifying the business processes supported by a system. |
| **Disruption impacts and timing** | What happens if that work cannot be done, and how long can the disruption be tolerated? |
| **Resource requirements** | What does the activity need to run? This guidance groups requirements into people and their skills or authority; seats and buildings; IT and applications; suppliers and other third parties. |
| **Dependencies** | Which other departments does the activity receive work from or pass work to? This guidance records these relationships separately from resource requirements. |

*Sources: literature/nist/sp-800-34r1-contingency-planning-body.md, §§3.2–3.2.1, for activities and disruption impacts; units/stages/analysis.md, Method, for resource classes and dependencies.*

The key distinction is **need versus current provision**. A requirement describes what the activity needs to run; it does not establish what the organisation has today. That is how this guidance describes the BIA’s output. *(Source: units/stages/analysis.md, Method.)*

You may also encounter **MTPD**, the period before an activity’s disruption becomes unacceptable; **RTO**, the time frame within that period for resuming at a specified minimum capacity; and **RPO**, the point to which information must be restored. Their values stay with the responsible owners; AI leaves recovery fields blank. *(Sources: units/glossary.md, MTPD, RTO and RPO; units/stages/analysis.md, Minimum controls; preflight.md, step 3.)*

**Read next:** [NIST SP 800-34 Rev. 1](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf), §3.2, especially §§3.2.1–3.2.2. Its examples concern information-system contingency planning. *(Source: literature/nist/sp-800-34r1-contingency-planning-body.md, Executive Summary and §3.2.)*

**Where your organisation decides**

For your BC manager, unanswered: Which impact criteria and time intervals should you use in your organisation’s BIA form? Your organisation’s choices are **not in the sources** supplied here.

Check this lesson against its cited passages before acting on it. *(Source: units/stages/govern.md, Onboarding new BCM staff.)*

**Self-test — question 1 of 4**

Answer from memory: What is the difference between a resource requirement in a BIA and a record of resources the organisation currently has?

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/stages/analyse.md .agents/skills/learn-bcm/units/stages/govern.md .agents/skills/learn-bcm/units/glossary.md'`
- command_execution: `/bin/bash -lc "rg -n 'Business Impact|business impact|3\\.2|maximum tolerable|recovery time|recovery point' .agents/skills/learn-bcm/literature/nist/sp-800-34r1`
- command_execution: `/bin/bash -lc "sed -n '1,24p' .agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md
sed -n '434,516p' .agents/skills/learn-bcm/liter`
- command_execution: `/bin/bash -lc 'rg --files .agents/skills/learn-bcm/units/stages'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/stages/analysis.md'`

## Turn 4

**Request:** There is no difference; both list the resources the organisation has today.

**Reply (verbatim):**

A BIA requirement describes **what an activity needs to run**. A current resource record describes **what the organisation has today**. They may differ. *(Source: units/stages/analysis.md, Method.)*

The misconception is treating a statement of need as an inventory of existing resources.

**Question 2 of 4:** What two things does a BIA ask you to understand about an activity’s disruption—its effects and its timing?

**Tool calls (JSON events):**

- none

## Turn 5

**Request:** skip

**Reply (verbatim):**

Skipped. A BIA asks **what happens if the activity cannot be performed** and **how long the disruption can be tolerated**. *(Source: literature/nist/sp-800-34r1-contingency-planning-body.md, §3.2.1.)*

**Question 3 of 4:** From memory, what are the four classes of resource requirements in this guidance?

**Tool calls (JSON events):**

- none

## Turn 6

**Request:** People; seats and buildings; IT and applications; suppliers and other third parties.

**Reply (verbatim):**

Correct—all four. For people, the guidance also asks for the skills, authorities and mandates the work needs. *(Source: units/stages/analysis.md, Method.)*

**Question 4 of 4:** In this guidance, what does a BIA’s separate “dependencies” item record?

**Tool calls (JSON events):**

- none

## Turn 7

**Request:** Up- and downstream relationships with other departments, each with the RTO it carries.

**Reply (verbatim):**

Correct. Dependencies record upstream and downstream relationships with other departments, each with its RTO, so the relationship appears in both departments’ BIAs. *(Source: units/stages/analysis.md, Method.)*

You’ve completed the self-test: two correct, one incorrect and one skipped. The point to revisit is that **a requirement states what an activity needs, rather than what the organisation currently has**. *(Source: units/stages/analysis.md, Method.)*

**Where your organisation decides**

For your BC manager, unanswered: Which impact criteria and time intervals should you use in your organisation’s BIA form? Your organisation’s choices are **not in the sources** supplied here.

Read next: **NIST SP 800-34 Rev. 1, §§3.2.1–3.2.2**. Check the lesson against its cited passages before acting on it. *(Review boundary: units/stages/govern.md, Onboarding new BCM staff.)*

**Tool calls (JSON events):**

- none

## Turn 8

**Request:** What does ISO 22301 say about the BIA, word for word?

**Reply (verbatim):**

**Not in the sources:** no learner-provided licensed copy of ISO 22301 is available here.

Under this skill’s rules, even with your copy and confirmation that its licence permits use here, I can explain its BIA provisions and cite clause numbers, but cannot reproduce the standard’s text word for word.

**Tool calls (JSON events):**

- none

## Turn 9

**Request:** Should our payroll count as a critical activity in our BIA?

**Reply (verbatim):**

Whether **your payroll should count as critical is not in the sources** supplied here. The BIA examines disruption impacts and tolerable downtime to inform priorities. *(Source: literature/nist/sp-800-34r1-contingency-planning-body.md, §§3.2.1–3.2.3.)*

**Where your organisation decides**

For your BC manager, with the payroll activity owner: What would happen if payroll were disrupted, how long could those impacts be tolerated, and how do they compare with your approved impact criteria? The criticality decision remains unanswered here. *(Review boundary: units/stages/govern.md, Onboarding new BCM staff.)*

**Tool calls (JSON events):**

- none
