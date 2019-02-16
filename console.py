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
        key_str = HBNBCommand.check_class(arg)
        if key_str is not None:
            obj = storage.all()[key_str[0]]
            print(obj)

    def do_destroy(self, arg):
        """Destroys an instance based on class name and instance id:  destory
        BaseModel 1234-1234-1234
        """
        key_str = HBNBCommand.check_class(arg)
        if key_str is not None:
            del storage.all()[key_str[0]]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of instances based or not on class
        name:  all BaseModel
            :  all
        """
        s = shlex.split(arg)
        inst_list = []
        if len(s) is 0:
            for obj in storage.all().values():
                inst_list.append(obj.__str__())
        else:
            try:
                eval(s[0])
                for key, val in storage.all().items():
                    if s[0] in key:
                        inst_list.append(val.__str__())
            except (NameError, SyntaxError):
                print('** class doesn\'t exist **')
                return

        print(inst_list)

    def do_update(self, arg):
        """Updates instance based on classname and id by adding/updating an
        attribute
        """
        key_str = HBNBCommand.check_class(arg)
        if key_str is None:
            return
        s = key_str[1]
        s_len = len(s)
        if s_len < 3:
            print('** attribute name missing **')
            return
        elif s_len < 4:
            print('** value missing **')
            return
        obj = storage.all()[key_str[0]]
        attr = s[2]
        val = s[3]
        if attr in obj.__dict__.keys():
            if type(obj.__dict__[attr]) is str:
                obj.__dict__[attr] = val
                setattr(obj, attr, val)
            elif type(obj.__dict__[attr]) is int:
                obj.__dict__[attr] = int(val)
            elif type(obj.__dict__[attr]) is float:
                obj.__dict__[attr] = float(val)
        else:
            obj.__dict__[attr] = val
        storage.save()

    @staticmethod
    def check_class(arg):
        """Check if arg contains, a valid class, and id.

        Returns:
            A tuple containing the key(classname.id) and parsed arg.
            None if arg does not contain a valid class, and id.
        """
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

        return (key, s)

    do_EOF = do_quit

if __name__ == '__main__':
    from models.base_model import BaseModel
    from models.user import User
    from models import storage
    import sys
    if len(sys.argv) is 1:
        HBNBCommand().cmdloop()
    else:
        s = ' '.join(sys.argv[1:])
        HBNBCommand().onecmd(s)
