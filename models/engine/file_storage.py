#!/usr/bin/python3
'''Module to define a FileStorage'''

import json
from models.base_model import BaseModel


class FileStorage:
    '''Define a FileStorage'''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Method returns the dictionary __objects'''

        return self.__objects

    def new(self, obj):
        '''Method sets in __objects the obj with key <obj class name>.id'''

        k = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[k] = obj

    def save(self):
        '''Method serializes __objects to the JSON file (path: __file_path)'''

        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'a') as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        '''
        Method that deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn't exist, no exception should be raised)
        '''

        try:
            with open(self.__file_path) as f:
                new_dict = json.load(f)
                cls = '__class__'
                for key, value in new_dict.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(value[cls] + '(**value)')
        except FileNotFoundError:
            pass
