#!/usr/bin/python3
""" models package initialization module. """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
