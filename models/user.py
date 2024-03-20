#!/usr/bin/python3
"""User Class."""
from models.base_model import BaseModel


class User(BaseModel):
    """User Representation

    Attributes:
        email (str): User Email.
        password (str): User Password.
        first_name (str): User first name
        last_name (str): User last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
