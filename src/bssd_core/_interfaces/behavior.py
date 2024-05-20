from abc import ABC, abstractmethod
from typing import Optional, Iterator

from osmium import osm


class Behavior(ABC):

    @property
    @abstractmethod
    def speed_max(self) -> Optional[float]:
        pass

    @property
    @abstractmethod
    def speed_time_max(self) -> Optional[float]:
        pass

    @property
    @abstractmethod
    def speed_wet_max(self) -> Optional[float]:
        pass

    @property
    @abstractmethod
    def overtake(self) -> Optional[bool]:
        pass

    @property
    @abstractmethod
    def speed_indicator(self) -> Iterator[osm.RelationMember]:
        pass

    @property
    @abstractmethod
    def overtake_indicator(self) -> Iterator[osm.RelationMember]:
        pass

    @property
    @abstractmethod
    def speed_time_interval(self) -> Optional[str]:
        pass

    @property
    @abstractmethod
    def boundary_left(self) -> Iterator[osm.RelationMember]:
        pass

    @property
    @abstractmethod
    def boundary_right(self) -> Iterator[osm.RelationMember]:
        pass

    @property
    @abstractmethod
    def boundary_long(self) -> Iterator[osm.RelationMember]:
        pass

    @property
    @abstractmethod
    def reservation(self) -> Iterator[osm.RelationMember]:
        pass
