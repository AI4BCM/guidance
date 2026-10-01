# ask-ai4bcm case2-challenge-or-red-team: Claude Code 2.1.284, 2026-10-01

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /ask-ai4bcm should I use challenge-my-plan or red-team-assumptions on our recovery option paper that the steering group already likes?

**Reply (verbatim):**

# Use `/red-team-assumptions`

The steering group already likes this option, and that is the case `/red-team-assumptions` is built for. It reads the whole option paper and returns everything the paper silently relies on in a single reply, with the check that would settle each assumption.

`/challenge-my-plan` works differently. It interviews the plan's owner one round at a time and waits for an answer before giving its own view, so it fits when you want the owner to do the thinking. When the room has already agreed, what's missing is the list of assumptions nobody has checked.

| | |
|---|---|
| **Skill** | `/red-team-assumptions`, which you type yourself. This router doesn't run it. |
| **Read** | [`units/stages/design.md`](units/stages/design.md) and [`units/prompts/review.md`](units/prompts/review.md). This is Stage 4, Design. |
| **Level** | 3, Defined |
| **Gate** | You need retrieval across **both** registers (e.g. your requirements and your suppliers), with role-based access and a documented use case. A single register won't show the finding the stage is built around. That example is one shipping company quietly serving both sites. Without both registers in one place, the red-team can only check the paper against itself. |
| **Time** | An afternoon, and only once both registers are in one place. |
| **Data rule first** | Classify the paper and the registers using [`units/data-rules.md`](units/data-rules.md) before anything goes into a tool. Recovery options and supplier dependencies are usually confidential. Anything pasted into the wrong tool can't be taken back. |

**After the red-team:**
- **The owner decides.** Each assumption on the list goes to the option's owner to confirm or disprove. A model's list is not a finding.
- **Then use `/challenge-my-plan` if it helps.** It's useful on the revised paper before it goes back to the steering group.
- **Once an option is chosen**, run `/check-against-bia` on the plan built from it. That's Stage 5, Implement.
