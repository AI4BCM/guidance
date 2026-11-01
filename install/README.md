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

**GitHub Copilot can start a skill you did not name.** It reads neither of the two settings that
hold the skills back on the other clients, and loads a skill when it judges it relevant. Read
[github-copilot.md](github-copilot.md) before you rely on it.

## Other tools, and no tool

Three pages cover the AI tools without a skill route, and the reader with no AI tool at all. They
are on GitHub only: the PDF and the .md file carry the units, not these install notes.

| Situation | Page |
|---|---|
| Microsoft 365 Copilot at work (not GitHub Copilot, a different product) | [microsoft-365-copilot.md](microsoft-365-copilot.md) |
| Claude on the web or in the desktop app, outside Claude Code | [claude-apps.md](claude-apps.md) |
| IT blocks outside AI tools, no route fits, or you work offline | [no-install-route.md](no-install-route.md) |

A ChatGPT plan without skills (Free, Go, Plus, Pro) is covered at the end of [chatgpt.md](chatgpt.md).

## The connector, and whether you need it

**You do not need it to use the skills.** No install route on these pages uses it: every package
carries its own units, and none declares an MCP server.

The connector is a second, separate way in. It is an open MCP server at
`https://mcp.ai4bcm.org/mcp` that serves this guidance and its open literature, the same corpus the
question box at ai4bcm.org/chat answers from. An AI tool that can add a remote MCP server can search
the guidance through it while you work, instead of you attaching a file. It needs no account and no
token. It offers five tools, all read-only: `search`, `fetch` (one section's full text with its
licence and citation line), `get_workflow`, `get_prompt_template` and `identify_ai_risks`. Its
release and size are at <https://mcp.ai4bcm.org/health>, and every section it serves, with its
GitHub link, at <https://mcp.ai4bcm.org/index.json>.

It reads nothing of yours: it has no access to your files or your tools. What reaches it is what your
AI sends as a search, so the data rules still apply to the words of your question (`units/data-rules.md`).
Add it only where your organisation allows outside connectors, and treat it as one under *Before you
approve a tool* in `units/tools.md`. Where you add it differs per tool: [claude-apps.md](claude-apps.md) and
[microsoft-365-copilot.md](microsoft-365-copilot.md) say where. Adding it in ChatGPT is not covered yet.

Reach for the connector when your tool cannot take a skill or a file but can take a remote MCP
server. Otherwise a skill, or the .md file, gives you the same guidance with nothing outside your
environment.

## How the installs were checked

`python3 tools/check_installs.py` installs a fresh clone of the repository by three routes into an
empty folder (the Claude Code plugin, the `skills` CLI for Codex and GitHub Copilot, and the ChatGPT
zips) and checks on disk that every installed skill is byte for byte its package, with
`preflight.md` and `units/` in it. Last run: 2026-10-02, Claude Code 2.1.288, `skills` 1.7.0, all
ten skills on all three routes. It checks the files, not what a client does with them; that is the
evals' job.
