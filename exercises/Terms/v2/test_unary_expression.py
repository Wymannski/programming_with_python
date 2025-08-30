from unittest import TestCase

from v2.unary_operator import UnaryOperator
from v2.constant import Constant
from v2.context import Context
from v2.unary_expression import UnaryExpression


class TestUnaryExpression(TestCase):
    def setUp(self):
        self.context = Context()
        self.constant = Constant(2)

    def test_eval_minus(self):
        operator = UnaryOperator.MINUS
        unary_expression = UnaryExpression(operator,self.constant)
        self.assertEqual(-2,unary_expression.eval(self.context))


