from term import Term
from binary_operator import BinaryOperator
from context import Context

class BinaryExpression(Term):
    def __init__(self,operator:BinaryOperator,left:Term,right:Term):
        self.__operator = operator
        self.__left = left
        self.__right = right

    def eval(self,context:Context) -> float:
        match self.__operator:
            case BinaryOperator.PLUS:
                return self.__left.eval(context) + self.__right.eval(context)
            case BinaryOperator.MINUS:
                return self.__left.eval(context) - self.__right.eval(context)
            case BinaryOperator.MUL:
                return self.__left.eval(context) * self.__right.eval(context)
            case BinaryOperator.DIV:
                return self.__left.eval(context) / self.__right.eval(context)

        # bin_op_dict = {
        #     BinaryOperator.PLUS : lambda l,r: l+r,
        #     BinaryOperator.MINUS: lambda l, r: l - r,
        #     BinaryOperator.MUL: lambda l, r: l * r,
        #     BinaryOperator.DIV: lambda l, r: l / r,
        # }
        #
        # operation = bin_op_dict[self.__operator]
        # return operation(self.__left,self.__right)