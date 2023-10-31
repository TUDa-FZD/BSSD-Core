from abc import ABC, abstractmethod
from typing import Iterator, Optional

from osmium import osm

from .._types import CrossingType


class BoundaryLat(ABC):

    @property
    @abstractmethod
    def boundary(self) -> Iterator[osm.RelationMember]:
        pass

    @property
    @abstractmethod
    def crossing(self) -> Optional[CrossingType]:
        pass

    @property
    @abstractmethod
    def parking_only(self) -> Optional[bool]:
        pass
