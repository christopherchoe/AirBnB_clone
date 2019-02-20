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
import json
import os
import models.engine.file_storage


class TestConsole(unittest.TestCase):
    """
        Test class for HBNBCommandClass.
    """

    def setUp(self):
        """setup for tests."""

        self.mock_stdin = create_autospec(HBNBCommand().stdin)
        self.mock_stdout = create_autospec(HBNBCommand().stdout)

        try:
            os.remove('file.json')
        except OSError:
            pass

        f1 = models.engine.file_storage.FileStorage()
        f1.reload()

    def tearDown(self):
        """teardown for tests."""

        try:
            os.remove('file.json')
        except OSError:
            pass

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
        self.assertIsNone(cli.onecmd(""))
        self.assertEqual("", self._last_write())

    def test_create_0(self):
        """Test create command without arguments"""
        cli = self.create()
        ex_o = "** class name missing **\n"
        self.assertFalse(cli.onecmd("create"))
        self.assertEqual(ex_o, self._last_write())

    def test_create_1(self):
        """Test create command with invalid class name"""
        cli = self.create()
        ex_o = "** class doesn't exist **\n"
        self.assertFalse(cli.onecmd("create DontExist"))
        self.assertEqual(ex_o, self._last_write())

    def test_create_2(self):
        """Test create command with valid class"""
        cli = self.create()
        self.assertTrue(cli.onecmd("create User"))
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
        self.assertTrue(cli.onecmd("quit"))
        self.assertEqual("", self._last_write())

    def test_EOF(self):
        """Test EOF command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("EOF"))
        self.assertEqual("", self._last_write())

    def test_show_0(self):
        """Test show command without arguments"""
        cli = self.create()
        ex_o = "** class name missing **\n"
        self.assertFalse(cli.onecmd("show"))
        self.assertEqual(ex_o, self._last_write())

    def test_show_1(self):
        """Test show command with invalid class name"""
        cli = self.create()
        ex_o = "** class doesn't exist **\n"
        self.assertFalse(cli.onecmd("show DontExist"))
        self.assertEqual(ex_o, self._last_write())

    def test_show_2(self):
        """Test show command with valid class, no id"""
        cli = self.create()
        self.assertFalse(cli.onecmd("show User"))
        self.assertEqual('** instance id missing **\n', self._last_write())

    def test_show_3(self):
        """Test show command with valid class but invalid id"""
        cli = self.create()
        self.assertFalse(cli.onecmd("show User 1010101"))
        self.assertEqual('** no instance found **\n', self._last_write())

    def test_show_4(self):
        """Test show command with valid class but invalid id"""
        cli = self.create()
        self.assertFalse(cli.onecmd("show User"))
        cmp_str = '** instance id missing **\n'
        self.assertEqual(cmp_str, self._last_write())

    def test_show_5(self):
        """Test show command with invalid class name"""
        cli = self.create()
        ex_o = "** class doesn't exist **\n"
        self.assertFalse(cli.onecmd("DontExist.show()"))
        self.assertEqual(ex_o, self._last_write())

    def test_show_6(self):
        """Test show command with valid class, no id"""
        cli = self.create()
        self.assertFalse(cli.onecmd("User.show()"))
        self.assertEqual('** instance id missing **\n', self._last_write())

    def test_show_7(self):
        """Test show command with valid class but invalid id"""
        cli = self.create()
        self.assertFalse(cli.onecmd("User.show(1010101)"))
        self.assertEqual('** no instance found **\n', self._last_write())

    def test_show_8(self):
        """Test show command with valid class but invalid id"""
        cli = self.create()
        self.assertFalse(cli.onecmd("DontExist.show("))
        self.assertEqual('*** Unknown syntax: DontExist.show(\n',
                         self._last_write())

    def test_show_9(self):
        """Test show command with valid class but invalid id"""
        cli = self.create()
        self.assertTrue(cli.onecmd("create User"))
        id_user = self._last_write()
        self.mock_stdout.reset_mock()
        self.assertFalse(cli.onecmd("User.show({})".format(id_user)))
        cmp_str = '** instance id missing **\n'
        self.assertNotEqual(cmp_str, self._last_write())

    def test_destroy_0(self):
        """Test show command without arguments"""
        cli = self.create()
        ex_o = "** class name missing **\n"
        self.assertFalse(cli.onecmd("destroy"))
        self.assertEqual(ex_o, self._last_write())

    def test_destroy_1(self):
        """Test destroy command with invalid class name"""
        cli = self.create()
        ex_o = "** class doesn't exist **\n"
        self.assertFalse(cli.onecmd("destroy DontExist"))
        self.assertEqual(ex_o, self._last_write())

    def test_destroy_2(self):
        """Test destroy command with valid class, no id"""
        cli = self.create()
        self.assertFalse(cli.onecmd("destroy User"))
        self.assertEqual('** instance id missing **\n', self._last_write())

    def test_destroy_3(self):
        """Test destroy command with valid class but invalid id"""
        cli = self.create()
        self.assertFalse(cli.onecmd("destroy User 1010101"))
        self.assertEqual('** no instance found **\n', self._last_write())

    def test_destroy_4(self):
        """Test destroy command with valid input"""
        cli = self.create()
        self.assertFalse(cli.onecmd("destroy User"))
        self.assertFalse(cli.onecmd("destroy User {}".format(
                                                        self._last_write())))
        self.assertNotEqual('** instance id missing **\n', self._last_write())

    def test_destroy_5(self):
        """Test destroy command with invalid class name"""
        cli = self.create()
        ex_o = "** class doesn't exist **\n"
        self.assertFalse(cli.onecmd("DontExist.destroy()"))
        self.assertEqual(ex_o, self._last_write())

    def test_destroy_6(self):
        """Test destroy command with valid class, no id"""
        cli = self.create()
        self.assertFalse(cli.onecmd("User.destroy()"))
        self.assertEqual('** instance id missing **\n', self._last_write())

    def test_destroy_7(self):
        """Test destroy command with valid class but invalid id"""
        cli = self.create()
        self.assertFalse(cli.onecmd("User.destroy(1010101)"))
        self.assertEqual('** no instance found **\n', self._last_write())

    def test_destroy_8(self):
        """Test destroy command with valid input"""
        cli = self.create()
        self.assertTrue(cli.onecmd("create User"))
        id_user = self._last_write()
        self.mock_stdout.reset_mock()
        self.assertTrue(cli.onecmd("User.destroy(\"{}\")".format(id_user[:-1]))
                        )
        self.assertEqual('', self._last_write())

    def test_all_0(self):
        """Test all command without arguments"""
        cli = self.create()
        self.assertTrue(cli.onecmd("create User"))
        self.mock_stdout.reset_mock()
        with open('file.json') as f:
            s = json.load(f)
        test_dict = {}
        test_list = []
        for key, val in s.items():
            test_dict[key] = eval(val["__class__"])(**val)
        for obj in test_dict.values():
            test_list.append(obj.__str__())
        self.assertTrue(cli.onecmd("all"))
        self.assertEqual(str(test_list), self._last_write()[:-1])
