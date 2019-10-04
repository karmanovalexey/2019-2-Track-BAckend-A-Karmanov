import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase, TicTacToe):
    def test_change_cell(self):
        self.assertFalse(self.change_cell(0, 0, 'X'))
        self.assertFalse(self.change_cell(-1, -2, 'X'))
        self.assertFalse(self.change_cell(110, 10, 'X'))
        self.assertFalse(self.change_cell('f', [0, 10], 'X'))
        self.assertFalse(self.change_cell(0, 0, '0'))
        self.assertFalse(self.change_cell(0, 5, 'O'))
        self.assertFalse(self.change_cell(5, 0, 'O'))
        self.assertFalse(self.change_cell(0, 5, 6))
        self.assertFalse(self.change_cell(0, 5, 'das'))
        self.assertFalse(self.change_cell(0, 5, [23, 56]))

        instance = TicTacToe()
        instance.change_cell(1, 1, 'X')
        self.assertFalse(self.change_cell(1, 1, 'X'))

    def test_winner_check(self):
        instance = TicTacToe()
        instance.change_cell(1, 1, 'X')
        instance.change_cell(1, 2, 'X')
        instance.change_cell(1, 3, 'X')
        self.assertTrue(self.check_if_there_is_a_winner())

        instance = TicTacToe()
        instance.change_cell(1, 1, 'X')
        instance.change_cell(2, 2, 'X')
        instance.change_cell(3, 3, 'X')
        self.assertTrue(self.check_if_there_is_a_winner())

        instance = TicTacToe()
        instance.change_cell(1, 1, 'X')
        instance.change_cell(2, 1, 'X')
        instance.change_cell(3, 1, 'X')
        self.assertTrue(self.check_if_there_is_a_winner())

        instance = TicTacToe()
        instance.change_cell(1, 1, 'O')
        instance.change_cell(2, 2, 'X')
        instance.change_cell(3, 3, 'X')
        self.assertFalse(self.check_if_there_is_a_winner())


        




if __name__ == '__main__':
    unittest.main()
