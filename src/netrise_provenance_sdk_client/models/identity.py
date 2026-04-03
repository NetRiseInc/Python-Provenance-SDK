from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Identity")


@_attrs_define
class Identity:
    """
    Attributes:
        declared_names (list[str]):
        emails (list[str] | Unset):
        usernames (list[str] | Unset):
    """

    declared_names: list[str]
    emails: list[str] | Unset = UNSET
    usernames: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        declared_names = self.declared_names

        emails: list[str] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        usernames: list[str] | Unset = UNSET
        if not isinstance(self.usernames, Unset):
            usernames = self.usernames

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "declared_names": declared_names,
            }
        )
        if emails is not UNSET:
            field_dict["emails"] = emails
        if usernames is not UNSET:
            field_dict["usernames"] = usernames

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        declared_names = cast(list[str], d.pop("declared_names"))

        emails = cast(list[str], d.pop("emails", UNSET))

        usernames = cast(list[str], d.pop("usernames", UNSET))

        identity = cls(
            declared_names=declared_names,
            emails=emails,
            usernames=usernames,
        )

        identity.additional_properties = d
        return identity

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
