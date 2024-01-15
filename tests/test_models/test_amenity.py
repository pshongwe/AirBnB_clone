#!/usr/bin/python3
""" amenity unit tests """
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ amenity class unit tests class """
    def setUp(self):
        """setup"""
        self.amenity = Amenity()
        self.models_storage = storage.all()

    def tearDown(self):
        """teardown"""
        storage.delete(self.amenity)

    def test_amenity_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_amenity_creation(self):
        """Test create"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(self.amenity.id)
        self.assertTrue(self.amenity.created_at)
        self.assertTrue(self.amenity.updated_at)

    def test_str_representation(self):
        """Test string representation"""
        expected_str = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected_str)

    def test_name_attribute_type(self):
        """Test if the 'name' attribute is a string"""
        self.assertIsInstance(self.amenity.name, str)

    def test_name_initial_value(self):
        """Test the initial value of the 'name' attribute"""
        self.assertEqual(self.amenity.name, "")

    def test_update_name_attribute(self):
        """Test updating the 'name' attribute"""
        new_name = "New Amenity Name"
        self.amenity.name = new_name
        self.assertEqual(self.amenity.name, new_name)

    def test_name_attribute_with_spaces(self):
        """Test setting the 'name' attribute with spaces"""
        name_with_spaces = "Amenity with Spaces"
        self.amenity.name = name_with_spaces
        self.assertEqual(self.amenity.name, name_with_spaces)


if __name__ == '__main__':
    unittest.main()
