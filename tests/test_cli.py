
import unittest
from unittest.mock import patch
from io import StringIO

from main import main


class TestCalculatorCLI(unittest.TestCase):

    @patch("builtins.input", side_effect=["+", "8", "2", "q"])
    def test_addition_and_quit(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as output:
            main()

        result = output.getvalue()
        self.assertIn("Result: 10.0", result)
        self.assertIn("Goodbye!", result)

    @patch(
        "builtins.input",
        side_effect=["*", "3", "4", "-", "9", "2", "q"]
    )
    def test_two_calculations(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as output:
            main()

        result = output.getvalue()
        self.assertIn("Result: 12.0", result)
        self.assertIn("Result: 7.0", result)

    @patch("builtins.input", side_effect=["x", "q"])
    def test_invalid_operation(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as output:
            main()

        self.assertIn("Invalid choice!", output.getvalue())

    @patch("builtins.input", side_effect=["+", "hello", "q"])
    def test_invalid_number(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as output:
            main()

        self.assertIn("Invalid input!", output.getvalue())

    @patch("builtins.input", side_effect=["/", "8", "0", "q"])
    def test_division_by_zero(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as output:
            main()

        result = output.getvalue()
        self.assertIn("Cannot divide by zero.", result)
        self.assertNotIn("Result:", result)

    @patch("builtins.input", side_effect=["%", "10", "0", "q"])
    def test_modulo_by_zero(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as output:
            main()

        result = output.getvalue()
        self.assertIn("Cannot calculate modulo by zero.", result)
        self.assertNotIn("Result:", result)


if __name__ == "__main__":
    unittest.main()
