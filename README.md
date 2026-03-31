# Provenance API Python SDK

Python SDK for the Provenance API, providing access to package, repository, and contributor intelligence.

## Installation

```bash
pip install netrise-provenance-sdk
```

## Quick Start

```python
from netrise_provenance_sdk import ProvenanceClient, ProvenanceClientConfig

# Load config from environment variables
config = ProvenanceClientConfig.from_env()
client = ProvenanceClient(config)

# Get package information by PURL
package = client.get_package("pkg:deb/debian/curl@7.68.0?arch=amd64&distro=debian-12")
print(package.data.product)

# Get contributor by email
contributor = client.get_contributor(email="developer@example.com")
print(contributor.data.identity)

# Get repository health metrics
health = client.get_repository_health("https://github.com/example/repo")
print(health.data.scorecard)
```

## Configuration

Set environment variables in a `.env` file or export them:

```bash
# Required
PROVENANCE_ENDPOINT=https://api.provenance.netrise.io/v1/provenance
PROVENANCE_API_TOKEN=your_api_token
```

## API Reference

### Contributors

- `get_contributor(email=None, username=None)` - Get contributor by email or GitHub username
- `get_contributor_security(email=None, username=None)` - Get contributor security information

### Packages

- `get_package(identifier, depth=1)` - Get package by PURL identifier
- `search_packages(identifier)` - Search packages with optional version constraints
- `get_dependents(identifier)` - Get packages that depend on a given PURL

### Repositories

- `get_repository(repo_url)` - Get repository details by URL
- `get_repository_health(repo_url)` - Get repository health metrics

### Advisories

- `get_advisory(advisory_id)` - Get information about an advisory

## Development

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Generate OpenAPI client
make provenance-python-generate
```

