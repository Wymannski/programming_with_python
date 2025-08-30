from unittest import TestCase

from context import Context
from custom_exception import CannotBeBlankException
from variable import Variable


class TestVariable(TestCase):
    def setUp(self):
        self.context = Context()
        self.context.bind("a",1)
        self.variable = Variable("a")

    def test_eval(self):
        self.assertEqual(self.variable.eval(self.context),1)

    def test_init_exception(self):
        with self.assertRaises(CannotBeBlankException):
            variable = Variable("")
