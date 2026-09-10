#!/usr/bin/env bash
# Publish the AI4BCM knowledge base — a ROOT round the owner runs. No session runs this.
#
#   sudo /opt/apps/ai4bcm-guidance/tools/publish_knowledge.sh
#
# It replaces steps 2 and 3 of bia-workflow's publish_knowledge.sh, which built this corpus and
# these pages out of a repository named after a different product (kb-move ticket 06, 2026-09-10).
# What it does NOT do is as important: it does not touch the BIA MCP service, its data directory,
# its manager's guide or its demo rooms. Those stay in bia-workflow's round.
#
# ---------------------------------------------------------------------------------------------
# ROLLBACK — one line, and it is written here BEFORE the first cutover rather than after it:
#
#   rm -rf /var/www/ai4bcm-demo/kb && mv /var/www/ai4bcm-demo/kb.prev /var/www/ai4bcm-demo/kb
#
# That works because this script never edits the served tree in place. It builds into a scratch
# directory, and only once the build has succeeded does it swap the two with a pair of renames.
# A failed build leaves the live pages untouched; a bad build is one rename from undone. The
# previous tree is kept as kb.prev — one generation, overwritten by the next publish. Older
# archives beside it (kb.retired-2026-09-10) are the owner's to prune; this script never deletes
# anything it did not create in this run.
# ---------------------------------------------------------------------------------------------
#
# Stdlib only. This repository needs no virtualenv and this script needs no venv python — that is
# a property of the corpus build, not an accident, and test_source_registry.py guards it.
set -euo pipefail

APP_ROOT="${AI4BCM_APP_ROOT:-/opt/apps/ai4bcm-guidance}"
DATA_DIR="${AI4BCM_DATA_DIR:-$APP_ROOT/data}"
KB_ROOT="${AI4BCM_KB_ROOT:-/var/www/ai4bcm-demo/kb}"
PYTHON="${AI4BCM_PYTHON:-/usr/bin/python3}"
# A published page's own citation URL. Spot-checked at the end, because a page tree that built
# perfectly and is not reachable is the failure this estate has already had.
PUBLIC_INDEX="${AI4BCM_PUBLIC_INDEX:-https://agent.ai4bcm.org/demo/kb/}"

STAGE="$KB_ROOT.new"
PREV="$KB_ROOT.prev"

echo "1/6 pull"
git -C "$APP_ROOT" pull --ff-only

# literature/ is passed explicitly, not discovered: a file there becomes a chunk only if
# sources.json claims it, and an unclaimed file stops this build rather than publishing text
# whose licence nobody checked. Dropping --source-dir here builds the 96-chunk units-only corpus
# and would silently unpublish 287 pages — the flag is the difference between the two corpora.
echo "2/6 build chunks -> $DATA_DIR"
"$PYTHON" "$APP_ROOT/tools/build_chunks.py" --data-dir "$DATA_DIR" \
  --source-dir "$APP_ROOT/literature"

echo "3/6 render pages -> $STAGE"
rm -rf "$STAGE"
"$PYTHON" "$APP_ROOT/tools/build_kb_pages.py" --chunks "$DATA_DIR/chunks.json" --out "$STAGE"

# Ownership and mode are set on the STAGE tree, before the swap, so the live tree is never
# briefly unreadable. Public static content is served through the OTHER bits — group www-data is
# there to match its neighbours under /var/www, not to carry the read permission.
echo "4/6 permissions"
find "$STAGE" -type d -exec chmod 755 {} +
find "$STAGE" -type f -exec chmod 644 {} +
if [ "$(id -u)" -eq 0 ]; then
  chown -R root:www-data "$STAGE"
else
  # Deliberately not fatal. Everything above this line is unprivileged, so an agent can rehearse
  # this exact script into a scratch KB_ROOT and see the swap and the spot-check run for real
  # instead of reading them. Only the group matters here and only for tidiness: the pages are
  # served through the OTHER bits, so a tree that never got chowned still serves.
  echo "  not root — skipping chown (rehearsal); the real round runs as root"
fi

echo "5/6 swap into place (previous tree kept as $PREV)"
test -s "$STAGE/index.html" || { echo "stage has no index.html — refusing to swap" >&2; exit 1; }
rm -rf "$PREV"
if [ -e "$KB_ROOT" ]; then mv "$KB_ROOT" "$PREV"; fi
mv "$STAGE" "$KB_ROOT"

echo "6/6 verify the served pages, not the build"
# `active` is not `working`, and a directory that exists is not a page that answers. Resolve a
# real citation URL through nginx, not a path on disk.
# Report the corpus count, not a directory count. /demo/kb/ holds one directory per chunk PLUS
# t/ (the prompt-template pages), so the top-level directory count is 384 while the corpus is 383,
# and quoting the wrong one of those two is how "96" survived in four documents.
chunks=$("$PYTHON" -c 'import json,sys; print(len(json.load(open(sys.argv[1]))))' "$DATA_DIR/chunks.json")
pages=$(find "$KB_ROOT" -mindepth 1 -maxdepth 1 -type d | wc -l)
echo "  $chunks chunks -> $pages page directories (chunks + t/)"
curl -fsS -o /dev/null -w '  index      %{http_code}\n' "$PUBLIC_INDEX"
sample=$(find "$KB_ROOT" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | LC_ALL=C sort | sed -n '1p')
curl -fsS -o /dev/null -w "  $sample  %{http_code}\n" "$PUBLIC_INDEX$sample/"
echo "published AI4BCM knowledge — $chunks chunks"
