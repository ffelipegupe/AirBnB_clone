#!/usr/bin/python3
"""Unittest module for place
"""
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """"Place testing"""
    def setup(self):
        """Setting up an instance of Place for each case"""
        self.pt = Place()

    def test_single_id(self):
        """Testing UUID4 uniqueness"""
        n_pt = Place()
        self.assertNotEqual(self.pt.id, n_pt.id)

    def test_str_id(self):
        """Testing UUID4 convertion to string"""
        self.assertEqual(type(self.pt.id), str)

    def test_datetime_created(self):
        """Testing datetime type"""
        self.assertEqual(type(self.pt.created_at), datetime)

    def test_datetime_updated(self):
        """Testing datetime type"""
        self.assertEqual(type(self.pt.updated_at), datetime)

    def test_str(self):
        """Testing __str__ return"""
        n_str = "[BaseModel] ({}) {}".format(self.pt.id, self.pt.__dict__)
        self.assertEqual(str(self.pt), n_str)

    def test_save(self):
        """Testing date update from save method"""
        p_update = self.pt.updated_at
        self.pt.save()
        self.assertNotEqual(p_update, self.pt.updated_at)

    def test_to_dict(self):
        """Testing to_dict return and attribptes"""
        n_to_dict = self.pt.to_dict()
        self.assertEqual(type(n_to_dict['created_at']), str)
        self.assertEqual(type(n_to_dict['updated_at']), str)
        self.assertEqual(type(n_to_dict), dict)
        self.assertTrue(hasattr(n_to_dict, '__class__'))

    def test_kargs(self):
        """Testing argument line instantation"""
        n_dict = self.pt.to_dict()
        n_pt = Place(**n_dict)
        self.assertNotEqual(self.pt, n_pt)
        self.assertEqual(self.pt.updated_at, n_pt.updated_at)
        self.assertEqual(self.pt.created_at, n_pt.created_at)
        self.assertEqual(self.pt.id, n_pt.id)

    def tearDown(self):
        """Tear down BaseModel instance before new test"""
        del self.pt
