#!/usr/bin/python3
"""Test Module that contain the test of class amenity"""


from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test class Amenity"""

    def setUp(self):
        """create a instance"""
        self.my_model = BaseModel()

    def tearDown(self):
        """ainici"""
        self.my_model = None

    def test_base_model(self):
        """check the type attributes"""
        self.my_model.name = ""
        self.my_model.my_number = 89
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertEqual(self.my_model.name, "")
        self.assertEqual(type(self.my_model.name), str)
        self.assertEqual(type(self.my_model.my_number), int)
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)

    def test_base_model_kwargs(self):
        """test kwargs"""
        attributes = {'id': "565741c1-f2f9-4bd4-8b66-b73ffe1e3d45",
                      'created_at': '2021-06-28T21:10:25.934419',
                      'updated_at': '2021-06-28T21:10:33.702066',
                      'first_name': 'Betty',
                      "last_name": "Holberton",
                      "email": "airbnb@holbertonshool.com",
                      "password": "root"}
        my_model = BaseModel(**attributes)
        self.assertEqual(my_model.id, "565741c1-f2f9-4bd4-8b66-b73ffe1e3d45")
        self.assertEqual(my_model.updated_at.isoformat(),
                         "2021-06-28T21:10:33.702066")
        self.assertEqual(my_model.created_at.isoformat(),
                         "2021-06-28T21:10:25.934419")
        self.assertEqual(my_model.first_name, "Betty")
        self.assertEqual(my_model.last_name, "Holberton")
        self.assertEqual(my_model.email, "airbnb@holbertonshool.com")
        self.assertEqual(my_model.password, "root")

    def test_diff_intance(self):
        """test to diference between atributtes instances"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        base_model3 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)
        self.assertNotEqual(base_model1.id, base_model3.id)
        self.assertNotEqual(base_model2.id, base_model3.id)
        self.assertEqual(type(base_model1.id), type(base_model2.id))
        self.assertNotIn("name", base_model1.__dict__)


if __name__ == "__main__":
    unittest.main()
