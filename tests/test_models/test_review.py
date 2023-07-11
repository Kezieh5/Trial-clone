#!/usr/bin/python3
"""
Unittest for review module
"""
import os
import unittest
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_Review(unittest.TestCase):
    """ Test for
    Review Class """

    r = Review()

    def setUp(self):
        """set up the
        test for testing Reviews"""
        FileStorage._FileStorage__file_path = "test.json"
        self.rev = Review()
        self.rev.place_id = "12"
        self.rev.user_id = "13"
        self.rev.text = "good"
        self.rev.save()

    def test_atrr_type_review(self):
        """test attribute for Review"""
        self.assertEqual(type(self.r.place_id), str)
        self.assertEqual(type(self.r.user_id), str)
        self.assertEqual(type(self.r.text), str)

    def test_attribute_place_id(self):
        """ Tests attr """
        self.assertEqual(hasattr(self.r, "place_id"), True)
        self.assertEqual(hasattr(self.r, "user_id"), True)
        self.assertEqual(hasattr(self.r, "text"), True)

    def test_subcls_Review(self):
        """subclass  BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)
        self.assertIsInstance(self.rev, Review)

    def test_docstring_Review(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def testpublic(self):
        self.assertEqual(str, type(Review().id))


if __name__ == "__main__":
    unittest.main()
