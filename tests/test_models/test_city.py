#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from models import storage
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()
        self.models_storage = storage.all()

    def tearDown(self):
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
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)


if __name__ == '__main__':
    unittest.main()
