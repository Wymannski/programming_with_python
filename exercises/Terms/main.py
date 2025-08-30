from context import Context
from constant import Constant
from custom_exception import CannotBeBlankException, NotBoundException
from variable import Variable
from unary_expression import UnaryExpression
from unary_operator import UnaryOperator
from binary_operator import BinaryOperator
from binary_expression import BinaryExpression

def main():
    context = Context()
    constant5 = Constant(5)
    constant3 = Constant(3)
    try:
        variable: Variable = Variable('d')
    except CannotBeBlankException as e:
        print(e)

    context.bind('d',7)
    try:
        unary_expression = UnaryExpression(UnaryOperator.MINUS, variable)
        binary_expression_add = BinaryExpression(BinaryOperator.PLUS, constant3, unary_expression)
        binary_expression_mul = BinaryExpression(BinaryOperator.MUL, binary_expression_add, constant5)

        print(binary_expression_mul.eval(context))
    except CannotBeBlankException or NotBoundException as e:
        print(e)




if __name__ == '__main__':
    main()