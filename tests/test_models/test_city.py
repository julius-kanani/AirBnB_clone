#!/usr/bin/python3
""" The test_city module. """
import unittest
import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def test_city_default_attributes(self):
        """
        Test default attributes of the City instance.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_state_id(self):
        """
        Test setting and getting the state_id attribute of the City instance.
        """
        city = City()
        city.state_id = "CA"
        self.assertEqual(city.state_id, "CA")

    def test_city_name(self):
        """
        Test setting and getting the name attribute of the City instance.
        """
        city = City()
        city.name = "San Francisco"
        self.assertEqual(city.name, "San Francisco")

    def test_city_id(self):
        """
        Test presence of the id attribute in the City instance.
        """
        city = City()
        self.assertTrue(hasattr(city, 'id'))

    def test_city_created_at(self):
        """
        Test presence of the created_at attribute in the City instance.
        """
        city = City()
        self.assertTrue(hasattr(city, 'created_at'))

    def test_city_updated_at(self):
        """
        Test presence of the updated_at attribute in the City instance.
        """
        city = City()
        self.assertTrue(hasattr(city, 'updated_at'))

    def test_city_to_dict(self):
        """
        Test the to_dict() method of the City instance.
        """
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_city_str(self):
        """
        Test the __str__() method of the City instance.
        """
        city = City()
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)

    def test_city_instance(self):
        """
        Test if the City instance is an instance of City class.
        """
        city = City()
        self.assertIsInstance(city, City)

    def test_city_id_type(self):
        """
        Test the type of id attribute in the City instance.
        """
        city = City()
        self.assertIsInstance(city.id, str)

    def test_city_created_at_type(self):
        """
        Test the type of created_at attribute in the City instance.
        """
        city = City()
        self.assertIsInstance(city.created_at, datetime.datetime)

    def test_city_updated_at_type(self):
        """
        Test the type of updated_at attribute in the City instance.
        """
        city = City()
        self.assertIsInstance(city.updated_at, datetime.datetime)

    def test_city_state_id_type(self):
        """
        Test the type of state_id attribute in the City instance.
        """
        city = City()
        self.assertIsInstance(city.state_id, str)

    def test_city_state_id_assignment(self):
        """
        Test assigning a valid value to the state_id attribute of the City
        instance.
        """
        city = City()
        city.state_id = "NY"
        self.assertEqual(city.state_id, "NY")

#    def test_city_state_id_assignment_invalid(self):
#        """
#        Test assigning an invalid value to the state_id attribute of the City
#        instance.
#        """
#        city = City()
#        with self.assertRaises(AttributeError):
#            city.state_id = 123

    def test_city_name_type(self):
        """
        Test the type of name attribute in the City instance.
        """
        city = City()
        self.assertIsInstance(city.name, str)

    def test_city_name_assignment(self):
        """
        Test assigning a valid value to the name attribute of the City
        instance.
        """
        city = City()
        city.name = "Los Angeles"
        self.assertEqual(city.name, "Los Angeles")

#    def test_city_name_assignment_invalid(self):
#        """
#        Test assigning an invalid value to the name attribute of the City
#        instance.
#        """
#        city = City()
#        with self.assertRaises(AttributeError):
#            city.name = 123


if __name__ == '__main__':
    unittest.main()
