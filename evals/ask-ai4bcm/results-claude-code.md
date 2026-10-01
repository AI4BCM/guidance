# /ask-ai4bcm on Claude Code: results

Claude Code 2.1.284, `--plugin-dir`, `--setting-sources project`, `--permission-mode dontAsk`, reads allowed (Read, Glob,
Grep), no write or shell tools. 2026-10-01, SKILL.md at the plugin's 2026.11.0. One run per case, none crashed; each
named case finished in one turn (no attachment, so no data-class question). Verbatim: `runs/2026-10-01-claude-code-<case>.md`.

| Case | Result | Evidence | Row broken |
|---|---|---|---|
| 1 BIA interview | pass | "Skill: `/prepare-bia`. It runs units/prompts/bia.md, Task choice 1, and leaves the recovery fields blank"; "Level: 2, Repeatable"; gate listed (saved prompt, approved tools named, data rule written down, named reviewer, approval route); "Data rule first. Read units/data-rules.md and classify …"; ends "When you're ready, type `/prepare-bia` to start it", no guide or question drafted | — |
| 2 challenge or red-team | pass | "Use `/red-team-assumptions`"; the test: challenge "interviews the plan's owner one round at a time and waits for an answer", red-team "reads the whole option paper and returns everything … in a single reply"; Level 3 with its gate, data rule; no assumptions drafted | — |
| 3 teach me RTO | partial | "this command doesn't teach. To be taught and tested on RTO, type `/learn-bcm`"; no lesson or quiz. But it quotes the glossary definition in full and adds explanation: "Read that one too, because the RTO only makes sense next to it", "An RTO is a decision the activity owner makes, and a model never proposes one" | Row 2 fail column: "An explanation of RTO beyond a one-line pointer". Cause: skill text; *Vocabulary underneath* routes word questions to the glossary, which the model read as licence to quote it |
| 4a by name | pass | `/ask-ai4bcm` started the skill: case 1 answers in the skill's route shape (skill, unit, level, gate, effort, data rule, then stop) | — |
| 4b no name | pass, environment note | stream: no `Skill` call, no read of `ask-ai4bcm/SKILL.md`; the answer has none of the router's shape (no level, gate or data-rules line). Note: with nothing in its folder the model grepped `/opt/brain` and read `units/` from an old print copy under `docs/issues/ai4bcm-skills/`, a test-machine artefact | — |
