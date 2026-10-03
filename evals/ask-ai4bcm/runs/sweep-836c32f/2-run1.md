# /ask-ai4bcm case 2, run1: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `3c42fd88-8101-49d3-90ed-d7056569fbef`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

The skill is **`/check-against-bia`**. I can't run it for you or change the plan's RTO. It starts only when you type it yourself, and the 8-hour change belongs to the plan's owner, not to you or me.

**Route: Stage 5, Implement**
- **Skill:** **`/check-against-bia`** compares a plan, or a coming change, against the BIA. It lists every place they disagree, each with a proposed owner. Type `/check-against-bia` to start it.
- **Read:** [`units/stages/implement.md`](units/stages/implement.md) and [`units/prompts/review.md`](units/prompts/review.md).
- **Maturity level:** Level 3, Defined.
- **Gate (Level 3's):** each use case is written down with its prompt, sources, review point and limits. It has an owner. All five self-check questions answer yes, with evidence.
- **Effort:** about forty minutes.
- **Data rule:** first classify the dispatch plan and the BIA against [`units/data-rules.md`](units/data-rules.md). Do this before either goes into any tool.

**The RTO change.** This is the plan owner's change, not yours or mine. The Implement unit's one control is: *"no live plan can be changed without the owner's approval and the creation of a new version."* If `/check-against-bia` finds a gap between the plan's RTO and the BIA's 8 hours, it lists that gap as a proposed finding for the owner. The owner decides, approves the change and issues a new version of the plan. Check that the 8 hours comes from the approved version of the BIA, because the skill won't treat a draft as current.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units && grep -n -i -E "owner|version|RTO" stages/implement.md | head -40`
- Grep: `(?i)owner|version|RTO`
