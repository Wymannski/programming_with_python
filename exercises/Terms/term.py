from abc import ABC, abstractmethod
from context import Context
class Term(ABC):
    @abstractmethod
    def eval(self,context:Context)-> float:
        pass
