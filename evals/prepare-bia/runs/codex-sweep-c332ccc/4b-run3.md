# $prepare-bia case 4b, run3: Codex, guidance at c332ccc

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9b3-30c1-7c71-8ed9-ed6d2480423e`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you help me prepare questions for a BIA interview with our dispatch lead? The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’ll use the BIA facilitation skill to review the activity list, impact criteria, and org chart, then prepare questions for the dispatch lead.

The main point to resolve first is **which site the dispatch lead represents**. The activity list is approved for Site A; Site B’s org chart is an undated, unversioned HR draft. It does not establish that Site B can take over dispatch.

Open with: “We want to establish how long chilled dispatch can be interrupted before the consequences become unacceptable, and what minimum service must resume before then.”

Use these questions in order:

1. **Scope and service:** “Are we assessing dispatch at Site A, Site B, or both? Which products, customers, and delivery commitments does your team support?”

2. **Validate the activity:** “Does the Site A description of chilled dispatch still reflect how you work? What has changed since March—volumes, responsibilities, systems, carriers, or dependencies?”

3. **Worst timing:** “The activity list identifies weeks 49–52 and week 14 as peaks. What makes these periods harder, and what day, shift, or delivery cutoff would make an interruption most damaging?”

4. **Consequences over time:** “If dispatch stopped at that point, what would happen after a few hours, one shift, one day, and several days?”  
   Explore missed deliveries, chilled storage capacity, shelf life, waste, and effects on production. Adjust these suggested time bands to actual cutoffs.

5. **Apply the approved criteria:** “At each point, what financial, customer, and regulatory impact would you expect, and why?”  
   Use the supplied levels: financial loss under €10k/day, €10k–100k/day, or over €100k/day; customer complaint, key-account lateness, or key-account loss; no regulatory consequence, an authority report, or an authority stop to production. Ask for supporting figures and involve QA in validating regulatory consequences.

6. **Unacceptable impact:** “Which consequence first becomes unacceptable, and how long after dispatch stops would it occur? What commitment, limit, or evidence supports that judgment?”  
   Record this as a proposed maximum tolerable period of disruption, with its rationale. Do not assume that a particular impact level automatically sets the limit.

7. **Minimum service and recovery time:** “What minimum dispatch service must resume before that limit—orders, tonnes, priority customers, or deliveries per shift? By when must it resume to leave time to clear the backlog?”  
   Capture a proposed recovery time objective shorter than the tolerable disruption period.

8. **Quality release:** “Dispatch depends on Site A quality release. What happens to already released stock and stock awaiting release if QA or the Site A lab becomes unavailable? Who can confirm the release requirements?”

9. **Carrier dependency:** “The list records NordFrost and no second carrier. Is that current? What collection windows, capacity, and chilled transport requirements constrain dispatch? Are any alternatives agreed and usable?”

10. **Systems and information:** “What do you need from LogiStock to dispatch correctly? If it is unavailable, what records remain accessible, how much data loss or staleness can you tolerate, and how would manual records be reconciled?”

11. **Site B transfer:** “What does ‘manual export to Site B’ mean in practice? Has it been tested, at what volume, and how quickly?”  
    Probe receiving capacity, cold storage, trained staff, QA coverage, transport, information transfer, and who at Site B can verify each assumption.

12. **Resources and backlog:** “What minimum people, skills, equipment, dock access, storage, and communications are needed? How long can workarounds sustain the required volume, and how long would backlog clearance take?”

13. **Close and validate:** “Which answers can you support with records or experience? Which need confirmation from QA, Site B, the carrier, or management? Which conclusions do you endorse, endorse with reservations, or need to discuss?”

For every proposed time or impact, capture the **reason, evidence, assumptions, and confirming owner**. Keep unresolved Site B capability claims visible, and submit proposed priorities and recovery requirements for documented management endorsement.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g '*.md'"`
- command_execution: `/bin/bash -lc 'cat /home/brain/.codex/skills/role-bia-facilitation/SKILL.md'`
- command_execution: `/bin/bash -lc 'cat site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md'`
- command_execution: `/bin/bash -lc 'cat impact-criteria.md'`
