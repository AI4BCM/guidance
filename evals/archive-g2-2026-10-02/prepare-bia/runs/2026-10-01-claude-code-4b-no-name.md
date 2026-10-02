# /prepare-bia on Claude Code: case 4b-no-name

Date 2026-10-01. Claude Code 2.1.284, `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, scratch folder with the case files copied in; later turns with `--resume`. One run; no crash.

## Turn 1

**Request:**

> Can you help me prepare questions for a BIA interview with our dispatch lead? The files in this folder (site-a-activity-list.md, impact-criteria.md, site-b-org-chart.md) are attached.

**Tool calls** (stream-json): Bash {"command": "ls -la && for f in *.md; do echo \"=== $f\"; cat \"$f\"; done", "description": "List folder and print the three markdown files"}; Read {"file_path": "/tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/evals/prepare-bia/4b-; Read {"file_path": "/tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/evals/prepare-bia/4b-; Read {"file_path": "/tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/evals/prepare-bia/4b-

No `Skill` call; no read of any `SKILL.md`. Bash was denied by dontAsk mode. The init event lists the skills under `slash_commands`: ai4bcm-guidance:ask-ai4bcm, ai4bcm-guidance:challenge-my-plan, ai4bcm-guidance:check-against-bia, ai4bcm-guidance:check-against-standards, ai4bcm-guidance:check-my-ai-tool, ai4bcm-guidance:debrief-to-action, ai4bcm-guidance:learn-bcm, ai4bcm-guidance:prepare-bia, ai4bcm-guidance:red-team-assumptions, ai4bcm-guidance:role-card.

**Final text:**

I've drafted a question set for the dispatch lead based on your three files. One thing needs settling first.

**Which dispatch lead is it?** Both sites have one. Site A's activity list has dispatch as activity A2, owned by the "Dispatch lead". Site B's org chart also lists a "Dispatch lead, Site B" with three shift leaders under them. I've assumed you mean **Site A**, because A2 is the only dispatch activity your documents cover. If it's the Site B lead, you'd be working without an activity list, and the Site B org chart is an undated, unversioned HR draft. In that case the interview would need to build the activity picture from scratch. Section 4 includes questions on Site B because Site B is the backup for dispatch.

---

## BIA interview: Dispatch, chilled (A2, Site A)

**Before the interview**
- Confirm the interviewee's name and that they own A2.
- Send them the impact criteria (v1.1) ahead of time, so they can rate impacts against the approved levels rather than by gut feel.

### 1. Confirm the activity
1. Does "Dispatch, chilled" describe what your team does? What's in scope: picking, loading, paperwork, temperature checks, customer booking?
2. The list gives weeks 49–52 and week 14 as peaks. What drives week 14? Are there other peaks it doesn't show?
3. How many people do this on a normal day, and in peak weeks? Over how many shifts?

### 2. Impact over time
For each interval (e.g. 4 hours, 1 day, 3 days, 1 week), ask in a normal week **and** in a peak week:

4. **Financial:** if dispatch stopped completely, roughly what would it cost per day? Is it under €10k, €10k–100k or over €100k?
5. **Customer:** which customers count as key accounts? At what point is a key account late, and at what point might you lose one?
6. **Regulatory:** what kind of dispatch failure would trigger a report to the food authority? Examples might be a temperature excursion, a traceability gap or shipping unreleased product. Could anything lead the authority to stop production?
7. How long could dispatch stop before the damage becomes unacceptable? This gives you the maximum tolerable period of disruption (MTPD).
8. How quickly would dispatch need to be running again, and at what minimum level (volume, or which customers first)? This gives you the recovery time objective (RTO) and the minimum level.
9. Does product shelf life limit how long you can hold finished goods? How much chilled storage do you have before you run out of space?

### 3. Dependencies
**Quality release (A3)**
10. Nothing ships until QA releases it, and the lab is only at Site A. What happens if the lab or QA is unavailable? Is there any route to emergency or conditional release?

**NordFrost**
11. NordFrost is the only carrier on record for both goods receipt (A1) and dispatch (A2). Do you actually have a second carrier, even informally? If NordFrost failed tomorrow, what would you do, and how long would it take to get another chilled carrier?

**LogiStock**
12. What can't you do without LogiStock: picking lists, labels, delivery notes, traceability records? Is there a manual or paper fallback, and has it ever been used?
13. How much data could you lose without real harm, e.g. the last hour of picks? This gives you the recovery point objective (RPO).

**Facilities and people**
14. Does dispatch use the same two dock doors as goods receipt? What happens if one of them is out of service?
15. Which roles or individual people can't be replaced at short notice: forklift licences, LogiStock power users, shift leaders?
16. Do you rely on any other suppliers or utilities: refrigeration maintenance, pallets, packaging, power, the network?

### 4. Workaround: manual export to Site B
17. The list says a "manual export to Site B" is possible. What does that involve in practice? Who exports what, in what format, and how long does it take?
18. Has it ever been tested or used for real? When, and what went wrong?
19. How much of Site A's volume could Site B handle, especially in weeks 49–52?
20. Site B's QA is "covered from Site A". If Site A is down, can product dispatched from Site B still be released?
21. Who at Site B would you call? The org chart lists a dispatch lead with three shift leaders. Is that current?

### 5. Close
22. Which past disruptions have hit dispatch, and how were they handled?
23. Who else should we speak to? For example, the NordFrost account manager, the LogiStock admin or the Site B dispatch lead.
24. Which documents can you share: shift plans, SOPs, carrier contracts?

---

**Gaps to raise with the BCM manager rather than the interviewee**
- The impact criteria have no category for **food safety or consumer health**, which matters for chilled food.
- The criteria don't define what a "key account" is.
- The Site B org chart is an undated draft and shouldn't be relied on as a source.

I can also put this into a shareable doc or interview template with space for answers if that helps.
