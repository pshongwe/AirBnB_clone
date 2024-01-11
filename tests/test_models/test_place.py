import unittest
from unittest.mock import patch
from io import StringIO
import sys
from models import storage
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """ place classs unit tests class """
    def setUp(self):
        self.place = Place()
        self.models_storage = storage.all()

    def tearDown(self):
        storage.delete_all()

    def test_place_attributes(self):
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
        self.assertIsInstance(self.place, Place)
        self.assertTrue(self.place.id)
        self.assertTrue(self.place.created_at)
        self.assertTrue(self.place.updated_at)

    def test_str_representation(self):
        expected_str = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)


if __name__ == '__main__':
    unittest.main()

