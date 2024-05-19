#!/usr/bin/python3
"""The `state` module

Defining the  `State() class,
which  is a sub-class of  the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A state in the application.

    Attributes:
        name
    """
    name = ""
