from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Popularity")


@_attrs_define
class Popularity:
    """
    Attributes:
        star_count (int):
        fork_count (int):
        watcher_count (int):
        dependent_repo_count (int):
        contributor_count (int): All-time contributor count
        active_contributor_count_12mo (int): Contributors with commits in the last 12 months
    """

    star_count: int
    fork_count: int
    watcher_count: int
    dependent_repo_count: int
    contributor_count: int
    active_contributor_count_12mo: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        star_count = self.star_count

        fork_count = self.fork_count

        watcher_count = self.watcher_count

        dependent_repo_count = self.dependent_repo_count

        contributor_count = self.contributor_count

        active_contributor_count_12mo = self.active_contributor_count_12mo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "star_count": star_count,
                "fork_count": fork_count,
                "watcher_count": watcher_count,
                "dependent_repo_count": dependent_repo_count,
                "contributor_count": contributor_count,
                "active_contributor_count_12mo": active_contributor_count_12mo,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        star_count = d.pop("star_count")

        fork_count = d.pop("fork_count")

        watcher_count = d.pop("watcher_count")

        dependent_repo_count = d.pop("dependent_repo_count")

        contributor_count = d.pop("contributor_count")

        active_contributor_count_12mo = d.pop("active_contributor_count_12mo")

        popularity = cls(
            star_count=star_count,
            fork_count=fork_count,
            watcher_count=watcher_count,
            dependent_repo_count=dependent_repo_count,
            contributor_count=contributor_count,
            active_contributor_count_12mo=active_contributor_count_12mo,
        )

        popularity.additional_properties = d
        return popularity

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
