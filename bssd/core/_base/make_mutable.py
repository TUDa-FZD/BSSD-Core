from abc import ABC
from .. import mutable
from .relation import Relation


class MakeMutable(Relation, ABC):

    def make_mutable(self):
        cls = getattr(mutable, type(self).__name__)
        return cls(self._data)
