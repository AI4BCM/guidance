# /ask-ai4bcm case 2, run3: Claude Code, guidance at 6aaa84b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `3d1abc6b-62a5-49a3-b16d-4f52ac739d65`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm should I use challenge-my-plan or red-team-assumptions on our recovery option paper that the steering group already likes?

**Reply (verbatim):**

**Use `/red-team-assumptions`.**

A recovery option paper belongs to stage 4, Design (choosing continuity solutions). That stage names `/red-team-assumptions` for the case you describe: the option everyone already likes. It reads the paper and returns, in one reply, everything the paper silently relies on and a check for each. When the steering group has already agreed, the risk is assumptions nobody has questioned, and this skill is built to find them.

`/challenge-my-plan` does a different job. It questions you about a plan you own, round by round, and gives its view only after you answer. It helps you think a plan through before it's settled. It's less useful once others have bought in and the paper's hidden assumptions are the real question.

**Route**
- **Data rule first:** read [`units/data-rules.md`](units/data-rules.md) before you paste anything. Recovery options often include supplier, site or cost details. Once text is pasted into the wrong tool, you can't take it back.
- **Read:** [`units/stages/design.md`](units/stages/design.md) and [`units/prompts/review.md`](units/prompts/review.md).
- **Skill:** `/red-team-assumptions`. It starts only when you type it.
- **Maturity level:** 3.
- **Gate:** retrieval across both registers with role-based access. If you can't meet that yet, you can still run it on the paper alone. But the checks it returns will need someone to test them against the registers by hand.
- **Effort:** about an afternoon.

**After the draft:** the result is a list of assumptions and checks for a named reviewer. The option's owner, as named in the design unit, decides what to do with it. The steering group sees the checks, not just the agreement. If an assumption traces back to a requirement that was never established, that work belongs to stage 3, Analysis.
