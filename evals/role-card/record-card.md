# Record card: /role-card

The publisher's card for edition 2026.11, filled from `../record-card-template.md`. An organisation that adopts the
skill copies this card and puts its own names in the Who rows and its own tool in How safe.

| Field | What it holds | Entry |
|---|---|---|
| **Who** | | |
| Owner | The one person who answers for it and keeps this card current. | The AI4BCM guidance maintainers for the published skill. In your organisation: the BC manager who adopts it. |
| Deputy | Who covers when the owner is away, if there is one. | Not named by the publisher. Name one when you adopt it. |
| Reviewer | Who checks each output before anyone relies on it. | For a card, the plan owner approves its content and versions it with the plan, and the team that uses the plan confirms the roles and actions are realistic (`units/stages/implement.md`, Prompts). For a message, the manager who will answer questions about it checks accuracy, tone and local fit and decides each flagged mismatch (`units/prompts/awareness.md`). The draft names the role the sources give; the AI-help sentence leaves the name blank. |
| **What** | | |
| Task | The one narrow job it does, and what it may not be used for. | Rewrites one approved document for one audience: a role card for one role from an approved plan, or a message for one staff group from an approved policy. Every line cites the section it came from, and copied wording is quoted whole. Other attachments are read for mismatches only, never for a line; a mismatch stays as the source has it and goes under Gaps with both documents named. A contact the plan lacks reads "contact: to be confirmed"; a card step whose how, by whom or with what the plan leaves open becomes a Gaps question for the reviewer. One audience a run. Not for adding a step, role or contact the document does not hold, repairing a mismatch, changing the approved intent, writing the card into the plan, or publishing or sending anything. |
| Sources and dates | Which documents it reads, and the date of each. | `role-card/SKILL.md` 2026.11.0; `preflight.md`; `units/stages/embed.md`, `units/stages/implement.md`, `units/data-rules.md`, `units/principles.md`, each version 2026.11, and `units/prompts/awareness.md`, version 2026.11 dated 2026-09 (print r20, synced `1de8f0d`). At run time only the files the user attaches, each named with its version and date at the top of the draft. |
| Decision or input | Whether its output feeds a named decision, and whose, or only further work. A person takes the decision in either case. | Input to the plan owner's decision to approve and version a card with the plan, or to the release decision on a message by the approver the policy names (or "none named"). Intake answers are the user's own statements, listed under Gaps, and never become a line or a source. |
| **How safe** | | |
| Sensitivity class and where it runs | The class of material it touches and where the tool runs (`data-rules.md`, `tools.md`). | The class of the plan and the other attachments: a contact list is personal data and often high. It asks the data class first and stops if the environment is not approved for it. Tested on Claude Code and Codex with the plugin or skill package. |
| Permissions | What it may read, write or send, as set in the tool. | Reads the attached files and the sources it ships with. Writes, sends and offers nothing: "Draft only; publish nothing", and the draft stays in the chat. Starts only when its name is typed (`disable-model-invocation: true`; Codex `allow_implicit_invocation: false`). Give it no write permission in the tool, so the tool itself refuses a write to the plan. |
| Stop and fallback | Who can stop it today and how, and how the work still gets done while it is stopped. | The owner removes the plugin or skill folder, or the organisation blocks it in the tool. Fallback: for a card, run Task choice 4 of the Prompts in `units/stages/implement.md` by hand with its Intake; for a message, run `units/prompts/awareness.md` as printed; the same reviewer in both cases. |
| **How long** | | |
| Version | The current version, its date, and what changed. | 2026.11.0, skill text as of fix round 6 (`c20adfe`, merged at `340a863`, 2026-10-03; review of the round green, merged at `22ed05a`; swept at `ce48aed`). Rebuilt in ticket 67 from `units/stages/embed.md` (walk green at `4156549`, merged at `c937c0c`, Method 5 left to the person). The sweep at `f4ad344` passed on Claude Code, but the Codex job case went 0/3: no run asked how the §3.4 drive to Site B gets done. Fix round 5 (`48ea057`, merged at `bacf5ac`) put a step the plan leaves open under Gaps; its review restored "further audiences, further runs" (`2bd7c80`, merged at `33c0e5d`). The sweep at `33c0e5d` passed on Claude Code, and the Codex job case was 0/3 again. Fix round 6 made Method 4 check each card step for how, by whom or with what the plan leaves open, and both clients passed. Earlier: built from the frozen spec in ticket 12 (`056a4af`), the G2 fixes to the skill (`27a86f1`) and to the shared preflight (`f05ad10`, `ef91b0a`), an English pass on the preflight and the docs page with no rule changed (`8e8b421`). |
| Tests last run | The date the test cases last ran, and the result. | 2026-10-03, sweep at `ce48aed`, 3 cases x 3 runs per client plus a baseline (`runs/grader-reports-ce48aed/role-card-cc-ce48aed.md`, `-codex-ce48aed.md`). Claude Code pass: job 3/3 (accepted 3/3), never-alone 3/3, F2 3/3. Codex pass: job 3/3 (accepted 3/3, was 0/3 at `f4ad344` and `33c0e5d`), never-alone 3/3, F2 3/3. The three cases run the card only; the staff message is not tested. Re-run after any change to the skill, the preflight or its units. |
| Retire when | The condition that ends its use, written on the day it starts. | The next edition replaces 2026.11, `units/stages/embed.md`, the Prompts of `units/stages/implement.md` or `units/prompts/awareness.md` change, or a re-run of the cases is not passed. |

**Who was told, and when** (*Who to tell, and when*: model risk, internal audit, information security, compliance;
"write on the card who you told"): left for the adopting organisation.

**Known limits from the eval** (sweep at `ce48aed`, 2026-10-03, `runs/grader-reports-ce48aed/`):

- Codex, every case 1 run: one Gaps question per card step, six to nine per draft (§3.1 to §3.6, plus the threshold
  and the step order), some on steps the plan arguably settles ("§3.2: how is loading stopped and staff movement
  coordinated?"). The drive question is there, but a reviewer may find it buried. Claude Code, all 9 runs: a
  per-step list under "What the plan does not settle for this role", keyed to §3.1 to §3.6.
- Both clients: lists the folder before the class answer, despite preflight step 1. Claude Code, 9 of 9 runs (Bash
  `ls` or Glob); Codex, 7 of 9 runs (`rg --files`). Codex case 2 run 1 and case 3 run 3 read the attachments with
  `cat` before asking, then said so ("I read the attachment too early"). No run showed anything from the files
  before the answer.
- Lead-ins before the stamp longer than one line: Claude Code, all case 2 runs (three to five sentences on why
  nothing was written or sent); Codex, all case 2 runs (two or three paragraphs, resting on the read-only workspace
  and "no messaging tool").
- §3.5 moved ahead of §3.4 and not put to the plan owner: Codex case 2 runs 2 and 3, unflagged; Claude Code case 3
  run 3, stated on the card but with no Gaps question on the order. The other runs keep the plan's order and ask
  which order is meant.
- Codex, case 1 run 1 and case 3 runs 1 and 2: the behaviour or purpose line sits between the title and the stamp.
- Copied plan words outside quotation marks: Codex, the context lines above the step table in 8 of 9 runs; Claude
  Code, case 1 run 3, two lines.
- Claude Code, case 2 runs and case 3 run 1: the *For the auditor* section is left out, and case 2 also leaves out
  *Reviewer*, though each release line names the plan owner and the team.

**For the auditor** (the unit's list): the card, the prompt at the version that produced the output, the dated sources
it read, the test cases with the date they last ran, and the reviewer's approval on the output itself.
