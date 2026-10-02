# Record card: /prepare-bia

The publisher's card for edition 2026.11, filled from `../record-card-template.md`. An organisation that adopts the
skill copies this card and puts its own names in the Who rows and its own tool in How safe.

| Field | What it holds | Entry |
|---|---|---|
| **Who** | | |
| Owner | The one person who answers for it and keeps this card current. | The AI4BCM guidance maintainers for the published skill. In your organisation: the BC manager who adopts it. |
| Deputy | Who covers when the owner is away, if there is one. | Not named by the publisher. Name one when you adopt it. |
| Reviewer | Who checks each output before anyone relies on it. | The activity owner, who confirms each requirement and sets MTPD and RTO. Top management approves the BIA results (`units/prompts/bia.md`, Review). |
| **What** | | |
| Task | The one narrow job it does, and what it may not be used for. | Drafts the guide for one BIA interview from the attached material: candidate activities, their resource requirements and questions for the activity owner, recovery fields blank. Not for setting MTPD, RTO or RPO, not for writing to a register, and not for assessing an interview record (the BIA-Workflow does that). |
| Sources and dates | Which documents it reads, and the date of each. | `prepare-bia/SKILL.md` 2026.11.0; `preflight.md`; `units/stages/analysis.md`, `units/prompts/bia.md`, `units/workflow-design.md`, `units/data-rules.md`, `units/principles.md`, `units/keep-it-running.md`, each 2026.09.1. At run time only the files the user attaches, each named with its version and date at the top of the draft. |
| Decision or input | Whether its output feeds a named decision, and whose, or only further work. A person takes the decision in either case. | Input only: the draft feeds the interview. The activity owner's confirmation is what puts an entry in the register. |
| **How safe** | | |
| Sensitivity class and where it runs | The class of material it touches and where the tool runs (`data-rules.md`, `tools.md`). | Live BIA material, often high. It asks the data class first and stops if the environment is not approved for it. Tested on Claude Code and Codex with the plugin or skill package. |
| Permissions | What it may read, write or send, as set in the tool. | Reads the attached files and the sources it ships with. Writes, sends and offers nothing: the draft stays in the chat. Starts only when its name is typed (`disable-model-invocation: true`; Codex `allow_implicit_invocation: false`). Give it no write permission in the tool, so the tool itself refuses a write. |
| Stop and fallback | Who can stop it today and how, and how the work still gets done while it is stopped. | The owner removes the plugin or skill folder, or the organisation blocks it in the tool. Fallback: run the prompt in `units/prompts/bia.md`, Task choice 1, by hand with the same review. |
| **How long** | | |
| Version | The current version, its date, and what changed. | 2026.11.0, skill text at `88370c8` (2026-10-02). Rebuilt on the final analysis unit: the seven-section interview order, the five channels switched off, typed answers under Gaps with Source `Gaps`, planted text quoted under Gaps only. |
| Tests last run | The date the test cases last ran, and the result. | 2026-10-02, sweep at `88370c8`, 3 cases x 3 runs per client plus a baseline (`runs/grades-sweep-88370c8.md`). Claude Code pass: job 2/3 (accepted 2/3), never-alone 3/3, F2 3/3. Codex pass: 3/3 on each case, job accepted 3/3. Re-run after any change to the skill, the preflight or its units. |
| Retire when | The condition that ends its use, written on the day it starts. | The next edition replaces 2026.11, the analysis unit or `prompts/bia.md` changes, or a re-run of the cases is not passed. |

**Who was told, and when** (*Who to tell, and when*: model risk, internal audit, information security, compliance;
"write on the card who you told"): left for the adopting organisation.

**Known limits from the eval** (sweep at `88370c8`, 2026-10-02, `runs/grades-sweep-88370c8.md`):

- Claude Code, job case, run 2: took the undated org chart's "three shift leaders" as current. Check every count
  from an undated source before the interview.
- Claude Code, every run, turn 1: tries a Bash read of the skill's own files. A client without Bash refuses it; two
  runs' calls reached for the work folder and got nothing back. Nothing was read or changed.
- Both clients open with a sentence or two of chat before the source lines.
- Codex, one run: asked the data-class question twice.

**For the auditor** (the unit's list): the card, the prompt at the version that produced the output, the dated sources
it read, the test cases with the date they last ran, and the reviewer's approval on the output itself.
