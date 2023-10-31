from typing import Optional, Iterator

from osmium import osm

from .. import _base
from .. import _interfaces as I


class ReservationBase(_base.Relation, I.Reservation):

    @property
    def reservation(self) -> Optional[str]:
        return self._get_tag("reservation")

    @property
    def link(self) -> Iterator[osm.RelationMember]:
        """
        Returns an iterator of all members with the role "link"
        """
        return self._find_roles("link")

    @property
    def pedestrian(self) -> Optional[bool]:
        return self._get_yesno_tag("pedestrian")

    @property
    def bicycle(self) -> Optional[bool]:
        return self._get_yesno_tag("bicycle")

    @property
    def motor_vehicle(self) -> Optional[bool]:
        return self._get_yesno_tag("motor_vehicle")

    @property
    def railed_vehicle(self) -> Optional[bool]:
        return self._get_yesno_tag("railed_vehicle")

    @property
    def traffic_light_active(self) -> Optional[bool]:
        return self._get_yesno_tag("traffic_light_active")

    @property
    def red_light_condition(self) -> Optional[bool]:
        return self._get_yesno_tag("red_light_condition")

    @property
    def turn_arrow_active(self) -> Optional[bool]:
        return self._get_yesno_tag("turn_arrow_active")

