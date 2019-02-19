#!/usr/bin/python3
"""
    Test module for console.
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from unittest.mock import create_autospec
from console import HBNBCommand
import unittest
import sys


class TestConsole(unittest.TestCase):
    """
        Test class for HBNBCommandClass.
    """

    def setUp(self):
        """setup for tests."""

        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self):
        """Return a console object that uses `mock_stdin` and `mock_stdout`."""

        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        """Returns last `n` output lines."""

        if nr is None:
            return "".join(map(lambda c: c[0][0],
                           self.mock_stdout.write.call_args_list[:]))
            # return self.mock_stdout.write.call_args[0][0]

        return "".join(map(lambda c: c[0][0],
                           self.mock_stdout.write.call_args_list[-nr:]))

    def test_empty(self):
        """Test empty input"""
        cli = self.create()
        cli.onecmd("")
        self.assertEqual("", self._last_write())

    def test_create_0(self):
        """Test create command without arguments"""
        cli = self.create()
        ex_o = "** class name missing **\n"
        cli.onecmd("create")
        self.assertEqual(ex_o, self._last_write())

    def test_create_1(self):
        """Test create command with invalid class name"""
        cli = self.create()
        ex_o = "** class doesn't exist **\n"
        cli.onecmd("create DontExist")
        self.assertEqual(ex_o, self._last_write())

    def test_create_2(self):
        """Test create command with valid class"""
        cli = self.create()
        cli.onecmd("create User")
        self.assertNotEqual('', self._last_write())

    def test_help_command(self):
        """Test help"""
        cli = self.create()
        cli.onecmd("help")
        ex_o = "\nDocumented commands (type help <topic>):\n" \
            "========================================\n" \
            "EOF  all  create  destroy  help  quit  show  update\n\n"
        self.assertEqual(ex_o, self._last_write())

    def test_EOF_help(self):
        """Test help for EOF command"""
        cli = self.create()
        cli.onecmd("help EOF")
        self.assertIsNotNone(self._last_write())

    def test_all_help(self):
        """Test help for all command"""
        cli = self.create()
        cli.onecmd("help all")
        self.assertIsNotNone(self._last_write())

    def test_create_help(self):
        """Test help for create command"""
        cli = self.create()
        cli.onecmd("help create")
        self.assertIsNotNone(self._last_write())

    def test_destroy_help(self):
        """Test help for destroy command"""
        cli = self.create()
        cli.onecmd("help destroy")
        self.assertIsNotNone(self._last_write())

    def test_help_help(self):
        """Test help for help command"""
        cli = self.create()
        cli.onecmd("help help")
        self.assertIsNotNone(self._last_write())

    def test_quit_help(self):
        """Test help for quit command"""
        cli = self.create()
        cli.onecmd("help quit")
        self.assertIsNotNone(self._last_write())

    def test_show_help(self):
        """Test help for show command"""
        cli = self.create()
        cli.onecmd("help show")
        self.assertIsNotNone(self._last_write())

    def test_update_help(self):
        """Test help for update command"""
        cli = self.create()
        cli.onecmd("help update")
        self.assertIsNotNone(self._last_write())

    def test_quit(self):
        """Test quit command"""
        cli = self.create()
        cli.onecmd("quit")
        self.assertEqual("", self._last_write())

    def test_EOF(self):
        """Test EOF command"""
        cli = self.create()
        cli.onecmd("EOF")
        self.assertEqual("", self._last_write())
