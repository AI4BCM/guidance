#!/usr/bin/env python3
"""Single-column PDF prose -> Markdown, with anything that is not prose marked as such.

Built for the NIST publications: one column of prose, numbered headings, boxed sidebars and
a handful of wide tables. Extraction runs in `pdftotext -raw`, which follows the tagged
reading order, because `-layout` weaves a sidebar into the sentence beside it and produces
lines that were never written. Raw mode has the opposite failure: a table arrives as its
cells one after another, and re-flowing those into a paragraph would read as a sentence the
publisher never wrote. So every re-flowed run is tested for prose - English prose is roughly
a third function words - and a run that fails is emitted verbatim in a fenced block, marked
as a raw extraction whose order is not reliable. Nothing is dropped and nothing is invented.
"""
from __future__ import annotations

import argparse
import re
import subprocess
from collections import Counter

CAPTION = re.compile(r"^\s*(Table|Figure)\s+([A-Z]?\d+-\d+|\d+)[.:]\s*(.*)$")
HEADING = re.compile(r"^\s{0,6}((?:Chapter\s+\d+\.)|(?:Appendix\s+[A-Z][—-])|(?:\d+(?:\.\d+)+))\s+(\S.*)$")
FOOTER = re.compile(r"^\s*(CHAPTER|APPENDIX|SECTION)\s+[A-Z0-9]{1,4}\s+\d{1,4}\s*$", re.I)
PAGE_NO = re.compile(r"^\s*(\d{1,3}|[ivxlcdm]{1,7})\s*$", re.I)
COLUMNAR = re.compile(r"\S {4,}\S")
NUMBERED = re.compile(r"^\s*\d{1,3}\.\s+[A-Z(\u2018\u201c]")
BULLET = re.compile(r"^\s*[•▪●-]\s+(\S.*)$")


def pages_of(pdf: str, first: int, last: int) -> list[list[str]]:
    txt = subprocess.run(["pdftotext", "-raw", "-f", str(first), "-l", str(last), pdf, "-"],
                         check=True, capture_output=True, text=True).stdout
    return [p.splitlines() for p in txt.split("\f")]


def running_lines(pages: list[list[str]]) -> set[str]:
    """Lines that repeat on most pages are the running header or footer, not content."""
    counts: Counter[str] = Counter()
    for page in pages:
        for line in page[:2] + page[-2:]:
            s = line.strip()
            if s:
                counts[s] += 1
    threshold = max(3, len(pages) // 3)
    return {s for s, n in counts.items() if n >= threshold}


def dehyphenate(lines: list[str]) -> str:
    """Re-join wrapped lines, telling a line-break hyphen from a real one.

    `contin-` + `gency` is one word broken across lines; `AI-` + `enabled` is a hyphenated
    word that happened to break at its own hyphen. The letter before the hyphen decides:
    lower case means the break is the extractor's, anything else means the author's.
    """
    out = ""
    for ln in lines:
        ln = ln.strip()
        if not out:
            out = ln
        elif out.endswith("-") and ln[:1].islower():
            out = (out[:-1] if len(out) > 1 and out[-2].islower() else out) + ln
        else:
            out += " " + ln
    return re.sub(r"\s+", " ", out).strip()


FUNCTION_WORDS = {"the", "and", "of", "to", "a", "in", "is", "are", "for", "that", "with",
                  "on", "be", "by", "as", "it", "or", "which", "this", "an", "must",
                  "should", "not", "their", "its", "from", "all", "at", "can", "has",
                  "may", "will", "these", "such", "each", "when", "if", "any"}


def reads_as_prose(text: str) -> bool:
    tokens = [t.lower().strip(".,;:()'\u2018\u2019\u201c\u201d") for t in text.split()]
    if len(tokens) < 25:
        return True
    hits = sum(1 for t in tokens if t in FUNCTION_WORDS)
    return hits / len(tokens) >= 0.08


def convert(pdf: str, first: int, last: int) -> tuple[list[str], list[str]]:
    pages = pages_of(pdf, first, last)
    skip = running_lines(pages)
    out: list[str] = []
    raw_blocks: list[str] = []
    buf: list[str] = []
    last_caption = ""
    expect_table = False

    def flush(page_no: int):
        nonlocal buf, expect_table
        if not buf:
            return
        text = dehyphenate(buf)
        was_table, expect_table = expect_table, False
        if reads_as_prose(text) and not was_table:
            out.append(text)
            out.append("")
        else:
            name = last_caption or "A block that does not read as prose"
            out.append(f"*{name} — raw text extraction from page {page_no} of the PDF, in the "
                       f"order the extractor produced it. It is a table's cells or a figure's "
                       f"labels, not a sentence; it is shown as extracted rather than re-flowed. "
                       f"The PDF is authoritative.*")
            out.append("")
            out.append("```text")
            out.extend(buf)
            out.append("```")
            out.append("")
            raw_blocks.append(f"{name} (p. {page_no})")
        buf = []

    for idx, page in enumerate(pages):
        page_no = first + idx
        for raw in page:
            s_line = raw.strip()
            if not s_line or s_line in skip or PAGE_NO.match(raw) or FOOTER.match(raw):
                flush(page_no)
                continue
            cap = CAPTION.match(raw)
            if cap and len(s_line) < 120:
                flush(page_no)
                last_caption = s_line.rstrip(".")
                expect_table = s_line.lower().startswith("table")
                out.append("*%s*" % s_line)
                out.append("")
                continue
            m = HEADING.match(raw)
            if m and len(s_line) < 100 and not s_line.endswith((".", ",", ";")):
                flush(page_no)
                num, title = m.group(1), m.group(2).strip()
                level = 2 if num.startswith(("Chapter", "Appendix")) else min(5, 2 + num.count("."))
                out.append("#" * level + " " + num + " " + re.sub(r"\s+", " ", title))
                out.append("")
                continue
            b = BULLET.match(raw)
            if b:
                flush(page_no)
                out.append("- " + re.sub(r"\s+", " ", b.group(1).strip()))
                continue
            if NUMBERED.match(raw):
                flush(page_no)        # a numbered paragraph starts its own block
            buf.append(s_line)
        flush(page_no)
    return out, raw_blocks


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("out")
    ap.add_argument("--header", required=True, help="file holding the H1 and the conversion note")
    ap.add_argument("--first", type=int, default=1)
    ap.add_argument("--last", type=int, default=0)
    args = ap.parse_args()
    last = args.last or int(subprocess.run(["pdfinfo", args.pdf], capture_output=True, text=True)
                            .stdout.split("Pages:")[1].split()[0])
    body, dropped = convert(args.pdf, args.first, last)
    header = open(args.header, encoding="utf-8").read().rstrip()
    txt = re.sub(r"\n{3,}", "\n\n", header + "\n\n" + "\n".join(body)).strip() + "\n"
    open(args.out, "w", encoding="utf-8").write(txt)
    print(args.out, len(txt), "blocks shown raw (not prose):", len(dropped))
    for d in dropped:
        print("   ", d)


if __name__ == "__main__":
    main()
