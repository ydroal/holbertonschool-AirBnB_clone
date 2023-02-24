import unittest
import os
import json
from models import storage
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
        self.assertEqual(os.path.isfile('file.json'), True)
        with open(self.fs._FileStorage__file_path) as f:
            saved_dict = json.load(f)
        self.assertIn('BaseModel.' + obj.id, saved_dict)

    def test_object(self):
        object_dict = FileStorage._FileStorage__objects
        self.assertEqual(dict, type(object_dict))

    # Test __file path is exit
    def test_file_path(self):
        path = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(path))

    # Test the reload() method
    def test_reload(self):
        """ test for file storage reloading """
        self.fs.save()
        s = FileStorage()
        s.reload()
        kx = s.all().keys()
        ky = self.fs.all().keys()
        self.assertTrue(kx, ky)


if __name__ == "__main__":
    unittest.main()
