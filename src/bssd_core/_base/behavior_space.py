from typing import Iterator

from osmium import osm

from .. import _base
from .. import _interfaces as I


class BehaviorSpaceBase(_base.Relation, I.BehaviorSpace):

    @property
    def lanelet(self) -> Iterator[osm.RelationMember]:
        """
        Returns an iterator of all members with the role "lanelet"
        """
        return self._find_roles("lanelet")

    @property
    def along(self) -> Iterator[osm.RelationMember]:
        """
        Returns an iterator of all members with the role "along"
        """
        return self._find_roles("along")

    @property
    def against(self) -> Iterator[osm.RelationMember]:
        """
        Returns an iterator of all members with the role "against"
        """
        return self._find_roles("against")
