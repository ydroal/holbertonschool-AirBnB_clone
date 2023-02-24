#!/usr/bin/python3
""" unittest for amenity file """
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


def Test_Amenity(unitest.TestCase):
    """ unittest for amenity class """
    amenity = Amenity()
    self.assertEqual("", amenity.name)
