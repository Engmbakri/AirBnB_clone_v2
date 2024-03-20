#!/usr/bin/python3
"""Review Class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Representation

    Attributes:
        place_id (str): Place Id.
        user_id (str): User Id.
        text (str): Text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
