
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """private class attributes 
    
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns private class attribute"""
        return FileStorage.__objects
    """
    purpose: serializes __objects to the JSON fiel
    """
    def new(self, obj):
        """
        method to set in __objects, the obj with key <obj class name>.id
        Args:
            obj: the object to be set
        """
        if obj:
            key = "{}{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] =  obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path,"w", encoding="utf-8") as json_file:
            objects_json = (
                {k: v.to_dict() for k, v in
                    FileStorage.__objects.items()}
            )
            json.dump(objects_json, json_file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; 
        otherwise, do nothing. 
        If the file doesnt exist, no exception should be raised
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as myFile:
                for k, v in json.load(myFile).items():
                    instance = eval(v['__class__'])(**v)
                    self.__objects[k] = instance

