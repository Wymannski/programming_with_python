from unittest import TestCase

from v2.binary_expression import BinaryExpression
from v2.binary_operator import BinaryOperator
from v2.constant import Constant
from v2.context import Context


class TestBinaryExpression(TestCase):
    def setUp(self):
        self.context = Context()
        self.constant8 = Constant(8)
        self.constant2 = Constant(2)

    def test_eval_plus(self):
        operator = BinaryOperator.PLUS
        binary_expression = BinaryExpression(operator,self.constant8,self.constant2)
        self.assertEqual(10,binary_expression.eval(self.context))

    def test_eval_minus(self):
        operator = BinaryOperator.MINUS
        binary_expression = BinaryExpression(operator, self.constant8, self.constant2)
        self.assertEqual(6, binary_expression.eval(self.context))

    def test_eval_mul(self):
        operator = BinaryOperator.MUL
        binary_expression = BinaryExpression(operator, self.constant8, self.constant2)
        self.assertEqual(16, binary_expression.eval(self.context))

    def test_eval_idv(self):
        operator = BinaryOperator.DIV
        binary_expression = BinaryExpression(operator, self.constant8, self.constant2)
        self.assertEqual(4, binary_expression.eval(self.context))

