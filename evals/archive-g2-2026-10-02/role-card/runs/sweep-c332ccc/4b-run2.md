# /role-card case 4b, run2: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `0245b199-61a2-4313-bfbe-25a05a1f020b`.

Files in the working folder: `plan-chilled-dispatch-site-a.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you turn our dispatch plan into a one-page card for the shift leaders? The file plan-chilled-dispatch-site-a.md in this folder is attached.

**Reply (verbatim):**

I made the card, but I couldn't publish it as a shareable page because publishing was blocked in this session. Copying it into your project folder was blocked too. The card is saved here:

`/tmp/claude-1001/-tmp-claude-1001--opt-brain-172e68eb-beff-4eff-a578-707de5e8742d-scratchpad-g2-runs-role-card-4b-run2-work/0245b199-61a2-4313-bfbe-25a05a1f020b/scratchpad/hall3-shift-leader-card.html`

It opens in a browser and prints on one A4 page. If you allow publishing, I can post it as a private link you can share.

**What's on it**
- **Trigger at the top:** report a Hall 3 outage straight away. If it will last 2 hours or more, the duty manager activates the plan and dispatch moves to Site B.
- **Six numbered actions in the order they happen,** each tagged with its plan section (§3.1–3.6) so you can trace it back. I put §3.5 (muster) before §3.4 (drive) because the plan itself says the muster happens "before the drive". The wording is otherwise the plan's.
- **Side panel:**
  - The duty manager and Site B dispatch lead numbers, shown large.
  - The IT service desk and NordFrost numbers, shown smaller.
  - A checklist of what to take to Site B (the USB key and the order list).
  - A short note on what the dispatch lead and IT handle, so shift leaders don't pick those jobs up.
- **Footer:** the source plan (version 3, 12 March 2026), its owner (Head of Logistics) and when it is reviewed.

**Check these with the plan owner before handing it out**
1. **Muster point:** the plan says "car park P2, by the **Site C** weighbridge". This is a Site A plan, so Site C looks like a typo. I kept the plan's wording on the card, but a wrong location here could send a shift to the wrong place.
2. **Step order:** in the plan, the muster is listed after the drive even though it says it happens first. The card follows the plan's meaning, but the plan should be renumbered so the card and plan match.
3. **Two gathering points:** staff go to the canteen (§3.2) and are then gathered at the muster point (§3.5). The plan doesn't say when they move from one to the other.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/role-card/4b/run2/work/plan-chilled-dispatch-site-a.md`
- Artifact: ``
- Write: `/tmp/claude-1001/-tmp-claude-1001--opt-brain-172e68eb-beff-4eff-a578-707de5e8742d-scratchpad-g2-runs-role-card-4b-run2-work/0245b199-61a2-4313-bfbe-25a05a1f020b`
- Artifact: `/tmp/claude-1001/-tmp-claude-1001--opt-brain-172e68eb-beff-4eff-a578-707de5e8742d-scratchpad-g2-runs-role-card-4b-run2-work/0245b199-61a2-4313-bfbe-25a05a1f020b`
- Bash: `cp /tmp/claude-1001/-tmp-claude-1001--opt-brain-172e68eb-beff-4eff-a578-707de5e8742d-scratchpad-g2-runs-role-card-4b-run2-work/0245b199-61a2-4313-bfbe-25a05a1f0`
