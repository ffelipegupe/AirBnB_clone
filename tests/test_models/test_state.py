#!/usr/bin/python3
"""Unittest module for state
"""
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """"State testing"""
    def setup(self):
        """Setting up an instance of State for each case"""
        self.st = State()

    def test_single_id(self):
        """Testing UUID4 uniqueness"""
        n_st = State()
        self.assertNotEqual(self.st.id, n_st.id)

    def test_str_id(self):
        """Testing UUID4 convertion to string"""
        self.assertEqual(type(self.st.id), str)

    def test_datetime_created(self):
        """Testing datetime type"""
        self.assertEqual(type(self.st.created_at), datetime)

    def test_datetime_updated(self):
        """Testing datetime type"""
        self.assertEqual(type(self.st.updated_at), datetime)

    def test_str(self):
        """Testing __str__ return"""
        n_str = "[BaseModel] ({}) {}".format(self.st.id, self.st.__dict__)
        self.assertEqual(str(self.st), n_str)

    def test_save(self):
        """Testing date update from save method"""
        p_update = self.st.updated_at
        self.st.save()
        self.assertNotEqual(p_update, self.st.updated_at)

    def test_to_dict(self):
        """Testing to_dict return and attribstes"""
        n_to_dict = self.st.to_dict()
        self.assertEqual(type(n_to_dict['created_at']), str)
        self.assertEqual(type(n_to_dict['updated_at']), str)
        self.assertEqual(type(n_to_dict), dict)
        self.assertTrue(hasattr(n_to_dict, '__class__'))

    def test_kargs(self):
        """Testing argument line instantation"""
        n_dict = self.st.to_dict()
        n_st = State(**n_dict)
        self.assertNotEqual(self.st, n_st)
        self.assertEqual(self.st.updated_at, n_st.updated_at)
        self.assertEqual(self.st.created_at, n_st.created_at)
        self.assertEqual(self.st.id, n_st.id)

    def tearDown(self):
        """Tear down BaseModel instance before new test"""
        del self.st
