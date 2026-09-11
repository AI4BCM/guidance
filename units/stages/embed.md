<!-- meta: unit=stages/embed version=2026.09 -->
# Embedding BCM in the Organisation

## Situation

Embedding means explaining, over and over, to people who do not use your vocabulary. AI is good at that: it tailors one approved message for executives, line managers, new starters and a site that works in another language. AI writes the twentieth version as easily as the first.

That is also where it can go wrong. Success at this stage means people understand and act. Repeated AI-generated messages that read as generic reduce engagement rather than improve it, and culture is not produced by volume.

## Typical AI uses

- drafting awareness plans, campaign themes and manager talking points
- tailoring one approved message by audience, function or site
- simplifying policy and plan language, and translating it for review
- creating FAQs, onboarding text, quiz items and microlearning content
- clustering anonymised survey or workshop feedback into themes
- answering routine staff questions through an assistant bounded to approved staff-facing content
- finding recent public incidents in the sector for awareness use, once a person has verified the facts
- scheduling recurring awareness drafts and manager reminders through a workflow, with publication held for human approval

The capability and environment for each use are in the selection guide in `tools.md`.

## Minimum controls

The one control that matters: **the organisation stays the visible author.** Staff-facing material is reviewed for accuracy, tone and local credibility before publication, by someone who will be asked about it afterwards.

- Employee comments, transcripts and survey text are handled in approved environments only, at an aggregated level, under privacy and retention rules.
- AI is not used to monitor, score or label individuals.
- An internal assistant is grounded in approved staff-facing content only, and respects existing access rights.

## Method

1. Name the behaviour you want to change — plan ownership, interview attendance, knowing who to call — not the artefact you want produced.
2. Assemble the approved content base and its dates: policy extract, awareness notes, role descriptions, existing induction material.
3. Draft the core message once, then adapt it per audience. Adaptation changes the wording, never the approved intent.
4. Require the model to flag what it cannot fix rather than repair it silently: wrong footage, a number that no longer answers, an example from the wrong site.
5. Publish through the normal route and review the effect with participation data and feedback, not with output count.

## Case studies and scheduled awareness

Two methods sit beside the core message. A recent public incident makes an awareness message concrete. A workflow keeps the programme running when nobody has time to write the next reminder. Both keep the organisation as the visible author. Neither publishes anything on its own.

| | Current public case studies | Scheduled awareness |
|---|---|---|
| Inputs | public reporting on recent incidents in the sector, with nothing about your organisation entered | the approved awareness plan and its calendar, the approved core message and the manager list |
| Capability | the public research row of the `tools.md` selection guide | the scheduled awareness row of the same guide, built on the checklist in `workflow-design.md` |
| Output | a short case note carrying the source and date of each fact and the lesson it holds for this audience | a dated draft or reminder in the reviewer's queue, with nothing published from it |
| Review boundary | the BCM professional verifies each fact against the original report before the case is used; a case that cannot be verified is dropped | a named person approves every publication; the workflow drafts and reminds, and sends nothing |

A case study borrowed from another organisation's incident becomes your message once it carries your lesson, and a scheduled reminder is still yours when it reaches a manager's inbox; the reviewer who will be asked about either is the one who releases it.

## Prompts

The awareness prompt is `prompts/awareness.md`; the case below runs its tailoring task on the induction script with the BC policy extract attached. A case note from a public incident uses the same prompt with the verified report as its only source.

## Case example

**Prompt.** Rewrite our induction e-learning script for the newly acquired site.

**Response.** A draft script based on Induction v4.2. Flagged but not fixed: the footage shows the existing sites; the emergency number is the parent company's; there is no version in the language the new site uses.

**What changed.** Induction training is now available in the site's own language. The script took an afternoon. The dubbing took three weeks, and that is where the real timeline was.

## Level

Level 2, Repeatable. Awareness drafting works from a fixed content base with a saved prompt and a named reviewer; it needs no connector. The bounded staff assistant is Level 3, Defined, because its sources, its access control and its limits must be written down and owned before staff can ask it anything.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
