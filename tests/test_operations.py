
import unittest

from calculator.operations import (
    add,
    subtract,
    multiply,
    divide,
    modulo,
)


class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_modulo_exact_division(self):
        self.assertEqual(modulo(12, 4), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            modulo(10, 0)


if __name__ == "__main__":
    unittest.main()
