import unittest
from price_info import total_cost_shopping, cost_of_fruits

class TestPriceInfoFunctions(unittest.TestCase):
    def test_total_cost_shopping(self):
        # Test total_cost_shopping with a sample quantity list
        expected_total_cost = 5 * 1.20 + 5 * 1.40 + 1 * 6.50 + 2 * 2.70 + 10 * 0.90 + 1 * 2.95 + 2 * 4.95
        self.assertEqual(total_cost_shopping(), expected_total_cost)

    def test_cost_of_fruits(self):
        # Test cost_of_fruits with a sample fruit and quantity
        expected_cost = 10 * 1.20
        self.assertEqual(cost_of_fruits('apple', 10), expected_cost)

        # Test cost_of_fruits with a fruit not in the price list
        self.assertEqual(cost_of_fruits('banana', 5), "banana is not in the price list.")

if __name__ == '__main__':
    unittest.main()