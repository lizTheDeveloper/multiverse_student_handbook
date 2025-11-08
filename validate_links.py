#!/usr/bin/env python3
"""
Validate all links in the handbook to ensure they don't return 404s or other errors.
Uses Playwright for 403 errors to bypass bot detection.
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

# Try to import playwright - optional dependency
try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    print("⚠️  Playwright not available - 403 errors won't be re-checked")
    print("   Install with: pip3 install playwright && python3 -m playwright install chromium\n")

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

def check_url_with_playwright(url):
    """Check if a URL is accessible using Playwright (bypasses bot detection)."""
    if not PLAYWRIGHT_AVAILABLE:
        return None, "Playwright not available"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Try to load the page
            response = page.goto(url, timeout=TIMEOUT * 1000, wait_until='domcontentloaded')

            status_code = response.status if response else None
            browser.close()

            if status_code and 200 <= status_code < 400:
                return status_code, "OK (via Playwright)"
            elif status_code:
                return status_code, f"HTTP {status_code} (via Playwright)"
            else:
                return None, "No response (via Playwright)"

    except Exception as e:
        return None, f"Playwright error: {str(e)[:50]}"

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
    bot_protected = []  # 403s that work with Playwright

    for i, (url, locations) in enumerate(url_locations.items(), 1):
        print(f"[{i}/{len(url_locations)}] Checking: {url}")

        status_code, reason = check_url(url)

        # If we get a 403, retry with Playwright
        if status_code == 403 and PLAYWRIGHT_AVAILABLE:
            print(f"  🔄 Got 403, retrying with Playwright...")
            time.sleep(1)  # Be extra nice before playwright request
            pw_status, pw_reason = check_url_with_playwright(url)

            if pw_status and 200 <= pw_status < 400:
                print(f"  ✅ OK with Playwright ({pw_status}) - Bot protection only")
                working_links += 1
                bot_protected.append((url, locations))
            else:
                print(f"  ❌ FAILED with Playwright: {pw_reason}")
                broken_links.append((url, status_code, f"403 Forbidden (also failed Playwright: {pw_reason})", locations))
        elif status_code is None:
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
    if bot_protected:
        print(f"Bot-protected (403 but work in browser): {len(bot_protected)}")
    print(f"Broken links: {len(broken_links)}")

    if bot_protected:
        print("\n" + "="*80)
        print("BOT-PROTECTED LINKS (403 for bots, OK for humans)")
        print("="*80)
        print("\nThese sites block automated requests but work fine for actual visitors:\n")
        for url, locations in bot_protected:
            print(f"✅ {url}")

    if broken_links:
        print("\n" + "="*80)
        print("BROKEN LINKS")
        print("="*80)
        print("\n⚠️  Note: In current political climate (Nov 2025), some sites may be")
        print("   genuinely taken down by government or shut down due to funding cuts.\n")

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
