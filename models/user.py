#!/usr/bin/python3
""" class User """
import models
from models.base_model import BaseModel


class User(BaseModel):
    """ class representation of User object """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
