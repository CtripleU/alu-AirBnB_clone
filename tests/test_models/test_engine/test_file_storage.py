#!/usr/bin/python
"""
Test for file storage
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """test"""
    def setUp(self):
        """setup"""
        self.base = BaseModel()
        self.store = FileStorage()

    def teardown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_save_reload(self):
        """ test save and reload from json """
        self.base.name = "Bond"
        self.base.my_number = 7
        name = str(self.base.__class__.__name__)
        key = f"{name}.{str(self.base.id)}"
        self.base.save()
        self.assertTrue(os.path.exists('file.json'))
        self.store.reload()
        obj = self.store.all()
        self.assertIsNotNone(obj[key])
        self.obj_reload = obj[key]
        self.assertTrue(self.base.__dict__ == self.obj_reload.__dict__)
        self.assertIsInstance(self.obj_reload, BaseModel)
        self.assertTrue(self.base is not self.obj_reload)
        self.assertTrue(self.base.created_at != self.base.updated_at)


class TestSave(unittest.TestCase):
    """doc"""
    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))
