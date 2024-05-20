from abc import ABC, abstractmethod
from typing import Optional, Iterator

from osmium import osm

from .._types import ReservationType


class Reservation(ABC):

    @property
    @abstractmethod
    def reservation(self) -> Optional[ReservationType]:
        pass

    @property
    @abstractmethod
    def link(self) -> Iterator[osm.RelationMember]:
        pass

    @property
    @abstractmethod
    def pedestrian(self) -> Optional[bool]:
        pass

    @property
    @abstractmethod
    def bicycle(self) -> Optional[bool]:
        pass

    @property
    @abstractmethod
    def motor_vehicle(self) -> Optional[bool]:
        pass

    @property
    @abstractmethod
    def railed_vehicle(self) -> Optional[bool]:
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
    def turn_arrow_active(self) -> Optional[bool]:
        pass
