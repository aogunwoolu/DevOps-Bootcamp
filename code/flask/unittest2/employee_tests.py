from employee import Employee
import unittest

class TestEmployee(unittest.TestCase):

    def setUp(self):
        # Arrange
        self.emp1 = Employee("Bob", "Marley", 800000)
        self.emp2 = Employee("Dennis", "Brown", 100000)

    def test_email(self):
        # Act and Assert
        self.assertEqual(self.emp1.email, "Bob.Marley@email.com")
        self.assertEqual(self.emp2.email, "Dennis.Brown@email.com")

        self.emp1._firstname = "Rob"
        self.emp2._firstname = "Henry"

        # Act and Assert
        self.assertEqual(self.emp1.email, "Rob.Marley@email.com")
        self.assertEqual(self.emp2.email, "Henry.Brown@email.com")

    