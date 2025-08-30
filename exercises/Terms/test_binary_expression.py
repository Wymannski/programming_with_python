from unittest import TestCase

from binary_expression import BinaryExpression
from binary_operator import BinaryOperator
from constant import Constant
from context import Context


class TestBinaryExpression(TestCase):
    def setUp(self):
        self.context = Context()
        self.constant5 = Constant(5)
        self.constant3 = Constant(3)

    def test_eval_plus(self):
        binary_expression = BinaryExpression(BinaryOperator.PLUS, self.constant5, self.constant3)
        self.assertEqual(binary_expression.eval(self.context), 8)

    def test_eval_minus(self):
        binary_expression = BinaryExpression(BinaryOperator.MINUS, self.constant5, self.constant3)
        self.assertEqual(binary_expression.eval(self.context), 2)


    def test_eval_multiply(self):
        binary_expression = BinaryExpression(BinaryOperator.MUL, self.constant5, self.constant3)
        self.assertEqual(binary_expression.eval(self.context), 15)

    def test_eval_division(self):
        delta = 1E-2
        binary_expression = BinaryExpression(BinaryOperator.DIV, self.constant5, self.constant3)
        self.assertAlmostEqual(binary_expression.eval(self.context), 1.66,delta=delta)
