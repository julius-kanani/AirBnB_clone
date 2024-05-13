#!/usr/bin/python3
""" test_base_model module. """
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up a BaseModel instance before each test.
        """
        self.obj = BaseModel()

    def test_instance_creation(self):
        """
        Test if an instance of BaseModel is created successfully.
        """
        self.assertIsInstance(self.obj, BaseModel)

    def test_attributes(self):
        """
        Test if the attributes id, created_at, and updated_at are present.
        """
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_id_uniqueness(self):
        """
        Test if the id attribute is unique for each BaseModel instance.
        """
        obj2 = BaseModel()
        self.assertNotEqual(self.obj.id, obj2.id)

    def test_save_method(self):
        """
        Test if the save method updates the updated_at attribute.
        """
        updated_at_before_save = self.obj.updated_at
        self.obj.save()
        updated_at_after_save = self.obj.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_to_dict_method(self):
        """
        Test if the to_dict method returns a dictionary with expected keys.
        """
        obj_dict = self.obj.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertEqual(sorted(obj_dict.keys()), sorted(expected_keys))

    def test_str_method(self):
        """
        Test if the __str__ method returns the expected string representation.
        """
        expected_string = "[{}] ({}) {}".format(
                'BaseModel', self.obj.id, self.obj.__dict__)
        self.assertEqual(str(self.obj), expected_string)


if __name__ == '__main__':
    unittest.main()
