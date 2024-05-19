#!/usr/bin/python3
"""
Module: file_storage.py

Defines a `FileStorage` class for managing object serialization and deserialization.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """
    Serializes and deserializes objects to and from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary containing all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the internal storage.

        Args:
            obj: The object to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes all stored objects to a JSON file.
        """
        with open(FileStorage.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes objects from a JSON file if it exists.

        Supported classes are registered in the `classes` dictionary.
        """
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review

        }

        if not os.path.exists(FileStorage.__file_path):
            return

        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                FileStorage.__objects = {
                    k: classes[k.split(".")[0]](**v) for k, v in data.items()
                }
        except (FileNotFoundError, json.JSONDecodeError):
            pass
