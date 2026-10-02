# ask-ai4bcm case2 run3: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /ask-ai4bcm should I use challenge-my-plan or red-team-assumptions on our recovery option paper that the steering group already likes?

**Reply (verbatim):**

# Use `/red-team-assumptions`

The test that separates the two skills is this. `/challenge-my-plan` interviews you one round at a time and waits for your answer before it moves on. `/red-team-assumptions` reads the paper and returns the whole list in one reply. Use challenge when the owner should do the thinking. Use red-team when the room already likes the option, which is your situation. When a steering group likes an option, its assumptions have usually stopped being questioned, and red-team is built to surface those.

- **Stage:** 4, Design. Read [`units/stages/design.md`](units/stages/design.md) and use [`units/prompts/review.md`](units/prompts/review.md).
- **Skill:** type **`/red-team-assumptions`** yourself; this router doesn't start it. It returns a draft in the chat: what the paper silently relies on, and the check that would settle each item. It writes nothing anywhere.
- **Level:** 3, Defined. **Gate:** retrieval across **both** registers, with role-based access and a documented use case. You can run the skill on the paper alone, but the important finding often isn't in one register. The guidance's example is one shipping company quietly serving both sites.
- **Effort:** an afternoon, once both registers are in one place.
- **Data rule:** check [`units/data-rules.md`](units/data-rules.md) first. Recovery options often reveal dependencies and weak points, so decide which tool the paper may go into before you paste it anywhere.

**After the draft:**
- **The owner decides.** Each assumption on the list goes to the person who owns that check. It is a question to settle, not a finding yet.
- **Use `/challenge-my-plan` later, if at all.** It fits once you are revising the paper yourself and want to test your own reasoning before it goes back to the steering group.
- **Then `/check-against-bia` (stage 5)** on the plan built from whichever option is finally chosen.
