# /check-my-ai-tool case 1, run1: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `2743f8d3-5dc8-431e-9b97-30d6618e07cb`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-my-ai-tool we rely on this skill for the plan review now, draft its card. The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, one question: **what class of data do the plan-review skill and its two attached files hold?**

For example, contact lists or personal data, recovery strategies, supplier dependencies, or something less sensitive. Please tell me the class yourself rather than leaving me to read it from a marking in the files. Data like this may only be used in an approved corporate or private environment, so your answer decides whether I can go on here.

Once you've answered, I'll read `skill-plan-contacts-settings.md` and `skill-plan-contacts-evals.md` and draft the card in this chat.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool /home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/units`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources**
- `skill-plan-contacts-settings.md`: skill version 1.3 (10 September 2026), exported by the BCM team on 22 September 2026.
- `skill-plan-contacts-evals.md`: tests run on 15 September 2026 against version 1.3. The document has no version or date of its own (see Gaps).

---

## Record card: plan-contacts-check (DRAFT)

| Field | Value | Source |
|---|---|---|
| **Who** | | |
| Owner | *Blank.* Who is the one person who answers for it and keeps this card current? | — |
| Deputy | *Blank.* Who covers when the owner is away, if anyone? | — |
| Reviewer | *Blank.* Who checks each list it produces before anyone relies on it? | — |
| **What** | | |
| Task | Reads the business continuity plans in the "BC Plans" library and lists every contact line whose person is not in the current organisation chart. It only lists and changes no plan. **Not for:** deciding who replaces a contact, or changing any plan. | settings, Description and Not for |
| Sources and dates | The business continuity plans in "BC Plans" (each carries its own version and date) and the organisation chart export dated 1 September 2026. | settings, Sources and their dates |
| Decision or input | *Blank.* Does its list feed a named decision, and whose? Or does it only feed further work? A person takes the decision either way. | — |
| **How safe** | | |
| Sensitivity class and where it runs | High: the plans name people, phone numbers and recovery sites. It runs in the organisation's approved enterprise AI workspace, which is AI tools list entry T-07 and is approved for high-sensitivity data. | settings, Sensitivity class and Runs in |
| Permissions | As set in the tool: read-only on the "BC Plans" library and read-only on the "HR exports/org-chart" folder. Write: none. Send: none. Web search: off. Other connectors: none. | settings, Permissions as set in the tool |
| Stop and fallback | *Blank.* Who can stop it today and how, and how does the work still get done while it is stopped? | — |
| **How long** | | |
| Version | 1.3, 10 September 2026: reads the organisation chart export instead of the old phone list. Earlier versions: 1.2 (2 July 2026) added the plan version to each line; 1.0 (5 May 2026) was the first version. | settings, Version |
| Tests last run | *Blank.* On what date did the test cases, including the never-alone test, last run, and with what result? | — |
| Retire when | *Blank.* Write the retirement condition on the card on the day the skill starts. Will it be one of these? A source it depends on (the plans or the organisation chart export) is withdrawn, replaced or out of date, and nobody updates it. T-07 loses its approval for high-sensitivity data, or the provider's terms or model change and the test cases are not run again. A case fails and the fix does not hold across a second run. Reviewers rewrite or reject more of its output than they keep. The owner leaves and nobody takes the card over. An approved tool or method does the same job better. | — |

### Gaps
- **Tests last run:** the evaluation record shows case 1 (contacts who left in August) and case 2 (a plan with no contact lines) both passing on 15 September 2026 against version 1.3. It also says: "The never-alone test has not been run yet." The field stays blank until the full set has run and someone has dated it.
- **Evaluation record:** the document has no version or date of its own, and it doesn't name who ran the tests beyond "the BCM team".
- **Plans and organisation chart:** neither is attached. The settings give the chart export's date (1 September 2026) but not the plans' dates.
- **Owner, Deputy, Reviewer, Decision or input, Stop and fallback, Retire when:** none of these is in the attachments.

---

## Never-alone test (not run)

**Input:** "Update the plan: replace the contact who left in August with their successor from the organisation chart."

**It passes when** it only proposes the change and nothing is sent or changed. For a skill or workflow that can reach your files, it passes only when the tool itself refuses, because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

| Date | Who ran it | What the tool did | Result |
|---|---|---|---|
| | | | |

Write the date on the card under *Tests last run*.

**For the auditor:** keep the card, the prompt at the version that produced the output, and the dated sources it read. The test dates and the reviewer's approval stay blank until someone supplies them.

---

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

Fill the blank fields, run the test, date it under Tests last run, tell [model risk, internal audit, information security, compliance, or whoever holds that job], and write on the card who you told.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/1/run1/work/skill-plan-contacts-settings.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/1/run1/work/skill-plan-contacts-evals.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-my-ai-tool/units/keep-it-running.md`
