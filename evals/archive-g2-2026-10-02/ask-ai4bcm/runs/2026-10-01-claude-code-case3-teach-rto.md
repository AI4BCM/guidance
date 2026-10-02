# ask-ai4bcm case3-teach-rto: Claude Code 2.1.284, 2026-10-01

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /ask-ai4bcm teach me what an RTO is

**Reply (verbatim):**

I can point you to the right place, but this command doesn't teach. To be taught and tested on RTO, type **`/learn-bcm`**.

**The word.** [`units/glossary.md`](units/glossary.md) defines it in one line:

> **RTO**: Recovery Time Objective; the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity (ISO 22301:2019).

That definition uses a second term, MTPD, which has its own entry in the same file. Read that one too, because the RTO only makes sense next to it.

**The skill.** **`/learn-bcm`** teaches one part of the practice per session, using this guidance and its open sources, then checks that you understood. Ask it about RTO and it will explain it and test you.

**The unit.** RTOs are set during Stage 3, Analysis: [`units/stages/analysis.md`](units/stages/analysis.md). In the BIA prompt [`units/prompts/bia.md`](units/prompts/bia.md), the recovery fields are left blank on purpose. An RTO is a decision the activity owner makes, and a model never proposes one.

**Level and gate.** Level 1 or 2. The gate is that the tool you use is approved and nothing confidential goes into it. Learning a definition from published guidance passes easily, but it stops passing if you paste in your organisation's own RTOs to "check" them.

**Time.** Ten minutes for the glossary entry, or one `/learn-bcm` session.

**Data rule.** [`units/data-rules.md`](units/data-rules.md) applies before anything else. Generic questions about RTO are fine. Real RTOs, BIA records or recovery figures are among the most sensitive material in BCM, so classify them before they go into any tool.

**Next step.** No owner decision is needed, because nothing has been drafted yet. If you go on to work with real RTOs, you'll be in the Analysis stage route, starting with **`/prepare-bia`**.
