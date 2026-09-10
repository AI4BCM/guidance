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
| `retrieval.py` | the search/fetch index, stdlib only |
| `brand.py` | the visual tokens, masthead and footer; no imports at all |
| `build_kb_pages.py` | one static HTML page per chunk, so citation URLs resolve |
| `literature/` | four converters, run by hand when a source is added |

## Build

Stdlib only, on system `python3` — this repo needs no virtualenv.

```sh
python3 tools/build_chunks.py                          # 96 chunks: the units
python3 tools/build_chunks.py --source-dir literature  # 383 chunks: units + eight sources
python3 tools/build_kb_pages.py --chunks data/chunks.json --out <dir>
python3 -m pytest tools/test_source_registry.py -q     # 12 passed
```

## Two names that have not moved yet

`BIA_WORKFLOW_DATA_DIR` still overrides the data directory in `build_kb_pages.py`, and the deploy
default is still `/var/www/ai4bcm-demo/kb`. Both are deploy-path questions settled in ticket 06, not
build questions; renaming them here would have broken the byte-identical proof for no gain.

## What did not come

`build_guide_page.py` stayed behind. It builds *"Running a BIA with the assistant — a manager's
guide"*, reads `server.py` at build time to count MCP tools, and renders an Excalidraw scene from
`docs/`. It is a BIA product page that happened to import `brand`. See ticket 03.
