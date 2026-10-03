"""Top-k hit rate of the connector's search on the eval set (search_eval.json).

    python3 tools/eval_search.py <data dir holding chunks.json and index.json>

A question is a hit when a chunk of any expected unit is in the top k. Stdlib only.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from retrieval import GuidanceIndex

EVAL = Path(__file__).resolve().parent / "search_eval.json"


def main(data_dir: str) -> int:
    spec = json.loads(EVAL.read_text(encoding="utf-8"))
    index = GuidanceIndex(Path(data_dir))
    hits = 0
    for question in spec["questions"]:
        units = [chunk.unit for chunk in index.search(question["q"], limit=spec["k"])]
        rank = next((n for n, unit in enumerate(units, 1) if unit in question["expect"]), None)
        hits += rank is not None
        print(f"{'miss' if rank is None else f'#{rank}  '}  {question['q']}  ->  {', '.join(units)}")
    print(f"hit@{spec['k']}: {hits}/{len(spec['questions'])}  ({index.chunks[0].release_tag})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
