from context import Context
from term import Term

class Constant(Term):
    def __init__(self,value:float):
        self.__value = value

    def eval(self,context:Context)->float:
        return self.__value