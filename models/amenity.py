#!/usr/bin/python3
""" amenity module that contains the Amenity class. """


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for storing amenity information.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
