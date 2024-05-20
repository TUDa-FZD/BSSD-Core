import pytest
from osmium import osm

from bssd.core import mutable


@pytest.fixture
def osm_relation():
    return osm.mutable.Relation(tags={}, members=[])


@pytest.fixture
def relation(osm_relation) -> mutable.Relation:
    class R(mutable.Relation):
        _roles = []
        _type = ""
    return R(osm_relation)


@pytest.mark.parametrize("prop", [
    "visible",
    "id",
    "version",
    "timestamp",
    "user",
    "uid",
    "changeset"
])
def test_mutable(osm_relation, relation, prop):
    setattr(relation, prop, prop)
    p = getattr(osm_relation, prop)

    assert p == prop
