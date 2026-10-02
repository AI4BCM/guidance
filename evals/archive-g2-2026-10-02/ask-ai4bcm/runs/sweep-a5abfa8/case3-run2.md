# ask-ai4bcm case3 run2: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /ask-ai4bcm teach me what an RTO is

**Reply (verbatim):**

I can point you to where to learn this, but I won't explain RTO here. Defining terms is the job of a different skill.

**Route: the word is the problem, not the process**

- **Read:** the **RTO** entry in [`units/glossary.md`](units/glossary.md). It sits next to **MTPD** and **BIA**, which you'll need alongside it. If the units didn't come with your install, read it at github.com/AI4BCM/guidance under `units/glossary.md`.
- **Skill:** **`/learn-bcm`**. Type it with "RTO" as the topic. It teaches one part of BCM from this guidance and its open sources, then tests whether you understood. I only route you there.
- **Where RTO shows up:** Stage 3, **Analysis** ([`units/stages/analysis.md`](units/stages/analysis.md)). In the pre-interview BIA draft (**`/prepare-bia`**), the recovery fields, including RTO, **stay blank on purpose**. A model doesn't set a recovery time. The activity owner does.
- **Level:** 1 is enough. **Gate:** the tool is approved and nothing confidential goes in. Learning a term only uses public guidance.
- **Time:** about ten minutes for the glossary entry, or one `/learn-bcm` session.
- **Data rule:** [`units/data-rules.md`](units/data-rules.md) comes first. Learning the term needs none of your organisation's data. If you later want to test it against your own RTO figures or BIA records, classify them before pasting them anywhere.

**After that:** once you know the term and want to use it on real activities, take the Analysis route with **`/prepare-bia`**. The owner of each activity decides its RTO.
