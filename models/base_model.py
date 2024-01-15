#!/usr/bin/python3
"""A module that defines a BaseModel class"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """A Base class with all public instances"""
    def __init__(self, *args, **kwargs):
        """Initialization of the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        # Check if kwargs is not empty
        if kwargs:
            # Iterate through the key-value pairs in kwargs
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)

                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    self.__dict__[key] = value

        else:
            # Generate a unique ID for the instance
            self.id = str(uuid.uuid4())

            # Set the created_at and updated_at attrbs to the current datetime
            current_time = datetime.utcnow()
            self.created_at = current_time
            self.updated_at = current_time

            models.storage.new(self)

    def save(self):
        """Update the updated_at attribute to the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Converts created_at and updated_at to str objects in ISO format"""
        time_fmt = '%Y-%m-%dT%H:%M:%S.%f'
        if isinstance(self.created_at, str):
            self.created_at = datetime.strptime(self.created_at, time_fmt)
        if isinstance(self.updated_at, str):
            self.updated_at = datetime.strptime(self.updated_at, time_fmt)

        c_at_string = self.created_at.strftime(time_fmt)
        u_at_string = self.updated_at.strftime(time_fmt)

        my_dict = {
            k: v for k, v in self.__dict__.items() if not k.startswith('_')
        }

        my_dict['created_at'] = c_at_string
        my_dict['updated_at'] = u_at_string

        my_dict['__class__'] = self.__class__.__name__

        return my_dict

    def __str__(self):
        """return the string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def delete(self):
        """deletes instance"""
        models.storage.delete(self)
