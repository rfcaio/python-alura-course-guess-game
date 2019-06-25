from unittest import TestCase

from guess import equals, is_greater_than

class TestGuess(TestCase):
    def test_equals(self):
        self.assertEqual(equals(4, 7), False)
        self.assertEqual(equals(7, 7), True)


    def test_is_greater_than(self):
        self.assertEqual(is_greater_than(4, 7), False)
        self.assertEqual(is_greater_than(11, 7), True)
