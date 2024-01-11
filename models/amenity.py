#!/usr/bin/python3
"""Module that defines class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialization method for Amenity"""
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        """String representation of the Amenity object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
