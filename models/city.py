#!/usr/bin/python3
"""Module that defines class city"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """initialization method for city"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

    def __str__(self):
        """String representation of the City object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
