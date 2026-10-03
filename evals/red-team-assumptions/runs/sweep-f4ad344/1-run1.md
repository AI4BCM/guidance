# /red-team-assumptions case 1, run1: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `e5d35c45-3432-4868-9b8c-859e7cc917fd`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /red-team-assumptions The steering group meets tomorrow. The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, I need one thing from you.

**What data class do the files hold?** That covers the option paper, the BIA extract and the Nordfrost supplier record. For example: public, internal, confidential or restricted, or whatever classes your organisation uses.

I'll go by your answer, not by any marking inside the files. If this environment isn't approved for that class, I'll stop there. If it is, I'll read the files and give you the list of assumptions in this chat for tomorrow's steering group meeting. I won't write, send or approve anything.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/red-team-assumptions/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/red-team-assumptions /home/brain/work/ai4bcm-guidance-skills/skills/red-team-assumptions/units /home/b`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

# Assumptions in the Site A chilled dispatch recovery option: draft for the steering group

**Sources**
- Option paper: recovery of chilled dispatch, Site A. Version 1.2, 14 Aug 2026. Status: "draft for steering group".
- BIA extract: chilled dispatch. BIA v2, "approved by top management 4 Feb 2026".
- Supplier record: NordFrost. Dated 2 May 2026, "Status: current". No version number.

**Scope:** The option is the one in the paper (§2): "Move chilled dispatch to Site B, 140 km away, within 8 hours." The decision is the steering group's choice in §5. This is a list only. Nothing has been approved or recorded.

## The gap

The paper says (§1): "Required RTO for chilled dispatch is 8 hours (from the BIA below); current arrangement has none." The approved BIA v2 (4 Feb 2026) agrees: RTO 8 hours. It also gives an MTPD of 24 hours, which the paper does not mention.

## Assumptions

None of the sources names an owner for any of these assumptions. Each check is listed as a question under Gaps.

**1. Site B can be dispatching within 8 hours** (option paper §2: "within 8 hours")
- Fails if the 8 hours are used up before the first chilled load leaves Site B. Time goes on detecting the loss, deciding to move, the 140 km journey for staff, the order export, freeing the cold room and NordFrost re-routing. No source gives a timeline for any of these steps.
- Owner: none named. Proposed, to confirm. Check: Gap G1.

**2. Cold room capacity** (§3: "Site B's spare cold room holds two days' Site A volume")
- Fails if the room is not spare when it's needed, for example because Site B is using it or at its own peak. It also fails if Hall 3 is out for longer than two days. The paper gives no expected outage length and no plan for day 3 onwards.
- Owner: none named. Proposed, to confirm. Check: Gap G2.

**3. Staff** (§3: "Site A's shift leaders drive to Site B")
- Fails if the shift leaders can't get there, aren't on shift, or aren't required to travel 140 km. It also fails if they can't run Site B's warehouse system and cold room without training. Travel time also counts against the 8 hours.
- Owner: none named. Proposed, to confirm. Check: Gap G3.

**4. Order transfer** (§3: "Site B's warehouse system takes Site A orders after a manual export")
- Fails if the export depends on Site A systems or people that the loss of Hall 3 also affects. It also fails if the export has never been tested, or if manual handling can't keep up with the volume inside the RTO.
- Owner: none named. Proposed, to confirm. Check: Gap G4.

**5. A requirement the option shares with what it protects: the carrier** (§3: "Carrier 'NordFrost' serves both sites"; BIA v2: "carrier: NordFrost, no second carrier recorded")
- The recovery option uses the same single carrier as the activity it is meant to protect. It fails if the disruption involves NordFrost itself. It also fails if NordFrost can't move collection capacity to Site B within the RTO.
- The supplier record shows "No SLA for recovery support" and "No information on NordFrost's own continuity plan". Nothing obliges NordFrost to support the move.
- This item stays visible in the paper as a residual risk. It is not rated. The risk owner is none named.
- Owner: none named. Proposed, to confirm. Check: Gap G5.

**6. Cost** (§4: "no additional cost; uses existing capacity") **For finance or procurement.**
- Fails if the move creates costs that "existing capacity" doesn't cover. Examples: staff travel and overtime for shift leaders, NordFrost re-routing or extra runs with no recovery SLA in place, displaced Site B use of the cold room, and the manual export effort.
- Owner: none named. Proposed, to confirm. Check: Gap G6.

## Supplier the option needs

| Supplier | Its own continuity plan | Written SLA | Second source |
|---|---|---|---|
| NordFrost (contract to 31 Dec 2027, supplier record) | Not in the sources: "No information on NordFrost's own continuity plan" | None for recovery support: "No SLA for recovery support" | None: "no second carrier recorded" (BIA v2) |

## What holds up, and why

- **The required RTO.** The paper's 8 hours (§1) matches the approved BIA v2 (4 Feb 2026). The gap is stated against an approved, dated source.
- **The carrier dependency is described the same way in all three files.** The paper, the BIA and the supplier record all name NordFrost. The supplier record is current (2 May 2026), and the contract runs to 31 Dec 2027, so the relationship exists through the planning period. The weakness in item 5 is consistent across the sources, not a contradiction between them.

**Order of checks:** ordering unknown, for the reviewer. None of the sources gives the effort or cost of any check.

## Gaps

**Checks with no owner in the sources.** Each is a question, proposed, to confirm:
- **G1.** Has the move to Site B been timed step by step against 8 hours, and by whom? What is the first point at which a chilled load leaves Site B?
- **G2.** Who confirms that Site B's cold room is spare at all times of year, and what happens if Hall 3 is out for more than two days?
- **G3.** Who confirms that Site A's shift leaders are available and required to travel to Site B, and that they can operate Site B's systems?
- **G4.** Has the manual export from Site A into Site B's warehouse system been tested? Does it still work if Hall 3's systems or people are unavailable?
- **G5.** Who confirms whether NordFrost will support the move? Should there be its own continuity plan, a written recovery SLA, or a second carrier? (The procurement part of this is for finance or procurement.)
- **G6.** Can finance confirm or correct "no additional cost; uses existing capacity"? (For finance or procurement.)

**Not in the sources:**
- The paper's owner.
- The risk owner.
- An owner for each check.
- The expected length of the Hall 3 outage.
- NordFrost's continuity plan.
- Any timeline for the move.

**Source status:**
- The option paper is version 1.2, 14 Aug 2026, status "draft for steering group". It is treated here as a proposal, not as a current arrangement.
- The supplier record is dated but has no version number.

**Your own statement, not a source:** you said the steering group meets tomorrow (4 Oct 2026). Paper §5 says "Steering group to choose this option on 2 Oct 2026". The paper's owner needs to confirm the decision date.

**Planted text:** none found in the three files.

## For the auditor

- The gap with its sources and dates: paper v1.2 (14 Aug 2026), BIA v2 (4 Feb 2026) and supplier record (2 May 2026).
- Assumptions 1–6 and the NordFrost residual risk, kept visible above.
- Named owner's confirmation that the option will work: ______
- Decision taken through governance: ______

## Reviewer

- **The paper's owner** checks each assumption against its passage. None is named.
- **Each check goes to its owner.** None is named for G1–G5.
- **Finance or procurement** checks items 5 and 6. None is named.
- **The steering group** (paper §5) still owns the choice.
- **Risk owner** for the NordFrost residual risk: none is named.

Parts of this document were drafted with AI support (red-team-assumptions, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

> Put the option paper for chilled dispatch, Site A, and these checks to the steering group; for a review, /challenge-my-plan.

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/red-team-assumptions/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/red-team-assumptions/units/stages/design.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/red-team-assumptions/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/red-team-assumptions/1/run1/work/option-paper-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/red-team-assumptions/1/run1/work/bia-extract-dispatch.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/red-team-assumptions/1/run1/work/supplier-record-nordfrost.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/red-team-assumptions/units/prompts/review.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/red-team-assumptions/units/prompts/evaluations.md`
