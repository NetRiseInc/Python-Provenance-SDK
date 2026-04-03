from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DataSourceAttribution")


@_attrs_define
class DataSourceAttribution:
    """
    Attributes:
        provider (str): The name of the data provider
        url (str): The URL for the data provider
        license_ (str): The license under which the data is provided
        reason (str): The reason for including this attribution
    """

    provider: str
    url: str
    license_: str
    reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        url = self.url

        license_ = self.license_

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "url": url,
                "license": license_,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = d.pop("provider")

        url = d.pop("url")

        license_ = d.pop("license")

        reason = d.pop("reason")

        data_source_attribution = cls(
            provider=provider,
            url=url,
            license_=license_,
            reason=reason,
        )

        data_source_attribution.additional_properties = d
        return data_source_attribution

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
