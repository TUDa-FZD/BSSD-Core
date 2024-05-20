from . import _base


class Behavior(_base.BehaviorBase, _base.MakeMutable):
    pass


class BehaviorSpace(_base.BehaviorSpaceBase, _base.MakeMutable):
    pass


class Reservation(_base.ReservationBase, _base.MakeMutable):
    pass


class BoundaryLat(_base.BoundaryLatBase, _base.MakeMutable):
    pass


class BoundaryLong(_base.BoundaryLongBase, _base.MakeMutable):
    pass
