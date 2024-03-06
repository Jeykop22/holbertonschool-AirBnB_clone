#!/usr/bin/python3
"""
This module represents the console
"""

import cmd
from models.base_model import BaseModel
import json

class HBNBCommand(cmd.Cmd):
    """
    This class defines console functions
    """
    
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_create(self, arg):
        """Create command to create an instance of a class"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        found_instance = BaseModel().get(class_name, instance_id)
        if not found_instance:
            print("** no instance found **")
        else:
            print(found_instance)

    def do_destroy(self, arg):
        """Destroy command to delete an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        found_instance = BaseModel().get(class_name, instance_id)
        if not found_instance:
            print("** no instance found **")
        else:
            found_instance.delete()
            BaseModel().save()

    def do_all(self, arg):
        """Prints all instances"""
        args = arg.split()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        all_instances = BaseModel().all()
        instance_strings = [str(instance) for instance in all_instances]
        print(instance_strings)

    def do_update(self, arg):
        """Updates an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        found_instance = BaseModel().get(class_name, instance_id)
        if not found_instance:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        setattr(found_instance, attribute_name, attribute_value)
        found_instance.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Handles empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
