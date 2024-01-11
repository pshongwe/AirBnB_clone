#!/usr/bin/python3
""" console unit tests """
import unittest
import os
import sys
from models import storage
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """ console unit tests class """
    def test_prompt(self):
        """ check prompt string is correct """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", mock_stdout.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
