---
status: accepted
---

# A part is a reading step, not a unit

From release `2026.11` the print edition and the website follow a red thread of eight **parts**,
0 to 7, each answering one reader question: is this for me, what must I remember, where do I stand,
which rules can I never break, where in my BCM work does AI help, what do I type, which tool may I
use, and how do I keep it running and defend it. The units keep their files and their headings; only
the print order and the site's `READING_ORDER` and groups change (owner, 2026-09-28). The word is
"part" (owner, 2026-09-28), and readers see each part's question, never its number.

This is recorded because the obvious next move is wrong. A contributor who sees the website grouped
by parts will want to rename or split unit files to match them, or to cite "Part 5". Units are what
a route names, what a chunk is keyed on and what a citation resolves to at a release tag, so a unit
rename breaks every citation and chunk address made before it. A part changes nothing a citation
points at.

## Considered options

- **"Chapter"**: the word everyone reaches for, and on this glossary's avoid list for Unit, because
  it suggests a file.
- **"Step" or "reading step"**: collides with the Method steps in the stage units and the site's
  one-step-per-page thread.
- **"Section"**: already on the avoid list for Chunk.
- **"Part"** was chosen although "part" also names the six parts of the prompt pattern and the five
  parts of a route. Those are parts of one prompt or one answer; a reader never meets them next to a
  numbered part, because the number is never shown.

## Consequences

- A site group is headed by its part's question. The `GROUP_NOTES` line "One part for each stage of
  the work" in `ai4bcm-site` is reworded, since a stage unit is no longer a part.
- Reordering parts, or moving a unit between parts, changes no chunk and no citation. Renaming a
  unit or its headings still does, and needs a release.
- The print edition may show a part as a run of sheets; nothing requires a sheet to belong to a
  single part.
