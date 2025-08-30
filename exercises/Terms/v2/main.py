from v2.context import Context
from v2.constant import Constant
from v2.custom_exception import CannotBeBlankException, NotBoundException
from v2.variable import Variable
from v2.unary_expression import UnaryExpression
from v2.unary_operator import UnaryOperator
from v2.binary_operator import BinaryOperator
from v2.binary_expression import BinaryExpression

def main():
    context = Context({})
    constant5 = Constant(5)
    constant3 = Constant(3)
    try:
        variable: Variable = Variable('d')
    except CannotBeBlankException as e:
        print(e)

    context = context.bind('d',7)
    try:
        unary_expression = UnaryExpression(UnaryOperator.MINUS, variable)
        binary_expression_add = BinaryExpression(BinaryOperator.PLUS, constant3, unary_expression)
        binary_expression_mul = BinaryExpression(BinaryOperator.MUL, binary_expression_add, constant5)

        print(binary_expression_mul.eval(context))
    except CannotBeBlankException or NotBoundException as e:
        print(e)




if __name__ == '__main__':
    main()