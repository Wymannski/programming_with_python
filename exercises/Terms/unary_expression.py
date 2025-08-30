from term import Term
from unary_operator import UnaryOperator
from context import Context

class UnaryExpression(Term):
    def __init__(self,operator:UnaryOperator,term:Term):
        self.__operator = operator
        self.__term = term

    def eval(self,context:Context) -> float:
        match self.__operator:
            case UnaryOperator.MINUS:
                return self.__term.eval(context) * (-1)
