#!/usr/bin/python3
""" test_state module for test cases for the state module. """
import unittest
import datetime
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def test_state_default_attributes(self):
        """
        Test default attributes of the State instance.
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_state_name(self):
        """
        Test setting and getting the name attribute of the State instance.
        """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_state_id(self):
        """
        Test presence of the id attribute in the State instance.
        """
        state = State()
        self.assertTrue(hasattr(state, 'id'))

    def test_state_created_at(self):
        """
        Test presence of the created_at attribute in the State instance.
        """
        state = State()
        self.assertTrue(hasattr(state, 'created_at'))

    def test_state_updated_at(self):
        """
        Test presence of the updated_at attribute in the State instance.
        """
        state = State()
        self.assertTrue(hasattr(state, 'updated_at'))

    def test_state_to_dict(self):
        """
        Test the to_dict() method of the State instance.
        """
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_state_str(self):
        """
        Test the __str__() method of the State instance.
        """
        state = State()
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)

    def test_state_instance(self):
        """
        Test if the State instance is an instance of State class.
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_state_id_type(self):
        """
        Test the type of id attribute in the State instance.
        """
        state = State()
        self.assertIsInstance(state.id, str)

    def test_state_created_at_type(self):
        """
        Test the type of created_at attribute in the State instance.
        """
        state = State()
        self.assertIsInstance(state.created_at, datetime.datetime)

    def test_state_updated_at_type(self):
        """
        Test the type of updated_at attribute in the State instance.
        """
        state = State()
        self.assertIsInstance(state.updated_at, datetime.datetime)

    def test_state_name_type(self):
        """
        Test the type of name attribute in the State instance.
        """
        state = State()
        self.assertIsInstance(state.name, str)

    def test_state_name_assignment(self):
        """
        Test assigning a valid value to the name attribute of the State
        instance.
        """
        state = State()
        state.name = "New York"
        self.assertEqual(state.name, "New York")

#    def test_state_name_assignment_invalid(self):
#        """
#        Test assigning an invalid value to the name attribute of the State
#        instance.
#        """
#        state = State()
#        with self.assertRaises(AttributeError):
#            state.name = 123


if __name__ == '__main__':
    unittest.main()
