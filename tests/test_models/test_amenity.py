#!/usr/bin/python3
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
        self.amenity = Amenity()
        self.models_storage = storage.all()

    def tearDown(self):
        storage.delete(self.amenity)

    def test_amenity_attributes(self):
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_amenity_creation(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(self.amenity.id)
        self.assertTrue(self.amenity.created_at)
        self.assertTrue(self.amenity.updated_at)

    def test_str_representation(self):
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)


if __name__ == '__main__':
    unittest.main()

