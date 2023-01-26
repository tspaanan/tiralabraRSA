# Run unittests:
# python3 -m unittest Testit/unittests.py

import algorithms
import unittest

class TestAlgorithms(unittest.TestCase):

    def test_Euclidean_algorithm(self):
        self.assertEqual(algorithms.Euclidean_algorithm(408,112), 8)
        self.assertNotEqual(algorithms.Euclidean_algorithm(408,112), 11)
        self.assertEqual(algorithms.Euclidean_algorithm(25,15), 5)
        self.assertNotEqual(algorithms.Euclidean_algorithm(25,15), 13)

    def test__factoring_out_powers_of_2(self):
        self.assertEqual(algorithms._factoring_out_powers_of_2(220), (55,4))
        self.assertNotEqual(algorithms._factoring_out_powers_of_2(220), (54,6))

    def test_Miller_Rabin_test(self):
        self.assertTrue(algorithms.Miller_Rabin_test(19997,11))
        self.assertFalse(algorithms.Miller_Rabin_test(19995,11))
        self.assertTrue(algorithms.Miller_Rabin_test(541,11))
        self.assertFalse(algorithms.Miller_Rabin_test(539,11))

if __name__ == '__main__':
    unittest.main()