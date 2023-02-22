#!/usr/bin/python3
'''Module to define a User class'''

from models.base_model import BaseModel


class User(BaseModel):
    email = None
    password = None
    first_name = None
    last_name = None
