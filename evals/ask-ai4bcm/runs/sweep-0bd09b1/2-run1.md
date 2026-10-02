# /ask-ai4bcm case 2, run1: Claude Code, guidance at 0bd09b1

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c1b682d4-84a1-40dd-8e77-7b44bf2d1bcf`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm should I use challenge-my-plan or red-team-assumptions on our recovery option paper that the steering group already likes?

**Reply (verbatim):**

# Use `/red-team-assumptions`

Your case is the one the Design stage names: a recovery option paper that the steering group already likes.

**Classify the paper first.** Before you paste it anywhere, read [`units/data-rules.md`](units/data-rules.md). Recovery option papers usually include supplier names, costs and site details. Once something goes into the wrong tool, you can't take it back.

**Why red-team and not challenge:**
- **`/red-team-assumptions`** reads the paper and returns everything it quietly relies on in one reply, with a check for each item. When everyone already agrees, those unexamined assumptions are where the risk is, and this skill finds them without depending on anyone's view of the option.
- **`/challenge-my-plan`** asks you hard questions about a plan you own, one round at a time. It tests how well you can defend the option. It doesn't check what the paper takes for granted.

If you're the author and want to practise defending the option before the next steering meeting, you could run `/challenge-my-plan` after the red-team pass. Run red-team first.

**Route**
- **Stage:** 4, Design. Read [`units/stages/design.md`](units/stages/design.md) and [`units/prompts/review.md`](units/prompts/review.md).
- **Maturity level:** 3.
- **Gate:** retrieval across both registers with role-based access. If you don't have that yet, you're below the gate. See the self-check in [`units/levels.md`](units/levels.md).
- **Effort:** an afternoon.

**After the draft:** you get a list of assumptions and checks, and nothing is written anywhere. A named reviewer checks the list, and the option owner named in the Design unit decides what changes in the paper. The skill only starts when you type `/red-team-assumptions` yourself.
