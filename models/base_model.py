#!/usr/bin/python3
"""
Module is for base.py
"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    BaseModel class that generates the  common
    attributes and methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        creates an instance of an object with its attributes
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
            if key in ("created_at", "updated_at"):
                value = datetime.fromisoformat(value)
            setattr(self, key, value)
        return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)
    def __str__(self):
         """
         Returns a string representation of the object.
         This includes the class name, object ID, and all its attributes.
         """
         return f"[<{self.__class__.__name__}>] ({self.id}) {self.__dict__}"
    def save(self):
        """
         Updates the updated_at attribute with the current datetime.

         This method should also call the storage functionality 
         to persist the changes to the object
        """
        self.updated_at = datetime.now().isoformat()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.
        """
        return {k: v.isoformat() if isinstance(v, datetime) else v for k, v in self.__dict__.items()}
