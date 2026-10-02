# /ask-ai4bcm case 2, run1: Claude Code, guidance at 6aaa84b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `b8f6e1f2-25d2-43aa-8b55-4a353b554127`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm should I use challenge-my-plan or red-team-assumptions on our recovery option paper that the steering group already likes?

**Reply (verbatim):**

**Use `/red-team-assumptions`.** The guidance names it for this exact case: Stage 4 (Design), "on the option everyone already likes."

**Why not `/challenge-my-plan`:** it questions *you* about a plan you own, one round at a time, and only gives its view once you've answered. That's useful, but the risk with your paper is different. A steering group that already likes a paper stops checking what it quietly assumes. `/red-team-assumptions` reads the paper and returns, in one reply, everything it relies on without saying so, with a check for each. That gives the group a list it can work through.

**Before you start, check the data rule.** Read [`units/data-rules.md`](units/data-rules.md) before you paste anything. A recovery option paper usually draws on BIA figures, supplier details and requirements. Once something is pasted into the wrong tool, it can't be taken back.

| | |
|---|---|
| **Skill** | `/red-team-assumptions` (type it yourself; this router doesn't run it) |
| **Read** | [`units/stages/design.md`](units/stages/design.md) + [`units/prompts/review.md`](units/prompts/review.md) |
| **Level** | 3 |
| **Gate** | Retrieval across both registers, with role-based access. The assumptions can only be checked against your actual requirements and options. |
| **Effort** | An afternoon |
| **Data** | [`units/data-rules.md`](units/data-rules.md), first |

**If you're not at Level 3 yet:** you can still run the skill on the paper alone. The checks it returns will then be open questions, not checks against your records. Each one needs answering from the registers by hand.

**After the draft:** it goes to a named reviewer. The owner named in the Design unit decides what happens to the option. If you own the paper, you can type `/challenge-my-plan` afterwards to work through the assumptions it flagged before you go back to the steering group.
