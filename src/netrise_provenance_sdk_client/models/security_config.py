from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SecurityConfig")


@_attrs_define
class SecurityConfig:
    """
    Attributes:
        security_md_exists (bool):
        has_security_advisories (bool):
        security_advisory_count (int):
        dependabot_alerts_enabled (bool):
        has_ci_workflows (bool):
    """

    security_md_exists: bool
    has_security_advisories: bool
    security_advisory_count: int
    dependabot_alerts_enabled: bool
    has_ci_workflows: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        security_md_exists = self.security_md_exists

        has_security_advisories = self.has_security_advisories

        security_advisory_count = self.security_advisory_count

        dependabot_alerts_enabled = self.dependabot_alerts_enabled

        has_ci_workflows = self.has_ci_workflows

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "security_md_exists": security_md_exists,
                "has_security_advisories": has_security_advisories,
                "security_advisory_count": security_advisory_count,
                "dependabot_alerts_enabled": dependabot_alerts_enabled,
                "has_ci_workflows": has_ci_workflows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        security_md_exists = d.pop("security_md_exists")

        has_security_advisories = d.pop("has_security_advisories")

        security_advisory_count = d.pop("security_advisory_count")

        dependabot_alerts_enabled = d.pop("dependabot_alerts_enabled")

        has_ci_workflows = d.pop("has_ci_workflows")

        security_config = cls(
            security_md_exists=security_md_exists,
            has_security_advisories=has_security_advisories,
            security_advisory_count=security_advisory_count,
            dependabot_alerts_enabled=dependabot_alerts_enabled,
            has_ci_workflows=has_ci_workflows,
        )

        security_config.additional_properties = d
        return security_config

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
