#!/usr/bin/python3
"""
Tests for Place
"""

import unittest
import pep8
from datetime import datetime
import models
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests"""

    def setUp(self):
        self.place = Place()

    def test_city_id(self):
        """
        1. test that the city_id attribute of the
           Place object is an instance of the str class
        2. test that the city_id atttribute has the value of an empty string
        """
        self.assertIsInstance(self.place.city_id, str)
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """
        1. test that the user_id attribute of the
           Place object is an instance of the str class
        2. test that the user_id atttribute has the value of an empty string
        """
        self.assertIsInstance(self.place.user_id, str)
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """
        1. test that the name attribute of the
           Place object is an instance of the str class
        2. test that the name atttribute has the value of an empty string
        """
        self.assertIsInstance(self.place.name, str)
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """
        1. test that the description attribute of the
           Place object is an instance of the str class
        2. test that the description atttribute has the
           value of an empty string
        """
        self.assertIsInstance(self.place.description, str)
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """
        1. test that the number_rooms attribute of the
           Place object is an instance of the int class
        2. test that the number_rooms atttribute has the value of 0
        """
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """
        1. test that the number_bathrooms attribute of the
           Place object is an instance of the int class
        2. test that the number_bathrooms atttribute has the value of 0
        """
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """
        1. test that the max_guest attribute of the
           Place object is an instance of the int class
        2. test that the max_guest atttribute has the value of 0
        """
        self.assertIsInstance(self.place.max_guest, int)
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """
        1. test that the price_by_night attribute of the
           Place object is an instance of the int class
        2. test that the price_by_night atttribute has the value of 0
        """
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """
        1. test that the latitude attribute of the
           Place object is an instance of the float class
        2. test that the latitude atttribute has the value of 0.0
        """
        self.assertIsInstance(self.place.latitude, float)
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """
        1. test that the longitude attribute of the
           Place object is an instance of the float class
        2. test that the longitude atttribute has the value of 0.0
        """
        self.assertIsInstance(self.place.longitude, float)
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """
        1. test that the amenity_ids attribute of the
           Place object is an instance of the list class
        2. test that the amenity_ids atttribute has the value of an empty list
        """
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_pep8(self):
        """test that place.py is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")

    def test_pep8(self):
        """test that this file is PEP8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 errors found")


if __name__ == "__main__":
    unittest.main()
