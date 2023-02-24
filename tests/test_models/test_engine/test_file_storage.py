#!/usr/bin/python3
"""Unit tests for FileStorage class"""


import unittest
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel
import json
import models
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Unittests for FileStorage"""

    my_model = BaseModel()

    def test_instanciates(self):
        "Tests that FileStorage correctly instanciates"
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """Test __file path is exited"""
        path = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(path))

    def test_object(self):
        """Test __object is type dict after deserialization object - dict"""
        object_dict = FileStorage._FileStorage__objects
        self.assertEqual(dict, type(object_dict))

    def test_all(self):
        """Test FileStorage: all()"""
        dict_return = {}
        FileStorage.all(None)
        self.assertEqual(os.path.isfile('file.json'), True)

if __name__ == "__main__":
    unittest.main()
