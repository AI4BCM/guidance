# tools/ — the knowledge-base machinery

Moved out of `KoGerner/bia-workflow` on 2026-09-10 (`bia-workflow` at `2b2d3c9`, this repo at
`b5ff391`). Design of record: `/opt/brain/docs/issues/ai4bcm-knowledge-base-move/`.

The builder now sits beside its own inputs — `units/`, `literature/` and `releases/` are siblings of
this directory — so the corpus and the release tag cannot disagree.

| File | What it does |
|---|---|
| `build_chunks.py` | builds the corpus; licence gate refuses anything not class A |
| `sources.json` | the source registry: identifier, edition, licence, citation |
| `test_source_registry.py` | 12 tests over the registry and the gate |
| `test_build_source.py` | 4 tests pinning the corpus to its expected chunk count |
| `retrieval.py` | the search/fetch index, stdlib only |
| `guidance_tools.py` | the five guidance tools a connector exposes; no BIA imports |
| `test_guidance_tools.py` | 12 tests over those five |
| `server.py` | the connector: those five over MCP, plus `/health` and `/index.json`. Open, no token |
| `test_server.py` | 14 tests over the transport; skips when `mcp` is not installed |
| `requirements.txt` | the SERVER's dependencies. Nothing else in this directory needs them |
| `literature/` | four converters, run by hand when a source is added |
| `publish_knowledge.sh` | the root round: build the corpus, restart the connector, prove a citation |

## Build

Stdlib only, on system `python3` — this repo needs no virtualenv.

```sh
python3 tools/build_chunks.py                          # 96 chunks: the units
python3 tools/build_chunks.py --source-dir literature  # 383 chunks: units + eight sources
python3 -m pytest tools/ -q                            # 28 passed, 1 skipped
```

## Serve

The connector is the one thing here that is not stdlib: it needs the MCP SDK. That is why the
dependency lives in its own file and why `test_server.py` skips itself rather than failing — the
build and its 28 tests keep running on system `python3` with nothing installed.

```sh
python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt
.venv/bin/python tools/server.py --port 8788      # /mcp and /health
.venv/bin/python -m pytest tools/ -q              # 42 passed
```

`AI4BCM_DATA_DIR` picks the corpus (default: this repo's `data/`).
`AI4BCM_MCP_ALLOWED_HOSTS` must name the public host, or DNS-rebinding protection answers 421 to
every `/mcp` request. `/health` is outside that check and answers on any Host.

**The connector is open — no token** (owner, 2026-09-10): it serves CC BY 4.0 guidance already
public as static pages. The rate limit that makes that safe is nginx's, in
`deploy/nginx-ai4bcm-mcp.conf`. Not installed; where `/mcp` lands is ticket 06's call.

## Where a citation points (contract version 2, 2026-09-12)

`build_chunks.PUBLIC_BASE_URL` is gone. A chunk's `url` is this repository, pinned to the release
tag, anchored on the chunk's heading:

```
https://github.com/AI4BCM/guidance/blob/2026.09.1/units/stages/govern.md#level
```

Version 1 pointed at `agent.ai4bcm.org/demo/kb/<chunk-id>/` — the other product's hostname, and
383 static pages this directory used to render. **Those pages are retired**, and
`build_kb_pages.py` and `brand.py` went with them: the guidance is read on GitHub now. The two
consequences worth knowing before changing anything here:

- **A citation cannot be built from a chunk id.** It carries a source file and a GitHub anchor,
  and GitHub's anchor rules are not the chunk-id rules — see `CITATION-CONTRACT.md`. Read the
  `url` from the index; `build_chunks.github_anchors()` is the one implementation of the rule.
- **The index is published**, at `https://mcp.ai4bcm.org/index.json`, unauthenticated. It has to
  be, for the reason above.

## Publishing

`tools/publish_knowledge.sh` is the root round the owner runs. It builds the corpus into
`$DATA_DIR`, restarts the connector and proves a citation — four steps, and it writes exactly one
directory.

**The restart is a step, not an afterthought.** `server.py` builds its index once into a module
global, so a rebuilt `chunks.json` changes nothing the connector serves until the process
restarts — and `/health` keeps answering convincingly in the meantime, because `built_at` is the
file's mtime read fresh on every request while `search` and `fetch` answer out of the old index.

**A change to this script takes effect one round late.** Step 1 pulls the tree the running script
lives in, and bash keeps executing the file it started with. That is not theoretical: the
2026-09-12 round rebuilt the corpus and skipped a restart step that was already on disk.

**Rollback** is `git checkout <previous tag>` and a re-run: there is no page tree to
swap back since 2026-09-12.

## Deploying the connector

`deploy/ai4bcm-guidance-mcp.service` and `deploy/nginx-mcp-ai4bcm.conf`. **Both are installed and
live**, each by a kgadmin round on 2026-09-10: the unit into `/etc/systemd/system/` at 15:43:30Z,
the vhost into `/etc/nginx/sites-available/mcp-ai4bcm` at 15:43:47Z with the `sites-enabled`
symlink a second later. The `mcp` A + AAAA records the vhost once waited on exist —
`95.217.162.203` and `2a01:4f9:c013:a840::1` — so nothing here is blocked. Read the header of each
file before editing it: the reason the connector took the new hostname rather than moving the BIA
endpoint, and the `svc-ai4bcm` uid, are stated there.

Neither file deploys itself, and an edit to either reaches nothing until it is copied into place:

```sh
sudo cp deploy/ai4bcm-guidance-mcp.service /etc/systemd/system/ && sudo systemctl daemon-reload
sudo cp deploy/nginx-mcp-ai4bcm.conf /etc/nginx/sites-available/mcp-ai4bcm && sudo nginx -t && sudo systemctl reload nginx
```

A comment-only change needs no restart: `ExecMainStartTimestamp` should not move, and if it does,
something other than the comment changed. Check the artefact rather than this file — and without
a `--resolve` pin, so that DNS is part of what you prove:

```sh
curl https://mcp.ai4bcm.org/health
```
