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
        self.user = User()
        self.models_storage = storage.all()

    def tearDown(self):
        storage.delete()

    def test_user_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, '_password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_password_hashing(self):
        password = "password123"
        self.user.password = password
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        self.assertEqual(self.user._password, hashed_password)

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertTrue(self.user.id)
        self.assertTrue(self.user.created_at)
        self.assertTrue(self.user.updated_at)


if __name__ == '__main__':
    unittest.main()
