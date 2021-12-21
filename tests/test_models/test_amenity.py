#!/usr/bin/python3
"""Test Module that contain the test of class amenity"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test class Amenity"""

    def setUp(self):
        """create a instance"""
        self.new_amenity = Amenity()

    def tearDown(self):
        """check the type attributes"""
        self.new_amenity = None

    def test_amenity(self):
        """check the type attributes"""
        self.assertIsInstance(self.new_amenity, Amenity)
        self.assertEqual(type(self.new_amenity.name), str)
        self.assertEqual(self.new_amenity.name, "")
