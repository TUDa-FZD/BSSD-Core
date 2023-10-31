from typing import Iterator, Optional

from osmium import osm

from .. import _base
from .. import _interfaces as I


class BoundaryLatBase(_base.Relation, I.BoundaryLat):

    @property
    def boundary(self) -> Iterator[osm.RelationMember]:
        """
        Returns an iterator of all members with the role "boundary"
        """
        return self._find_roles("boundary")

    @property
    def crossing(self) -> Optional[str]:
        return self._get_tag("crossing")

    @property
    def parking_only(self) -> Optional[bool]:
        return self._get_yesno_tag("parking_only")
