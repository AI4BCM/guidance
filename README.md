# AI4BCM guidance — machine edition

The machine edition of the AI4BCM guidance: one markdown unit per topic, sized so a
model can read a whole unit and cite it. The same markdown is the source for the
print edition (an eight-page PDF at `ai4bcm.org/guidance`), so text is written once
and published twice.

> Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.

## The three ways in

- **Guidance chatbot** — ask the guidance questions in the browser; it reads nothing of yours.
- **`/ask-ai4bcm` skill** — a router you invoke in your own assistant; it points you at the unit, the prompt and the maturity level for your situation, and reads your files inside your own tenant.
- **BIA workflow** — the five-stage business impact analysis run against your own process data.

## Layout

- `units/` — the guidance itself, one file per topic. See [units/README.md](units/README.md).
- `ask-ai4bcm/` — the router. See [ask-ai4bcm/README.md](ask-ai4bcm/README.md).

## Sending changes

Open an issue for anything wrong, missing or unclear, quoting the unit and the line.
Send corrections as a pull request against `main`; keep each unit inside its word cap
(the caps are listed in `units/README.md`) and leave the citation line at the foot of
every unit intact.

## Releases

Releases are tagged by calendar month, `YYYY.MM`. The first is `2026.09`; the next is
`2026.11`. One tag covers all four outputs — the PDF, these units, the skill pack and
the chatbot — so a citation naming a tag names the same text everywhere.

## Licence

CC BY 4.0. See [LICENSE](LICENSE).
