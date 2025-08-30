from term import Term
from v2.context import Context
from v2.unary_operator import UnaryOperator


class UnaryExpression:
    def __init__(self,unary_operator:UnaryOperator,term:Term):
        self.__term = term
        self.__unaryOperator = unary_operator

    def eval(self,context:Context)->float:
        match self.__unaryOperator:
            case UnaryOperator.MINUS:
                return (-1) * self.__term.eval(context)
            case _:
                return self.__term.eval(context)
