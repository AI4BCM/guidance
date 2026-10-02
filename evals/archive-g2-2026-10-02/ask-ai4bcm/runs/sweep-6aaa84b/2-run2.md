# /ask-ai4bcm case 2, run2: Claude Code, guidance at 6aaa84b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `12e62df3-324f-4532-93d7-4c158d8cb92e`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm should I use challenge-my-plan or red-team-assumptions on our recovery option paper that the steering group already likes?

**Reply (verbatim):**

Use **`/red-team-assumptions`**. The Design stage names it for this exact case: the option everyone already likes.

**Why not `/challenge-my-plan`:** challenge-my-plan interviews you about a plan you own, one round at a time, and only gives its view after you answer. That suits testing your own thinking. Your question is different: what does a paper the group has already accepted quietly rely on? Red-team reads the paper and gives you every assumption in one reply, each with a check. A single list like that is easier to bring back to a steering group than a transcript of a dialogue.

**The route**
- **First, the data rule:** read [`units/data-rules.md`](units/data-rules.md) before you paste the paper anywhere. Recovery option papers often name suppliers, sites and costs, and once pasted into the wrong tool they can't be taken back.
- **Skill:** **`/red-team-assumptions`**. It only runs when you type it.
- **Read:** [`units/stages/design.md`](units/stages/design.md) and [`units/prompts/review.md`](units/prompts/review.md).
- **Maturity level:** 3.
- **Gate:** retrieval across both registers with role-based access. That lets each assumption be checked against your actual requirements and solutions records. If you don't have that yet, the checks it returns are things to verify by hand, not confirmed findings.
- **Effort:** an afternoon.

**After the draft:** the output is a draft for a named reviewer. The paper's owner named in the Design unit decides what changes and what goes back to the steering group. If you want to test your own answers to the strongest assumptions before that meeting, that's when to type `/challenge-my-plan`.
