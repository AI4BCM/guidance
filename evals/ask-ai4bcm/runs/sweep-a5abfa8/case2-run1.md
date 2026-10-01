# ask-ai4bcm case2 run1: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /ask-ai4bcm should I use challenge-my-plan or red-team-assumptions on our recovery option paper that the steering group already likes?

**Reply (verbatim):**

Use **`/red-team-assumptions`**.

The two skills differ in one way. `/challenge-my-plan` questions you one round at a time and waits for your answer each time, so it fits when the plan's owner should do the thinking. `/red-team-assumptions` reads the paper and returns everything it silently relies on in one reply, with the check that would settle each item. When the room already likes the option, the problem is the room's shared assumptions. Answering questions yourself won't bring those out. A full list will.

- **Stage:** 4, Design. Read [`units/stages/design.md`](units/stages/design.md) and [`units/prompts/review.md`](units/prompts/review.md).
- **Level:** 3, Defined.
- **Gate:** retrieval must cover **both** registers (for example, your own and the other site's or supplier's), with role-based access and a written-down use case. One register alone doesn't hold the finding. In the guidance's worked example, that finding was one shipping company quietly serving both sites. If your registers aren't in one place yet, the run gives you a list of questions, not findings.
- **Time:** an afternoon, once both registers are in one place.
- **Data rule, first:** classify the paper and the registers using [`units/data-rules.md`](units/data-rules.md) before anything goes into a tool. Recovery options and dependency registers are usually sensitive, and what goes into the wrong tool can't be taken back.

**After the draft:** the red-team list goes to the paper's owner, and they decide which assumptions to check. A person turns an assumption into a finding, not the model. Once an option is chosen and built into a plan, `/check-against-bia` is the next skill to read it. If the owner then reworks the paper before it goes back to the steering group, that's the moment to run `/challenge-my-plan`.

To start, type `/red-team-assumptions`. I only point you to it and won't run it.
