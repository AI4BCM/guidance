# ask-ai4bcm case3-teach-rto, final round (f05ad10), Claude Code 2.1.284, 2026-10-01

No files. Guidance repo at f05ad10. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`.

## Turn 1

Session `040cfbc1-6c65-452e-8aa6-49cd7c8d8f0c`. Request:

```text
/ask-ai4bcm teach me what an RTO is
```

Final text:

`````markdown
I can't teach it here. This command only points you to the right place and stops. Teaching a term and checking that you understood it is what `/learn-bcm` does.

- **Skill:** type **`/learn-bcm`** and ask for RTO. It teaches one part of BCM practice per session, using this guidance and its open sources, and then tests you.
- **Unit to read:** `units/glossary.md`, entry **RTO**. Read **MTPD** next to it, because an RTO is defined against the MTPD. If you need the source the definition comes from, it's in `units/references.md`.
- **Where you'll use it:** stage 3, Analysis (`units/stages/analysis.md` and `units/prompts/bia.md`). That's where an RTO gets set, and `/prepare-bia` leaves the recovery fields empty on purpose. **The activity owner sets the RTO, not the model.**
- **Level:** 1 or 2. **Gate:** the tool you use is approved, and nothing confidential goes in. Learning a term doesn't need any of your organisation's records.
- **Time:** one `/learn-bcm` session.
- **Data rule:** read `units/data-rules.md` first. If you try the term out on one of your real activities, check its class before you paste anything about it.

**Next step:** type `/learn-bcm`. The decision you're learning about, which RTO a given activity gets, still belongs to its owner.
`````
