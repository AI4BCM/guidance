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

Use the pages below for Microsoft 365 Copilot, Claude outside Claude Code, or work without AI.
These install notes are on GitHub only. The PDF and the .md file contain the guidance units.

| Situation | Page |
|---|---|
| Microsoft 365 Copilot at work (a different product from GitHub Copilot) | [microsoft-365-copilot.md](microsoft-365-copilot.md) |
| Claude on the web or in the desktop app, outside Claude Code | [claude-apps.md](claude-apps.md) |
| IT blocks outside AI tools, no route fits, or you work offline | [no-install-route.md](no-install-route.md) |

For ChatGPT without skills (Free, Go, Plus, Pro), see the end of [chatgpt.md](chatgpt.md).

## The connector, and whether you need it

**You do not need the connector to use the skills.** Every package includes the guidance units.
None declares an MCP server, so none of these install routes needs the connector.

Use the connector if your tool accepts a remote MCP server but cannot accept a skill or a file.
Otherwise, a skill or the .md file gives you the same guidance in your approved tool, without
another service to approve.

The connector lets an AI tool search the guidance while you work. This saves you attaching a
file. It is an open MCP server at `https://mcp.ai4bcm.org/mcp`, with the guidance and its open
literature. The question box at ai4bcm.org/chat uses the same sources. You need no account or token.

The connector cannot access your files or tools. It receives what your AI sends: search words,
a sentence describing a task, or the name of a workflow or prompt. Keep case details out of
these requests. The data rules for outside tools apply. Data classes are defined under
*Classification levels* on page 7 of the PDF, or in
[units/data-rules.md](../units/data-rules.md) on GitHub.

For IT, the connector offers five read-only tools:

- `search`;
- `fetch`, which returns one section's full text, licence and citation line;
- `get_workflow`;
- `get_prompt_template`;
- `identify_ai_risks`.

Its release and size are at <https://mcp.ai4bcm.org/health>. All sections it serves, with their
GitHub links, are at <https://mcp.ai4bcm.org/index.json>.

Add it only if your organisation allows outside connectors. Apply the checks in *Before you
approve a tool* in `units/tools.md`. For setup steps, see [claude-apps.md](claude-apps.md) or
[microsoft-365-copilot.md](microsoft-365-copilot.md). These pages do not yet cover adding it in ChatGPT.

## How the installs were checked

`python3 tools/check_installs.py` installs a fresh clone of the repository by three routes into an
empty folder (the Claude Code plugin, the `skills` CLI for Codex and GitHub Copilot, and the ChatGPT
zips) and checks on disk that every installed skill is byte for byte its package, with
`preflight.md` and `units/` in it. Last run: 2026-10-02, Claude Code 2.1.288, `skills` 1.7.0, all
ten skills on all three routes. It checks the files, not what a client does with them; that is the
evals' job.
