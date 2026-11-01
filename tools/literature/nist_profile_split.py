#!/usr/bin/env python3
"""Restore the row and heading breaks `pdf_prose_to_md.py` runs together in NIST AI 600-1.

The Generative AI Profile has two shapes the NIST converter does not see. Its numbered
sub-sections ("2.2. Confabulation", "A.1.3. Third-Party Considerations") end with a full stop
after the number, so they are read as the first words of the paragraph below. Its action
tables (Action ID, Suggested Action, GAI Risks) pass the prose test, because each cell is a
sentence, and so arrive as one paragraph per table.

This pass changes line breaks only. It takes the sub-section titles from the PDF's own lines,
marks them as headings, and starts a new paragraph at each table caption (GOVERN 1.2: ...),
at each column-header row, at each action id (GV-6.2-006) and at each "AI Actor Tasks" line.
It refuses to write if the sequence of words differs from its input.

Usage: nist_profile_split.py PDF MARKDOWN   (rewrites MARKDOWN in place)
"""
from __future__ import annotations

import re
import subprocess
import sys

SUBSECTION = re.compile(r"^((?:2\.\d+\.)|(?:A\.\d+\.(?:\d+\.)?)) \S.*$")
ACTION_ID = re.compile(r" (?=(?:GV|MP|MS|MG)-\d+\.\d+-\d{3} )")
CAPTION = re.compile(r" (?=(?:GOVERN|MAP|MEASURE|MANAGE) \d+\.\d+: )")
BREAK_BEFORE = ("Action ID Suggested Action GAI Risks", "AI Actor Tasks:")


def words(text: str) -> list[str]:
    return re.sub(r"(?m)^#+ ", "", text).split()


def split(md: str, pdf_lines: list[str]) -> str:
    out = md
    for line in pdf_lines:
        m = SUBSECTION.match(line.strip())
        if not m:
            continue
        title = line.strip()
        level = "###" if title.startswith("2.") or title.count(".") == 2 else "####"
        out = out.replace(f" {title} ", f"\n\n{level} {title}\n\n", 1) if f"\n{title} " not in out \
            else out.replace(f"\n{title} ", f"\n{level} {title}\n\n", 1)
    out = ACTION_ID.sub("\n\n", out)
    out = CAPTION.sub("\n\n", out)
    for marker in BREAK_BEFORE:
        out = out.replace(f" {marker}", f"\n\n{marker}")
    return re.sub(r"\n{3,}", "\n\n", out)


def main() -> int:
    pdf, md_path = sys.argv[1], sys.argv[2]
    pdf_lines = subprocess.run(["pdftotext", "-raw", pdf, "-"], check=True, capture_output=True,
                               text=True).stdout.splitlines()
    md = open(md_path, encoding="utf-8").read()
    out = split(md, pdf_lines)
    if words(out) != words(md):
        raise SystemExit("word sequence changed; refusing to write")
    open(md_path, "w", encoding="utf-8").write(out)
    print(md_path, "headings:", len(re.findall(r"(?m)^#{3,4} ", out)),
          "action ids:", len(re.findall(r"(?m)^(?:GV|MP|MS|MG)-\d+\.\d+-\d{3} ", out)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
