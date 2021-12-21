#!/usr/bin/python3
"""Test Module that contain the test of class amenity"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ test class city """

    def setUp(self):
        """create a instance"""
        self.new_city = City()

    def test_city(self):
        """check the type attributes"""
        self.assertEqual(type(self.new_city.state_id), str)
        self.assertEqual(type(self.new_city.name), str)
