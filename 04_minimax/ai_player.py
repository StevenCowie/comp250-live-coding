import random


def minimax(board):
    result = board.get_result(2)
    if result is not None:
        return result
    else:
        if board.current_player == 1:
            best_value = 1000
        else:
            best_value = -1000

        for move in board.get_moves():
            board.do_move(move)
            value = minimax(board)
            board.undo_move(move)
            if board.current_player == 1:
                best_value = min(value, best_value)
                if best_value == -1:
                    return best_value
            else:
                best_value = max(value, best_value)
                if best_value == 1:
                    return best_value

        return best_value


def choose_move(board):
    """ Takes a game board, and returns a move to play as a tuple (x,y)
    """

    best_move = None
    best_value = -1000

    for move in board.get_moves():
        board.do_move(move)
        value = minimax(board)
        board.undo_move(move)
        print move, value
        if value > best_value:
            best_move = move
            best_value = value

    print
    return best_move
