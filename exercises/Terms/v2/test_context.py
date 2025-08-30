from unittest import TestCase

from v2.context import Context
from v2.custom_exception import CannotBeBlankException


class TestContext(TestCase):
    def setUp(self):
        self.context = Context()

    def test_bind(self):
        name = 'a'
        value = 2
        self.context.bind(name,value)
        self.assertEqual(value,self.context.get_value(name))

    def test_bind_cannot_be_blank(self):
        name = ''
        value = 2
        with self.assertRaises(CannotBeBlankException):
            self.context.bind(name,value)

    def test_get_value(self):
        name = 'a'
        value = 2
        self.context.bind(name,value)
        self.assertEqual(value,self.context.get_value(name))

    def test_get_value_cannot_be_blank(self):
        name = ''
        with self.assertRaises(CannotBeBlankException):
            self.context.get_value(name)


