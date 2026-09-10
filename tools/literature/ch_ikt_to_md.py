#!/usr/bin/env python3
"""Swiss ICT minimum standard (BWL/BACS, English, May 2023) -> Markdown.

The PDF mixes two layouts, and each needs a different extraction:

* Two-column prose (the preface, Section 1, Part 2's overview, Section 3). Plain
  `pdftotext -layout` interleaves the columns into nonsense; `pdftotext -raw` follows the
  tagged reading order and gets them right, so prose pages are read in raw mode and
  re-flowed into paragraphs.
* The task, reference and glossary tables (Section 2 and the glossary). Raw mode flattens
  them — every label first, then every text — so those pages are read in layout mode and the
  columns are split at the header's own column position, which is what pairs a task id with
  its task.

Nothing is summarised or re-worded. Pages that are neither (the cover, the contents, the
lists of figures and tables, the credits) are left out.
"""
from __future__ import annotations

import re
import subprocess
import sys

FUNCTIONS = {"Identify", "Protect", "Detect", "Respond", "Recover"}
SKIP = "\x00"                     # a line to drop without breaking the paragraph it sits in
RUNNING_HEAD = re.compile(r"^\s*(\d)\s+(Section \d+ .|Part \d+ .|Appendix)")
FOOTER = re.compile(r"^\s*Minimum ICT standard 2023\s+\d+\s*$")
HEADING = re.compile(r"^\s{0,3}(\d+(?:\.\d+)*)\s+(\S.{0,80})$")
TABLE_CAPTION = re.compile(r"^\s*Table\s+\d+:\s*(.+)$")
FIGURE_CAPTION = re.compile(r"^\s*Figure\s+\d+:\s*(.+)$")
HEADERS = ("Description", "Standard", "Term")


def pdftotext(pdf: str, first: int, last: int, mode: str) -> str:
    return subprocess.run(["pdftotext", mode, "-f", str(first), "-l", str(last), pdf, "-"],
                          check=True, capture_output=True, text=True).stdout


# The assessment example on pages 38-39 is a screenshot of an Excel sheet with German
# labels and a broken font encoding; pdftotext returns it as mojibake. Any paragraph
# carrying those glyphs is dropped rather than published as the publisher's wording.
MOJIBAKE = re.compile(r"[\u0100-\u024f]")
FUNCTION_WORDS = {"the", "and", "of", "to", "a", "in", "is", "are", "for", "that", "with",
                  "on", "be", "by", "as", "it", "or", "which", "this", "an", "must",
                  "should", "not", "their", "its", "from", "all", "at", "can", "has"}


def is_garbage(paragraph: str) -> bool:
    """True for text the extraction cannot be trusted to have read in order.

    Two shapes appear in this PDF, both from the assessment example's charts: a broken
    font encoding, and a long run of chart labels. English prose is roughly a third
    function words; a thirty-token run with almost none is a picture's labels.
    """
    if len(MOJIBAKE.findall(paragraph)) > 2:
        return True
    tokens = [t.lower().strip(".,;:()'\u2018\u2019") for t in paragraph.split()]
    if len(tokens) < 30:
        return False
    hits = sum(1 for t in tokens if t in FUNCTION_WORDS)
    return hits / len(tokens) < 0.02


QUOTED = re.compile(r"\u2018([^\u2019]{1,60})\u2019(?=[A-Za-z])")


def spacing(text: str) -> str:
    """Restore the spaces the PDF's kerning drops around quoted terms.

    `the\u2018Framework\u2019section` is how pdftotext reads a quoted word in this file. Only a
    quote that closes an opening quote is touched, so possessives are left alone.
    """
    text = QUOTED.sub(lambda m: "\u2018%s\u2019 " % m.group(1), text)
    text = re.sub(r"(?<=[A-Za-z,:;.])\u2018", " \u2018", text)
    return re.sub(r"  +", " ", text)


def bullets(paragraph: str) -> list[str]:
    """A run of `\u2022` markers in one re-flowed paragraph is a list; give it its lines back."""
    if " \u2022 " not in paragraph:
        return [paragraph]
    head, _, rest = paragraph.partition(" \u2022 ")
    out = [head] if head.strip() else []
    return out + ["- " + p.strip() for p in rest.split(" \u2022 ") if p.strip()]


def dehyphenate(lines: list[str]) -> str:
    out = ""
    for ln in lines:
        ln = ln.strip()
        if not out:
            out = ln
        elif out.endswith("-") and ln[:1].islower():
            out = out[:-1] + ln
        else:
            out += " " + ln
    return out


def clean(lines: list[str]) -> list[str]:
    keep = []
    for ln in lines:
        s = ln.strip()
        if FOOTER.match(ln):
            keep.append(SKIP)
            continue
        if not s:
            keep.append("")
            continue
        if s in FUNCTIONS and len(ln) - len(ln.lstrip()) > 40:
            keep.append(SKIP)
            continue
        keep.append(ln.rstrip())
    return keep


def looks_like_heading(m: re.Match, line: str) -> bool:
    """A numbered heading, not a sentence that happens to start with a figure.

    `0 and 4 (the coloured line)...` is a wrapped sentence; `3.2.1 Tier 1: partial` is a
    heading. A bare top-level number only counts in front of Section, Part or Appendix.
    """
    num, title = m.group(1), m.group(2).strip()
    if len(line) >= 90 or line.endswith((".", ",", ";")):
        return False
    if not title[:1].isupper():
        return False
    return "." in num or title.startswith(("Section", "Part", "Appendix"))


def heading_md(num: str, title: str) -> str:
    level = min(4, 1 + num.count(".") + 1)  # "2" -> ##, "2.2" -> ###, "2.2.1" -> ####
    return "#" * level + " " + num + " " + title.strip()


seen: set[str] = set()
dropped: list[str] = []


def prose_pages(pdf: str, first: int, last: int) -> list[str]:
    out: list[str] = []
    buf: list[str] = []

    def flush():
        nonlocal buf
        if buf:
            para = spacing(dehyphenate(buf))
            buf = []
            if is_garbage(para):
                dropped.append(para[:60])
                return
            out.extend(bullets(para))
            out.append("")

    for raw in clean(pdftotext(pdf, first, last, "-raw").splitlines()):
        if raw == SKIP:
            continue
        s = raw.strip()
        if not s:
            flush()
            continue
        m = HEADING.match(raw)
        if m and looks_like_heading(m, s):
            head = heading_md(m.group(1), m.group(2))
            if RUNNING_HEAD.match(raw) and head in seen:
                continue                      # a page's running head, not a new section
            if head in seen:
                continue
            flush()
            seen.add(head)
            out.append(head)
            out.append("")
            continue
        buf.append(s)
    flush()
    return out


def table_pages(pdf: str, first: int, last: int) -> list[str]:
    out: list[str] = []
    buf: list[str] = []
    rows: list[list[str]] = []
    header: tuple[str, str] | None = None
    col2 = 0

    def flush_prose():
        nonlocal buf
        if buf:
            out.extend(bullets(spacing(dehyphenate(buf))))
            out.append("")
            buf = []

    def flush_table():
        nonlocal rows, header
        if header and rows:
            out.append("| %s | %s |" % header)
            out.append("|---|---|")
            for label, text in rows:
                out.append("| %s | %s |" % (spacing(label).replace("|", "\\|"),
                                            spacing(text).replace("|", "\\|")))
            out.append("")
        rows, header = [], None

    for raw in clean(pdftotext(pdf, first, last, "-layout").splitlines()):
        if raw == SKIP:
            continue
        s = raw.strip()
        if not s:
            continue
        cap = TABLE_CAPTION.match(raw) or FIGURE_CAPTION.match(raw)
        if cap:
            flush_table()
            flush_prose()
            out.append("*%s*" % s)
            out.append("")
            continue
        first_word = s.split()[0]
        if header is None and first_word in HEADERS and len(s.split()) <= 3:
            flush_prose()
            parts = re.split(r"\s{2,}", s)
            if len(parts) == 2:
                header = (parts[0], parts[1])
                col2 = raw.index(parts[1])
                rows = []
                continue
        if header is not None:
            indent = len(raw) - len(raw.lstrip())
            if indent >= col2 - 2 and rows:
                cont = raw[col2 - 2:].strip() if len(raw) > col2 - 2 else s
                prev = rows[-1]
                prev[1] = dehyphenate([prev[1], cont])
            elif indent >= col2 - 2 and not rows:
                continue
            else:
                label = raw[:col2].strip()
                text = raw[col2:].strip()
                if not label and rows:
                    rows[-1][1] = dehyphenate([rows[-1][1], text])
                elif label.startswith(tuple("0123456789")) and HEADING.match(raw):
                    flush_table()
                    m = HEADING.match(raw)
                    out.append(heading_md(m.group(1), m.group(2)))
                    out.append("")
                else:
                    rows.append([label, text])
            continue
        m = HEADING.match(raw)
        if m and looks_like_heading(m, s):
            head = heading_md(m.group(1), m.group(2))
            if head in seen:
                continue
            flush_prose()
            seen.add(head)
            out.append(head)
            out.append("")
            continue
        buf.append(s)
    flush_table()
    flush_prose()
    return out


# Page 2 sets the preface and the management summary side by side with no paragraph break
# of their own, so the re-flow returns them as one run. These two splits give the headings
# back without changing a word.
PAGE2_SPLITS = (
    ("Preface Digitalisation demands defensive action ",
     "## Preface\n\n**Digitalisation demands defensive action**\n\n"),
    (" Management Summary This Minimum ICT Standard serves",
     "\n\n## Management Summary\n\nThis Minimum ICT Standard serves"),
)


def main(pdf: str, out_path: str, header: str) -> None:
    parts: list[str] = [header.rstrip(), ""]
    parts += prose_pages(pdf, 2, 2)      # preface and management summary
    parts += prose_pages(pdf, 4, 13)     # Section 1 - Introduction
    parts += prose_pages(pdf, 14, 14)    # Part 2 - overview
    parts += table_pages(pdf, 15, 36)    # Part 2 - the 106 tasks and their references
    parts += prose_pages(pdf, 37, 39)    # Section 3 - Assessment
    # The glossary (pp. 41-42) is deliberately NOT carried: its term column runs onto a
    # second line and the column split pairs the halves wrongly, cutting words in two. A
    # gap is honest; a mangled definition under the publisher name is not.
    txt = "\n".join(parts)
    for old, new in PAGE2_SPLITS:
        if old not in txt:
            raise SystemExit("page 2 did not extract as expected: %r not found" % old[:40])
        txt = txt.replace(old, new, 1)
    txt = re.sub(r"\n{3,}", "\n\n", txt).strip() + "\n"
    open(out_path, "w", encoding="utf-8").write(txt)
    print(out_path, len(txt))
    for d in dropped:
        print("  dropped (unreadable extraction):", d)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], open(sys.argv[3], encoding="utf-8").read())
