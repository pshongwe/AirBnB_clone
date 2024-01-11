#!/usr/bin/python3
""" class User """
import models
import hashlib
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """ class representation of User object """
    email = ""
    _password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialize user"""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        """ hash password """
        self._password = hashlib.md5(pwd.encode()).hexdigest()
