# Link Validation

This handbook contains 228 unique external links to resources, organizations, and tools.

## Running the Validation Script

```bash
python3 validate_links.py
```

The script will:
- Scan all markdown files for links
- Check each URL to verify it's accessible
- Retry 403 errors with Playwright (bypasses bot detection)
- Report broken links vs bot-protected links
- Distinguish between genuinely down sites vs anti-bot measures

**Note:** Playwright is required for full validation. Install with:
```bash
pip3 install playwright --break-system-packages
python3 -m playwright install chromium
```

## Context: November 2025

**Political situation affecting resources:**
- Fascist takeover of United States government
- Government shutdowns eliminating services
- Federal funding cuts ("Big Beautiful Bill")
- 988 LGBTQ+ youth services shut down (July 2025)
- National Autism Resources weaponized (making lists)
- Targeting of LGBTQ+ people and minorities
- **International mail to US shut down** (Trump tariffs broke international mail agreements)
- **Information heavily manipulated** (can't find protests on Google, feeds controlled)

**Some "broken" links may be genuinely shut down by government, not technical errors.**

**Mail shutdown affects:**
- DIY HRT shipments from international suppliers (not arriving)
- International medication orders
- Any physical resources that require shipping to US

**Information manipulation affects:**
- Finding resources through search
- Social media algorithms hiding organizing
- Need for VPN, encrypted communication, peer networks

---

## Latest Validation Results

**Last run:** 2026-09-29 · 77 markdown files · 228 unique URLs · 198 OK on the first request

The 30 that failed the first request break down as follows. The Playwright re-check could not run in the environment used for this pass, so 403s were re-checked with a browser user agent and the response headers instead.

### Genuinely broken (needs a fix)

| Link | Result | Where |
|---|---|---|
| `lib.berkeley.edu/goldman` | 404 (Emma Goldman Papers page moved) | `part7/liberatory-resources.md`, `part7/thinker-goldman.md` |
| `lgbtcenters.org/LGBTCenters` | Redirects to `lgbtqcenters.org`, then 404. The homepage `lgbtqcenters.org` works. | `part7/survival-resources.md`, `part7/lgbtq-resources.md` |

**Fixed since the run:** the `themultiverse.school/x/` and `/tools/` links (7 in total) pointed at index pages that don't exist (404 whether or not you're logged in). They now point to the path dashboard at `themultiverse.school/paths`, which links each student's tools and class companions. Individual tools under `/tools/<name>` need a login, and redirect to it.

### Bot protection (403 to automated requests; not broken)

Cloudflare or similar challenges automated requests to these; they load for people:

`findhelp.org` (9 locations), `rainn.org`, `goodrx.com`, `7cups.com`, `adaa.org`, `emdria.org`, `coachingfederation.org`, `dyslexiaida.org`, `womenslaw.org`, `lgbthotline.org`, `nfb.org`, `perkins.org`, the Ginwright article on `medium.com`

These returned 403 to the script but **200 with a browser user agent**, so they're fine: `plannedparenthood.org`, `careeronestop.org`, `glaad.org/transgender`, `healthunlocked.com`, `nationaleatingdisorders.org`

### Inconclusive (check by hand)

- `freedomofmind.com` (both links) — the TLS certificate didn't match the host name. That is either a problem with the site or with the network used for this pass.
- `hrtcafe.net` — the network used for this pass refused the connection, so nothing is known about the site itself.
- `modestneeds.org`, `butyoudontlooksick.com` (both links) — timed out. `butyoudontlooksick.com` also timed out in the 2025 run.

### False positive

- `tr.ee/kqykEpLW34` (`part7/emigration-resources.md`) — the script's bare-URL pattern misreads a link whose text is itself a URL. The link works (it redirects to the Nope Brigade linktree).

---

## Previous run (2025-11-07)

**✅ 404 errors fixed (13 links):** `suicidepreventionlifeline.org` safety plan → `988lifeline.org`; ICSA therapist finder; CNVC feelings and needs inventories; transformharm.org TJ principles; Icarus Project → Fireweed Collective; GLMA directory and findalgbtqtherapist.com → `lgbtqhealthcaredirectory.org`; two Trevor Project pages; PFLAG coming out; True Colors United; AT3 Center state programs.

**✅ Connection errors fixed (8 links):** bell hooks center → `berea.edu/bhc/`; `embrace-autism.com`; `lgbthotline.org`; `outcarehealth.org`; `lgbtqhealthcaredirectory.org`; stimtastic.co, gurudwaralocator.com and doeskits.com removed.

**⚠️ Dangerous link removed:** National Autism Resources (weaponized against autistic people, making lists).

---

## Maintaining Links

### When adding new links:

1. **Test manually first**
2. **Run validation script after updates**
3. **Prefer international resources** (less vulnerable to US government takedowns)
4. **Prefer community-based orgs** over government-funded resources
5. **Avoid organizations weaponized against minorities**
6. **Include archive.org links as backups** for critical resources

### Current priorities:

- **Emigration resources** - visas, leaving the US
- **International alternatives** to US-based services
- **Community mutual aid** over government programs
- **Grassroots organizations** less vulnerable to federal cuts
- **Peer warmlines** as alternatives to government crisis lines
- **Local, in-person organizing** (feeds are manipulated)
- **DIY/mutual aid networks** that don't rely on international shipping
- **Thailand trans healthcare** as best emigration destination for trans people

---

## Safety Notes

**Resources to avoid (Nov 2025):**
- ❌ National Autism Resources (making lists of autistic people)
- ⚠️ Government-funded hotlines (vulnerable to shutdown)
- ⚠️ Federal healthcare programs (being eliminated)

**Recommended:**
- ✅ International resources
- ✅ Peer-run/mutual aid organizations
- ✅ Community-based support (less reliant on government)
- ✅ DIY alternatives
- ✅ Grassroots networks

---

## For Students: What This Means

If you see a "broken link" error in this handbook:
1. **The site might be genuinely down** (government shutdown, funding cuts)
2. **It might be bot-protected** (works fine when you visit)
3. **Report it** so we can find alternatives
4. **In crisis?** Use international resources or peer support lines (Wildflower Alliance: 888-407-4515)

**Information is being manipulated:**
- Can't find protests or organizing on Google
- Social media feeds are controlled
- Use VPN for research
- Trust peer networks over official channels
- Verify through international sources
- Use encrypted communication (Signal)

**International mail is shut down:**
- DIY HRT from international suppliers not arriving reliably
- Prioritize leaving the US or local healthcare
- Stockpile while you can
- See emigration resources

**Your safety comes first. Learning can wait.**

---

## Technical Details

### Validation Process:
1. Extract all URLs from markdown files
2. Check with `requests` library (HTTP HEAD/GET)
3. If 403 error → retry with Playwright (real browser)
4. Categorize: Working | Bot-protected | Genuinely broken
5. Report results with political context

### Exit Codes:
- `0` - All links working or bot-protected only
- `1` - Genuinely broken links found

### Files Scanned:
- All `.md` files in handbook directory (recursive)
- 77 markdown files
- 228 unique URLs

---

Last updated: 2026-09-29
