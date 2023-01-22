#!/usr/bin/python3
"""
FileStorage Module
"""

import json
from models.base_model import BaseModel
import os


class FileStorage():
    """serializes instances to a JSON file and
       deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for k, ob in self.__objects.items():
            new_dict[k] = ob.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        new_obj_dict = {}
        try:
            with open(self.__file_path, mode="r", encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
                for k, v in new_obj_dict.items():
                    self.__objects[k] = eval(v["__class__"])(**v)
                    # above is similar to self.__objects[k] = BaseModel(**v)
        except FileNotFoundError:
            pass
        # if os.path.isfile(self.__file_path):
        #     with open(self.__file_path, mode="r", encoding="UTF-8") as f:
        #         new_obj_dict = json.load(f)
        #         for k, v in new_obj_dict.items():
        #             self.__objects[k] = BaseModel(**v)
