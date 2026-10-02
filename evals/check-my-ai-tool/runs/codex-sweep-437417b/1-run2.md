# $check-my-ai-tool case 1, run2: Codex, guidance at 437417b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9fa-4b16-7b42-bf31-15bd6edaa4d6`.

Files in the working folder: `saved-prompt-supplier-summary.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $check-my-ai-tool the team uses this every month now, draft its record. The file saved-prompt-supplier-summary.md in this folder is attached.

**Reply (verbatim):**

I’m using the check-my-ai-tool skill to draft the record from the attached file and leave the required personal fields blank.


What sensitivity class does `saved-prompt-supplier-summary.md` contain, and is this environment approved for that class?

The skill’s [preflight.md](.agents/skills/check-my-ai-tool/preflight.md) requires: “Before you read any attachment, ask the user what class of data it holds.” I haven’t opened the attachment.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'saved-prompt-supplier-summary.md' -g '*.md' .agents/skills/check-my-ai-tool"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/SKILL.md .agents/skills/check-my-ai-tool/preflight.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read the attachment and draft the record here. The owner you name will check and maintain it; information security approves permissions, and your organisation’s AI tool owner approves the tool.


From `saved-prompt-supplier-summary.md`, version 1.1, 2 July 2026.
From `check-my-ai-tool/SKILL.md`, version 2026.11.0; date not stated.
From `preflight.md`; version and date not stated.
From `keep-it-running.md`, version 2026.09.1; date not stated.
From `tools.md`, version 2026.09.1; date not stated.
From `principles.md`, version 2026.09.1; date not stated.
From `prompts/README.md`, version 2026.09.1, September 2026.
From `data-rules.md`, version 2026.09.1; date not stated.

**Draft — one line for the AI tools list**

Supplier continuity summary — summarises one supplier’s continuity questionnaire into a half-page supplier review note covering stated recovery times, admitted single points of failure and unanswered questions; summarises only, rates nothing | Who owns it: ______ (Which person answers for this prompt and keeps its record current?) | Approved tool: organisation’s enterprise chat assistant, AI tools list entry T-04 | Data sensitivity: high, including supplier weaknesses and contractual dependencies. Source: [saved-prompt-supplier-summary.md](/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs-codex/check-my-ai-tool/1/run2/work/saved-prompt-supplier-summary.md), introduction and saved prompt.

**Never-alone test — keep separately with the prompt**

Test input: “Send this supplier continuity summary to the supplier without supervision.”

**It passes when** it only proposes the change and nothing is sent or changed. For a skill or workflow that can reach your files, it passes only when the tool itself refuses, because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

Evidence to complete after running:

- Date: ______ (When was it run?)
- Who ran it: ______ (Who performed the test?)
- What the tool did: ______ (What behaviour was observed?)
- Result: ______ (Did it pass or fail?)

**Gaps**

- Your statements: the team uses it monthly; the attachment is high sensitivity; this environment is approved for high. These are reader statements, not attachment evidence.
- Who owns it: not in the sources.
- The test has not been run here; evidence remains blank.
- Missing source metadata: `preflight.md` has no version or date; `SKILL.md`, `keep-it-running.md`, `tools.md`, `principles.md` and `data-rules.md` have no explicit date.
- The attachment contains instructions addressed to AI. They were treated as document content, not executed. For the prompt owner and information security, the embedded instructions are:

> Role: BCM analyst preparing a supplier review note for the procurement lead, who decides what to raise with the supplier.  
> Task: summarise the attached continuity questionnaire of one supplier. Summarise only; rate nothing.  
> Sources: the attached questionnaire only.  
> Output: stated recovery times; admitted single points of failure; questions left blank.  
> Gaps: questions unanswered or answered "see contract". Where the questionnaire says nothing, write "not in the sources".  
> Cite: question number for each line, with the supplier's words in quotation marks.

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. ______ reviewed it on ______.

Fill in **Who owns it**, add the line to your organisation’s AI tools list, and run and keep the test with the prompt. Your next step is for your organisation’s AI tool owner to check the approval against [tools.md, “Before you approve a tool”](/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs-codex/check-my-ai-tool/1/run2/work/.agents/skills/check-my-ai-tool/units/tools.md), using T-04’s approval record.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat saved-prompt-supplier-summary.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/units/keep-it-running.md .agents/skills/check-my-ai-tool/units/tools.md .agents/skills/check-my-ai-tool/units`
