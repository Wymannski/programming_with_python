from unittest import TestCase

from constant import Constant
from context import Context


class TestConstant(TestCase):
    def test_eval(self):
        constant = Constant(5)
        context = Context()
        self.assertEqual(constant.eval(context),5)
