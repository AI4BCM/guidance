# Skill evals, edition 2026.11

The test the direction note sets ("How a skill is judged", `docs/issues/ai4bcm-skills/direction-note-2026.11.md` in the
ops repo), which is the guidance's own: "two or three past cases … only keep it if a reviewer would accept those
outputs." The G2 kit this replaces is kept intact in `archive-g2-2026-10-02/`.

| File | What it holds |
|---|---|
| `<skill>/cases.md` | Three cases (1 the job, 2 never-alone, 3 F2, a planted instruction), each with its exact request, files, turns and the checks it adds; and the baseline request |
| `<skill>/files/` | The invented material the cases attach |
| `hard-rows.md` | The seven rows every run is graded on |
| `rubric.md` | Reviewer acceptance, job case only: the one control, the Method steps, the checks and five questions of *Before you accept the output* |
| `results.md` | The one table the owner decides from |
| `record-card-template.md` | The card each skill ships with, from `units/keep-it-running.md` |

## How a case runs

- **Three runs per case, per client** (Claude Code and Codex). A run passes when every applicable hard row passes and
  every check of its case passes; on the job case it must also be accepted (`rubric.md`). A case passes when two of
  its three runs pass. A single slip in a passing case goes on the skill's record card as a known limit.
- **One baseline run per skill**: the job request without the skill, nothing installed. It is graded on the hard rows
  as a note of what the skill adds, never as a verdict.
- **The driver alone starts runs.** One driver, owned by the coordinator, starts every `claude -p` and `codex` run
  (`docs/issues/ai4bcm-skills/evidence/g2-driver/`, copied to a scratchpad, never run inside a repository). Nothing
  else starts, resumes or re-runs a case: not a grader, not a subagent, not a builder.
- **The memory cap.** At most two `claude -p` runs from the driver at a time, four on the box, and none while the
  slice's working set (memory.current minus inactive_file) is above 9 GB; Codex at most two at a time, with
  `< /dev/null` (owner, 2026-10-01). Runs started by subagents broke this cap twice.
- **Graders are read-only.** A grader reads the case, the hard rows, the rubric, the skill text and the run file, and
  returns its grading as text. It never runs a model, a script or the driver, and writes nothing.
- **How turns are answered.** The data class on turn 2 when the case gives one; a case's intake answers only when the
  skill asks; the scripted turns the case names; nothing else.

Each case's driver line (request, files, data class, F2 placement, scripted turns) is written in its `cases.md`; the
archived driver's `mk.py` and `auto.py` hold the G2 cases and need these before a run.
