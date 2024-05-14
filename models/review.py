#!/usr/bin/python3
""" review module that contains the Review class. """


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for storing review information.

    Attributes:
        place_id (str): The id of the place that the review is for.
        user_id (str): The id of the user who wrote the review.
        text (str): The text content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
