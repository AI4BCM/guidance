# /prepare-bia: the analysis stage's pre-interview draft, made runnable

Rebuild `prepare-bia/SKILL.md` (edition 2026.11, ticket 64) from its stage unit. Job, word for word from the
manifest: "Asks who the interview is with and what you need back, then drafts the interview guide from your
material." Keep the frontmatter's `name`, `description`, `license`, `disable-model-invocation: true` and
`metadata.version: "2026.11.0"`.

## What the skill is built from

- **Stage unit:** `units/stages/analysis.md`. Its one control (Minimum controls, "The one control that matters"), its
  Method steps 1 to 5, its **For the auditor** paragraph.
- **The interview order:** analysis.md's paragraph after the Method and `units/workflow-design.md` ("The interview
  covers the following in this order: impacts over time, the MTPD, the resource requirements in their four classes
  and the dependencies"): impacts over time; the MTPD; people with their skills, authorities and mandates; seats and
  buildings; IT and applications, each with RTO and RPO; suppliers and other third parties; dependencies as their own
  item, up- and downstream with other departments, each with the RTO it carries. MTPD, RTO and RPO stay empty.
- **Task choice:** `units/prompts/bia.md`, the first choice in its Task line (candidate activities, resource
  requirements and interview questions for the site in the attached material), with that prompt's Intake, Output,
  Gaps and Cite as written. Link the prompt; quote only what the skill needs.
- **Reviewer:** the activity owner, who confirms each requirement and sets MTPD and RTO (`prompts/bia.md`, Review).
- **Hand-over:** after the interview, the AI4BCM BIA-Workflow takes the interview record to a signed BIA (the
  manifest's `next`). Say it as a `> ` line the model writes just before the preflight's AI-help sentence.
- **Sources:** cite the rule behind each thing the skill makes the model do: principle 4 and the units' own
  sections, and from `units/references.md` "Cited in the units" only what a rule rests on.

## What the eval found in the old skill (the reason for this rebuild)

Three of four runs broke the interview order (suppliers before IT and buildings; the carrier dependency filed under
suppliers; impacts and MTPD dropped). One named no reviewer; one cited the organiser's typed answer as a source; one
lost the activity list's "no second carrier recorded". The new body must make each of these hard to get wrong: the
order as a numbered list, dependencies as their own step, the organiser's answers as statements not sources, and a
single-source dependency (one carrier, one supplier) always a question for the activity owner.

## For the reviewer

Rows beyond One control and Method 1 to 5: the interview order (each of the seven items above), Task choice 1, For
the auditor, the reviewer, the hand-over.
