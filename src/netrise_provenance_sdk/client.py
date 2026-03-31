from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import httpx
from dotenv import find_dotenv, load_dotenv

# Import the generated client
from netrise_provenance_sdk_client import AuthenticatedClient
from netrise_provenance_sdk_client.api.contributors import (
    get_contributor,
    get_contributor_security,
)
from netrise_provenance_sdk_client.api.packages import (
    get_package,
    search_packages,
    get_dependents,
)
from netrise_provenance_sdk_client.api.repositories import (
    get_repository,
    get_repository_health,
)
from netrise_provenance_sdk_client.api.advisories import get_advisory
from netrise_provenance_sdk_client.models import (
    ContributorResponse,
    ContributorSecurityResponse,
    PackageResponse,
    PackageSearchResponse,
    PackageDependentResponse,
    RepositoryResponse,
    RepositoryHealthResponse,
    AdvisoryResponse,
    ErrorResponse,
)


@dataclass(frozen=True)
class ProvenanceClientConfig:
    """Configuration for the Provenance API client.

    Attributes:
        endpoint: The base URL for the Provenance API
            (e.g., https://api.provenance.netrise.io/v1/provenance)
        api_token: API token for authentication
    """

    endpoint: str
    api_token: str

    @staticmethod
    def from_env(load_env_file: bool = True) -> "ProvenanceClientConfig":
        """Load config from environment variables.

        If `load_env_file` is True, automatically loads a `.env` file from:
        - Current working directory (most common)
        - Parent directories (walks up the directory tree)

        Environment variables can also be set directly without a `.env` file.
        Set `load_env_file=False` to disable automatic `.env` file loading.
        """
        if load_env_file:
            # Prioritize .env file in current working directory
            current_dir_env = Path.cwd() / ".env"
            if current_dir_env.exists():
                load_dotenv(current_dir_env, override=False)
            else:
                # If no .env in current directory, search parent directories
                dotenv_path = find_dotenv(usecwd=True)
                if dotenv_path:
                    load_dotenv(dotenv_path, override=False)
                else:
                    # Fallback to default behavior
                    load_dotenv(override=False)

        endpoint = (os.getenv("PROVENANCE_ENDPOINT") or "").strip()
        if not endpoint:
            raise ValueError(
                "PROVENANCE_ENDPOINT is required "
                "(e.g., https://api.provenance.netrise.io/v1/provenance)"
            )

        api_token = (os.getenv("PROVENANCE_API_TOKEN") or "").strip()
        if not api_token:
            raise ValueError("PROVENANCE_API_TOKEN is required")

        return ProvenanceClientConfig(
            endpoint=endpoint,
            api_token=api_token,
        )


class ProvenanceClient:
    """Sync-first Provenance API client.

    Example:
        >>> config = ProvenanceClientConfig.from_env()
        >>> client = ProvenanceClient(config)
        >>> package = client.get_package("pkg:deb/debian/curl@7.68.0?arch=amd64&distro=debian-12")
        >>> print(package.data.product)
    """

    def __init__(
        self,
        config: ProvenanceClientConfig,
        *,
        timeout: float = 30.0,
    ) -> None:
        self._config = config
        self._timeout = timeout

    @property
    def config(self) -> ProvenanceClientConfig:
        return self._config

    def _get_client(self) -> AuthenticatedClient:
        """Get an authenticated client instance."""
        token = self._config.api_token
        # Strip "Bearer " prefix if present, AuthenticatedClient adds it
        if token.startswith("Bearer "):
            token = token[7:]

        return AuthenticatedClient(
            base_url=self._config.endpoint,
            token=token,
            timeout=httpx.Timeout(self._timeout),
            raise_on_unexpected_status=True,
        )

    # --- Contributor endpoints ---

    def get_contributor(
        self,
        *,
        email: Optional[str] = None,
        username: Optional[str] = None,
    ) -> ContributorResponse:
        """Get contributor by email or GitHub username.

        Args:
            email: Contributor's email address
            username: Contributor's GitHub username

        Returns:
            ContributorResponse with identity, contributions, organizations, and advisories

        Raises:
            ValueError: If both or neither email and username are provided
            httpx.HTTPStatusError: For API errors
        """
        if email and username:
            raise ValueError("email and username are mutually exclusive")
        if not email and not username:
            raise ValueError("Either email or username is required")

        with self._get_client() as client:
            result = get_contributor.sync(
                client=client,
                email=email if email else get_contributor.UNSET,
                username=username if username else get_contributor.UNSET,
            )

        if isinstance(result, ErrorResponse):
            raise _api_error(result)
        if result is None:
            raise RuntimeError("Unexpected empty response from API")
        return result

    def get_contributor_security(
        self,
        *,
        email: Optional[str] = None,
        username: Optional[str] = None,
    ) -> ContributorSecurityResponse:
        """Get security information for a contributor.

        Args:
            email: Contributor's email address
            username: Contributor's GitHub username

        Returns:
            ContributorSecurityResponse with breach status, signing key info, etc.

        Raises:
            ValueError: If both or neither email and username are provided
            httpx.HTTPStatusError: For API errors
        """
        if email and username:
            raise ValueError("email and username are mutually exclusive")
        if not email and not username:
            raise ValueError("Either email or username is required")

        with self._get_client() as client:
            result = get_contributor_security.sync(
                client=client,
                email=email if email else get_contributor_security.UNSET,
                username=username if username else get_contributor_security.UNSET,
            )

        if isinstance(result, ErrorResponse):
            raise _api_error(result)
        if result is None:
            raise RuntimeError("Unexpected empty response from API")
        return result

    # --- Package endpoints ---

    def get_package(
        self,
        identifier: str,
    ) -> PackageResponse:
        """Get package by PURL identifier.

        Args:
            identifier: Package URL (PURL) in the format
                pkg:type/namespace/name@version?arch=ARCH&distro=DISTRO

        Returns:
            PackageResponse with package details, contributors, dependencies

        Raises:
            httpx.HTTPStatusError: For API errors
        """
        with self._get_client() as client:
            result = get_package.sync(
                client=client,
                identifier=identifier,
            )

        if isinstance(result, ErrorResponse):
            raise _api_error(result)
        if result is None:
            raise RuntimeError("Unexpected empty response from API")
        return result

    def search_packages(self, identifier: str) -> PackageSearchResponse:
        """Search packages by PURL with optional version constraints.

        Args:
            identifier: PURL with optional version constraints
                (supports operators: >=, <=, >, <, =)

        Returns:
            PackageSearchResponse with array of matching PURLs

        Raises:
            httpx.HTTPStatusError: For API errors
        """
        with self._get_client() as client:
            result = search_packages.sync(
                client=client,
                identifier=identifier,
            )

        if isinstance(result, ErrorResponse):
            raise _api_error(result)
        if result is None:
            raise RuntimeError("Unexpected empty response from API")
        return result

    def get_dependents(self, identifier: str) -> PackageDependentResponse:
        """Get packages that depend on a given PURL.

        Args:
            identifier: Package URL (PURL) identifier

        Returns:
            PackageDependentResponse with array of dependent package PURLs

        Raises:
            httpx.HTTPStatusError: For API errors
        """
        with self._get_client() as client:
            result = get_dependents.sync(
                client=client,
                identifier=identifier,
            )

        if isinstance(result, ErrorResponse):
            raise _api_error(result)
        if result is None:
            raise RuntimeError("Unexpected empty response from API")
        return result

    # --- Repository endpoints ---

    def get_repository(self, repo_url: str) -> RepositoryResponse:
        """Get repository details by URL.

        Args:
            repo_url: Repository URL (e.g., https://github.com/org/repo)

        Returns:
            RepositoryResponse with packages, contributors, repository info

        Raises:
            httpx.HTTPStatusError: For API errors
        """
        with self._get_client() as client:
            result = get_repository.sync(
                client=client,
                repo_url=repo_url,
            )

        if isinstance(result, ErrorResponse):
            raise _api_error(result)
        if result is None:
            raise RuntimeError("Unexpected empty response from API")
        return result

    def get_repository_health(self, repo_url: str) -> RepositoryHealthResponse:
        """Get repository health metrics.

        Args:
            repo_url: Repository URL (e.g., https://github.com/org/repo)

        Returns:
            RepositoryHealthResponse with scorecard, activity, security config, etc.

        Raises:
            httpx.HTTPStatusError: For API errors
        """
        with self._get_client() as client:
            result = get_repository_health.sync(
                client=client,
                repo_url=repo_url,
            )

        if isinstance(result, ErrorResponse):
            raise _api_error(result)
        if result is None:
            raise RuntimeError("Unexpected empty response from API")
        return result

    # --- Advisory endpoint ---

    def get_advisory(self, advisory_id: str) -> AdvisoryResponse:
        """Get information about an advisory.

        Args:
            advisory_id: Advisory identifier (e.g., CVE-2021-44228)

        Returns:
            AdvisoryResponse with advisory details and affected components

        Raises:
            httpx.HTTPStatusError: For API errors
        """
        with self._get_client() as client:
            result = get_advisory.sync(
                client=client,
                advisory_id=advisory_id,
            )

        if isinstance(result, ErrorResponse):
            raise _api_error(result)
        if result is None:
            raise RuntimeError("Unexpected empty response from API")
        return result


class ProvenanceAPIError(Exception):
    """Exception raised when the Provenance API returns an error response."""

    def __init__(self, error_response: ErrorResponse):
        self.error_response = error_response
        super().__init__(str(error_response))


def _api_error(error_response: ErrorResponse) -> ProvenanceAPIError:
    """Create a ProvenanceAPIError from an ErrorResponse."""
    return ProvenanceAPIError(error_response)
