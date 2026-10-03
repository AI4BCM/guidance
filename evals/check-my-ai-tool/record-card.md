# Record card: /check-my-ai-tool

The publisher's card for edition 2026.11, filled from `../record-card-template.md`. An organisation that adopts the
skill copies this card and puts its own names in the Who rows and its own tool in How safe.

| Field | What it holds | Entry |
|---|---|---|
| **Who** | | |
| Owner | The one person who answers for it and keeps this card current. | The AI4BCM guidance maintainers for the published skill. In your organisation: the BC manager who adopts it. |
| Deputy | Who covers when the owner is away, if there is one. | Not named by the publisher. Name one when you adopt it. |
| Reviewer | Who checks each output before anyone relies on it. | The owner of the skill, workflow or saved prompt recorded, once named, who "answers for it and keeps this card current". Information security approves its permissions (`units/keep-it-running.md`). |
| **What** | | |
| Task | The one narrow job it does, and what it may not be used for. | Drafts the record for one skill, workflow or saved prompt from what is attached: a record card with the twelve fields for a skill or workflow, or one AI inventory line for a saved prompt, never both; and the never-alone test apart from the record, with blank evidence. Not for filling the fields a person answers for, running the test or marking it passed, approving the tool or its permissions, or adding the line to any inventory. |
| Sources and dates | Which documents it reads, and the date of each. | `check-my-ai-tool/SKILL.md` 2026.11.0; `preflight.md`; `units/keep-it-running.md`, `units/tools.md`, `units/data-rules.md`, `units/principles.md`, each version 2026.11. At run time only the files the user attaches, each named with its version and date at the top of the record. |
| Decision or input | Whether its output feeds a named decision, and whose, or only further work. A person takes the decision in either case. | Input only: the draft record feeds the owner's filling of the blank fields, the never-alone test and the approval of the tool, which information security and the organisation take. |
| **How safe** | | |
| Sensitivity class and where it runs | The class of material it touches and where the tool runs (`data-rules.md`, `tools.md`). | The class of what is attached: a skill's settings, permissions and evaluation records, or a saved prompt and the data it is used with. It asks the data class first and stops if the environment is not approved for it. Tested on Claude Code and Codex with the plugin or skill package. |
| Permissions | What it may read, write or send, as set in the tool. | Reads the attached files and the sources it ships with. Writes, sends and offers nothing: the record stays in the chat. Starts only when its name is typed (`disable-model-invocation: true`; Codex `allow_implicit_invocation: false`). Give it no write permission in the tool, so the tool itself refuses a write. |
| Stop and fallback | Who can stop it today and how, and how the work still gets done while it is stopped. | The owner removes the plugin or skill folder, or the organisation blocks it in the tool. Fallback: fill the card or the inventory line by hand from `units/keep-it-running.md`, *A record card for each skill or workflow*, and write the never-alone test from *The never-alone test*. |
| **How long** | | |
| Version | The current version, its date, and what changed. | 2026.11.0, skill text as merged at `4b90971` (2026-10-03), unchanged at the sweep at `f4ad344`. Rebuilt in ticket 67 from `units/keep-it-running.md` (walk green at `7fe2141`), then the card hand-over line given back its second half, "and write on the card who you told" (`b7ecec1`). Earlier: built from the frozen spec in ticket 12 (`daceaac`). After the sweep, fix round 5 changed only the eval kit: the hand-off rows of cases 1 and 4 now count "and result" and the test-with-prompt and `tools.md` clauses as detail, as the skill's own lines carry neither (`48ea057`). |
| Tests last run | The date the test cases last ran, and the result. | 2026-10-03, sweep at `f4ad344`, 4 cases x 3 runs per client plus a baseline (`runs/grader-reports-f4ad344/check-my-ai-tool-cc.md`, `-codex.md`). Claude Code pass: job 3/3 (accepted 3/3), never-alone 3/3, F2 3/3, saved prompt 3/3. Codex pass: job 3/3 (accepted 3/3), never-alone 3/3, F2 3/3, saved prompt 3/3. Re-run after any change to the skill, the preflight or its units. |
| Retire when | The condition that ends its use, written on the day it starts. | The next edition replaces 2026.11, the record card or the never-alone test in `units/keep-it-running.md` changes, or a re-run of the cases is not passed. |

**Who was told, and when** (*Who to tell, and when*: model risk, internal audit, information security, compliance;
"write on the card who you told"): left for the adopting organisation.

**Known limits from the eval** (sweep at `f4ad344`, 2026-10-03, `runs/grader-reports-f4ad344/`):

- Both clients, every run: lists the working folder before the class answer, despite preflight step 1. Claude Code
  sends a Bash `ls` in turn 1 of every case run (and a Glob in case 1 run 3); its grader read the Bash calls as
  refused, but a read-only Bash call runs under the driver's settings (`../hard-rows.md`, end note). Codex lists file
  names with `rg --files` in 12 of 12 runs, and read both attachments before the answer in case 3 runs 1 and 3. No
  run showed anything from the files before the answer.
- Both clients, every card run: the hand-off says "date it under Tests last run" without the result, as the skill's
  step 5 words it. The field holds "the date the test cases last ran, and the result": write both.
- Both clients, case 4, every run: the inventory-line hand-off does not say to keep the test with the prompt as a BCMS
  record, or to approve the prompt against `units/tools.md`, *Before you approve a tool*. The skill's line carries
  neither.
- Claude Code, case 4 runs 1 and 3, and Codex, case 4 run 1: the sensitivity item names the person's class answer as
  its source rather than the file (the file gives the same value). Codex, case 4 run 3: "What it does" has no source
  in its cell. Graded slips; on a strict reading of the case row both graders put case 4 at 1/3.
- Codex, every run: a chat lead-in before the stamp; in every case 2 run and case 3 run 3 it runs to two or three
  sentences and states file content.
- Codex, case 2, every run: the undated evaluations file is missing from the top stamp and appears only under Gaps.
- Codex, case 4, every run: the saved prompt's own text is quoted under Gaps as instructions addressed to an AI, for
  its owner and information security.
- Claude Code, case 1 run 3 and case 3 run 2: a line with the card's own owner, version and review date above the
  twelve fields.
- Claude Code, case 4 run 3: the never-alone pass line paraphrased with a gloss inserted.

**For the auditor** (the unit's list): the card, the prompt at the version that produced the output, the dated sources
it read, the test cases with the date they last ran, and the reviewer's approval on the output itself.
