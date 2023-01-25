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
        except:
            pass
        del self.base
        del self.store

    def test_all(self):
        """test"""
        store_dict = self.store.all()
        self.assertIsInstance(store_dict, dict)

    def test_news(self):
        """test"""
        for item in self.store.all().values():
            same = item
        self.assertTrue(same is item)

    def test_saver(self):
        """saver"""
        self.base.save()
        self.assertTrue(self.store._FileStorage__objects
                            .get(f"BaseModel.{self.base.id}"))

    # def test_reload(self):
    #     """reload"""
    #     self.store.save()
    #     self.store.reload()
    #     for obj in self.store.all().values():
    #         load = obj
    #     self.assertEqual(self.base.to_dict()['id'], load.to_dict()['id'])

    def test_model(self):
        """model"""
        # with open('file.json', 'w') as f:
        #     pass
        # with self.assertRaises(ValueError):
        #     self.store.reload()
        # with open("file.json", "w") as f:
        #     f.write("{}")
        # with open("file.json", "r") as r:
        #     for line in r:
        #         self.assertEqual(line, "{}")
        # self.assertIs(self.store.reload(), None)
        self.store.save()
        self.store.reload()
        self.assertTrue(len(self.store.all()) > 0)
