''' Includes tic-tac-toe game class '''

FIGURE = {
    'Space' : ' ',
    'Cross' : 'X',
    'Circle' : 'O'
}

DEFAULT_FIELD_OUTLOOK = '''
{a[0]}|{a[1]}|{a[2]}
- - -
{a[3]}|{a[4]}|{a[5]}
- - -
{a[6]}|{a[7]}|{a[8]}\n'''

class TicTacToe():
    '''A functional tic-tac-toe game class. Game can be started by calling a play(...) method'''
    field = [FIGURE['Space']] * 9
    def __init__(self):
        '''Creating an empty field'''
        self.field = [FIGURE['Space']] * 9
    def print_field(self):
        '''ASCII printing classical 3x3 tic-tac-toe field'''
        result = DEFAULT_FIELD_OUTLOOK.format(a=self.field)
        print(result)

    def change_cell(self, row, col, val):
        '''Validating input(row column value) and modifying field'''
        if val in ('X', 'O') and 0 < row < 4 and 0 < col < 4:
            if self.field[(row - 1) * 3 + (col - 1)] == ' ':
                self.field[(row - 1) * 3 + (col - 1)] = val
                return True
            return False
        return False

    def check_if_there_is_a_winner(self):
        '''Searching for a sequence of equal cells in up-down, left-right and cross cases'''
        if (self.field[0] == self.field[1] == self.field[2] != ' ' or
                self.field[3] == self.field[4] == self.field[5] != ' ' or
                self.field[6] == self.field[7] == self.field[8] != ' '):
            return True
        if (self.field[0] == self.field[3] == self.field[6] != ' ' or
                self.field[1] == self.field[4] == self.field[7] != ' ' or
                self.field[2] == self.field[5] == self.field[8] != ' '):
            return True
        if (self.field[0] == self.field[4] == self.field[8] != ' ' or
                self.field[2] == self.field[4] == self.field[6] != ' '):
            return True
        return False

    def play(self, player1, player2):
        '''Launching a game loop, waiting for a winner to win)'''
        print("{}: X ".format(player1))
        print("{}: O ".format(player2))
        print("To place a figure - type row and column number separated by space")

        cur_player = 0

        while not self.check_if_there_is_a_winner():
            cur_player = 0 if bool(cur_player) else 1
            print("{}`s turn".format(player1 if bool(cur_player) else player2))
            self.print_field()
            tmp_inp = [int(s) for s in input().split(' ')]

            while not self.change_cell(tmp_inp[0], tmp_inp[1], 'X' if cur_player == 1 else 'O'):
                print("Invalid input, try again")
                tmp_inp = [int(s) for s in input().split(' ')]

        print("Congratulations to {}! You won!".format(player1 if bool(cur_player) else player2))
