#!/usr/bin/python3
# from uuid import uuid4
# from datetime import datetime
# import models

from models.base_model import BaseModel

"""
Module User
defines a user class with attributes including email,
password, first_name, and last_name
"""


class User(BaseModel):
    """
    User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
