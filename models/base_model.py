#!/usr/bin/python3
# A module that defines a BaseModel class

import uuid
from datetime import datetime


class BaseModel:
    """A Base class with all public instances"""
    def __init__(self, *args, **kwargs):
        """Initialization of the class"""

        # Check if kwargs is not empty
        if kwargs:
            # Iterate through the key-value pairs in kwargs
            for key, value in kwargs.items():
                # Exclude the __class__ key
                if key != '__class__':
                    setattr(self, key, value)

                    # Convert created_at and updatated_at strs to datetime objs
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))

        else:
            # Generate a unique ID for the instance
            self.id = str(uuid.uuid4())

            # Set the created_at and updated_at attrbs to the current datetime
            current_time = datetime.utcnow()
            self.created_at = current_time
            self.updated_at = current_time

    def save(self):
        """Update the updated_at attribute to the current datetime"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Converts created_at and updated_at to str objects in ISO format"""
        c_at_string = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        u_at_string = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')

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
