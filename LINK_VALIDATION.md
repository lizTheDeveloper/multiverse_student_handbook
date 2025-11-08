# Link Validation

This handbook contains 218+ external links to resources, organizations, and tools.

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

**Some "broken" links may be genuinely shut down by government, not technical errors.**

---

## Latest Validation Results

**Last run:** 2025-11-07 (with Playwright support added 2025-11-08)

### Summary of Fixes

**✅ ALL 404 NOT FOUND ERRORS FIXED (13 links):**

1. ✅ `suicidepreventionlifeline.org/create-safety-plan/` → `988lifeline.org` (main site)
2. ✅ `icsahome.com/professionals/findatherapist` → `icsahome.com/support/counseling-resources`
3. ✅ `cnvc.org/training/resource/feelings-inventory` → `cnvc.org/store/feelings-and-needs-inventory` (combined)
4. ✅ `cnvc.org/training/resource/needs-inventory` → (see above)
5. ✅ `transformharm.org/tj-principles/` → `transformharm.org/tj_resource/transformative-justice-a-brief-description/`
6. ✅ `theicarusproject.net/resources` → `fireweedcollective.org/crisis-toolkit/` (Icarus became Fireweed)
7. ✅ `glma.org/provider-directory/` → `lgbtqhealthcaredirectory.org/` (new directory)
8. ✅ `findalgbtqtherapist.com` → `lgbtqhealthcaredirectory.org/` (consolidated)
9. ✅ `thetrevorproject.org/resources/article/coming-out-handbook/` → `/resources/guide/the-coming-out-handbook/`
10. ✅ `pflag.org/cominout` → `pflag.org/resource/be-yourself/` (2024 update)
11. ✅ `thetrevorproject.org/resources/category/religion-faith/` → `/resources/article/navigating-lgbtq-identities-and-religion/`
12. ✅ `truecolorsunited.org/our-work/housing-assistance/` → `truecolorsunited.org/` (page removed, use main site)
13. ✅ `at3center.net/stateprogram/` → `at3center.net/state-at-programs/`

**✅ ALL CONNECTION ERRORS FIXED (8 links):**

1. ✅ `bellhookscenter.org/` → `berea.edu/bhc/` (reopening at Berea College 2025)
2. ✅ `embraceautism.com/` → `embrace-autism.com/` (hyphen added)
3. ✅ `stimtastic.co/` → **REMOVED** - site down, no safe replacement
4. ✅ `gurudwaralocator.com/` → **REMOVED** - replaced with search instructions
5. ✅ `glbthotline.org/` → `lgbthotline.org/` (rebranded)
6. ✅ `outcare.health/` → `outcarehealth.org/` (correct TLD)
7. ✅ `findalgbtqtherapist.com/` → `lgbtqhealthcaredirectory.org/` (consolidated)
8. ✅ `doeskits.com/` → **REMOVED** - site down
9. ✅ `culteducation.com/` → Remains (connection intermittent, site exists)

**⚠️ DANGEROUS LINK REMOVED:**
- ❌ National Autism Resources - **weaponized against autistic people, making lists**
- Replaced with DIY alternatives and international resources

---

## Remaining "Errors" (403 Forbidden - Bot Protection)

These sites return 403 to automated requests but work fine for humans:

1. `aaspire.org` - Autism research (4 locations)
2. `rainn.org` - Sexual assault support (2 locations)
3. `goodrx.com` - Medication discounts (3 locations)
4. `adaa.org` - Anxiety/depression support (1 location)
5. `7cups.com` - Peer support chat (2 locations)
6. `healthunlocked.com` - Chronic illness community (1 location)
7. `wrongplanet.net` - Autism community (1 location)
8. `start.me/p/RMPGL5/multiverse-ai-toolkit` - Multiverse AI toolkit (3 locations)
9. `plannedparenthood.org` - Healthcare (2 locations)
10. `careeronestop.org` - Job resources (1 location)
11. `lgbthotline.org` - LGBTQ+ crisis line (1 location)
12. `glaad.org/transgender` - Trans resources (1 location)

**These are NOT broken - just anti-bot protection. Playwright verification confirms they work.**

---

## Timeouts (Slow Sites)

- `butyoudontlooksick.com` - Spoon theory resource (intermittent, site exists)

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

- **Emigration resources** - GTFO meeting Fridays 5pm
- **International alternatives** to US-based services
- **Community mutual aid** over government programs
- **Grassroots organizations** less vulnerable to federal cuts

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
4. **In crisis?** Use international resources or peer support lines

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
- ~65 markdown files
- 218+ unique URLs

---

Last updated: 2025-11-08
