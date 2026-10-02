# /ask-ai4bcm case 3, run1: Claude Code, guidance at 0bd09b1

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `eb7e04b1-7a0a-4a0e-aba9-acf84b544865`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm teach me what an RTO is

**Reply (verbatim):**

This router points you to the right place but doesn't teach. To learn what an RTO is, use these:

- **Skill:** type **`/learn-bcm`** to run it. It teaches one part of the practice per session and then tests you. Ask it for the RTO, starting from the Analysis stage, because that's where the business impact analysis (BIA) sets RTOs.
- **Unit to read:** the **RTO** entry in [`units/glossary.md`](units/glossary.md) (line 30). It points to MTPD, which you'll need alongside it. After that, read [`units/stages/analysis.md`](units/stages/analysis.md) to see where the RTO is used in practice.
- **Level:** 1. **Gate:** an approved tool, with nothing confidential put into it.
- **Effort:** one `/learn-bcm` session.
- **Data rule:** [`units/data-rules.md`](units/data-rules.md) applies first. Learning the term needs none of your own records. If you want to practise on a real activity's recovery figures, those come from your BIAs, which are among the most sensitive material in BCM. Check the data rules before you paste any of them anywhere.

**Next step:** you type `/learn-bcm`. If you then want to set RTOs for real, that's Stage 3 (Analysis), with **`/prepare-bia`**.
