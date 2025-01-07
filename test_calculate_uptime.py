import unittest
from calculate_uptime import parse_input, calculate_uptime

class TestChargerUptimeCalculation(unittest.TestCase):
    def test_basic_functionality(self):
        # Test for basic functionality
        file_path = '//path to input1 file'
        expected_output = {0: 100, 1: 0, 2: 75}  # Expected results need to be set based on the file contents
        stations, chargers = parse_input(file_path)
        result = calculate_uptime(stations, chargers)
        self.assertEqual(result, expected_output)

    def test_overlapping_periods(self):
        # Test for overlapping periods
        file_path = '//path to input2 file'
        expected_output = {0: 66, 1:100}  # Expected results need to be set based on the file contents
        stations, chargers = parse_input(file_path)
        result = calculate_uptime(stations, chargers)
        self.assertEqual(result, expected_output)

    # More tests can be added here

if __name__ == '__main__':
    unittest.main()
