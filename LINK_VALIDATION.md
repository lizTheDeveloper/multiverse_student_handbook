# Link Validation

This handbook contains 218 external links to resources, organizations, and tools.

## Running the Validation Script

```bash
python3 validate_links.py
```

The script will:
- Scan all markdown files for links
- Check each URL to verify it's accessible
- Report any broken links with their locations

## Latest Validation Results

**Last run:** 2025-11-07

- **Total URLs:** 218
- **Working:** 184 (84%)
- **Broken:** 34 (16%)

### Types of Issues

1. **403 Forbidden (11 links)** - Sites blocking automated requests
   - These often work fine when accessed manually
   - Examples: aaspire.org, rainn.org, goodrx.com, plannedparenthood.org

2. **404 Not Found (13 links)** - Pages that have moved or been removed
   - These need to be updated or replaced
   - Examples: suicide prevention safety plan, ICSA therapist finder, CNVC inventories

3. **Connection Error (8 links)** - Sites down or blocking requests
   - Examples: bellhookscenter.org, embraceautism.com, stimtastic.co

4. **Timeout (2 links)** - Sites too slow to respond
   - Examples: butyoudontlooksick.com

### Critical Links to Fix

The following 404 errors should be addressed:

1. `suicidepreventionlifeline.org/create-safety-plan/` - Find updated safety plan URL
2. `icsahome.com/professionals/findatherapist` - Update ICSA therapist directory link
3. `cnvc.org/training/resource/feelings-inventory` - Find new CNVC feelings list
4. `cnvc.org/training/resource/needs-inventory` - Find new CNVC needs list
5. `transformharm.org/tj_resource/transformative-justice-a-brief-description/` - Update transformative justice link
6. `fireweedcollective.org/crisis-toolkit/` - Icarus Project resources
7. `lgbtqhealthcaredirectory.org/` - Update LGBTQ+ provider directory
8. `thetrevorproject.org` - Several Trevor Project resource pages
9. `pflag.org/resource/be-yourself/` - PFLAG coming out resources
10. `truecolorsunited.org/` - Youth housing resources
11. `at3center.net/state-at-programs/` - Assistive technology centers

## Maintaining Links

When adding new links:
1. Test them manually first
2. Run the validation script after updates
3. Prefer stable, institutional URLs over personal blogs
4. Include archive.org links as backups for critical resources

## Note on 403 Errors

Some sites (rainn.org, plannedparenthood.org, goodrx.com, etc.) return 403 Forbidden to automated requests but work fine for human visitors. This is intentional bot protection. These don't need to be "fixed" - they're accessible to students.
