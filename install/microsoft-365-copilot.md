# Microsoft 365 Copilot

Sources, all read 2026-11-01:
[File upload in Microsoft Copilot](https://support.microsoft.com/en-us/microsoft-365-copilot/file-upload-in-microsoft-copilot),
[Copilot FAQ](https://learn.microsoft.com/en-us/copilot/faq),
[Refer to specific files](https://support.microsoft.com/en-us/microsoft-365-copilot/refer-to-specific-files-and-more-in-microsoft-365-copilot),
[Agent capabilities and licensing](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites),
[Add knowledge in Agent Builder](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge),
[Add skills in Agent Builder](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills) and
[MCP in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp).

**Test tier: none.** No route on this page has been run in a Microsoft 365 tenant by the maintainer.

## Not GitHub Copilot

Microsoft 365 Copilot is the assistant in Teams, Outlook, Word and the Copilot app at
m365.cloud.microsoft, signed in with your work account. GitHub Copilot is a coding assistant in
code editors and on GitHub; its install page is [github-copilot.md](github-copilot.md) and none of
it applies here. Microsoft 365 Copilot has no route that installs the ten skills the way Claude Code
or Codex does. It can still work from the guidance, in three ways.

## Attach the guidance to a chat

The quickest way, and the one that works with or without a Microsoft 365 Copilot licence. Download
the .md file (or the PDF) from <https://ai4bcm.org/guidance>, then in Copilot Chat use
**Add content** (+) or drag the file into the box, and ask your question. Microsoft lists PDF, TXT
and MD among the types a chat takes, up to 20 files in one conversation and 50 MB per file; the .md
file is about 140 KB. An uploaded file is stored in your OneDrive for Business.

If the file is already in OneDrive or SharePoint, type **/** and the file name to point Copilot at it
instead of uploading it again.

Your organisation's terms with Microsoft apply to the file and to everything you type next to it.
The guidance is public, so the file itself is no risk; your BCM material still needs a tool approved
for its class (`units/data-rules.md`).

## Build an agent that knows the guidance

For a team that wants the guidance at hand in every chat. In Copilot Chat, **Agents & Skills**, then
**New agent**. Give it the guidance as knowledge and tell it, in its instructions, to answer from
that text and to name the unit it took each answer from.

- **Knowledge.** Agent Builder takes uploaded files and SharePoint or OneDrive files, but its list of
  types is .doc, .docx, .pdf, .ppt, .pptx, .txt, .xls and .xlsx: not .md. Upload the PDF, or save the
  .md file as .txt first. Grounding on uploaded files or SharePoint needs a Microsoft 365 Copilot
  licence, or pay-as-you-go billing turned on for your tenant; without either, an agent can use web
  search and its instructions, but not your uploaded files or SharePoint.
- **Skills.** Agent Builder also takes Agent Skills, the format the AI4BCM skills are written in:
  **Configure**, **Skills**, **Add**, and upload a zip. It needs a Microsoft 365 Copilot licence or
  pay-as-you-go, and allows up to eight skills per agent. Microsoft's package has `SKILL.md` at the
  root of the zip, so zip the *contents* of a package folder `skills/<name>/`, not the folder
  itself: the ChatGPT zips ([chatgpt.md](chatgpt.md)) have the folder at their root and are not
  that format. Untested here: Claude refuses these packages for a frontmatter field
  (`disable-model-invocation`, see [claude-apps.md](claude-apps.md)) and Microsoft may too, so check
  the upload and that every file arrived before you rely on it.

Your administrator can turn Agent Builder off for your tenant. If you see no **New agent**, ask
them, or use the first way above.

## The connector, through Copilot Studio

Copilot Studio agents can call MCP servers, so an agent built there can search the guidance through
the AI4BCM connector rather than through uploaded files (see *The connector, and whether you need
it* in [README.md](README.md)). It is a maker's route, set up in Copilot Studio with generative
orchestration turned on, not something a reader does in chat. Agent Builder itself cannot add one.

## Which way for you

| You have | Do this |
|---|---|
| Copilot Chat, with or without a licence | attach the .md file to the chat |
| A Microsoft 365 Copilot licence, and a team that asks often | an agent with the PDF as knowledge, or with skills |
| Copilot Studio and an agent maker | an agent that calls the connector |
| Nothing approved, or IT blocks outside tools | [no-install-route.md](no-install-route.md) |
