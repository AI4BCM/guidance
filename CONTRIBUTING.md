# Contributing

Corrections are welcome from anyone who uses this guidance in practice. A finding from one BCM
manager who ran a prompt against a real inventory is worth more here than a stylistic pass.

## Terms

This guidance is published under CC BY 4.0, and anything you send is accepted under the same
licence. By opening a pull request you agree that your contribution may be published under CC BY 4.0
with attribution to the guidance as a whole, in the form of the citation line at the foot of every
unit:

> Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.

Send only material you are free to license this way. Do not paste text from a standard, a
professional body's publication or your employer's documents into an issue or a unit; describe the
requirement in your own words instead, and name the source so it can be checked. Do not put your
organisation's data, supplier names or site detail in an issue: the same rule the guidance gives its
readers in `units/data-rules.md` applies to the guidance's own issue tracker.

## How a correction arrives

1. Open an issue quoting the unit and the line, or the print sheet and the paragraph. One issue per
   change.
2. Say what is wrong, and what it should say. A replacement sentence settles a question that a
   report of unease leaves open.
3. If you have the fix, send it as a pull request against `main`, one unit per pull request where
   that is possible.

Length is a measurement here. Earlier editions of this repository carried per-unit word caps and
those caps no longer apply. Keep the citation line at the foot of every unit, keep the `<!-- meta -->`
anchor at the top, and do not duplicate an explanation that already has a home in another unit —
point at it.

## Who decides what

`units/prompts/` is the living part of the guidance. Its owner is Konstantin Gerner, who edits the
prompts, keeps their dates current and decides what a prompt asks for. A prompt changes when
practice or the models change, which is more often than the rest of the guidance moves.

The five principles, the five maturity levels, the six lifecycle stages and the rule that people
decide, approve and act are the settled design of this edition. A pull request that reopens one of
them is a discussion first: open an issue.

## Review cycle

Issues and pull requests are read as they arrive. Accepted changes are folded into the next calendar
release, tagged `YYYY.MM`; a citation that names a tag names the text as it stood at that tag, and
`releases/<tag>.json` resolves the tag to a commit and to a hash per citable file. What each release
contains, and the citation form: `CHANGELOG.md`. The current cycle runs to the `2026.11` release,
with contributor comments closing 27 October 2026.
