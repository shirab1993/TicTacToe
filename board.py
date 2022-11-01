class Board:
    board = [' '] * 9

    def print_board(self):
        print(self.board[0] + '|' + self.board[1] + '|' + self.board[2])
        print('-+-+-')
        print(self.board[3] + '|' + self.board[4] + '|' + self.board[5])
        print('-+-+-')
        print(self.board[6] + '|' + self.board[7] + '|' + self.board[8])
        print("\n")

    def is_legal_place(self, place):
        if self.board[place] == ' ':
            return True
        else:
            return False

    def is_empty(self):
        if 'x' in self.board or 'o' in self.board:
            return False
        else:
            return True

    def place_mark(self, marker, place):
        if self.is_legal_place(place):
            self.board[place] = marker

    def is_winner(self, marker):
        winning_positions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        return any([sum([self.board[i] == marker for i in pos]) == 3 for pos in winning_positions])

    def is_draw(self):
        return ' ' not in self.board
