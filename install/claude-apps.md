# Claude on the web and the desktop app

**On any Claude plan, including Free, create a project, add the .md file from
<https://ai4bcm.org/guidance>, and ask your question.** On a paid plan you can add the AI4BCM
plugin instead.
This page covers claude.ai and the Claude desktop app. For Claude Code, the developer tool, see
[claude-code.md](claude-code.md).

## A project with the guidance in it

Projects are on every plan, with five on the free plan. Create a project and add the .md file to
its knowledge. If Claude refuses the .md, rename it `.txt`. Add an instruction such as *Use the
AI4BCM guidance in this project to answer, and name the unit you used.* Claude can then use the
guidance in every chat in that project. For one question, you can attach the file to a chat.

With a project, you must check the class of your data before pasting it. The skills ask you to
do this; a project does not. The classes are defined under *Classification levels* on page 7 of
the PDF, or in [units/data-rules.md](../units/data-rules.md) on GitHub.

## The plugin, on a paid plan

The AI4BCM plugin works in Claude Code, on claude.ai and in the desktop app on Pro, Max, Ultra,
Team and Enterprise. Open **Plugins** in the sidebar, then **Add**, **Add marketplace**,
**Add from a repository**, and enter `AI4BCM/guidance`. Install `ai4bcm-guidance`. If your organisation limits which plugins you can use,
ask your administrator to allow this one. Claude Code (2.1.273 or later) gets the plugin too when
you sign in with the same account.

## The connector

The AI4BCM connector lets Claude search this guidance. See [README.md](README.md) under
*The connector, and whether you need it*. To add it, open **Plugins** in the sidebar, then
**Connectors**, **+ Add**, **Add custom connector**, and enter
`https://mcp.ai4bcm.org/mcp`. It needs no sign-in. The free plan allows one custom connector. On
Team and Enterprise an owner adds it under **Organization settings**, **Connectors**, **Add**,
**Custom**, **Web**, and members then connect it for themselves.

## Uploading one skill does not work yet

Use a project or the plugin: claude.ai refuses AI4BCM skills uploaded as zip files. It accepts
single skills, but their header (frontmatter) may contain only `name`, `description`, `license`,
`compatibility`, `metadata` and `allowed-tools`. Every AI4BCM package also carries
`disable-model-invocation: true`, which stops Claude Code starting a skill you did not name
([claude-code.md](claude-code.md)). Do not delete that line. It would allow the upload but also let
the skill start on its own.

## How sure this page is

Not yet run on claude.ai or in the desktop app. The full evaluation runs on Claude Code. This
page does not cover the phone apps. Older accounts still show **Customize** until the **Plugins**
rollout ends: 9 November 2026 for Free, Pro, Max, Ultra and Team; 30 November 2026 for Enterprise.
The rollout began on 29 October 2026. Steps follow Anthropic's help centre, read on 1 November 2026:
[Plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude),
[One Plugins page](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page),
[Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude),
[Custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills),
[Skill frontmatter outside Claude Code](https://code.claude.com/docs/en/skills#using-skill-frontmatter-outside-claude-code),
[Projects](https://support.claude.com/en/articles/9517075-what-are-projects),
[Uploads](https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai),
[Custom connectors](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).
