# $learn-bcm case 4b, run2: Codex, guidance at c332ccc

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9c0-ddd5-7cf1-9c7d-32af1b0e13ad`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you teach me what a BIA asks for and then quiz me on it?

**Reply (verbatim):**

I’ll use the BIA facilitation skill to explain what a Business Impact Analysis asks for, then quiz you one question at a time.

A **Business Impact Analysis (BIA)** asks: **If our work is interrupted, how do the consequences grow over time, and how quickly must we recover?**

Start with the products or services the organisation delivers, then identify the activities that support them. For each activity, a BIA asks for:

| What it asks | Example: processing payroll |
|---|---|
| **What is delivered, and to whom?** | Employees receive accurate pay on time. |
| **What happens if it stops, over time?** | A short delay may be manageable; missing payday causes employee hardship and possible legal consequences. |
| **When do impacts become unacceptable?** | The deadline beyond which disruption cannot be tolerated: **MTPD**, maximum tolerable period of disruption. |
| **How quickly must it resume?** | **RTO**, recovery time objective—a target earlier than the MTPD, leaving time to catch up. |
| **What minimum level must resume?** | Enough capacity to pay everyone due, even if other payroll tasks wait. |
| **What does recovery depend on?** | People, payroll data, systems, bank access and suppliers. |
| **How much data loss is tolerable, where relevant?** | **RPO**, recovery point objective—how far back recovered data may go. |

Two habits make the answers useful: **explain the reason behind every timeframe**, and **consider the worst timing**, such as an interruption just before payday.

A BIA examines consequences of disruption. A risk assessment examines causes and likelihood. BIA findings inform recovery priorities, which management reviews and endorses; they do not prove the organisation can actually recover that quickly.

Let’s quiz you one question at a time. I’ll give feedback after each answer.

**Question 1:** Someone writes in a BIA: “Payroll is critical because ransomware is likely.”

What is missing from that answer, and what would you ask them next?

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat /home/brain/.codex/skills/role-bia-facilitation/SKILL.md'`
