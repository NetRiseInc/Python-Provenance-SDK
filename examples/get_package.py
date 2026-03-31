#!/usr/bin/env python3
"""Example: Get package information by PURL.

This script demonstrates how to look up package details using the Provenance API.

Usage:
    python get_package.py [PURL]

Environment:
    Requires .env file or environment variables (see .env.example)
"""

import sys
from netrise_provenance_sdk import ProvenanceClient, ProvenanceClientConfig

# Default example PURL if none provided
DEFAULT_PURL = "pkg:deb/ubuntu/python-django-doc@2:3.2.12-2ubuntu1.25?arch=all&distro=ubuntu-22.04"


def main():
    purl = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PURL

    print(f"Looking up package: {purl}")
    print("-" * 60)

    config = ProvenanceClientConfig.from_env()
    client = ProvenanceClient(config)

    response = client.get_package(purl)

    if response.data:
        pkg = response.data
        print(f"Product:      {pkg.product}")
        print(f"Version:      {pkg.version}")
        print(f"Type:         {pkg.package_type}")
        print(f"License:      {pkg.package_details.license_}")
        summary = pkg.package_details.summary[:60] if pkg.package_details.summary else "N/A"
        print(f"Summary:      {summary}...")

        if pkg.repository_details:
            print(f"\nRepository:   {pkg.repository_details.url}")
            if pkg.repository_details.contributors:
                print(f"Contributors: {len(pkg.repository_details.contributors)}")
                for c in pkg.repository_details.contributors[:5]:
                    print(f"  - {c.email}")

        if pkg.dependencies:
            print(f"\nDependencies: {len(pkg.dependencies)}")
            for dep in pkg.dependencies[:5]:
                print(f"  - {dep.purl}")

        if pkg.advisories:
            print(f"\nAdvisories: {len(pkg.advisories)}")
            for adv in pkg.advisories[:3]:
                print(f"  - {adv.name} ({adv.relationship})")
    else:
        print("No data returned")


if __name__ == "__main__":
    main()
