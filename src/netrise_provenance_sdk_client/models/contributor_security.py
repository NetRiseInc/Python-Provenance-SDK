from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.breach_detail import BreachDetail
    from ..models.metadata import Metadata
    from ..models.signing_key_info import SigningKeyInfo


T = TypeVar("T", bound="ContributorSecurity")


@_attrs_define
class ContributorSecurity:
    """
    Attributes:
        has_breached_credentials (bool):
        signed_commit_ratio (float): Ratio of signed to total commits across all repos (0.0-1.0)
        signing_key_info (SigningKeyInfo):
        has_password_exposure (bool): Whether any email has been exposed in a breach containing passwords
        breach_details (list[BreachDetail]):
        breach_last_refreshed_at (datetime.datetime | None | Unset): When the breach data was last refreshed
        metadata (Metadata | Unset):
    """

    has_breached_credentials: bool
    signed_commit_ratio: float
    signing_key_info: SigningKeyInfo
    has_password_exposure: bool
    breach_details: list[BreachDetail]
    breach_last_refreshed_at: datetime.datetime | None | Unset = UNSET
    metadata: Metadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_breached_credentials = self.has_breached_credentials

        signed_commit_ratio = self.signed_commit_ratio

        signing_key_info = self.signing_key_info.to_dict()

        has_password_exposure = self.has_password_exposure

        breach_details = []
        for breach_details_item_data in self.breach_details:
            breach_details_item = breach_details_item_data.to_dict()
            breach_details.append(breach_details_item)

        breach_last_refreshed_at: None | str | Unset
        if isinstance(self.breach_last_refreshed_at, Unset):
            breach_last_refreshed_at = UNSET
        elif isinstance(self.breach_last_refreshed_at, datetime.datetime):
            breach_last_refreshed_at = self.breach_last_refreshed_at.isoformat()
        else:
            breach_last_refreshed_at = self.breach_last_refreshed_at

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_breached_credentials": has_breached_credentials,
                "signed_commit_ratio": signed_commit_ratio,
                "signing_key_info": signing_key_info,
                "has_password_exposure": has_password_exposure,
                "breach_details": breach_details,
            }
        )
        if breach_last_refreshed_at is not UNSET:
            field_dict["breach_last_refreshed_at"] = breach_last_refreshed_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.breach_detail import BreachDetail
        from ..models.metadata import Metadata
        from ..models.signing_key_info import SigningKeyInfo

        d = dict(src_dict)
        has_breached_credentials = d.pop("has_breached_credentials")

        signed_commit_ratio = d.pop("signed_commit_ratio")

        signing_key_info = SigningKeyInfo.from_dict(d.pop("signing_key_info"))

        has_password_exposure = d.pop("has_password_exposure")

        breach_details = []
        _breach_details = d.pop("breach_details")
        for breach_details_item_data in _breach_details:
            breach_details_item = BreachDetail.from_dict(breach_details_item_data)

            breach_details.append(breach_details_item)

        def _parse_breach_last_refreshed_at(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                breach_last_refreshed_at_type_0 = isoparse(data)

                return breach_last_refreshed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        breach_last_refreshed_at = _parse_breach_last_refreshed_at(
            d.pop("breach_last_refreshed_at", UNSET)
        )

        _metadata = d.pop("metadata", UNSET)
        metadata: Metadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        contributor_security = cls(
            has_breached_credentials=has_breached_credentials,
            signed_commit_ratio=signed_commit_ratio,
            signing_key_info=signing_key_info,
            has_password_exposure=has_password_exposure,
            breach_details=breach_details,
            breach_last_refreshed_at=breach_last_refreshed_at,
            metadata=metadata,
        )

        contributor_security.additional_properties = d
        return contributor_security

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
