# /ask-ai4bcm case 4b, run3: Claude Code, guidance at 6aaa84b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `2acc9f77-bb3f-4c8e-85a6-2436adfaa07e`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** which unit and prompt fit a BIA interview?

**Reply (verbatim):**

I couldn't find your specific list of units and prompts. The working directory is empty, there are no saved notes, and searches of Google Drive and SharePoint were blocked. So this is the standard approach for a Business Impact Analysis (BIA) interview, not a pick from your own options.

**Unit: interview one business process (or a small business unit), not a whole department or an IT system.**
- Talk to the **process owner** plus 1–2 people who do the work every day. Managers tend to overstate impact, and frontline staff know the real workarounds.
- Keep each interview to one process, such as "Accounts Payable – vendor payments", not "Finance". If you go broader, the recovery targets get blurred into one average.
- Cover IT systems as dependencies of each process, not as separate interview subjects.

**Prompt: work through the questions in this order:**
1. **Process:** What does this process deliver, to whom, and how often? Are there peak periods (month-end, seasonal)?
2. **Impact over time:** If it stopped, what happens after 1 hour, 4 hours, 1 day, 3 days, 1 week? Cover financial, customer, regulatory/legal, reputational and safety impact.
3. **Maximum tolerable downtime (MTD):** At what point does the outage become unacceptable?
4. **Recovery time objective (RTO):** How soon must it be running again, even at a reduced level?
5. **Recovery point objective (RPO):** How much data or work could you lose and re-create?
6. **Dependencies:** Which systems, applications, data, suppliers, other teams, sites and equipment does it rely on?
7. **Minimum resources:** What is the smallest staff, seat and equipment setup that keeps it running?
8. **Workarounds:** Can it be done manually or from another site? For how long?
9. **Backlog:** How long would it take to catch up after recovery?

Bring a fixed impact scale (for example 1–5 per impact category and time band) so answers can be compared across units.

If "unit" and "prompt" are fields in a specific tool or template you're using, paste the options or point me to the file and I'll pick the right ones.

**Tool calls (stream-json):**

- Bash: `cd /tmp/claude-1001/-opt-brain-172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/ask-ai4bcm/4b/run3/work 2>/dev/null || pwd; git ls-files | head -100; ls `
- Glob: `**/*`
- Glob: `**/*`
- ToolSearch: ``
- mcp__claude_ai_Google_Drive__search_files: ``
- mcp__claude_ai_Microsoft_365__sharepoint_search: ``
