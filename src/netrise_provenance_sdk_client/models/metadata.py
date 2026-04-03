from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_attribution import DataSourceAttribution


T = TypeVar("T", bound="Metadata")


@_attrs_define
class Metadata:
    """
    Attributes:
        compiled_at (str):
        attributions (list[DataSourceAttribution] | Unset): Data source attributions required by licensing agreements
    """

    compiled_at: str
    attributions: list[DataSourceAttribution] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compiled_at = self.compiled_at

        attributions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attributions, Unset):
            attributions = []
            for attributions_item_data in self.attributions:
                attributions_item = attributions_item_data.to_dict()
                attributions.append(attributions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "compiled_at": compiled_at,
            }
        )
        if attributions is not UNSET:
            field_dict["attributions"] = attributions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_attribution import DataSourceAttribution

        d = dict(src_dict)
        compiled_at = d.pop("compiled_at")

        _attributions = d.pop("attributions", UNSET)
        attributions: list[DataSourceAttribution] | Unset = UNSET
        if _attributions is not UNSET:
            attributions = []
            for attributions_item_data in _attributions:
                attributions_item = DataSourceAttribution.from_dict(
                    attributions_item_data
                )

                attributions.append(attributions_item)

        metadata = cls(
            compiled_at=compiled_at,
            attributions=attributions,
        )

        metadata.additional_properties = d
        return metadata

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
