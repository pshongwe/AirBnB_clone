#!/usr/bin/python3
"""Module that defines FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User

classes = {"BaseModel": BaseModel, "User": User}


class FileStorage:
    """class that uses private class attributes below"""

    __file_path = "file.json"
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
        with open(self.__file_path, 'w') as f:
            json.dump(seria_objs, f)

    def reload_helper(self, data, key):
        """ reload helper """
        return classes[data[key]["__class__"]](**data[key])

    def reload(self):
        """Deserializes the JSON file to __objects if exists otherwise no"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    data = json.load(f)

                    for key in data:
                        self.__objects[key] = self.reload_helper(data, key)
            except:
                pass

    def delete(self, obj=None):
        """deletes object if present"""
        if obj is not None:
            del self.__objects[obj.__class__.__name__ + '.' + obj.id]
            self.save()
