# /ask-ai4bcm case 3, run1: Claude Code, guidance at 6aaa84b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `b1ded980-447e-4cb8-a825-c6552f37978b`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm teach me what an RTO is

**Reply (verbatim):**

RTO is a vocabulary question, so this router points you to the definition and to the skill that teaches it. It doesn't do the teaching itself.

**The definition:** [`units/glossary.md`](units/glossary.md), line 30:

> **RTO**: Recovery Time Objective. The time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity (ISO 22301:2019).

In practice this means two things:
- The RTO always sits inside the MTPD (Maximum Tolerable Period of Disruption, which has its own glossary entry). The MTPD is the point where the damage can no longer be accepted. The RTO is the earlier target you set so that you resume before you reach it.
- The RTO covers getting back to a **minimum acceptable capacity**, not to full normal operation.

**To learn it properly:** type **`/learn-bcm`**. It teaches one part of the practice per session and then tests you. Ask it for the Analysis stage (stage 3), because RTOs are set in the business impact analysis (BIA). For background reading first, see [`units/stages/analysis.md`](units/stages/analysis.md).

**Data rule:** learning the concept doesn't need any of your organisation's material. If you later bring real BIA figures into a session, check [`units/data-rules.md`](units/data-rules.md) first. BIA data is the most sensitive material in BCM.

**Next move:** once you're working with real RTOs, that's stage 3. The route there is **`/prepare-bia`**, which needs Level 2 and has this gate: approved tools, a written data rule and a named reviewer.
