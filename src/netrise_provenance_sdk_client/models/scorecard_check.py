from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scorecard_check_risk import ScorecardCheckRisk

T = TypeVar("T", bound="ScorecardCheck")


@_attrs_define
class ScorecardCheck:
    """
    Attributes:
        name (str): Check name (e.g., Code-Review, Branch-Protection)
        score (int):
        reason (str): Human-readable explanation of the score
        risk (ScorecardCheckRisk):
    """

    name: str
    score: int
    reason: str
    risk: ScorecardCheckRisk
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        score = self.score

        reason = self.reason

        risk = self.risk.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "score": score,
                "reason": reason,
                "risk": risk,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        score = d.pop("score")

        reason = d.pop("reason")

        risk = ScorecardCheckRisk(d.pop("risk"))

        scorecard_check = cls(
            name=name,
            score=score,
            reason=reason,
            risk=risk,
        )

        scorecard_check.additional_properties = d
        return scorecard_check

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
