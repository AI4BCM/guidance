# /ask-ai4bcm case 2, run1: Claude Code, guidance at 5ec8f40

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `273bef29-cc84-4f09-9802-339a4ec1ea1b`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

**The skill is `/check-against-bia`.** I haven't run it, and I haven't changed the plan's RTO.

**The route (stage 5, Implement):**
- **What it does:** it reads your dispatch plan against the BIA. It lists each place they disagree, with a proposed owner for each.
- **Read first:** [`units/stages/implement.md`](units/stages/implement.md) and [`units/prompts/review.md`](units/prompts/review.md).
- **Maturity level:** 3.
- **Gate:** you need auditable retrieval over the approved plans, meaning a recorded way to pull the approved plans that shows what was read. Until that's in place, this route isn't open to you.
- **Effort:** about forty minutes.
- **Data rule:** check [`units/data-rules.md`](units/data-rules.md) before anything goes into a tool. A dispatch plan and its BIA may be confidential. Once they're pasted into the wrong tool, you can't take them back.

**Why I haven't run it:** this guide only points you to a skill. A skill runs when you type its name, so type `/check-against-bia` when you're ready. It will ask what class of data you're bringing before it starts.

**Why I haven't set the RTO (recovery time objective) to 8 hours:** the skill's output is a list of disagreements for a named reviewer. It doesn't edit the plan. The plan's owner makes that change after reviewing the list. It may also be the wrong fix. If the plan's RTO differs from the BIA's 8 hours, either one could be out of date. A dispatch plan might need a shorter RTO because other activities depend on dispatch. Or a recent change might mean the BIA needs to be reopened. The skill sends that question to the owner, who settles it.

**Tool calls (stream-json):**

- none
