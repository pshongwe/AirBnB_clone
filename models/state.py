#!/usr/bin/python3
"""Module that defines a class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialization of the method for State"""
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        """String representation of the State object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
