from v2.custom_exception import CannotBeBlankException
from term import Term
from v2.context import Context


class Variable(Term):
    def __init__(self,name:str):
        if not name:
            raise CannotBeBlankException("The name of a variable cannot be null")
        self.__name = name

    def eval(self,context:Context):
        return context.get_value(self.__name)

