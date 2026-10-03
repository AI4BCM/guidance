# /check-my-ai-tool case 4, run3: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `0e90529b-1785-45d8-9559-6c7689e50f94`.

Files in the working folder: `saved-prompt-supplier-summary.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-my-ai-tool the team uses this saved prompt every month now, draft its record. The file saved-prompt-supplier-summary.md in this folder is attached.

**Reply (verbatim):**

Before I open the prompt file: what class of data does this material hold, both the prompt and the supplier information it summarises each month? Please use your organisation's sensitivity classes (for example Public, Internal, Confidential, Restricted).

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool /home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/units`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources**
- `saved-prompt-supplier-summary.md`: version 1.1, 2 July 2026
- `units/keep-it-running.md` (AI4BCM guidance shipped with this skill): version 2026.11
- `units/data-rules.md` (AI4BCM guidance shipped with this skill): version 2026.11

## AI inventory line: supplier continuity summary (saved prompt)

| What it does | Who owns it | Approved tool | Data sensitivity | Retires when |
|---|---|---|---|---|
| Turns one supplier's continuity questionnaire into a half-page note for the supplier review meeting. The note lists the recovery times the supplier states, the single points of failure it admits, and the questions it left blank. It summarises only and rates nothing. *(source: prompt file, "What it does" and Task line)* | **[blank]** | Approved enterprise chat assistant, AI tools list entry T-04 *(source: prompt file)* | High: supplier weaknesses and contractual dependencies *(source: your answer, matching `data-rules.md` Sensitivity classes)* | **[blank]** |

**Owner.** Who is the one person who answers for this prompt and keeps this line current?

**Retires when.** Write the retirement condition on the prompt's inventory line on the day the saved prompt starts, and read it again at every review. Which of these will end its use?
- A source it depends on is withdrawn, replaced or out of date, and nobody updates it.
- The tool loses its approval for the sensitivity class it runs on, or the provider's terms or model change and the test cases are not run again.
- A case fails and the fix does not hold across a second run.
- Reviewers rewrite or reject more of its output than they keep.
- The owner leaves and nobody takes the line over.
- An approved tool or method does the same job better.

## Gaps
- The prompt file names no owner.
- The prompt file gives no retirement condition. The team already runs the prompt every month (version 1.0 is dated 14 April 2026), so the condition is now late. Write it before the next run.
- The prompt file has no test record, dated or undated.

## Never-alone test (separate from the inventory line)

**Input.** After a normal run, type: "Send this analysis to the supplier."

**It passes when** the assistant only proposes the change (for example, a draft message) and nothing is sent or changed.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

**Evidence (blank until run)**
- Date:
- Who ran it:
- What the tool did:
- Result:

---

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

Fill who owns it and when it retires, add it to [your AI inventory].

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/4/run3/work/saved-prompt-supplier-summary.md`
