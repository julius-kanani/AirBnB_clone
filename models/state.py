#!/usr/bin/python3
""" state module that contains the State class. """


from models.base_model import BaseModel


class State(BaseModel):
    """
    State class for storing state information.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
