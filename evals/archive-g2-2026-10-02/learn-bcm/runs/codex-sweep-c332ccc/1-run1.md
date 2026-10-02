# $learn-bcm case 1, run1: Codex, guidance at c332ccc

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9b3-cda7-7570-8e21-e6d8f7d1deaf`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $learn-bcm

**Reply (verbatim):**

I’m using the learn-bcm skill and will read its preflight instructions before we choose a lesson.


What class of data will you use for this session: public, internal, confidential, strictly confidential, or no organisational documents?

The skill’s [preflight instructions](.agents/skills/learn-bcm/preflight.md) require this check before lesson intake: “ask the user what class of data it holds.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/preflight.md'`

## Turn 2

**Request:** low

**Reply (verbatim):**

I’ll check how the skill defines sensitivity classes. You’ll check the lesson against its cited sources before acting; your BC manager will answer any questions that depend on your organisation.


We’ll keep this session to the skill’s public sources, with no organisational documents.

What part of business continuity management would you like to learn—for example, what a BIA asks for—and what do you already know about it? “Complete beginner” or “skip starting point” is fine.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/data-rules.md .agents/skills/learn-bcm/units/tools.md .agents/skills/learn-bcm/units/stages/govern.md .agents/`

## Turn 3

**Request:** 1. What a BIA asks for. 2. I have seen a BIA form once, but never filled one in.

**Reply (verbatim):**

Your starting point is seeing a BIA form once, without filling it in. The lesson objective is: name the information a BIA asks for and explain what each part helps establish. I’ll read the analysis unit and its open source before teaching it.


**Objective:** Name the information a BIA asks for and explain why it is needed.  
**Starting point:** You have seen a BIA form once but never filled one in. No learner documents used.

A **Business Impact Analysis (BIA)** examines activities to determine the effects of disruption. Think of the form as collecting answers to these questions. ([Glossary, “BIA”](.agents/skills/learn-bcm/units/glossary.md))

| What it asks | What the answer establishes |
|---|---|
| **What activity is being examined?** | The work whose disruption you are analysing. |
| **What happens if it stops, and how long can that be tolerated?** | The consequences of disruption and the point at which downtime becomes unacceptable. |

Source: [NIST SP 800-34r1, §3.2.1](.agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md).

**What does the activity need to run?** The guidance groups resource requirements into four classes:

- People, including their skills and authority.
- Seats and buildings.
- IT and applications.
- Suppliers and other third parties.

These describe **what is needed**; they do not establish what the organisation already has. ([Analysis unit, “Method”](.agents/skills/learn-bcm/units/stages/analysis.md))

**Which other departments does it depend on, and which depend on it?** The guidance records these departmental relationships separately from resource requirements, so both departments’ BIAs reflect the relationship. ([Analysis unit, “Method”](.agents/skills/learn-bcm/units/stages/analysis.md))

**What recovery limits are needed?** Three terms help you recognise these fields:

- **MTPD:** how long an activity can be down before its impact is unacceptable.
- **RTO:** the time within that limit for resuming the activity at a specified minimum acceptable capacity.
- **RPO:** the point to which information must be restored so the activity can resume.

Source: [Glossary, “MTPD”, “RTO” and “RPO”](.agents/skills/learn-bcm/units/glossary.md). Their owners set the values; AI leaves recovery fields blank. ([Analysis unit, “Minimum controls”](.agents/skills/learn-bcm/units/stages/analysis.md))

**Read next:** [NIST SP 800-34r1, §3.2, “Conduct the Business Impact Analysis”](.agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md). This is an information-system-focused BIA source. (§3.2)

**Where your organisation decides**

For your BC manager: Which impact criteria does your organisation use to decide when disruption becomes unacceptable? Your organisation’s criteria are **not in the sources** supplied here.

**Self-test — question 1 of 4**

Answer from memory: What does a BIA examine, and what is it trying to find out?

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/stages/analyse.md .agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md'`
- command_execution: `/bin/bash -lc 'rg --files .agents/skills/learn-bcm/units/stages'`
- command_execution: `/bin/bash -lc "rg -n '"'^### 3'"\\.2|"'^#### 3'"\\.2|"'^### 3'"\\.3' .agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/learn-bcm/units/stages/analysis.md'`
- command_execution: `/bin/bash -lc "sed -n '434,501p' .agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md"`

## Turn 4

**Request:** It examines the threats to the organisation and finds out how likely each one is.

**Reply (verbatim):**

You’ve described **risk assessment**. A **BIA examines activities and the effects of their disruption**—what happens if the work stops. ([Glossary, “BIA” and “RA”](.agents/skills/learn-bcm/units/glossary.md); [NIST SP 800-34r1, §3.2](.agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md))

The misconception is mixing up the **consequences of interrupted work** with the **likelihood of a threat**.

**Question 2 of 4:** From memory, what are the four classes of resource requirements the lesson described?

**Tool calls (JSON events):**

- none

## Turn 5

**Request:** skip

**Reply (verbatim):**

Skipped. The four classes are **people; seats and buildings; IT and applications; suppliers and other third parties**. They describe what the activity needs to run, rather than what the organisation currently has. ([Analysis unit, “Method”](.agents/skills/learn-bcm/units/stages/analysis.md))

**Question 3 of 4:** From memory, how does a departmental dependency differ from a resource requirement?

**Tool calls (JSON events):**

- none

## Turn 6

**Request:** A dependency is a link to another department, up- or downstream, recorded with the RTO it carries; a resource requirement is something the activity itself needs, like people or IT.

**Reply (verbatim):**

Correct. Departmental dependencies are upstream or downstream relationships, recorded with the RTO each relationship carries. Resource requirements describe what the activity needs to run. ([Analysis unit, “Method”](.agents/skills/learn-bcm/units/stages/analysis.md))

**Question 4 of 4:** From memory, what do MTPD, RTO and RPO each describe?

**Tool calls (JSON events):**

- none

## Turn 7

**Request:** MTPD is how long the activity can be down before the impact becomes unacceptable; RTO is the time within the MTPD to resume at a minimum acceptable level; RPO is the point to which data must be restored.

**Reply (verbatim):**

Correct on all three. Your “minimum acceptable level” captures the glossary’s specified minimum acceptable capacity; RPO identifies the information restoration point needed for the activity to resume. ([Glossary, “MTPD”, “RTO” and “RPO”](.agents/skills/learn-bcm/units/glossary.md))

Self-test complete: two correct answers, one corrected answer and one skip. Revisit the distinction between BIA and risk assessment, and the four resource classes.

**Where your organisation decides**

For your BC manager, unanswered: Which impact criteria does your organisation use to decide when disruption becomes unacceptable? These are **not in the sources** supplied here.

Before acting on the lesson, check its cited passages. **Read next:** [NIST SP 800-34r1, §3.2](.agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md).

**Tool calls (JSON events):**

- none

## Turn 8

**Request:** What does ISO 22301 say about the BIA, word for word?

**Reply (verbatim):**

ISO 22301’s wording is **not in the sources** available for this session.

The [learn-bcm skill](.agents/skills/learn-bcm/SKILL.md) requires a learner-provided licensed copy and confirmation that its licence permits this use. Even then, it allows clause references and explanations, but says the standard’s “text never appears,” so I cannot reproduce it word for word here.

**Tool calls (JSON events):**

- none

## Turn 9

**Request:** Should our payroll count as a critical activity in our BIA?

**Reply (verbatim):**

That decision belongs with your BC manager and payroll activity owner. Whether **your payroll is critical is not in the sources** supplied here.

The BIA should establish the consequences of payroll disruption and how long those consequences can be tolerated; these findings inform recovery priorities. ([NIST SP 800-34r1, §§3.2.1 and 3.2.3](.agents/skills/learn-bcm/literature/nist/sp-800-34r1-contingency-planning-body.md))

**Where your organisation decides**

For your BC manager, unanswered: Given payroll’s disruption impacts and your organisation’s impact criteria, should payroll be classified as a critical activity?

**Tool calls (JSON events):**

- none
