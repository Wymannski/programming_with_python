from unittest import TestCase

from constant import Constant
from context import Context
from unary_expression import UnaryExpression
from unary_operator import UnaryOperator


class TestUnaryExpression(TestCase):
    def test_eval(self):
        context = Context()
        constant = Constant(5)
        unary_expression = UnaryExpression(UnaryOperator.MINUS,constant)
        self.assertEqual(unary_expression.eval(context),-5)
