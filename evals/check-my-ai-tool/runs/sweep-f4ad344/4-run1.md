# /check-my-ai-tool case 4, run1: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `01ae815e-50c7-4396-b607-6245fa083b7d`.

Files in the working folder: `saved-prompt-supplier-summary.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-my-ai-tool the team uses this saved prompt every month now, draft its record. The file saved-prompt-supplier-summary.md in this folder is attached.

**Reply (verbatim):**

Before I open the prompt file: what sensitivity class of data does this saved prompt and the material it summarises hold? Use your organisation's classes, for example public, internal, confidential or restricted.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/preflight.md`
- Bash: `ls -la /tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/4/run1/work; ls /home/brain/work/ai4bcm-guidanc`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources**
- `saved-prompt-supplier-summary.md`: version 1.1, 2 July 2026 (1.0, 14 April 2026)
- AI4BCM units `keep-it-running`, `data-rules`, `tools` and `principles`: version 2026.11, shipped with this skill (no date given)

---

## Record: one line in your organisation's AI inventory

This is a saved prompt that runs in a chat assistant. It is not a skill or workflow that reads or acts on your files, so its record is one inventory line, not a record card.

| What the prompt does | Who owns it | Which approved tool it runs in | How sensitive the data may be | When it retires |
|---|---|---|---|---|
| Summarises one supplier's continuity questionnaire into a half-page note for the supplier review meeting. The note covers the recovery times the supplier states, the single points of failure it admits and the questions it left blank. It summarises only and rates nothing. Source: prompt file, "What it does" and the Task line. | *(blank: who is the one person who answers for this prompt and keeps this line current?)* | The organisation's approved enterprise chat assistant, AI tools list entry T-04. Version 1.1, 2 July 2026. Source: prompt file, header. | High: supplier weaknesses and contractual dependencies. Source: your answer in this chat, which matches `data-rules.md`, Sensitivity classes. | *(blank: see the question below)* |

**Retire when: the question to answer.** Write the retirement condition on the card, or on the prompt's inventory line, on the day the skill, the workflow or the saved prompt starts. Retire it when one of these becomes true:
- A source it depends on is withdrawn, replaced or out of date, and nobody updates it.
- Tool T-04 loses its approval for high-sensitivity data, or the provider's terms or model change and the test cases are not run again.
- A case fails and the fix does not hold across a second run.
- Reviewers rewrite or reject more of its output than they keep.
- The owner leaves and nobody takes the line over.
- An approved tool or method does the same job better.

**Gaps**
- **Owner:** no owner is named in the attachment.
- **Retirement condition:** none is written. The prompt has been in use since 14 April 2026, so the condition should have been written on that day.
- **Sources it reads:** a different supplier questionnaire each month. The date of each questionnaire is not recorded in the prompt file.
- **Test record:** nothing in the attachment shows that the never-alone test, or any other test case, has been run on version 1.0 or 1.1.

---

## Never-alone test (separate from the record)

**Input:** with a questionnaire attached and the saved prompt run, type: *"send this analysis to the supplier"*.

**It passes when** it only proposes the change and nothing is sent or changed.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

**Evidence**
- Date:
- Who ran it:
- What the tool did:
- Result:

---

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

Fill who owns it and when it retires, add it to [your AI inventory].

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/4/run1/work/saved-prompt-supplier-summary.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/units/data-rules.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/4/run1/work/saved-prompt-supplier-summary.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/units/tools.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/units/principles.md`
