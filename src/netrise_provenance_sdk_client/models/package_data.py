from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advisory_attribution import AdvisoryAttribution
    from ..models.metadata import Metadata
    from ..models.package_data_dependencies_item import PackageDataDependenciesItem
    from ..models.package_data_package_details import PackageDataPackageDetails
    from ..models.package_data_repository_details import PackageDataRepositoryDetails


T = TypeVar("T", bound="PackageData")


@_attrs_define
class PackageData:
    """
    Attributes:
        package_type (str):
        vendor (str):
        product (str):
        version (str):
        package_details (PackageDataPackageDetails):
        metadata (Metadata):
        arch (str | Unset):
        distro (str | Unset):
        repository_details (PackageDataRepositoryDetails | Unset):
        advisories (list[AdvisoryAttribution] | Unset):
        dependencies (list[PackageDataDependenciesItem] | Unset):
    """

    package_type: str
    vendor: str
    product: str
    version: str
    package_details: PackageDataPackageDetails
    metadata: Metadata
    arch: str | Unset = UNSET
    distro: str | Unset = UNSET
    repository_details: PackageDataRepositoryDetails | Unset = UNSET
    advisories: list[AdvisoryAttribution] | Unset = UNSET
    dependencies: list[PackageDataDependenciesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_type = self.package_type

        vendor = self.vendor

        product = self.product

        version = self.version

        package_details = self.package_details.to_dict()

        metadata = self.metadata.to_dict()

        arch = self.arch

        distro = self.distro

        repository_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository_details, Unset):
            repository_details = self.repository_details.to_dict()

        advisories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.advisories, Unset):
            advisories = []
            for componentsschemas_advisories_attributed_item_data in self.advisories:
                componentsschemas_advisories_attributed_item = (
                    componentsschemas_advisories_attributed_item_data.to_dict()
                )
                advisories.append(componentsschemas_advisories_attributed_item)

        dependencies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = []
            for dependencies_item_data in self.dependencies:
                dependencies_item = dependencies_item_data.to_dict()
                dependencies.append(dependencies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package_type": package_type,
                "vendor": vendor,
                "product": product,
                "version": version,
                "package_details": package_details,
                "metadata": metadata,
            }
        )
        if arch is not UNSET:
            field_dict["arch"] = arch
        if distro is not UNSET:
            field_dict["distro"] = distro
        if repository_details is not UNSET:
            field_dict["repository_details"] = repository_details
        if advisories is not UNSET:
            field_dict["advisories"] = advisories
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisory_attribution import AdvisoryAttribution
        from ..models.metadata import Metadata
        from ..models.package_data_dependencies_item import PackageDataDependenciesItem
        from ..models.package_data_package_details import PackageDataPackageDetails
        from ..models.package_data_repository_details import (
            PackageDataRepositoryDetails,
        )

        d = dict(src_dict)
        package_type = d.pop("package_type")

        vendor = d.pop("vendor")

        product = d.pop("product")

        version = d.pop("version")

        package_details = PackageDataPackageDetails.from_dict(d.pop("package_details"))

        metadata = Metadata.from_dict(d.pop("metadata"))

        arch = d.pop("arch", UNSET)

        distro = d.pop("distro", UNSET)

        _repository_details = d.pop("repository_details", UNSET)
        repository_details: PackageDataRepositoryDetails | Unset
        if isinstance(_repository_details, Unset):
            repository_details = UNSET
        else:
            repository_details = PackageDataRepositoryDetails.from_dict(
                _repository_details
            )

        _advisories = d.pop("advisories", UNSET)
        advisories: list[AdvisoryAttribution] | Unset = UNSET
        if _advisories is not UNSET:
            advisories = []
            for componentsschemas_advisories_attributed_item_data in _advisories:
                componentsschemas_advisories_attributed_item = (
                    AdvisoryAttribution.from_dict(
                        componentsschemas_advisories_attributed_item_data
                    )
                )

                advisories.append(componentsschemas_advisories_attributed_item)

        _dependencies = d.pop("dependencies", UNSET)
        dependencies: list[PackageDataDependenciesItem] | Unset = UNSET
        if _dependencies is not UNSET:
            dependencies = []
            for dependencies_item_data in _dependencies:
                dependencies_item = PackageDataDependenciesItem.from_dict(
                    dependencies_item_data
                )

                dependencies.append(dependencies_item)

        package_data = cls(
            package_type=package_type,
            vendor=vendor,
            product=product,
            version=version,
            package_details=package_details,
            metadata=metadata,
            arch=arch,
            distro=distro,
            repository_details=repository_details,
            advisories=advisories,
            dependencies=dependencies,
        )

        package_data.additional_properties = d
        return package_data

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
