from collections import namedtuple

import pytest
from osmium import osm

from bssd.core import _base

RelationMember = namedtuple("RelationMember", "role, ref, type")


@pytest.fixture
def relation():
    return osm.mutable.Relation(tags={}, members=[])


def _test_tag(prop, relation, cls):
    relation.tags[prop] = prop
    p = getattr(cls, prop)

    assert p == prop


def _test_bool_tags(prop, relation, cls):
    relation.tags[prop] = "yes"
    p = getattr(cls, prop)

    assert p


def _test_members(prop, relation, cls):
    m = RelationMember(role=prop, ref=0, type="r")
    relation.members.append(m)
    p = [e for e in getattr(cls, prop)]

    assert len(p) == 1
    assert p[0] is m


class TestBehavior:

    @pytest.fixture
    def behavior(self, relation):
        return _base.BehaviorBase(relation)

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
        _test_members(prop, relation, behavior)


class TestBehaviorSpace:

    @pytest.fixture
    def behavior_space(self, relation):
        return _base.BehaviorSpaceBase(relation)

    @pytest.mark.parametrize("prop", [
        "lanelet",
        "along",
        "against",
    ])
    def test_members(self, prop, relation, behavior_space):
        _test_members(prop, relation, behavior_space)


class TestBoundaryLat:

    @pytest.fixture
    def boundary_lat(self, relation):
        return _base.BoundaryLatBase(relation)

    def test_crossing(self, relation, boundary_lat):
        relation.tags["crossing"] = "allowed"

        assert boundary_lat.crossing == "allowed"

    @pytest.mark.parametrize("prop", [
        "parking_only",
    ])
    def test_bool_tags(self, prop, relation, boundary_lat):
        _test_bool_tags(prop, relation, boundary_lat)

    @pytest.mark.parametrize("prop", [
        "boundary",
    ])
    def test_members(self, prop, relation, boundary_lat):
        _test_members(prop, relation, boundary_lat)


class TestBoundaryLong:

    @pytest.fixture
    def boundary_long(self, relation):
        return _base.BoundaryLongBase(relation)

    def test_crossing(self, relation, boundary_long):
        relation.tags["crossing"] = "allowed"

        assert boundary_long.crossing == "allowed"

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
        _test_members(prop, relation, boundary_long)


class TestReservation:

    @pytest.fixture
    def reservation(self, relation):
        return _base.ReservationBase(relation)

    def test_reservation_type(self, relation, reservation):
        relation.tags["reservation"] = "own"

        assert reservation.reservation == "own"

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
        _test_members(prop, relation, reservation)
