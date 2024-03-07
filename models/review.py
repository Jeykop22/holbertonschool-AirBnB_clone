#!/usr/bin/python3
"""class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
        Review class for the Airbnb project
        with public class attributes
    """
    place_id = ""
    user_id = ""
    text = ""
