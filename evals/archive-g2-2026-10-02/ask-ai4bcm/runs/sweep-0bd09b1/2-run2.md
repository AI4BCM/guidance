# /ask-ai4bcm case 2, run2: Claude Code, guidance at 0bd09b1

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `e57e8635-85e4-415f-bd42-f6196c0289d2`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm should I use challenge-my-plan or red-team-assumptions on our recovery option paper that the steering group already likes?

**Reply (verbatim):**

**Use `/red-team-assumptions`.** Your situation is the one the Design stage names for this skill: "the option everyone already likes." It reads the paper and gives you, in one reply, everything the paper quietly relies on and a check for each one. `/challenge-my-plan` works differently. It interviews the plan's owner over several rounds and only gives its view after you answer. That suits a plan you're still shaping, not a paper that already has backing. Red-teaming also leaves you a written list you can bring back to the steering group.

- **Check the data rules first:** read [`units/data-rules.md`](units/data-rules.md) before you paste the paper anywhere. Recovery option papers often draw on BIA figures, which are the most sensitive material in BCM. Once something is pasted into the wrong tool, you can't take it back.
- **Read:** [`units/stages/design.md`](units/stages/design.md) and [`units/prompts/review.md`](units/prompts/review.md).
- **Level:** 3.
- **Gate:** retrieval across both registers, with role-based access. If you don't have that yet, do the work at Level 2 instead. That means pasting in the paper plus the relevant requirements by hand, through an approved tool, with a named reviewer.
- **Effort:** an afternoon.

**After the draft:** the decision stays with the owner that the design unit names, and you need a named reviewer to check the list. If an assumption turns out to rest on recovery requirements that don't hold, that work belongs to Stage 3 (Analysis), not Design. Go back to [`units/stages/analysis.md`](units/stages/analysis.md).

You start the skill yourself by typing `/red-team-assumptions`. This router doesn't run it.
