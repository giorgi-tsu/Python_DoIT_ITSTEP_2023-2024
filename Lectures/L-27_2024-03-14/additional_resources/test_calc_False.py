import os
import unittest
import calc  # importing calc is easy since it's in the 
             # same directory
 
class TestCalc(unittest.TestCase):
 
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 14)


if __name__ == "__main__":
    unittest.main()