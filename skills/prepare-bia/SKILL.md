---
name: prepare-bia
description: Asks who the interview is with and what you need back, then drafts the interview guide from your material.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.11.0"
---

First run [`preflight.md`](preflight.md).

## The one control

"A resource requirement drafted by AI is only a question for the activity owner. It goes into the register only when
the owner confirms it." "Recovery fields stay empty in anything AI produces."

## Method

1. **Fix the sources you will attach, and their dates.** The prompt's Intake asks the organiser, in one message, what
   the material leaves open: the interviewee's role, what they know the organiser does not, what you need back, and
   the impact criteria if none are attached, and whether memory, past chats, connectors or web search are on. Their
   answers go under Gaps as "own statements, not sources", never a value; any of those on goes under Gaps too, since
   "the model may draw on it without saying so".
2. **Draft before interviewing (activities, resource requirements, questions, recovery fields blank).** Run the Task
   choice, then order the guide as seven numbered sections:
   1. impacts over time;
   2. the MTPD;
   3. people, "with the skills, authorities and mandates the work needs";
   4. seats and buildings;
   5. IT and applications, "each with its RTO and its RPO";
   6. suppliers and other third parties;
   7. dependencies, as their own section: "up- and downstream relationships with other departments, each recorded with
      the RTO the relationship carries".

   MTPD, RTO and RPO stay empty. A single supplier, carrier or person behind a resource is a question for the activity
   owner, not a finding.
3. **Interview.** Tell the owner to "use the draft as the thing to correct, not the thing to confirm; record what it
   could not have known".
4. **Compare registers across sites.** Name each conflict between the attached sites and put it "to the two owners,
   not to the model".
5. **Hand the register on with the confirmed and unconfirmed marks intact.** Every entry stays labelled "candidate, to
   confirm". Just before the preflight's AI-help sentence, write:

   > After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

## Task choice

[`units/prompts/bia.md`](units/prompts/bia.md), first in its Task line: "draft candidate activities, their
resource requirements and interview questions for the site in the attached material". Keep its Intake, Output, Gaps
and Cite as written.

## For the auditor

The register carries "the source, the interview it came from and the date behind each entry". In the pre-interview
draft three fields stay blank: the interview, the confirmation date and "the recovery times the owner set".

## Reviewer

The activity owner confirms each requirement and sets MTPD and RTO. "Top management approves the BIA results." Name
both in the draft.

## Sources

- The one control, and recovery fields blank: `units/stages/analysis.md, Minimum controls`; principle 4
- Sources and dates before drafting: `units/stages/analysis.md, Method`; principle 3
- The interview order and dependencies: `units/stages/analysis.md, Method`; `units/workflow-design.md, The BIA workflow, five stages`
- The organiser's answers as statements: `units/prompts/bia.md`; principle 3
- Correct the draft, do not confirm it: `units/stages/analysis.md, Method`; IMDA section 2.2.2
- Marks kept intact, and who reviews: `units/stages/analysis.md, Method`; `units/prompts/bia.md`
