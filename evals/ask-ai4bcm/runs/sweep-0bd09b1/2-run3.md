# /ask-ai4bcm case 2, run3: Claude Code, guidance at 0bd09b1

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `1217daa4-49ae-4373-9f6e-613e531fc81b`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm should I use challenge-my-plan or red-team-assumptions on our recovery option paper that the steering group already likes?

**Reply (verbatim):**

# Use `/red-team-assumptions`

The guidance names this case directly: in Stage 4 (Design), `/red-team-assumptions` is the skill to run "on the option everyone already likes."

**Why not `/challenge-my-plan`:** That skill questions you about a plan you own, round by round, and only gives its view after you answer. You need something else here. The steering group has already accepted the paper, so the risk is the assumptions it relies on without saying so. `/red-team-assumptions` reads the paper and returns the full list of those assumptions in one reply, with a check for each.

| | |
|---|---|
| **Data rule (do this first)** | Classify the paper before it goes into any tool, using [`units/data-rules.md`](units/data-rules.md). Recovery options often name sites, suppliers and dependencies. Once something is pasted into the wrong tool, you can't take it back. |
| **Stage** | 4, Design: [`units/stages/design.md`](units/stages/design.md) |
| **Prompt** | [`units/prompts/review.md`](units/prompts/review.md) |
| **Skill** | `/red-team-assumptions`. It starts only when you type it. |
| **Maturity level** | Level 3 |
| **Gate** | The tool can search both registers, with access controlled by role. If you can't show that yet, check where you stand in [`units/levels.md`](units/levels.md) before running it. |
| **Effort** | An afternoon |

**After the draft:** It goes to a named reviewer, and the owner named in the Design unit decides what to do with the assumptions it lists. The steering group's approval doesn't make that decision for them. If you want your own answers to the findings tested afterwards, you can then run `/challenge-my-plan` yourself.
