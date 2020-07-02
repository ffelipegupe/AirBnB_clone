#!/usr/bin/python3
"""FileStorage class module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ FileStorage class body """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return __objects dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        keyobj = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[keyobj] = obj

    def save(self):
        """  Serializes __objects to the JSON file (path: __file_path) """
        dicobj = {}
        for key in self.__objects.keys():
            dicobj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dicobj, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as f:
                objdic = json.load(f)
                for key, obj in objdic.items():
                    self.__objects[key] = eval(obj['__class__'])(obj)
        except FileNotFoundError:
            pass
