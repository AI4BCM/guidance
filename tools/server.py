#!/usr/bin/env python3
"""The AI4BCM guidance connector: five tools, a corpus, and nothing else.

kb-move ticket 04. This is the transport half; the tool half is `guidance_tools.py`, whose
payloads were diffed against the 849-line `bia-workflow` original across five tools and eight
queries. **That file is the compatibility contract ticket 06 cuts over against — this module
wraps it and must not reshape what it returns.**

What this server deliberately does NOT have, and why:

- **No auth.** Owner decision, 2026-09-10: the AI4BCM connector is open. It serves CC BY 4.0
  guidance that is already public as static pages at `/demo/kb/`, and a connector people install
  works best with nothing to configure. `MCP_SCOPES = ("bia:use",)` and the `StaticTokenVerifier`
  stay with the BIA endpoint in `bia-workflow`; nothing here inherits a scope named `bia:use`.
- **No rate limit in this process.** Because the endpoint is open, a ceiling is load-bearing —
  but the estate already limits at nginx (`limit_req_zone` beside the vhost so it installs in one
  root step). `deploy/nginx-ai4bcm-mcp.conf` here is that block, following the pattern
  `deploy/nginx-agent-ai4bcm.conf` in `bia-workflow` already uses for `/demo/claim`. A second
  limiter in Python would be a second thing to reason about for no gain.
- **No spend ceiling.** The website's ceiling ticket guards a lane that calls a model and costs
  money per answer. Every tool here is a local index lookup over `chunks.json`: the cost of an
  abusive caller is CPU, which is exactly what the rate limit is for.
- **No BIA anything.** `grep -E '^(import|from) (answer_sheet|call_log|graph_files|journeys)'`
  returns nothing here or in `guidance_tools.py`, and a test enforces it.

Where `/mcp` lands is ticket 06's call. Nothing here is deployed.

Run:
    python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt
    .venv/bin/python tools/server.py --port 8788
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from mcp.types import CallToolResult, TextContent, ToolAnnotations
from starlette.responses import JSONResponse, PlainTextResponse

sys.path.insert(0, str(Path(__file__).resolve().parent))

import guidance_tools
from retrieval import GuidanceIndex

# The corpus this server publishes. `build_chunks.py --data-dir <dir>` writes it; the default is
# the repo's own `data/`, file-relative so a second checkout serves its own build and never the
# other one's. Ticket 06 decides what the deployed value is.
DATA_DIR = Path(os.environ.get("AI4BCM_DATA_DIR", Path(__file__).resolve().parent.parent / "data"))
SERVER_VERSION = "1.0.0"  # the connector's own version; the corpus carries its own release_tag

# DNS-rebinding protection needs the public name, and the public name is ticket 06's decision.
# One env knob rather than a guess: whatever host `/mcp` ends up on goes here, or the SDK
# answers 421 and the connector looks broken for a reason nobody will find quickly.
ALLOWED_HOSTS = [h.strip() for h in os.environ.get(
    "AI4BCM_MCP_ALLOWED_HOSTS", "agent.ai4bcm.org").split(",") if h.strip()]

NO_CORPUS = (
    f"No chunk corpus at {DATA_DIR}. Build it first:\n"
    f"  python3 tools/build_chunks.py --data-dir {DATA_DIR}                          # 96 chunks\n"
    f"  python3 tools/build_chunks.py --data-dir {DATA_DIR} --source-dir literature  # 383 chunks"
)

logging.basicConfig(level="INFO", format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("ai4bcm-guidance")

_index: GuidanceIndex | None = None


def get_index() -> GuidanceIndex:
    """The chunk index, built on first use and kept. Also what the tool surface reads.

    Built here rather than left to `guidance_tools._idx()` so the server and its tools can never
    end up on two different corpora — and so a missing corpus is one RuntimeError with a build
    command in it, raised where `main()` can turn it into a refusal to start rather than a 500
    on the first call.
    """
    global _index
    if _index is None:
        try:
            _index = GuidanceIndex(DATA_DIR)
        except FileNotFoundError as exc:
            raise RuntimeError(NO_CORPUS) from exc
        guidance_tools.use_index(_index)
    return _index


INSTRUCTIONS = (
    "The AI4BCM guidance: how to use AI in business continuity work, published under CC BY 4.0. "
    "Search first, then fetch the section id you want to quote — a fetch carries the section's "
    "licence and citation line, so quote from a fetch, never from a search result. Every answer "
    "here is guidance about method; it holds no company data and runs no session."
)

READ_ONLY = ToolAnnotations(
    readOnlyHint=True,
    destructiveHint=False,
    openWorldHint=False,
    idempotentHint=True,
)

mcp = FastMCP(
    "ai4bcm-guidance",
    instructions=INSTRUCTIONS,
    host="127.0.0.1",
    port=8788,  # 8787 is the BIA endpoint's; the two run side by side until ticket 06 says otherwise
    streamable_http_path="/mcp",
    json_response=True,
    # Same reasoning as the BIA server: stateless Streamable HTTP is the SDK's recommended
    # production config and the most compatible with connectors that do not reliably carry an
    # Mcp-Session-Id. With no auth there is nothing a session would have held anyway.
    stateless_http=True,
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=["127.0.0.1:*", "localhost:*", *ALLOWED_HOSTS],
        allowed_origins=[
            "http://127.0.0.1:*",
            "http://localhost:*",
            "https://chatgpt.com",
            "https://chat.openai.com",
            "https://claude.ai",
        ],
    ),
)


def tool_result(payload: dict[str, Any], *, is_error: bool = False) -> CallToolResult:
    """Same envelope as the BIA server: structured content plus a JSON text fallback."""
    return CallToolResult(
        content=[TextContent(type="text", text=json.dumps(payload, ensure_ascii=False))],
        structuredContent=payload,
        isError=is_error,
    )


# ── the five tools ───────────────────────────────────────────────────────────────────────
# Descriptions carried from the registrations `bia-workflow` cut on 2026-09-02 (`b308aa0`,
# "five zero-use tools"), with three edits that are not cosmetic:
#   - "AI Addendum" is the retired name. It is the AI4BCM guidance (owner, 2026-09-08).
#   - the search description advertised a `pp` filter; the parameter has always been `unit`.
#   - the guided_journey sentence told the caller to call `open_bia`, which is not here.
# `get_workflow` was never registered anywhere, so its description is new.
#
# Measured 2026-09-10 across both published corpora (96 units, 383 with literature):
# `risk_level`, `mode` and `confidentiality` are empty on EVERY chunk. The parameters stay —
# they are `guidance_tools.search_fn`'s and the build still emits the fields — but no
# description promises a filter that currently selects nothing.

@mcp.tool(
    name="search",
    title="Search the AI4BCM guidance",
    description=(
        "Use this when the user asks how AI applies to BCM work, BCM professional practices, "
        "tools, controls, prompting, adoption, or AI4BCM terminology. Optional filters that "
        "select today: unit (e.g. 'principles', 'data-rules', 'stages-analysis'), output_type "
        "('guidance', 'governance', 'prompt', 'workflow', 'reference', 'tool-selection', "
        "'definition'), bcm_process (e.g. 'bia', 'exercise', 'prompting', 'ai-governance'). "
        "risk_level, mode and confidentiality are carried on every result but are empty "
        "throughout the published corpus — filtering on them returns nothing. Results are "
        "metadata only: fetch the id to get the text and its citation line."
    ),
    annotations=READ_ONLY,
)
def search(
    query: str,
    unit: str | None = None,
    output_type: str | None = None,
    risk_level: str | None = None,
    confidentiality: str | None = None,
    bcm_process: str | None = None,
    mode: str | None = None,
) -> CallToolResult:
    results = guidance_tools.search_fn(
        query, unit=unit, output_type=output_type, risk_level=risk_level,
        confidentiality=confidentiality, bcm_process=bcm_process, mode=mode)
    return tool_result({"results": results})


@mcp.tool(
    name="fetch",
    title="Fetch one AI4BCM guidance section",
    description=(
        "Use this when the user needs the full text for one guidance section id returned by "
        "search. Returns the section's words together with its licence and citation line — "
        "quote from here, and cite what this returns."
    ),
    annotations=READ_ONLY,
)
def fetch(id: str) -> CallToolResult:
    payload = guidance_tools.fetch_fn(id)
    return tool_result(payload, is_error="error" in payload)


@mcp.tool(
    name="get_workflow",
    title="Get an AI4BCM workflow",
    description=(
        "Use this when the user asks how a piece of BCM work is actually run end to end — the "
        "steps, not a definition. Pass a workflow id, or the name of the work in plain words "
        "('workflow design', 'BIA'); the closest published workflow is returned in full. If "
        "nothing matches, the answer lists every available workflow id."
    ),
    annotations=READ_ONLY,
)
def get_workflow(workflow_id: str) -> CallToolResult:
    payload = guidance_tools.get_workflow_fn(workflow_id)
    return tool_result(payload, is_error="error" in payload)


@mcp.tool(
    name="get_prompt_template",
    title="Get a BCM prompt template",
    description=(
        "Use this when the user needs a ready-to-use prompt for a BCM task. Provide the task "
        "name (e.g. 'BIA preparation', 'exercise scenario', 'plan review', 'management "
        "summary'). Returns copy-paste prompts with their applicable controls and "
        "data-handling warnings."
    ),
    annotations=READ_ONLY,
)
def get_prompt_template(task: str, risk_level: str | None = None) -> CallToolResult:
    payload = guidance_tools.get_prompt_template_fn(task, risk_level=risk_level)
    return tool_result(payload, is_error="error" in payload)


@mcp.tool(
    name="identify_ai_risks",
    title="Identify AI risks for a BCM task",
    description=(
        "Use this before a user begins any AI-assisted BCM task. Searches the guidance for "
        "applicable controls, data-handling warnings, and 'do not use AI for this' guidance. "
        "Provide a plain-language description of the task (e.g. 'I want to use an AI tool to "
        "run a BIA for our IT department'). Returns applicable controls, do-not-use warnings, "
        "and the cited guidance sections."
    ),
    annotations=READ_ONLY,
)
def identify_ai_risks(task_description: str) -> CallToolResult:
    return tool_result(guidance_tools.identify_ai_risks_fn(task_description))


# ── /health and / ────────────────────────────────────────────────────────────────────────
def _iso(ts: float | None) -> str | None:
    return datetime.fromtimestamp(ts, timezone.utc).isoformat(timespec="seconds") if ts else None


def health_payload() -> dict[str, Any]:
    """Chunk count, version and build date — the three the ticket asked for.

    `version` is this server's; `release_tag` is the corpus's, read from the index the build
    wrote, because "which guidance is this" is the question a caller actually has. `built_at`
    is chunks.json's mtime, rewritten on every build.

    Deliberately NOT here: the BIA server's `stale` flag. It compares the corpus mtime against
    `units/**/*.md`, which is honest only where the sources sit beside the served corpus. Where
    the deployed corpus lives is ticket 06's decision, so a staleness claim now would be a guess
    dressed as a measurement.
    """
    index = get_index()
    chunks_path = DATA_DIR / "chunks.json"
    return {
        "ok": True,
        "chunks": len(index.chunks),
        "version": SERVER_VERSION,
        "release_tag": index.index.get("release_tag", ""),
        "built_at": _iso(chunks_path.stat().st_mtime if chunks_path.exists() else None),
    }


@mcp.custom_route("/health", methods=["GET"], include_in_schema=False)
async def health(_request):
    return JSONResponse(health_payload())


@mcp.custom_route("/", methods=["GET"], include_in_schema=False)
async def root(_request):
    return PlainTextResponse("AI4BCM guidance MCP server. Use /mcp for MCP clients.")


def main() -> int:
    import uvicorn
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default=os.environ.get("HOST", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8788")))
    args = parser.parse_args()
    try:
        chunks = len(get_index().chunks)  # fail fast: no corpus, and the process never serves
    except RuntimeError as exc:
        raise SystemExit(str(exc)) from exc
    logger.info("index ready: %d chunks from %s", chunks, DATA_DIR)
    logger.info("starting AI4BCM guidance MCP server on %s:%s/mcp (open, no token)",
                args.host, args.port)
    uvicorn.run(mcp.streamable_http_app(), host=args.host, port=args.port)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
