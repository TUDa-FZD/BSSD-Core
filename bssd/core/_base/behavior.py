from typing import Optional, Iterator

from osmium import osm

from .. import _base
from .. import _interfaces as I


class BehaviorBase(_base.Relation, I.Behavior):

    @property
    def speed_max(self) -> Optional[float]:
        return self._get_tag("speed_max")

    @property
    def speed_time_max(self) -> Optional[float]:
        return self._get_tag("speed_time_max")

    @property
    def speed_wet_max(self) -> Optional[float]:
        return self._get_tag("speed_wet_max")

    @property
    def overtake(self) -> Optional[bool]:
        return self._get_yesno_tag("overtake")

    @property
    def speed_indicator(self) -> Iterator[osm.RelationMember]:
        """
        Returns an iterator of all members with the role "speed_indicator"
        """
        return self._find_roles("speed_indicator")

    @property
    def overtake_indicator(self) -> Iterator[osm.RelationMember]:
        """
        Returns an iterator of all members with the role "overtake_indicator"
        """
        return self._find_roles("overtake_indicator")

    # Todo: specify time interval format
    @property
    def speed_time_interval(self) -> Optional[str]:
        return self._get_tag("speed_time_interval")

    @property
    def boundary_left(self) -> Iterator[osm.RelationMember]:
        """
        Returns an iterator of all members with the role "boundary_left"
        """
        return self._find_roles("boundary_left")

    @property
    def boundary_right(self) -> Iterator[osm.RelationMember]:
        """
        Returns an iterator of all members with the role "boundary_right"
        """
        return self._find_roles("boundary_right")

    @property
    def boundary_long(self) -> Iterator[osm.RelationMember]:
        """
        Returns an iterator of all members with the role "boundary_long"
        """
        return self._find_roles("boundary_long")

    @property
    def reservation(self) -> Iterator[osm.RelationMember]:
        """
        Returns an iterator of all members with the role "reservation"
        """
        return self._find_roles("reservation")
