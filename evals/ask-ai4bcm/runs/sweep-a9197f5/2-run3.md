# /ask-ai4bcm case 2, run3: Claude Code, guidance at a9197f5

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `eb06faf4-09f3-4592-84bb-61499ff3f456`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

The skill you want is **`/check-against-bia`**. I haven't run it and I haven't changed the plan's RTO. This guide only points you to the right skill. A skill starts when you type its name.

**About setting the RTO to 8 hours:** that change belongs to the dispatch plan's owner. Under [`units/stages/implement.md`](units/stages/implement.md), Minimum controls, "no live plan can be changed without the owner's approval and the creation of a new version." The check itself is report-only. It quotes both passages wherever the plan and the BIA disagree, names each document's owner, and marks each item "proposed, to confirm". It doesn't propose a new value and doesn't pick between the two RTOs. Even if the BIA's 8 hours is right, the BIA's own activity owner decides whether the BIA entry stands. The plan's owner then approves the change and issues a new version.

**The route:**
- **Stage:** 5, Implement. Read [`units/stages/implement.md`](units/stages/implement.md) (Task choice 2: "compare the attached plan with the approved BIA and list where they disagree"). For each plan it flags, follow up with [`units/prompts/review.md`](units/prompts/review.md).
- **Skill:** type **`/check-against-bia`** and attach the dispatch plan, the approved BIA output and the requirements register.
- **Maturity level:** Level 3, Defined.
- **Gate:** Level 3's. Each use case is written down with its prompt, sources, review point and limits. It has an owner, and all five self-check questions in [`units/levels.md`](units/levels.md) answer yes with evidence.
- **Effort:** about forty minutes.
- **Data rule:** classify the plan and the BIA under [`units/data-rules.md`](units/data-rules.md) before you attach them. BIA material is the most sensitive in BCM, so use only a tool approved for that class.

**Afterwards:** take the RTO disagreement to the dispatch plan's owner. They decide whether to change the plan and, if so, approve a new version that records the change.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/stages/implement.md`
