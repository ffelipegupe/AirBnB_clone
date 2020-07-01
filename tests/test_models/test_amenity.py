#!/usr/bin/python3
"""Unittest module for amenity
"""
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """"Amenity testing"""
    def setup(self):
        """Setting up an instance of Amenity for each case"""
        self.at = Amenity()

    def test_single_id(self):
        """Testing UUID4 uniqueness"""
        n_at = Amenity()
        self.assertNotEqual(self.at.id, n_at.id)

    def test_str_id(self):
        """Testing UUID4 convertion to string"""
        self.assertEqual(type(self.at.id), str)

    def test_datetime_created(self):
        """Testing datetime type"""
        self.assertEqual(type(self.at.created_at), datetime)

    def test_datetime_updated(self):
        """Testing datetime type"""
        self.assertEqual(type(self.at.updated_at), datetime)

    def test_str(self):
        """Testing __str__ return"""
        n_str = "[BaseModel] ({}) {}".format(self.at.id, self.at.__dict__)
        self.assertEqual(str(self.at), n_str)

    def test_save(self):
        """Testing date update from save method"""
        p_update = self.at.updated_at
        self.at.save()
        self.assertNotEqual(p_update, self.at.updated_at)

    def test_to_dict(self):
        """Testing to_dict return and attribates"""
        n_to_dict = self.at.to_dict()
        self.assertEqual(type(n_to_dict['created_at']), str)
        self.assertEqual(type(n_to_dict['updated_at']), str)
        self.assertEqual(type(n_to_dict), dict)
        self.assertTrue(hasattr(n_to_dict, '__class__'))

    def test_kargs(self):
        """Testing argument line instantation"""
        n_dict = self.at.to_dict()
        n_at = Amenity(**n_dict)
        self.assertNotEqual(self.at, n_at)
        self.assertEqual(self.at.updated_at, n_at.updated_at)
        self.assertEqual(self.at.created_at, n_at.created_at)
        self.assertEqual(self.at.id, n_at.id)

    def tearDown(self):
        """Tear down BaseModel instance before new test"""
        del self.at
