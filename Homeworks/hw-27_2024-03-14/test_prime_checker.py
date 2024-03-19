import unittest
from prime_checker import is_prime

class TestPrime_checker(unittest.TestCase):
    
    def test_is_prime(self):
        self.assertTrue(is_prime(2), "2 is Prime")
        self.assertTrue(is_prime(3), "2 is Prime")
        self.assertFalse(is_prime(4), "4 is NOT Prime")
        self.assertTrue(is_prime(5), "2 is Prime")
        self.assertFalse(is_prime(6), "4 is NOT Prime")

if __name__ == "__main__":
    unittest.main()