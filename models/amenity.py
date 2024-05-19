#!/usr/bin/python3
"""Amenity module

Defines one class: Amenity(),
which  is a sub-classe of  the BaseModel() class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenities offered by a place or a house.

    Attributes:
        name
    """

    name = ""
