from typing import Iterator, Optional

from osmium import osm

from .. import _base
from .. import _interfaces as I


class BoundaryLongBase(_base.Relation, I.BoundaryLong):

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
    def traffic_light_active(self) -> Optional[bool]:
        return self._get_yesno_tag("traffic_light_active")

    @property
    def red_light_condition(self) -> Optional[bool]:
        return self._get_yesno_tag("red_light_condition")

    @property
    def stop(self) -> Optional[bool]:
        return self._get_yesno_tag("stop")

    @property
    def no_stagnant_traffic(self) -> Optional[bool]:
        return self._get_yesno_tag("no_stagnant_traffic")

    @property
    def no_red_light(self) -> Optional[bool]:
        return self._get_yesno_tag("no_red_light")

    @property
    def residents_only(self) -> Optional[bool]:
        return self._get_yesno_tag("residents_only")

    @property
    def time_interval_only(self) -> Optional[bool]:
        return self._get_yesno_tag("time_interval_only")
