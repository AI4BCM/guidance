# /ask-ai4bcm case 2, run2: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `19cd78a8-b7e5-47ca-bf67-68bdf7c78a5a`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

The skill you want is **`/check-against-bia`**. It belongs to stage 5, Implement. I'm not running it from here, and I'm not changing the RTO. It starts when you type `/check-against-bia` yourself.

**Changing the RTO to 8 hours isn't a change I or the skill can make for you.** The unit's one rule is: *"no live plan can be changed without the owner's approval and the creation of a new version."* The skill only reports. It quotes the plan's recovery time next to the BIA's, names the owner of each document, and marks each line "proposed, to confirm". It doesn't choose between the two recovery times. If the dispatch plan and the BIA disagree:

- The **dispatch plan's owner** decides whether the plan changes to 8 hours. If it does, they approve it and issue a new version.
- The **BIA activity owner** confirms that the 8 hours is current. If the 8 hours turns out to be wrong, the BIA changes, not the plan.

**Route**
- **What to read:** `units/stages/implement.md` (Method and Prompts, Task choice 2), with `units/prompts/review.md` for any plan it flags.
- **Maturity level:** Level 3, Defined.
- **Gate:** you can retrieve over the approved plans in a way that can be audited, and the use case is written down.
- **Effort:** about forty minutes.
- **Data rule:** check `units/data-rules.md` first. The dispatch plan and the BIA output can only go into a tool approved to hold them.

Give the skill the dispatch plan, the approved BIA output and the requirements register. If the BIA isn't the approved version, the skill lists it under Gaps and doesn't treat it as current.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/stages/implement.md`
