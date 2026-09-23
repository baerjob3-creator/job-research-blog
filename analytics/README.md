# Cloudflare Web Analytics

For the stable GitHub Pages site.

1. Open https://dash.cloudflare.com/ → **Analytics & Logs** → **Web Analytics**
2. **Add a site** with hostname: `baerjob3-creator.github.io`
   (GitHub Pages project site lives under that host)
3. Choose **Enable with JS Snippet installation** (manual) — not automatic injection
4. Copy the **token** from the JS snippet (`data-cf-beacon='{"token":"..."}'`)
5. Paste the token alone into `cf-web-analytics-token.txt` (one line, no quotes)
6. Rebuild: `python3 scripts/build.py` then sync `dist/` → `docs/` and push so Pages serves the beacon

Public site: https://baerjob3-creator.github.io/job-research-blog/

Dashboard: Cloudflare → Web Analytics → select this site.
