#!/usr/bin/env python3
"""Example: Get contributor information.

This script demonstrates how to look up contributor details by email or GitHub username.

Usage:
    python get_contributor.py --email example@example.com
    python get_contributor.py --username example-user

Environment:
    Requires .env file or environment variables (see .env.example)
"""

import argparse
from netrise_provenance_sdk import ProvenanceClient, ProvenanceClientConfig


def main():
    parser = argparse.ArgumentParser(description="Look up contributor information")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--email", help="Contributor's email address")
    group.add_argument("--username", help="Contributor's GitHub username")
    args = parser.parse_args()

    identifier = args.email or args.username
    print(f"Looking up contributor: {identifier}")
    print("-" * 60)

    config = ProvenanceClientConfig.from_env()
    client = ProvenanceClient(config)

    response = client.get_contributor(email=args.email, username=args.username)

    if response.data:
        contrib = response.data

        if contrib.identity:
            print("Identity:")
            emails = contrib.identity.emails if hasattr(contrib.identity.emails, '__iter__') and not isinstance(contrib.identity.emails, str) else []
            usernames = contrib.identity.usernames if hasattr(contrib.identity.usernames, '__iter__') and not isinstance(contrib.identity.usernames, str) else []
            print(f"  Emails:    {', '.join(emails) if emails else 'N/A'}")
            print(f"  Usernames: {', '.join(usernames) if usernames else 'N/A'}")
            print(f"  Names:     {', '.join(contrib.identity.declared_names or [])}")

        if contrib.summary and contrib.summary.repos_contributed_to:
            repos = contrib.summary.repos_contributed_to
            print(f"\nContributions: {len(repos)} repositories")
            for repo in repos[:5]:
                signed = "✓ signed" if repo.has_signed_commits else ""
                print(f"  - {repo.url} {signed}")

        if contrib.organizations:
            print(f"\nOrganizations: {len(contrib.organizations)}")
            for org in contrib.organizations[:5]:
                print(f"  - {org.name} ({org.repository_url})")

        if contrib.advisories:
            print(f"\nAdvisories: {len(contrib.advisories)}")
            for adv in contrib.advisories[:5]:
                print(f"  - {adv.name} ({adv.relationship})")

        if contrib.locations:
            print(f"\nLocations: {len(contrib.locations)}")
            for loc in contrib.locations[:3]:
                print(f"  - {loc.country} ({loc.confidence}% confidence)")
    else:
        print("No data returned")


if __name__ == "__main__":
    main()
