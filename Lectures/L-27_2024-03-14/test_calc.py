import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(2, 5), 7)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-2, -5), -7)
        self.assertEqual(calc.add(2, -5), -3)
    
    
    def test_substract(self):
        self.assertEqual(calc.substract(2, 5), -3)
        self.assertEqual(calc.substract(-2, 5), -7)
        self.assertEqual(calc.substract(-2, -5), 3)
        self.assertEqual(calc.substract(2, -5), 7)


    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 5), 10)
        self.assertEqual(calc.multiply(-2, 5), -10)
        self.assertEqual(calc.multiply(-2, -5), 10)
        self.assertEqual(calc.multiply(2, -5), -10)


    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-10, 5), -2)
        self.assertEqual(calc.divide(10, -5), -2)
        self.assertEqual(calc.divide(-10, -5), 2)
        self.assertEqual(calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc.divide(5, 0)

    
        
# if __name__ == "__main__":
#     unittest.main()