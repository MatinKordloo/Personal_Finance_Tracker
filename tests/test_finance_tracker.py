import unittest
from unittest.mock import patch
from decimal import Decimal

import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import (
    get_valid_amount,
    get_valid_date,
    get_valid_month
)


class TestFinanceTracker(unittest.TestCase):

    # Test valid amount
    @patch("builtins.input", return_value="100.50")
    def test_valid_amount(self, mock_input):
        result = get_valid_amount()
        self.assertEqual(result, Decimal("100.50"))

    # Test invalid amount followed by valid amount
    @patch("builtins.input", side_effect=["100.505", "100.50"])
    def test_invalid_amount(self, mock_input):
        result = get_valid_amount()
        self.assertEqual(result, Decimal("100.50"))

    # Test valid date
    @patch("builtins.input", return_value="2026-10-05")
    def test_valid_date(self, mock_input):
        result = get_valid_date()
        self.assertEqual(result, "2026-10-05")

    # Test invalid date followed by valid date
    @patch("builtins.input", side_effect=["2026-02-30", "2026-10-05"])
    def test_invalid_date(self, mock_input):
        result = get_valid_date()
        self.assertEqual(result, "2026-10-05")

    # Test valid month
    @patch("builtins.input", return_value="2026-10")
    def test_valid_month(self, mock_input):
        result = get_valid_month()
        self.assertEqual(result, "2026-10")

    # Test that a valid amount is greater than zero
    @patch("builtins.input", return_value="50")
    def test_positive_amount(self, mock_input):
        result = get_valid_amount()
        self.assertGreater(result, 0)

    # Test that a valid month has the correct format
    @patch("builtins.input", return_value="2026-10")
    def test_month_format(self, mock_input):
        result = get_valid_month()
        self.assertEqual(len(result), 7)
        self.assertEqual(result[4], "-")


if __name__ == "__main__":
    unittest.main()