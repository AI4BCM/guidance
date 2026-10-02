# ask-ai4bcm case3 run3: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /ask-ai4bcm teach me what an RTO is

**Reply (verbatim):**

You asked to be taught, and this router doesn't teach. It points you to the right place and stops, so here is the route rather than a definition.

**Skill:** type **`/learn-bcm`** and ask for RTO. It teaches one part of the practice per session, using this guidance and its open sources, and then tests you. That check is what you're asking for. I can't start it for you; it runs only when you type its name.

**Unit:** if you only need to look the word up, the **RTO** entry is in [`units/glossary.md`](units/glossary.md). The **MTPD** and **BIA** entries are in the same file. RTO is set inside the BIA and sits under the MTPD, so read all three together. To see where an RTO comes from in practice, the next step is Stage 3, Analysis, in [`units/stages/analysis.md`](units/stages/analysis.md). There the recovery fields stay blank in the AI draft, and the activity owner sets the RTO.

**Level and gate:** this is Level 1 or 2. Learning a term uses only published guidance and needs no connector. The gate is that the tool you use is approved and nothing confidential goes into it.

**Effort:** one `/learn-bcm` session, roughly ten to twenty minutes including the test.

**Data rule:** classify first, using [`units/data-rules.md`](units/data-rules.md). Ask about RTO in general terms. Don't paste your organisation's real recovery times or BIA records as examples. Those are among the most sensitive material in BCM, and once they're pasted into the wrong tool you can't take them back.

**Next move:** after `/learn-bcm`, you decide whether you understood it. If you then want to work on real RTOs, take the Stage 3 route with **`/prepare-bia`**.
