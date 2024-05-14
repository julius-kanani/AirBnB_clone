#!/usr/bin/python3
"""Module for the HBNB command interpreter."""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
