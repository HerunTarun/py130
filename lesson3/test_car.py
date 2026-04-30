import unittest
from car import Car

class CarTest(unittest.TestCase):
    def test_wheels(self):
        car = Car()
        self.assertEqual(4, car.wheels)


if __name__ == '__main__':
    unittest.main()