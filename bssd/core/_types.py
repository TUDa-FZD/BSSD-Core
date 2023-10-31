from enum import Enum
from typing import NamedTuple


class Member(NamedTuple):
    type: str
    ref: int
    role: str


class Role(Enum):
    NODE = "n"
    WAY = "w"
    RELATION = "r"


class ReservationType(Enum):
    OWN = "own"
    EXTERNALLY = "externally"
    EQUALLY = "equally"


class CrossingType(Enum):
    ALLOWED = "allowed"
    CONDITIONAL = "conditional"
    PROHIBITED = "prohibited"
    NOT_POSSIBLE = "not_possible"
