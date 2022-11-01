from board import Board
from player import Player
from player import Computer
import random


class Game:
    def __init__(self):
        self.players = []
        self.turn = 0
        self.board = Board()
        self.computer_score = 0
        self.player_score = 0

    def set_players(self, p1, p2):
        self.players = [p1, p2]

    def set_turn(self, turn):
        self.turn = turn

    def flip_coin(self):
        result = random.randint(0, 1)
        print("in flip coin: ", result)
        if result == 0:

            print('computer play first')
        else:
            print('you win, play first')

        return result

    def two_players(self):
        p1 = (input('player x - please enter your name:\n'))
        p2 = (input('player y - please enter your name:\n'))
        self.set_players(Player(p1, 'x', 'o'), Player(p2, 'o', 'x'))
        self.play()

    def player_vs_computer(self):
        play_again = True
        p1 = input('player x - please enter your name:\n')
        while play_again:
            res = self.flip_coin()
            self.set_turn(res)
            self.set_players(Computer('computer', 'o', 'x'), Player(p1, 'x', 'o'))
            self.play()
            again = str(input('Do you want to play again? type yes or no\n'))
            if again == 'no':
                play_again = False
                exit()
            self.board.__init__()

    def update_print_score_table(self):
        '''
        The winner is The winner is the one whose last turn is his Therefore if there is no tie we will update the winner
        :return:print table score
        '''

        winner = self.players[int(self.turn)]
        if self.board.is_draw():
            self.computer_score += 1
            self.player_score += 1
        elif winner == 0:
            self.player_score += 2
        else:
            self.player_score += 2

        print(f'Table score--> computer score: {self.computer_score}| player score: {self.player_score}')

    def play(self):

        while True:
            current_player = self.players[int(self.turn)]
            self.board.print_board()
            move = current_player.make_move(self.board)
            self.board.place_mark(current_player.marker, move)
            is_winning = self.board.is_winner(current_player.marker)

            if self.board.is_draw():
                print(f"It's a draw")
                self.board.print_board()
                self.update_print_score_table()
                break

            elif is_winning:
                print(f'Congratulations {current_player.name} you win !!')
                self.board.print_board()
                self.update_print_score_table()
                break
            else:
                self.turn = not self.turn
