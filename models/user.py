#!/usr/bin/python3
'''Module to define a User class'''

from models.base_model import BaseModel


class User(BaseModel):
    '''Define a User'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
