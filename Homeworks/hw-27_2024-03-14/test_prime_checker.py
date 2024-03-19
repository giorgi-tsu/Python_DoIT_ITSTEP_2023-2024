import unittest
from prime_checker import is_prime

class TestPrime_checker(unittest.TestCase):
    
    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(6), False)

if __name__ == "__main__":
    unittest.main()