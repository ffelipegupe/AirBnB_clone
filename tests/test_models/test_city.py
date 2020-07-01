#!/usr/bin/python3
"""Unittest module for city
"""
import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """"City testing"""
    def setup(self):
        """Setting up an instance of City for each case"""
        self.ct = City()

    def test_single_id(self):
        """Testing UUID4 uniqueness"""
        n_ct = City()
        self.assertNotEqual(self.ct.id, n_ct.id)

    def test_str_id(self):
        """Testing UUID4 convertion to string"""
        self.assertEqual(type(self.ct.id), str)

    def test_datetime_created(self):
        """Testing datetime type"""
        self.assertEqual(type(self.ct.created_at), datetime)

    def test_datetime_updated(self):
        """Testing datetime type"""
        self.assertEqual(type(self.ct.updated_at), datetime)

    def test_str(self):
        """Testing __str__ return"""
        n_str = "[BaseModel] ({}) {}".format(self.ct.id, self.ct.__dict__)
        self.assertEqual(str(self.ct), n_str)

    def test_save(self):
        """Testing date update from save method"""
        p_update = self.ct.updated_at
        self.ct.save()
        self.assertNotEqual(p_update, self.ct.updated_at)

    def test_to_dict(self):
        """Testing to_dict return and attribctes"""
        n_to_dict = self.ct.to_dict()
        self.assertEqual(type(n_to_dict['created_at']), str)
        self.assertEqual(type(n_to_dict['updated_at']), str)
        self.assertEqual(type(n_to_dict), dict)
        self.assertTrue(hasattr(n_to_dict, '__class__'))

    def test_kargs(self):
        """Testing argument line instantation"""
        n_dict = self.ct.to_dict()
        n_ct = City(**n_dict)
        self.assertNotEqual(self.ct, n_ct)
        self.assertEqual(self.ct.updated_at, n_ct.updated_at)
        self.assertEqual(self.ct.created_at, n_ct.created_at)
        self.assertEqual(self.ct.id, n_ct.id)

    def tearDown(self):
        """Tear down BaseModel instance before new test"""
        del self.ct
