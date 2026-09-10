#!/usr/bin/env python3
"""EUR-Lex Cellar XHTML -> Markdown, enacting terms only.

Structure-preserving: chapter/section headings become H2, each article an H3, the
OJ two-column label tables become markdown lists, any other table a markdown table.
"""
import html, re, sys
from html.parser import HTMLParser

VOID = {"br","img","col","meta","link","hr","input"}

class Node:
    def __init__(self, tag, attrs=None):
        self.tag = tag; self.attrs = dict(attrs or {}); self.kids = []
    def cls(self): return self.attrs.get("class","")
    def text(self):
        out=[]
        for k in self.kids:
            out.append(k if isinstance(k,str) else k.text())
        return "".join(out)

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root"); self.stack=[self.root]
    def handle_starttag(self, tag, attrs):
        n=Node(tag,attrs); self.stack[-1].kids.append(n)
        if tag not in VOID: self.stack.append(n)
    def handle_startendtag(self, tag, attrs):
        self.stack[-1].kids.append(Node(tag,attrs))
    def handle_endtag(self, tag):
        if tag in VOID: return
        for i in range(len(self.stack)-1,0,-1):
            if self.stack[i].tag==tag:
                del self.stack[i:]; return
    def handle_data(self, data):
        self.stack[-1].kids.append(data)

def parse(path):
    p=P(); p.feed(open(path,encoding="utf-8").read()); return p.root

def find(node, pred, out=None):
    out = [] if out is None else out
    for k in node.kids:
        if isinstance(k,Node):
            if pred(k): out.append(k)
            find(k,pred,out)
    return out

def norm(s):
    s = s.replace("\xa0"," ").replace("’","'").replace("‘","'")
    s = s.replace("“",'"').replace("”",'"')
    return re.sub(r"[ \t\n]+"," ",s).strip()

def inline(node):
    """Inline text of a node, skipping nested tables (they are rendered as lists)."""
    parts=[]
    for k in node.kids:
        if isinstance(k,str): parts.append(k); continue
        if k.tag=="br": parts.append(" "); continue
        if k.tag=="table": continue
        if "oj-note-tag" in k.cls() or "note-tag" in k.cls():
            parts.append("[%s]" % norm(k.text())); continue
        parts.append(inline(k))
    return "".join(parts)

def direct_rows(table):
    """Rows belonging to this table only — never a nested table's rows."""
    rows=[]
    def rec(n):
        for k in n.kids:
            if not isinstance(k,Node): continue
            if k.tag=="table": continue
            if k.tag=="tr":
                rows.append([c for c in k.kids if isinstance(c,Node) and c.tag in ("td","th")])
            else:
                rec(k)
    rec(table)
    return rows

def child_tables(node):
    out=[]
    def rec(n):
        for k in n.kids:
            if not isinstance(k,Node): continue
            if k.tag=="table": out.append(k)
            else: rec(k)
    rec(node)
    return out

LABEL = re.compile(r"^\(?[0-9ivxlcIVXLC]{1,6}\)?\.?$|^\([a-zA-Z]{1,3}\)$|^[-—–•]$")

def render_table(table, indent=""):
    rows=direct_rows(table)
    cells_txt=[[norm(inline(c)) for c in r] for r in rows]
    keep=[i for i,r in enumerate(cells_txt) if any(r) or any(child_tables(c) for c in rows[i])]
    if not keep: return ""
    rows=[rows[i] for i in keep]; cells_txt=[cells_txt[i] for i in keep]
    lines=[]
    if all(len(r)<=2 for r in cells_txt) and all(
            (len(r)==1) or LABEL.match((r[0] or "-").lstrip("'")) for r in cells_txt):
        for r_nodes, r in zip(rows, cells_txt):
            if len(r)==2:
                lines.append(("%s- %s %s" % (indent, r[0], r[1])).rstrip())
                nested_host = r_nodes[1]
            else:
                lines.append(("%s- %s" % (indent, r[0])).rstrip())
                nested_host = r_nodes[0]
            for t in child_tables(nested_host):
                sub=render_table(t, indent+"  ")
                if sub: lines.append(sub.strip("\n"))
        return "\n" + "\n".join(lines) + "\n"
    width=max(len(r) for r in cells_txt)
    padded=[r+[""]*(width-len(r)) for r in cells_txt]
    md=["| " + " | ".join(c.replace("|","\\|") for c in padded[0]) + " |",
        "|" + "---|"*width]
    for r in padded[1:]:
        md.append("| " + " | ".join(c.replace("|","\\|") for c in r) + " |")
    return "\n" + "\n".join(md) + "\n"

def render_block(node, out):
    """Render a container's block-level children into markdown lines."""
    for k in node.kids:
        if isinstance(k,str):
            t=norm(k)
            if t: out.append(t)
            continue
        if k.tag=="p":
            t=norm(inline(k))
            if t: out.append(t)
        elif k.tag=="table":
            t=render_table(k).strip()
            if t: out.append(t)
        elif k.tag in ("div","span","td","tr","tbody","table"):
            render_block(k,out)

def wrap(k):
    n = Node("div"); n.kids=[k]; return n

def article_md(art):
    ti = next((n for n in find(art, lambda n:"oj-ti-art" in n.cls())), None)
    sti = next((n for n in find(art, lambda n:"oj-sti-art" in n.cls())), None)
    title = norm(ti.text()) if ti is not None else art.attrs.get("id","")
    sub = norm(sti.text()) if sti is not None else ""
    head = "%s \u2014 %s" % (title, sub) if sub else title
    body=[]
    for k in art.kids:
        if not isinstance(k,Node): continue
        if ("oj-ti-art" in k.cls()) or ("eli-title" in k.cls()): continue
        render_block(wrap(k), body)
    return head, body

def walk(node, emit, skip_ids):
    for k in node.kids:
        if not isinstance(k,Node): continue
        i=k.attrs.get("id","")
        if "eli-subdivision" in k.cls() and re.match(r"^art_\d+$", i):
            emit("art", k); continue
        if "eli-subdivision" in k.cls() and re.match(r"^(rct|cit)_", i):
            continue
        if k.tag=="p" and "oj-ti-section-1" in k.cls():
            emit("s1", k); continue
        if k.tag=="p" and "oj-ti-section-2" in k.cls():
            emit("s2", k); continue
        if "eli-subdivision" in k.cls() and re.match(r"^anx", i):
            emit("anx", k); continue
        walk(k, emit, skip_ids)

def main(path, out_path, h1, preamble):
    root=parse(path)
    lines=[ "# "+h1, "", preamble.strip(), "" ]
    state={"pend":None}
    def emit(kind, node):
        if kind=="s1":
            state["pend"]=norm(node.text()); return
        if kind=="s2":
            t=norm(node.text())
            lines.append("## " + ((state["pend"]+" \u2014 " + t) if state["pend"] else t)); lines.append("")
            state["pend"]=None; return
        if state["pend"]:
            lines.append("## "+state["pend"]); lines.append(""); state["pend"]=None
        if kind=="art":
            head, body = article_md(node)
            lines.extend(["### "+head, ""]); lines.extend(body); lines.append("")
        elif kind=="anx":
            body=[]; render_block(node, body)
            if body:
                lines.extend(["## Annex", ""]); lines.extend(body); lines.append("")
    walk(root, emit, set())
    txt = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()+"\n"
    open(out_path,"w",encoding="utf-8").write(txt)
    print(out_path, len(txt), "articles:", sum(1 for l in txt.splitlines() if l.startswith("### ")))

if __name__=="__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
