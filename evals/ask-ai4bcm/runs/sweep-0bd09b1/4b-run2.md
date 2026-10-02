# /ask-ai4bcm case 4b, run2: Claude Code, guidance at 0bd09b1

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a885f790-f55b-42f7-9a69-950fc11e9bf6`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** which unit and prompt fit a BIA interview?

**Reply (verbatim):**

I couldn't find the material you're asking about. The working folder is empty, and Drive and SharePoint search were both denied in this mode. So I can't tell you which unit and prompt from your set fit. If you paste the options or say where they are, I'll pick.

Here's a general answer for a Business Impact Analysis (BIA) interview in the meantime.

**Unit:** Interview one business unit or process owner at a time, such as Payroll, Customer Support or Order Fulfilment. Don't interview a whole department or an IT system. A BIA looks at what happens to a business function when it stops, so the person you talk to should own one set of processes and know how it depends on people, systems, suppliers and data.

**Time unit for the answers:** Use hours or days on a fixed scale, for example 4h / 24h / 72h / 1 week / 2 weeks+. That's how recovery time (RTO), maximum tolerable downtime (MTPD) and acceptable data loss (RPO) are usually stated, and a fixed scale lets you compare answers across units.

**Prompt:** Ask open questions that stay on one scenario:

> "If [process] stopped completely and without warning, what would happen after 4 hours, 1 day, 3 days and 1 week? Think about financial, customer, legal/regulatory and reputational impact. At what point does it become unacceptable? What's the minimum you'd need to restart: people, systems, data, suppliers, location? How much data could you afford to lose?"

Follow-up questions to add:
- When in the day, month or year is this process most critical (peak periods)?
- Which upstream processes or vendors does it depend on, and which downstream ones depend on it?
- Are there manual workarounds, and how long could you keep them going?

**Tool calls (stream-json):**

- Bash: `git ls-files | head -100 && git ls-files | wc -l`
- Bash: `find . -maxdepth 4 -not -path '*/.git/*' | head -200`
- Bash: `ls -la /home/brain/.claude/projects/-tmp/memory/ 2>&1; cat /home/brain/.claude/projects/-tmp/memory/MEMORY.md 2>&1`
- Glob: `*`
- ToolSearch: ``
- mcp__claude_ai_Google_Drive__search_files: ``
- mcp__claude_ai_Microsoft_365__sharepoint_search: ``
