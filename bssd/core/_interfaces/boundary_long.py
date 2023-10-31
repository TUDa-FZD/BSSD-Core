from abc import ABC, abstractmethod
from typing import Iterator, Optional

from osmium import osm

from .._types import CrossingType


class BoundaryLong(ABC):

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
    def traffic_light_active(self) -> Optional[bool]:
        pass

    @property
    @abstractmethod
    def red_light_condition(self) -> Optional[bool]:
        pass

    @property
    @abstractmethod
    def stop(self) -> Optional[bool]:
        pass

    @property
    @abstractmethod
    def no_stagnant_traffic(self) -> Optional[bool]:
        pass

    @property
    @abstractmethod
    def no_red_light(self) -> Optional[bool]:
        pass

    @property
    @abstractmethod
    def residents_only(self) -> Optional[bool]:
        pass

    @property
    @abstractmethod
    def time_interval_only(self) -> Optional[bool]:
        pass
