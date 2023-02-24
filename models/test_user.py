#!/usr/bin/python3
""" unittest for user file """
from models.base_model import BaseModel
from models.user import user
import email
import unittest


class Test_User(unittest.TestCase):
    """ unittest for user class """
    user = User
    self.assertEqual("", user.email)

    self.assertEqual("", user.password)

    self.assertEqual("", user.first_name)

    self.assertEqual("", user.last_name)
