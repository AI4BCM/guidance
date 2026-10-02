# $prepare-bia case 4b, run1: Codex, guidance at c332ccc

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9b2-1d3a-7721-9738-7471ffa32247`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you help me prepare questions for a BIA interview with our dispatch lead? The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’ll use the BIA facilitation skill to review the files and prepare questions tailored to the dispatch lead.

Is the interview with the dispatch lead at Site A or Site B? The activity list is approved for Site A, while the Site B organisation chart is an undated draft.
- Site A
- Site B
- Both sites

The files identify useful interview topics: dispatch depends on QA release and NordFrost, uses LogiStock, and has a possible manual export to Site B. That export still needs validation as a recovery option. The documents also cover different sites, so I’ll make scope confirmation the first question and treat the Site B draft as a lead to check.

Use this opening: **“We want to establish how long dispatch can be interrupted before the consequences become unacceptable, and what minimum service must recover before then.”**

The files cover different sites: the activity list is approved for **Site A**, while the **Site B** organisation chart is an undated draft. Confirm the interviewee’s scope first; use Site A details as prompts to validate if interviewing Site B.

Suggested questions, in interview order:

1. **Which site and dispatch responsibilities do you own?** Where does your responsibility begin and end, and who owns the handoffs?
2. **Which products, customers and delivery commitments does dispatch support?** Are service priorities already agreed, and where are they documented?
3. **What does normal dispatch look like?** Establish daily volumes, shift coverage, order cutoffs and chilled-product handling requirements.
4. **When would an interruption hurt most?** Site A lists weeks 49–52 and week 14. Are these still accurate, and which day or cutoff within those periods matters most?

Then walk through an interruption starting at the worst credible time. Begin with dispatch unavailable and assess reduced service separately.

5. **What happens after one missed cutoff, one shift, 24 hours, 48 hours and longer?** Adjust these time bands to the operation; capture consequences at each point.
6. **What financial losses arise at each point?** Separate delayed revenue from lost sales, spoilage, penalties and extra costs. What records support the estimates?
7. **Which customer commitments fail first?** When would this move from a complaint to a late key account, and potentially to losing that account?
8. **What food-safety or regulatory consequences arise, and when?** What would trigger an authority report or a production stop? Which conclusions need QA confirmation?
9. **When does the disruption become unacceptable, and why?** Record the specific consequence and evidence behind the proposed maximum tolerable period of disruption.

Use the approved impact criteria to score each time band:

| Level | Financial per day | Customer | Regulatory |
|---|---|---|---|
| 1 | Under €10k | One customer complains | None |
| 2 | €10k–100k | A key account is late | A report to the food authority |
| 3 | Over €100k | A key account is lost | Authority stops production |

**The criteria do not specify which level makes disruption unacceptable or how to combine categories.** Record category scores separately and flag these interpretation questions for the criteria owner.

Continue with recovery requirements and dependencies:

10. **What minimum dispatch service must resume, and by when?** Quantify volume, products, customers and shifts. The proposed recovery time should be shorter than the maximum tolerable disruption.
11. **What backlog would accumulate, and how long would clearing it take?** Consider chilled storage capacity, shelf life and later delivery slots.
12. **What exactly does dispatch need from QA release?** Site A records release before dispatch and a laboratory only at Site A. What happens to already-released stock versus stock awaiting release?
13. **What does dispatch need from NordFrost, and by which cutoffs?** No second carrier is recorded for Site A. Is that current, and is any alternative contracted and usable?
14. **Which LogiStock functions and records are essential?** How much dispatch or traceability data could be lost or require reconstruction before safe operation becomes impossible?
15. **What does “manual export to Site B” actually enable?** Is it a data transfer, or can Site B physically dispatch the goods? Who accepts it, how long does setup take, what capacity is available, and when was it last tested?
16. **What minimum people, skills, equipment and facilities are needed?** Include shift cover, chilled storage, loading capacity, communications and supporting systems. For Site B, verify the draft’s three shift leaders and QA coverage from Site A.

Close with:

17. **Which answers can you confirm, which carry reservations, and which need another owner’s input?** Name the evidence, owner and follow-up date for each open point.
18. **Who will review and approve the proposed priorities and recovery requirements?** Treat interview findings as inputs to management endorsement.

For every time or quantity, capture **the rationale, evidence source and uncertainty**. Keep conflicting estimates visible, and distinguish required recovery performance from demonstrated capability.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g 'AGENTS.md' -g 'site-a-activity-list.md' -g 'impact-criteria.md' -g 'site-b-org-chart.md' && cat /home/brain/.codex/skills/r`
- command_execution: `/bin/bash -lc 'cat site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat impact-criteria.md'`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md'`
- command_execution: `/bin/bash -lc 'cat /home/brain/.codex/skills/role-bia-facilitation/references/iso-ts-22317-2015.md'`
