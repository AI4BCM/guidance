#!/usr/bin/env bash
# Publish the AI4BCM knowledge base — a ROOT round the owner runs. No session runs this.
#
#   sudo /opt/apps/ai4bcm-guidance/tools/publish_knowledge.sh
#
# It replaced step 2 of bia-workflow's publish_knowledge.sh, which built this corpus out of a
# repository named after a different product (kb-move ticket 06, 2026-09-10). Since 2026-09-12 it
# publishes a corpus and nothing else: the static knowledge base it also rendered is retired, and
# the guidance is read on GitHub.
#
# ---------------------------------------------------------------------------------------------
# ROLLBACK — `git -C /opt/apps/ai4bcm-guidance checkout <previous tag>` and run this again.
#
# Until 2026-09-12 this script also rendered 383 static pages into /var/www/ai4bcm-demo/kb, and
# most of its machinery was there to make that tree replaceable in one rename (build into a
# scratch dir, swap, keep kb.prev). Those pages are retired: the guidance is published on GitHub
# and every citation resolves there. What is left writes ONE directory, $DATA_DIR, and restarts
# one service, so the rollback is the checkout that produced the previous corpus.
#
# It still does NOT touch the BIA MCP service, its data directory or its demo rooms. Those are
# bia-workflow's round.
# ---------------------------------------------------------------------------------------------
#
# Stdlib only. This repository needs no virtualenv and this script needs no venv python — that is
# a property of the corpus build, not an accident, and test_source_registry.py guards it.
set -euo pipefail

APP_ROOT="${AI4BCM_APP_ROOT:-/opt/apps/ai4bcm-guidance}"
DATA_DIR="${AI4BCM_DATA_DIR:-$APP_ROOT/data}"
PYTHON="${AI4BCM_PYTHON:-/usr/bin/python3}"


echo "1/4 pull"
git -C "$APP_ROOT" pull --ff-only

# literature/ is passed explicitly, not discovered: a file there becomes a chunk only if
# sources.json claims it, and an unclaimed file stops this build rather than publishing text
# whose licence nobody checked. Dropping --source-dir here builds the 96-chunk units-only corpus
# and would silently unpublish 287 pages — the flag is the difference between the two corpora.
echo "2/4 build chunks -> $DATA_DIR"
"$PYTHON" "$APP_ROOT/tools/build_chunks.py" --data-dir "$DATA_DIR" \
  --source-dir "$APP_ROOT/literature"

# Step 3 was "render the knowledge-base pages", and it is GONE — owner decision 2026-09-12.
# /demo/kb/ answers 410 now: this repository on GitHub is the source of truth and every citation
# resolves there (CITATION-CONTRACT.md version 2). build_kb_pages.py and brand.py went with the
# step, because the 383 pages were their only consumer here. bia-workflow keeps its own copy of
# build_kb_pages.py, which is a different thing: there it is the rendering library
# interview_guide.py imports STYLE and render_markdown from.
#
# What this removes from the round: the scratch build, the permissions pass, the swap and the
# kb.prev rollback. They existed to make a 7.5M page tree replaceable in one rename. There is no
# page tree any more, so the round is a corpus build and a restart.

echo "3/4 restart the connector"
systemctl restart ai4bcm-guidance-mcp
for i in $(seq 1 15); do
  curl -fsS -m 5 http://127.0.0.1:8788/health >/dev/null 2>&1 && break
  [ "$i" -eq 15 ] && { echo "the connector did not come back after 15s" >&2; exit 1; }
  sleep 1
done

echo "4/4 verify the citation a reader gets, not the build"
# `active` is not `working`. Until 2026-09-12 this block counted page directories under
# /var/www/ai4bcm-demo/kb and curled two of them; there are no pages now, so what it proves
# instead is the one thing a reader depends on — that the connector serves a citation, and that
# the citation points at this repository.
chunks=$("$PYTHON" -c 'import json,sys; print(len(json.load(open(sys.argv[1]))))' "$DATA_DIR/chunks.json")
echo "  $chunks chunks built"
# The citation a reader actually gets, resolved through the connector rather than read off disk.
# `active` is not `working`: this is the one line that proves the restart above took.
#
# 127.0.0.1:8788, NOT https://mcp.ai4bcm.org/index.json. What this step proves is that the
# process reloaded its index — a property of the service, not of the vhost in front of it. Going
# through nginx made this round depend on a `location = /index.json` being installed, which on
# 2026-09-12 it was not: the publish round ran BEFORE the nginx round in the same sitting, the
# curl 404'd, `set -e` aborted the whole thing, and a corpus that had in fact published
# correctly looked like a failure. Whether the public route works is the nginx round's business.
INDEX_URL="${AI4BCM_INDEX_URL:-http://127.0.0.1:8788/index.json}"
served=$(curl -fsS -m 10 "$INDEX_URL" \
  | "$PYTHON" -c 'import json,sys; print(json.load(sys.stdin)["topics"][0]["url"])')
echo "  citation   $served"
case "$served" in
  https://github.com/AI4BCM/guidance/blob/*\#*) ;;
  *) echo "the connector is still serving $served — the restart did not take" >&2; exit 1;;
esac
echo "published AI4BCM knowledge — $chunks chunks"
