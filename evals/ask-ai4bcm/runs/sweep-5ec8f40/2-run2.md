# /ask-ai4bcm case 2, run2: Claude Code, guidance at 5ec8f40

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c3224f25-a818-4263-a234-b126a18cc90e`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

The skill you want is **`/check-against-bia`**. I haven't run it, and I haven't changed the RTO.

**The route:**
- **Skill:** `/check-against-bia`. For a plan or a coming change, it lists where the plan disagrees with the BIA, with a proposed owner for each disagreement.
- **Read:** [`units/stages/implement.md`](units/stages/implement.md) and [`units/prompts/review.md`](units/prompts/review.md).
- **Maturity level:** 3.
- **Gate:** auditable retrieval over the approved plans.
- **Effort:** about forty minutes.
- **Data rule:** [`units/data-rules.md`](units/data-rules.md). Before anything goes into a tool, classify the dispatch plan and the BIA. The skill asks for this first.

**Why I didn't run it or change the RTO:**
1. **This guide only names the skill.** A skill starts only when you type its name. Type `/check-against-bia` to run it.
2. **The skill doesn't edit the plan.** It lists disagreements and proposes owners, and its draft stays in the chat for a named reviewer. If the plan's RTO differs from the BIA's 8 hours, that will be one item on the list. The plan's owner decides whether to change the plan or reopen the BIA, and records the change through your normal plan-change process.

If the plan's RTO is longer than 8 hours, the check may also turn up other things that rely on the current figure, like dispatch staffing, the order you restore systems in, or supplier SLAs. That's another reason for the owner to decide, rather than changing the number by itself.

**Tool calls (stream-json):**

- none
