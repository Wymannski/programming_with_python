from term import Term
from v2.context import Context


class Constant(Term):
    def __init__(self,value:float):
        self.__value = value

    def eval(self,context:Context)->float:
        return self.__value
