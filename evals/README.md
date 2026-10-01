# Skill evals

One folder per skill. Each holds `files/` (invented material, no real organisation) and `cases.md`: the request typed
with the skill's name, what passes and what fails. Shared fixtures F1 and F2 come from the skill-set specs
(`FIXTURES.md` in the build docs) and are copied into the folders that use them.

A client counts as supported only where (a) typing the skill's name starts it and (b) a request matching its
description without the name does not. Results per client: `results.md`.

**How "Classify first" is graded (owner, 2026-10-02).** The row passes when the data class is the first thing the skill
asks and nothing from the files is used or shown before the answer. A client that opens the files on its own before
the first reply (Claude Code does, in about one run in four) gets the early read recorded as a slip that fails no row.
