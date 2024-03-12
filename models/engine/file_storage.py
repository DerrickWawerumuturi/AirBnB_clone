#!/usr/bin/python3
"""
    Define class FileStorage Module
"""
import json
from models.base_model import BaseModel
from models.user import User
import os


class FileStorage:
    """
        Serializes instances to JSON file and deserializes to JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Return the dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Set new obj into __objects
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        Serializes the objects into JSON file
        """
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

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
