#!/usr/bin/python3
"""
Test module
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from io import StringIO
from contextlib import redirect_stdout
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Test"""

    def test_to_dict(self):
        """test to_dict method"""

        copy = BaseModel()
        copy_dict = copy.to_dict()
        self.assertIsInstance(copy_dict["created_at"], str)

    def test_unique_id(self):
        """test id uniqueness"""
        copy = BaseModel()
        copy_2 = BaseModel()
        self.assertNotEqual(copy.id, copy_2.id)

    def test_created_at(self):
        """test created_at attribute"""
        copy = BaseModel()
        self.assertIsInstance(copy.created_at, datetime)

    def test_str(self):
        """test str method"""
        with StringIO() as bufr, redirect_stdout(bufr):
            my_cop = BaseModel()
            print(my_cop.__str__())
            a = bufr.getvalue()
        self.assertIn(
            f'[{my_cop.__class__.__name__}] ({my_cop.id}) {my_cop.__dict__}',
            a)

    def test_save(self):
        """test save()"""
        copy = BaseModel()
        sleep(1)
        # copy_1.name = "James"
        copy.save()
        self.assertNotEqual(copy.created_at, copy.updated_at)


if __name__ == "__main__":
    unittest.main()
