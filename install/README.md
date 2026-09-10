# Installing `/ask-ai4bcm`

The router is one folder, `ask-ai4bcm/`, holding `SKILL.md` and `agents/openai.yaml`. It follows the
Agent Skills format (https://agentskills.io/specification, read 2026-09-10), so a client that reads
that format reads this one.

## Three routes, and what each one brings

**As a Claude Code plugin.** Two commands, and the units come with it, so every link in the router
resolves:

```
/plugin marketplace add AI4BCM/guidance
/plugin install ai4bcm-guidance@ai4bcm
```

**With the `skills` CLI**, which installs into whichever agent directories it finds:

```
npx skills@latest add AI4BCM/guidance
```

Update later with `npx skills update`. This copies the skill folder alone. The router then names
units that are not on disk beside it, and says so; read them from the repository, or clone it and
use the folder route instead.

**By hand, as a folder.** Clone the repository and copy `ask-ai4bcm/` and `units/` together into the
directory your client scans. One page per client, each written from that client's own current
documentation with the URL and the date it was read:

- [Claude Code](claude-code.md)
- [Codex](codex.md)
- [GitHub Copilot](github-copilot.md)
- [ChatGPT](chatgpt.md)

## What the router does, and what holds it back

It routes and nothing else. It names the unit to read, the prompt to run and the maturity level the
work needs, then hands over. Running the prompt is yours.

Two of the four clients can be told to leave the skill alone until you ask for it by name. Claude
Code reads `disable-model-invocation: true` in `SKILL.md`; Codex and the ChatGPT desktop app read
`policy.allow_implicit_invocation: false` in `agents/openai.yaml`. GitHub Copilot reads neither, and
its own documentation says it loads a skill when it judges it relevant.
