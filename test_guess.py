from unittest import TestCase

from guess import equals, get_quantity_of_turns, is_greater_than, is_out_of_range, show_status, update_points


class TestGuess(TestCase):
    def test_equals_should_return_true_when_the_first_number_is_equal_to_second_number(self):
        self.assertEqual(equals(7, 7), True)


    def test_equals_should_return_false_when_the_first_number_is_not_equal_to_second_number(self):
        self.assertEqual(equals(4, 7), False)


    def test_get_quantity_of_turns_should_return_20_when_1_is_passed_as_parameter(self):
        self.assertEqual(get_quantity_of_turns(1), 20)


    def test_get_quantity_of_turns_should_return_10_when_2_is_passed_as_parameter(self):
        self.assertEqual(get_quantity_of_turns(2), 10)


    def test_get_quantity_of_turns_should_return_5_when_another_number_is_passed_as_parameter(self):
        self.assertEqual(get_quantity_of_turns(-1), 5)
        self.assertEqual(get_quantity_of_turns(0), 5)
        self.assertEqual(get_quantity_of_turns(3), 5)


    def test_is_greater_than_should_return_true_when_the_first_number_is_greater_than_the_second_number(self):
        self.assertEqual(is_greater_than(11, 7), True)


    def test_is_greater_than_should_return_false_when_the_first_number_is_not_greater_than_the_second_number(self):
        self.assertEqual(is_greater_than(4, 7), False)


    def test_is_out_of_range_should_return_false_when_the_number_is_in_the_range(self):
        self.assertEqual(is_out_of_range(3, 1, 10), False)


    def test_is_out_of_range_should_return_true_when_the_number_is_not_in_the_range(self):
        self.assertEqual(is_out_of_range(-1, 1, 10), True)


    def test_is_out_of_range_should_use_1_and_100_as_default_for_start_and_end_respectively(self):
        self.assertEqual(is_out_of_range(0), True)
        self.assertEqual(is_out_of_range(101), True)


    def test_show_status_should_return_a_string_with_the_current_game_round(self):
        self.assertEqual(show_status(3, 7), 'TURN 3 OF 7')


    def test_update_points_should_return_the_amount_of_points_minus_the_difference_between_secret_number_and_guess_number(self):
        self.assertEqual(update_points(100, 75, 50), 75)
        self.assertEqual(update_points(100, 25, 50), 75)
