#!/usr/bin/python3
""" unittest for State """
from models.state import State
from models.base_model import BaseModel
import unittest


class Test_State(unittest.TestCase):
    """ unittest for State class """
    def test_name(self):
        state = State()
        self.assertEqual("", state.name)
