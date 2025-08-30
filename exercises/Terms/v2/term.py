from abc import ABC,abstractmethod

from v2.context import Context


class Term(ABC):
    @abstractmethod
    def eval(self,context:Context)->float:
        pass