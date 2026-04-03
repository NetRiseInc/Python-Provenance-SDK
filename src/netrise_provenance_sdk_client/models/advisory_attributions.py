from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvisoryAttributions")


@_attrs_define
class AdvisoryAttributions:
    """
    Attributes:
        direct (list[str] | Unset): Components that are directly impacted by advisory
        indirect (list[str] | Unset): Components that are indirectly impacted by advisory
    """

    direct: list[str] | Unset = UNSET
    indirect: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direct: list[str] | Unset = UNSET
        if not isinstance(self.direct, Unset):
            direct = self.direct

        indirect: list[str] | Unset = UNSET
        if not isinstance(self.indirect, Unset):
            indirect = self.indirect

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if direct is not UNSET:
            field_dict["direct"] = direct
        if indirect is not UNSET:
            field_dict["indirect"] = indirect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        direct = cast(list[str], d.pop("direct", UNSET))

        indirect = cast(list[str], d.pop("indirect", UNSET))

        advisory_attributions = cls(
            direct=direct,
            indirect=indirect,
        )

        advisory_attributions.additional_properties = d
        return advisory_attributions

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
