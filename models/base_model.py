#!/usr/bin/python3
'''Module to define a BaseModel'''

import uuid
from datetime import datetime
import models


class BaseModel:
    '''Define a BaseModel'''

    def __init__(self, *args, **kwargs):
        '''
        check if there is **kwargs (Instances are created by dictionaries)
        if key is created_at or updated_at -> change str to datetime
        set the attributes with key and values using setattr() .
        '''

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    """convertie l'objet en datatime"""
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''Method that return a string to print the instance.'''

        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''
        Method that updates the public instance attribute updated_at
        with the current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        Method that returns a dictionary containing all keys/values of
        __dict__ of the instance
        '''

        res = self.__dict__.copy()
        res['__class__'] = self.__class__.__name__
        res['created_at'] = datetime.isoformat(self.created_at)
        res['updated_at'] = datetime.isoformat(self.updated_at)

        return res

