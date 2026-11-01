# Microsoft 365 Copilot

**Yes. Download the .md file from <https://ai4bcm.org/guidance>, attach it to a Copilot Chat
conversation, and ask your question.** That works today, with or without a Copilot licence. There is
no AI4BCM skill to install in Microsoft 365 Copilot.

## Not GitHub Copilot

Microsoft 365 Copilot is the assistant in Teams, Outlook, Word and the Copilot app at
m365.cloud.microsoft, signed in with your work account. GitHub Copilot is a coding assistant for
developers, a different product; its page is [github-copilot.md](github-copilot.md) and none of it
applies here.

## Attach the guidance to a chat

In Copilot Chat, use **Add content** (+) or drag the .md file into the box, then ask. Copilot Chat
takes PDF, TXT and MD files, up to 20 in one conversation and 50 MB each; the .md file is about
140 KB. If the file is already in OneDrive or SharePoint, type **/** and its name instead.

The guidance is public, so the file is no risk. Your BCM material is not public: it still needs a
tool approved for its class (`units/data-rules.md`).

## For a team: an agent, set up with IT

If your team asks often, IT or a colleague who builds agents can make one that always has the
guidance. In Copilot Chat: **Agents & Skills**, **New agent**. Give it the guidance as knowledge,
tell it to answer from that text and name the unit behind each answer, and turn on **Only use
specified sources** (the agent then prefers the guidance, though it can still fall back on general
knowledge).

- Agent Builder does not take .md files as knowledge. Upload the PDF, or save the .md file as .txt.
- Uploaded files as knowledge need a Microsoft 365 Copilot licence, or pay-as-you-go billing turned
  on for your organisation. Without either, an agent has web search and its instructions, not your
  files.
- Agent Builder also takes Agent Skills, the format of the AI4BCM skills (**Configure**, **Skills**,
  **Add**, upload a zip; licence or pay-as-you-go; up to eight per agent). Microsoft wants
  `SKILL.md` at the root of the zip, so zip the *contents* of `skills/<name>/`, not the folder. Claude
  refuses these packages for a frontmatter field ([claude-apps.md](claude-apps.md)); Microsoft may
  too, so check the upload.

If you see no **New agent**, your administrator may have turned Agent Builder off.

## For a maker: the AI4BCM connector

The AI4BCM connector is an open search service for this guidance, explained in
[README.md](README.md) under *The connector, and whether you need it*. A Copilot Studio agent can
call it, because Copilot Studio agents can use MCP servers (with generative orchestration on).
Agent Builder cannot. Microsoft ties authoring in Copilot Studio to licences or billing your
administrator sets up.

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
