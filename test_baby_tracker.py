
import unittest
from baby_tracker import get_week_number

class TestGetWeekNumber(unittest.TestCase):

    def test_get_week_number(self):
        # Test a date from the first week of the year
        self.assertEqual(get_week_number('2023-01-01'), 1)

        # Test a date from the second week of the year
        self.assertEqual(get_week_number('2023-01-08'), 2)

        # Test a date from the last week of the year
        self.assertEqual(get_week_number('2023-12-31'), 53)


