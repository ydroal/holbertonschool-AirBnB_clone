#!/usr/bin/python3
'''Module to define a BaseModel'''

import uuid
from datetime import datetime


class BaseModel:
    '''Define a BaseModel'''

    def __init__(self, *args, **kwargs):
        '''Initialize'''
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''Method that return a string to print the instance.'''

        return f'[{__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''
        Method that updates the public instance attribute updated_at
        with the current datetime
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        Method that returns a dictionary containing all keys/values of
        __dict__ of the instance
        '''

        res = self.__dict__.copy()
        res['__class__'] = __class__.__name__
        res['created_at'] = datetime.isoformat(self.created_at)
        res['updated_at'] = datetime.isoformat(self.updated_at)

        return res
