# /ask-ai4bcm case 3, run3: Claude Code, guidance at 0bd09b1

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `9f62a2c0-2396-452c-bad4-ba813c90a524`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm teach me what an RTO is

**Reply (verbatim):**

I can point you to the right place, but this router doesn't do the teaching itself. Teaching is the job of **`/learn-bcm`**.

**Where to look:** "RTO" has its own row in [`units/glossary.md`](units/glossary.md) (line 30). The definition there is quoted from ISO 22301:2019, and the source is listed in [`units/references.md`](units/references.md).

**To learn it properly:** type **`/learn-bcm`** and ask for the **Analysis** stage. RTO belongs there, together with MTPD and RPO. That session teaches it and then tests you. The section to read is [`units/stages/analysis.md`](units/stages/analysis.md): it covers where the RTO sits in the BIA interview and how it relates to the MTPD, and it says that AI can test whether a proposed RTO fits the impact criteria but doesn't set it.

- **Maturity level:** 1 is enough, because you're learning a term and not working with your own records.
- **Gate:** an approved tool, with nothing confidential pasted in.
- **Effort:** about ten minutes for the glossary row, or one `/learn-bcm` session.
- **Data rule first:** check [`units/data-rules.md`](units/data-rules.md) before you add a real BIA or your organisation's recovery figures to the session.

**Next move:** once the term is clear and you want to apply it to a real activity, run **`/prepare-bia`** (Analysis stage, Level 2). It deliberately leaves the RTO field blank, because the activity owner sets that number in the interview, not the AI.
