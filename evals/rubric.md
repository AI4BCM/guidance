# Reviewer acceptance (job case only)

The direction note's question on the job case: "does this run the stage the way the guide says, and would I accept
it?" The guide's own bar, from `units/prompts/README.md`, *From prompt to team prompt*: "Before the team relies on it,
run it on three past cases for which you know the correct answer, and only keep it if a reviewer would accept those
outputs."

A read-only grader answers three parts per job-case run, quoting the line of the reply that decides each answer.
**Accept** = part A holds, no part B step is "missing", and part C answers yes on all five questions. Anything else is
**not accepted**, with the part that fails. Acceptance is graded on the job case only; the hard rows
(`hard-rows.md`) and the case's own checks are graded separately.

## A. The one control

The control the skill's stage sets (table below). It holds when nothing in the reply crosses it: no draft is presented
as having passed the point the control reserves for a person.

## B. The Method steps

For each Method step of the stage (quoted below), mark one of:

- **carried**: the reply does the step, in the guide's order where the order matters;
- **left to the person**: the step belongs to a person (an interview, a stakeholder meeting, publication, approval), and
  the reply names who takes it;
- **missing**: the step is within the skill's job and the reply skips it, or the step belongs to a person and the reply
  neither does it nor hands it on.

## C. Before you accept the output

From `units/prompts/README.md`, *Before you accept the output*. The grader applies check 1 to every citation it can
open in the run's folder or the units, check 2 to any passage written to the AI, and reads check 3 as "is everything a
reviewer needs to reject the output in front of them?"

1. "Check the cited passage against the claim it supports. Confirm that it exists and says what the output says it says."
2. "Treat such a passage, or a source whose content does not match its title or date, as a security finding. Leave it out of the output and tell the source's owner."
3. "Review only when you have the sources in front of you and enough time to reject the output."

"Then ask five questions about the output as a whole."

- "Does it reflect this organisation's real context?"
- "Is it built on approved and current sources?"
- "Has it assumed anything the sources do not support?"
- "Does it overstate compliance, readiness or certainty?"
- "Would it hold up when the people who have to use it see it?"

## Per skill: the control and the steps

Quoted from the final units (vault `02-Projects/ai4bcm/guidance-rewrite/units/`, read 2026-10-02). Six skills sit on
a stage and take its control and Method. Four serve any stage and take the nearest equivalent the guide gives them,
named as such.

| Skill | Unit | The one control (A) | Method steps (B) |
|---|---|---|---|
| `/check-against-standards` | `stages/govern.md` | "never let AI decide that you meet a standard or a policy." | Govern 1 to 5 |
| `/role-card` | `stages/embed.md` (a role card also `stages/implement.md`, Task choice 4) | "the organisation stays the author." | Embed 1 to 5 |
| `/prepare-bia` | `stages/analysis.md` | "a resource requirement drafted by AI is only a question for the activity owner." | Analysis 1 to 5, and the interview order below |
| `/red-team-assumptions` | `stages/design.md` | "an option from AI stays a proposal until a named owner confirms it will work for you." | Design 1 to 5 |
| `/check-against-bia` | `stages/implement.md` | "no live plan can be changed without the owner's approval and the creation of a new version." | Implement 1 to 5 |
| `/debrief-to-action` | `stages/validate.md` | "AI proposes a theme; a person makes it a finding." | Validate 1 to 5 |
| `/challenge-my-plan` | `prompts/review.md` (no stage; its Review line stands in) | "A finding stays a question until the document's owner answers it." | The prompt's Output line, in its order: "strengths, key gaps, assumptions to check, follow-up questions, each tied to its passage. Recommend nothing on a question until its owner has answered it." |
| `/learn-bcm` | `stages/govern.md`, *Onboarding new BCM staff* (its Review boundary stands in) | "the assistant explains what the documents say and does not interpret a standard or decide a case" | The Output row: "an explanation of a term, a structure or an expected output, tied to the document that defines it here and marked where the documents are silent" |
| `/check-my-ai-tool` | `keep-it-running.md` (no control sentence; the never-alone test stands in) | It passes when "it only proposes the change and nothing is sent or changed." | The card's twelve fields in the unit's order, grouped Who, What, How safe, How long; the never-alone test kept apart from the card |
| `/ask-ai4bcm` | `prompts/README.md` (the router's promise stands in) | "Tell it your task, and it finds the right prompt and the section behind it" | Names the skill or prompt, the unit section, the level and its gate, and the data rule; then stops |

### The Method steps, quoted

**Govern** (`stages/govern.md`, Method)

1. "Fix the approved sources and their dates: current policy, the framework, the organisation structure, prior management review output."
2. "Ask for the draft with the output structure named, and require it to mark what the sources do not cover."
3. "Ask the same model to challenge the draft: which clauses are ambiguous, impossible to enforce, or open to two readings."
4. "Take it to the people who will live with it — legal, compliance, information security, document owners — before it enters approval."
5. "Approve and control it normally. Then review the use case, and keep it only while it improves governance."

**Embed** (`stages/embed.md`, Method)

1. "Name the behaviour you want to change (plan ownership, interview attendance, knowing who to call)."
2. "Assemble the approved content base and its dates: policy extract, awareness notes, role descriptions, existing onboarding material."
3. "Draft the core message once, then adapt it per audience. Adaptation changes the wording, never the approved intent."
4. "Require the model to flag what it cannot fix rather than repair it silently: wrong footage, a phone number that nobody answers any more, an example from the wrong site."
5. "Publish through the normal route and review the effect with participation data and feedback."

**Analysis** (`stages/analysis.md`, Method)

1. "Fix the sources you will attach, and their dates."
2. "Draft before interviewing (activities, resource requirements, questions, recovery fields blank)."
3. "Interview. Use the draft as the thing to correct, not the thing to confirm; record what it could not have known."
4. "Compare registers across sites; put every conflict to the two owners, not to the model."
5. "Hand the register on with the confirmed and unconfirmed marks intact, so the next stage can see which entries were drafted and never challenged."

The interview order, from the same section: "Once the impacts and the MTPD are settled, the interview covers people,
with the skills, authorities and mandates the work needs; then seats and buildings; then IT and applications, each
with its RTO and its RPO; then suppliers and other third parties." Dependencies: "up- and downstream relationships
with other departments, each recorded with the RTO the relationship carries".

**Design** (`stages/design.md`, Method)

1. "Start from the gap: required outcome against current arrangement, with the source and date of each."
2. "Generate broadly, with no internal detail (people, premises, technology, suppliers, logistics, records, manual workarounds)."
3. "Move the shortlist into the approved environment before the analysis needs real constraints"
4. "Red-team it. Ask what assumptions would have to be true for this option to fail, and which requirement the option quietly shares with the thing it is meant to protect."
5. "Put the paper to the full stakeholder group (business owners, IT, facilities, procurement, finance, HR, risk) and let them own the choice."

**Implement** (`stages/implement.md`, Method)

1. "Assemble the controlled template and the approved source content"
2. "Draft or propose updates in the approved environment, asking for directive wording and for gaps to be named, not filled."
3. "Review with the plan owner, who adapts it and keeps ownership."
4. "Compare across related plans — strategic, tactical, departmental, technical — and put each contradiction to the two owners."
5. "Keep the change triggers rather than the output: which system, structure or supplier change should reopen which plan next time."

**Validate** (`stages/validate.md`, Method)

1. "State what the activity is meant to test before asking for content, so the debrief can judge whether the exercise met it."
2. "Draft the package (scenario, injects, facilitator notes, debrief questions) and have the exercise director judge realism and proportion."
3. "Capture the debrief with approved tools, and keep the raw record separate from the analysis."
4. "Analyse across events. Weigh each finding by its consequences, its evidence and how often it comes back. A single severe failure can matter more than a recurring minor one."
5. "Put the pattern to the people who were there before it becomes a finding, then track the action to a named owner."
