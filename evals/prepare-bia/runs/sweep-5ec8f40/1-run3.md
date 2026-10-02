# /prepare-bia case 1, run3: Claude Code, guidance at 5ec8f40

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `74ee3cf1-619f-4570-957f-e047fc54400c`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, I need one answer:

**What class of data do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` hold?**

Under the AI4BCM data rules (`units/data-rules.md`, Sensitivity classes), BIA data, personnel records and contact lists, supplier weaknesses and site detail are all high-sensitivity. They may only be handled in an approved corporate or private environment. So please tell me:

1. the class you'd give this material (for example, high-sensitivity BIA and personnel data, or internal only), and
2. whether this Claude Code environment is approved for that class.

If it isn't approved, I'll stop here without reading the files. If it is, I'll read them and send one question to you as the organiser. Then I'll draft the dispatch interview guide, which will stay in this chat and won't be written to any file.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md && ls -R; echo ---; ls -la /tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files and found no embedded instructions in them. Before I draft, I have three questions as the organiser's intake (`prompts/bia.md`, Intake). Your answers will appear in the guide under Gaps as your own statements, not as sources. They can shape the scope but won't fill any value.

1. **Who are you interviewing, and what do they know that you don't?** I'm assuming it's the "Dispatch lead, Site B". Does this person own dispatch at Site B and decide on its resources? Or do the three shift leaders, or the site manager, hold some of that? Anything you already know they know that isn't in the files (systems, carriers, customers, how dispatch links to Site A) helps me aim the questions. It still won't become a value in the guide.
2. **What do you need back, and how long is the interview?** For example: a corrected activity and requirements list for dispatch only, or for dispatch plus its links to warehouse and QA. I need the length in minutes to size the take-in sheet.
3. **Are memory, past chats, project files, connectors and web search all switched off for this work?** Any that are on will be listed under Gaps, because the draft could draw on them without saying so.

Here's what I'll work from, so you can correct it now if it's wrong:
- **Site A activity list**: v3, 12 March 2026, approved.
- **Impact criteria**: v1.1, 4 February 2026, approved by top management.
- **Site B org chart**: undated draft with no version. It goes under Gaps and isn't treated as current.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/1/run3/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/1/run3/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/1/run3/work/site-b-org-chart.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/keep-it-running.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

Here's the draft. It stays in this chat and nothing has been saved to a file.

---

# Interview guide: dispatch at Site B (candidate, to confirm)

**Sources**
- Site A activity list (chilled food production): version 3, 12 March 2026, approved by the site manager.
- Impact criteria: version 1.1, 4 February 2026, approved by top management.
- Site B organisation structure: no version and no date ("Undated draft from HR, no version."). It's listed under Gaps and not used as current.
- Method: `prompts/bia.md` 2026.09.1, `stages/analysis.md` 2026.09.1.

**Interviewee:** the Dispatch lead at Site B (your statement, G2). **Scope:** resources and peak weeks (your statement, G2).

## Gaps

- **G1.** The Site B org chart is an undated draft. The roles below that come from it are candidates only. *Settled by* a dated, approved Site B org chart from HR.
- **G2.** **Organiser's own statements, not sources:** (a) the interviewee is the Dispatch lead at Site B; (b) they know the shift pattern and the carrier contacts; (c) what's needed back is resources and peak weeks. These shape the scope but fill no value.
- **G3.** The interview length wasn't given. *Assumption:* about 60 minutes. The take-in sheet is sized to that.
- **G4.** You didn't say whether memory, past chats, project files, connectors and web search were off. *Assumption:* they're not confirmed off, so they're listed here. This draft read only the three attached files and the units shipped with the skill.
- **G5.** None of the sources give Site B's activities, peak weeks, buildings, IT, carriers or downstream recipients: "not in the sources". *Settled by* this interview.
- **G6.** It's "not in the sources" whether dispatch at Site B is chilled. Site A's dispatch is ("Dispatch, chilled").
- **G7.** None of the sources propose an MTPD, RTO or RPO, so there's no recovery-time note.
- **G8.** None of the attached files contain instructions to an AI.

## 1. Impacts over time: dispatch, Site B (rated in full)

This is the only activity in scope. The sources give no time bands, so the owner places the point at which each level is reached. All cells are blank until the owner fills them.

| # | Question for the owner | Source | Normal weeks | Peak weeks | Mark |
|---|---|---|---|---|---|
| R1 | Which weeks are peak weeks for dispatch at Site B? Site A's dispatch peaks in "weeks 49–52, week 14". | Site A list v3, A2; G5 | | | candidate, to confirm |
| R2 | How long after dispatch stops does the loss reach "EUR 10k–100k a day" (level 2), and "over EUR 100k a day" (level 3)? | Impact criteria v1.1, Financial | | | candidate, to confirm |
| R3 | When is "a key account is late" (level 2) reached, and when "a key account is lost" (level 3)? Which key accounts does Site B dispatch serve? | Impact criteria v1.1, Customer | | | candidate, to confirm |
| R4 | Can a stop in dispatch lead to "a report to the food authority" (level 2) or "the authority stops production" (level 3)? | Impact criteria v1.1, Regulatory | | | candidate, to confirm |

## 2. MTPD

| # | Question for the owner | Source | MTPD | Mark |
|---|---|---|---|---|
| R5 | Given the impacts above, after how long without dispatch would the damage become unacceptable? | Impact criteria v1.1 | ____ (owner sets) | candidate, to confirm |

## 3. People, "with the skills, authorities and mandates the work needs"

| # | Question for the owner | Source | Mark |
|---|---|---|---|
| R6 | Which decisions in dispatch can only the Dispatch lead take, and who takes them in their absence? | Site B org chart (G1) | candidate, to confirm |
| R7 | What is the shift pattern? How many people does each shift need at minimum, in normal and in peak weeks, and which skills and mandates must be on every shift? | Site B org chart, "(three shift leaders)" (G1); Gaps (G2b) | candidate, to confirm |
| R8 | Who else holds the carrier contacts and can book or change a carrier when the Dispatch lead is away? | Gaps (G2b) | candidate, to confirm |

## 4. Seats and buildings

| # | Question for the owner | Source | Mark |
|---|---|---|---|
| R9 | Which buildings, dock doors and workplaces does dispatch use? Could it run from anywhere else? | Not in the sources (G5); Site A records "two dock doors" only for its goods receipt (A1) | candidate, to confirm |
| R10 | Is dispatch at Site B chilled, as Site A's is? If so, which chilled space does it need? | Site A list v3, A2; G6 | candidate, to confirm |

## 5. IT and applications, "each with its RTO and its RPO"

| # | Question for the owner | Source | RTO | RPO | Mark |
|---|---|---|---|---|---|
| R11 | Does Site B dispatch use "LogiStock", or does it receive Site A's "manual export to Site B"? | Site A list v3, A2 | ____ | ____ | candidate, to confirm |
| R12 | Which other systems does dispatch need? | Not in the sources (G5) | ____ | ____ | candidate, to confirm |

## 6. Suppliers and other third parties

| # | Question for the owner | Source | Mark |
|---|---|---|---|
| R13 | Does Site B ship with "NordFrost"? At Site A there is "no second carrier recorded". Is there a second carrier for Site B? | Site A list v3, A1, A2, Dependencies | candidate, to confirm |
| R14 | Which carriers does Site B use, under which contracts, and do the same ones serve peak weeks? | Gaps (G2b) | candidate, to confirm |

## 7. Dependencies: up- and downstream relationships with other departments, "each recorded with the RTO the relationship carries"

| # | Question for the owner | Source | RTO of relationship | Mark |
|---|---|---|---|---|
| R15 | Upstream: does Site B dispatch wait for quality release from Site A's lab, as Site A records "A2 depends on A3 (release before dispatch)"? | Site A list v3, A3 "lab at Site A only", Dependencies; Site B org chart "QA: covered from Site A" (G1) | ____ | candidate, to confirm |
| R16 | Site A dispatch ↔ Site B dispatch: what does the "manual export to Site B" carry, in which direction, and when is it used? | Site A list v3, A2 | ____ | candidate, to confirm |
| R17 | Does dispatch depend on the Site B warehouse, or the warehouse on dispatch? | Site B org chart, "Warehouse lead, Site B" (G1) | ____ | candidate, to confirm |
| R18 | Downstream: which internal departments receive from dispatch? | Not in the sources (G5) | ____ | candidate, to confirm |

## Conflicts between sites, for the two owners and not for the model

- **C1. The manual export.** Site A's dispatch records "manual export to Site B possible", but Site A records no dependency on Site B, and Site B's material records no link back. *Put to:* Dispatch lead, Site A, and Dispatch lead, Site B.
- **C2. Quality release.** Site B's chart says "QA: covered from Site A". Site A's list records quality release with its "lab at Site A only" and only Site A's dispatch depending on it. No Site B dependency is recorded. *Put to:* QA manager, Site A, and Dispatch lead, Site B.
- **Possible shared supplier, not a conflict yet.** If Site B also ships with NordFrost, both sites rest on one carrier. That's a question for both dispatch owners.

## For the interview

Tell the Dispatch lead to "use the draft as the thing to correct, not the thing to confirm; record what it could not have known". The organiser says that includes the shift pattern and the carrier contacts.

## For the auditor

The register carries "the source, the interview it came from and the date behind each entry". Before the interview, three things stay blank for every entry R1 to R18:
- Interview: ____
- Confirmed on: ____
- "the recovery times the owner set": ____

## Reviewer

- **Activity owner, Dispatch lead at Site B:** confirms each requirement and sets the MTPD, RTO and RPO. The Site A owners named in C1 and C2 confirm their side of each relationship.
- **Top management:** "Top management approves the BIA results."

## Organiser's take-in sheet (about 60 minutes)

1. Site A says its dispatch can send a manual export to Site B. What does it carry, when is it used, and who handles it at your end?
2. Quality release is done in Site A's lab. Does your dispatch wait for that release, and what happens if it's late?
3. Which weeks of the year are your peak weeks?
4. If dispatch stopped in a peak week, how soon would losses pass ten thousand euros a day, and how soon a hundred thousand?
5. When would a key account be late, and when would one be lost?
6. Could a stop in dispatch lead to a report to the food authority?
7. After how long without dispatch would the damage become unacceptable?
8. How does the shift pattern work, and how many people does each shift need at minimum?
9. Which decisions can only you take, and who stands in for you?
10. Who else has the carrier contacts and can book a carrier when you're away?
11. Which buildings, dock doors and workplaces do you use, and is any of it chilled?
12. Which systems do you dispatch with, and is LogiStock one of them?
13. Which carriers do you use, and do you ship with NordFrost?
14. Which departments do you wait on, and which wait on you?

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

Two answers are still open:
- **Interview length:** the take-in sheet assumes about 60 minutes (G3). Give me the real length and I'll trim or extend it.
- **Memory, connectors and web search:** you didn't say whether they're off, so G4 lists them as not confirmed off. Confirm they are and that entry goes.

**Tool calls (stream-json):**

- none
