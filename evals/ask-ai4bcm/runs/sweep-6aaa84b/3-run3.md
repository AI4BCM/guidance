# /ask-ai4bcm case 3, run3: Claude Code, guidance at 6aaa84b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `7eb315ab-8af1-4dfd-bed6-cc0a4a3c8207`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm teach me what an RTO is

**Reply (verbatim):**

You're asking about a term, so this router gives you the glossary entry and sends you to the skill that does the teaching.

**The entry:** the **RTO** row in [`units/glossary.md`](units/glossary.md) (line 30) defines it as:

> Recovery Time Objective: the time frame within the MTPD (Maximum Tolerable Period of Disruption) for resuming disrupted activities at a specified minimum acceptable capacity (ISO 22301:2019).

**To learn it, type `/learn-bcm`.** Each session covers one part of the practice and then tests you. Ask it for business impact analysis, the part where RTO is set alongside MTPD. Nothing starts until you type the command.

- **Where it's used:** stage 3, Analysis. See [`units/stages/analysis.md`](units/stages/analysis.md).
- **Maturity level:** 1. The gate is an approved tool with nothing confidential pasted in. Learning the concept needs no organisational data.
- **Effort:** one `/learn-bcm` session.
- **Data rule:** check [`units/data-rules.md`](units/data-rules.md) first. Use generic examples, not your own BIA figures.

**Next move:** once you know the term and want to set RTOs for real activities, use **`/prepare-bia`** before each interview. That's level 2, and its gate is a saved prompt, approved tools, a written data rule and a named reviewer.
