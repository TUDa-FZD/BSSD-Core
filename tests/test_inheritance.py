from typing import List

import pytest
import bssd.core as core
from bssd.core import _base, mutable, _interfaces


def test_make_mutable_inherits_from_relation():
    assert issubclass(_base.MakeMutable, _base.Relation)


def test_mutable_relation_inherits_from_relation():
    assert issubclass(mutable.Relation, _base.Relation)


@pytest.mark.parametrize("cls", [
    "Behavior",
    "BehaviorSpace",
    "BoundaryLong",
    "BoundaryLat",
    "Reservation"
])
class TestClasses:
    def test_base_inherits_from_relation(self, cls):
        b = getattr(_base, cls + "Base")
        assert issubclass(b, _base.Relation)

    def test_base_implements_interface(self, cls):
        b = getattr(_base, cls + "Base")
        i = getattr(_interfaces, cls)

        assert issubclass(b, i)

    def test_immutables_inherit_from_make_mutable(self, cls):
        i = getattr(core, cls)

        assert issubclass(i, _base.MakeMutable)

    def test_mutable_mro_order(self, cls):
        b = getattr(_base, cls + "Base")
        m: List[type] = getattr(mutable, cls).mro()

        # first is the class itself
        # second should be mutable.Relation
        # third should be its own class from the module _base
        assert m[1] == mutable.Relation
        assert m[2] == b
