#!/usr/bin/python3
"""importing modules"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

"""creating a class to handle storage in a file"""


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        method to return dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        method to set in __objects, the obj with key <obj class name>.id
        Args:
            obj: the object to be set
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        method that serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as myFile:
            objects_json = (
                    {k: v.to_dict() for k, v in
                        FileStorage.__objects.items()}
                    )
            json.dump(objects_json, myFile)

    def reload(self):
        """
        method that deserializes the JSOn file to __objects (only
        if the JSON file (__file_path) exists; otherwise, do nothing
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as myFile:
                for k, v in json.load(myFile).items():
                    instance = eval(v['__class__'])(**v)
                    self.__objects[k] = instance