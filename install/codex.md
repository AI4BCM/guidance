# Codex

Source: https://learn.chatgpt.com/docs/build-skills, read 2026-09-10, reached by permanent redirect
from https://developers.openai.com/codex/skills/.

## Where the folder goes

Codex reads skills from repository, user, admin and system locations. The documented directories:

```
$CWD/.agents/skills
$CWD/../.agents/skills
$REPO_ROOT/.agents/skills
$HOME/.agents/skills
/etc/codex/skills
```

For a router you want everywhere, `$HOME/.agents/skills/ask-ai4bcm/` is the one to use.

## Steps

1. Clone or download this repository.
2. Copy `ask-ai4bcm/` into `~/.agents/skills/`.
3. Copy `units/` alongside it, or clone the whole repository and point `~/.agents/skills/ask-ai4bcm`
   at the clone, so the relative links into `../units/` resolve.
4. In the Codex CLI or IDE extension, type `$ask-ai4bcm`. `/skills` lists what Codex has found.

Codex detects skill changes without a restart.

## What `agents/openai.yaml` does here

The file beside `SKILL.md` reads:

```yaml
policy:
  allow_implicit_invocation: false
```

With that setting, only explicit invocation works. It is how Codex is told what
`disable-model-invocation: true` tells Claude Code.
