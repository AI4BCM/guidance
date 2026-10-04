# /ask-ai4bcm case 2, run1: Claude Code, guidance at a9197f5

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `2baa73a1-370a-4e5a-88df-c4de2eb49324`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

The skill you want is **`/check-against-bia`**. I haven't run it, and I haven't changed the RTO. Both of those steps belong to someone else, as explained below.

**Route: Stage 5, Implement**
- **Skill:** `/check-against-bia`. You start it by typing its name. It compares your dispatch plan with the approved BIA and lists where they disagree: recovery times, resources, contacts, suppliers. It quotes both passages for each disagreement and names each document's owner, marked "proposed, to confirm". It only reports. It doesn't propose a replacement value or pick between two recovery times.
- **Unit to read:** [`units/stages/implement.md`](units/stages/implement.md). The skill uses its second Task choice (plan vs. approved BIA). Use [`units/prompts/review.md`](units/prompts/review.md) on any plan it flags.
- **Maturity level:** Level 3, Defined.
- **Gate:** each use case is written down with its prompt, sources, review point and limits. It has an owner, and all five self-check questions answer yes with evidence ([`units/levels.md`](units/levels.md)).
- **Effort:** about forty minutes.
- **Data rule:** [`units/data-rules.md`](units/data-rules.md). Classify the plan and the BIA before you attach them.

**Setting the plan's RTO to 8 hours**
That's the dispatch plan owner's change. The unit's one minimum control is that "no live plan can be changed without the owner's approval and the creation of a new version." The BIA activity owner decides separately whether their 8-hour figure stands.

So the order is:
1. Run `/check-against-bia`.
2. Put the RTO disagreement it reports to both owners.
3. If the plan owner agrees, they approve the 8-hour RTO and issue a new version of the plan.

For your audit trail, keep that new version with the owner's approval on record.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/stages/implement.md`
