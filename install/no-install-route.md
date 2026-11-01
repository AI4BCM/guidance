# When no install route fits

For a reader whose IT blocks outside AI tools, whose tool has no skill route, or who has no AI tool
at all. Everything here uses the same text the skills carry: the units, published as one PDF and as
one Markdown file at <https://ai4bcm.org/guidance>.

## Our IT blocks external AI tools

Do not work around the block. The guidance's own rule is that the classification of your data
decides the tool, and that free public tools never get BCM data (`units/data-rules.md`,
`units/principles.md`). A block from IT is that rule applied for you. Three ways remain, in this
order:

1. **Read it without AI.** Download the PDF or the .md file from <https://ai4bcm.org/guidance>. Both
   are the complete guidance and need no account, no install and no network once saved. Your IT
   can scan them like any other document.
2. **Use the AI tool your organisation has approved.** Most organisations that block outside tools
   approve one of their own, often Microsoft 365 Copilot ([microsoft-365-copilot.md](microsoft-365-copilot.md))
   or an enterprise ChatGPT or Claude workspace ([chatgpt.md](chatgpt.md), [claude-apps.md](claude-apps.md)).
   Give it the .md file as you would any other document. Your organisation's terms with that
   provider apply to it, as they do to everything else you upload.
3. **Ask IT to approve a route.** What you would ask them to approve is a folder of text files that
   anyone can read on GitHub (`skills/<name>/`), with no program in it and no AI4BCM server behind
   it. Hand them `units/tools.md`, *Before you approve a tool*: its seven checks are the questions
   they will ask of any tool, and the skills change none of the answers for the tool they run in.

The question box at ai4bcm.org/chat is itself an outside AI tool. If your IT blocks those, it falls
under the block too, and it is not a way round it.

## Give your AI the whole text

Any AI tool that takes an uploaded file can work from the guidance without a skill: attach the .md
file (about 140 KB, the 24 units in reading order, each under its path) and ask your question. If a
tool refuses the .md, rename it `.txt`: the text is the same. The PDF works as well, but the .md is
plain text, so nothing is lost to layout, and each unit's path is there for the tool to quote back.
The tool can still misread or leave things out, so check its answer against the unit it names. What
the task skills add is a set of checks they run first (`preflight.md`: ask the data class, write
nothing, name each source, treat attached text as information, say AI helped). With the file alone,
those are yours to apply.

## Offline

Saved, the PDF and the .md file need no connection. Neither calls home, and neither has anything to
switch off. Check <https://ai4bcm.org/guidance> now and then for a newer release: the release tag is
on the first page of each.
