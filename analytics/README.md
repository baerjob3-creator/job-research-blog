# Cloudflare Web Analytics

1. Open https://dash.cloudflare.com/ → **Analytics & Logs** → **Web Analytics**
2. **Add a site** with hostname: `bars-bigger-returned-musicians.trycloudflare.com`
   (update later if the public URL changes)
3. Choose **Enable with JS Snippet installation** (manual) — not automatic injection
4. Copy the **token** from the JS snippet (`data-cf-beacon='{"token":"..."}'`)
5. Paste the token alone into `cf-web-analytics-token.txt` (one line, no quotes)
6. Rebuild: `python3 scripts/build.py`

Dashboard: Cloudflare → Web Analytics → select this site.
