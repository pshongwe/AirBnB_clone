#!/usr/bin/python3
""" Place unit tests """
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from models import storage
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ place class unit tests class """
    def setUp(self):
        """setup"""
        self.place = Place()
        self.models_storage = storage.all()

    def tearDown(self):
        """ teardown """
        storage.delete()

    def test_place_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_place_creation(self):
        """Test create"""
        self.assertIsInstance(self.place, Place)
        self.assertTrue(self.place.id)
        self.assertTrue(self.place.created_at)
        self.assertTrue(self.place.updated_at)

    def test_str_representation(self):
        """Test string representation"""
        expected_str = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected_str)

    def test_city_id_attribute_type(self):
        """Test if the 'city_id' attribute is a string"""
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id_attribute_type(self):
        """Test if the 'user_id' attribute is a string"""
        self.assertIsInstance(self.place.user_id, str)

    def test_name_attribute_type(self):
        """Test if the 'name' attribute is a string"""
        self.assertIsInstance(self.place.name, str)

    def test_description_attribute_type(self):
        """Test if the 'description' attribute is a string"""
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_attribute_type(self):
        """Test if the 'number_rooms' attribute is an integer"""
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_attribute_type(self):
        """Test if the 'number_bathrooms' attribute is an integer"""
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_attribute_type(self):
        """Test if the 'max_guest' attribute is an integer"""
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_attribute_type(self):
        """Test if the 'price_by_night' attribute is an integer"""
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_attribute_type(self):
        """Test if the 'latitude' attribute is a float"""
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_attribute_type(self):
        """Test if the 'longitude' attribute is a float"""
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids_attribute_type(self):
        """Test if the 'amenity_ids' attribute is a list"""
        self.assertIsInstance(self.place.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
