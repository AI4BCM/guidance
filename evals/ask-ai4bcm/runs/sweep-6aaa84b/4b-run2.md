# /ask-ai4bcm case 4b, run2: Claude Code, guidance at 6aaa84b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a9b9b5e5-d972-49cf-84e6-8d1311f347fe`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** which unit and prompt fit a BIA interview?

**Reply (verbatim):**

I couldn't find the units and prompts you mean, so I can't name the right ones yet. The working folder is empty. Shell and Google Drive access are both blocked in the current permission mode, so I haven't searched your files for a BIA (business impact analysis) unit or a prompt library.

To get you a real answer, either:
- **Tell me where they are:** paste the list of units and prompts, give me a file path, or share a Drive or claude.ai link.
- **Or allow Google Drive search** (or Bash) and I'll look for them myself.

If it helps while you check: a BIA interview usually belongs in the unit on **business impact analysis / identifying critical processes**. The prompt that fits best is one that generates or structures a **process-owner interview**. It should cover:
- what the process does and what it depends on (people, IT systems, suppliers, sites)
- how the impact grows over time if it stops (money, legal or contractual, reputation, customers), e.g. at 4h, 1 day, 3 days and 1 week
- how long it can be down (MTPD, the maximum tolerable period of disruption), the recovery time objective (RTO) and the recovery point objective (RPO)
- the minimum level it has to keep running at, any manual workarounds, and the busiest times of the year

Once I can see your material, I'll match this to the specific unit and prompt.

**Tool calls (stream-json):**

- Bash: `cd /tmp/claude-1001/-opt-brain-172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/ask-ai4bcm/4b/run2/work 2>/dev/null || pwd; git ls-files | head -200; ls `
- Glob: `**/*`
- Grep: `BIA|business impact`
- Glob: `**/*`
- ToolSearch: ``
- mcp__claude_ai_Google_Drive__search_files: ``
