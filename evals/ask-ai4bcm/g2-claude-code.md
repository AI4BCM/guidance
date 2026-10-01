# /ask-ai4bcm, G2 on Claude Code: three runs per case

Commit under test: **a5abfa8** (HEAD of the guidance repo at the start and the end of the sweep). Claude Code 2.1.284,
`--plugin-dir`, `--setting-sources project`, `--permission-mode dontAsk`, `--allowedTools Read,Glob,Grep`, stdin closed,
2026-10-01. Each run in its own fresh, empty folder; every case is a request alone and finished in one turn (no
attachment, so no data-class question). Case 4b ran with `--output-format stream-json --verbose`. Verbatim turns:
`runs/sweep-a5abfa8/<case>-run<N>.md`. All runs ended with `subtype: success`; none crashed. These runs ran before the
shared `cap-claude.sh` wrapper existed.

Rule: fail = anything in the Fail column; partial = no Fail item but part of a Pass row missing; pass = every Pass row
met. A case passes on two of three runs.

| Case | Run 1 | Run 2 | Run 3 | Case | Non-pass runs: the row they break |
|---|---|---|---|---|---|
| 1 BIA interview | pass | pass | pass | pass | |
| 2 challenge or red-team | pass | pass | pass | pass | |
| 3 teach me RTO | pass | pass | pass | pass | (run 3 borderline, see slips) |
| 4a by name | pass | pass | pass | pass | Evidence: every `/ask-ai4bcm` run in cases 1 to 3 answered in the router's shape (skill, unit, level, gate, effort, data rule, then stop) |
| 4b no name | pass | pass | pass | pass | |

**Verdict: /ask-ai4bcm passes G2 on Claude Code at a5abfa8.** Every case passes on three of three runs.

## Evidence per case (one line each)

- **1:** all three: "**`/prepare-bia`**" is the only skill named before the route ("It runs `units/prompts/bia.md`, Task choice 1, and leaves the recovery fields blank"); "Level 2, Repeatable" with the gate (prompt saved, approved tools named, data rule written down, named reviewer, normal approval route); data rule first with `units/data-rules.md`; no interview guide or question drafted; `/challenge-my-plan` named only as an optional later read of the draft.
- **2:** all three: "Use `/red-team-assumptions`", with the router's test ("`/challenge-my-plan` interviews you one round at a time and waits ...; `/red-team-assumptions` reads the paper and returns the whole list in one reply"); Level 3 with its gate; data rule; no assumptions listed; "This router doesn't run it".
- **3:** all three: "this router doesn't teach", "type **`/learn-bcm`**", pointer to the **RTO** entry in `units/glossary.md`; no definition quoted, no lesson, example or quiz.
- **4b:** stream checked per run: 0 `Skill` calls, 0 reads of any `SKILL.md`; none of the router's shape (no level with a gate). Runs 1 and 3 named `units/stages/analysis.md` and `units/prompts/bia.md` from the owner's published "Get the guidance" artifact page; run 2 found nothing and wrote its own interview prompt.

## Slips that fail no row

- **Case 3, a clause about the term beside the pointer** (as in the earlier final round): run 1 "Read the MTPD entry next to it as well, because the two terms only make sense together"; run 2 "A model doesn't set a recovery time. The activity owner does."; run 3, the strongest, "RTO is set inside the BIA and sits under the MTPD, so read all three together". None defines or teaches the term; graded as route content. Run 3 is the one a stricter reader could call "an explanation beyond a one-line pointer"; even so the case would pass on runs 1 and 2.
- **Case 3 invents a route for a word question:** all three give a level (1, or "1 or 2") and a gate ("the tool is approved and nothing confidential goes in") that the router's *Vocabulary underneath* does not give a word question; run 1 adds "roughly the ten minutes it takes to place yourself on the ladder" as the effort, borrowed from the "Where do we start?" on-ramp.
- **Case 2 run 1** glosses "both registers" as "your own and the other site's or supplier's", which is not the router's wording (the stage's two registers are risk and dependency, as run 2 says).
- **4b environment:** with only Read, Glob and Grep allowed, read-only Bash and `Artifact` list/read still ran (the harness auto-allows them), so runs 1 and 3 answered from the owner's own published artifact page; run 2 tried Google Drive search (refused). A test-machine artefact, not the skill.
