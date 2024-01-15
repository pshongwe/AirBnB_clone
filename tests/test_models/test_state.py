#!/usr/bin/python3
""" State unit tests """
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from models import storage
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ state class unit tests class """
    def setUp(self):
        """Setup"""
        self.state = State()
        self.models_storage = storage.all()

    def tearDown(self):
        """Teardown"""
        storage.delete(self.state)

    def test_state_attributes(self):
        """Test if State instance has the expected attributes"""
        self.assertTrue(hasattr(self.state, 'name'))

    def test_state_creation(self):
        """Test the creation of a State instance"""
        self.assertIsInstance(self.state, State)
        self.assertTrue(self.state.id)
        self.assertTrue(self.state.created_at)
        self.assertTrue(self.state.updated_at)

    def test_str_representation(self):
        """Test the string representation of a State instance"""
        expected_str = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected_str)

    def test_name_attribute_type(self):
        """Test if the 'name' attribute is a string"""
        self.assertIsInstance(self.state.name, str)

    def test_name_attribute_initial_value(self):
        """Test the initial value of the 'name' attribute"""
        self.assertEqual(self.state.name, "")

    def test_update_name_attribute(self):
        """Test updating the 'name' attribute"""
        new_name = "New State Name"
        self.state.name = new_name
        self.assertEqual(self.state.name, new_name)

    def test_name_attribute_with_spaces(self):
        """Test setting the 'name' attribute with spaces"""
        name_with_spaces = "State with Spaces"
        self.state.name = name_with_spaces
        self.assertEqual(self.state.name, name_with_spaces)


if __name__ == '__main__':
    unittest.main()
