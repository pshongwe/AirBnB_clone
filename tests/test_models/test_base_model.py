#!/usr/bin/python3
""" console unit tests """
import unittest
import os
import sys
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
        self.user = User()
        self.models_storage = storage.all()
        self.output = StringIO()

    def tearDown(self):
        """Reset file storage data"""
        storage.delete()
        self.output.close()

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
        instance_id = "{}.{}".format(self.base.__class__.__name__, self.base.id)
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
        instance_id = "{}.{}".format(self.base.__class__.__name__, self.base.id)
        attribute_name = "name"
        new_value = 'Updated'

        self.cmd.onecmd("create BaseModel")
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd(f"update BaseModel {self.base.id} {attribute_name} '{new_value}'")
            output = mock_stdout.getvalue().strip()

        updated_instance = self.models_storage.get(instance_id)
        A = getattr(updated_instance, attribute_name).strip("'").lower()
        B = new_value.strip("'").lower()
        self.assertEqual(A, B)
    
    def test_EOF(self):
        result = self.cmd.do_EOF(None)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
