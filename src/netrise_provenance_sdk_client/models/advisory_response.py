from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_attributions import AdvisoryAttributions
    from ..models.metadata import Metadata


T = TypeVar("T", bound="AdvisoryResponse")


@_attrs_define
class AdvisoryResponse:
    """
    Attributes:
        name (str): Name of the advisory
        description (str): Text description of the advisory
        created_at (datetime.datetime): The time (ISO 8601) when the advisory was added to Provenance
        metadata (Metadata):
        urls (list[str] | Unset): Reference URLs with further information about the advisory
        repositories (AdvisoryAttributions | Unset):
        packages (AdvisoryAttributions | Unset):
        contributor_emails (AdvisoryAttributions | Unset):
        contributor_usernames (AdvisoryAttributions | Unset):
    """

    name: str
    description: str
    created_at: datetime.datetime
    metadata: Metadata
    urls: list[str] | Unset = UNSET
    repositories: AdvisoryAttributions | Unset = UNSET
    packages: AdvisoryAttributions | Unset = UNSET
    contributor_emails: AdvisoryAttributions | Unset = UNSET
    contributor_usernames: AdvisoryAttributions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        created_at = self.created_at.isoformat()

        metadata = self.metadata.to_dict()

        urls: list[str] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        repositories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = self.repositories.to_dict()

        packages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.packages, Unset):
            packages = self.packages.to_dict()

        contributor_emails: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contributor_emails, Unset):
            contributor_emails = self.contributor_emails.to_dict()

        contributor_usernames: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contributor_usernames, Unset):
            contributor_usernames = self.contributor_usernames.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "created_at": created_at,
                "metadata": metadata,
            }
        )
        if urls is not UNSET:
            field_dict["urls"] = urls
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if packages is not UNSET:
            field_dict["packages"] = packages
        if contributor_emails is not UNSET:
            field_dict["contributor_emails"] = contributor_emails
        if contributor_usernames is not UNSET:
            field_dict["contributor_usernames"] = contributor_usernames

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_attributions import AdvisoryAttributions
        from ..models.metadata import Metadata

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        created_at = isoparse(d.pop("created_at"))

        metadata = Metadata.from_dict(d.pop("metadata"))

        urls = cast(list[str], d.pop("urls", UNSET))

        _repositories = d.pop("repositories", UNSET)
        repositories: AdvisoryAttributions | Unset
        if isinstance(_repositories, Unset):
            repositories = UNSET
        else:
            repositories = AdvisoryAttributions.from_dict(_repositories)

        _packages = d.pop("packages", UNSET)
        packages: AdvisoryAttributions | Unset
        if isinstance(_packages, Unset):
            packages = UNSET
        else:
            packages = AdvisoryAttributions.from_dict(_packages)

        _contributor_emails = d.pop("contributor_emails", UNSET)
        contributor_emails: AdvisoryAttributions | Unset
        if isinstance(_contributor_emails, Unset):
            contributor_emails = UNSET
        else:
            contributor_emails = AdvisoryAttributions.from_dict(_contributor_emails)

        _contributor_usernames = d.pop("contributor_usernames", UNSET)
        contributor_usernames: AdvisoryAttributions | Unset
        if isinstance(_contributor_usernames, Unset):
            contributor_usernames = UNSET
        else:
            contributor_usernames = AdvisoryAttributions.from_dict(
                _contributor_usernames
            )

        advisory_response = cls(
            name=name,
            description=description,
            created_at=created_at,
            metadata=metadata,
            urls=urls,
            repositories=repositories,
            packages=packages,
            contributor_emails=contributor_emails,
            contributor_usernames=contributor_usernames,
        )

        advisory_response.additional_properties = d
        return advisory_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
