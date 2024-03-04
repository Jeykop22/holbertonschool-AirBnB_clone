#!/usr/bin/python3
"""This module contains the console for the AirBnB project."""

import cmd

class HBNBCommand(cmd.Cmd):
    """Class for the command line interpreter."""
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
