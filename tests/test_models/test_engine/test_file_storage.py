#!/usr/bin/python3
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    '''Test class for BaseModel'''
    # set up the test environment
    def setUp(self):
        self.fs = FileStorage()

    # clean up resource file that created by test method
    def tearDown(self):
        if os.path.exists(self.fs._FileStorage__file_path):
            os.remove(self.fs._FileStorage__file_path)

    # Test create FireStorage instance
    def test_create_instance(self):
        self.assertIsInstance(self.fs, FileStorage)

    # Test the all() method
    def test_all(self):
        obj_dict = self.fs.all()
        self.assertEqual(type(obj_dict), dict)

    # Test the new() method
    def test_new(self):
        obj = BaseModel()
        self.fs.new(obj)
        obj_dict = self.fs.all()
        self.assertIn('BaseModel.' + obj.id, obj_dict)

    # Test the save() method
    def test_save(self):
        obj = BaseModel()
        self.fs.new(obj)
        self.fs.save()
        with open(self.fs._FileStorage__file_path) as f:
            saved_dict = json.load(f)
        self.assertIn('BaseModel.' + obj.id, saved_dict)

    # Test the reload() method
    def test_reload(self):
        obj = BaseModel()
        self.fs.new(obj)
        self.fs.save()
        self.fs.reload()
        obj_dict = self.fs.all()
        self.assertIn('BaseModel.' + obj.id, obj_dict)

if __name__ == '__main__':
    unittest.main()
