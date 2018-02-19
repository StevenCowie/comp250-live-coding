import random


def minimax(board, depth):
    result = board.get_result(2)
    if result is not None:
        return result
    elif depth == 0:
        return 0
    elif board.current_player == 2:
        best_value = -1000
        for move in board.get_moves():
            board.do_move(move)
            v = minimax(board, depth-1)
            board.undo_move(move)
            best_value = max(best_value, v)
        return best_value
    elif board.current_player == 1:
        best_value = 1000
        for move in board.get_moves():
            board.do_move(move)
            v = minimax(board, depth - 1)
            board.undo_move(move)
            best_value = min(best_value, v)
        return best_value


def choose_move(board):
    """ Takes a game board, and returns a move to play
    """

    best_value = -1000
    best_move = None

    for move in board.get_moves():
        board.do_move(move)
        v = minimax(board, 6)
        print move, v
        board.undo_move(move)
        if v > best_value:
            best_value = v
            best_move = move

    return best_move

    return random.choice(board.get_moves())
