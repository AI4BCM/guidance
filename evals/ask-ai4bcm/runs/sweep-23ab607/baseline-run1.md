# ask-ai4bcm baseline (no skill loaded), run1: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `07abab9f-cfde-49d0-82ba-44b66ddfb0ad`.

Files in the working folder: none.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** I have to prepare a BIA interview with our dispatch lead next week. Which section, prompt and maturity level of the AI4BCM guidance fit, and what data rule applies?

**Reply (verbatim):**

I couldn't find the AI4BCM guidance, so I can't tell you which section, prompt, maturity level or data rule applies.

- **Working directory:** it's empty. There's no guidance document and no git repo in it.
- **Local search:** the only files mentioning "AI4BCM" near here are this session's own request logs, not the guidance itself.
- **Web search and broader filesystem search:** both were blocked by the current permission mode ("don't ask"), so I couldn't look further.

I'd rather not guess. Made-up section names or maturity levels would be worse than no answer when you're preparing a real BIA (business impact analysis) interview.

Any of these would let me give you a precise answer:
1. **Put the AI4BCM document in the working directory** (PDF, Markdown or similar), or give me its path, and I'll find the section, prompt, maturity level and data rule.
2. **Paste the relevant parts** here, such as the table of contents, the prompt library and the data-handling rules.
3. **Allow web search or fetch** (or give me a URL), if the guidance is published online.

Until then, some general points hold for a BIA interview with a dispatch lead whatever the framework:
- **What to cover:** the critical dispatch processes, the maximum tolerable downtime, recovery time and recovery point objectives, dependencies (CAD/telephony, radio, staff, suppliers), peak periods and workarounds.
- **Data:** frameworks like this usually require that you don't put personal data, caller or incident details, or confidential operational data into an AI tool. Anonymise or use placeholder data, and keep a human reviewing the output. Check that against the actual rule in AI4BCM once I can see it.

**Tool calls (stream-json):**

- Bash: `git ls-files | head -100 && ls -la`
- Bash: `grep -rli "ai4bcm" ~ /opt /tmp/claude-1001 2>/dev/null | grep -v "/runs/" | head -20`
- Grep: `(?i)ai4bcm`
- ToolSearch: ``
- WebSearch: ``
