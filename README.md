# AI4BCM guidance — machine edition

The machine edition of the AI4BCM guidance: one markdown unit per topic, sized so a
model can read a whole unit and cite it. The same markdown is the source for the print
edition published at `ai4bcm.org/guidance`, so text is written once and published twice.

> Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.

## The three ways in

- **Guidance chatbot** — ask the guidance questions in the browser; it reads nothing of yours.
- **`/ask-ai4bcm` skill** — a router you invoke in your own assistant; it points you at the unit, the prompt and the maturity level for your situation, and reads your files inside your own tenant.
- **BIA workflow** — the five-stage business impact analysis run against your own process data.

## Installing the router

In Claude Code, where the units install alongside the router:

```
/plugin marketplace add AI4BCM/guidance
/plugin install ai4bcm-guidance@ai4bcm
```

In Codex, GitHub Copilot and anything else the `skills` CLI knows:

```
npx skills@latest add AI4BCM/guidance
```

That second route copies the skill folder alone, so the units stay here. One page per client, with
the folder paths each one scans and what each does about a skill it was not asked for, is in
[install/](install/README.md).

## Layout

- `units/` — the guidance itself, one file per topic.
- `ask-ai4bcm/` — the router, `SKILL.md`. See [ask-ai4bcm/README.md](ask-ai4bcm/README.md).
- `install/` — installing the router in Claude Code, Codex, GitHub Copilot or ChatGPT.
  See [install/README.md](install/README.md).

## Sending changes

Open an issue for anything wrong, missing or unclear, quoting the unit and the line.
Send corrections as a pull request against `main`, and leave the citation line at the foot
of every unit intact. The terms, the review cycle and who owns the living prompts are in
[CONTRIBUTING.md](CONTRIBUTING.md).

## Releases

Releases are tagged by calendar month, `YYYY.MM`. The first is `2026.09`; the next is
`2026.11`. A citation naming a tag names the text as it stood at that tag.

## Licence

CC BY 4.0. See [LICENSE](LICENSE).
