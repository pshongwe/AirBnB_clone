#!/usr/bin/python3
"""command interpreter"""
import cmd
import models
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """ console class """
    prompt = '(hbnb) '
    
    def do_show(self, args):
        """Prints instance as string based on the class and id"""
        _args = args.split()

        if not _args:
            print("** class name missing **")
            return

        class_name = _args[0]
    
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(_args) < 2:
            print("** instance id missing **")
            return

        instance_id = class_name + "." + _args[1]

        if instance_id in models.storage.all():
            print(models.storage.all()[instance_id])
        else:
            print("** no instance found **")
        
    def do_create(self, args):
        """Creates new instance of class"""
        _args = args.split()
        if len(_args) == 0:
            print("** class name missing **")
            return False
        elif _args[0] in classes:
            new_dict = self._parse_dict(_args[1:])
            instance = classes[_args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)  # prints uuid
        instance.save()

    def my_filter(self, objects, class_name):
        filtered_objects = filter(
            lambda item: isinstance(item[1], classes[class_name]),
            objects.items()
        )
        return dict(filtered_objects)

    def do_all(self, args):
        """Prints string representation of instances"""
        _args = args.split()

        if not _args:
            objects = models.storage.all()
        elif _args[0] in classes:
            class_name = _args[0]
            objects = models.storage.all()
            filtered_objects = self.my_filter(objects, class_name)
            objects = filtered_objects
        else:
            print("** class doesn't exist **")
            return False

        print("[", end="")
        print(", ".join(str(obj) for obj in objects.values()), end="")
        print("]")

    def _parse_dict(self, args):
        """creates dictionary from list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                key, value = arg.split('=', 1)
                value = value.strip('"').replace('_', ' ')
                try:
                    if '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                except (ValueError, TypeError):
                    pass
                new_dict[key] = value
        return new_dict

    def do_EOF(self, args):
        """ exits console """
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ override cmd emptyline method """
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
