from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity import Activity
    from ..models.code_hygiene import CodeHygiene
    from ..models.contributor_risk import ContributorRisk
    from ..models.metadata import Metadata
    from ..models.popularity import Popularity
    from ..models.scorecard_type_0 import ScorecardType0
    from ..models.security_config import SecurityConfig


T = TypeVar("T", bound="RepositoryHealth")


@_attrs_define
class RepositoryHealth:
    """
    Attributes:
        popularity (Popularity):
        activity (Activity):
        security_config (SecurityConfig):
        contributor_risk (ContributorRisk):
        code_hygiene (CodeHygiene):
        metadata (Metadata):
        scorecard (None | ScorecardType0 | Unset): Null if the repository has not been scanned by OpenSSF Scorecard
        repo_health_last_checked (datetime.datetime | None | Unset): When the GitHub scraper last refreshed repository
            metadata used for this health snapshot (null if never looked up)
    """

    popularity: Popularity
    activity: Activity
    security_config: SecurityConfig
    contributor_risk: ContributorRisk
    code_hygiene: CodeHygiene
    metadata: Metadata
    scorecard: None | ScorecardType0 | Unset = UNSET
    repo_health_last_checked: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.scorecard_type_0 import ScorecardType0

        popularity = self.popularity.to_dict()

        activity = self.activity.to_dict()

        security_config = self.security_config.to_dict()

        contributor_risk = self.contributor_risk.to_dict()

        code_hygiene = self.code_hygiene.to_dict()

        metadata = self.metadata.to_dict()

        scorecard: dict[str, Any] | None | Unset
        if isinstance(self.scorecard, Unset):
            scorecard = UNSET
        elif isinstance(self.scorecard, ScorecardType0):
            scorecard = self.scorecard.to_dict()
        else:
            scorecard = self.scorecard

        repo_health_last_checked: None | str | Unset
        if isinstance(self.repo_health_last_checked, Unset):
            repo_health_last_checked = UNSET
        elif isinstance(self.repo_health_last_checked, datetime.datetime):
            repo_health_last_checked = self.repo_health_last_checked.isoformat()
        else:
            repo_health_last_checked = self.repo_health_last_checked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "popularity": popularity,
                "activity": activity,
                "security_config": security_config,
                "contributor_risk": contributor_risk,
                "code_hygiene": code_hygiene,
                "metadata": metadata,
            }
        )
        if scorecard is not UNSET:
            field_dict["scorecard"] = scorecard
        if repo_health_last_checked is not UNSET:
            field_dict["repo_health_last_checked"] = repo_health_last_checked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity import Activity
        from ..models.code_hygiene import CodeHygiene
        from ..models.contributor_risk import ContributorRisk
        from ..models.metadata import Metadata
        from ..models.popularity import Popularity
        from ..models.scorecard_type_0 import ScorecardType0
        from ..models.security_config import SecurityConfig

        d = dict(src_dict)
        popularity = Popularity.from_dict(d.pop("popularity"))

        activity = Activity.from_dict(d.pop("activity"))

        security_config = SecurityConfig.from_dict(d.pop("security_config"))

        contributor_risk = ContributorRisk.from_dict(d.pop("contributor_risk"))

        code_hygiene = CodeHygiene.from_dict(d.pop("code_hygiene"))

        metadata = Metadata.from_dict(d.pop("metadata"))

        def _parse_scorecard(data: object) -> None | ScorecardType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_scorecard_type_0 = ScorecardType0.from_dict(data)

                return componentsschemas_scorecard_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ScorecardType0 | Unset, data)

        scorecard = _parse_scorecard(d.pop("scorecard", UNSET))

        def _parse_repo_health_last_checked(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repo_health_last_checked_type_0 = isoparse(data)

                return repo_health_last_checked_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        repo_health_last_checked = _parse_repo_health_last_checked(
            d.pop("repo_health_last_checked", UNSET)
        )

        repository_health = cls(
            popularity=popularity,
            activity=activity,
            security_config=security_config,
            contributor_risk=contributor_risk,
            code_hygiene=code_hygiene,
            metadata=metadata,
            scorecard=scorecard,
            repo_health_last_checked=repo_health_last_checked,
        )

        repository_health.additional_properties = d
        return repository_health

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
