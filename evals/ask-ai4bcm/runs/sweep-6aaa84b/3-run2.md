# /ask-ai4bcm case 3, run2: Claude Code, guidance at 6aaa84b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `758f7636-e556-4020-9e1c-4be1d5184714`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm teach me what an RTO is

**Reply (verbatim):**

This tool only points you to the right place. It doesn't teach. For a term like RTO, it gives you the glossary entry and the skill that does the teaching.

**The word:** [`units/glossary.md`](units/glossary.md), entry **RTO**:

> Recovery Time Objective: the time frame within the MTPD for resuming disrupted activities at a specified minimum acceptable capacity (ISO 22301:2019).

RTO depends on **MTPD** (Maximum Tolerable Period of Disruption), which has its own entry in the same glossary. MTPD is how long an activity can be down before the impact becomes unacceptable. The RTO has to fall inside that limit.

**To learn it, type `/learn-bcm`** and ask for the **Analysis** section, [`units/stages/analysis.md`](units/stages/analysis.md). That's where RTO is used: the business impact analysis (BIA) records an RTO for each IT system and application, and for each dependency between departments. It teaches one section per session and then tests you.

- **Level:** 1. You're only reading the guidance, so you don't need an approved tool for this part.
- **Effort:** about one session.
- **Data rule:** you don't need any of your own data to learn the term. If you later practise on real BIA records, read [`units/data-rules.md`](units/data-rules.md) first, because BIA material is the most sensitive data in BCM.

The guidance is firm on one point: **the activity owner sets the RTO**. AI can check whether a proposed RTO fits the impact criteria, but it doesn't set it.

The skill starts only when you type `/learn-bcm` yourself.
