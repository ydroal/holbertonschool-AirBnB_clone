#!/usr/bin/python3
'''Module to define a FileStorage'''

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''Define a FileStorage'''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Method returns the dictionary __objects'''

        return FileStorage.__objects

    def new(self, obj):
        '''Method sets in __objects the obj with key <obj class name>.id'''
        if obj:
            k = f'{obj.__class__.__name__}.{obj.id}'
            self.__objects[k] = obj

    def save(self):
        '''Method serializes __objects to the JSON file (path: __file_path)'''

        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        '''
        Method that deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn't exist, no exception should be raised)
        '''

        try:
            with open(FileStorage.__file_path, encoding="utf-8") as json_file2:
                new_dict = json.load(json_file2)
                cls = '__class__'
                for key, value in new_dict.items():
                    self.__objects[key] = eval(value[cls] + '(**value)')
        except FileNotFoundError:
            pass
