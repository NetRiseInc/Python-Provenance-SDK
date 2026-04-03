from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.architecture_option import ArchitectureOption


T = TypeVar("T", bound="ArchitecturesByPackageType")


@_attrs_define
class ArchitecturesByPackageType:
    """
    Attributes:
        deb (list[ArchitectureOption] | Unset):
        rpm (list[ArchitectureOption] | Unset):
        apk (list[ArchitectureOption] | Unset):
        ipk (list[ArchitectureOption] | Unset):
    """

    deb: list[ArchitectureOption] | Unset = UNSET
    rpm: list[ArchitectureOption] | Unset = UNSET
    apk: list[ArchitectureOption] | Unset = UNSET
    ipk: list[ArchitectureOption] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deb: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.deb, Unset):
            deb = []
            for deb_item_data in self.deb:
                deb_item = deb_item_data.to_dict()
                deb.append(deb_item)

        rpm: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rpm, Unset):
            rpm = []
            for rpm_item_data in self.rpm:
                rpm_item = rpm_item_data.to_dict()
                rpm.append(rpm_item)

        apk: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.apk, Unset):
            apk = []
            for apk_item_data in self.apk:
                apk_item = apk_item_data.to_dict()
                apk.append(apk_item)

        ipk: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ipk, Unset):
            ipk = []
            for ipk_item_data in self.ipk:
                ipk_item = ipk_item_data.to_dict()
                ipk.append(ipk_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deb is not UNSET:
            field_dict["deb"] = deb
        if rpm is not UNSET:
            field_dict["rpm"] = rpm
        if apk is not UNSET:
            field_dict["apk"] = apk
        if ipk is not UNSET:
            field_dict["ipk"] = ipk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.architecture_option import ArchitectureOption

        d = dict(src_dict)
        _deb = d.pop("deb", UNSET)
        deb: list[ArchitectureOption] | Unset = UNSET
        if _deb is not UNSET:
            deb = []
            for deb_item_data in _deb:
                deb_item = ArchitectureOption.from_dict(deb_item_data)

                deb.append(deb_item)

        _rpm = d.pop("rpm", UNSET)
        rpm: list[ArchitectureOption] | Unset = UNSET
        if _rpm is not UNSET:
            rpm = []
            for rpm_item_data in _rpm:
                rpm_item = ArchitectureOption.from_dict(rpm_item_data)

                rpm.append(rpm_item)

        _apk = d.pop("apk", UNSET)
        apk: list[ArchitectureOption] | Unset = UNSET
        if _apk is not UNSET:
            apk = []
            for apk_item_data in _apk:
                apk_item = ArchitectureOption.from_dict(apk_item_data)

                apk.append(apk_item)

        _ipk = d.pop("ipk", UNSET)
        ipk: list[ArchitectureOption] | Unset = UNSET
        if _ipk is not UNSET:
            ipk = []
            for ipk_item_data in _ipk:
                ipk_item = ArchitectureOption.from_dict(ipk_item_data)

                ipk.append(ipk_item)

        architectures_by_package_type = cls(
            deb=deb,
            rpm=rpm,
            apk=apk,
            ipk=ipk,
        )

        architectures_by_package_type.additional_properties = d
        return architectures_by_package_type

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
