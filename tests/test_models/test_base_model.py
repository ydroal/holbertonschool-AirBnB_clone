#!/usr/bin/python3
'''Unit test for BaseModel class'''

import unittest
import datetime
import os
import json
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    '''Test class for BaseModel'''

    def setUp(self):
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    # clean up resource file that created by test method
    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_id(self):
        # IDs are unique
        self.assertNotEqual(self.base1.id, self.base2.id)

    def test_created_at(self):
        self.assertNotEqual(self.base1.created_at, self.base2.created_at)
        self.assertEqual(type(self.base1.created_at), datetime.datetime)

    def test_str(self):
        self.base1.name = 'My First Model'
        self.base1.my_number = 89
        output = str(self.base1)
        self.assertEqual(output[:11], '[BaseModel]')
        target = "'my_number': 89"
        self.assertTrue(target in output)

    def test_to_dict(self):
        self.base1.name = 'My First Model'
        self.base1.my_number = 89
        dict1 = self.base1.to_dict()
        self.assertEqual(dict1['__class__'], 'BaseModel')
        self.assertEqual(dict1['name'], 'My First Model')
        self.assertEqual(dict1['my_number'], 89)

    def test_save(self):
        self.base1.save()
        k = 'BaseModel' + '.' + self.base1.id
        with open('file.json') as f:
            # json file to dict
            j = json.load(f)
            self.assertEqual(j[k], self.base1.to_dict())


if __name__ == '__main__':
    unittest.main()
