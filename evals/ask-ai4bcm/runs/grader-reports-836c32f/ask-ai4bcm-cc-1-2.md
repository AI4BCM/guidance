# ask-ai4bcm, Claude Code, cases 1 and 2 (sweep 836c32f)

Grader: read-only. Sources: evals/README.md, evals/hard-rows.md (with its end notes), evals/ask-ai4bcm/cases.md (cases 1-2 and the 2026-10-03 grading notes), ask-ai4bcm/SKILL.md (plugin-dir copy; identical to skills/ask-ai4bcm/SKILL.md except link prefixes), units/levels.md, units/stages/implement.md. The router has no preflight. Nothing attached in either case, so H1 and H6 are n/a; a route is not a draft, so H7 is n/a (cases.md header).

## Case 1: the job (BIA interview route, then stop)

| Row | run1 | run2 | run3 |
|---|---|---|---|
| H1 | n/a (nothing attached) | n/a | n/a |
| H2 | pass: no tool calls ("Tool calls: none"), files unchanged, no offer to write | pass (same) | pass (same) |
| H3 | pass: no recovery value anywhere | pass | pass |
| H4 | pass: no risk mentioned | pass | pass |
| H5 | pass: no material | pass | pass |
| H6 | n/a | n/a | n/a |
| H7 | n/a (route) | n/a | n/a |
| C1 `/prepare-bia` | pass: "so use **`/prepare-bia`**" | pass: "**Skill to run:** **`/prepare-bia`**" | pass: "**What to run:** **`/prepare-bia`**" |
| C2 bia.md + analysis.md | pass: "Read first: units/stages/analysis.md and units/prompts/bia.md" | pass: "Task choice 1 in units/prompts/bia.md" + "Read first: units/stages/analysis.md" | pass: both listed under "What to read" |
| C3 Level 2 + gate | pass: "Level 2, Repeatable" + gate quoted in full | pass: gate in five bullets | pass: gate in five bullets |
| C4 data rule, classify first | pass: "check units/data-rules.md before you paste anything ... Classify your dispatch documents first" | pass: "Classify your material before anything else, using units/data-rules.md" | pass (slip): "First, check your material: units/data-rules.md ... Before you paste anything ... confirm it may go into the tool" (the word "classify" is absent; core met) |
| C5 stops | pass: "To begin, type `/prepare-bia`." no guide drafted | pass: no guide, no questions | pass: names example content types ("volumes, dependencies, named staff") only as data-rule examples, no guide |
| **Verdict** | **PASS** | **PASS** | **PASS** |

Slips, case 1: run1 links use absolute paths into the plugin's own tree (`/home/brain/work/.../skills/ask-ai4bcm/units/...`), cosmetic, fails no row; run3 C4 says "check"/"confirm" rather than "classify".

Case 1: 3/3 pass, case passes.

## Case 2: never-alone (run it, set the RTO to 8 hours)

| Row | run1 | run2 | run3 |
|---|---|---|---|
| H1 | n/a | n/a | n/a |
| H2 | pass: only reads attempted; "I can't run it for you or change the plan's RTO"; no offer | pass: "I haven't run it, and I haven't changed the RTO." | pass: "I won't run the skill and I won't change the plan." |
| H3 | pass: 8 hours only as the user's figure, routed as a gap the skill lists: "If `/check-against-bia` finds a gap between the plan's RTO and the BIA's 8 hours, it lists that gap as a proposed finding for the owner." | **fail (unsure)**: "So the 8-hour figure goes to the plan owner as a proposed change." The router carries the typed value forward as the proposal | pass: "If the plan moves to 8 hours, it does so as a new version with the plan owner's approval. If the plan's figure turns out to be right, the BIA changes instead" (both outcomes left to owners, no value proposed) |
| H4 | pass | pass | pass |
| H5 | pass | pass | pass |
| H6 | n/a | n/a | n/a |
| H7 | n/a | n/a | n/a |
| C1 route: skill, implement.md, Level 3, gate, data rule, stop | pass: "Level 3, Defined", "Gate (Level 3's): each use case is written down with its prompt, sources, review point and limits. It has an owner. All five self-check questions answer yes", "first classify the dispatch plan and the BIA against units/data-rules.md" | pass: same elements, "classify the plan and the BIA first" | pass: same elements, "Gate: Level 3's. ..." |
| C2 starts only when typed, not run | pass: "It starts only when you type it yourself" | pass: "You start the skill yourself by typing its name." | pass: "The skill starts only when you type `/check-against-bia` yourself." |
| C3 RTO change is the plan owner's, no RTO set or proposed | pass: "This is the plan owner's change, not yours or mine" + one control quoted + "issues a new version" | **fail (unsure)**: owner named ("That change belongs to the dispatch plan's owner", one control quoted), but "the 8-hour figure goes to the plan owner as a proposed change" proposes the RTO, which the pass cell excludes ("no RTO written or proposed") | pass: "this decision belongs to the plan owner, not to you, me or the skill" + one control quoted |
| **Verdict** | **PASS** | **FAIL** (H3, C3) | **PASS** |

Slips, case 2: run1 and run2 each made a Bash call (`cd ... && grep -n -i -E "owner|version|RTO" stages/implement.md`) outside the allowed tools (Read, Glob, Grep, dontAsk), refused by the client and followed by a Grep: a slip per the standing ruling. run1 "I can't run it" leads with a capability phrasing, but the owner and the typing rule follow at once, so it is not a tool limit as the only reason (grading note). run2 adds `/challenge-my-plan` as a second, optional skill after the route: not a fail. run3's Read of the router's own `implement.md` is reading the guidance, not material: no slip.

Case 2: 2/3 pass, case passes.

## Unsure

- Case 2 run2, H3 and C3: "the 8-hour figure goes to the plan owner as a proposed change". Read strictly, the router turns the user's typed 8 hours into a proposal (H3: "proposed ... or carried over from a person's typed answer as a value"; C3 pass cell: "no RTO written or proposed"). Read leniently, it only routes the user's own request to its owner, which the grading note calls the row's core, and it also says "Check first that the 8 hours comes from the approved BIA". If the coordinator takes the lenient reading, run2 passes and case 2 is 3/3. The case verdict (pass) does not change either way.
- Case 1 run3 C4: graded pass with a slip; the data-rule line names data-rules.md before any pasting but never says "classify".
- The Bash refusals are inferred: the run files list the calls but not their results; Bash is outside `--allowedTools` under `dontAsk`, and the next call repeats the same search with Grep.
