#!/usr/bin/env python3
"""Example: Get repository information and health metrics.

This script demonstrates how to look up repository details and health scores.

Usage:
    python get_repository.py [REPO_URL]

Environment:
    Requires .env file or environment variables (see .env.example)
"""

import sys
from netrise_provenance_sdk import ProvenanceClient, ProvenanceClientConfig

# Default example repository if none provided
DEFAULT_REPO = "https://github.com/django/django.git"


def main():
    repo_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_REPO

    print(f"Looking up repository: {repo_url}")
    print("-" * 60)

    config = ProvenanceClientConfig.from_env()
    client = ProvenanceClient(config)

    # Get basic repository info
    print("\n[Repository Info]")
    repo_response = client.get_repository(repo_url)

    if repo_response.data:
        repo = repo_response.data
        details = repo.repository_details
        desc = details.description[:80] if details.description else "N/A"
        print(f"Description:  {desc}...")
        print(f"Languages:    {', '.join(details.languages) if details.languages else 'N/A'}")
        print(f"Stars:        {int(details.star_count)}")
        print(f"Forks:        {int(details.fork_count)}")

        if repo.packages:
            print(f"\nPackages: {len(repo.packages)}")
            for pkg in repo.packages[:5]:
                print(f"  - {pkg.purl}")

        if details.contributors:
            print(f"\nContributors: {len(details.contributors)}")
            for c in details.contributors[:5]:
                signed = "✓ signed" if c.has_signed_commits else ""
                print(f"  - {c.email} {signed}")

    # Get health metrics
    print("\n[Repository Health]")
    health_response = client.get_repository_health(repo_url)

    if health_response.data:
        health = health_response.data

        if health.scorecard:
            print(f"Scorecard Score: {health.scorecard.aggregate_score}")
            if health.scorecard.checks:
                print("Checks:")
                for check in health.scorecard.checks[:5]:
                    print(f"  - {check.name}: {check.score}/10")

        if health.security_config:
            sec = health.security_config
            print(f"\nSecurity Config:")
            print(f"  Dependabot Alerts:  {sec.dependabot_alerts_enabled}")
            print(f"  Security.md:        {sec.security_md_exists}")
            print(f"  CI Workflows:       {sec.has_ci_workflows}")

        if health.activity:
            act = health.activity
            print(f"\nActivity:")
            print(f"  Last Commit:      {act.last_commit_date}")
            print(f"  Commits (90d):    {act.commit_frequency.days_90}")
            print(f"  Archived:         {act.is_archived}")
    else:
        print("No health data returned")


if __name__ == "__main__":
    main()
