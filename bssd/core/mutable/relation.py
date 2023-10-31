import abc
from datetime import datetime
from typing import Optional

from osmium import osm

from .. import _base
from .._types import Member


class Relation(_base.Relation, metaclass=abc.ABCMeta):

    def __init__(self, relation: osm.Relation = None):
        # todo: add from classmethods
        if relation is None:
            relation = osm.mutable.Relation(tags={"type": self._type}, members=[])
        elif isinstance(relation, osm.Relation):
            relation = relation.replace(tags={k: v for k, v in relation.tags})

        _base.Relation.__init__(self, relation)

    @property
    @abc.abstractmethod
    def _type(self) -> str:
        pass

    def _set_tag(self, k: str, v: any):
        self.tags[k] = v

    def _link_relation(self, ref: int, role: str):
        self.members.append(Member(ref=ref, role=role, type="r"))

    def _link_way(self, ref: int, role: str):
        self.members.append(Member(ref=ref, role=role, type="w"))

    # without redefinition pycharm will show false positive warnings
    # for missing setters or getters
    @property
    def id(self) -> Optional[int]:
        return _base.Relation.id.fget(self)

    @id.setter
    def id(self, i: int):
        self._data.id = i

    @property
    def version(self) -> Optional[int]:
        return _base.Relation.version.fget(self)

    @version.setter
    def version(self, i: int):
        self._data.version = i

    @property
    def visible(self) -> Optional[bool]:
        return _base.Relation.visible.fget(self)

    @visible.setter
    def visible(self, b: bool):
        self._data.visible = b

    @property
    def timestamp(self) -> Optional[datetime]:
        return _base.Relation.timestamp.fget(self)

    @timestamp.setter
    def timestamp(self, dt: Optional[datetime]):
        self._data.timestamp = dt

    @property
    def changeset(self) -> Optional[int]:
        return _base.Relation.changeset.fget(self)

    @changeset.setter
    def changeset(self, i: Optional[int]):
        self._data.changeset = i

    @property
    def uid(self) -> Optional[int]:
        return _base.Relation.uid.fget(self)

    @uid.setter
    def uid(self, i: Optional[int]):
        self._data.uid = i

    @property
    def user(self) -> Optional[str]:
        return _base.Relation.user.fget(self)

    @user.setter
    def user(self, s: Optional[str]):
        self._data.user = s
