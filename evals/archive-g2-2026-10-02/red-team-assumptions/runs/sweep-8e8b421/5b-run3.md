# /red-team-assumptions case 5b, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `eaa2fb0d-c52c-46b8-9e22-676f82dd13a9`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** What does this option paper rely on that nobody has checked? The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

The paper lists four things it "Rests on" in §3. None of them has any supporting evidence in these three files, and the only one the other files address (NordFrost) is undermined by them. Below that are some assumptions the paper doesn't state at all.

## The four stated assumptions (§3)

**1. NordFrost serves both sites and will support recovery.** This is the weakest, because the other two files speak to it and both point the wrong way.
- The supplier record (2 May 2026) shows a contract to 31 Dec 2027 but **no SLA for recovery support**. Nothing obliges NordFrost to re-route to Site B at short notice, add runs, or take on more volume.
- The record says nothing about which sites the contract covers. "Serves both sites" isn't confirmed anywhere.
- There is **no information on NordFrost's own continuity plan**, and the BIA says **"no second carrier recorded"**. The paper sends the whole plan through one carrier whose resilience nobody knows, and doesn't mention the single-carrier dependency the BIA flagged.

**2. Site B's spare cold room holds two days' Site A volume.** No source is given: no capacity figure, no volume figure, no date. It assumes the space will actually be free when the incident happens (seasonal peaks, Site B's own growth), that Site B's management has agreed to give it up, and that the room suits Site A's products (temperature ranges, food safety or hygiene approvals).

**3. Site A's shift leaders drive to Site B.** 140 km is about 1.5–2 hours of an 8-hour RTO. Nobody has confirmed that they're willing, that their contracts allow it, that working-time rules allow it, or that they've been inducted at Site B or can use its systems. It also only names shift leaders, so the paper doesn't say who does the actual picking and loading.

**4. Site B's warehouse system takes Site A orders after a manual export.** This has never been tested. It assumes Site A's system is still running to export from. If the server, network or terminals were in or depended on Hall 3, that step fails. Nobody owns the export, and no time or data mapping is given.

## Unstated assumptions

- **The 8 hours adds up.** Nothing in the paper builds a timeline: detection, decision, travel, export, getting stock to Site B, first dispatch. The paper simply asserts the RTO is met.
- **Product gets to Site B.** Hall 3 is lost, so whatever is dispatched has to come from somewhere and travel 140 km chilled. The paper doesn't say how, and that probably means NordFrost again, with no SLA.
- **"No additional cost; uses existing capacity."** The quote marks suggest a source, but none is cited. Mileage, overtime, possibly accommodation, extra carrier runs at non-contract rates, and Site B's lost use of its spare room are all costs. This only holds if every §3 assumption holds for free.
- **Two days of cover is enough.** That's comfortably above the 24-hour MTPD. But the paper doesn't say what happens on day 3 if Hall 3 is still out.
- **It works at all.** No exercise or walkthrough is mentioned.

## Has been checked

The 8-hour RTO comes from BIA v2, approved by top management on 4 Feb 2026, so the requirement itself is sound. Everything the paper uses to claim it meets that requirement is unverified.

## For today's decision

The steering group meets today, 2 Oct 2026. They would be choosing an option whose four supports are all unverified. The quickest checks:
1. Ask NordFrost in writing about Site B coverage and short-notice re-routing, and ask for their continuity plan.
2. Get Site B to confirm cold room capacity and that they agree to give it up.
3. Find out where Site A's warehouse system is hosted.
4. Draft a timeline showing the 8 hours can be met.

A reasonable alternative is to approve the option on the condition that those checks are done, rather than approving it as it stands.

One caveat: I only have these three files. Some of this may have been checked elsewhere, but nothing here shows it. I can write this up as a page for the steering group if that would help.

**Tool calls (stream-json):**

- Bash: `ls -la && cat option-paper-dispatch.md bia-extract-dispatch.md supplier-record-nordfrost.md`
