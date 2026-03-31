#!/usr/bin/env python3
"""Example: Search for packages with version constraints.

This script demonstrates how to search for packages using PURL patterns
and version constraints.

Usage:
    python search_packages.py [PURL_PATTERN]

Examples:
    python search_packages.py "pkg:deb/ubuntu/python-django-doc@>=2:3.0.0?arch=all&distro=ubuntu-22.04"

Environment:
    Requires .env file or environment variables (see .env.example)
"""

import sys
from netrise_provenance_sdk import ProvenanceClient, ProvenanceClientConfig

# Default example search if none provided
DEFAULT_SEARCH = "pkg:deb/ubuntu/python-django-doc@>=2:3.0.0?arch=all&distro=ubuntu-22.04"


def main():
    search_pattern = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SEARCH

    print(f"Searching for packages: {search_pattern}")
    print("-" * 60)

    config = ProvenanceClientConfig.from_env()
    client = ProvenanceClient(config)

    response = client.search_packages(search_pattern)

    if response and response.purls:
        print(f"Found {len(response.purls)} matching packages:\n")
        for purl in response.purls[:20]:  # Show first 20
            print(f"  {purl}")

        if len(response.purls) > 20:
            print(f"\n  ... and {len(response.purls) - 20} more")
    else:
        print("No matching packages found")


if __name__ == "__main__":
    main()
