# Claude on the web and the desktop app

Sources, all read 2026-11-01:
[Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude),
[One Plugins page](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page),
[Skill frontmatter outside Claude Code](https://code.claude.com/docs/en/skills#using-skill-frontmatter-outside-claude-code),
[Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude),
[How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills),
[What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects),
[What kinds of documents can I upload?](https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai)
and [Custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).

**Test tier: none.** The full eval runs on Claude Code ([claude-code.md](claude-code.md)). No route
on this page has been run in claude.ai by the maintainer.

Claude Code is the command-line and editor tool for developers. This page is for everyone else:
Claude in a browser at claude.ai and the Claude desktop app. Three ways that work, and one that
does not yet. The phone apps are not covered: nothing on this page has been checked there.

**The menu is being renamed.** From 29 October 2026 (Enterprise from 30 November) the sidebar's
**Customize** becomes **Plugins**, one page that holds plugins, skills and connectors. The steps
below name the old menu; on the new page, look for the same items there.

## The plugin, on a paid plan

The same plugin Claude Code installs. On Pro, Max, Ultra, Team and Enterprise, plugins work in chat
on the web, in the desktop app's Chat tab and in Cowork. Open **Customize** in the left sidebar,
the **Plugins** tab, **Add**, then **Add marketplace**, **Add from a repository**, and enter
`AI4BCM/guidance`. Install `ai4bcm-guidance` from it. If your organisation restricts marketplace
sources, Claude refuses a repository it does not allow; ask your administrator to add it.

Signed in with the same account, Claude Code (2.1.273 or later) picks up the installed plugin as
well.

## Uploading one skill does not work yet

Skills are on Free, Pro, Max, Ultra, Team and Enterprise, with code execution turned on, and Claude
takes a zip with the skill folder at its root, which is how the ChatGPT zips `<name>.zip` are built
([chatgpt.md](chatgpt.md), Route A). **The AI4BCM packages are refused all the same.** An uploaded
skill may carry only `name`, `description`, `license`, `compatibility`, `metadata` and
`allowed-tools` in its frontmatter, and an upload with any other field fails. Every package carries
`disable-model-invocation: true`, the line that stops Claude Code starting a skill you did not name
([claude-code.md](claude-code.md)). Deleting that line would let the upload through and the skill
start on its own, so do not; use the plugin or a project instead.

## A project with the guidance in it

Projects are on every plan, the free one included (five projects there). Create a project, add the
.md file from <https://ai4bcm.org/guidance> to its knowledge (the help centre takes PDF and text
files, up to 30 MB each; the .md is about 140 KB; if it is refused, rename it `.txt`), and add an instruction such as *Answer from the
AI4BCM guidance in this project and name the unit each answer comes from.* Every chat in the project
then starts with the guidance in front of Claude. Attaching the file to one chat works too, for a
single question.

A project carries no preflight. The task skills ask the data class before they start; with a
project, that question is yours (`units/data-rules.md`).

## The connector

Claude can add a remote MCP server as a custom connector on every plan (one on Free). For yourself:
**Customize** (or **Plugins**), **Connectors**, **+ Add**, **Add custom connector**, and enter
`https://mcp.ai4bcm.org/mcp`; it needs no sign-in. On Team and Enterprise an owner adds it under
**Organization settings**, **Connectors**, and members then click **Connect**. What the connector is
and whether you need it: [README.md](README.md), *The connector, and whether you need it*.

