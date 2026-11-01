# Claude on the web and the desktop app

**On any Claude plan, the free one included: make a project, add the .md file from
<https://ai4bcm.org/guidance> to it, and ask.** On a paid plan you can add the AI4BCM plugin instead.
This page is for claude.ai and the Claude desktop app; Claude Code, the developers' tool, has its
own page, [claude-code.md](claude-code.md).

## A project with the guidance in it

Projects are on every plan (five on the free one). Create a project and add the .md file to its
knowledge; if Claude refuses the .md, rename it `.txt`. Add an instruction such as *Answer from the
AI4BCM guidance in this project and name the unit each answer comes from.* Every chat in the project
then starts with the guidance in front of Claude. For one question, attaching the file to a chat
works too.

A project does not ask you what class of data you are about to paste; the skills do. With a project
that check is yours (`units/data-rules.md`).

## The plugin, on a paid plan

The plugin Claude Code installs also works on claude.ai and in the desktop app on Pro, Max, Ultra,
Team and Enterprise. In the sidebar, open **Customize** (called **Plugins** on newer accounts), go
to **Plugins**, then **Add**, **Add marketplace**, **Add from a repository**, and enter
`AI4BCM/guidance`. Install `ai4bcm-guidance`. If your organisation restricts where plugins may come
from, ask your administrator to allow this one. Signed in with the same account, Claude Code
(2.1.273 or later) gets the plugin too.

## The connector

The AI4BCM connector is an open search service for this guidance; [README.md](README.md) explains
it under *The connector, and whether you need it*. To add it for yourself: **Customize**
(**Plugins**), **Connectors**, **+ Add**, **Add custom connector**, and enter
`https://mcp.ai4bcm.org/mcp`; it needs no sign-in. The free plan allows one custom connector. On
Team and Enterprise an owner adds it under **Organization settings**, **Connectors**, **Add**,
**Custom**, **Web**, and members then connect it for themselves.

## Uploading one skill does not work yet

claude.ai lets you upload a single skill as a zip, but it refuses the AI4BCM packages. An uploaded
skill may carry only `name`, `description`, `license`, `compatibility`, `metadata` and
`allowed-tools` in its frontmatter. Every AI4BCM package also carries
`disable-model-invocation: true`, the line that stops Claude Code starting a skill you did not name
([claude-code.md](claude-code.md)). Deleting that line would let the upload through and let the
skill start on its own, so do not; use a project or the plugin.

## How sure this page is

Not yet run on claude.ai or in the desktop app; the full eval runs on Claude Code. The phone apps
are not covered. Every step follows Anthropic's help centre as read on 1 November 2026, where the
sidebar's **Customize** becomes **Plugins** from 29 October 2026 (Enterprise from 30 November):
[Plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude),
[One Plugins page](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page),
[Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude),
[Custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills),
[Skill frontmatter outside Claude Code](https://code.claude.com/docs/en/skills#using-skill-frontmatter-outside-claude-code),
[Projects](https://support.claude.com/en/articles/9517075-what-are-projects),
[Uploads](https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai),
[Custom connectors](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).
