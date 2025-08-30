from unittest import TestCase

from v2.constant import Constant
from v2.context import Context


class TestConstant(TestCase):
    def test_eval(self):
        context = Context()
        value = 2
        const = Constant(value)
        self.assertEqual(value,const.eval(context))
