#!/usr/bin/python3
""" unitest for testing BaseModel class """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ Unittests for testing the basemodel class"""

    def __init__(self, *args, **kwargs):
        """ Unittests for testing the basemodel class"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Unittests for testing the basemodel class"""
        pass

    def tearDown(self):
        """ Unittests for testing the basemodel class"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ Unittests for testing the basemodel class"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Unittests for testing the basemodel class"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ Unittests for testing the basemodel class"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Unittests for testing the basemodel class"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ Unittests for testing the basemodel class"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ Unittests for testing the basemodel class"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Unittests for testing the basemodel class"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ Unittests for testing the basemodel class"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ Unittests for testing the basemodel class"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Unittests for testing the basemodel class"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Unittests for testing the basemodel class"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
