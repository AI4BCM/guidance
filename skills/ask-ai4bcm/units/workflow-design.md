<!-- meta: unit=workflow-design version=2026.11 -->
# Workflow Design

A workflow runs a defined process over approved inputs with named human gates, so two runs can be compared and a third person can see what happened.

## The design checklist

Define all eight before the workflow runs on anything real. Five of them stay with the workflow afterwards on the record card in `keep-it-running.md`, which also says who to tell about it and when to retire it.

| Define | What it means | Example |
|---|---|---|
| the trigger | when the workflow starts | plan review date reached; supplier status changed |
| the approved data sources | which repositories it may read, with what permissions | organisation-specific, named and access-controlled |
| the AI task | one narrow step a person can check | retrieve the approved plan and template, then flag inconsistencies |
| the output format | what it hands over | draft review note with assigned actions |
| the named reviewer or approver | who decides | the BC manager approves next steps |
| logging and traceability | what is recorded | steps taken, sources used, the approver |
| exception handling | what happens when it breaks | missing source data, low-quality output, connector failure, rejected approval |
| the fallback procedure | how the work continues without it, who may start the manual alternative, and that this person has done it once | manual review if the workflow or AI service fails, started by a named person who has run it before |

Identify the manual alternative and exercise it. AI services fail through platform outage, identity failure, rate limiting, licensing changes and network or access problems, and the work is still due that day. Exception handling covers the approver as well as the tool; when the named reviewer is unreachable, the run stops instead of proceeding (IMDA, 2026, section 2.2.2). Fallback may be manual processing (NIST AI 600-1, 2024, GV-6.2-006), and the incident and recovery plan for the workflow is written and tested like any other (ETSI EN 304 223, 2025, provision 5.2.2-5).

## Suitable and unsuitable

Suitable: draft generation for review, checks that plans agree, debrief summaries, action extraction, reminders and routing, review prompts when something changes, evidence pack assembly.

Unsuitable or tightly restricted: autonomous incident declaration, autonomous plan invocation, unsupervised external messaging, uncontrolled amendment of BCMS records, automatic risk acceptance or compliance sign-off.

Also unsuitable: bulk generation of generic BCM documentation that carries no operational ownership, realism or validation.

## The BIA workflow, five stages

This is the worked example to copy. Every stage is human-in-the-loop.

Impact categories, time horizons and thresholds are method parameters. They are agreed and supplied before stage 1 runs, and no stage of the workflow sets them.

| Stage | Deliverable | Accepted when |
|---|---|---|
| 1 Identification of scope | scope statement and activity list | boundary and exclusions are written down |
| 2 Structured interview (conversational) | interview record per activity | every candidate activity has an owner who answered |
| 3 Convert the interview to the standardised template | completed template per department | every statement in the record is placed in a template field |
| 4 List the requirements (RTO, MTPD, RPO) | list of resource requirements carrying the numbers | impacts over time are evidenced; the owner set the recovery fields |
| 5 Consolidate the requirements and sanity check, then handover | approved BIA report | requirements are consolidated across departments, checked, recorded and retained |

The interview covers the following in this order: impacts over time, the MTPD, the resource requirements in their four classes and the dependencies.

Conducting the stage does not pass its gate. The BCM professional checks the result against the condition beside it. This guidance places the approvals with the activity owner, who approves the data and sets MTPD and RTO, and with top management, which approves the BIA results before solutions design starts. A result that fails stops the run there and is reworked or done by hand before a later stage uses it. Stage detail for the analysis work is in `stages/analysis.md`.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
