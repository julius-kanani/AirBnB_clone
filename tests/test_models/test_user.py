#!/usr/bin/python3
""" test_user module for test cases for the user module. """
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User model class.
    """

    def setUp(self):
        """ Setup class for User testcases. """

        self.user = User()

    def test_default_attributes(self):
        """ Test default attribute values. """

        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_setting_attributes(self):
        """
        Test if User instance attributes are set correctly.
        """

        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

#    def test_to_dict(self):
#        """
#        Test the to_dict method of User object.
#        """
#
#        user_dict = self.user.to_dict()
#        expected_keys = [
#                "id", "created_at", "updated_at", "email", "password",
#                "first_name", "last_name", "__class__"]
#        self.assertEqual(set(user_dict.keys()), set(expected_keys))
#        self.assertEqual(user_dict["email"], "")
#        self.assertEqual(user_dict["password"], "")
#        self.assertEqual(user_dict["first_name"], "")
#        self.assertEqual(user_dict["last_name"], "")

    def test_str_representation(self):
        """
        Test the string representation of User object.
        """

        self.assertEqual(str(self.user), "[User] ({}) {}".format(
            self.user.id, self.user.__dict__))


if __name__ == '__main__':
    unittest.main()
