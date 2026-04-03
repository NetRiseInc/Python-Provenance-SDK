from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PackageAffiliation")


@_attrs_define
class PackageAffiliation:
    """
    Attributes:
        confidence (int): A confidence rating of this attribution as a percentage (0-100)
        methods (list[str]): A list of method names that attributed this quality to the entity
        purl (str):
    """

    confidence: int
    methods: list[str]
    purl: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confidence = self.confidence

        methods = self.methods

        purl = self.purl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confidence": confidence,
                "methods": methods,
                "purl": purl,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confidence = d.pop("confidence")

        methods = cast(list[str], d.pop("methods"))

        purl = d.pop("purl")

        package_affiliation = cls(
            confidence=confidence,
            methods=methods,
            purl=purl,
        )

        package_affiliation.additional_properties = d
        return package_affiliation

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
