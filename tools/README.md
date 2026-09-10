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
| `server.py` | the connector: those five over MCP, plus `/health`. Open, no token |
| `test_server.py` | 14 tests over the transport; skips when `mcp` is not installed |
| `requirements.txt` | the SERVER's dependencies. Nothing else in this directory needs them |
| `brand.py` | the visual tokens, masthead and footer; no imports at all |
| `build_kb_pages.py` | one static HTML page per chunk, so citation URLs resolve |
| `literature/` | four converters, run by hand when a source is added |

## Build

Stdlib only, on system `python3` — this repo needs no virtualenv.

```sh
python3 tools/build_chunks.py                          # 96 chunks: the units
python3 tools/build_chunks.py --source-dir literature  # 383 chunks: units + eight sources
python3 tools/build_kb_pages.py --chunks data/chunks.json --out <dir>
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

## Two names that have not moved yet

`BIA_WORKFLOW_DATA_DIR` still overrides the data directory in `build_kb_pages.py`, and the deploy
default is still `/var/www/ai4bcm-demo/kb`. Both are deploy-path questions settled in ticket 06, not
build questions; renaming them here would have broken the byte-identical proof for no gain.

## What did not come

`build_guide_page.py` stayed behind. It builds *"Running a BIA with the assistant — a manager's
guide"*, reads `server.py` at build time to count MCP tools, and renders an Excalidraw scene from
`docs/`. It is a BIA product page that happened to import `brand`. See ticket 03.
