from typing import Optional

from .relation import Relation
from .. import _base
from .._util import _to_yesno


class Behavior(Relation, _base.BehaviorBase):
    _type = "behavior"

    @_base.BehaviorBase.speed_max.setter
    def speed_max(self, f: Optional[float]):
        self._set_tag("speed_max", f)

    @_base.BehaviorBase.speed_time_max.setter
    def speed_time_max(self, f: Optional[float]):
        self._set_tag("speed_time_max", f)

    @_base.BehaviorBase.speed_wet_max.setter
    def speed_wet_max(self, f: Optional[float]):
        self._set_tag("speed_wet_max", f)

    @_base.BehaviorBase.overtake.setter
    def overtake(self, b: Optional[bool]):
        self._set_tag("overtake", _to_yesno(b))

    @_base.BehaviorBase.speed_time_interval.setter
    def speed_time_interval(self, s: Optional[str]):
        self._set_tag("speed_time_interval", s)

    def add_speed_indicator(self, ref: int):
        self._link_relation(ref, "speed_indicator")

    def add_overtake_indicator(self, ref: int):
        self._link_relation(ref, "overtake_indicator")

    def add_boundary_left(self, ref: int):
        self._link_relation(ref, "boundary_left")

    def add_boundary_right(self, ref: int):
        self._link_relation(ref, "boundary_right")

    def add_boundary_long(self, ref: int):
        self._link_relation(ref, "boundary_long")

    def add_reservation(self, ref: int):
        self._link_relation(ref, "reservation")
