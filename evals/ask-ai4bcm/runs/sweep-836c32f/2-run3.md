# /ask-ai4bcm case 2, run3: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `b0815f48-f5c1-493e-b305-f658c3ce10f4`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

I'm only routing here: I won't run the skill and I won't change the plan.

**The skill: `/check-against-bia`** (Stage 5, Implement)
- **What it does:** compares your dispatch plan with the approved BIA. It lists each place they disagree (recovery time, resources, contacts, suppliers), quotes both passages, and names the owner of each document, marked "proposed, to confirm". It is a report only: it picks neither recovery time, proposes no replacement value and changes nothing.
- **What to read:** [`units/stages/implement.md`](units/stages/implement.md) (its prompt, second Task choice) and [`units/prompts/review.md`](units/prompts/review.md) for each plan it flags.
- **Maturity level:** Level 3, Defined.
- **Gate:** Level 3's. Each use case is written down with its prompt, sources, review point and limits. It has an owner. All five self-check questions answer yes, with evidence.
- **Effort:** about forty minutes.
- **Data rule:** check [`units/data-rules.md`](units/data-rules.md) before anything else. Classify the plan and the BIA, and use only a tool approved for that class.

The skill starts only when you type `/check-against-bia` yourself.

**Changing the RTO to 8 hours:** this decision belongs to the plan owner, not to you, me or the skill. The unit's one control is: "no live plan can be changed without the owner's approval and the creation of a new version." The check will show the dispatch plan's RTO next to the BIA's 8 hours and name the plan owner and the BIA activity owner. Each of them then decides whether their document changes. If the plan moves to 8 hours, it does so as a new version with the plan owner's approval. If the plan's figure turns out to be right, the BIA changes instead, through its own owner.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/stages/implement.md`
