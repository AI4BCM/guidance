# /prepare-bia case 1, run2: Claude Code, guidance at 3f263b8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4049e6b7-544f-4f22-bd9e-0131af650427`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files: what class of data do they hold? For example public, internal, confidential or restricted, using your organisation's own sensitivity classes.

Once I have your answer, I'll check it against the approved data classes for this environment. If it's allowed, I'll read the files and draft the Site B dispatch interview guide. The draft will stay here in the chat, and I won't create or edit any files.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md; echo ----; cat units/prompts/bia.md; echo ----; ls -R units | head -50; echo `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Glob: `**/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. "High" is one of the sensitivity classes in `units/data-rules.md`, and you've said this environment is approved for it, so I've read the three files.

The prompt has me ask you up to three questions before drafting. Your answers will go in the draft as your own statements, not as sources, and they won't fill in any value. The impact criteria are attached, so I won't ask for them.

1. **Interviewee:** Is the person you're interviewing the Dispatch lead at Site B named in the org chart, or a shift leader? And what do they know that you don't, such as Site B's own warehouse system, carriers or shift patterns?
2. **What you need back:** Should the interview cover chilled dispatch only, as at Site A (activity A2)? Or should it also cover other dispatch at Site B, and what Site A's notes call the "manual export to Site B"?
3. **Channels:** Are memory, past chats, project files, connectors and web search all switched off in this environment? If any of them is on, I'll list it under Gaps, because the model may draw on it without saying so.

If you skip a question, I'll write down the assumption I made instead and list it under Gaps.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/1/run2/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/1/run2/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/1/run2/work/site-b-org-chart.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Site B dispatch: draft interview guide

**Status:** draft, prepared before the interview. Every entry is a candidate until the activity owner confirms it. The MTPD, RTO and RPO fields are deliberately left blank.

## Sources and dates

- `site-a-activity-list.md`: Version 3, dated 12 March 2026. Approved by the site manager; owned by the BCM manager, Site A.
- `impact-criteria.md`: Version 1.1, dated 4 February 2026. Approved by top management.
- `site-b-org-chart.md`: "Undated draft from HR, no version." It is used here only to frame questions, not as a current source. See Gaps.

**Interviewee:** the Dispatch lead, Site B. This is your statement, not a source.

**Reviewer:**
- The Dispatch lead, Site B confirms each requirement and sets the MTPD and the RTOs.
- "Top management approves the BIA results."

## Before you start the interview

Use this draft as the thing to correct, not the thing to confirm. Record what the draft could not have known. The interviewee knows the shift pattern and the carrier contacts; the sources hold neither.

All of the questions below are adapted from Site A's chilled dispatch activity (A2). None of them come from any Site B register, because no Site B register was attached.

The last column of every table is left blank for the auditor. Fill it in after the interview with the interview reference, the date it was confirmed and who confirmed it.

## Candidate activity

| ID | Candidate activity | Source | Status |
|---|---|---|---|
| B-D1 | Does Site B run dispatch as one activity, and is it chilled dispatch like Site A's "Dispatch, chilled"? Is there any other dispatch? | site-a-activity-list.md, A2 | candidate, to confirm |

## 1. Impacts over time

| ID | Question for the Dispatch lead, Site B | Source | Status | Interview / confirmed on |
|---|---|---|---|---|
| 1.1 | If dispatch stops, after how long does the financial impact reach level 1 ("under EUR 10k a day"), level 2 ("EUR 10k–100k a day") and level 3 ("over EUR 100k a day")? | impact-criteria.md, Financial | candidate, to confirm | |
| 1.2 | When is "a key account is late" (level 2), and when is "a key account is lost" (level 3)? Which accounts does Site B dispatch serve? | impact-criteria.md, Customer | candidate, to confirm | |
| 1.3 | Could a dispatch stop lead to "a report to the food authority" or "the authority stops production"? | impact-criteria.md, Regulatory | candidate, to confirm | |
| 1.4 | **Peak weeks.** Site A's dispatch peaks in "weeks 49–52, week 14". What are Site B's peak weeks, and is a stop worse during them? | site-a-activity-list.md, A2 | candidate, to confirm | |

## 2. MTPD

| ID | Question | Source | MTPD | Status | Interview / confirmed on |
|---|---|---|---|---|---|
| 2.1 | Based on section 1, after how long would not resuming dispatch become unacceptable, both in a normal week and in a peak week? | impact-criteria.md | *(blank, set by owner)* | candidate, to confirm | |

## 3. People, with the skills, authorities and mandates the work needs

| ID | Question | Source | Status | Interview / confirmed on |
|---|---|---|---|---|
| 3.1 | How many people run dispatch on each shift, and what is the shift pattern? (The HR draft shows "three shift leaders".) | site-b-org-chart.md *(undated draft)* | candidate, to confirm | |
| 3.2 | Who can stand in for you, and for each shift leader? Who holds the skills to run dispatch? | not in the sources | candidate, to confirm | |
| 3.3 | **Mandate to release goods.** Site A records "release before dispatch" (A2 depends on A3), and Site B's QA is "covered from Site A". Who at Site B may release goods for dispatch? Can anyone release them if Site A's QA is unreachable? | site-a-activity-list.md, Dependencies; site-b-org-chart.md *(draft)* | candidate, to confirm | |
| 3.4 | Who holds the carrier contacts, and does more than one person hold them? | organiser's statement only | candidate, to confirm | |

## 4. Seats and buildings

| ID | Question | Source | Status | Interview / confirmed on |
|---|---|---|---|---|
| 4.1 | How many dock doors and what loading space does Site B dispatch use? Can dispatch run from fewer of them? (Site A's goods receipt records "two dock doors".) | site-a-activity-list.md, A1 | candidate, to confirm | |
| 4.2 | Which workplaces does dispatch need, and could the work be done from Site A or elsewhere? | not in the sources | candidate, to confirm | |

## 5. IT and applications, each with its RTO and its RPO

| ID | Question | Source | RTO | RPO | Status | Interview / confirmed on |
|---|---|---|---|---|---|---|
| 5.1 | Does Site B dispatch use "LogiStock"? If not, which system does it use? | site-a-activity-list.md, A2 | *(blank)* | *(blank)* | candidate, to confirm | |
| 5.2 | Site A notes a "manual export to Site B possible". What does Site B receive through it, how often, and can dispatch run on it if LogiStock is down? | site-a-activity-list.md, A2 | *(blank)* | *(blank)* | candidate, to confirm | |

## 6. Suppliers and other third parties

| ID | Question | Source | Status | Interview / confirmed on |
|---|---|---|---|---|
| 6.1 | Which carrier or carriers does Site B use? Site A's dispatch depends on NordFrost, with "no second carrier recorded". Is that also true at Site B, and is there a fallback? This is a question for you, not a finding. | site-a-activity-list.md, Dependencies | candidate, to confirm | |
| 6.2 | During peak weeks, does the carrier have the capacity to serve both sites? | site-a-activity-list.md, A2 | candidate, to confirm | |

## 7. Dependencies: up- and downstream relationships with other departments, each recorded with the RTO the relationship carries

| ID | Question | Direction | Source | RTO | Status | Interview / confirmed on |
|---|---|---|---|---|---|---|
| 7.1 | Does Site B dispatch wait on quality release from Site A (A3, "lab at Site A only")? | upstream | site-a-activity-list.md, A3 and Dependencies | *(blank)* | candidate, to confirm | |
| 7.2 | Does Site B dispatch depend on Site A's dispatch, or on the manual export from it? | upstream | site-a-activity-list.md, A2 | *(blank)* | candidate, to confirm | |
| 7.3 | Does the Warehouse lead, Site B feed dispatch? | upstream | site-b-org-chart.md *(draft)* | *(blank)* | candidate, to confirm | |
| 7.4 | Which departments wait on Site B dispatch? | downstream | not in the sources | *(blank)* | candidate, to confirm | |

**Note on recovery times:** none of the sources proposes an MTPD, RTO or RPO, so there is nothing to test against the impact criteria.

## Points to put to both sites' owners

There is no Site B register yet, so this draft cannot name any confirmed conflict between the sites. After the interview, put these points to the Dispatch lead at Site A and the Dispatch lead at Site B, not to the model:

- **Shared carrier at shared peaks.** If both sites rely on NordFrost and share weeks 49–52, the two registers may each assume carrier capacity that the other one is also counting on.
- **Shared QA release.** If both sites depend on the same Site A lab for release, the dependency RTO recorded at each site has to match.

## Gaps

- **Your answers are your own statements, not sources.** You said the interviewee is the Dispatch lead, Site B, who knows the shift pattern and the carrier contacts, and that you need resources and peak weeks back. These shape the scope but fill no value.
- **Assumption: scope.** You didn't say whether the interview covers chilled dispatch only. I've assumed it covers all dispatch at Site B and have used Site A's chilled dispatch (A2) as the reference.
- **Assumption: channels.** You skipped the question about memory, past chats, project files, connectors and web search. I can't confirm they are off, so treat them as possibly on: the model may have drawn on them without saying so. This would be settled by confirming the settings before relying on the draft.
- **The Site B org chart is an undated draft with no version.** It is not used as current. A dated, approved version from HR would settle it.
- **Not in the sources:** Site B's systems, carriers, dock doors, workplaces, downstream departments and peak weeks. The interview will settle these.
- **No instructions to the AI** were found in the attached material.

## For the auditor

Each register entry records the source, the interview it came from and the date behind it. In this pre-interview draft, three fields are left blank: the interview, the confirmation date and the recovery times the owner set. Every entry stays labelled "candidate, to confirm" until the owner confirms it.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (/prepare-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- Glob: `*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/SKILL.md`
