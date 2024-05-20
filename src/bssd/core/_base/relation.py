from datetime import datetime
from typing import Optional, Union, Final, Iterator

from osmium import osm

from .. import CrossingType, ReservationType


class Relation:
    """
    Extends osm.Relation behaviour trough aggregation.
    """

    def __init__(self, relation: osm.Relation):
        self._data: Final[osm.Relation] = relation

    @property
    def id(self) -> Optional[int]:
        return self._data.id

    @property
    def version(self) -> Optional[int]:
        return self._data.version

    @property
    def visible(self) -> Optional[bool]:
        return self._data.visible

    @property
    def tags(self) -> osm.TagList:
        return self._data.tags

    @property
    def members(self) -> osm.RelationMemberList:
        return self._data.members

    @property
    def timestamp(self) -> Optional[datetime]:
        return self._data.timestamp

    @property
    def changeset(self) -> Optional[int]:
        return self._data.changeset

    @property
    def uid(self) -> Optional[int]:
        return self._data.uid

    @property
    def user(self) -> Optional[str]:
        return self._data.user

    def get_osmium(self) -> osm.Relation:
        return self._data

    def _tag_to_crossing(self, s: str) -> Optional[CrossingType]:
        try:
            return CrossingType(self.tags[s])
        except (ValueError, KeyError):
            return None

    def _tag_to_reservation(self, s: str) -> Optional[ReservationType]:
        try:
            return ReservationType(self.tags[s])
        except (ValueError, KeyError):
            return None

    def _find_roles(self, role: str) -> Iterator[osm.RelationMember]:
        return (m for m in self.members if m.role == role)

    def _get_tag(self, k: str) -> Optional[Union[str, int, float]]:
        return self.tags[k] if k in self.tags else None

    def _get_yesno_tag(self, k: str) -> Optional[bool]:
        if k not in self.tags:
            return None

        return self.tags[k] == "yes"
