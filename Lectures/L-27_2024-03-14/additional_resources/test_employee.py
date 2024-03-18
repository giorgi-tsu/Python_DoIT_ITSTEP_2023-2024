import os
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee("Corey", "Schafer", 50000)
        emp_2 = Employee("Sue", "Smith", 60000)

        self.assertEqual(emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(emp_2.email, "Sue.Smith@email.com")

        emp_1.first = "John"
        emp_2.first = "Jane"

        self.assertEqual(emp_1.email, "John.Schafer@email.com")
        self.assertEqual(emp_2.email, "Jane.Smith@email.com")

if __name__ == "__main__":
    unittest.main()