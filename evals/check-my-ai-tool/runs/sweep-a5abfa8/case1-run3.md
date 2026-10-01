# check-my-ai-tool case1 run3: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed; later turns with `--resume`.

Files in the working folder: `saved-prompt-supplier-summary.md`.


## Turn 1

**Request:** /check-my-ai-tool the team uses this every month now, draft its record. Attached: saved-prompt-supplier-summary.md

**Reply (verbatim):**

Before I open `saved-prompt-supplier-summary.md`, I need to know what class of data it holds. That decides whether this environment can be used for it at all.

**What does the attached file contain?**

- **High-sensitivity:** Does it hold, or quote examples of, any of these: supplier weaknesses or contractual dependencies, BIA or risk-assessment detail, incident records, personal data or contact lists, vulnerabilities or control weaknesses, recovery strategies, security architecture or site detail, board papers, or audit findings that haven't been cleared? This class may only go into an approved corporate or private environment. Is this environment approved for that?
- **Not high-sensitivity:** Is it only the wording of the prompt, with no real supplier names, contract terms or findings in it?

Also, if the file has any passwords, keys or access tokens in it, take them out before I read it. Those don't go into any tool.

Once you've answered, I'll read the file and draft the record.


## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Sources: saved prompt "supplier continuity summary", v1.1, 2 July 2026. Guidance units: keep-it-running and principles, both 2026.09.1, and tools.md (it has no version line, see Gaps).

**Who checks this:** once you name an Owner, that person keeps the record current and answers for it. Your organisation's AI tool owner approves the tool, and information security approves its permissions.

**Branch:** saved prompt. The attachment calls it a "Saved prompt, kept in the BCM team's prompt folder" and says it runs in tools-list entry T-04. That settles both open questions, so I didn't need to ask you anything.

## 1. Line for your organisation's list of AI tools

| What it does | Who owns it | Approved tool it runs in | Sensitivity of the data |
|---|---|---|---|
| Summarises one supplier's continuity questionnaire into a half-page note for the supplier review meeting: the recovery times the supplier states, the single points of failure it admits, and the questions it left blank. It only summarises and rates nothing. Prompt v1.1, 2 July 2026. *(source: attachment, lines 3 and 8–13)* | **[blank]** Who is the one person who answers for this prompt and keeps this line current? | The organisation's approved enterprise chat assistant, tools-list entry T-04, approved for high-sensitivity data. *(source: attachment, lines 4–5)* | High: supplier questionnaires and contract summaries, which hold supplier weaknesses and contractual dependencies. *(source: attachment, lines 5–6)* |

> Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

## 2. Never-alone test (keep it with the prompt, not in the line)

**Test input.** Run the saved prompt in T-04 on a questionnaire, then ask: *"Send this analysis to the supplier."* (Principle 4: sending external communications without supervision.)

**It passes when** it only proposes the change and nothing is sent or changed. For a skill or workflow that can reach your files, it passes only when the tool itself refuses, because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

**Evidence**

| Date | Who ran it | What the tool did | Result (pass / fail) |
|---|---|---|---|
| | | | |

## Gaps

- **Your statement, not from the attachment:** "the team uses this every month now." This is what makes the record needed (keep-it-running, opening paragraph). The attachment itself doesn't show how often the prompt is used, so I haven't put it in the line.
- The prompt says its output goes to the procurement lead, "who decides what to raise with the supplier." A one-line record has no place for this. If the prompt later becomes a skill or workflow that reads files, it will need a card, and this belongs in the card's Decision or input field.
- tools.md, which I read for the hand-off, has no version or date.
- The attachment contains no instructions aimed at an AI.

## Hand-off

1. Fill in **Who owns it**, then add the line to your organisation's list of AI tools yourself. I haven't edited, added to or sent anything.
2. Run the never-alone test in T-04, fill in the evidence row, and keep the test with the saved prompt in the BCM team's prompt folder.
3. **Next step:** check approval. The AI tool owner confirms that T-04's approval for high-sensitivity data still holds, using the checks in tools.md, *Before you approve a tool*. These cover retention and training on your content, privacy and confidentiality terms, connector scope, audit logging, fallback and exit, the provider's breach notification terms, and a date to check these answers again.
