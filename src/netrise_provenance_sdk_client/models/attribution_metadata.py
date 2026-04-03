from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AttributionMetadata")


@_attrs_define
class AttributionMetadata:
    """
    Attributes:
        confidence (int): A confidence rating of this attribution as a percentage (0-100)
        methods (list[str]): A list of method names that attributed this quality to the entity
    """

    confidence: int
    methods: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence

        methods = self.methods

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidence": confidence,
                "methods": methods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confidence = d.pop("confidence")

        methods = cast(list[str], d.pop("methods"))

        attribution_metadata = cls(
            confidence=confidence,
            methods=methods,
        )

        attribution_metadata.additional_properties = d
        return attribution_metadata

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
