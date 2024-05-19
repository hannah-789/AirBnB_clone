#!usr/bin/python3
from models.base_model import BaseModel
"""The `user` module

Defining the  `User() class,
which  is a sub-class of  the `BaseModel()` class.`
"""

class User(BaseModel):
    """Creates a new user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
