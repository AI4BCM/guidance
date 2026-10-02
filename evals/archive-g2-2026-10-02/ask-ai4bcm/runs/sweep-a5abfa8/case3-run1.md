# ask-ai4bcm case3 run1: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /ask-ai4bcm teach me what an RTO is

**Reply (verbatim):**

This router points you to the right material. It doesn't teach, so I won't define RTO here.

**Run:** **`/learn-bcm`** with the topic "RTO". This is the skill that teaches: it covers one part of BCM practice per session, using this guidance and its open sources, and then checks that you understood. To start it, type `/learn-bcm teach me what an RTO is`.

**Read:** the **RTO** entry in [`units/glossary.md`](units/glossary.md), which is the single place the guidance defines its terms. Read the **MTPD** entry next to it as well, because the two terms only make sense together.

**Where it shows up in the work:** Stage 3, **Analysis**, in [`units/stages/analysis.md`](units/stages/analysis.md). In the pre-interview BIA draft (`/prepare-bia`), the recovery fields, including the RTO, are left **blank on purpose**. The activity owner sets the RTO, never the model. Once you've learned the term, this is where you'll meet it.

**Level:** 1, Learning. **Gate:** the tool is approved and nothing confidential goes in.

**Time:** one `/learn-bcm` session, roughly the ten minutes it takes to place yourself on the ladder, plus the test at the end.

**Data rule:** run [`units/data-rules.md`](units/data-rules.md) first. Learning the term uses only the guidance and public sources, so it needs none of your organisation's data. Don't paste a real BIA or recovery figures into the session to make it "concrete". Once pasted into the wrong tool, it can't be taken back.

**Next step:** you decide whether to start it. When you're ready, type `/learn-bcm`.
