from .relation import Relation
from .. import _base


class BehaviorSpace(Relation, _base.BehaviorSpaceBase):

    _type = "behavior_space"

    def add_lanelet(self, ref: int):
        self._link_relation(ref, "lanelet")

    def add_along(self, ref: int):
        self._link_relation(ref, "along")

    def add_against(self, ref: int):
        self._link_relation(ref, "against")
