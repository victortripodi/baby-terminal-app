import unittest
from unittest.mock import patch
from baby_tracker import get_week_number, get_valid_float

# First test - Check week number
class TestGetWeekNumber(unittest.TestCase):

    def test_get_week_number(self):
        # Test a date from the first week of the year
        self.assertEqual(get_week_number('2023-01-01'), 1)

        # Test a date from the second week of the year
        self.assertEqual(get_week_number('2023-01-08'), 2)

        # Test a date from the last week of the year
        self.assertEqual(get_week_number('2023-12-31'), 53)

# Second test - Valid input
class TestGetValidFloat(unittest.TestCase):
    # Test a valid float number
    @patch('builtins.input', side_effect=['3.14'])
    def test_valid_input(self, mock_input):
        result = get_valid_float("Enter a floating number: ")
        self.assertAlmostEqual(result, 3.14)

    # Test quit from get_valid_float
    @patch('builtins.input', side_effect=['q'])
    def test_quit_input(self, mock_input):
        result = get_valid_float("Enter a floating number (or 'q' to quit): ")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()