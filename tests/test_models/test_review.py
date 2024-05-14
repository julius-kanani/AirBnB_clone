#!/usr/bin/python3
""" The test_review module. """


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def test_review_default_attributes(self):
        """
        Test default attributes of the Review instance.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_place_id(self):
        """
        Test setting and getting the place_id attribute of the Review instance.
        """
        review = Review()
        review.place_id = "123"
        self.assertEqual(review.place_id, "123")

    def test_review_user_id(self):
        """
        Test setting and getting the user_id attribute of the Review instance.
        """
        review = Review()
        review.user_id = "456"
        self.assertEqual(review.user_id, "456")

    def test_review_text(self):
        """
        Test setting and getting the text attribute of the Review instance.
        """
        review = Review()
        review.text = "Great experience, highly recommend!"
        self.assertEqual(review.text, "Great experience, highly recommend!")


if __name__ == '__main__':
    unittest.main()
