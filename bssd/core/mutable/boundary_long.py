from typing import Union, Optional

from .relation import Relation
from .. import _base
from .._types import CrossingType
from .._util import _to_yesno


class BoundaryLong(Relation, _base.BoundaryLongBase):

    _type = "boundary_long"

    def add_boundary(self, ref: int):
        self._link_way(ref, "boundary")

    @_base.BoundaryLongBase.crossing.setter
    def crossing(self, ct: Union[CrossingType, str, None]):
        if isinstance(ct, CrossingType):
            ct: str = ct.value
        self._set_tag("crossing", ct)

    @_base.BoundaryLongBase.traffic_light_active.setter
    def traffic_light_active(self, b: Optional[bool]):
        self._set_tag("traffic_light_active", _to_yesno(b))

    @_base.BoundaryLongBase.red_light_condition.setter
    def red_light_condition(self, b: Optional[bool]):
        self._set_tag("red_light_condition", _to_yesno(b))

    @_base.BoundaryLongBase.stop.setter
    def stop(self, b: Optional[bool]):
        self._set_tag("stop", _to_yesno(b))

    @_base.BoundaryLongBase.no_stagnant_traffic.setter
    def no_stagnant_traffic(self, b: Optional[bool]):
        self._set_tag("no_stagnant_traffic", _to_yesno(b))

    @_base.BoundaryLongBase.no_red_light.setter
    def no_red_light(self, b: Optional[bool]):
        self._set_tag("no_red_light", _to_yesno(b))

    @_base.BoundaryLongBase.residents_only.setter
    def residents_only(self, b: Optional[bool]):
        self._set_tag("residents_only", _to_yesno(b))

    @_base.BoundaryLongBase.time_interval_only.setter
    def time_interval_only(self, b: Optional[bool]):
        self._set_tag("time_interval_only", _to_yesno(b))
