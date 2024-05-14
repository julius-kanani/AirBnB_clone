#!/usr/bin/python3
""" The test_place module. """


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def test_place_default_attributes(self):
        """
        Test default attributes of the Place instance.
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_city_id(self):
        """
        Test setting and getting the city_id attribute of the Place instance.
        """
        place = Place()
        place.city_id = "123"
        self.assertEqual(place.city_id, "123")

    def test_place_user_id(self):
        """
        Test setting and getting the user_id attribute of the Place instance.
        """
        place = Place()
        place.user_id = "456"
        self.assertEqual(place.user_id, "456")

    def test_place_name(self):
        """
        Test setting and getting the name attribute of the Place instance.
        """
        place = Place()
        place.name = "Cozy Apartment"
        self.assertEqual(place.name, "Cozy Apartment")

    def test_place_description(self):
        """
        Test setting and getting the description attribute of the Place
        instance.
        """
        place = Place()
        place.description = "Beautiful view of the mountains"
        self.assertEqual(place.description, "Beautiful view of the mountains")

    def test_place_number_rooms(self):
        """
        Test setting and getting the number_rooms attribute of the Place
        instance.
        """
        place = Place()
        place.number_rooms = 2
        self.assertEqual(place.number_rooms, 2)

    def test_place_number_bathrooms(self):
        """
        Test setting and getting the number_bathrooms attribute of the Place
        instance.
        """
        place = Place()
        place.number_bathrooms = 1
        self.assertEqual(place.number_bathrooms, 1)

    def test_place_max_guest(self):
        """
        Test setting and getting the max_guest attribute of the Place instance.
        """
        place = Place()
        place.max_guest = 4
        self.assertEqual(place.max_guest, 4)

    def test_place_price_by_night(self):
        """
        Test setting and getting the price_by_night attribute of the Place
        instance.
        """
        place = Place()
        place.price_by_night = 100
        self.assertEqual(place.price_by_night, 100)

    def test_place_latitude(self):
        """
        Test setting and getting the latitude attribute of the Place instance.
        """
        place = Place()
        place.latitude = 40.7128
        self.assertEqual(place.latitude, 40.7128)

    def test_place_longitude(self):
        """
        Test setting and getting the longitude attribute of the Place instance.
        """
        place = Place()
        place.longitude = -74.0060
        self.assertEqual(place.longitude, -74.0060)

    def test_place_amenity_ids(self):
        """
        Test setting and getting the amenity_ids attribute of the Place
        instance.
        """
        place = Place()
        place.amenity_ids = ["123", "456", "789"]
        self.assertEqual(place.amenity_ids, ["123", "456", "789"])


if __name__ == '__main__':
    unittest.main()
