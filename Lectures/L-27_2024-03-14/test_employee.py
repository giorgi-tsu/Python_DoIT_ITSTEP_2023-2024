import  unittest
from employee import Employee
#fixture

class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\nSetUpClass")
    
    @classmethod
    def tearDown(cls):
        print("\nTearDown")


    def setUp(self):
        print("\nSetup")
        self.employee1 = Employee("Elene", "Sulukhia", 100)
        self.employee2 = Employee("Giorgi", "Tsutskiridze", 100)
        
    def tearDown(self):
        print("\nTearDown")

    def test_email(self):
        print("test_email")
        
        self.assertEqual(self.employee1.email, "sulukhia_elene@gmail.com")
        self.assertEqual(self.employee2.email, "tsutskiridze_giorgi@gmail.com")

        self.employee1.first = "Mariami"
        self.employee2.first = "Levani"

        self.assertEqual(self.employee1.email, "sulukhia_mariami@gmail.com")
        self.assertEqual(self.employee2.email, "tsutskiridze_levani@gmail.com")

    def test_fulllname(self):
        print("test_fullname")
    
        self.assertEqual(self.employee1.fullname, "Elene Sulukhia")
        self.assertEqual(self.employee2.fullname, "Giorgi Tsutskiridze")

    def test_apply_raise(self):
        self.employee1.apply_raise()
        self.employee2.apply_raise()

        self.assertEqual(self.employee1.pay, 105)
        self.assertEqual(self.employee2.pay, 105)



if __name__ == "__main__":
    unittest.main()