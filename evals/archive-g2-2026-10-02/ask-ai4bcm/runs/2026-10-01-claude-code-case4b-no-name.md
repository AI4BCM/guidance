# ask-ai4bcm case4b-no-name: Claude Code 2.1.284, 2026-10-01

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** which unit and prompt fit a BIA interview?

**Reply (verbatim):**

For a BIA interview, use the **Analysis stage unit** together with the **BIA support prompt**.

**Unit: `stages/analysis.md` (Analysis: Business Impact and Risk)**
- Its Method section puts the interview at step 3, after a draft prepared from your sources (step 2). The draft is there to be corrected in the interview, not just confirmed. Note down whatever the draft couldn't have known.
- It sets the interview order. Settle the impacts and the MTPD first. Then cover the four requirement classes: people and mandates, then seats and buildings, then IT and applications (each with RTO and RPO), then suppliers. Dependencies on other departments are a separate item.
- The full five-stage BIA workflow (scope, structured interview, template, requirements, consolidation) is in `workflow-design.md`.

**Prompt: `prompts/bia.md` (BIA support)**
The Task line offers two choices, depending on where you are relative to the interview:
- **Before the interview:** "draft candidate activities, their resource requirements and interview questions for the site in the attached material". This produces the interview guide, and it's the choice the Analysis case example uses.
- **After the interview:** "assess this activity's impacts, resource requirements and assumptions from the attached interview record".

Before it starts, the prompt asks you up to three questions about what the attached material leaves open. If you haven't attached impact criteria, one of those questions asks for them.

There is also a skill for the pre-interview draft: `/prepare-bia` drafts the interview guide from your material.

**Rules that apply either way:**
- Every requirement the AI drafts is only a question for the activity owner. It enters the register only once the owner confirms it.
- MTPD, RTO and RPO stay empty. The owner sets them, and top management approves the BIA results.
- Live BIA data goes only into an approved environment.

Both files are under `/opt/brain/docs/issues/ai4bcm-skills/print-today/units/`.


## Tool calls in the stream (turn 1)

- `Bash {"command": "git ls-files | head -100 && ls -la", "description": "List repository files"}`
- `Bash {"command": "cd /tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/evals/ask-ai4bcm && `
- `Glob {"pattern": "**/*", "path": "/tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/evals/a`
- `Grep {"pattern": "BIA|business impact", "path": "/opt/brain", "-i": true, "head_limit": 40}`
- `Read {"file_path": "/opt/brain/docs/issues/ai4bcm-skills/print-today/units/prompts/bia.md"}`
- `Read {"file_path": "/opt/brain/docs/issues/ai4bcm-skills/print-today/units/prompts/README.md"}`
- `Read {"file_path": "/opt/brain/docs/issues/ai4bcm-skills/print-today/units/stages/analysis.md"}`

No `Skill` call; no read of `ask-ai4bcm/SKILL.md`.
