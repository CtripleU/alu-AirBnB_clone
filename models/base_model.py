#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

"""
Module BaseModel
defines all common attributes/methods for other classes
"""


class BaseModel():
    """
    Base class for project
    """

    def __init__(self, *args, **kwargs):
        """Initialization"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    pass
                elif k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """human readable representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns dict containing all keys/values of instance"""
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for attr in self.__dict__:
            if attr == "created_at" or attr == "updated_at":
                my_dict[attr] = getattr(self, attr).isoformat()
            else:
                my_dict[attr] = getattr(self, attr)
        return my_dict
