#!/usr/bin/python3
'''Unit test for BaseModel class'''

import unittest
import datetime
import os
import json
from uuid import UUID
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    '''Test class for BaseModel'''

    def __init__(self, *args, **kwargs):
        """ This ensures that the parent class is initialized correctly """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel


    def test_id(self):
        "testing id"
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_str(self):
        """ testing str """
        y = self.value()
        self.assertEqual(str(y), '[{}] ({}) {}'.format(self.name, y.id,
                                                       y.__dict__))

    def test_to_dict(self):
        """ testing to_dict """
        base = BaseModel()
        r_dict = base.to_dict()
        self.assertIsInstance(r_dict, dict)
        self.assertTrue("__class__" in r_dict)
        self.assertEqual(r_dict["__class__"], type(base).__name__)

    def test_save(self):
        """ testing save """
        y = self.value()
        y.save()
        k = self.name + '.' + y.id
        with open('file.json', 'r') as f:
            # json file to dict
            j = json.load(f)
            self.assertEqual(j[k], y.to_dict())


if __name__ == '__main__':
    unittest.main()
