'''TicTacToe game tests'''

import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase, TicTacToe):
    '''Unittesting game class'''
    def test_change_cell(self):
        """Trying to break changing precautions"""
        self.assertFalse(self.change_cell(0, 0, 'X'))
        self.assertFalse(self.change_cell(-1, -2, 'X'))
        self.assertFalse(self.change_cell(110, 10, 'X'))
        self.assertFalse(self.change_cell(0, 0, '0'))
        self.assertFalse(self.change_cell(0, 5, 'O'))
        self.assertFalse(self.change_cell(5, 0, 'O'))
        self.assertFalse(self.change_cell(0, 5, 6))
        self.assertFalse(self.change_cell(0, 5, 'das'))

        instance = TicTacToe()
        instance.change_cell(1, 1, 'X')
        self.assertFalse(self.change_cell(1, 1, 'X'))

    def test_winner_check(self):
        """Testing win check by implementing possible case"""
        instance = TicTacToe()
        instance.change_cell(1, 1, 'X')
        instance.change_cell(1, 2, 'X')
        instance.change_cell(1, 3, 'X')
        self.assertTrue(self.check_if_there_is_a_winner())

if __name__ == '__main__':
    unittest.main()
