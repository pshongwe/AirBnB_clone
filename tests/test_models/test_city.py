#!/usr/bin/python3
""" City unit tests """
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from models import storage
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ city unit tests """
    def setUp(self):
        """ setup """
        self.city = City()
        self.models_storage = storage.all()

    def tearDown(self):
        """ teardown """
        storage.delete(self.city)

    def test_city_attributes(self):
        """Test if City instance has the expected attributes"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_city_creation(self):
        """Test the creation of a City instance"""
        self.assertIsInstance(self.city, City)
        self.assertTrue(self.city.id)
        self.assertTrue(self.city.created_at)
        self.assertTrue(self.city.updated_at)

    def test_str_representation(self):
        """Test the string representation of a City instance"""
        expected_str = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected_str)

    def test_state_id_attribute_type(self):
        """Test if the 'state_id' attribute is a string"""
        self.assertIsInstance(self.city.state_id, str)

    def test_name_attribute_type(self):
        """Test if the 'name' attribute is a string"""
        self.assertIsInstance(self.city.name, str)

    def test_state_id_initial_value(self):
        """Test the initial value of the 'state_id' attribute"""
        self.assertEqual(self.city.state_id, "")

    def test_name_initial_value(self):
        """Test the initial value of the 'name' attribute"""
        self.assertEqual(self.city.name, "")

    def test_update_state_id_attribute(self):
        """Test updating the 'state_id' attribute"""
        new_state_id = "NewStateID"
        self.city.state_id = new_state_id
        self.assertEqual(self.city.state_id, new_state_id)

    def test_update_name_attribute(self):
        """Test updating the 'name' attribute"""
        new_name = "New City Name"
        self.city.name = new_name
        self.assertEqual(self.city.name, new_name)

    def test_name_attribute_with_spaces(self):
        """Test setting the 'name' attribute with spaces"""
        name_with_spaces = "City with Spaces"
        self.city.name = name_with_spaces
        self.assertEqual(self.city.name, name_with_spaces)


if __name__ == '__main__':
    unittest.main()
