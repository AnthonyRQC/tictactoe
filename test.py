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

# agregando un movimiento
board_o_turn2 = t.result(board_o_turn, (0, 2))
print(f"before put{board_o_turn}")
print(f"after put{board_o_turn2}")

# si el movimiento no es valido
# board_o_turn_bad = t.result(board_o_turn, (0, 0))
# print(f"before put{board_o_turn_bad}")

o_winner = [['X', 'X', 'O'], 
            [None, 'O', 'X'], 
            ['O', None, None]]

x_winner = [['X', 'X', 'X'], 
            [None, 'O', None], 
            [None, 'O', None]]
draw = [['X', 'O', 'X'], 
        ['X', 'O', 'X'], 
        ['O', 'X', 'O']]

print(f"winner o: {t.winner(o_winner)}")
print(f"winner x: {t.winner(x_winner)}")
print(f"draw: {t.winner(draw)}")

#### test terminal

print(f"should true {t.terminal(draw)}")
print(f"should true {t.terminal(o_winner)}")
print(f"should false {t.terminal(board_o_turn2)}")




