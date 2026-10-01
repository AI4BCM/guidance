# ask-ai4bcm case2 run2: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /ask-ai4bcm should I use challenge-my-plan or red-team-assumptions on our recovery option paper that the steering group already likes?

**Reply (verbatim):**

**Use `/red-team-assumptions`.** Your steering group already likes the option, and that is the case red-team is for. It reads the paper and returns everything the option silently relies on in one reply, with the check that would settle each assumption. `/challenge-my-plan` questions the owner one round at a time and waits for their answer each time. That suits a draft whose owner still has the thinking to do. It doesn't suit an option the room has already settled on.

- **Stage:** 4, Design (choosing continuity solutions).
- **Read:** [`units/stages/design.md`](units/stages/design.md) and [`units/prompts/review.md`](units/prompts/review.md).
- **Maturity level:** Level 3, Defined.
- **Gate:** red-team needs both your risk and dependency registers, searchable in one place with access by role, and the use case written down. A single register usually won't show the finding. The case in the guidance is one shipping company quietly serving both sites, which only appears when both registers are read together. If your registers aren't in one place yet, the run will look complete but can't find that kind of dependency.
- **Effort:** an afternoon, once both registers are in one place.
- **Data rule, before anything else:** classify the option paper and the registers under [`units/data-rules.md`](units/data-rules.md) before any of it goes into a tool. Whatever you paste into the wrong tool stays there.

**After the draft:** the list of assumptions goes to the person who owns the option, and they decide which checks to run. Two follow-ups, if you need them:
- `/challenge-my-plan` on your own cover note before you send it to the steering group.
- `/check-against-bia` on the recovery plan once it's built from the chosen option. That's stage 5, Implement.

Type `/red-team-assumptions` to start it. This router doesn't run it.
