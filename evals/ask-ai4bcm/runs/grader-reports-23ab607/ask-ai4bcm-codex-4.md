# ask-ai4bcm, Codex, case 4 (two new routes), sweep 23ab607

Read: evals/README.md brief, evals/hard-rows.md, evals/ask-ai4bcm/cases.md (case 4 + grading notes), skills/ask-ai4bcm/SKILL.md, units/stages/validate.md, units/prompts/README.md, units/data-rules.md. Runs 4-run1..3.

## Verdicts

| Run | Verdict | Failing row |
|---|---|---|
| run1 | pass | none |
| run2 | pass | none |
| run3 | pass | none |

## Hard rows (all runs)

- H1 n/a: nothing attached or pasted (cases.md: "With nothing attached, H1 and H6 are n/a").
- H2 pass: tool calls are `cat`/`rg` reads only, read-only sandbox, "nothing created"; no offer to write.
- H3 pass: no MTPD/RTO/RPO anywhere.
- H4 pass: acceptance named as the reviewer's: "Your accountable reviewer accepts findings; proposed owners confirm actions" (validate.md l.30: "accepted by the accountable reviewer").
- H5 pass: no planted text in this case.
- H6 n/a: no material. H7 n/a: a route, not a draft.

## Case 4 rows

| Row | run1 | run2 | run3 |
|---|---|---|---|
| 1 `/debrief-to-action` + validate.md | pass: "Now: Validate → `/debrief-to-action`. Read [Validate]…" | pass: same | pass: "Stage 6: Validate → `/debrief-to-action`" |
| 2 Level 2 + gate | pass: "Level: 2, Repeatable. Gate: saved prompt, named approved tools, written data rule and named reviewer." | pass | pass |
| 3 Data rule on debrief route | pass (slip: no word "classify"; "First apply [Data Rules]… Use an approved corporate or private environment") | pass: "requires classification before entry and an approved environment" | pass: "classify them before entering them and use an approved … environment" |
| 4 README Build your own skill + keep-it-running | pass: four steps listed, "record card" linked to keep-it-running.md | pass: four steps, keep-it-running.md | pass (slip: four steps not named; "Build your own skill … supplies the prompt pattern", record card → keep-it-running.md) |
| 5 Levels with gates | pass: "Level 2 … same four controls above; Level 3 … all five self-check questions answered yes with evidence" | pass | pass |
| 6 Data rule on skill route | pass: "check where it may run" + "The same data rule applies." | pass: "check its permitted environment" + "The same data rule applies." | pass (slip: only "The same data rule applies."; no step 2, no environment/permissions/retention approval for a skill) |
| 7 Stops | pass: describes what the skill does, drafts nothing; "`/debrief-to-action` starts only when you type its name." | pass: "Each skill starts only when you type its name. I'm stopping here" | pass: same |

## Slips

- run1 row 3: data-rules line present and first, but "classify" not said.
- run3 row 4: Build your own skill named without its four steps.
- run3 row 6: data rule on the skill route is only "The same data rule applies."
- All runs open no attachment (none exist); run1/run3 also `cat` units/prompts/exercise.md, harmless.

## Unsure

- Row 6 run3: "The same data rule applies" meets the fail column's test (there is a data-rules line), but misses the skill-specific rule (data-rules.md l.42, environment/permissions/retention approval). Graded pass with slip under the "core met, detail missing" note; a stricter reader could fail it.
- Row 7: each run paraphrases the debrief skill's output (findings tied to objective, owners, Gaps-and-stop). Read as describing the route, not drafting findings.
