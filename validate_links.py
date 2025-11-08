#!/usr/bin/env python3
"""
Validate all links in the handbook to ensure they don't return 404s or other errors.
"""

import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse
import requests

# Configuration
TIMEOUT = 10  # seconds
DELAY = 0.5  # seconds between requests to be nice to servers
USER_AGENT = 'Mozilla/5.0 (compatible; LinkChecker/1.0)'

def extract_urls_from_markdown(file_path):
    """Extract all URLs from a markdown file."""
    urls = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

        # Match markdown links: [text](url)
        markdown_links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
        for text, url in markdown_links:
            if url.startswith('http'):
                urls.append((url, file_path, f'[{text}]({url})'))

        # Match bare URLs: http(s)://...
        bare_urls = re.findall(r'(?<!\()(https?://[^\s\)]+)', content)
        for url in bare_urls:
            urls.append((url, file_path, url))

    return urls

def check_url(url):
    """Check if a URL is accessible."""
    try:
        response = requests.head(
            url,
            timeout=TIMEOUT,
            headers={'User-Agent': USER_AGENT},
            allow_redirects=True
        )

        # Some servers don't respond to HEAD, try GET
        if response.status_code == 405 or response.status_code == 404:
            response = requests.get(
                url,
                timeout=TIMEOUT,
                headers={'User-Agent': USER_AGENT},
                allow_redirects=True,
                stream=True  # Don't download the whole page
            )

        return response.status_code, response.reason

    except requests.exceptions.Timeout:
        return None, "Timeout"
    except requests.exceptions.ConnectionError:
        return None, "Connection Error"
    except requests.exceptions.TooManyRedirects:
        return None, "Too Many Redirects"
    except requests.exceptions.RequestException as e:
        return None, str(e)

def main():
    """Main function to validate all links."""
    # Find all markdown files
    handbook_dir = Path(__file__).parent
    md_files = list(handbook_dir.rglob('*.md'))

    print(f"Scanning {len(md_files)} markdown files for links...\n")

    # Extract all URLs
    all_urls = []
    for md_file in md_files:
        urls = extract_urls_from_markdown(md_file)
        all_urls.extend(urls)

    if not all_urls:
        print("No URLs found in markdown files.")
        return 0

    # Deduplicate URLs but keep track of where they appear
    url_locations = {}
    for url, file_path, context in all_urls:
        if url not in url_locations:
            url_locations[url] = []
        url_locations[url].append((file_path, context))

    print(f"Found {len(url_locations)} unique URLs to check.\n")

    # Check each URL
    broken_links = []
    working_links = 0

    for i, (url, locations) in enumerate(url_locations.items(), 1):
        print(f"[{i}/{len(url_locations)}] Checking: {url}")

        status_code, reason = check_url(url)

        if status_code is None:
            print(f"  ❌ FAILED: {reason}")
            broken_links.append((url, None, reason, locations))
        elif 200 <= status_code < 400:
            print(f"  ✅ OK ({status_code})")
            working_links += 1
        else:
            print(f"  ❌ ERROR: {status_code} {reason}")
            broken_links.append((url, status_code, reason, locations))

        # Be nice to servers
        time.sleep(DELAY)

    # Print summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total URLs checked: {len(url_locations)}")
    print(f"Working links: {working_links}")
    print(f"Broken links: {len(broken_links)}")

    if broken_links:
        print("\n" + "="*80)
        print("BROKEN LINKS")
        print("="*80)

        for url, status_code, reason, locations in broken_links:
            print(f"\n❌ {url}")
            if status_code:
                print(f"   Status: {status_code} {reason}")
            else:
                print(f"   Error: {reason}")
            print(f"   Found in {len(locations)} location(s):")
            for file_path, context in locations:
                print(f"     - {file_path}")
                print(f"       {context}")

        return 1  # Exit with error code
    else:
        print("\n✅ All links are working!")
        return 0

if __name__ == '__main__':
    sys.exit(main())
