# Student Handbook — Stale Content Audit

Swept 2026-08-25 using the same checks as the school-site audit
(`themultiverse.school/scripts/roster.py`).

---

## P0 — Students see wrong instructions right now

### 1. "Learn to Code" standup is retired — README tells students to join it

**README.md:14**
```
Come to "Learn to Code" stand-up — 9am daily
```

"Learn to Code Standup" was renamed to "Make and Do" (Neek's class). The standup
students actually join is **Founding Federation** with Spencer and Neek, Mon–Thu
9 AM (not daily). This is the first thing a new student reads.

**README.md:60**
```
Daily stand-up (9am)
```

Same issue — says "daily" (implies Mon–Sun), actual schedule is Mon–Thu.

**Fix:** Replace with current program name and correct days. Example:
`Come to Founding Federation standup — Mon–Thu, 9 AM Pacific`

---

### 2. "so Liz can follow you" — README step 1

**README.md:11**
```
Add your contact info & social media so Liz can follow you
```

Liz is no longer the person onboarding students day-to-day. This should name
whoever actually follows new sign-ups, or just say "so the team can welcome you."

---

### 3. Six dead Obsidian links

**README.md:13, 29, 30, 39, 58, 63** — all point to:
```
https://publish.obsidian.md/multiversecurriculum/Curriculum/Interactive+Tutors/1+-+Start+Here
```

The Obsidian-published curriculum vault is gone (Quartz was retired and Obsidian
Publish was decommissioned). These links 404. The Interactive AI Tutors now live
on the school site under `/curriculum/…`. Every "Start Here" link in the README
is broken.

**Fix:** Replace with the current curriculum URL on themultiverse.school.

---

## P1 — Wrong but less immediate

### 4. GTFO Meeting — "Fridays 5pm" may be stale

**README.md:116**, **emigration-resources.md:40, 204, 330, 440**,
**LINK_VALIDATION.md:130**

The GTFO meeting was announced in November 2025. If it's still running at the
same time, no fix needed. If it has moved, stopped, or changed cadence, five
places need updating. Worth confirming with Megs or Nico.

---

### 5. "November 2025" context sections

**self-awareness.md:11**, **common-misunderstandings.md:109**,
**recognizing-dependency.md:11, 104**, **README.md:115**,
**GETTING_STARTED.md:180**, **README.md:179**

The handbook was written in November 2025 and several sections frame themselves
as "November 2025: Crisis Changes the Calculus." Nine months later, the crisis
context is still relevant but the date-stamp makes the handbook feel
unmaintained. Consider removing the month or generalizing to "current political
context."

**README.md:179** also says "Last Updated: November 2025" — that's now 9 months
stale.

---

### 6. Liz as operational contact — 12 places in mentoring-guidelines

**mentoring-guidelines.md:40, 71, 106, 205, 218, 254, 334, 350, 358**,
**cohabitation-policy.md:155**, **multiverse-code-of-conduct.md:190**,
**healthy-vs-unhealthy-communities.md:229, 241, 357**,
**how-multiverse-works.md:111, 299, 411**

Liz is referenced as the person to "notify," "alert," "coordinate with," "talk
to," and "report to" throughout the mentoring and policy docs. Some of these
(founder attribution in how-multiverse-works) are accurate historical statements.
But the operational ones ("Notify Liz immediately," "Alert Liz," "Coordinate with
Liz first") route students and mentors to the wrong person if Liz is no longer
the day-to-day program coordinator.

**Fix options:**
- Replace "Liz" with "the program coordinator" or "staff" in operational
  instructions, and leave founder attribution as-is.
- Or replace with the current coordinator's name if there is one.

---

### 7. Luma link — may be stale

**README.md:116**, **emigration-resources.md:42**
```
luma.com/MultiverseSchool
```

If the Multiverse School Luma page is still active for the GTFO meeting, fine.
If Luma is no longer used for event sign-ups, this link is dead. Worth checking.

---

## P2 — Structural / low-severity

### 8. "Version 1.0 | Last Updated: November 2025"

**README.md:179**, **GETTING_STARTED.md:178-180**

Not wrong per se, but signals the handbook hasn't been touched in 9 months. If
updates are made from this audit, bump the date.

---

### 9. multiverse.school vs themultiverse.school

**README.md:11**
```
https://multiverse.school/dashboard
```

The canonical domain is `themultiverse.school`. If `multiverse.school` redirects,
this is fine but inconsistent. If it doesn't, it's a broken link.

---

### 10. Code of Conduct quote attributes to "the instructor (Liz)"

**multiverse-code-of-conduct.md:190**
```
From the instructor (Liz):
"I have expelled 9 paying students over the years."
```

This is a historical quote and attribution is correct. Flagging only because if
the handbook is updated to remove Liz as operational contact elsewhere, this
should stay — it's a direct quote, not a routing instruction.

---

## Summary

| Severity | Count | Category |
|----------|-------|----------|
| P0       | 3     | Broken links (Obsidian), retired program name, wrong contact |
| P1       | 4     | Stale dates, Liz as operational contact, GTFO meeting status |
| P2       | 3     | Version stamp, domain inconsistency, historical quote |

**What the handbook does NOT have (good news):**
- No stale schedule times (no "10–11 AM" or "Mon–Wed" errors)
- No retired instructor names (Jordan, Toni, Francina, Mea)
- No "Shipping Software" references
- No Gather Town references
- No references to Spencer, Neek, Lajoie, or Sandra (the handbook predates them)
- The mentoring and policy content is structurally sound — just routes to Liz
  instead of the current coordinator

**The biggest student-facing issue is the README.** It's the first thing a new
student reads, and it tells them to join a class that doesn't exist anymore
("Learn to Code stand-up"), says it runs daily (it's Mon–Thu), sends them to
six dead Obsidian links, and names Liz as the person who will follow them.
