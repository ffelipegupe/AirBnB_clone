#!/usr/bin/python3
"""Unittest module for basemodel
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """"BaseModel testing"""
    def setup(self):
        """Setting up an instance of BaseModel for each case"""
        self.bt = BaseModel()

    def test_single_id(self):
        """Testing UUID4 uniqueness"""
        n_bt = BaseModel()
        self.assertNotEqual(self.bt.id, n_bt.id)

    def test_str_id(self):
        """Testing UUID4 convertion to string"""
        self.assertEqual(type(self.bt.id), str)

    def test_datetime_created(self):
        """Testing datetime type"""
        self.assertEqual(type(self.bt.created_at), datetime)

    def test_datetime_updated(self):
        """Testing datetime type"""
        self.assertEqual(type(self.bt.updated_at), datetime)

    def test_str(self):
        """Testing __str__ return"""
        n_str = "[BaseModel] ({}) {}".format(self.bt.id, self.bt.__dict__)
        self.assertEqual(str(self.bt), n_str)

    def test_save(self):
        """Testing date update from save method"""
        p_update = self.bt.updated_at
        self.bt.save()
        self.assertNotEqual(p_update, self.bt.updated_at)

    def test_to_dict(self):
        """Testing to_dict return and attributes"""
        n_to_dict = self.bt.to_dict()
        self.assertEqual(type(n_to_dict['created_at']), str)
        self.assertEqual(type(n_to_dict['updated_at']), str)
        self.assertEqual(type(n_to_dict), dict)
        self.assertTrue(hasattr(n_to_dict, '__class__'))

    def test_kargs(self):
        """Testing argument line instantation"""
        n_dict = self.bt.to_dict()
        n_bt = BaseModel(**n_dict)
        self.assertNotEqual(self.bt, n_bt)
        self.assertEqual(self.bt.updated_at, n_bt.updated_at)
        self.assertEqual(self.bt.created_at, n_bt.created_at)
        self.assertEqual(self.bt.id, n_bt.id)

    def tearDown(self):
        """Tear down BaseModel instance before new test"""
        del self.bt
