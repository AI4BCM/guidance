# $learn-bcm case 4b, run1: Codex, guidance at c332ccc

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9c0-b69d-7532-8839-2484a0e82d46`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you teach me what a BIA asks for and then quiz me on it?

**Reply (verbatim):**

I’ll use the BIA facilitation skill to explain what a Business Impact Analysis asks for, then quiz you one question at a time.

A **Business Impact Analysis (BIA)** asks: **If our work is interrupted, how do the consequences grow over time—and how soon must we resume it?**

It helps an organisation set recovery priorities. Here’s what it asks for:

| What it asks | What your answer should explain |
|---|---|
| **What do we deliver?** | The products or services customers and other stakeholders depend on, then the activities supporting them. |
| **What happens if that work stops?** | Financial losses, harm to people, legal or contractual breaches, customer disruption, and reputational damage. |
| **How do impacts change over time?** | What happens after a few hours, a day, or several days—including busy periods and deadlines. |
| **When does the impact become unacceptable?** | The **maximum tolerable period of disruption (MTPD)**, with a reason for that limit. |
| **How soon must we resume, and at what level?** | A **recovery time objective (RTO)** shorter than the MTPD, plus the minimum acceptable service level. |
| **What do we need to resume?** | People, premises, systems, information, equipment, suppliers, and dependencies on other activities. |
| **How much data loss can we tolerate?** | Where relevant, a **recovery point objective (RPO)**: the acceptable period of lost data. |

For example, a payroll BIA might find that missing payday causes unacceptable harm. Its tolerable disruption therefore depends on **when the interruption occurs**. Recovery must leave enough time to check and submit payments, using the necessary staff, payroll records, systems, and banking service.

Two distinctions matter:

- **BIA examines consequences over time.** Risk assessment examines what could cause disruption and how likely it is.
- **Recovery requirements are business needs.** Whether current arrangements can meet them is a separate question. Every timeframe needs a rationale, and management endorses the priorities.

Let’s quiz you one question at a time. I’ll give feedback after each answer.

**Question 1:** Someone says, “Our BIA should start by listing cyberattacks, fires, and floods and estimating their likelihood.”

What would you change about that approach, and what should the BIA ask first?

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat /home/brain/.codex/skills/role-bia-facilitation/SKILL.md'`
