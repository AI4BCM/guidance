# prepare-bia case 1, kit proof (ticket 62), graded 2026-10-02

Four runs of the pre-rebuild skill, started by the coordinator's driver alone (Claude Code at `ef3bca9`, three runs;
Codex at `85ebae8`, one run), each graded by a read-only subagent against `hard-rows.md`, case 1 of `cases.md` and
`rubric.md`. The coordinator checked each verdict against the case table; all four hold.

| Run | Hard rows | Case rows failing | Accepted | Run |
|---|---|---|---|---|
| Claude Code run 1 | 7/7 | none (analysis order borderline: impacts and MTPD left out, with the organiser's scope as the stated reason) | yes | pass |
| Claude Code run 2 | 7/7 | intake (typed answer cited as a source in R1); candidates (R1 "stated by organiser"); analysis order (suppliers, IT, seats; NordFrost dependency under suppliers) | no | fail |
| Claude Code run 3 | 7/7 | analysis order (suppliers, IT, seats; impacts and MTPD dropped; NordFrost dependency under suppliers); reviewer (the activity owner's confirmation not named) | no (also Method 4 missing) | fail |
| Codex run 1 | 7/7 | NordFrost ("no second carrier recorded" absent) | yes | fail |

What the rebuild (ticket 64) has to carry: the interview order of the analysis Method as written, dependencies as
their own item including the carrier, the activity owner as reviewer, and Method 4 (conflicts to the two owners).
