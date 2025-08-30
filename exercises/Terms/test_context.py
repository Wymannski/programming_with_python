from unittest import TestCase

from context import Context
from custom_exception import CannotBeBlankException, NotBoundException


class TestContext(TestCase):
    def setUp(self):
        self.context = Context()

    def test_bind(self):
        self.context.bind("a",1)
        self.assertEqual(self.context.get_value("a"),1)

    def test_bind_exception(self):
        with self.assertRaises(CannotBeBlankException):
            self.context.bind("",0)

    def test_get_value_cannot_be_blank_exception(self):
        with self.assertRaises(CannotBeBlankException):
            self.context.get_value("")

    def test_get_value_not_bound_exception(self):
        with self.assertRaises(NotBoundException):
            self.context.get_value("a")
