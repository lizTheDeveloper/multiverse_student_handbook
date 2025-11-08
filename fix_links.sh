#!/bin/bash
# Bulk fix broken links found in validation

# Fix transformharm.org TJ principles
find . -name "*.md" -type f -exec sed -i '' 's|transformharm\.org/tj-principles/|transformharm.org/tj_resource/transformative-justice-a-brief-description/|g' {} \;

# Fix Icarus Project -> Fireweed Collective
find . -name "*.md" -type f -exec sed -i '' 's|theicarusproject\.net/resources|fireweedcollective.org/crisis-toolkit/|g' {} \;

# Fix GLMA provider directory
find . -name "*.md" -type f -exec sed -i '' 's|glma\.org/provider-directory/|lgbtqhealthcaredirectory.org/|g' {} \;

# Fix Trevor Project coming out handbook
find . -name "*.md" -type f -exec sed -i '' 's|thetrevorproject\.org/resources/article/coming-out-handbook/|thetrevorproject.org/resources/guide/the-coming-out-handbook/|g' {} \;

# Fix PFLAG coming out
find . -name "*.md" -type f -exec sed -i '' 's|pflag\.org/cominout|pflag.org/resource/be-yourself/|g' {} \;

# Fix Trevor Project religion/faith
find . -name "*.md" -type f -exec sed -i '' 's|thetrevorproject\.org/resources/category/religion-faith/|thetrevorproject.org/resources/article/navigating-lgbtq-identities-and-religion/|g' {} \;

# Fix True Colors United housing (just use main site)
find . -name "*.md" -type f -exec sed -i '' 's|truecolorsunited\.org/our-work/housing-assistance/|truecolorsunited.org/|g' {} \;

# Fix AT3 Center state programs
find . -name "*.md" -type f -exec sed -i '' 's|at3center\.net/stateprogram/|at3center.net/state-at-programs/|g' {} \;

# Fix bell hooks center
find . -name "*.md" -type f -exec sed -i '' 's|bellhookscenter\.org/|berea.edu/bhc/|g' {} \;

# Fix embrace autism (add hyphen)
find . -name "*.md" -type f -exec sed -i '' 's|embraceautism\.com/|embrace-autism.com/|g' {} \;

# Fix LGBT hotline
find . -name "*.md" -type f -exec sed -i '' 's|glbthotline\.org/|lgbthotline.org/|g' {} \;

# Fix OutCare Health
find . -name "*.md" -type f -exec sed -i '' 's|outcare\.health/|outcarehealth.org/|g' {} \;

# Fix cult education
find . -name "*.md" -type f -exec sed -i '' 's|culteducation\.com/|culteducation.com/|g' {} \;

echo "Link fixes applied!"
