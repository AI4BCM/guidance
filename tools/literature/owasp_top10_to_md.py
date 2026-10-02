#!/usr/bin/env python3
"""OWASP Top 10 for Agentic Applications (PDF) -> Markdown, the ten entries only.

The OWASP PDF is a Word export with one column of prose, a fixed set of sub-headings per entry
and numbered lists. `pdf_prose_to_md.py` is tuned for NIST and reads every numbered list item as
a heading, so this converter knows the OWASP shape instead:

- `pdftotext -raw`, the running "Page N" and "genai.owasp.org" lines dropped;
- `ASIxx: Title` becomes `##` (a title wrapped over two lines is joined), the five fixed
  sub-headings become `###`;
- a numbered item starts its own line; other lines are joined into paragraphs, and a paragraph
  ends where a line ends a sentence well short of the column width.

Only line breaks are changed: the converter refuses to write unless the words of the output equal
the words of the extracted range, in order. Nothing is summarised.

Usage: owasp_top10_to_md.py PDF OUT --header HEADER_FILE
"""
from __future__ import annotations

import argparse
import re
import subprocess

SUBHEADINGS = ("Description", "Common Examples of the Vulnerability", "Example Attack Scenarios",
               "Prevention and Mitigation Guidelines", "References")
START = re.compile(r"^ASI01: ")
STOP = "Appendix A - OWASP Agentic"
RUNNING = re.compile(r"^(Page \d+|genai\.owasp\.org)$")
ENTRY = re.compile(r"^ASI\d\d: ")
ITEM = re.compile(r"^\d{1,2}\. ")
FULL_WIDTH = 90


def extract(pdf: str) -> list[str]:
    txt = subprocess.run(["pdftotext", "-raw", pdf, "-"], check=True, capture_output=True,
                         text=True).stdout
    lines = [l.rstrip() for l in txt.replace("\f", "\n").splitlines()]
    # The contents page and the "At a glance" diagram name ASI01 too; the entry itself is the
    # ASI01 line followed by its Description heading.
    start = next(i for i, l in enumerate(lines)
                 if START.match(l) and lines[i + 1].strip() == "Description")
    stop = next(i for i, l in enumerate(lines) if l.strip().startswith(STOP) and i > start)
    return [l for l in lines[start:stop] if l.strip() and not RUNNING.match(l.strip())]


def convert(lines: list[str]) -> str:
    out: list[str] = []
    buf: list[str] = []

    def flush() -> None:
        if buf:
            out.append(" ".join(buf))
            buf.clear()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if ENTRY.match(line):
            flush()
            title = line
            while i + 1 < len(lines) and lines[i + 1].strip() not in SUBHEADINGS:
                i += 1
                title += " " + lines[i].strip()
            out.append(f"## {title}")
        elif line in SUBHEADINGS:
            flush()
            out.append(f"### {line}")
        else:
            if ITEM.match(line):
                flush()
            buf.append(line)
            if re.search(r"[.:]$", line) and len(line) < FULL_WIDTH:
                flush()
        i += 1
    flush()
    return "\n\n".join(out)


def words(text: str) -> list[str]:
    return [w for w in re.sub(r"^#+ ", "", text, flags=re.M).split()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("out")
    ap.add_argument("--header", required=True)
    args = ap.parse_args()
    lines = extract(args.pdf)
    body = convert(lines)
    if words(body) != words("\n".join(lines)):
        raise SystemExit("word sequence changed in conversion; refusing to write")
    header = open(args.header, encoding="utf-8").read().rstrip()
    open(args.out, "w", encoding="utf-8").write(header + "\n\n" + body + "\n")
    print(args.out, "entries:", body.count("\n## ") + body.startswith("## "), "words:", len(words(body)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
