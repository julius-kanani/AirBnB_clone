#!/usr/bin/python3
""" base_module for the BaseModel class."""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines all common attributes/methods for other classes.

    Attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last
        updated.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.

        Sets id to a unique identifier, created_at and updated_at to the
        current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A string containing class name, id, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the instance's updated_at attribute to the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the instance attributes to a dictionary.

        Returns:
            dict: A dictionary containing all instance attributes and their
            values.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
