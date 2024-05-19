#!/usr/bin/python3
"""The place module

Defining the class Place(),
which  is a sub-class of  the `BaseModel()` class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A  chosen place or house in the application.

    Defining the place or house of choice 
    by the users of the application.

    Attributes:
        amenity_ids
        city_id
        description
        latitude
        longitude
        max_guest
        name
        number_bathrooms
        number_rooms
        price_by_night
        user_id
    """
    amenity_ids = []
    city_id = ""
    description = ""
    latitude = 0.0
    longitude = 0.0
    max_guest = 0
    name = ""
    number_bathrooms = 0
    number_rooms = 0
    price_by_night = 0
    user_id = ""
