#!/usr/bin/python3
"""
It's the module: __init__.py
"""
from models.engine import file_storage
"""
Retrieving the file storage instance
"""
storage = file_storage.FileStorage()
storage.reload()
