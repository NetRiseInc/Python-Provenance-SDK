from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PackageDataDependenciesItem")


@_attrs_define
class PackageDataDependenciesItem:
    """
    Attributes:
        purl (str): Dependency PURL with version constraint
        depth (int): Depth level from root package (1-3)
    """

    purl: str
    depth: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purl = self.purl

        depth = self.depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "purl": purl,
                "depth": depth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        purl = d.pop("purl")

        depth = d.pop("depth")

        package_data_dependencies_item = cls(
            purl=purl,
            depth=depth,
        )

        package_data_dependencies_item.additional_properties = d
        return package_data_dependencies_item

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
