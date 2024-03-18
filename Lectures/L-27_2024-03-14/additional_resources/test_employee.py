import os
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        pass
    
    
    def tearDown(self):
        pass
    
    
    def test_email(self):
        emp_1 = Employee("Corey", "Schafer", 50000)
        emp_2 = Employee("Sue", "Smith", 60000)

        self.assertEqual(emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(emp_2.email, "Sue.Smith@email.com")

        emp_1.first = "John"
        emp_2.first = "Jane"

        self.assertEqual(emp_1.email, "John.Schafer@email.com")
        self.assertEqual(emp_2.email, "Jane.Smith@email.com")


    def test_fullname(self):
        emp_1 = Employee("Corey", "Schafer", 50000)
        emp_2 = Employee("Sue", "Smith", 60000)

        self.assertEqual(emp_1.fullname, "Corey Schafer")
        self.assertEqual(emp_2.fullname, "Sue Smith")

        emp_1.first = "John"
        emp_2.first = "Jane"

        self.assertEqual(emp_1.fullname, "John Schafer")
        self.assertEqual(emp_2.fullname, "Jane Smith")


    def test_apply_raise(self):
        emp_1 = Employee("Corey", "Schafer", 50000)
        emp_2 = Employee("Sue", "Smith", 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()      

        self.assertEqual(emp_1.pay, int(50000*1.05))
        self.assertEqual(emp_2.pay, int(60000*1.05))


if __name__ == "__main__":
    unittest.main()
    