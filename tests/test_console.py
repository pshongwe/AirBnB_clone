#!/usr/bin/python3
""" console unit tests """
import unittest
import os
import sys
from models import storage
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import console


class TestConsole(unittest.TestCase):
    """ console unit tests class """
    def test_prompt(self):
        """ check prompt string is correct """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", mock_stdout.getvalue().strip())

    def test_console_module_docstring(self):
        """Test console module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_command_class_docstring(self):
        """Test command class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")


if __name__ == '__main__':
    unittest.main()
