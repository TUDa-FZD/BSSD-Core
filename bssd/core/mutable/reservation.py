from typing import Union, Optional

from .relation import Relation
from .. import _base
from .._types import ReservationType
from .._util import _to_yesno


class Reservation(Relation, _base.ReservationBase):

    _type = "reservation"

    def add_link(self, ref: int):
        self._link_relation(ref, "link")

    @_base.ReservationBase.reservation.setter
    def reservation(self, rt: Union[ReservationType, str, None]):
        if isinstance(rt, ReservationType):
            rt: str = rt.value
        self._set_tag("reservation", rt)

    @_base.ReservationBase.pedestrian.setter
    def pedestrian(self, b: Optional[bool]):
        self._set_tag("pedestrian", _to_yesno(b))

    @_base.ReservationBase.bicycle.setter
    def bicycle(self, b: Optional[bool]):
        self._set_tag("bicycle", _to_yesno(b))

    @_base.ReservationBase.motor_vehicle.setter
    def motor_vehicle(self, b: Optional[bool]):
        self._set_tag("motor_vehicle", _to_yesno(b))

    @_base.ReservationBase.railed_vehicle.setter
    def railed_vehicle(self, b: Optional[bool]):
        self._set_tag("railed_vehicle", _to_yesno(b))

    @_base.ReservationBase.traffic_light_active.setter
    def traffic_light_active(self, b: Optional[bool]):
        self._set_tag("traffic_light_active", _to_yesno(b))

    @_base.ReservationBase.red_light_condition.setter
    def red_light_condition(self, b: Optional[bool]):
        self._set_tag("red_light_condition", _to_yesno(b))

    @_base.ReservationBase.turn_arrow_active.setter
    def turn_arrow_active(self, b: Optional[bool]):
        self._set_tag("turn_arrow_active", _to_yesno(b))
