from unittest import TestCase

from hangman import sanitize


class TestHangman(TestCase):
    def test_sanitize_should_return_a_string_in_lower_case_with_no_blank_spaces(self):
        self.assertEqual(sanitize(' Foo '), 'foo')
        self.assertEqual(sanitize('  Foo'), 'foo')
        self.assertEqual(sanitize('Foo  '), 'foo')
