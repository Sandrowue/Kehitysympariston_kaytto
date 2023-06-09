# For testing the timetools module

# Libraries and modules
import unittest
import timetools

# Test classes
class test_time(unittest.TestCase):

    def test_datediff_days(self):
        expected_result = 3
        result = timetools.datediff_days('2023-06-09', '2023-06-06')
        self.assertEqual(result, expected_result)
    if __name__ == "__main__":
        unittest.main()