<!-- meta: unit=workflow-design version=2026.09 cites=1.4.9,1.5.2,annex-b2 -->
# Workflow Design

A workflow is a conversation you do not have to remember. It runs a defined process over approved inputs with named human gates, so two runs are comparable and a third person can see what happened. Most BCM value sits here rather than in ad hoc prompting.

## The design checklist

Define all eight before the workflow runs on anything real.

| Define | What it means | Example |
|---|---|---|
| the trigger | when the workflow starts | plan review date reached; supplier status changed; exercise completed |
| the approved data sources | which repositories and locations it may read, with what permissions | organisation-specific, named and access-controlled |
| the AI task | one narrow, governable step | retrieve the approved plan and template, then identify inconsistencies and likely outdated sections |
| the output format | what it hands over | draft review note with assigned actions |
| the named reviewer or approver | who decides | the BC manager reviews and approves next steps |
| logging and traceability | what is recorded | steps taken, sources used, identity of the approver |
| exception handling | what happens when it breaks | missing source data, empty or low-quality output, connector failure, rejected approval |
| the fallback procedure | how the work continues without it | manual review process if the workflow or AI service fails |

The fallback row is not paperwork. Identify the manual alternative and exercise it, because AI services fail through platform outage, identity failure, rate limiting, licensing, network or local access problems, and a continuity capability that stops when its tooling stops is not one.

## Suitable and unsuitable

Suitable: draft generation for review, plan consistency checks, debrief summarisation, action extraction, reminders and routing, change-triggered review prompts, evidence pack assembly.

Unsuitable or tightly restricted: autonomous incident declaration, autonomous plan invocation, unsupervised external messaging, uncontrolled amendment of BCMS records, automatic risk acceptance or compliance sign-off.

Also unsuitable: generating large volumes of generic BCM documentation that look impressive and tick boxes but carry no operational ownership, realism or validation.

## The BIA workflow, five stages

The worked example, and the pattern to copy. Every stage is human-in-the-loop, and the gate is the deliverable of that stage.

| Stage | The gate |
|---|---|
| 1 Scope | you confirm the scope |
| 2 Interviews | you prepare and conduct the interviews |
| 3 Mapping | you check the dependency register against what was said |
| 4 Draft | you approve the findings |
| 5 Handover | the BIA ends here; hand over to solutions design |

Five gates, five places the run can stop. The model moves work between the gates. The gates are where the BCM professional decides. Stage detail for the analysis work itself is in `stages/analysis.md`.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
