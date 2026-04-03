from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_frequency import CommitFrequency


T = TypeVar("T", bound="Activity")


@_attrs_define
class Activity:
    """
    Attributes:
        last_commit_date (datetime.datetime):
        commit_frequency (CommitFrequency):
        is_archived (bool):
        is_deprecated (bool): True if repository topics or README indicate unmaintained/deprecated status
        open_issues_count (int):
        issue_close_rate_180d (float): Ratio of issues closed to issues opened in the last 180 days (0.0-1.0)
        open_pr_count (int):
        pr_merge_rate_180d (float): Ratio of PRs merged to PRs opened in the last 180 days (0.0-1.0)
        has_readme (bool): True if README exists and is non-trivial (> 100 bytes)
        has_changelog (bool):
        last_release_date (datetime.datetime | None | Unset): Null if the repository has never published a release
        release_cadence_days (float | None | Unset): Average days between releases over trailing 12 months. Null if
            fewer than 2 releases.
    """

    last_commit_date: datetime.datetime
    commit_frequency: CommitFrequency
    is_archived: bool
    is_deprecated: bool
    open_issues_count: int
    issue_close_rate_180d: float
    open_pr_count: int
    pr_merge_rate_180d: float
    has_readme: bool
    has_changelog: bool
    last_release_date: datetime.datetime | None | Unset = UNSET
    release_cadence_days: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_commit_date = self.last_commit_date.isoformat()

        commit_frequency = self.commit_frequency.to_dict()

        is_archived = self.is_archived

        is_deprecated = self.is_deprecated

        open_issues_count = self.open_issues_count

        issue_close_rate_180d = self.issue_close_rate_180d

        open_pr_count = self.open_pr_count

        pr_merge_rate_180d = self.pr_merge_rate_180d

        has_readme = self.has_readme

        has_changelog = self.has_changelog

        last_release_date: None | str | Unset
        if isinstance(self.last_release_date, Unset):
            last_release_date = UNSET
        elif isinstance(self.last_release_date, datetime.datetime):
            last_release_date = self.last_release_date.isoformat()
        else:
            last_release_date = self.last_release_date

        release_cadence_days: float | None | Unset
        if isinstance(self.release_cadence_days, Unset):
            release_cadence_days = UNSET
        else:
            release_cadence_days = self.release_cadence_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last_commit_date": last_commit_date,
                "commit_frequency": commit_frequency,
                "is_archived": is_archived,
                "is_deprecated": is_deprecated,
                "open_issues_count": open_issues_count,
                "issue_close_rate_180d": issue_close_rate_180d,
                "open_pr_count": open_pr_count,
                "pr_merge_rate_180d": pr_merge_rate_180d,
                "has_readme": has_readme,
                "has_changelog": has_changelog,
            }
        )
        if last_release_date is not UNSET:
            field_dict["last_release_date"] = last_release_date
        if release_cadence_days is not UNSET:
            field_dict["release_cadence_days"] = release_cadence_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit_frequency import CommitFrequency

        d = dict(src_dict)
        last_commit_date = isoparse(d.pop("last_commit_date"))

        commit_frequency = CommitFrequency.from_dict(d.pop("commit_frequency"))

        is_archived = d.pop("is_archived")

        is_deprecated = d.pop("is_deprecated")

        open_issues_count = d.pop("open_issues_count")

        issue_close_rate_180d = d.pop("issue_close_rate_180d")

        open_pr_count = d.pop("open_pr_count")

        pr_merge_rate_180d = d.pop("pr_merge_rate_180d")

        has_readme = d.pop("has_readme")

        has_changelog = d.pop("has_changelog")

        def _parse_last_release_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_release_date_type_0 = isoparse(data)

                return last_release_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_release_date = _parse_last_release_date(d.pop("last_release_date", UNSET))

        def _parse_release_cadence_days(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        release_cadence_days = _parse_release_cadence_days(
            d.pop("release_cadence_days", UNSET)
        )

        activity = cls(
            last_commit_date=last_commit_date,
            commit_frequency=commit_frequency,
            is_archived=is_archived,
            is_deprecated=is_deprecated,
            open_issues_count=open_issues_count,
            issue_close_rate_180d=issue_close_rate_180d,
            open_pr_count=open_pr_count,
            pr_merge_rate_180d=pr_merge_rate_180d,
            has_readme=has_readme,
            has_changelog=has_changelog,
            last_release_date=last_release_date,
            release_cadence_days=release_cadence_days,
        )

        activity.additional_properties = d
        return activity

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
