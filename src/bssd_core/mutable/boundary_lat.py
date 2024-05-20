from typing import Union, Optional

from .relation import Relation
from .. import _base
from .._types import CrossingType
from .._util import _to_yesno


class BoundaryLat(Relation, _base.BoundaryLatBase):

    _type = "boundary_lat"

    def add_boundary(self, ref: int):
        self._link_way(ref, "boundary")

    @_base.BoundaryLatBase.crossing.setter
    def crossing(self, ct: Union[CrossingType, str, None]):
        if isinstance(ct, CrossingType):
            ct: str = ct.value
        self._set_tag("crossing", ct)

    @_base.BoundaryLatBase.parking_only.setter
    def parking_only(self, b: Optional[bool]):
        self._set_tag("parking_only", _to_yesno(b))
