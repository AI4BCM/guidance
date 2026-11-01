---
name: prepare-bia
description: Asks who the interview is with and what you need back, then drafts the interview guide from your material.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.11.1"
---

First run [`preflight.md`](preflight.md). This is prepare-bia, version 2026.11.1.

## The one control

"A resource requirement drafted by AI is only a question for the activity owner. It goes into the register only when
the owner confirms it." "Recovery fields stay empty in anything AI produces."

## Method

1. **Fix the sources and their dates.** Ask the organiser, in one message, these three
   ("at most three questions the attached material leaves open"): who the interview is with, what you need back, and how long it runs. Confirm once, as a statement, that memory, past chats, project files, connectors and web search are off. Answers go under
   Gaps as "own statements, not sources", never a value; an entry only they support has Source `Gaps`, and any channel left on goes under Gaps.
2. **Draft first.** Run the Task choice; sections in this order:
   1. impacts over time;
   2. the MTPD;
   3. people, "with the skills, authorities and mandates the work needs";
   4. seats and buildings;
   5. IT and applications, "each with its RTO and its RPO";
   6. suppliers and other third parties;
   7. dependencies, their own section: "up- and downstream relationships with other departments, each recorded with
      the RTO the relationship carries".

   A single supplier, carrier or person behind a resource is a question for the activity
   owner. An earlier record's
   name is never stated as current: ask *is [name] still the one?* Rate impacts over time in full only for the activity or two the sources rank highest; for the
   rest, ask only where they differ.

   Add the organiser's take-in sheet: plain spoken questions, one per line, conflicts between sources first, a
   rough time per section, marking those to drop first if it runs late; no tables or file codes. No scripted opening line.
3. **Interview.** Tell the owner to "use the draft as the thing to correct, not the thing to confirm; record what it
   could not have known".
4. **Compare registers across sites.** Put each conflict "to the two owners,
   not to the model".
5. **Hand on with the confirmed and unconfirmed marks intact.** New entries are labelled "candidate, to
   confirm"; one the sources show confirmed keeps its mark. Before the preflight's AI-help sentence, write:

   > After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

## Task choice

[`units/prompts/bia.md`](units/prompts/bia.md), first in its Task line: "draft candidate activities, their
resource requirements and interview questions for the site in the attached material". Keep its Intake, Output, Gaps
and Cite.

## For the auditor

The register carries "the source, the interview it came from and the date behind each entry". Blank before the interview: the interview, the confirmation date and "the recovery times the owner set".

## Reviewer

The activity owner confirms each requirement and sets MTPD and RTO. "Top management approves the BIA results." Name both.

## Sources

- One control, recovery fields blank: `units/stages/analysis.md, Minimum controls`; principle 3
- Method, organiser's answers, reviewer: `units/stages/analysis.md, Method`; `units/workflow-design.md, The BIA workflow, five stages`; `units/prompts/bia.md`; principle 4; IMDA section 2.2.2
