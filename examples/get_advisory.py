#!/usr/bin/env python3
"""Example: Get security advisory information.

This script demonstrates how to look up security advisory details by ID.

Usage:
    python get_advisory.py [ADVISORY_ID]

Examples:
    python get_advisory.py NETR-2026-0001

Environment:
    Requires .env file or environment variables (see .env.example)
"""

import sys
from netrise_provenance_sdk import ProvenanceClient, ProvenanceClientConfig

# Default example advisory
DEFAULT_ADVISORY = "NETR-2024-0001"


def main():
    advisory_id = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_ADVISORY

    print(f"Looking up advisory: {advisory_id}")
    print("-" * 60)

    config = ProvenanceClientConfig.from_env()
    client = ProvenanceClient(config)

    response = client.get_advisory(advisory_id)

    if response:
        adv = response
        print(f"Name:        {adv.name}")
        print(f"Created:     {adv.created_at}")

        if adv.description:
            print(f"\nDescription:\n{adv.description[:500]}...")

        if adv.urls:
            print(f"\nReferences:")
            for url in adv.urls[:5]:
                print(f"  - {url}")

        if adv.packages and adv.packages.direct:
            print(f"\nDirectly Affected Packages: {len(adv.packages.direct)}")
            for purl in adv.packages.direct[:5]:
                print(f"  - {purl}")

        if adv.packages and adv.packages.indirect:
            print(f"\nIndirectly Affected Packages: {len(adv.packages.indirect)}")
            for purl in adv.packages.indirect[:5]:
                print(f"  - {purl}")

        if adv.repositories and adv.repositories.direct:
            print(f"\nAffected Repositories: {len(adv.repositories.direct)}")
            for repo in adv.repositories.direct[:5]:
                print(f"  - {repo}")
    else:
        print("No data returned")


if __name__ == "__main__":
    main()
