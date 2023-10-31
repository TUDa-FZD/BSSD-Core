from abc import ABC, abstractmethod
from typing import Iterator

from osmium import osm


class BehaviorSpace(ABC):

    @property
    @abstractmethod
    def lanelet(self) -> Iterator[osm.RelationMember]:
        pass

    @property
    @abstractmethod
    def along(self) -> Iterator[osm.RelationMember]:
        pass

    @property
    @abstractmethod
    def against(self) -> Iterator[osm.RelationMember]:
        pass
