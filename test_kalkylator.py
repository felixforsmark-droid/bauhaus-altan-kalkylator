import unittest

class TestDeckCalculator(unittest.TestCase):

    def test_calculate_area(self):
        # Test the area calculation functionality
        self.assertEqual(calculate_area(5, 3), 15)
        self.assertEqual(calculate_area(0, 5), 0)
        self.assertEqual(calculate_area(4.5, 2.5), 11.25)

    def test_calculate_cost(self):
        # Test the cost calculation based on area and cost per square meter
        self.assertEqual(calculate_cost(15, 100), 1500)
        self.assertEqual(calculate_cost(20, 50), 1000)

    def test_invalid_inputs(self):
        # Check responses for invalid inputs
        with self.assertRaises(ValueError):
            calculate_area(-5, 3)
        with self.assertRaises(ValueError):
            calculate_cost(15, -100)

if __name__ == '__main__':
    unittest.main()