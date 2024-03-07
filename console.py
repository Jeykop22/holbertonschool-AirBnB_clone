#!/usr/bin/python3
"""
This module represents the console
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """
    This class defines console functions
    """

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create command to create an instance of a class"""
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return False

        if len(args) > 1:
            print("Incorrect number of arguments")
            return False

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return False

        if len(args) == 1:
            print("** instance id missing **")
            return False

        if len(args) > 2:
            print("Incorrect number of arguments")
            return False

        instance_id = args[1]
        found_instance = BaseModel().get(class_name, instance_id)
        if found_instance:
            print(found_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy command to delete an instance"""
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return False

        if len(args) == 1:
            print("** instance id missing **")
            return False
        
        if len(args) > 2:
            print("Incorrect numer of arguments")
            return False

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
        if len(arg) == 0:
            print("** class name missing **")
            return False

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        instance_id = args[1]
        found_instance = BaseModel().get(class_name, instance_id)
        if not found_instance:
            print("** no instance found **")
            return False

        if len(args) == 2:
            print("** attribute name missing **")
            return False

        attribute_name = args[2]

        if len(args) == 3:
            print("** value missing **")
            return False

        attribute_value_str = args[3]

        if attribute_value_str[0] == '"' and attribute_value_str[-1] == '"':
            attribute_value = attribute_value_str[1:-1]
        else:
            try:
                attribute_value = int(attribute_value_str)
            except ValueError:
                try:
                    attribute_value = float(attribute_value_str)
                except ValueError:
                    attribute_value = attribute_value_str

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
