#!/usr/bin/python3
""" unittest for City file """
from models.base_model import BaseModel
from models.city import City
import unittest


class Test_City(unittest.TestCase):
    """ unittest for city class """
    def test_city(self):
        city = City()
        self.assertEqual("", city.name)

        self.assertEquam("", city.state_id)
