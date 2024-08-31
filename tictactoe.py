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
    count_x = 0
    count_o = 0
    for row in board:
        for item in row:
            if item == X:
                count_x += 1
            if item == O:
                count_o += 1

    if count_x > count_o:
        return O
    else:
        return X

    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                # agregar direccion del elemento a la lista
                actions.add((row, col)) 
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] == EMPTY:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(new_board)
        return new_board
    else:  
        raise NameError('Invalid action space not empty')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # for lines
    for i in range(len(board)):
        if all(board[i][j] == board[i][0] and board[i][j] != EMPTY for j in range(len(board))):
            return board[i][0]

    # for columns
    for j in range(len(board)):
        if all(board[i][j] == board[0][j] and board[i][j] != EMPTY for i in range(len(board))):
            return board[0][j]

    # x lines
    if all(board[i][i] == board[0][0] and board[i][i] != '-' for i in range(len(board))):
        return board[0][0]
    if all(board[i][len(board)-i-1] == board[0][len(board)-1] and board[i][len(board)-i-1] != '-' for i in range(len(board))):
        return board[0][len(board)-1]

    # no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    there_empty = False
    for row in board:
        for cell in row:
            if cell == EMPTY: 
                there_empty = True
                break

    if winner(board) or not there_empty:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X:
        for action in actions(board):
            if max_value(board) == min_value(result(board, action)):
                return action
    
    if player(board) == O:
        for action in actions(board):
            if min_value(board) == max_value(result(board, action)):
                return action


def max_value(state):
    v = -math.inf
    if terminal(state):
        return utility(state)
    for action in actions(state):
        v = max(v, min_value(result(state, action)))
    return v

def min_value(state):
    v = math.inf
    if terminal(state):
        return utility(state)
    for action in actions(state):
        v = min(v, max_value(result(state, action)))
    return v