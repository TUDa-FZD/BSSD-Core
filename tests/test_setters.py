from collections import namedtuple

import pytest
from osmium import osm

from bssd.core import CrossingType
from bssd.core import mutable, ReservationType

RelationMember = namedtuple("RelationMember", "role, ref, type")


@pytest.fixture
def relation():
    return osm.mutable.Relation(tags={}, members=[])


def _test_tag(prop, relation, cls):
    setattr(cls, prop, prop)
    p = relation.tags[prop]

    assert p == prop


def _test_bool_tags(prop, relation, cls):
    setattr(cls, prop, True)
    assert relation.tags[prop] == "yes"
    setattr(cls, prop, False)
    assert relation.tags[prop] == "no"


def _test_add_members(prop, obj):
    getattr(obj, f"add_{prop}")(prop)
    p = obj.members

    assert len(p) == 1
    assert p[0].ref == prop
    assert p[0].role == prop


class TestBehavior:

    @pytest.fixture
    def behavior(self, relation):
        return mutable.Behavior(relation)

    @pytest.mark.parametrize("prop", [
        "speed_max",
        "speed_time_max",
        "speed_wet_max",
        "speed_time_interval"
    ])
    def test_behavior_tags(self, prop, relation, behavior):
        _test_tag(prop, relation, behavior)

    @pytest.mark.parametrize("prop", [
        "overtake",
    ])
    def test_bool_tags(self, prop, relation, behavior):
        _test_bool_tags(prop, relation, behavior)

    @pytest.mark.parametrize("prop", [
        "speed_indicator",
        "overtake_indicator",
        "boundary_left",
        "boundary_right",
        "boundary_long",
        "reservation",
    ])
    def test_members(self, prop, relation, behavior):
        _test_add_members(prop, behavior)


class TestBehaviorSpace:

    @pytest.fixture
    def behavior_space(self, relation):
        return mutable.BehaviorSpace(relation)

    @pytest.mark.parametrize("prop", [
        "lanelet",
        "along",
        "against",
    ])
    def test_members(self, prop, relation, behavior_space):
        _test_add_members(prop, behavior_space)


class TestBoundaryLat:

    @pytest.fixture
    def boundary_lat(self, relation):
        return mutable.BoundaryLat(relation)

    @pytest.mark.parametrize("values", [
        (None, None),
        ("allowed", "allowed"),
        (CrossingType.ALLOWED, CrossingType.ALLOWED.value)
    ])
    def test_crossing(self, relation, boundary_lat, values):
        v1, v2 = values
        boundary_lat.crossing = v1

        assert relation.tags["crossing"] == v2

    @pytest.mark.parametrize("prop", [
        "parking_only",
    ])
    def test_bool_tags(self, prop, relation, boundary_lat):
        _test_bool_tags(prop, relation, boundary_lat)

    @pytest.mark.parametrize("prop", [
        "boundary",
    ])
    def test_members(self, prop, relation, boundary_lat):
        _test_add_members(prop, boundary_lat)


class TestBoundaryLong:

    @pytest.fixture
    def boundary_long(self, relation):
        return mutable.BoundaryLong(relation)

    @pytest.mark.parametrize("values", [
        (None, None),
        ("allowed", "allowed"),
        (CrossingType.ALLOWED, CrossingType.ALLOWED.value)
    ])
    def test_crossing(self, relation, boundary_long, values):
        v1, v2 = values
        boundary_long.crossing = v1

        assert relation.tags["crossing"] == v2

    @pytest.mark.parametrize("prop", [
        "traffic_light_active",
        "red_light_condition",
        "stop",
        "no_stagnant_traffic",
        "no_red_light",
        "residents_only",
        "time_interval_only"
    ])
    def test_bool_tags(self, prop, relation, boundary_long):
        _test_bool_tags(prop, relation, boundary_long)

    @pytest.mark.parametrize("prop", [
        "boundary",
    ])
    def test_members(self, prop, relation, boundary_long):
        _test_add_members(prop, boundary_long)


class TestReservation:

    @pytest.fixture
    def reservation(self, relation):
        return mutable.Reservation(relation)

    @pytest.mark.parametrize("values", [
        (None, None),
        ("own", "own"),
        (ReservationType.OWN, ReservationType.OWN.value)
    ])
    def test_reservation_type(self, relation, reservation, values):
        v1, v2 = values
        reservation.reservation = v1

        assert relation.tags["reservation"] == v2

    @pytest.mark.parametrize("prop", [
        "pedestrian",
        "bicycle",
        "motor_vehicle",
        "railed_vehicle",
        "traffic_light_active",
        "red_light_condition",
        "turn_arrow_active"
    ])
    def test_bool_tags(self, prop, relation, reservation):
        _test_bool_tags(prop, relation, reservation)

    @pytest.mark.parametrize("prop", [
        "link",
    ])
    def test_members(self, prop, relation, reservation):
        _test_add_members(prop, reservation)
