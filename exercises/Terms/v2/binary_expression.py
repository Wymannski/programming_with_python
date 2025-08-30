from term import Term
from v2.binary_operator import BinaryOperator
from v2.context import Context


class BinaryExpression:
    def __init__(self,binary_operator:BinaryOperator,left:Term,right:Term):
        self.__left = left
        self.__right = right
        self.__binary_operator = binary_operator

    def eval(self,context:Context)->float:
        match self.__binary_operator:
            case BinaryOperator.PLUS:
                return self.__left.eval(context) + self.__right.eval(context)
            case BinaryOperator.MINUS:
                return self.__left.eval(context) - self.__right.eval(context)
            case BinaryOperator.MUL:
                return self.__left.eval(context) * self.__right.eval(context)
            case BinaryOperator.DIV:
                return self.__left.eval(context) / self.__right.eval(context)

