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
    def test_instanciates(self):
        self.assertIsInstance(self.fs, FileStorage)

    # Test if __file path is exit
    def test_file_path(self):
        path = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(path))

    # Test __object is type dict after deserialization
    def test_object(self):
        object_dict = FileStorage._FileStorage__objects
        self.assertEqual(dict, type(object_dict))

    # Test all() method
    def test_all(self):
        obj_dict = self.fs.all()
        self.assertEqual(type(obj_dict), dict)


if __name__ == "__main__":
    unittest.main()
