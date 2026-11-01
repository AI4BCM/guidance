# Microsoft 365 Copilot

**Attach the .md file from <https://ai4bcm.org/guidance> to Copilot Chat and ask your question.**
This works with or without a Copilot licence. Microsoft 365 Copilot has no AI4BCM skill to install.

## Not GitHub Copilot

Microsoft 365 Copilot is the assistant in Teams, Outlook, Word and the Copilot app at
m365.cloud.microsoft, signed in with your work account. GitHub Copilot is a coding assistant for
developers. Its instructions are at [github-copilot.md](github-copilot.md).

## Attach the guidance to a chat

In Copilot Chat, use **Add content** (+) or drag the .md file into the box, then ask. Copilot Chat
takes PDF, TXT and MD files, up to 20 in one conversation and 50 MB each; the .md file is about
140 KB. If the file is already in OneDrive or SharePoint, type **/** and its name instead.

The guidance is public. Your BCM material needs a tool approved for its data class. The classes
are defined under *Classification levels* on page 7 of the PDF, or in
[units/data-rules.md](../units/data-rules.md) on GitHub.

## For a team: an agent, set up with IT

IT or a colleague who builds agents can set up an agent that keeps the guidance for your team.
In Copilot Chat, open **Agents & Skills**, then **New agent**. Add the guidance as knowledge.
Tell the agent to answer from it and name the unit used. Turn on **Only use specified sources**.
This makes the agent prefer the guidance, but it can still use general knowledge.

- Agent Builder does not take .md files as knowledge. Upload the PDF, or save the .md file as .txt.
- Using uploaded files as knowledge needs a Microsoft 365 Copilot licence, or pay-as-you-go
  billing turned on for your organisation. Without either, the agent can use web search and its
  instructions but cannot use your files.
- Agent Builder also takes Agent Skills, the format of the AI4BCM skills (**Configure**, **Skills**,
  **Add**, upload a zip; licence or pay-as-you-go; up to eight per agent). Microsoft requires
  `SKILL.md` at the root of the zip, so zip the *contents* of `skills/<name>/`, not the folder. Claude
  refuses these packages because of a field in their header (frontmatter). See
  [claude-apps.md](claude-apps.md). Microsoft may refuse them too, so check the upload.

If you see no **New agent**, your administrator may have turned Agent Builder off.

## For a maker: the AI4BCM connector

A Copilot Studio agent can use the AI4BCM connector with generative orchestration on. Agent
Builder cannot. The connector is an open search service for this guidance, using MCP. See
[README.md](README.md) under *The connector, and whether you need it*. Building agents in Copilot
Studio needs licences or billing set up by your administrator.

## How sure this page is

Not yet run in a live Microsoft 365 tenant. Every step follows Microsoft's documentation as read on
1 November 2026:
[File upload](https://support.microsoft.com/en-us/microsoft-365-copilot/file-upload-in-microsoft-copilot),
[Copilot FAQ](https://learn.microsoft.com/en-us/copilot/faq),
[Refer to files](https://support.microsoft.com/en-us/microsoft-365-copilot/refer-to-specific-files-and-more-in-microsoft-365-copilot),
[Agent licensing](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites),
[Agent knowledge](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge),
[Agent skills](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills),
[MCP in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp).
