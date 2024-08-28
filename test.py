import tictactoe as t
import copy

new_board = t.initial_state()
print(f'state: {new_board}')
board_x_turn = copy.deepcopy(new_board)
board_x_turn[0][0] = t.X
board_x_turn[1][1] = t.O

print(board_x_turn)
print(t.player(board_x_turn))

board_o_turn = copy.deepcopy(board_x_turn)
board_o_turn[0][1] = t.X

print(board_o_turn)
print(t.player(board_o_turn))


print(f'actions for X{t.actions(board_x_turn)}')
print(f'actions for O{t.actions(board_o_turn)}')