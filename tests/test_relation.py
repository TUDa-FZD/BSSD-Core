from typing import Tuple

import pytest
from osmium import osm

from bssd.core import _base


@pytest.fixture
def relation() -> Tuple[_base.Relation, osm.Relation]:
    r = osm.mutable.Relation()
    return _base.Relation(r), r


@pytest.mark.parametrize("prop", [
    "visible",
    "id",
    "version",
    "timestamp",
    "user",
    "uid",
    "changeset"
])
class TestProperties:
    def test_none(self, relation, prop):
        r1, r2 = relation
        p1 = getattr(r1, prop)
        p2 = getattr(r2, prop)

        assert p1 is p2 is None

    def test_getter(self, relation, prop):
        r1, r2 = relation
        setattr(r2, prop, prop)
        p1 = getattr(r1, prop)
        p2 = getattr(r2, prop)

        assert p1 == p2 == prop

    def test_immutable(self, relation, prop):
        with pytest.raises(AttributeError):
            setattr(relation, prop, prop)


def test_get_osmium(relation):
    r1: _base.Relation
    r1, r2 = relation

    assert r1.get_osmium() is r2
