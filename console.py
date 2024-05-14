#!/usr/bin/python3
"""Module for the HBNB command interpreter."""

import cmd
import sys
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def postcmd(self, stop, line):
        """Print an extra empty line after each command."""
        if line != 'quit' and line != 'EOF':
            print("")
        return stop

    def help_quit(self):
        """Print help for quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Print help for EOF command."""
        print("EOF command (Ctrl+D) to exit the program")

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.storage.classes:
            print("** class doesn't exist **")
            return
        new_instance = models.storage.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Print all instances."""
        if arg:
            if arg not in models.storage.classes:
                print("** class doesn't exist **")
                return
            instances = models.storage.all()
        else:
            instances = models.storage.all()
        print([str(obj) for obj in instances.values()])

    def do_update(self, arg):
        """Update an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        obj = models.storage.all()[key]
        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass
        setattr(obj, attr_name, attr_value)
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
