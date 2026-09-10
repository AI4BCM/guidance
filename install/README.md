# Installing `/ask-ai4bcm`

The router is one folder, `ask-ai4bcm/`, holding `SKILL.md` and `agents/openai.yaml`. It follows the
Agent Skills format (https://agentskills.io/specification, read 2026-09-10), so a client that reads
that format reads this one.

One page per client, each written from that client's own current documentation with the URL and the
date it was read:

- [Claude Code](claude-code.md)
- [Codex](codex.md)
- [GitHub Copilot](github-copilot.md)
- [ChatGPT](chatgpt.md)

The router routes and nothing else. It names the unit to read, the prompt to run and the maturity
level the work needs, then hands over. Running the prompt is yours.

Two of the four clients can be told to leave the skill alone until you ask for it by name. Claude
Code reads `disable-model-invocation: true` in `SKILL.md`; Codex and the ChatGPT desktop app read
`policy.allow_implicit_invocation: false` in `agents/openai.yaml`. GitHub Copilot reads neither, and
its own documentation says it loads a skill when it judges it relevant.

Whichever client you use, the units it points at are the ones in `units/` beside this folder. Copy
the whole repository, or the `ask-ai4bcm/` and `units/` folders together, so the links in the router
resolve.
