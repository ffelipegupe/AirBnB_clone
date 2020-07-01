#!/usr/bin/python3
"""Unittest module for file_storage
"""
import json
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorege(unittest.TestCase):
    """FileStorage testing"""
    def setUp(self):
        """Setting up __objects and __file_path"""
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path

    def test_objects(self):
        """__objetcs testing"""
        self.assertTrue(isinstance(self.objects, dict))

    def test_file_path(self):
        """__file_path testing"""
        self.assertTrue(isinstance(self.file_path, str))

    def test_all(self):
        """all() method testing"""
        self.assertTrue(isinstance(self.objects, dict))

    def test_reload(self):
        """reload() method testing"""
        self.assertTrue(isinstance(self.objects, dict))

    def test_new(self):
        """new() method testing"""
        n_model = BaseModel()
        l = len(self.objects)
        models.storage.new(n_model)
        self.assertTrue(l == len(self.objects))

class TestBaseModelFileStorage(unittest.TestCase):
    """BaseModel->FileStorage testing"""
    def setUp(self):
        """Setting up BaseModel instance"""
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.bt = BaseModel()
        self.bt.save()

    def test_bm_update(self):
        """__objects object insertion testing"""
        self.assertIn('BaseModel.{}'.format(self.bt.id), self.objects.keys())

    def test_bm_dict(self):
        """__objects dict insertion testing"""
        bt_dict = self.bt.to_dict()
        self.assertIn(bt_dict, self.objects.values())

class TestUserFileStorage(unittest.TestCase):
    """User->FileStorage testing"""
    def setUp(self):
        """Setting up User instance"""
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.ut = User()
        self.ut.save()

    def test_u_update(self):
        """__objects object insertion testing"""
        self.assertIn('User.{}'.format(self.ut.id), self.objects.keys())

    def test_u_dict(self):
        """__objects dict insertion testing"""
        ut_dict = self.ut.to_dict()
        self.assertIn(ut_dict, self.objects.values())

class TestStateFileStorage(unittest.TestCase):
    """State->FileStorage testing"""
    def setUp(self):
        """Setting up State instance"""
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.st = State()
        self.st.save()

    def test_u_update(self):
        """__objects object insertion testing"""
        self.assertIn('State.{}'.format(self.st.id), self.objects.keys())

    def test_u_dict(self):
        """__objects dict insertion testing"""
        st_dict = self.st.to_dict()
        self.assertIn(st_dict, self.objects.values())

class TestAmenityFileStorage(unittest.TestCase):
    """Amenity->FileStorage testing"""
    def setUp(self):
        """Setting up Amenity instance"""
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.at = Amenity()
        self.at.save()

    def test_u_update(self):
        """__objects object insertion testing"""
        self.assertIn('Amenity.{}'.format(self.at.id), self.objects.keys())

    def test_u_dict(self):
        """__objects dict insertion testing"""
        at_dict = self.at.to_dict()
        self.assertIn(at_dict, self.objects.values())

class TestCityFileStorage(unittest.TestCase):
    """City->FileStorage testing"""
    def setUp(self):
        """Setting up City instance"""
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.ct = City()
        self.ct.save()

    def test_u_update(self):
        """__objects object insertion testing"""
        self.assertIn('City.{}'.format(self.ct.id), self.objects.keys())

    def test_u_dict(self):
        """__objects dict insertion testing"""
        ct_dict = self.ct.to_dict()
        self.assertIn(ct_dict, self.objects.values())

class TestReviewFileStorage(unittest.TestCase):
    """Review->FileStorage testing"""
    def setUp(self):
        """Setting up Review instance"""
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.rt = Review()
        self.rt.save()

    def test_u_update(self):
        """__objects object insertion testing"""
        self.assertIn('Review.{}'.format(self.rt.id), self.objects.keys())

    def test_u_dict(self):
        """__objects dict insertion testing"""
        rt_dict = self.rt.to_dict()
        self.assertIn(rt_dict, self.objects.values())

class TestPlaceFileStorage(unittest.TestCase):
    """Place->FileStorage testing"""
    def setUp(self):
        """Setting up Place instance"""
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path
        self.pt = Place()
        self.pt.save()

    def test_u_update(self):
        """__objects object insertion testing"""
        self.assertIn('Place.{}'.format(self.pt.id), self.objects.keys())

    def test_u_dict(self):
        """__objects dict insertion testing"""
        pt_dict = self.pt.to_dict()
        self.assertIn(pt_dict, self.objects.values())
