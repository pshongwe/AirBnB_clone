#!/usr/bin/python3
"""Module that defines FileStorage class"""


import json
import os


class FileStorage:
    """class that uses private class attributes below"""

    __file_path = "myfile"
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        seria_objs = {
                key: value.to_dict() for key, value in self.__objects.items()
                }
        with open(self.__file.path, 'w') as f:
            json.dump(seria_objs, f)

    def reload(self):
        """Deserializes the JSON file to __objects if exists otherwise no"""
        if os.path.exists(self.__file_path, 'r') as f:
            data = json.load(f)

            for key, value in data.items():
                class_name, obj_id = key.split('.')
                module = __import__(class_name)
                myclass = getattr(module, class_name)
                obj = myclass(**value)
                self.__object[key] = obj
