#!/usr/bin/python3
"""City module

Defining the City class: City(),
which is a  sub-classe of  the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class City(BaseModel):
    """A chosen city on the app

    Attributes:
        name
        state_id
    """
    name = ""
    state_id = ""
