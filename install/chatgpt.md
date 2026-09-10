# ChatGPT

Sources, each with the UTC time it was read:

- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt), 2026-09-10 10:51
- [Plugins in ChatGPT and Codex](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex), 2026-09-10 10:52
- [Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts), 2026-09-10 10:53
- [Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins), 2026-09-10 10:50
- [Build skills](https://learn.chatgpt.com/docs/build-skills), 2026-09-10 10:50
- [Skill controls](https://learn.chatgpt.com/docs/enterprise/skills), 2026-09-10 10:50

Re-read 2026-09-10 for the plugin package, with the sources that decided its shape:

- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt), 17:49
- [Plugins in ChatGPT and Codex](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex), 17:51
- [Importing and syncing plugin marketplaces from GitHub](https://help.openai.com/en/articles/20001504-importing-and-syncing-plugin-marketplaces-from-github), 17:52
- [Package your plugin](https://developers.openai.com/plugins/build/plugins.md), 17:48
- [Submit your Claude Code plugin to OpenAI](https://developers.openai.com/plugins/guides/submit-claude-plugin.md), 17:48
- [Agent Skills specification](https://agentskills.io/specification.md), 17:50

The `help.openai.com` articles were read in a browser; they answer HTTP 403 to `curl` from some
networks, and a check reporting them unreachable has hit that 403 rather than a dead page. The
`learn.chatgpt.com`, `developers.openai.com` and `agentskills.io` pages serve Markdown at a `.md`
suffix and answer plain `curl`.

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

## The plugin route

A plugin can bundle skills, and plugins work in Chat and Work across ChatGPT on the web, desktop and
mobile. That is the route worth having, because it reaches the phone and the browser as well as the
laptop, and a workspace administrator can hand it to everyone at once rather than to one machine at
a time.

The package exists now. It carries the router and the units together, which is the whole point: the
router names units by relative link, and a router whose links dangle is worse for you than no router
at all. The units travel inside the skill folder, at `skills/ask-ai4bcm/units/`, so the links resolve
wherever the folder lands.

**It declares no MCP server.** **MCP**, the Model Context Protocol, is a way for a client to reach a
live server while it answers a question; the router needs none, because it routes you to files
rather than fetching anything. Declaring one anyway would cost you the web: a plugin that declares an
MCP server is labelled **Desktop only** and cannot run on ChatGPT on the web, even when the server
sits behind a remote HTTPS URL. That is the one change that would silently take away the surface this
package exists to reach, so the package contains no `mcp.json` and no `.mcp.json`.

### Route A: import the marketplace from GitHub

For a workspace administrator who wants the guidance to stay current. ChatGPT re-reads the
repository daily.

1. Go to **Workspace settings > Plugins**, select **Add**, then **Import marketplace**.
2. In **Source**, enter `https://github.com/AI4BCM/guidance`. Enter the repository URL only, with no
   branch and no folder path after it.
3. Leave **Path** empty. The catalogue this repository publishes is at
   `.claude-plugin/marketplace.json` in its root, which is one of the manifest names the importer
   accepts.
4. Leave **Branch, tag, or commit** empty to follow the default branch, or name a tag to pin the
   wording your organisation reviewed. A pinned commit stays where you put it and never syncs
   forward.
5. Select **Import marketplace** and authorise GitHub access when prompted.
6. Open the imported `ai4bcm-guidance` plugin and set its **Installation policy**: *Available* lets
   eligible members install it themselves, *Installed* puts it on their accounts for them.

Import does not read the policy values written in the repository, so step 6 is not optional — until
you set a policy, nobody has the plugin. To pull a change before the next daily sync, open
**Marketplaces**, select the marketplace and choose **Sync now**.

The GitHub account you import with needs read access to the repository, and future syncs keep using
that account. If that person leaves, a new administrator imports the same source again with their own
GitHub connection rather than repairing the old one.

### Route B: upload the skill folder

For a workspace with no GitHub connection, or for one person testing the router before the
organisation commits to it. This installs the skill alone rather than the plugin.

Take `skills/ask-ai4bcm/` from the repository — the whole folder, including the `units/` directory
inside it — and upload it under **Plugins > Skills > Create > Upload from your computer**. An
administrator can do the same from the admin **Skills** page with **+ Add skill**, which puts it in
front of the workspace instead of one account.

ChatGPT scans an uploaded skill before it becomes available, and may mark it **Needs Review** before
you can use it. Review it yourself as well: it is a folder of instructions and text, it came from
outside your organisation, and the scan is not a substitute for your own judgement about what your
people are told to do with BCM material.

### What is not being claimed here

Neither route has been run in a real Business, Enterprise, Healthcare or Edu workspace, because this
guidance was packaged on a machine that has no such workspace. What has been checked is the package:
the archive was built, extracted, and every one of the router's 46 relative links resolved from
inside it. Whether ChatGPT accepts the upload, and what its scan says about a router that asks not to
be invoked on its own, are answered the first time an administrator with a workspace tries it. If you
are that person and something here is wrong, the repository takes issues.
