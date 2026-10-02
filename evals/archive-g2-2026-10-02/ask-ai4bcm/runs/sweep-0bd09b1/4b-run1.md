# /ask-ai4bcm case 4b, run1: Claude Code, guidance at 0bd09b1

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c17fe583-77ad-44b6-bbe1-3a9f729c7199`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** which unit and prompt fit a BIA interview?

**Reply (verbatim):**

For a BIA interview, use these two from the AI4BCM guideline:

- **Unit:** *Analysis: Business Impact and Risk*, at `units/stages/analysis.md`. This is the stage unit that covers the BIA.
- **Prompt:** *BIA support*, at `units/prompts/bia.md`. It's the only prompt in the set aimed at the BIA.

If you want a second pass on what comes out of the interview, *Review and challenge* (`units/prompts/review.md`) would also fit.

I found these in the unit list on your published "Get the guidance" page. That page only lists titles and file paths. I couldn't open the unit or prompt files themselves, so I can't confirm they include interview questions specifically, as opposed to BIA support in general. If you point me to the `units/` folder, I can check `bia.md` and pull out the interview part.

**Tool calls (stream-json):**

- Bash: `git ls-files | head -100 && ls -la`
- ToolSearch: ``
- Artifact: ``
- mcp__claude_ai_Google_Drive__search_files: ``
- Artifact: ``
- Bash: `F=/home/brain/.claude/projects/-tmp-claude-1001--opt-brain-172e68eb-beff-4eff-a578-707de5e8742d-scratchpad-g2-runs-ask-ai4bcm-4b-run1-work/c17fe583-77ad-44b6-bb`
- Grep: `BIA|[Ii]nterview`
- Read: `/home/brain/.claude/projects/-tmp-claude-1001--opt-brain-172e68eb-beff-4eff-a578-707de5e8742d-scratchpad-g2-runs-ask-ai4bcm-4b-run1-work/c17fe583-77ad-44b6-bbe1`
