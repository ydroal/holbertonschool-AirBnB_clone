#!/usr/bin/python3
""" unittest for review file """
from models.base_model import BaseModel
from models.review import Review
import unittest


class Test_Review(unittest.TestCase):
    """ unittest for Review class """
    def test_review(self):
        review = Review
        self.assertEqual("", review.place_id)

        self.assertEqual("", review.user_id)

        self.assertEqual("", review.text)
