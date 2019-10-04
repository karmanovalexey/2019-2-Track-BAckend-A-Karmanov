''' Includes tic-tac-toe game class '''

FIGURE = {
    'Space' : ' ',
    'Cross' : 'X',
    'Circle' : 'O'
}

class Field():
    '''A functional tic-tac-toe game class. Game can be started by calling for a play(...) method'''
    current_state = [FIGURE['Space']] * 9
    first_player = True
    def print_field(self):
        '''ASCII printing classical 3x3 tic-tac-toe field'''
        result = "{a[0]}|{a[1]}|{a[2]}\n- - -\n{a[3]}|{a[4]}|{a[5]}\n- - -\n{a[6]}|{a[7]}|{a[8]}".format(a = self.current_state)
        print(result)
#        result = '''    {a[0]}|{a[1]}|{a[2]} \n 
#                        - - -\n 
#                    {a[3]}|{a[4]}|{a[5]}\n
#                         - - -\n 
#                    {a[6]}|{a[7]}|{a[8]}\n'''.format(a=self.current_state)
#        print(result[1:11], result[36:42], result[63:70], result[95:103], result[124:130])

    def change_cell(self, row, col, val):
        '''Validating input(row column value) and modifying field'''
        if val in ('X', 'O') and 0 < row < 4 and 0 < col < 4 :
            if self.current_state[(row - 1) * 3 + (col - 1)] == ' ':
                self.current_state[(row - 1) * 3 + (col - 1)] = val
                return "Cell filled successfully"
            return "Cell is already filled"
        return "Invalid input"

    def check_if_there_is_a_winner(self):
        '''Searching for a sequence of equal cells in up-down case, left-right case and cross case'''
        if (self.current_state[0] == self.current_state[1] == self.current_state[2] != ' ' or
            self.current_state[3] == self.current_state[4] == self.current_state[5] != ' ' or
            self.current_state[6] == self.current_state[7] == self.current_state[8] != ' '):
            return True 
        if (self.current_state[0] == self.current_state[3] == self.current_state[6] != ' ' or
            self.current_state[1] == self.current_state[4] == self.current_state[7] != ' ' or
            self.current_state[2] == self.current_state[5] == self.current_state[8] != ' '):
            return True
        if (self.current_state[0] == self.current_state[4] == self.current_state[8] != ' ' or
            self.current_state[2] == self.current_state[4] == self.current_state[6] != ' '):
            return True
        return False
