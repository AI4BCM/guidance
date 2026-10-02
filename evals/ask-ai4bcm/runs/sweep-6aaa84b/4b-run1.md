# /ask-ai4bcm case 4b, run1: Claude Code, guidance at 6aaa84b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `30f9831f-8e1d-4e9c-a196-be431741d5a1`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** which unit and prompt fit a BIA interview?

**Reply (verbatim):**

For a BIA interview, use the **Analysis: Business Impact and Risk** unit (`units/stages/analysis.md`) with the **BIA support** prompt (`units/prompts/bia.md`).

- **Unit:** `analysis.md` is the lifecycle stage that covers business impact analysis. It's the only one of the six stage units that does.
- **Prompt:** `bia.md` is the only BIA prompt in the library. The others are for drafting, awareness content, review and challenge, exercise scenarios and management reporting.
- **Optional next step:** after the interview, you could run your notes or draft BIA through **Review and challenge** (`units/prompts/review.md`) to test it.

I found these in the unit list on your "Get the guidance" page (the AI4BCM guideline download). I only saw the titles and file paths, not what's inside the files. So I haven't checked whether `bia.md` is written for running the interview itself, or for preparing questions and processing the answers.

**Tool calls (stream-json):**

- Bash: `git ls-files | head -100 && git ls-files | wc -l`
- Bash: `find . -maxdepth 4 -not -path '*/node_modules*' -not -path '*/.git/*' | head -200`
- ToolSearch: ``
- mcp__claude_ai_Google_Drive__search_files: ``
- mcp__claude_ai_Microsoft_365__sharepoint_search: ``
- Bash: `ls -la /home/brain/.claude/projects/-tmp/memory/ 2>&1; cat /home/brain/.claude/projects/-tmp/memory/MEMORY.md 2>&1 | head -50`
- Artifact: ``
- Artifact: ``
- Artifact: ``
- Grep: `BIA|[Ii]nterview`
- Read: `/home/brain/.claude/projects/-tmp-claude-1001--opt-brain-172e68eb-beff-4eff-a578-707de5e8742d-scratchpad-g2-runs-ask-ai4bcm-4b-run1-work/30f9831f-8e1d-4e9c-a196`
