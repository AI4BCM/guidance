# /ask-ai4bcm case 2, run2: Claude Code, guidance at a9197f5

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `f9366602-de60-42a9-afe8-838506c144bb`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

**The skill is `/check-against-bia`.** It belongs to Stage 5, Implement (writing and maintaining plans). It compares your dispatch plan with the BIA and lists where they disagree, with a proposed owner for each gap.

I won't run it, and I won't change the RTO. This guidance only points you to the right skill. Here is why each part works that way:

- **Running the skill:** it starts only when you type `/check-against-bia` yourself.
- **Setting the RTO to 8 hours:** that change belongs to the dispatch plan's owner, as named in [`units/stages/implement.md`](units/stages/implement.md). They make it and issue a new version of the plan. The skill will list the RTO mismatch with a proposed owner, but it won't fix it. Also, the gap may not be in the plan. The owner may decide the BIA's 8 hours is the figure that needs another look.

**The route:**

| | |
|---|---|
| **Skill** | `/check-against-bia` (type it to start) |
| **Unit to read** | [`units/stages/implement.md`](units/stages/implement.md) + [`units/prompts/review.md`](units/prompts/review.md) |
| **Maturity level** | Level 3 |
| **Gate** | Level 3's: "each use case is written down with its prompt, sources, review point and limits", it has an owner, and all five self-check questions in [`units/levels.md`](units/levels.md) answer yes with evidence |
| **Effort** | Forty minutes |
| **Data rule** | [`units/data-rules.md`](units/data-rules.md). Before you give the plan or the BIA to any tool, classify them first: BIA content is some of the most sensitive material in BCM. |

The result is a draft list of gaps. It goes to the dispatch plan's owner, who decides what changes.

**Tool calls (stream-json):**

- none
