#!/usr/bin/python3
"""City Class."""
from models.base_model import BaseModel


class City(BaseModel):
    """City Representation.

    Attributes:
        state_id (str): State Id.
        name (str): Name of the city.
    """

    state_id = ""
    name = ""
