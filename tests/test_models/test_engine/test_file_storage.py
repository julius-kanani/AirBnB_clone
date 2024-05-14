#!/usr/bin/python3
""" test_file_storage module for the file_storage module. """
import unittest
import os
import pycodestyle
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj.name = "Test Object"
        self.obj.save()

    def tearDown(self):
        """Tear down test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test all method."""
        all_objs = self.storage.all()
        self.assertTrue(isinstance(all_objs, dict))
        self.assertIn("BaseModel." + self.obj.id, all_objs)
        self.assertEqual(all_objs["BaseModel." + self.obj.id], self.obj)

    def test_new(self):
        """Test new method."""
        new_obj = BaseModel()
        new_obj.save()
        self.assertIn("BaseModel." + new_obj.id, self.storage.all())

    def test_save_reload(self):
        """Test save and reload methods."""
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn("BaseModel." + self.obj.id, all_objs)
        self.assertEqual(all_objs["BaseModel." + self.obj.id].name, "Test Object")

    def test_pep8_compliance(self):
        """Test PEP 8 compliance."""
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "PEP 8 style errors found")


if __name__ == "__main__":
    unittest.main()
