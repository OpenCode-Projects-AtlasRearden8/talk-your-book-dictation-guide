import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
PAGES = SITE / "pages"

CHAPTERS = [
    ("index.md", "docs-index.html", "Docs Index"),
    ("00-introduction.md", "01-introduction.html", "Introduction"),
    ("01-free-dictation-by-platform.md", "02-free-dictation.html", "Free Dictation on Every Device"),
    ("02-transcription-endpoints.md", "03-transcription-endpoints.html", "OpenAI-Compatible & Local Transcription Endpoints"),
    ("03-punctuation-control.md", "04-punctuation-control.html", "Punctuation Control Tricks"),
    ("04-sculpting-drafts.md", "05-sculpting-drafts.html", "Sculpting Spoken Drafts into Readable Prose"),
    ("05-privacy.md", "06-privacy.html", "Protecting Manuscript Privacy"),
    ("06-30-day-word-flow-plan.md", "07-word-flow-trial.html", "The 30-Day Word-Flow Trial Plan"),
]

BY_DOC = {doc: (page, title) for doc, page, title in CHAPTERS}
HOME = "./pages/01-introduction.html"


def slug(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.ASCII)
    return re.sub(r"[\s_-]+", "-", text).strip("-").lower()


def inline(text: str) -> str:
    out = html.escape(text, quote=False)
    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", replace_link, out)
    out = re.sub(r"(\*\*)(.+?)\1", r"<strong>\2</strong>", out)
    out = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", out)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    return out


def replace_link(m: re.Match) -> str:
    label, target = m.group(1), m.group(2)
    if target.endswith(".md"):
        if target not in BY_DOC:
            raise ValueError(f"unknown docs link target: {target}")
        target = "./pages/" + BY_DOC[target][0]
    elif not (target.startswith("http") or target.startswith("#")):
        raise ValueError(f"unexpected link target in docs: {target}")
    return f"<a href='{target}'>{label}</a>"


def to_html(md: str) -> str:
    lines = md.splitlines()
    out = []
    in_code = in_list = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append("</code></pre>" if in_code else "<pre><code>")
            in_code = not in_code
            i += 1
            continue
        if in_code:
            out.append(line)
            i += 1
            continue
        if not line.strip():
            if in_list:
                out.append("</ul>")
                in_list = False
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.+)$", line)
        if m:
            if in_list:
                out.append("</ul>")
                in_list = False
            level, content = len(m.group(1)), inline(m.group(2).strip())
            out.append(f"<h{level} id='{slug(content)}'>{content}</h{level}>")
            i += 1
            continue
        m = re.match(r"^\s*-\s+\[([ x])\]\s+(.*)$", line)
        if m:
            if not in_list:
                out.append("<ul>")
                in_list = True
            box = "&#9745;" if m.group(1) == "x" else "&#9744;"
            out.append(f"<li>{box} {inline(m.group(2))}</li>")
            i += 1
            continue
        m = re.match(r"^\s*-\s+(.*)$", line)
        if m:
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(m.group(1))}</li>")
            i += 1
            continue
        if line.startswith(">"):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<blockquote><p>{inline(line.lstrip('> ').strip())}</p></blockquote>")
            i += 1
            continue
        if re.match(r"^\s\|\??", line) or line.lstrip().startswith("|"):
            if in_list:
                out.append("</ul>")
                in_list = False
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not re.match(r"^[\s:-]+$", "".join(cells)):
                    rows.append(cells)
                i += 1
            out.append(mk_table(rows))
            continue
        block = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^\s*(-|#{1,4}\s|```|>|\|)", lines[i]):
            block.append(lines[i])
            i += 1
        out.append(f"<p>{inline(' '.join(block))}</p>")
    if in_list:
        out.append("</ul>")
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def mk_table(rows: list) -> str:
    if not rows:
        return ""
    head = "<tr>" + "".join(f"<th>{inline(c)}</th>" for c in rows[0]) + "</tr>"
    body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
    return f"<table>{head}{body}</table>"


def nav_html(current: str) -> str:
    parts = []
    for doc, page, title in CHAPTERS:
        cls = " class=\"active\"" if doc == current else ""
        parts.append(f"<a href='./pages/{page}'{cls}>{title}</a>")
    return "\n".join(parts)


def nav_html(current: str, prefix: str) -> str:
    parts = []
    for doc, page, title in CHAPTERS:
        cls = " class=\"active\"" if doc == current else ""
        href = f"{prefix}index.html" if doc == "index.md" else f"{prefix}pages/{page}"
        parts.append(f"<a href='{href}'{cls}>{html.escape(title)}</a>")
    return "\n".join(parts)


def prevnext(current: str, prefix: str) -> str:
    i = [c[0] for c in CHAPTERS].index(current)
    parts = []
    if i > 0:
        prev = CHAPTERS[i - 1]
        prev_href = f"{prefix}index.html" if prev[0] == "index.md" else f"{prefix}pages/{prev[1]}"
        parts.append(f"&larr; <a href='{prev_href}'>{html.escape(prev[2])}</a>")
    if i < len(CHAPTERS) - 1:
        nxt = CHAPTERS[i + 1]
        parts.append(f"<a href='{prefix}pages/{nxt[1]}'>{html.escape(nxt[2])}</a> &rarr;")
    return " &nbsp;·&nbsp; ".join(parts) if parts else ""


def render(doc: str) -> str:
    _, title = BY_DOC[doc]
    md = (DOCS / doc).read_text(encoding="utf-8")
    md = re.sub(r"^# .*\n", "", md, count=1)
    prefix = "" if doc == "index.md" else "../"
    css_href = "style.css" if doc == "index.md" else "../style.css"
    brand_href = "index.html" if doc == "index.md" else "../index.html"
    body_md = re.sub(r"^\| Path \|.*?\n\n", "", md, count=1, flags=re.S) if doc == "index.md" else md
    return SHELL.format(title=html.escape(title), cssHref=css_href, brandHref=brand_href,
                        nav=nav_html(doc, prefix), body=to_html(body_md),
                        prevnext=prevnext(doc, prefix))


SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Talk Your Book</title>
<link rel="stylesheet" href="{cssHref}">
</head>
<body>
<header>
  <a class="brand" href="{brandHref}">Talk Your Book</a>
  <span class="tagline">A voice dictation manual for authors · Asdale Dynamics, LLC</span>
</header>
<div class="wrap">
<nav>
<h2>Contents</h2>
{nav}
</nav>
<main id="top">
{body}
<p class="prevnext">{prevnext}</p>
<footer>MIT License · Copyright (c) 2026 Asdale Dynamics, LLC · This site is generated offline from docs by <code>site/gen.py</code>. No tracking, no keys, no cloud.</footer>
</main>
</div>
</body>
</html>
"""


def css() -> str:
    return """
:root { --bg:#f7f4ed; --ink:#25211a; --muted:#6d655a; --accent:#2f6f4f; --card:#fffdf8; --line:#ddd6c5; }
* { box-sizing:border-box; }
body { margin:0; font:17px/1.65 Georgia, 'Times New Roman', serif; background:var(--bg); color:var(--ink); }
header { padding:1.1rem 2rem; border-bottom:3px solid var(--accent); background:var(--card); display:flex; flex-wrap:wrap; gap:.3rem 1.2rem; align-items:baseline; }
.brand { font-weight:700; font-size:1.35rem; color:var(--ink); text-decoration:none; }
.tagline { color:var(--muted); font-size:.85rem; }
.wrap { display:grid; grid-template-columns:17rem minmax(0,1fr); gap:2.5rem; max-width:75rem; margin:0 auto; padding:2rem 2rem 4rem; }
nav { position:sticky; top:1.5rem; align-self:start; font-size:.95rem; background:var(--card); border:1px solid var(--line); border-radius:10px; padding:1rem .4rem; }
nav h2 { font-size:.75rem; text-transform:uppercase; letter-spacing:.08em; color:var(--muted); margin:.2rem .8rem .5rem; }
nav a { display:block; padding:.35rem .8rem; color:var(--ink); text-decoration:none; border-left:3px solid transparent; }
nav a:hover { color:var(--accent); }
nav a.active { border-left-color:var(--accent); font-weight:700; }
main { max-width:46rem; }
h1,h2,h3 { line-height:1.25; }
h1 { font-size:1.9rem; margin-top:0; }
em { font-style:italic; }
code { background:#ece8dc; padding:.08rem .35rem; border-radius:4px; font-size:.88em; font-family:ui-monospace, Consolas, monospace; }
pre { background:#2c2a23; color:#f2efe5; padding:1rem 1.2rem; border-radius:8px; overflow:auto; }
pre code { background:none; color:inherit; padding:0; }
blockquote { margin:1.1rem 0; padding:.5rem 1.2rem; border-left:4px solid var(--accent); background:var(--card); font-style:italic; }
table { border-collapse:collapse; width:100%; margin:1.1rem 0; font-size:.93rem; background:var(--card); }
th, td { border:1px solid var(--line); padding:.45rem .7rem; text-align:left; vertical-align:top; }
th { background:#ece8dc; }
li { margin:.3rem 0; }
.prevnext { margin-top:2.5rem; padding-top:1rem; border-top:1px solid var(--line); display:flex; justify-content:space-between; gap:1rem; flex-wrap:wrap; }
footer { margin-top:2.5rem; font-size:.8rem; color:var(--muted); border-top:1px solid var(--line); padding-top:1rem; }
@media (max-width:720px) { .wrap { grid-template-columns:1fr; padding:1.2rem 1rem 3rem; } nav { position:static; } }
"""


def build():
    if PAGES.exists():
        shutil.rmtree(PAGES)
    PAGES.mkdir(parents=True)
    (SITE / "style.css").write_text(css(), encoding="utf-8")
    pages_html = {doc: render(doc) for doc, _, _ in CHAPTERS}
    for doc, page, _ in CHAPTERS:
        if doc == "index.md":
            continue
        (PAGES / page).write_text(pages_html[doc], encoding="utf-8")
    (SITE / "index.html").write_text(pages_html["index.md"], encoding="utf-8")
    print(f"built {len(CHAPTERS) - 1} chapter pages into {PAGES} plus site/index.html")


def verify() -> list:
    problems = []
    for doc, _, _ in CHAPTERS:
        if not (DOCS / doc).exists():
            problems.append(f"docs/{doc} missing")
    for p in list(SITE.rglob("*.html")) + [SITE / "style.css"]:
        if not p.is_file():
            problems.append(f"{p} missing")
    for p in SITE.rglob("*.html"):
        text = p.read_text(encoding="utf-8")
        for link in re.findall(r"href=[\"']([^\"']+)[\"']", text):
            if link.startswith("#"):
                continue
            if link.startswith("http"):
                continue
            target = (p.parent / link.split("#")[0]).resolve()
            if not target.exists():
                problems.append(f"{p.relative_to(SITE)}: broken link {link}")
        if "Copyright (c) 2026 Asdale Dynamics, LLC" not in text:
            problems.append(f"{p.relative_to(SITE)}: missing copyright footer")
    return problems


if __name__ == "__main__":
    build()
    problems = verify()
    if problems:
        for p in problems:
            print("PROBLEM:", p)
        raise SystemExit(1)
    print("verify: 0 broken links, all pages present")
