# /ask-ai4bcm case 3, run2: Claude Code, guidance at 0bd09b1

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `66a86d79-4258-4cab-8fc3-8cfb93389caa`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm teach me what an RTO is

**Reply (verbatim):**

I can point you to where RTO is covered, but this router doesn't teach. `/learn-bcm` does.

- **Read:** the **RTO** entry in [`units/glossary.md`](units/glossary.md) (line 30). It comes from ISO 22301:2019, and that standard is listed in [`units/references.md`](units/references.md).
- **To learn it:** type **`/learn-bcm`** and ask for RTO. It teaches one part of BCM per session and then tests you. Ask it to cover MTPD (maximum tolerable period of disruption) in the same session, because the glossary defines RTO in relation to MTPD.
- **Where RTO is used in practice:** Stage 3, Analysis ([`units/stages/analysis.md`](units/stages/analysis.md)). That's the business impact analysis (BIA) stage, where RTOs get set.
- **Level and gate:** Level 1. The only condition is an approved tool, and learning a term involves no organisational data.
- **Effort:** about ten minutes for the glossary entry, or one `/learn-bcm` session.
- **Data rule:** check [`units/data-rules.md`](units/data-rules.md) first. Don't paste your organisation's real RTOs or BIA records into the session. Use made-up examples.

**Next step:** read the glossary entry, then type `/learn-bcm` if you want it explained and tested.
