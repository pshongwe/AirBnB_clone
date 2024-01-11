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


class TestConsole(unittest.TestCase):
    """ console unit tests class """
    def setUp(self):
        """ initialize vars """
        self.cmd = HBNBCommand()
        self.base = BaseModel()
        self.user = User()
        self.models_storage = storage.all()
        self.output = StringIO()

    def tearDown(self):
        """ reset file storage data """
        storage.delete()
        self.output.close()

    def test_create_command(self):
        """ test create success """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)
            # self.assertIsInstance(self.models_storage.get(0), BaseModel)

    def test_create_command_nonexistent_class(self):
        """ test create invalid class """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("create NonExistentClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_command(self):
        """ test show command success """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("show BaseModel {}".format(self.base.id))
            output = mock_stdout.getvalue().strip()
            self.assertIn(str(self.base), output)

    def test_show_command_nonexistent_class(self):
        """ test show invalid class """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("show NonExistentClass {}".format(self.base.id))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_command_nonexistent_instance(self):
        """ test show invalid instance """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("show BaseModel NonExistentInstanceID")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_command(self):
        """  test destroy success """
        instance_id = "{}.{}".format(self.base.__class__.__name__, self.base.id)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("destroy BaseModel {}".format(self.base.id))
            output = mock_stdout.getvalue().strip()
            self.assertNotIn(instance_id, self.models_storage)
            self.assertEqual(output, "")

    def test_destroy_command_nonexistent_class(self):
        """ test destroy invalid class """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("destroy NonExistentClass {}".format(self.base.id))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_command_nonexistent_instance(self):
        """ test destroy invalid instance """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("destroy BaseModel NonExistentInstanceID")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_command(self):
        instance_id = "{}.{}".format(self.base.__class__.__name__, self.base.id)
        attribute_name = "name"
        new_value = 'Updated'

        self.cmd.onecmd("create BaseModel")
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("update BaseModel {} {} '{}'".format(self.base.id, attribute_name, new_value))
            output = mock_stdout.getvalue().strip()

        updated_instance = self.models_storage.get(instance_id)
        self.assertEqual(getattr(updated_instance, attribute_name).strip("'").lower(), new_value.strip("'").lower())


if __name__ == '__main__':
    unittest.main()
