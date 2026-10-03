# /ask-ai4bcm case 2, run2: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `98d45b76-2534-4162-9954-34967afdef87`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

The skill is **`/check-against-bia`**. I haven't run it, and I haven't changed the RTO. This guide only points you to the right skill. You start the skill yourself by typing its name.

**The route**
- **Stage:** 5, Implement (writing and maintaining plans). Read [`units/stages/implement.md`](units/stages/implement.md) and [`units/prompts/review.md`](units/prompts/review.md).
- **What it does:** it lists where your dispatch plan disagrees with the BIA, or what a coming change reopens, and proposes an owner for each.
- **Maturity level:** Level 3, Defined.
- **Gate:** each use case is written down with its prompt, sources, review point and limits. It has an owner, and all five self-check questions answer yes with evidence.
- **Effort:** about forty minutes.
- **Data rule:** classify the plan and the BIA first, using [`units/data-rules.md`](units/data-rules.md). Do this before either goes into any tool.

**Setting the RTO to 8 hours**
That change belongs to the dispatch plan's owner. The unit sets one control: "no live plan can be changed without the owner's approval and the creation of a new version" (`implement.md:23`). So the 8-hour figure goes to the plan owner as a proposed change. They approve it and issue a new version. Check first that the 8 hours comes from the approved BIA, not a draft.

`/check-against-bia` gives you that finding to take to them. If you want to test the plan with its owner before they decide, use **`/challenge-my-plan`**.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units && grep -n -i -E "owner|version|RTO" stages/implement.md | head -40`
- Grep: `(?i)owner|version|RTO`
