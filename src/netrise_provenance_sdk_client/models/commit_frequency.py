from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CommitFrequency")


@_attrs_define
class CommitFrequency:
    """
    Attributes:
        days_90 (int): Number of commits in the last 90 days
        days_180 (int): Number of commits in the last 180 days
        days_365 (int): Number of commits in the last 365 days
    """

    days_90: int
    days_180: int
    days_365: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days_90 = self.days_90

        days_180 = self.days_180

        days_365 = self.days_365

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days_90": days_90,
                "days_180": days_180,
                "days_365": days_365,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days_90 = d.pop("days_90")

        days_180 = d.pop("days_180")

        days_365 = d.pop("days_365")

        commit_frequency = cls(
            days_90=days_90,
            days_180=days_180,
            days_365=days_365,
        )

        commit_frequency.additional_properties = d
        return commit_frequency

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
