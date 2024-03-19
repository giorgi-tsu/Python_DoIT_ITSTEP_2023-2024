import unittest
from prime_checker import is_prime

class TestPrime_checker(unittest.TestCase):

    
    def test_is_prime(self):
        
        list_of_primes = [2, 5, 7, 11, 29]
        list_of_nonprimes = [4, 8, 12, 14, 28]


        for i in list_of_primes:
            self.assertTrue(is_prime(i), f"{i} is Prime")


        for i in list_of_nonprimes:
            self.assertFalse(is_prime(i), f"{i} is NOT Prime")


if __name__ == "__main__":
    unittest.main()