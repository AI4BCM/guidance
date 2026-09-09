<!-- meta: unit=stages/embed pp=2 version=2026.09 cites=3.1,3.2,3.4,3.5,3.6 -->
# Embedding BCM in the Organisation

## Situation

Embedding is explanation, repeated for audiences who do not share your vocabulary. AI is good at that: it tailors one approved message for executives, line managers, new starters and a site that works in another language, and it does the twentieth version as willingly as the first.

That is also the failure mode. The measure of this stage is not how much material exists but whether people understand and act. Repeated AI-generated messages that read as generic reduce engagement rather than improve it, and culture is not produced by volume.

## Typical AI uses

- drafting awareness plans, campaign themes and manager talking points
- tailoring one approved message by audience, function or site
- simplifying policy and plan language, and translating it for review
- creating FAQs, onboarding text, quiz items and microlearning content
- clustering anonymised survey or workshop feedback into themes
- answering routine staff questions through an assistant bounded to approved staff-facing content

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

## Prompts

```
Role: you are an internal communications adviser supporting BCM awareness.
Task: rewrite the attached induction script for staff at a newly acquired site.
Sources: use only the attached induction script and BC policy extract. Keep the approved intent unchanged.
Output: the revised script, then a separate list of items you changed for audience fit.
Gaps: flag anything that is inaccurate for this site rather than correcting it yourself, and list what is missing.
Cite: name the source version you worked from.
```

## Case example

**Prompt.** Rewrite our induction e-learning script for the newly acquired site.

**Response.** A draft script from Induction v4.2. Flagged and not fixed: the footage shows the existing sites; the emergency number is the parent organisation's; no version exists in the language the new site works in.

**What changed.** Induction training became available in the site's own language. The script took an afternoon; the dubbing took three weeks, which is where the real timeline sat.

## Level

Level 2, Team-level structured use. Awareness drafting works from a defined content base with a repeatable prompt and a named reviewer; it needs no connector. The bounded staff assistant is Level 3, because it retrieves from a controlled repository under access control.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
