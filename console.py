#!/usr/bin/python3
"""
    Module containing the ``HBNBCommand`` class.
"""
import cmd
import shlex

class HBNBCommand(cmd.Cmd):
    """
        The ``HBNBCommand`` class which inherits from ``cmd`` class.
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """Override emptyline from Cmd."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program:  quit
        """
        return True

    def do_create(self, arg):
        """Create an instance of a class and saves instance attributes to a
        JSON file:  create BaseModel
        """
        try:
            obj = eval(arg)()
            print(obj.id)
            obj.save()
        except SyntaxError:
            print('** class name missing ** ')
        except NameError:
            print('** class doesn\'t exist **')

    def do_show(self, arg):
        """Displays the string representation of an instance based on class
        name and instance id:  show BaseModel 1234-1234-1234
        """
        key = HBNBCommand.check_class(arg)
        if key is not None:
            val = storage.all()[key]
            obj = BaseModel(**val)
            print(obj)

    def do_destroy(self, arg):
        """Destroys an instance based on class name and instance id:  destory
        BaseModel 1234-1234-1234
        """
        key = HBNBCommand.check_class(arg)
        if key is not None:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of instances based or not on class
        name:  all BaseModel
            :  all
        """
        s = shlex.split(arg)
        inst_list = []
        if len(s) is 0:
            for val in storage.all().values():
                obj = BaseModel(**val)
                inst_list.append(obj.__str__())
        else:
            try:
                eval(s[0])
                for key, val in storage.all().items():
                    if s[0] in key:
                        inst_list.append(str(BaseModel(**val)))
            except (NameError, SyntaxError):
                print('** class doesn\'t exist **')
                return

        print(inst_list)

    @staticmethod
    def check_class(arg):
        s = shlex.split(arg)
        slen = len(s)
        if slen is 0:
            print('** class name missing **')
            return None
        try:
            eval(s[0])
        except (NameError, SyntaxError):
            print('** class doesn\'t exist **')
            return None
        if len(s) < 2:
            print('** instance id missing **')
            return None
        key = s[0] + '.' + s[1]
        if key not in storage.all().keys():
            print('** no instance found **')
            return None

        return key

    do_EOF = do_quit

if __name__ == '__main__':
    from models.base_model import BaseModel
    from models import storage
    import sys
    if len(sys.argv) is 1:
        HBNBCommand().cmdloop()
    else:
        s = ' '.join(sys.argv[1:])
        HBNBCommand().onecmd(s)
