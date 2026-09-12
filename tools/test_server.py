"""Tests for the guidance connector's transport (kb-move ticket 04).

`test_guidance_tools.py` pins the payloads; this file pins what a client actually reaches:
the published catalog, the /health shape, and the fact that a real MCP call over the
Streamable HTTP app returns the same bytes the tool function does.

These need `mcp`, which is NOT on system python3 — `tools/requirements.txt` and a venv are the
server's dependency, not the build's. Everything else in tools/ stays stdlib-only, so the whole
directory still collects and passes on the system interpreter: this file skips instead.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

pytest.importorskip("mcp", reason="the connector's transport needs tools/requirements.txt")

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Read from the release manifest, never spelled out: these tests were written at 2026.09 and
# the 2026.09.1 mint made two of them fail — invisibly, because this file skips on the system
# interpreter that the repo's usual `pytest tools` run uses.
import build_chunks as _bc  # noqa: E402

TAG = _bc.release_tag_from(REPO / "releases")


@pytest.fixture(scope="module")
def server(tmp_path_factory):
    """Import server.py against a corpus built from this repo, in a scratch data dir."""
    data = tmp_path_factory.mktemp("data")
    subprocess.run([sys.executable, str(REPO / "tools" / "build_chunks.py"),
                    "--data-dir", str(data)], check=True, capture_output=True)
    os.environ["AI4BCM_DATA_DIR"] = str(data)
    import server as srv
    srv.get_index()
    return srv


@pytest.fixture(scope="module")
def client(server):
    from starlette.testclient import TestClient
    # base_url matters: DNS-rebinding protection is ON, and TestClient's default Host is
    # "testserver", which is not in allowed_hosts — every request would 421 (as it should).
    with TestClient(server.mcp.streamable_http_app(), base_url="http://127.0.0.1:8788") as c:
        yield c


def call(client, method, params=None):
    """One JSON-RPC round trip. Stateless Streamable HTTP, json_response=True, so the answer
    is a plain JSON body rather than an SSE stream and no Mcp-Session-Id is carried."""
    body = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params or {}}
    resp = client.post("/mcp", json=body, headers={
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    })
    assert resp.status_code == 200, resp.text
    return resp.json()


# ── the catalog ──────────────────────────────────────────────────────────────────────────
FIVE = {"search", "fetch", "get_workflow", "get_prompt_template", "identify_ai_risks"}


def test_the_published_catalog_is_the_five_guidance_tools(client):
    """The whole point of the split: no BIA tool can appear here, not even by accident."""
    names = {t["name"] for t in call(client, "tools/list")["result"]["tools"]}
    assert names == FIVE


def test_no_bia_tool_name_survived_the_split(client):
    names = {t["name"] for t in call(client, "tools/list")["result"]["tools"]}
    bia = {"open_bia", "prepare_bia_stage", "confirm_bia_stage", "sign_bia", "record_turn",
           "list_company_files", "search_company_files", "read_company_file",
           "write_company_file", "update_register_entry", "update_bia_activity",
           "validate_bia_record"}
    assert not (names & bia)


def test_the_server_imports_no_bia_module():
    """Grepped, not read — the same guard test_guidance_tools.py puts on the tool surface."""
    src = (REPO / "tools" / "server.py").read_text(encoding="utf-8")
    for line in src.splitlines():
        assert not line.strip().startswith(("import answer_sheet", "from answer_sheet",
                                            "import call_log", "from call_log",
                                            "import graph_files", "from graph_files",
                                            "import journeys", "from journeys")), line


def test_every_tool_is_declared_read_only(client):
    for tool in call(client, "tools/list")["result"]["tools"]:
        assert tool["annotations"]["readOnlyHint"] is True, tool["name"]


# ── the calls ────────────────────────────────────────────────────────────────────────────
def payload_of(result):
    """A tool answer, taken from the text content — the fallback every client can read."""
    return json.loads(result["result"]["content"][0]["text"])


def test_search_over_the_wire_matches_the_tool_function(client, server):
    import guidance_tools as gt
    wire = payload_of(call(client, "tools/call",
                           {"name": "search", "arguments": {"query": "business impact analysis"}}))
    assert wire == {"results": gt.search_fn("business impact analysis")}
    assert wire["results"]


def test_fetch_over_the_wire_matches_the_tool_function(client, server):
    import guidance_tools as gt
    first = payload_of(call(client, "tools/call",
                            {"name": "search", "arguments": {"query": "principles"}}))["results"][0]
    wire = payload_of(call(client, "tools/call", {"name": "fetch", "arguments": {"id": first["id"]}}))
    assert wire == gt.fetch_fn(first["id"])
    assert wire["text"]


def test_a_chunk_id_that_does_not_resolve_is_an_error_result(client):
    result = call(client, "tools/call", {"name": "fetch", "arguments": {"id": "no-such-chunk"}})
    assert result["result"]["isError"] is True
    assert payload_of(result)["error"] == "not_found"


def test_no_answer_carries_a_journey_hint(client):
    """Dropped with the BIA coupling: the hint told the caller to call `open_bia`."""
    hits = payload_of(call(client, "tools/call",
                           {"name": "search", "arguments": {"query": "business impact analysis"}}))
    assert "guided_journey" not in hits
    for r in hits["results"]:
        assert "guided_journey" not in r
    one = payload_of(call(client, "tools/call",
                          {"name": "fetch", "arguments": {"id": hits["results"][0]["id"]}}))
    assert "guided_journey" not in one


def test_the_other_three_tools_answer_over_the_wire(client):
    workflow = payload_of(call(client, "tools/call",
                               {"name": "get_workflow", "arguments": {"workflow_id": "workflow"}}))
    assert workflow["text"]
    prompts = payload_of(call(client, "tools/call",
                              {"name": "get_prompt_template", "arguments": {"task": "BIA preparation"}}))
    assert prompts["templates"]
    risks = payload_of(call(client, "tools/call",
                            {"name": "identify_ai_risks",
                             "arguments": {"task_description": "use AI to run a BIA"}}))
    assert risks["cited_sections"]


# ── /health ──────────────────────────────────────────────────────────────────────────────
def test_health_reports_chunk_count_version_and_build_date(client, server):
    body = client.get("/health").json()
    assert body["ok"] is True
    assert body["chunks"] == len(server.get_index().chunks) == 96
    assert body["version"] == server.SERVER_VERSION
    assert body["release_tag"] == TAG
    assert body["built_at"] and body["built_at"].endswith("+00:00")


def test_index_json_publishes_every_chunks_citation(client, server):
    """Contract version 2: a consumer can no longer construct a citation from a chunk id, so
    the index that carries them is published — unauthenticated, like /health."""
    body = client.get("/index.json").json()
    assert body["release_tag"] == TAG
    assert body["chunk_count"] == len(body["topics"]) == len(server.get_index().chunks)
    for topic in body["topics"]:
        assert topic["url"].startswith(f"https://github.com/AI4BCM/guidance/blob/{TAG}/")
        assert "#" in topic["url"]
    ids = {t["id"] for t in body["topics"]}
    assert "stages-govern-level" in ids


def test_nothing_here_reads_an_authorization_header(client):
    """The connector is open (owner, 2026-09-10): no token verifier, no bearer middleware,
    no scope check, and no handler that looks at a request header at all. Over the SYNTAX,
    not the text — the module docstring names all four on purpose, to say why they are
    absent, and a grep cannot tell an explanation from an import.

    The way this regresses is someone copying a block over from the BIA server, where every
    one of these exists and is load-bearing."""
    import ast
    tree = ast.parse((REPO / "tools" / "server.py").read_text(encoding="utf-8"))
    names = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
    names |= {n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)}
    names |= {(a.asname or a.name).split(".")[0]
              for n in ast.walk(tree) if isinstance(n, ast.ImportFrom | ast.Import)
              for a in n.names}
    for banned in ("BearerAuthBackend", "TokenVerifier", "StaticTokenVerifier",
                   "AuthenticationMiddleware", "AuthContextMiddleware", "MCP_SCOPES",
                   "headers", "AuthSettings"):
        assert banned not in names, banned
    assert client.get("/health").status_code == 200


def test_an_unknown_host_is_refused(client):
    """The one knob ticket 06 must set: AI4BCM_MCP_ALLOWED_HOSTS. Without the public name in
    it the connector answers 421 to every request, which reads as broken rather than as
    misconfigured — so the behaviour is pinned here, where the knob is named.

    Host header rather than a second TestClient: `streamable_http_app()` wires a session
    manager whose `.run()` raises if a second app instance is started in the same process.

    Measured 2026-09-10: the check guards `/mcp` ONLY. `/health` is a custom route outside the
    transport-security wrapper and answers 200 on any Host — which is the behaviour a monitor
    wants, and is worth knowing before someone reads a green /health as proof the connector is
    reachable by its clients."""
    bad = {"Host": "evil.example", "Content-Type": "application/json",
           "Accept": "application/json, text/event-stream"}
    resp = client.post("/mcp", json={"jsonrpc": "2.0", "id": 1, "method": "tools/list",
                                     "params": {}}, headers=bad)
    assert resp.status_code == 421
    assert client.get("/health", headers={"Host": "evil.example"}).status_code == 200


def test_root_says_what_this_is(client):
    assert "/mcp" in client.get("/").text


def test_a_call_with_no_token_is_served(client):
    """The load-bearing consequence of the open decision, asserted rather than assumed."""
    result = call(client, "tools/call", {"name": "search", "arguments": {"query": "principles"}})
    assert "error" not in result
    assert payload_of(result)["results"]
