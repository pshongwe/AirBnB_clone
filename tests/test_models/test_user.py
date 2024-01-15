#!/usr/bin/python3
"""User class unit tests """
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import hashlib
from models import storage
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ User class unit tests class """
    def setUp(self):
        """Setup"""
        self.user = User()
        self.models_storage = storage.all()

    def tearDown(self):
        """Teardown"""
        storage.delete()

    def test_user_attributes(self):
        """Test user attributes"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_password_hashing(self):
        """Test password"""
        password = "password123"
        self.user.password = password
        self.assertEqual(self.user.password, password)

    def test_user_creation(self):
        """Test user create"""
        self.assertIsInstance(self.user, User)
        self.assertTrue(self.user.id)
        self.assertTrue(self.user.created_at)
        self.assertTrue(self.user.updated_at)

    def test_str_representation(self):
        """Test the string representation of a User instance"""
        expected_str = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_str)

    def test_email_attribute_type(self):
        """Test if the 'email' attribute is a string"""
        self.assertIsInstance(self.user.email, str)

    def test_password_attribute_type(self):
        """Test if the '_password' attribute is a string"""
        self.assertIsInstance(self.user.password, str)

    def test_first_name_attribute_type(self):
        """Test if the 'first_name' attribute is a string"""
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name_attribute_type(self):
        """Test if the 'last_name' attribute is a string"""
        self.assertIsInstance(self.user.last_name, str)

    def test_email_initial_value(self):
        """Test the initial value of the 'email' attribute"""
        self.assertEqual(self.user.email, "")

    def test_password_initial_value(self):
        """Test the initial value of the 'password' attribute"""
        self.assertEqual(self.user.password, "")

    def test_first_name_initial_value(self):
        """Test the initial value of the 'first_name' attribute"""
        self.assertEqual(self.user.first_name, "")

    def test_last_name_initial_value(self):
        """Test the initial value of the 'last_name' attribute"""
        self.assertEqual(self.user.last_name, "")

    def test_update_email_attribute(self):
        """Test updating the 'email' attribute"""
        new_email = "new_email@example.com"
        self.user.email = new_email
        self.assertEqual(self.user.email, new_email)

    def test_update_password_attribute(self):
        """Test updating the 'password' attribute"""
        new_password = "new_password_hashed"
        self.user.password = new_password
        self.assertEqual(self.user.password, new_password)

    def test_update_first_name_attribute(self):
        """Test updating the 'first_name' attribute"""
        new_first_name = "New First Name"
        self.user.first_name = new_first_name
        self.assertEqual(self.user.first_name, new_first_name)

    def test_update_last_name_attribute(self):
        """Test updating the 'last_name' attribute"""
        new_last_name = "New Last Name"
        self.user.last_name = new_last_name
        self.assertEqual(self.user.last_name, new_last_name)


if __name__ == '__main__':
    unittest.main()
