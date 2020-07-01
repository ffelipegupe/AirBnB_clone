#!/usr/bin/python3
"""Unittest module for user
"""
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """"User testing"""
    def setup(self):
        """Setting up an instance of User for each case"""
        self.ut = User()

    def test_single_id(self):
        """Testing UUID4 uniqueness"""
        n_ut = User()
        self.assertNotEqual(self.ut.id, n_ut.id)

    def test_str_id(self):
        """Testing UUID4 convertion to string"""
        self.assertEqual(type(self.ut.id), str)

    def test_datetime_created(self):
        """Testing datetime type"""
        self.assertEqual(type(self.ut.created_at), datetime)

    def test_datetime_updated(self):
        """Testing datetime type"""
        self.assertEqual(type(self.ut.updated_at), datetime)

    def test_str(self):
        """Testing __str__ return"""
        n_str = "[BaseModel] ({}) {}".format(self.ut.id, self.ut.__dict__)
        self.assertEqual(str(self.ut), n_str)

    def test_save(self):
        """Testing date update from save method"""
        p_update = self.ut.updated_at
        self.ut.save()
        self.assertNotEqual(p_update, self.ut.updated_at)

    def test_to_dict(self):
        """Testing to_dict return and attributes"""
        n_to_dict = self.ut.to_dict()
        self.assertEqual(type(n_to_dict['created_at']), str)
        self.assertEqual(type(n_to_dict['updated_at']), str)
        self.assertEqual(type(n_to_dict), dict)
        self.assertTrue(hasattr(n_to_dict, '__class__'))

    def test_kargs(self):
        """Testing argument line instantation"""
        n_dict = self.ut.to_dict()
        n_ut = User(**n_dict)
        self.assertNotEqual(self.ut, n_ut)
        self.assertEqual(self.ut.updated_at, n_ut.updated_at)
        self.assertEqual(self.ut.created_at, n_ut.created_at)
        self.assertEqual(self.ut.id, n_ut.id)

    def tearDown(self):
        """Tear down BaseModel instance before new test"""
        del self.ut
