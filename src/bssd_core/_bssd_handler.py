from typing import Final

import osmium
from osmium import osm

from . import Behavior, BehaviorSpace, BoundaryLat, BoundaryLong, Reservation


class _Handler(osmium.SimpleHandler):

    def relation(self, r: osm.Relation):
        pass


class BSSDHandler:
    _tag_class = {
        "behavior": Behavior,
        "behavior_space": BehaviorSpace,
        "boundary_lat": BoundaryLat,
        "boundary_long": BoundaryLong,
        "reservation": Reservation,
        "relation": lambda x: x
    }

    def __init__(self):
        # todo: create function pointer map here
        self._handler: Final[_Handler] = _Handler()
        # patch methods
        self._handler.relation = self._relation
        self.apply_file = self._handler.apply_file
        self.apply_buffer = self._handler.apply_buffer

    def _relation(self, r: osm.Relation):
        if "type" not in r.tags:
            return

        t = r.tags["type"]
        if t not in BSSDHandler._tag_class:
            t = "relation"

        func = getattr(self, t, None)
        if func is not None:
            cls = BSSDHandler._tag_class[t]
            func(cls(r))

