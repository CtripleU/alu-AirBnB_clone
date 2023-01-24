#!/usr/bin/python3
"""
Tests for User
"""

import unittest
import models
from models.user import User


class TestUser(unittest.TestCase):
    """Test"""
     
    def setUp(self):
        self.user = User()

    def test_email(self):
        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, "")

    def test_password(self):
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(self.user.password, "")

    def test_first_name(self):
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(self.user.first_name, "")     

    def test_last_name(self):
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(self.user.last_name, "")     


if __name__ == "__main__":
    unittest.main()
