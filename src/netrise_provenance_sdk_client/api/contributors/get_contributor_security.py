from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contributor_security_response import ContributorSecurityResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    email: str | Unset = UNSET,
    username: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["email"] = email

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contributor/security",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContributorSecurityResponse | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = ContributorSecurityResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ContributorSecurityResponse | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    username: str | Unset = UNSET,
) -> Response[ContributorSecurityResponse | ErrorResponse]:
    """Get contributor security info

     Get security information for a contributor including breach status, signing key details, and signed
    commit ratio

    Args:
        email (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContributorSecurityResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        email=email,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    username: str | Unset = UNSET,
) -> ContributorSecurityResponse | ErrorResponse | None:
    """Get contributor security info

     Get security information for a contributor including breach status, signing key details, and signed
    commit ratio

    Args:
        email (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContributorSecurityResponse | ErrorResponse
    """

    return sync_detailed(
        client=client,
        email=email,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    username: str | Unset = UNSET,
) -> Response[ContributorSecurityResponse | ErrorResponse]:
    """Get contributor security info

     Get security information for a contributor including breach status, signing key details, and signed
    commit ratio

    Args:
        email (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContributorSecurityResponse | ErrorResponse]
    """

    kwargs = _get_kwargs(
        email=email,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    username: str | Unset = UNSET,
) -> ContributorSecurityResponse | ErrorResponse | None:
    """Get contributor security info

     Get security information for a contributor including breach status, signing key details, and signed
    commit ratio

    Args:
        email (str | Unset):
        username (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContributorSecurityResponse | ErrorResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            email=email,
            username=username,
        )
    ).parsed
