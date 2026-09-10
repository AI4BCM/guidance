# Claude Code

Source: https://code.claude.com/docs/en/skills, read 2026-09-10.

## The short way, as a plugin

This repository is its own plugin marketplace. Two commands, and the units are installed alongside
the router, so its links resolve:

```
/plugin marketplace add AI4BCM/guidance
/plugin install ai4bcm-guidance@ai4bcm
```

`/plugin` then lists it as `ai4bcm-guidance@ai4bcm`, carrying one skill, `ask-ai4bcm`. Updates come
through `/plugin update ai4bcm-guidance`.

## Where the folder goes

Personal, available in every project on your machine:

```
~/.claude/skills/ask-ai4bcm/SKILL.md
```

Inside one repository, available to anyone who clones it:

```
.claude/skills/ask-ai4bcm/SKILL.md
```

The command name comes from the directory name, so the directory must stay `ask-ai4bcm`.

## Steps

1. Clone or download this repository.
2. Copy `ask-ai4bcm/` into `~/.claude/skills/` or into `.claude/skills/` in your project.
3. Copy `units/` alongside it, or clone the whole repository and symlink `ask-ai4bcm/`, so the
   relative links from `SKILL.md` into `../units/` resolve.
4. Type `/ask-ai4bcm` in a Claude Code session.

## What the frontmatter does here

`SKILL.md` carries `disable-model-invocation: true`. The documentation states the effect. You can
still invoke the skill with `/ask-ai4bcm`, the model cannot load it on its own, and its description
stays out of the model's context until you ask. That is the intended contract for this router.
