"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            if board[i][j] == O:
                o_count += 1

    if x_count > o_count:
        return O
    elif o_count == x_count:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    pl = player(board)
    result = copy.deepcopy(board)

    if not result[action[0]][action[1]] == EMPTY:
        raise Exception
    result[action[0]][action[1]] = pl
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    x_set = set()
    o_set = set()
    cell_num = 1
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_set.add(cell_num)
            if board[i][j] == O:
                o_set.add(cell_num)
            cell_num += 1

    if judgement(x_set):
        return X
    elif judgement(o_set):
        return O
    return None


def judgement(check_set):
    """
    Returns True if a player wins.
    """
    win_set = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7},
               {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]

    for t in win_set:
        if t <= check_set:
            return True
    return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not winner(board) == None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    tmp_action = None
    if player(board) == X:
        vv_max = -1
        for action in actions(board):
            v_tmp = min_value(result(board, action), vv_max)
            if vv_max < v_tmp:
                vv_max = v_tmp
                tmp_action = action
            if vv_max == 1:
                return tmp_action
    else:
        vv_min = 1
        for action in actions(board):
            v_tmp = max_value(result(board, action), vv_min)
            if vv_min > v_tmp:
                vv_min = v_tmp
                tmp_action = action
            if vv_min == -1:
                return tmp_action
    return tmp_action


def max_value(board, alpha):
    if terminal(board):
        return utility(board)
    v_max = -1
    for action in actions(board):
        v_tmp = min_value(result(board, action), v_max)
        if v_max < v_tmp:
            v_max = v_tmp
        if v_max >= alpha:
            return v_max
    return v_max


def min_value(board, alpha):
    if terminal(board):
        return utility(board)
    v_min = 1
    for action in actions(board):
        v_tmp = max_value(result(board, action), v_min)
        if v_min > v_tmp:
            v_min = v_tmp
        if v_min <= alpha:
            return v_min
    return v_min
