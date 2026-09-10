# ChatGPT

Sources: https://learn.chatgpt.com/docs/build-skills and
https://learn.chatgpt.com/docs/skills-and-plugins, both read 2026-09-10.

## What is possible today

ChatGPT cannot be handed this skill as a folder through any route its documentation describes.
There is no documented directory for the ChatGPT desktop app to scan and no import step in the
interface. What the documentation does say:

- "Standalone skills are available in the ChatGPT desktop app, Codex CLI, and IDE extension."
  The paths it lists for those skills are the Codex ones, `$HOME/.agents/skills` among them.
- "Skills bundled in plugins are also available in Chat and Work across ChatGPT on the web,
  desktop, and mobile." Distribution beyond a local machine goes through packaging a skill as a
  plugin.
- "ChatGPT supports `@` mentions, while Codex supports `$` mentions for skills."

This guidance ships no plugin, so ChatGPT on the web and on mobile has no way to load the router at
all.

## What to do instead

On a machine where the ChatGPT desktop app and Codex are both installed, follow [codex.md](codex.md)
and put the folder in `~/.agents/skills/ask-ai4bcm/`. The desktop app lists standalone skills from
the same place, and `@ask-ai4bcm` selects it.

Anywhere else, use the guidance without the router. `units/` is readable prose. Open the unit for
your stage, or start from `units/levels.md` under **Starting guide**, and paste the prompt you need
from `units/prompts/`. Classify the material first against `units/data-rules.md`, which is what the
router would have told you to do.
