import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        # Add the following test methods to the TestCalculator class:
        self.assertEqual(self.calc.add(-2, 29), 27)
        self.assertEqual(self.calc.add(-5, -11), -16)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 2), 8)
        self.assertEqual(self.calc.subtract(1, -2), 3)
        self.assertEqual(self.calc.subtract(8, -7), 15)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(9, -2), -18)
        self.assertEqual(self.calc.multiply(-7, -9), 63)
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(9, 3), 0)
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)
        

if __name__ == '__main__':
    unittest.main()