from unittest import TestCase

from car import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car(5,50.0)
        self.car.fill(50)

    def test_fill(self):
        self.assertEqual(self.car.gas_level,50)

    def test_drive(self):
        self.car.drive(100)
        self.assertEqual(self.car.gas_level,45)
