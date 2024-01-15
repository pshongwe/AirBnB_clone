#!/usr/bin/python3
""" Review unit tests """
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
        """Setup"""
        self.review = Review()
        self.models_storage = storage.all()

    def tearDown(self):
        """Teardown"""
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
        expected_str = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected_str)

    def test_place_id_attribute_type(self):
        """Test if the 'place_id' attribute is a string"""
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id_attribute_type(self):
        """Test if the 'user_id' attribute is a string"""
        self.assertIsInstance(self.review.user_id, str)

    def test_text_attribute_type(self):
        """Test if the 'text' attribute is a string"""
        self.assertIsInstance(self.review.text, str)

    def test_place_id_initial_value(self):
        """Test the initial value of the 'place_id' attribute"""
        self.assertEqual(self.review.place_id, "")

    def test_user_id_initial_value(self):
        """Test the initial value of the 'user_id' attribute"""
        self.assertEqual(self.review.user_id, "")

    def test_text_initial_value(self):
        """Test the initial value of the 'text' attribute"""
        self.assertEqual(self.review.text, "")

    def test_update_place_id_attribute(self):
        """Test updating the 'place_id' attribute"""
        new_place_id = "NewPlaceID"
        self.review.place_id = new_place_id
        self.assertEqual(self.review.place_id, new_place_id)

    def test_update_user_id_attribute(self):
        """Test updating the 'user_id' attribute"""
        new_user_id = "NewUserID"
        self.review.user_id = new_user_id
        self.assertEqual(self.review.user_id, new_user_id)

    def test_update_text_attribute(self):
        """Test updating the 'text' attribute"""
        new_text = "New Review Text"
        self.review.text = new_text
        self.assertEqual(self.review.text, new_text)


if __name__ == '__main__':
    unittest.main()
