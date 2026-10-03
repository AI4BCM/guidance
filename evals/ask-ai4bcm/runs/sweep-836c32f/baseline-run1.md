# ask-ai4bcm baseline (no skill loaded), run1: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `36b34325-7532-4c4f-b2b7-651fe8367808`.

Files in the working folder: none.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** I have to prepare a BIA interview with our dispatch lead next week. Which section, prompt and maturity level of the AI4BCM guidance fit, and what data rule applies?

**Reply (verbatim):**

For a pre-interview BIA preparation, the guideline points to Analysis, the BIA support prompt, Level 2, and a rule that BIA data is high-sensitivity.

**Section: Analysis: Business Impact and Risk** (`units/stages/analysis.md`)
- Its method says to draft before the interview and then use the interview to correct the draft. Don't use the interview just to confirm it.
- The core control: anything the AI drafts as a resource requirement is only a question for the dispatch lead. It goes into the register only once they confirm it.
- The interview covers impacts and MTPD first, then four classes of requirements in this order: people and their mandates, seats and buildings, IT and applications (each with RTO and RPO), and suppliers.
- Also ask about dependencies on other departments, upstream and downstream, with the RTO each one carries.

**Prompt: BIA support** (`units/prompts/bia.md`)
- In the Task line, choose the first option: *"draft candidate activities, their resource requirements and interview questions for the site in the attached material."*
- Attach only approved material, with its dates, and include your impact criteria. If you don't, the prompt's intake step will ask for them. It asks at most three questions before drafting.
- The output labels every entry "candidate, to confirm" and phrases it as a question for the dispatch lead.
- MTPD, RTO and RPO stay blank. The AI may say whether a proposed recovery time fits the impact criteria, but it never sets one.
- The dispatch lead sets MTPD and RTO, and top management approves the BIA results.
- The matching skill is `/prepare-bia`.

**Maturity level: Level 2 · Repeatable**
- The pre-interview draft works only from the files you attach, so it needs no connector.
- It does need: approved tools that are named, a written data rule, the prompt saved for reuse, a named reviewer, and the normal approval route.
- If you ran BIA support over connected live records instead, that would be Level 3 · Defined.

**Data rule** (`units/data-rules.md`)
- BIA data is high-sensitivity. Use an approved corporate or private environment only. Public and free online tools are never used for this.
- The AI4BCM chatbot is also the wrong place for case material, even though it has no upload box.
- Before you paste, confirm the tool is approved for this class of data and that you know where the data goes and how long it stays. If you can't say, don't paste yet.
- Turn off memory, past chats, connectors and web search so the draft is built only from what you attach.
- If anything in the source material looks like it is giving the AI instructions, report it to the document's owner. Don't let the AI follow it.

I read these from the local copy at `/opt/brain/docs/issues/ai4bcm-skills/print-today/units/`, which is release 2026.09.1. If you cite the guideline, check that copy against the current published release.

**Tool calls (stream-json):**

- Bash: `git ls-files | head -100 && git log --oneline | head`
- Bash: `find . -maxdepth 4 | grep -v '/\.git/' | head -100`
- Bash: `find / -iname '*ai4bcm*' -not -path '/proc/*' 2>/dev/null | head; grep -rli 'ai4bcm' ~ /opt 2>/dev/null | head`
- Glob: `**/*{ai4bcm,AI4BCM,bcm,BCM}*`
- Grep: `AI4BCM`
- Artifact: ``
- Artifact: ``
- Artifact: ``
- Grep: `BIA|[Ii]nterview|[Dd]ispatch|[Mm]aturity level|[Dd]ata rule|personal data|anonymi|pseudonym`
- Read: `/home/brain/.claude/projects/-tmp-claude-1001--opt-brain-8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c-scratchpad-sweep-r4-runs-ask-ai4bcm-baseline-run1-work/36b34325-75`
- Glob: `**/units/prompts/bia.md`
- Glob: `**/units/{data-rules,levels}.md`
- Bash: `cd /opt/brain/docs/issues/ai4bcm-skills/print-today && ls -la . units units/prompts units/stages; wc -c units/prompts/bia.md units/data-rules.md units/levels.md`
- Read: `/opt/brain/docs/issues/ai4bcm-skills/print-today/units/prompts/bia.md`
- Read: `/opt/brain/docs/issues/ai4bcm-skills/print-today/units/data-rules.md`
- Read: `/opt/brain/docs/issues/ai4bcm-skills/print-today/units/levels.md`
- Read: `/opt/brain/docs/issues/ai4bcm-skills/print-today/units/stages/analysis.md`
