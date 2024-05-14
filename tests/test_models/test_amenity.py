#!/usr/bin/python3
""" The test_amenity module. """


import unittest
import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_amenity_default_attributes(self):
        """
        Test default attributes of the Amenity instance.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_name(self):
        """
        Test setting and getting the name attribute of the Amenity instance.
        """
        amenity = Amenity()
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")

    def test_amenity_id(self):
        """
        Test presence of the id attribute in the Amenity instance.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))

    def test_amenity_created_at(self):
        """
        Test presence of the created_at attribute in the Amenity instance.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'created_at'))

    def test_amenity_updated_at(self):
        """
        Test presence of the updated_at attribute in the Amenity instance.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_amenity_to_dict(self):
        """
        Test the to_dict() method of the Amenity instance.
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_amenity_str(self):
        """
        Test the __str__() method of the Amenity instance.
        """
        amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)

    def test_amenity_instance(self):
        """
        Test if the Amenity instance is an instance of Amenity class.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_id_type(self):
        """
        Test the type of id attribute in the Amenity instance.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)

    def test_amenity_created_at_type(self):
        """
        Test the type of created_at attribute in the Amenity instance.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime.datetime)

    def test_amenity_updated_at_type(self):
        """
        Test the type of updated_at attribute in the Amenity instance.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime.datetime)

    def test_amenity_name_type(self):
        """
        Test the type of name attribute in the Amenity instance.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_amenity_name_assignment(self):
        """
        Test assigning a valid value to the name attribute of the Amenity
        instance.
        """
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")

#    def test_amenity_name_assignment_invalid(self):
#        """
#        Test assigning an invalid value to the name attribute of the Amenity
#        instance.
#        """
#        amenity = Amenity()
#        with self.assertRaises(AttributeError):
#            amenity.name = 123


if __name__ == '__main__':
    unittest.main()
