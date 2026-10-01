# ask-ai4bcm case4b run2: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** which unit and prompt fit a BIA interview?

**Reply (verbatim):**

I couldn't find any units or prompts to choose from. This working directory is empty, and I wasn't allowed to run shell commands or search your Google Drive. I'm guessing you mean an AI4BCM course or prompt library, but I haven't seen it, so I can't tell you which unit fits.

To get an exact answer, do one of these:
- paste the list of units and prompts here, or
- give me the file path or Drive link, or
- allow Drive search, and I'll look for "AI4BCM".

**In the meantime, here's what to look for.** A BIA interview fits a unit about the **Business Impact Analysis / analysis phase**, usually right after scoping and before risk assessment or strategy. Inside it, pick the prompt that **prepares for or runs an interview with a process owner**. Skip prompts that summarize a finished BIA or calculate recovery targets. Use them after the interview.

**If your material has no such prompt, you can start from this one:**

> You are a business continuity consultant preparing a BIA interview with the owner of the process **[process name]** in **[department]**. Draft a 45-minute interview guide covering:
> 1. What the process does, its outputs, and who receives them
> 2. Busy periods and deadlines
> 3. How impact grows over time (4h / 1d / 3d / 1w / 2w): financial, legal or regulatory, customer, reputational, and safety
> 4. MTPD (maximum tolerable period of disruption), RTO (recovery time objective), and RPO (how much data loss is acceptable), with the reasoning behind each
> 5. What the process depends on: people and key skills, IT systems and data, suppliers, sites, and other processes
> 6. Minimum staff and resources needed to keep running in an emergency, and any manual workarounds
> 7. Past disruptions and lessons learned
>
> Use open questions and add follow-up prompts. Finish with a table for capturing answers.

Once I can see your units, I'll point you to the exact one.


## Tool calls in the stream

- `Bash` {"command": "cd \"$PWD\" && git ls-files | head -200; ls -la", "description": "List repository files"}
- `Glob` {"pattern": "**/*"}
- `ToolSearch` {"query": "select:mcp__claude_ai_Google_Drive__search_files", "max_results": 1}
- `mcp__claude_ai_Google_Drive__search_files` {"query": "fullText contains 'AI4BCM' or (fullText contains 'BIA' and fullText contains 'prompt')", "pageSize": 10, "snippetVerbosity": "BRIEF"}
