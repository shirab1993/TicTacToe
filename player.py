import random
import math

MAX = math.inf
MIN = -math.inf


class Player:
    def __init__(self, name, marker, opponent_marker):
        self.name = name
        self.marker = marker
        self.opponent_marker = opponent_marker

    def make_move(self, board):
        move = (int(input(f'This is the current board, {self.name} please make a move 0-8.\n')))
        while True:
            try:
                if board.is_legal_place(move):
                    board.place_mark(self.marker, move)
                    return move
                else:
                    move = int(input(f'Illegal move, please try again\n'))
            except IndexError:
                move = int(input(f'Illegal move, please try again\n'))


class Computer(Player):
    def make_move(self, board):
        if board.is_empty():
            first_comp_move = random.randint(0,8)
            return first_comp_move

        else:

            best_score = -math.inf
            best_move = math.inf
            for i in range(9):
                if board.is_legal_place(i):
                    board.place_mark(self.marker, i)
                    score = self.minimax(board, 0, False,MIN,MAX)
                    board.board[i] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = i
            return best_move

    def minimax(self, board, depth, is_maximizing,alpha, beta):

        if board.is_winner(self.marker):
            return 1
        elif board.is_winner(self.opponent_marker):
            return -1
        elif board.is_draw():
            return 0

        if is_maximizing:

            best_score = -math.inf
            for i in range(9):
                if board.is_legal_place(i):
                    board.place_mark(self.marker, i)
                    score = self.minimax(board, depth + 1, False,alpha,beta)
                    board.board[i] = ' '
                    best_score = max(score,best_score)
                    alpha = max(alpha,best_score)
                #alpha beta pruning
                if beta <= alpha:
                    break

            return best_score

        else:

            best_score = math.inf
            for i in range(9):
                if board.is_legal_place(i):
                    board.place_mark(self.opponent_marker, i)
                    score = self.minimax(board, depth + 1, True,alpha,beta)
                    board.board[i] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta,best_score)
                if beta <= alpha:
                    break

            return best_score

