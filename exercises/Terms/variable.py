from custom_exception import CannotBeBlankException
from term import Term
from context import Context

class Variable(Term):
    def __init__(self,name:str):
        if not name:
            raise CannotBeBlankException(name)
        self.__name = name

    def eval(self,context:Context):
        return context.get_value(self.__name)