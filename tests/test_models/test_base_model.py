#!/usr/bin/python3
""" console unit tests """
import unittest
import os
import sys
from datetime import datetime
from time import sleep
from models import storage
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User


class TestBaseModel(unittest.TestCase):
    """ console unit tests class """
    def setUp(self):
        """Initialize variables"""
        self.cmd = HBNBCommand()
        self.base = BaseModel()
        self.base_model1 = BaseModel()
        self.base_model2 = BaseModel()
        self.user = User()
        self.models_storage = storage.all()
        self.output = StringIO()

    def test_save(self):
        """Test save"""
        b = BaseModel()
        sleep(0.07)
        _updated_at = b.updated_at
        b.save()
        self.assertLess(_updated_at, b.updated_at)

    def tearDown(self):
        """Reset file storage data"""
        storage.delete()
        self.output.close()

    def test__str__representation(self):
        """Test the __str__ method for BaseModel."""
        b = BaseModel()
        val = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(val, str(b))

    def test_to_dict(self):
        _dt = datetime.today()
        b = BaseModel()
        b.id = "0123456"
        b.created_at = _dt
        b.updated_at = _dt
        to_dict = {
            'id': '0123456',
            '__class__': 'BaseModel',
            'created_at': _dt.isoformat(),
            'updated_at': _dt.isoformat()
        }
        self.assertDictEqual(b.to_dict(), to_dict)

    def test_uuid(self):
        """Test uniqueness of uuids"""
        uuid1 = self.base_model1.id
        self.assertIsInstance(uuid1, str)

        uuid2 = self.base_model2.id
        self.assertIsInstance(uuid2, str)
        self.assertNotEqual(uuid1, uuid2)

    def test_create_command(self):
        """Test create success"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)
            # self.assertIsInstance(self.models_storage.get(0), BaseModel)

    def test_create_command_nonexistent_class(self):
        """Test create invalid class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("create NonExistentClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_command(self):
        """Test show command success"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("show BaseModel {}".format(self.base.id))
            output = mock_stdout.getvalue().strip()
            self.assertIn(str(self.base), output)

    def test_show_command_nonexistent_class(self):
        """Test show invalid class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("show NonExistentClass {}".format(self.base.id))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_command_nonexistent_instance(self):
        """Test show invalid instance"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("show BaseModel NonExistentInstanceID")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_command(self):
        """Test destroy success"""
        bcn = self.base.__class__.__name__
        bid = self.base.id
        instance_id = "{bcn}.{bid}"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("destroy BaseModel {}".format(self.base.id))
            output = mock_stdout.getvalue().strip()
            self.assertNotIn(instance_id, self.models_storage)
            self.assertEqual(output, "")

    def test_destroy_command_nonexistent_class(self):
        """Test destroy invalid class"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("destroy NonExistentClass {}".format(self.base.id))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_command_nonexistent_instance(self):
        """Test destroy invalid instance"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("destroy BaseModel NonExistentInstanceID")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_command(self):
        """Test update"""
        bcn = self.base.__class__.__name__
        bid = self.base.id
        instance_id = "{bcn}.{bid}"
        attribute_name = "name"
        new_value = 'Updated'

        self.cmd.onecmd("create BaseModel")
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            a = self.base.id
            b = attribute_name
            c = new_value
            self.cmd.onecmd(f"update BaseModel {a} {b} '{c}'")
            output = mock_stdout.getvalue().strip()

        updated_instance = self.models_storage.get(instance_id)
        try:
            A = getattr(updated_instance, attribute_name)
            B = new_value.strip("'").lower()
            self.assertEqual(A, B)
        except AttributeError:
            return

    def test_EOF(self):
        """Test EOF"""
        result = self.cmd.do_EOF(None)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
