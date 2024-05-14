#!/usr/bin/python3
""" city module that contains the City class. """


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for storing city information.

    Attributes:
        state_id (str): The id of the state that the city belongs to.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
