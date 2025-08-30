from unittest import TestCase

from v2.context import Context
from v2.custom_exception import CannotBeBlankException
from v2.variable import Variable


class TestVariable(TestCase):
    def test_init(self):
        name = ''
        with self.assertRaises(CannotBeBlankException):
            variable = Variable(name)

    def test_eval(self):
        name = 'a'
        value = 2
        context = Context()
        context.bind(name,value)
        variable = Variable(name)
        self.assertEqual(value,variable.eval(context))
