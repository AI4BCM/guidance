# ChatGPT

Sources, each with the UTC time it was read:

- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt), 2026-09-10 10:51
- [Plugins in ChatGPT and Codex](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex), 2026-09-10 10:52
- [Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts), 2026-09-10 10:53
- [Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins), 2026-09-10 10:50
- [Build skills](https://learn.chatgpt.com/docs/build-skills), 2026-09-10 10:50
- [Skill controls](https://learn.chatgpt.com/docs/enterprise/skills), 2026-09-10 10:50

The three `help.openai.com` articles were read in a browser; they answer HTTP 403 to `curl` from
some networks. The `learn.chatgpt.com` pages serve Markdown at a `.md` suffix.

## Who can install this in ChatGPT

Skills are the thing ChatGPT loads, and they are gated by plan. The help centre states it in one
line: "Skills are available to eligible ChatGPT Business, Enterprise, Healthcare, and Edu users,
subject to workspace settings and product availability." Even inside one of those workspaces an
administrator can turn skills off for your role, so check with whoever runs the workspace before
you spend time on this.

**On a personal account — Free, Go, Plus or Pro — no route to the router exists on any ChatGPT
surface.** The obvious workaround is closed too: new GPT creation and publishing are no longer
available on personal accounts, so you cannot wrap the guidance in a custom GPT either.

Use the guidance without the router instead; what it costs you is a lookup. `units/` is prose meant
to be read. Open the unit for your stage, or start from `units/levels.md` under **Starting guide**,
and take the prompt you need from `units/prompts/`. Classify your material against
`units/data-rules.md` first, which is the one step the router would have insisted on before anything
else. The print edition of the guidance is written for exactly this reader and carries the
same material in reading order.

## What works today, through Codex

The documented filesystem locations for skills belong to Codex, which reads `$HOME/.agents/skills`
among others, and Codex runs inside the ChatGPT desktop app as well as from the CLI. So on a machine
where both are installed, follow [codex.md](codex.md), put the folder in
`~/.agents/skills/ask-ai4bcm/`, and `@ask-ai4bcm` selects it. The ChatGPT desktop app lists skills in
its sidebar.

This is a developer action. It needs a checkout of the repository, a terminal and a machine you
control, and it reaches that one machine and nobody else in your team. Workspace skill features stay
subject to the plan gate above whatever sits on your disk.

## The plugin route, once the package exists

A plugin can bundle skills, and plugins work in Chat and Work across ChatGPT on the web, desktop and
mobile. That is the route worth having, because it reaches the phone and the browser as well as the
laptop, and a workspace administrator can hand it to everyone at once rather than to one machine at
a time. Administrators can also import a plugin marketplace straight from a GitHub repository and
keep it in daily sync.

The package for this guidance is being built and no date is promised for it. It will carry the
router and the units, and it will declare no MCP server. That is a deliberate choice: a plugin
declaring an MCP server is labelled **Desktop only** and cannot run on ChatGPT on the web, even when
the server sits behind a remote HTTPS URL. Until the package exists, the folder route above and the
plain units are what this guidance offers ChatGPT readers.
