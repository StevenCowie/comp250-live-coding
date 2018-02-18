import random


def choose_move(board):
    """ Takes a game board, and returns a move to play
    """

    return random.choice(board.get_moves())
