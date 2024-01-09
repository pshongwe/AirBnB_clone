#!/usr/bin/python3
# A module that defines a BaseModel class

import uuid
from datetime import datetime


class BaseModel:
    """A Base class with all public instances"""
    def __init__(self):
        """Initialization of the class"""
        self.id = str(uuid.uuid4())

        current_time = datetime.now()
        self.created_at = current_time
        self.updated_at = current_time

    def save(self):
        """Update the updated_at attribute to the current datetime"""
        self.updated_at = datetime.now

    def to_dict(self):
        """Creates a dictionary containing only instance att that have been set"""
        c_at_string = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        u_at_string = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')

        my_dict = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

        my_dict['created_at'] = c_at_string
        my_dict['updated_at'] = u_at_string

        my_dict['__class__'] = self.__class__.__name__

        return my_dict

    def __str__(self):
        """return the string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"