#!/usr/bin/python3
""" Tests for amenity class"""
import unittest
import models
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from sqlalchemy.exc import OperationalError
from os import getenv


class test_Amenity(unittest.TestCase):
    """ Define tests for Amenity class"""

    def __init__(self, *args, **kwargs):
        """ Initialisation of Amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "not supported")
    def test_no_name(self):
        """ Check for mandatory arguments"""
        new = self.value()
        with self.assertRaises(OperationalError):
            try:
                new.save()
            except Exception as error:
                models.storage._DBStorage__session.rollback()
                raise error

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "not supported")
    def test_amenity_instance(self):
        """ Check that amenity is an instance of Amenity class"""
        amenity = self.value()
        self.assertTrue(isinstance(amenity, Amenity))
