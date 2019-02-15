#!/usr/bin/python3
"""
    Module containing the ``HBNBCommand`` class.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        The ``HBNBCommand`` class which inherits from ``cmd`` class.
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """Override emptyline from Cmd"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    do_EOF = do_quit

if __name__ == '__main__':
    from models.base_model import BaseModel
    import sys
    if len(sys.argv) is 1:
        HBNBCommand().cmdloop()
    else:
        s = ' '.join(sys.argv[1:])
        HBNBCommand().onecmd(s)
