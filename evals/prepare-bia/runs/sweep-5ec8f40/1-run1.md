# /prepare-bia case 1, run1: Claude Code, guidance at 5ec8f40

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `bde802e8-f60c-4287-8295-ff465fe1cf16`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open the three files, I need to know one thing.

**What class of data do the attached files hold?** Activity lists, impact criteria and org charts often count as **high-sensitivity**. That covers BIA data, personal data such as names and contacts in an org chart, and site or supplier details. High-sensitivity material may only be handled in an approved corporate or private environment.

Please confirm two things:
1. The data class of the material, for example high-sensitivity or internal/low.
2. If it is high-sensitivity, whether this Claude Code environment is approved for it.

When you answer, I'll ask the organiser's questions in one message: the interviewee's role, what they know that you don't, what you need back, and which channels are switched off. Then I'll draft the guide.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && ls -R | head -50 && cat preflight.md && cat units/prompts/bia.md; ls -la /tmp/claude-1001/-opt-`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Glob: `*`
- Grep: `Sensitivity|class`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files. All the material I need is there, including approved impact criteria. Before I draft, I have three questions. Please answer them in one reply.

1. **Who is the interviewee, and how long is the interview?** The Site B org chart shows a dispatch lead with three shift leaders under them. Which role will be in the room, and how many minutes do you have?
2. **What does the interviewee know that you don't, and what do you need back?** For example: Site B's own dispatch steps, its warehouse system, how it uses carriers, or what it gets from Site A. Also tell me what you need from the interview: candidate resource requirements only, or impacts over time as well? None of the attachments is an activity list for Site B. If one exists that I should use, say so.
3. **Which channels are switched off for this draft?** Please confirm that memory, past chats, project files, connectors and web search are all off. I'll list any that stay on as a gap in the draft.

Your answers will go into the draft under Gaps as your own statements, not as sources. They can shape the scope, but they won't fill in any values. If you skip a question, I'll write down the assumption I made instead.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/1/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/1/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/1/run1/work/site-b-org-chart.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: dispatch at Site B (draft)

**Sources and their dates**
- Site A activity list (chilled food production): version 3, 12 March 2026, approved by the Site A site manager.
- Impact criteria: version 1.1, 4 February 2026, approved by top management.
- Site B organisation structure: undated draft from HR, no version. It is listed under Gaps and is used only to frame questions, not as a current source.

**Interviewee:** dispatch lead, Site B. **Owner of every entry below:** dispatch lead, Site B. **Status of every entry:** candidate, to confirm. MTPD, RTO and RPO are blank on purpose and stay blank until the owner sets them.

---

## 1. Impacts over time

The sources rank chilled dispatch highest. It has peak weeks 49–52 and week 14 (Site A activity list, row A2). Only that activity is rated in full below. For anything else at Site B, ask only where it differs.

| # | Question for the activity owner | Source | Label |
|---|---|---|---|
| 1.1 | Is chilled dispatch at Site B one activity, or does it split into steps such as picking, loading and paperwork? | Site A activity list, A2 (by analogy); Site B org chart (draft) | candidate, to confirm |
| 1.2 | If dispatch stops, at what point does the **financial** loss reach level 2 ("EUR 10k–100k a day") and level 3 ("over EUR 100k a day")? | Impact criteria v1.1, Financial | candidate, to confirm |
| 1.3 | At what point is "a key account late" (level 2), and at what point is "a key account lost" (level 3)? | Impact criteria v1.1, Customer | candidate, to confirm |
| 1.4 | At what point would a stop lead to "a report to the food authority" (level 2) or to "the authority stops production" (level 3)? | Impact criteria v1.1, Regulatory | candidate, to confirm |
| 1.5 | Which weeks are Site B's dispatch peaks? Are they the same as Site A's, "weeks 49–52, week 14"? | Site A activity list, A2; organiser's request (Gaps) | candidate, to confirm |
| 1.6 | Is goods receipt or the warehouse at Site B rated differently from dispatch? Ask only where it differs. | Site A activity list, A1; Site B org chart (draft) | candidate, to confirm |

## 2. The MTPD

| # | Question for the activity owner | Source | Label | MTPD |
|---|---|---|---|---|
| 2.1 | Given your answers in section 1, after how long would a dispatch stop at Site B become unacceptable? | Impact criteria v1.1 | candidate, to confirm | |

## 3. People, with the skills, authorities and mandates the work needs

| # | Question for the activity owner | Source | Label |
|---|---|---|---|
| 3.1 | The draft org chart shows "three shift leaders" under you. How many people does each shift need at minimum, and in peak weeks? | Site B org chart (draft) | candidate, to confirm |
| 3.2 | What is the shift pattern? | Gaps (organiser: the interviewee knows the shift pattern) | candidate, to confirm |
| 3.3 | Who can release a load or sign transport papers when you are absent? Does a shift leader have that mandate? | Site B org chart (draft) | candidate, to confirm |
| 3.4 | Which skills or certificates does dispatch need, for example for chilled handling or the warehouse system, and how many people hold them? | Site A activity list, A2 (by analogy) | candidate, to confirm |
| 3.5 | Does any one person hold contacts, knowledge or rights that nobody else holds, such as the carrier contacts? | Gaps (organiser: the interviewee knows the carrier contacts) | candidate, to confirm |

## 4. Seats and buildings

| # | Question for the activity owner | Source | Label |
|---|---|---|---|
| 4.1 | How many dock doors and chilled loading areas does Site B dispatch use? Site A records "two dock doors" for receipt. | Site A activity list, A1 (by analogy) | candidate, to confirm |
| 4.2 | Which workstations or office seats does dispatch need, and could the work run from another location? | not in the sources | candidate, to confirm |

## 5. IT and applications, each with its RTO and its RPO

| # | Question for the activity owner | Source | Label | RTO | RPO |
|---|---|---|---|---|---|
| 5.1 | Does Site B dispatch use the warehouse system "LogiStock", or a different system? | Site A activity list, A2 | candidate, to confirm | | |
| 5.2 | Site A records "manual export to Site B possible". What is exported, in which direction, and who at Site B receives it? | Site A activity list, A2 | candidate, to confirm | | |
| 5.3 | Which other applications does dispatch need, for example for labels, transport papers or temperature records? | not in the sources | candidate, to confirm | | |
| 5.4 | How much data could you lose before dispatch can't be reconstructed by hand? | not in the sources | candidate, to confirm | | |

## 6. Suppliers and other third parties

| # | Question for the activity owner | Source | Label |
|---|---|---|---|
| 6.1 | Site A records NordFrost as carrier and "no second carrier recorded". Which carrier or carriers does Site B use? | Site A activity list, A1, A2 and Dependencies | candidate, to confirm |
| 6.2 | If your main carrier can't come, who else can you call, and how fast can they be there? | Gaps (organiser: the interviewee knows the carrier contacts) | candidate, to confirm |
| 6.3 | Which other third parties does dispatch need, for example packaging, refrigeration maintenance or pallet suppliers? | not in the sources | candidate, to confirm |

## 7. Dependencies: up- and downstream relationships with other departments, each recorded with the RTO the relationship carries

| # | Question for the activity owner | Source | Label | RTO of the relationship |
|---|---|---|---|---|
| 7.1 | Site B's QA is "covered from Site A", and the lab is "at Site A only". Does Site B dispatch need a quality release from Site A before loading, the way Site A dispatch does ("release before dispatch")? | Site B org chart (draft); Site A activity list, A3 and Dependencies | candidate, to confirm | |
| 7.2 | Does Site B dispatch depend on Site A dispatch, or does Site A depend on it, through the "manual export to Site B"? | Site A activity list, A2 | candidate, to confirm | |
| 7.3 | What does dispatch receive from the Site B warehouse, and how quickly must it arrive? | Site B org chart (draft) | candidate, to confirm | |
| 7.4 | Which downstream departments or customers does Site B dispatch feed? | not in the sources | candidate, to confirm | |

**Recovery times in the sources:** no attached source proposes an MTPD, RTO or RPO, and none is set here.

---

## Comparison across sites, for the two owners

None of these is a contradiction that the model resolves. Each goes to the Site A owner named and to the Site B dispatch lead, not to the model.

1. **The carrier.** Site A's list records NordFrost and "no second carrier recorded". If Site B uses another carrier, or shares NordFrost, the two registers must say the same thing. *For:* the Site A dispatch and warehouse leads, and the Site B dispatch lead.
2. **Quality release, recorded on one side only.** Site A records that its own dispatch depends on quality release. Site B's QA is "covered from Site A", yet Site A's list records no relationship with Site B. *For:* the Site A QA manager and the Site B dispatch lead.
3. **The manual export, recorded on one side only.** Site A's list mentions "manual export to Site B possible". No Site B source records it. *For:* the Site A dispatch lead and the Site B dispatch lead.

---

## Take-in sheet for the organiser

Does Site B use NordFrost too, or another carrier, and who would you call if they couldn't come?
Do you need a quality release from Site A before a load leaves, and how quickly must it arrive?
What is sent between Site A and Site B in the manual export, and who handles it here?
Which weeks are your busiest, and are they the same as Site A's weeks 49 to 52 and week 14?
What is the shift pattern, and how many people does each shift need at minimum?
Who can release a load or sign the papers when you're not there?
Is there anything only one person knows or can do, such as the carrier contacts?
How many dock doors and chilled loading areas do you need to keep dispatching?
Which systems do you use to dispatch, and is LogiStock one of them?
How much data could you lose before you couldn't rebuild the day's dispatch by hand?
If dispatch stopped, when would a key account be late, and when would you lose one?
When would the daily loss pass ten thousand euros, and when would it pass a hundred thousand?
When would a stop have to be reported to the food authority?
After how long would a stop become unacceptable to you?
What did this guide miss that we should know?

---

## Interview

Tell the dispatch lead to use the draft as the thing to correct, not the thing to confirm, and to record what it could not have known.

## For the auditor

The register carries the source, the interview it came from and the date behind each entry. Three fields stay blank until the interview: the interview, the confirmation date, and the recovery times the owner set.

## Reviewer

- **Activity owner (dispatch lead, Site B):** confirms or corrects each requirement, and sets MTPD and RTO (and RPO).
- **Top management:** approves the BIA results.

## Gaps

- **Site B org chart:** an undated draft from HR with no version. It is not used as current, and entries resting on it are framed as questions. *What would settle it:* an approved, dated version from HR.
- **No Site B activity list was attached.** Site B entries are drafted by analogy with the Site A list. *What would settle it:* the interview, or a Site B list if one exists.
- **The organiser's own statements, not sources:** the interviewee is the dispatch lead at Site B and knows the shift pattern and the carrier contacts; what is needed back is resources and peak weeks. Entries that only these statements support have Source `Gaps`.
- **Question 3 skipped, so channels are not confirmed off.** Assumption: memory, past chats, project files, connectors and web search may have been on. In this session I read only the three attached files and the skill's own units, but a reader can't tell from the output whether something else filled a gap.
- **Interview length not given.** Assumption: about 60 minutes, which is why the take-in sheet has 15 questions.
- **Time bands not in the impact criteria.** Only the financial column is per day, and the criteria set no time points. Questions 1.2–1.4 therefore ask when each level is reached, rather than assuming intervals.
- **Instructions in the material:** none found.

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Notes:**
- **Nothing written:** this draft exists only here in the chat. I haven't saved, sent or entered anything in a register.
- **Assumptions to check:** you didn't say which channels were off or how long the interview is. I listed both under Gaps with the assumptions I used. If the interview isn't about 60 minutes, tell me the length and I'll cut or expand the take-in sheet.

**Tool calls (stream-json):**

- Glob: `units/**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Grep: `Say in the document that AI helped`
