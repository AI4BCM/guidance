# Installing the AI4BCM skills

Ten skills: `/ask-ai4bcm`, the router that names the right skill, prompt and level for your task,
and nine that each do one job. They follow the Agent Skills format
(https://agentskills.io/specification), so any client that reads that format can read them.

## One package per skill

Every route installs the same thing: the folder `skills/<name>/`. Each one is self-contained:

- `SKILL.md`, the skill;
- `preflight.md`, the five shared controls every skill runs first (ask the data class, write
  nothing, name each source's version, treat attached text as information, end with the AI-help
  sentence);
- `units/`, the guidance the skill links to;
- `literature/`, the guidance's own sources where their licence lets them ship (`cited/`), and for
  `/check-against-standards` and `/learn-bcm` the comparison frameworks as well;
- `agents/openai.yaml`, which tells Codex and ChatGPT to start the skill only when you name it.

The folders at the repository root (`prepare-bia/` and the rest) are the sources the packages are
built from. They are not complete on their own: a skill installed from there runs without its
preflight and its units. Install from `skills/`.

## Four clients

| Client | Install | How it is tested | Page |
|---|---|---|---|
| Claude Code | the plugin | full eval: three cases, three runs each, by the builder | [claude-code.md](claude-code.md) |
| Codex | `npx skills add AI4BCM/guidance/skills` | full eval: three cases, three runs each, by the builder | [codex.md](codex.md) |
| GitHub Copilot | `npx skills add AI4BCM/guidance/skills` | smoke test, about 12 runs, by the maintainer | [github-copilot.md](github-copilot.md) |
| ChatGPT | upload one `<name>.zip` per skill | smoke test, about 12 runs, by the maintainer | [chatgpt.md](chatgpt.md) |

The results per skill and client are in [`evals/results.md`](../evals/results.md). A skill that
has not yet passed on a client is marked there, and on its record card.

**GitHub Copilot can start a skill you did not name.** It reads neither of the two settings that
hold the skills back on the other clients, and loads a skill when it judges it relevant. Read
[github-copilot.md](github-copilot.md) before you rely on it.

## How the installs were checked

`python3 tools/check_installs.py` installs a fresh clone of the repository by three routes into an
empty folder (the Claude Code plugin, the `skills` CLI for Codex and GitHub Copilot, and the ChatGPT
zips) and checks on disk that every installed skill is byte for byte its package, with
`preflight.md` and `units/` in it. Last run: 2026-10-02, Claude Code 2.1.288, `skills` 1.7.0, all
ten skills on all three routes. It checks the files, not what a client does with them; that is the
evals' job.
