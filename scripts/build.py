#!/usr/bin/env python3
"""Build Job Baer's static research blog from Markdown posts."""

from __future__ import annotations

import html
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "content" / "posts"
DIST = ROOT / "dist"
CSS_SRC = ROOT / "src" / "css" / "style.css"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    meta: dict = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm, body = parts[1], parts[2]
            for line in fm.strip().splitlines():
                if ":" not in line:
                    continue
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip()
                if val.startswith("[") and val.endswith("]"):
                    inner = val[1:-1].strip()
                    meta[key] = [
                        t.strip().strip("\"'")
                        for t in inner.split(",")
                        if t.strip()
                    ]
                elif val.lower() in ("true", "false"):
                    meta[key] = val.lower() == "true"
                else:
                    meta[key] = val.strip("\"'")
    return meta, body.lstrip("\n")


def slug_from_filename(path: Path) -> str:
    name = path.stem
    # drop leading YYYY-MM-DD-
    m = re.match(r"^\d{4}-\d{2}-\d{2}-(.+)$", name)
    return m.group(1) if m else name


def format_date(date_str: str) -> str:
    try:
        d = datetime.strptime(date_str[:10], "%Y-%m-%d")
        return d.strftime("%B %-d, %Y")
    except ValueError:
        try:
            d = datetime.strptime(date_str[:10], "%Y-%m-%d")
            return d.strftime("%B %d, %Y").replace(" 0", " ")
        except ValueError:
            return date_str


def md_inline(text: str) -> str:
    # escape first, then restore intentional markdown transforms
    # Work on raw then escape carefully via placeholders
    parts: list[str] = []
    i = 0
    # code spans
    pattern = re.compile(
        r"`([^`]+)`"
        r"|\*\*(.+?)\*\*"
        r"|\*(.+?)\*"
        r"|_([^_]+)_"
        r"|\[([^\]]+)\]\(([^)]+)\)"
        r"|\*([^*]+)\*"
    )

    def repl(m: re.Match) -> str:
        if m.group(1) is not None:
            return f"<code>{html.escape(m.group(1))}</code>"
        if m.group(2) is not None:
            return f"<strong>{md_inline_simple(m.group(2))}</strong>"
        if m.group(3) is not None:
            return f"<em>{md_inline_simple(m.group(3))}</em>"
        if m.group(4) is not None:
            return f"<em>{md_inline_simple(m.group(4))}</em>"
        if m.group(5) is not None:
            label = html.escape(m.group(5))
            href = html.escape(m.group(6), quote=True)
            return f'<a href="{href}">{label}</a>'
        if m.group(7) is not None:
            return f"<em>{md_inline_simple(m.group(7))}</em>"
        return m.group(0)

    # Simpler sequential approach
    return md_inline_simple(text)


def md_inline_simple(text: str) -> str:
    # Protect code spans
    codes: list[str] = []

    def save_code(m: re.Match) -> str:
        codes.append(f"<code>{html.escape(m.group(1))}</code>")
        return f"\x00C{len(codes)-1}\x00"

    text = re.sub(r"`([^`]+)`", save_code, text)

    links: list[str] = []

    def save_link(m: re.Match) -> str:
        label = m.group(1)
        href = html.escape(m.group(2), quote=True)
        # label may contain bold/italic — process later
        links.append((label, href))
        return f"\x00L{len(links)-1}\x00"

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", save_link, text)

    # Escape remaining HTML-sensitive chars (but not our placeholders)
    out = []
    i = 0
    while i < len(text):
        if text[i] == "\x00":
            j = text.find("\x00", i + 1)
            out.append(text[i : j + 1])
            i = j + 1
        else:
            out.append(html.escape(text[i]))
            i += 1
    text = "".join(out)

    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"(?<![A-Za-z0-9])_([^_]+)_(?![A-Za-z0-9])", r"<em>\1</em>", text)

    # italicized Science journal etc: *Science*
    # already handled

    def restore_link(m: re.Match) -> str:
        idx = int(m.group(1))
        label, href = links[idx]
        # process label inline without re-escaping whole thing
        label_html = md_inline_simple(label) if "\x00" not in label else html.escape(label)
        # avoid recursion issues: label is plain
        label_html = html.escape(label)
        label_html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", label_html)
        return f'<a href="{href}">{label_html}</a>'

    text = re.sub(r"\x00L(\d+)\x00", restore_link, text)
    text = re.sub(r"\x00C(\d+)\x00", lambda m: codes[int(m.group(1))], text)
    return text


def markdown_to_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    in_list: str | None = None  # 'ul' or 'ol'
    para: list[str] = []

    def flush_para() -> None:
        nonlocal para
        if para:
            text = " ".join(para)
            out.append(f"<p>{md_inline_simple(text)}</p>")
            para = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            out.append(f"</{in_list}>")
            in_list = None

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # fenced code
        if stripped.startswith("```"):
            flush_para()
            close_list()
            lang = stripped[3:].strip()
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            code = html.escape("\n".join(code_lines))
            cls = f' class="language-{html.escape(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>{code}</code></pre>")
            i += 1
            continue

        # blank
        if not stripped:
            flush_para()
            close_list()
            i += 1
            continue

        # hr
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", stripped):
            flush_para()
            close_list()
            out.append("<hr>")
            i += 1
            continue

        # headings
        hm = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if hm:
            flush_para()
            close_list()
            level = len(hm.group(1))
            # skip duplicate H1 if same as title (we'll handle in caller by stripping first h1 optionally)
            out.append(f"<h{level}>{md_inline_simple(hm.group(2))}</h{level}>")
            i += 1
            continue

        # blockquote
        if stripped.startswith(">"):
            flush_para()
            close_list()
            qlines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                q = re.sub(r"^>\s?", "", lines[i].strip())
                qlines.append(q)
                i += 1
            # join paragraphs in blockquote
            qhtml = []
            qp: list[str] = []
            for ql in qlines + [""]:
                if ql:
                    qp.append(ql)
                elif qp:
                    qhtml.append(f"<p>{md_inline_simple(' '.join(qp))}</p>")
                    qp = []
            out.append("<blockquote>" + "".join(qhtml) + "</blockquote>")
            continue

        # unordered list
        um = re.match(r"^[-*+]\s+(.+)$", stripped)
        if um:
            flush_para()
            if in_list != "ul":
                close_list()
                out.append("<ul>")
                in_list = "ul"
            out.append(f"<li>{md_inline_simple(um.group(1))}</li>")
            i += 1
            continue

        # ordered list
        om = re.match(r"^(\d+)\.\s+(.+)$", stripped)
        if om:
            flush_para()
            if in_list != "ol":
                close_list()
                out.append("<ol>")
                in_list = "ol"
            out.append(f"<li>{md_inline_simple(om.group(1))}</li>")
            # bug: should use group(2)
            out[-1] = f"<li>{md_inline_simple(om.group(2))}</li>"
            i += 1
            continue

        # paragraph line
        close_list()
        para.append(stripped)
        i += 1

    flush_para()
    close_list()
    return "\n".join(out)


def strip_leading_h1(body_html: str, title: str) -> str:
    """Remove first H1 if it duplicates the page title."""
    # Match first h1
    m = re.match(r"^<h1>(.*?)</h1>\s*", body_html, re.DOTALL)
    if not m:
        return body_html
    # Always strip first H1 on post pages — title is in header
    return body_html[m.end() :]


SITE_NAME = "Job Baer — Research Blog"
SITE_TAGLINE = "Research notes and findings from Job Baer's research assistant."
# Cloudflare Web Analytics token (JS snippet). Put the site token in this file
# (one line, no quotes). Empty/missing = analytics off.
CF_WEB_ANALYTICS_TOKEN_FILE = ROOT / "analytics" / "cf-web-analytics-token.txt"


def cloudflare_web_analytics_snippet() -> str:
    """Return the CF Web Analytics beacon, or empty string if no token."""
    try:
        raw = CF_WEB_ANALYTICS_TOKEN_FILE.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return ""
    # Strip accidental quotes / whitespace; only allow safe token chars
    token = raw.strip().strip('"').strip("'").split()[0] if raw else ""
    if not token or not all(c.isalnum() or c in "-_" for c in token):
        return ""
    # Manual JS snippet install (required for trycloudflare / non-proxied hosts)
    beacon = '{"token": "%s"}' % token
    return (
        "\n  <!-- Cloudflare Web Analytics -->\n"
        "  <script defer src='https://static.cloudflareinsights.com/beacon.min.js' "
        "data-cf-beacon='%s'></script>\n"
        "  <!-- End Cloudflare Web Analytics -->"
    ) % beacon


def layout(
    title: str,
    content: str,
    *,
    active: str = "",
    description: str = "",
    css_href: str = "css/style.css",
) -> str:
    desc = description or SITE_TAGLINE
    nav = [
        ("index.html", "Home", "home"),
        ("blog.html", "Blog", "blog"),
        ("about.html", "About", "about"),
    ]
    nav_html = []
    for href, label, key in nav:
        cur = ' aria-current="page"' if key == active else ""
        nav_html.append(f'<a href="{href}"{cur}>{label}</a>')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{html.escape(desc)}">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{css_href}">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="site-title" href="index.html">Job Baer</a>
      <nav class="site-nav" aria-label="Primary">
        {" ".join(nav_html)}
      </nav>
    </div>
  </header>
  <main id="main" class="site-main">
{content}
  </main>
  <footer class="site-footer">
    <p>Job Baer’s research blog · Posts from a Research assistant · Static site</p>
  </footer>{cloudflare_web_analytics_snippet()}
</body>
</html>
"""


def post_card(post: dict, *, featured: bool = False) -> str:
    badge = ""
    if featured:
        badge = '<p class="post-meta"><strong>Featured</strong> · Latest research</p>'
    elif post.get("placeholder"):
        badge = '<p class="post-meta">Placeholder</p>'
    return f"""
<article class="post-card"{' data-featured="true"' if featured else ""}>
  {badge}
  <h2><a href="posts/{html.escape(post['slug'])}.html">{html.escape(post['title'])}</a></h2>
  <p class="post-meta"><time datetime="{html.escape(post['date'])}">{html.escape(post['date_display'])}</time></p>
  <p class="post-excerpt">{html.escape(post['excerpt'])}</p>
</article>
""".strip()


def load_posts() -> list[dict]:
    posts = []
    for path in sorted(POSTS_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        title = meta.get("title") or path.stem
        date = str(meta.get("date", ""))[:10] or path.stem[:10]
        excerpt = meta.get("excerpt") or ""
        slug = slug_from_filename(path)
        featured = bool(meta.get("featured"))
        # detect placeholder from title/content
        placeholder = "placeholder" in title.lower() or "placeholder" in body[:400].lower()
        body_html = markdown_to_html(body)
        body_html = strip_leading_h1(body_html, title)
        posts.append(
            {
                "title": title,
                "date": date,
                "date_display": format_date(date),
                "excerpt": excerpt,
                "slug": slug,
                "featured": featured,
                "placeholder": placeholder,
                "body_html": body_html,
                "path": path,
            }
        )
    # newest first
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def build() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    (DIST / "posts").mkdir(exist_ok=True)
    (DIST / "css").mkdir(exist_ok=True)

    # copy CSS
    css_dest = DIST / "css" / "style.css"
    css_dest.write_text(CSS_SRC.read_text(encoding="utf-8"), encoding="utf-8")

    posts = load_posts()
    if not posts:
        print("Warning: no posts found in", POSTS_DIR)

    featured = next((p for p in posts if p.get("featured")), posts[0] if posts else None)

    # --- Home ---
    cards = []
    if featured:
        cards.append(post_card(featured, featured=True))
    for p in posts:
        if featured and p["slug"] == featured["slug"]:
            continue
        cards.append(post_card(p))

    home_content = f"""
    <header class="page-header">
      <h1>Research Blog</h1>
      <p class="lede">{html.escape(SITE_TAGLINE)}</p>
    </header>
    <section aria-label="Posts">
      <ul class="post-list">
        {"".join(f"<li>{c}</li>" for c in cards)}
      </ul>
    </section>
"""
    (DIST / "index.html").write_text(
        layout("Home · " + SITE_NAME, home_content, active="home"),
        encoding="utf-8",
    )

    # --- Blog (same list, different chrome) ---
    blog_content = f"""
    <header class="page-header">
      <h1>All posts</h1>
      <p class="lede">Newest first. Featured research appears at the top.</p>
    </header>
    <section aria-label="All blog posts">
      <ul class="post-list">
        {"".join(f"<li>{c}</li>" for c in cards)}
      </ul>
    </section>
"""
    (DIST / "blog.html").write_text(
        layout("Blog · " + SITE_NAME, blog_content, active="blog"),
        encoding="utf-8",
    )

    # --- About ---
    about_content = """
    <header class="page-header">
      <h1>About</h1>
      <p class="lede">What this blog is and how posts get here.</p>
    </header>
    <div class="about-card prose">
      <p>This is <strong>Job Baer’s research blog</strong> — a place for clear write-ups of research threads, findings, and notes worth keeping.</p>
      <p>Posts are produced by a <strong>Research assistant</strong> and published here as static pages. The goal is a fast, accessible archive you can read on any device without accounts or apps.</p>
      <p>New posts start as Markdown files in the <code>content/posts</code> folder. A small build script turns those files into HTML. No database, no CMS — just files.</p>
      <p>Two early posts are marked as placeholders for layout. Newer research posts (when available) appear as featured on the home page.</p>
    </div>
"""
    (DIST / "about.html").write_text(
        layout(
            "About · " + SITE_NAME,
            about_content,
            active="about",
            description="About Job Baer's research blog.",
        ),
        encoding="utf-8",
    )

    # --- Individual posts ---
    for p in posts:
        # fix nav links from posts/ subdirectory
        post_body = f"""
    <article>
      <header class="article-header">
        <h1>{html.escape(p['title'])}</h1>
        <p class="post-meta"><time datetime="{html.escape(p['date'])}">{html.escape(p['date_display'])}</time>
        {" · Featured research" if p.get("featured") else ""}
        {" · Placeholder" if p.get("placeholder") and not p.get("featured") else ""}</p>
      </header>
      <div class="prose">
{p['body_html']}
      </div>
      <p class="back-link"><a href="../blog.html">← All posts</a></p>
    </article>
"""
        page = layout(
            f"{p['title']} · Job Baer",
            post_body,
            active="blog",
            description=p["excerpt"] or SITE_TAGLINE,
            css_href="../css/style.css",
        )
        # fix nav hrefs for subdirectory
        page = page.replace('href="index.html"', 'href="../index.html"')
        page = page.replace('href="blog.html"', 'href="../blog.html"')
        page = page.replace('href="about.html"', 'href="../about.html"')
        # site title link
        page = page.replace(
            '<a class="site-title" href="index.html">',
            '<a class="site-title" href="../index.html">',
        )
        # already replaced index — good. But we double-replaced? Let's check:
        # First replace href="index.html" -> ../index.html, including site-title.
        # Then the site-title specific replace won't match. OK.

        (DIST / "posts" / f"{p['slug']}.html").write_text(page, encoding="utf-8")

    print(f"Built {len(posts)} post(s) → {DIST}")
    for p in posts:
        flag = " [featured]" if p.get("featured") else (" [placeholder]" if p.get("placeholder") else "")
        print(f"  - {p['date']} {p['title'][:70]}{flag}")


if __name__ == "__main__":
    build()
