from unittest import TestCase

from hangman import has_hanged, has_won, sanitize


class TestHangman(TestCase):
    def test_has_hanged_should_return_false_when_the_amount_of_erros_is_lower_than_five(self):
        for error in range(0, 5):
            self.assertEqual(has_hanged(error), False)


    def test_has_hanged_should_return_true_when_the_amount_of_erros_is_greater_than_or_equals_five(self):
        self.assertEqual(has_hanged(5), True)
        self.assertEqual(has_hanged(6), True)


    def test_has_won_should_return_false_when_underscore_is_present_in_the_score(self):
        self.assertEqual(has_won(['j', '_', 'x']), False)


    def test_has_won_should_return_true_when_underscore_is_not_present_in_the_score(self):
        self.assertEqual(has_won(['j', 'a', 'x']), True)


    def test_sanitize_should_return_a_string_in_lower_case_with_no_blank_spaces(self):
        self.assertEqual(sanitize(' Foo '), 'foo')
        self.assertEqual(sanitize('  Foo'), 'foo')
        self.assertEqual(sanitize('Foo  '), 'foo')
