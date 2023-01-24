#!/usr/bin/python3
"""
Tests for State
"""

import unittest
import pep8
from datetime import datetime
from io import StringIO
from contextlib import redirect_stdout
import models
from models.state import State


class TestState(unittest.TestCase):
    """Tests"""
     
    def setUp(self):
        self.state = State()

    def test_state_init(self):
        """
        1. test that a new instance of the class 'State' is created correctly
        2. test that the 'name' attribute of the State object is an instance of the str class
        3. test that the initial value of 'name' attribute is an empty string
        """
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.user.name, str)
        self.asserEqual(self.state.name, "")

    def test_name_setter(self):
        """
        1. test that the 'name' attribute can be set to a new value correctly
        """
        self.state.name = "Lagos"
        self.assertEqual(self.state.name, "Lagos")

    def test_name_getter(self):
        """
        1. test that the 'name' attribute gets the correct value
        """
        self.state.name = "Enugu"
        self.assertEqual(self.state.name, "Enugu")

    def test_state_pep8(self):
        """test that state.py is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        """test that this file is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/tests_models/test_state.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

if __name__ == "__main__":
    unittest.main()

