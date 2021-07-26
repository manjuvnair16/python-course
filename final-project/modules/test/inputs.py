import unittest
from unittest import mock
from unittest import TestCase
import adventure_game
import modules.functions.graphics as display_functions

class TestGame(TestCase):
    @mock.patch('display_functions.display_start_menu.input', create=True)
    def test_main_input_validations(self, mocked_input):
        mocked_input.side_effect = ['M']
        result = adventure_game.main()
        self.assertRaises("Please enter from the following only: y or n" )

    def test_exit(self):
        result = adventure_game.exit_game()
        self.assertTrue(result)

    

if __name__ == "__main__":
       unittest.main()