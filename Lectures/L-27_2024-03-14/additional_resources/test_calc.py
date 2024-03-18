import os
import unittest
import calc  # importing calc is easy since it's in the 
             # same directory
 
class TestCalc(unittest.TestCase):
 
    def add_test(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 14)


if __name__ == "__main__":
    unittest.main()