# $learn-bcm case 4b, run3: Codex, guidance at c332ccc

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9c1-7b62-7530-a515-24f738e039a8`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you teach me what a BIA asks for and then quiz me on it?

**Reply (verbatim):**

I’ll use the BIA facilitation skill to explain what a Business Impact Analysis asks for, then quiz you one question at a time.

A **Business Impact Analysis (BIA)** asks: **“If our work stops, how do the consequences grow over time—and what must we recover, by when?”** It helps an organisation set recovery priorities.

Here’s what it asks you to explain:

| What it asks for | Example: an online retailer |
|---|---|
| **Products and services, then supporting activities** | Delivering customer orders depends on order processing and warehouse picking. |
| **Impacts over time** | After 4 hours, orders queue; after 24 hours, delivery promises are missed; after 3 days, refunds and lost customers increase. |
| **When impacts become unacceptable, and why** | Beyond 48 hours, missed contractual commitments become unacceptable. This is the **maximum tolerable period of disruption (MTPD)**. |
| **How soon work needs to resume** | Restore order processing within 12 hours. This is the **recovery time objective (RTO)**, which must sit inside the MTPD. |
| **The minimum acceptable operating level** | Initially, process 40% of normal orders, prioritising urgent deliveries. |
| **Dependencies and resources needed** | Staff, order data, IT systems, premises, couriers and suppliers—with minimum quantities where possible. |
| **Acceptable data loss, where relevant** | Lose no more than one hour of order data. This is the **recovery point objective (RPO)**. |

Impacts can include financial losses, harm to people, legal or regulatory consequences, service failures and reputational damage. Timing matters: a disruption during peak season may hurt much faster.

Every estimate needs a **reason or evidence**. “We’re critical; we need everything immediately” doesn’t establish a defensible priority. Management reviews and endorses the resulting priorities; recovery planning then works out how to meet them.

A useful distinction: **BIA examines the consequences of disruption over time. Risk assessment examines threats and their likelihood.**

Let’s quiz you one question at a time. I’ll give feedback after each answer.

**Question 1:** A payroll manager says, “Our biggest concern is ransomware; I think it’s likely this year.”

What would you ask next to learn about the **business impact** of payroll being unavailable?

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat /home/brain/.codex/skills/role-bia-facilitation/SKILL.md'`
