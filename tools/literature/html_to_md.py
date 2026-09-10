#!/usr/bin/env python3
"""A small, honest HTML -> Markdown converter for carried literature.

It handles exactly what the carried government HTML uses: headings, paragraphs,
lists, tables, inline emphasis and links. Anything it does not know it renders as
its text, so no wording is lost silently. Tables become real Markdown tables and are
spot-checked against the original before a file is registered.
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser

VOID = {"br", "img", "col", "meta", "link", "hr", "input", "source"}
SKIP = {"script", "style", "nav", "svg"}


class Node:
    def __init__(self, tag, attrs=None):
        self.tag = tag
        self.attrs = dict(attrs or {})
        self.kids = []

    def cls(self):
        return self.attrs.get("class", "")

    def text(self):
        return "".join(k if isinstance(k, str) else k.text() for k in self.kids)


class _P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs)
        self.stack[-1].kids.append(n)
        if tag not in VOID:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].kids.append(Node(tag, attrs))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        self.stack[-1].kids.append(data)


def parse(html: str) -> Node:
    p = _P()
    p.feed(html)
    return p.root


def norm(s: str) -> str:
    s = s.replace("\xa0", " ").replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    return re.sub(r"[ \t\n]+", " ", s).strip()


def inline(node: Node) -> str:
    out = []
    for k in node.kids:
        if isinstance(k, str):
            out.append(k)
            continue
        if k.tag in SKIP:
            continue
        if k.tag == "br":
            out.append(" ")
        elif k.tag in ("strong", "b"):
            t = inline(k).strip()
            out.append("**%s**" % t if t else "")
        elif k.tag in ("em", "i"):
            t = inline(k).strip()
            out.append("*%s*" % t if t else "")
        elif k.tag == "code":
            out.append("`%s`" % inline(k).strip())
        else:
            out.append(inline(k))
    return "".join(out)


def rows_of(table: Node):
    rows = []

    def rec(n):
        for k in n.kids:
            if not isinstance(k, Node):
                continue
            if k.tag == "table":
                continue
            if k.tag == "tr":
                rows.append([c for c in k.kids if isinstance(c, Node) and c.tag in ("td", "th")])
            else:
                rec(k)

    rec(table)
    return rows


def cell_text(cell: Node) -> str:
    """A table cell, with its line breaks kept visible.

    A `<br>` inside a cell means one of two things in the government HTML: a new
    sentence, or a new item in a short list. Ending punctuation tells them apart, so a
    four-item cell does not silently become one run of words.
    """
    parts, buf = [], []
    for k in cell.kids:
        if isinstance(k, Node) and k.tag == "br":
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(k if isinstance(k, str) else inline(k))
    parts.append("".join(buf))
    parts = [norm(p) for p in parts]
    parts = [p for p in parts if p]
    out = ""
    for p in parts:
        if not out:
            out = p
        elif out.endswith((".", ";", ":", "?", "!")):
            out += " " + p
        else:
            out += " / " + p
    return out


def render_table(table: Node) -> str:
    rows = [[cell_text(c) for c in r] for r in rows_of(table)]
    rows = [r for r in rows if any(r)]
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    md = ["| " + " | ".join(c.replace("|", "\\|") for c in rows[0]) + " |",
          "|" + "---|" * width]
    for r in rows[1:]:
        md.append("| " + " | ".join(c.replace("|", "\\|") for c in r) + " |")
    return "\n".join(md)


def render(node: Node, out: list, indent: str = "", heading_shift: int = 0) -> None:
    for k in node.kids:
        if isinstance(k, str):
            t = norm(k)
            if t:
                out.append(indent + t)
            continue
        if k.tag in SKIP:
            continue
        if re.fullmatch(r"h[1-6]", k.tag or ""):
            level = max(1, min(6, int(k.tag[1]) + heading_shift))
            t = norm(inline(k))
            if t:
                out.append("")
                out.append("#" * level + " " + t)
                out.append("")
        elif k.tag == "p":
            t = norm(inline(k))
            if t:
                out.append(indent + t)
                out.append("")
        elif k.tag in ("ul", "ol"):
            n = 0
            for li in [c for c in k.kids if isinstance(c, Node) and c.tag == "li"]:
                n += 1
                bullet = "- " if k.tag == "ul" else "%d. " % n
                inner = [c for c in li.kids if isinstance(c, Node) and c.tag in ("ul", "ol")]
                head = norm("".join(
                    (c if isinstance(c, str) else ("" if c.tag in ("ul", "ol") else inline(c)))
                    for c in li.kids))
                out.append(indent + bullet + head)
                for sub in inner:
                    wrapper = Node("div")
                    wrapper.kids = [sub]
                    render(wrapper, out, indent + "  ", heading_shift)
            out.append("")
        elif k.tag == "table":
            t = render_table(k)
            if t:
                out.append("")
                out.append(t)
                out.append("")
        elif k.tag == "blockquote":
            sub = []
            render(k, sub, "", heading_shift)
            out.extend("> " + line if line else ">" for line in sub)
            out.append("")
        else:
            render(k, out, indent, heading_shift)


def to_markdown(html: str, heading_shift: int = 0) -> str:
    out: list[str] = []
    render(parse(html), out, "", heading_shift)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


if __name__ == "__main__":
    sys.stdout.write(to_markdown(open(sys.argv[1], encoding="utf-8").read(),
                                 int(sys.argv[2]) if len(sys.argv) > 2 else 0))
