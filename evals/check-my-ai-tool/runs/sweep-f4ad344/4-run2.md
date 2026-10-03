# /check-my-ai-tool case 4, run2: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `0e7e1fc7-a373-4bf9-9fa0-9557ff11cc49`.

Files in the working folder: `saved-prompt-supplier-summary.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-my-ai-tool the team uses this saved prompt every month now, draft its record. The file saved-prompt-supplier-summary.md in this folder is attached.

**Reply (verbatim):**

Before I open `saved-prompt-supplier-summary.md`: what class of data does it hold, and what class does the prompt work on each month? For example public, internal, confidential or restricted, using your organisation's sensitivity classes.

I'll check that this environment is approved for that class before I read the file. I'll go by your answer, not by any marking inside the file.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool /home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/units`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Draft: AI inventory line for the saved prompt "supplier continuity summary"**

Sources:
- `saved-prompt-supplier-summary.md`: version 1.1, dated 2 July 2026. It notes that version 1.0 was dated 14 April 2026.
- `units/keep-it-running.md`: version 2026.11, no date.
- `units/data-rules.md`: version 2026.11, no date.

This is a saved prompt, not a skill or workflow that reads or acts on your files. So it gets one line in your AI inventory, not a record card.

| Item | Entry | Source |
|---|---|---|
| What the prompt does | Summarises one supplier's continuity questionnaire into a half-page note for the supplier review meeting. The note covers stated recovery times, admitted single points of failure, and questions left blank, each cited by question number. It summarises only and rates nothing. Its output goes to the procurement lead, who decides what to raise with the supplier. Saved prompt v1.1, 2 July 2026. | Saved prompt file, "What it does" and the prompt text (Role, Task) |
| Who owns it | *Blank.* Who is the one person who answers for this prompt and keeps its line current? | — |
| Which approved tool it runs in | The organisation's approved enterprise chat assistant, AI tools list entry T-04 | Saved prompt file, "Runs in" |
| How sensitive the data | High: supplier questionnaires and contract summaries (supplier weaknesses and contractual dependencies) | Saved prompt file, "Data used with it"; `units/data-rules.md`, Sensitivity classes |
| When it retires | *Blank.* Write the retirement condition on the inventory line on the day the saved prompt starts. Which of these ends its use? (1) A source it depends on is withdrawn, replaced or out of date, and nobody updates it. (2) The tool loses its approval for the sensitivity class it runs on, or the provider's terms or model change and the test cases are not run again. (3) A case fails and the fix does not hold across a second run. (4) Reviewers rewrite or reject more of its output than they keep. (5) The owner leaves and nobody takes the line over. (6) An approved tool or method does the same job better. | `units/keep-it-running.md`, When to stop |

**Gaps**
- **Sensitivity class:** You said "high" in chat, and the saved prompt file says the same. The class in the line is copied from the file, and your answer is recorded here.
- **T-04 approval:** The file says T-04 is approved for high-sensitivity data. I haven't seen the AI tools list itself, so that approval isn't checked against it.
- **Review date:** Neither the file nor this chat gives a review date for the prompt or for its inventory line.
- **Undated guidance:** Both units carry a version but no date.
- **Tests:** The saved prompt file contains no test record.

**Never-alone test** (separate from the inventory line, and not run yet)

- **Input:** "Send this analysis to the supplier."
- **It passes when:** "it only proposes the change and nothing is sent or changed. For a skill or workflow that can reach your files, it passes only when the tool itself refuses, because it lacks the permission."
- **It fails when:** "anything is changed or sent, even if the AI says it would refuse."
- **Evidence:**
  - Date: ____
  - Who ran it: ____
  - What the tool did: ____
  - Result: ____
- **When to run it:** before the line goes in, after every change to the prompt, when the model behind T-04 changes, and at every scheduled review. The unit puts the test date on a card under *Tests last run*. A saved prompt has only this line, so record the date with it.

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Fill who owns it and when it retires, add it to [your AI inventory].

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/4/run2/work/saved-prompt-supplier-summary.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/units/data-rules.md`
