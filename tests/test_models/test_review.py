#!/usr/bin/python3
"""Unittest module for review
"""
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """"Review testing"""
    def setup(self):
        """Setting up an instance of Review for each case"""
        self.rt = Review()

    def test_single_id(self):
        """Testing UUID4 uniqueness"""
        n_rt = Review()
        self.assertNotEqual(self.rt.id, n_rt.id)

    def test_str_id(self):
        """Testing UUID4 convertion to string"""
        self.assertEqual(type(self.rt.id), str)

    def test_datetime_created(self):
        """Testing datetime type"""
        self.assertEqual(type(self.rt.created_at), datetime)

    def test_datetime_updated(self):
        """Testing datetime type"""
        self.assertEqual(type(self.rt.updated_at), datetime)

    def test_str(self):
        """Testing __str__ return"""
        n_str = "[BaseModel] ({}) {}".format(self.rt.id, self.rt.__dict__)
        self.assertEqual(str(self.rt), n_str)

    def test_save(self):
        """Testing date update from save method"""
        p_update = self.rt.updated_at
        self.rt.save()
        self.assertNotEqual(p_update, self.rt.updated_at)

    def test_to_dict(self):
        """Testing to_dict return and attribrtes"""
        n_to_dict = self.rt.to_dict()
        self.assertEqual(type(n_to_dict['created_at']), str)
        self.assertEqual(type(n_to_dict['updated_at']), str)
        self.assertEqual(type(n_to_dict), dict)
        self.assertTrue(hasattr(n_to_dict, '__class__'))

    def test_kargs(self):
        """Testing argument line instantation"""
        n_dict = self.rt.to_dict()
        n_rt = Review(**n_dict)
        self.assertNotEqual(self.rt, n_rt)
        self.assertEqual(self.rt.updated_at, n_rt.updated_at)
        self.assertEqual(self.rt.created_at, n_rt.created_at)
        self.assertEqual(self.rt.id, n_rt.id)

    def tearDown(self):
        """Tear down BaseModel instance before new test"""
        del self.rt
