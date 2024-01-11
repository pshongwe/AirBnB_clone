#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from models import storage
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ review class unit tests class """
    def setUp(self):
        self.review = Review()
        self.models_storage = storage.all()

    def tearDown(self):
        storage.delete(self.review)

    def test_review_attributes(self):
        """Test if Review instance has the expected attributes"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_review_creation(self):
        """Test the creation of a Review instance"""
        self.assertIsInstance(self.review, Review)
        self.assertTrue(self.review.id)
        self.assertTrue(self.review.created_at)
        self.assertTrue(self.review.updated_at)

    def test_str_representation(self):
        """Test the string representation of a Review instance"""
        expected_str = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)


if __name__ == '__main__':
    unittest.main()
