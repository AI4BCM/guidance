# /ask-ai4bcm case 4b, run3: Claude Code, guidance at 0bd09b1

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `b39bab42-7c58-4e19-b1c9-00697cbd20d0`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** which unit and prompt fit a BIA interview?

**Reply (verbatim):**

For a BIA interview, use the **Analysis: Business Impact and Risk** unit (`units/stages/analysis.md`) together with the **BIA support** prompt (`units/prompts/bia.md`).

- **The unit** is the lifecycle-stage unit covering business impact analysis. It's the background for the interview itself.
- **The prompt** is the only one of the seven prompts written for BIA work. The other six cover drafting, awareness content, review, exercises, management reporting and evaluations.
- **Also read Data Rules** (`units/data-rules.md`) before you paste interview notes into a tool. The guidance puts it first because "what is pasted into the wrong tool cannot be unpasted," and BIA interview notes usually contain sensitive details.
- **For a critical reading of a draft BIA afterwards,** the **Review and challenge** prompt (`units/prompts/review.md`) is the one to use.

I matched these by title and path from the list of 21 units on your AI4BCM "Get the guidance" page. I couldn't open the unit files themselves, so I haven't checked whether `bia.md` is aimed at preparing for an interview, running one, or writing it up afterwards. If you point me at the units folder, I can check.

**Tool calls (stream-json):**

- Bash: `git ls-files | head -200 && git ls-files | wc -l`
- Bash: `find . -maxdepth 4 -not -path '*/node_modules*' | head -200`
- Bash: `ls -la /home/brain/.claude/projects/-tmp/memory/ 2>&1; cat /home/brain/.claude/projects/-tmp/memory/MEMORY.md 2>&1`
- Glob: `**/*`
- Artifact: ``
- Artifact: ``
- Artifact: ``
- Artifact: ``
- Artifact: ``
- Grep: `(?i)interview`
- Grep: `.{0,150}\bBIA\b.{0,150}`
- Artifact: ``
- Artifact: ``
- Grep: `(?i)(unit|prompt|BIA|impact analysis)`
- Bash: `cd /home/brain/.claude/projects/-tmp-claude-1001--opt-brain-172e68eb-beff-4eff-a578-707de5e8742d-scratchpad-g2-runs-ask-ai4bcm-4b-run3-work/b39bab42-7c58-4e19-b`
- Grep: `unit-list|<li|<h[1-4]|prompt`
- Grep: `unit-list|<li|<h[1-4]|BIA|interview`
- Read: `/home/brain/.claude/projects/-tmp-claude-1001--opt-brain-172e68eb-beff-4eff-a578-707de5e8742d-scratchpad-g2-runs-ask-ai4bcm-4b-run3-work/b39bab42-7c58-4e19-b1c9`
