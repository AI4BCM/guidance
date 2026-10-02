# /ask-ai4bcm case 2, run1: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `d8c68d70-5c53-49e2-b6cc-3051a9592eb8`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

You want **`/check-against-bia`**. I didn't run it or change the RTO. This guide only points you to the right skill. The skill starts when you type its name, and the RTO change is a decision for the plan's owner.

**The route: Stage 5, Implement**
- **Read:** `units/stages/implement.md`, and run `units/prompts/review.md` on any plan the check flags.
- **What it does:** it compares your dispatch plan with the approved BIA and lists where they disagree, such as the recovery time, resources, contacts or suppliers. It quotes both passages and names each document's owner, marked "proposed, to confirm". It doesn't change the plan or the BIA, and it doesn't pick between two recovery times.
- **Maturity level:** Level 3, Defined.
- **Gate:** retrieval over the approved plans that can be audited, and a written use case.
- **Effort:** about forty minutes.
- **Data rule:** check `units/data-rules.md` first. BIA data and recovery strategies are high-sensitivity, so use only an approved corporate or private environment.

**Setting the RTO to 8 hours**
The plan's owner has to make this change. The unit's one control is: "no live plan can be changed without the owner's approval and the creation of a new version." The BIA activity owner also has to confirm that 8 hours is the approved value. If the check shows the plan and BIA disagree on RTO, it gives you both passages and both owners. From there:
1. The dispatch plan owner decides whether to adopt 8 hours and approves it.
2. The change goes into a new version of the plan, with the approval on record for the auditor.
3. The team that uses the plan confirms the change is realistic for them.

To start, type `/check-against-bia` and attach the dispatch plan, the approved BIA output and the requirements register.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/stages/implement.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/data-rules.md`
