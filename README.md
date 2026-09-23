# Job Baer — Research Blog

A simple, static research blog for Job Baer. Posts are written in Markdown and built to plain HTML/CSS (no JavaScript required to read).

## Site location

- **Source:** `/workspace/job-blog`
- **Built site (serve this):** `/workspace/job-blog/dist`

## Preview

If a local server is already running (see below), open:

```
http://127.0.0.1:8080/
```

Or serve the built site yourself:

```bash
cd /workspace/job-blog/dist
python3 -m http.server 8080
```

Then open `http://127.0.0.1:8080/` in a browser.

You can also open `dist/index.html` directly as a file, but using the HTTP server is preferred (correct relative URLs and no browser quirks).

## Rebuild after editing posts

```bash
python3 /workspace/job-blog/scripts/build.py
```

Output goes to `dist/`. No extra Python packages are required.

## Add a new post

1. Create a Markdown file in `content/posts/` named like:

   ```
   YYYY-MM-DD-short-slug.md
   ```

   Example: `2026-09-21-my-new-finding.md`

2. Start with YAML front matter:

   ```markdown
   ---
   title: "Your post title"
   date: 2026-09-21
   excerpt: "One or two sentences for the home/blog list."
   featured: false
   ---

   # Your post title

   Your content here. Supports headings, lists, **bold**, *italic*,
   `code`, links, and blockquotes.
   ```

3. Set `featured: true` if this should appear as the featured/latest post on Home and Blog (only one featured post is highlighted; newest still sorts first).

4. Rebuild:

   ```bash
   python3 /workspace/job-blog/scripts/build.py
   ```

5. Refresh the browser.

## Pages

| Page | File |
|------|------|
| Home (post list) | `dist/index.html` |
| Blog (all posts) | `dist/blog.html` |
| About | `dist/about.html` |
| Individual posts | `dist/posts/*.html` |

## Design notes

- Semantic HTML, skip link, visible focus styles
- Readable typography, strong contrast
- Mobile-friendly layout
- Respects `prefers-color-scheme` (light/dark)

## Project layout

```
job-blog/
├── content/posts/     # Markdown source posts
├── src/css/style.css  # Stylesheet
├── scripts/build.py   # Markdown → static HTML
├── dist/              # Generated site (serve this)
└── README.md
```
