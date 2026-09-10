# GitHub Copilot

Sources: https://docs.github.com/en/copilot/concepts/agents/about-agent-skills and
https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills, both read
2026-09-10.

## Where the folder goes

Inside a repository, any of:

```
.github/skills
.claude/skills
.agents/skills
```

Personal, shared across your projects:

```
~/.copilot/skills
~/.agents/skills
```

## The short way

```
npx skills@latest add AI4BCM/guidance
```

The `skills` CLI finds `ask-ai4bcm` in the repository and copies it into the agent directories it
detects, recording what it installed in `skills-lock.json`; `npx skills update` refreshes it. It
copies the skill folder alone, so the units named in the router are not beside it. Either read them
from the repository, or take the folder route below, which puts `units/` where the router expects.

## Steps

1. Clone or download this repository.
2. Copy `ask-ai4bcm/` into `~/.copilot/skills/`, or into `.github/skills/` in the repository you
   work in.
3. Copy `units/` alongside it, so the relative links from `SKILL.md` into `../units/` resolve.
4. In the GitHub Copilot CLI, invoke it by name: `/ask-ai4bcm`.

`gh skill` in the GitHub CLI searches for, installs, updates and publishes agent skills, and
`copilot skill add <FILE | URL | DIRECTORY>` adds one from a path.

Copilot reads the skill in the cloud agent, in Copilot code review, in the GitHub Copilot CLI, in
the GitHub Copilot app, and in agent mode in Visual Studio Code and JetBrains IDEs.

## What Copilot does not read

Copilot reads neither `disable-model-invocation` nor `policy.allow_implicit_invocation`. Its
documentation says Copilot loads a skill when it judges the skill relevant to the task, and that
skills in `.github/skills` are also available to Copilot code review. So in Copilot the router can
open on its own, which it cannot do in Claude Code or Codex. It still routes and nothing more, naming a unit,
a prompt and a level, and running nothing itself.
