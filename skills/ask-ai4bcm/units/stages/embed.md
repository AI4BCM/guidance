<!-- meta: unit=stages/embed version=2026.09.1 -->
# Embedding BCM in the Organisation

## Situation

Embedding means explaining, over and over, to people who do not use your vocabulary. AI adapts one approved message for executives, line managers, new starters and a site that works in another language. AI writes the twentieth version as easily as the first.

Success at this stage means people understand and act. Repeated AI-generated messages that read as generic reduce engagement.

## Typical AI uses

- drafting awareness plans, campaign themes and manager talking points
- adapting one approved message by audience, function or site
- simplifying policy and plan language, and translating it for review
- creating FAQs, onboarding text, quiz items and microlearning content
- clustering anonymised survey or workshop feedback into themes
- answering routine staff questions through an assistant limited to approved staff-facing content
- finding recent public incidents in the sector for awareness use, once a person has checked each fact against the original report
- sending awareness reminders on a fixed calendar through a workflow, each one released by a named person

The type of tool and the environment for each use are in the selection guide in `tools.md`.

## Minimum controls

The one control that matters: **the organisation stays the author.** Staff-facing material is reviewed for accuracy, tone and local credibility before publication, by someone who will be asked about it afterwards.

- Employee comments, transcripts and survey text are handled in approved environments only, only as combined results, under privacy and retention rules.
- AI is not used to monitor, score or label individuals.
- An internal assistant is based on approved staff-facing content only, and respects existing access rights.

**For the auditor.** The approved core message and the dated content it came from, the named reviewer who released each version, and the participation and feedback figures that show whether the message worked.

## Method

1. Name the behaviour you want to change (plan ownership, interview attendance, knowing who to call).
2. Assemble the approved content base and its dates: policy extract, awareness notes, role descriptions, existing onboarding material.
3. Draft the core message once, then adapt it per audience. Adaptation changes the wording, never the approved intent.
4. Require the model to flag what it cannot fix rather than repair it silently: wrong footage, a phone number that nobody answers any more, an example from the wrong site.
5. Publish through the normal route and review the effect with participation data and feedback.

## Prompts

The awareness prompt is `prompts/awareness.md`; the case below uses it to adapt the onboarding script, with the BC policy extract attached. A case note from a public incident uses the same prompt with the verified report as its only source.

## Case example

**Prompt.** Rewrite our onboarding e-learning script for the newly acquired site.

**Response.** A draft script based on Onboarding v4.2. Flagged but not fixed: the footage shows the existing sites; the emergency number is the parent company's; there is no version in the language the new site uses.

**What changed.** Onboarding training is now available in the site's own language. The script took an afternoon. The dubbing took three weeks.

## Level

Level 2, Repeatable. Awareness drafting works from a fixed content base with a saved prompt and a named reviewer; it needs no connector. The staff assistant is Level 3, Defined, because its sources, its access control and its limits must be written down and owned before staff can ask it anything.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
