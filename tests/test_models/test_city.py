#!/usr/bin/python3
"""
Tests for City
"""

import unittest
import pep8
from datetime import datetime
import models
from models.city import City

class TestCity(unittest.TestCase):
    """Tests"""
     
    def setUp(self):
        self.city = City()

    def test_city_init(self):
        """
        1. test that a new instance of the class 'City' is created correctly
        2. test that the 'name' attribute of the City object is an instance of the str class
        3. test that the 'state_id' attribute of the City object is an instance of the str class
        4. test that the initial value of 'state_id' attribute is an empty string
        5. test that the initial value of 'name' attribute is an empty string
        """
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)
        self.asserEqual(self.city.state_id, "")
        self.asserEqual(self.city.name, "")

    def test_name_setter(self):
        """
        test that the 'name' attribute can be set to a new value correctly
        """
        self.city.name = "Onitsha"
        self.assertEqual(self.city.name, "Onitsha")

    def test_name_getter(self):
        """
        test that the 'name' attribute gets the correct value
        """
        self.city.name = "Port Harcourt"
        self.assertEqual(self.city.name, "Port Harcourt")

    def test_city_pep8(self):
        """test that city.py is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        """test that this file is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/tests_models/test_city.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

if __name__ == "__main__":
    unittest.main()
