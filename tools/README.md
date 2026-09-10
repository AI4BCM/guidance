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
| `publish_knowledge.sh` | the root round: build the corpus, render the pages, swap them into `/var/www` |

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

## The three deploy-path names, settled (ticket 06, 2026-09-10)

| Name | What happened | Why |
|---|---|---|
| `BIA_WORKFLOW_DATA_DIR` | **renamed** to `AI4BCM_DATA_DIR` in `build_kb_pages.py` | it is the same variable `server.py` already read, so one knob now points the build and the serve at one corpus. Renaming it changes no rendered byte, and the proof against `baseline/MANIFEST.sha256` was re-run afterwards: 529 of 529, empty diff |
| `DEFAULT_OUT` = `/var/www/ai4bcm-demo/kb` | **unchanged** | it is where nginx's `alias /var/www/ai4bcm-demo/` resolves `/demo/kb/`. A served path, not a product claim |
| `PUBLIC_BASE_URL` = `https://agent.ai4bcm.org/demo/kb` | **unchanged**, and the one to be careful with | it is baked into every rendered page and is the target of the chunk-id citation contract (ticket 07). It moves only when the corpus is republished under a new name |

**The consequence, stated rather than discovered later.** The connector is published as
`mcp.ai4bcm.org` and every citation it emits points at `agent.ai4bcm.org/demo/kb/`. That is
correct today — those are the URLs that exist, all four in a live search spot-check answer 200 —
but it means AI4BCM's own connector cites a hostname named after the other product. Closing that
is a republish of the corpus under a new base URL, which is the website's v2 work and ticket 07's
contract, not a repository move.

## Publishing

`tools/publish_knowledge.sh` is the root round the owner runs, and it replaced steps 2 and 3 of
`bia-workflow`'s script of the same name. That script no longer renders these pages — both wrote
`/var/www/ai4bcm-demo/kb`, and leaving two writers on one directory would have let the old round
overwrite the new one and destroy its rollback tree on the way past.

It never edits the served tree in place: it builds into `kb.new`, swaps, and keeps the previous
tree as `kb.prev`. **Rollback is one line**, and it is in the script's header rather than in
someone's memory:

```sh
rm -rf /var/www/ai4bcm-demo/kb && mv /var/www/ai4bcm-demo/kb.prev /var/www/ai4bcm-demo/kb
```

Everything before the swap is unprivileged, so the exact script can be rehearsed into a scratch
directory without root:

```sh
AI4BCM_APP_ROOT=<clone> AI4BCM_DATA_DIR=<clone>/data AI4BCM_KB_ROOT=/tmp/kb \
  bash <clone>/tools/publish_knowledge.sh
```

## Deploying the connector

`deploy/ai4bcm-guidance-mcp.service` and `deploy/nginx-mcp-ai4bcm.conf`. Neither is installed;
both are kgadmin rounds, and the nginx one is blocked on the owner adding `mcp` A + AAAA records
at All-Inkl. Read the header of each file before installing it — the DNS records, the reason the
connector took the new hostname rather than moving the BIA endpoint, and the `svc-ai4bcm` uid are
all stated there.
