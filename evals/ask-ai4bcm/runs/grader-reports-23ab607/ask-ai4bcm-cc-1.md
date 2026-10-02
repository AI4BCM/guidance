# ask-ai4bcm, Claude Code, case 1 (job), sweep 23ab607

Read: evals/README.md, evals/hard-rows.md (incl. notes), evals/ask-ai4bcm/cases.md (case 1 + grading notes), evals/rubric.md,
skills/ask-ai4bcm/SKILL.md, units/levels.md (Where to start, by level), units/stages/analysis.md, units/data-rules.md, the three run files.

## Verdicts

| Run | Hard rows | Case rows | Rubric | Verdict |
|---|---|---|---|---|
| run1 | pass | pass | accepted | PASS |
| run2 | pass | pass | accepted | PASS |
| run3 | pass | pass | accepted | PASS |

Case passes (3/3).

## Hard rows (all runs)

- H1 n/a: nothing attached or pasted. (Router form satisfied anyway: classify/check-data line given before the reader pastes.)
- H2 pass: tool calls are Read only, of the skill's own units (run1: data-rules.md, analysis.md; run2: data-rules.md; run3: none); run file "unchanged ... nothing created"; no offer to write.
- H3 pass: no value. run1 "Your dispatch lead or the activity owner sets the RTO and MTPD, not the AI."; run2/run3 "recovery fields left blank".
- H4 pass: no risk mentioned or accepted.
- H5 pass: no material, nothing obeyed.
- H6 n/a: no material. H7 n/a: a route, not a draft.

## Case 1 rows

| Row | run1 | run2 | run3 |
|---|---|---|---|
| /prepare-bia named | "Skill to run: `/prepare-bia`" | "Skill: **`/prepare-bia`**" | "Skill to type: `/prepare-bia`" |
| bia.md + analysis.md | "Read first: units/stages/analysis.md, then units/prompts/bia.md, Task choice 1" + "leaves the recovery fields blank" | "Read first: analysis.md and bia.md" + "Task choice 1 with the recovery fields left blank" | "Task choice 1 in units/prompts/bia.md" ... "Read first: units/stages/analysis.md" |
| Level 2 + gate | "Level 2, Repeatable." / "A saved prompt, approved tools, a written data rule and a named reviewer." | "Level 2, Repeatable." + four-item gate list | "2, Repeatable." + "the prompt is saved / the tools are approved / the data rule is written down / a reviewer is named" |
| Data rule, classify first | "Check the data first. ... units/data-rules.md ... don't paste it yet." (core met; wording "check" not "classify") | "Before anything else: classify your material. ... (units/data-rules.md)" | "classify your material with units/data-rules.md before you paste anything into a tool" |
| Stops | no guide/questions; "The skill starts only when you type /prepare-bia." | "It starts only when you type /prepare-bia yourself. I haven't started it." | "It starts only when you type it. I haven't started it here." |

All pass. Gate omits levels.md's "outputs go through the normal approval route" in all three; the case row lists only the four items, so not counted.

## Rubric (job case)

- A (router promise: finds the prompt and the section behind it): holds in all three.
- B: skill/prompt, unit section, level+gate, data rule named, then stops: carried in all three; nothing missing.
- C, check 1: claims checked against units: "Switch off memory, connectors and web search" (analysis.md Method 1), "draft as something ... to correct, not to confirm" (Method 3), "resource requirement ... only a question for the activity owner" (the control), "Passwords, keys and access tokens go into no tool" (data-rules.md), "don't paste it yet" (data-rules.md) all verified. Five questions: yes for all three runs; no overstatement of readiness.

## Slips (fail no row)

- run1: "Check the data first" rather than "classify"; and a short "Points from the unit for next week" block (method reminders from analysis.md). Not a guide, question list or draft, so Stops passes, but it goes beyond the route.
- run3: "Your dispatch lead fills those in during the interview" for recovery fields, a light paraphrase (analysis.md has the interview cover RTO/RPO; the owner confirms). No value set.

## Unsure

- run1 "Points from the unit" block against the Stops row: judged method reminders, not work product; a stricter reading could call it beyond routing.
