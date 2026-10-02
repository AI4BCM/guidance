# Claude Code

Sources: https://code.claude.com/docs/en/skills and
https://code.claude.com/docs/en/plugins-reference, both read 2026-10-02.

**Test tier: full eval.** Every skill is run on Claude Code in three cases (the job, never-alone, a
planted instruction), three runs each, plus a run without the skill. Results:
[`evals/results.md`](../evals/results.md).

## As a plugin (recommended)

This repository is its own plugin marketplace. In a Claude Code session:

```
/plugin marketplace add AI4BCM/guidance
/plugin install ai4bcm-guidance@ai4bcm
```

or from a terminal:

```
claude plugin marketplace add AI4BCM/guidance
claude plugin install ai4bcm-guidance@ai4bcm
```

The plugin loads the ten packages under `skills/`, each with its `preflight.md`, `units/` and
`literature/`. `claude plugin details ai4bcm-guidance@ai4bcm` should list ten skills, each name
once. Update with `/plugin update ai4bcm-guidance`.

Plugin skills carry the plugin's name: Claude Code lists them as `/ai4bcm-guidance:<skill>`, for
example `/ai4bcm-guidance:prepare-bia`.

## By hand, as folders

Copy the package, never the source folder at the repository root, which lacks the preflight and
the units:

```
cp -r skills/prepare-bia ~/.claude/skills/            # for you, in every project
cp -r skills/prepare-bia <your-project>/.claude/skills/   # for everyone who clones that project
```

The command name comes from the folder name, so keep it: the skill above is `/prepare-bia`.

## What holds a skill back

Every `SKILL.md` carries `disable-model-invocation: true`. Claude Code's documentation states the
effect: only you can start the skill, by typing its name, and Claude cannot load it on its own.
