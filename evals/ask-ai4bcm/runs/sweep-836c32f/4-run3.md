# /ask-ai4bcm case 4, run3: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `5733a746-f54f-4b24-913c-421bc78833e7`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

Your request has two parts, and each one has its own route. Before either, you need to classify the notes.

**First, classify the notes** ([`units/data-rules.md`](units/data-rules.md)). Debrief notes usually name people, and they often record weaknesses found during the exercise. Both count as high-sensitivity, so the notes can only go into an approved corporate or private environment. You also need to be able to say where the data goes and how long it is kept. If you can't, don't paste them in yet.

**1. Now: this tabletop's notes become findings and actions (Stage 6, Validate)**
- **Skill:** **`/debrief-to-action`**. It turns one exercise's notes into proposed findings. Each finding is tied to the objective it missed and has a proposed owner. It starts only when you type its name.
- **Read:** [`units/stages/validate.md`](units/stages/validate.md) and [`units/prompts/exercise.md`](units/prompts/exercise.md)
- **Maturity level:** Level 2, Repeatable
- **Gate (Level 2):** "the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route"
- **Effort:** forty minutes
- **Data:** debriefs name people, so the rule above applies.
- **After the draft:** it is a draft for the owners it proposes. Your reviewer checks it, and then it goes through your normal approval route.

**2. Later: turning your prompt into a skill of your own (on-ramp "I want a skill of our own")**
- **Read:** [`units/prompts/README.md`](units/prompts/README.md), section "Build your own skill: four steps". Step 2 decides where the skill may run (see the tool permissions in [`units/data-rules.md`](units/data-rules.md)). There is no separate prompt file: the pattern of the prompt you already use is the template.
- **Skill:** **`/check-my-ai-tool`** drafts the skill's card ([`units/keep-it-running.md`](units/keep-it-running.md)). It starts only when you type its name.
- **Maturity level:** Level 2, "as soon as a prompt becomes a team method", with Level 2's gate as above. If the skill ever reads connected records, it moves to Level 3. The Level 3 gate: "each use case is written down with its prompt, sources, review point and limits", the use case has an owner, and all five self-check questions answer yes with evidence. That record goes on the skill's card.
- **Effort:** an afternoon
- **Data:** [`units/data-rules.md`](units/data-rules.md)

Doing them in this order works well. Once you've used the prompt on this debrief and it has been through review, it counts as "the prompt that worked", saved for reuse, and that is what step 2 turns into a skill.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/data-rules.md`
