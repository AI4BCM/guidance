<!-- meta: unit=stages/embed version=2026.11.1 -->
# Embedding BCM in the organisation

Stage 2 of six.

## What this stage covers

This stage addresses the embedding of business continuity in organisational culture and practice, including awareness, engagement, education, communication, and the development of behaviours that support resilience in day-to-day work.

ILLUSTRATIVE. AWARENESS AND COMMUNICATION AS IN ISO 22301:2019, 7.3 AND 7.4

## Where does AI help, and where are its limits?

Much of this stage is explaining, adapting messages for each audience and reading feedback, and AI does that well. It tailors messages by role, simplifies guidance, writes quiz questions, finds themes in staff feedback and answers routine staff questions.

Culture still changes through people. AI makes messages more relevant and quicker to produce. The success of this stage should be judged by whether staff understand their role and participate, rather than by how much content is produced.

**Used today.** Cited public example, source in References, p. 31.

Fairfax County’s 911 call centre in Virginia collaborated with George Mason University to build an AI voicebot that plays practice scenarios to callers for new and experienced call-takers. The university reports this as a tested prototype for 2025, not reported as a result.

## What AI can do, by activity

Firstly, gather together the approved business continuity materials that staff can access. These may include policy extracts, awareness notes, role descriptions, onboarding content, exercise expectations and approved FAQs (*Data rules*, p. 7).

## Understanding the culture

Analyse surveys, workshop comments and free-text feedback in an approved, aggregated environment. The aim is to identify patterns, trends, areas of confusion and recurring concerns.

- **Anonymised feedback analysis.** Use a corporate AI or analytics tool to group survey comments into themes such as 'confusion', 'ownership gaps', 'confidence', and 'positive examples'. (L2)

## Awareness and communication

Start from the behaviour you want: for example, more people taking part in BIA interviews, plan owners keeping their plans up to date, and staff familiarising themselves with their response roles. Adapt the wording for each audience, but keep the approved version.

- **Simplification and translation.** Use AI to convert formal business continuity language into shorter, clearer wording or into other languages used within the organisation, with review before publication. (L1)
- **Current case-study creation.** Search-enabled AI can help you to identify recent public incidents that are relevant to your sector. You must verify the facts before use. (L1)
- Drafting an awareness campaign: creating messages, choosing formats and deciding on the timing for a specific audience and desired outcome. (L2)
- **Audience-specific message drafting.** Ask the AI to explain a business continuity topic to executives, line managers, site managers and support staff in plain language and in a specified format. (L2)
- **Scheduled awareness workflows.** A workflow can be set up to draft recurring awareness messages or manager reminders at regular intervals. Don't forget to approve each one before it is sent out. (L3)

## Training and competence

- Drafting FAQs, quiz questions, short learning texts, manager talking points, intranet pages and posters (L2)
- **Internal chatbot support.** A virtual assistant can answer routine questions such as where to find a plan, what a person's business continuity role involves, and why an exercise is important. However, it must be based only on approved content. (L3)

## Measuring the culture

Use participation data, survey trends, manager feedback, and validation evidence to assess whether awareness and engagement are improving.

- The themes in staff feedback and questions for the internal assistant show which awareness content should be changed, extended or stopped. (L4)

L1 Ad hoc · L2 Repeatable · L3 Defined · L4 Measured · L5 Optimising

## Minimum controls

The one control that matters: **the organisation stays the author.** Staff-facing material is reviewed for accuracy, tone and local credibility before publication, by someone who will be asked about it afterwards.

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

Skill: `/role-card` rewrites one approved document for one audience.

## Case example

**Prompt.** Rewrite our onboarding e-learning script for the newly acquired site.

**Response.** A draft script based on Onboarding v4.2. Flagged but not fixed: the footage shows the existing sites; the emergency number is the parent company's; there is no version in the language the new site uses.

**What changed.** Onboarding training is now available in the site's own language. The script took an afternoon. The dubbing took three weeks.

## Level

Level 2, Repeatable. Awareness drafting works from a fixed content base with a saved prompt and a named reviewer; it needs no connector. The staff assistant is Level 3, Defined, because its sources, its access control and its limits must be written down and owned before staff can ask it anything.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
