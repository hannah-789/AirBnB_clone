#!/usr/bin/python3
"""The `review` module.

Defining one class `Review(),
which is a  sub-class of  the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Allows users to post a review.

    It represents a review posted by the users
    of the application about a place/house.

    Attributes:
        text
        user_id
        place_id
    """
    user_id = ""
    text = ""
    place_id = ""
