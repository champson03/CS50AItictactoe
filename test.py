import tictactoe as ttt
X = "X"
O = "O"
EMPTY = None
board = [[X, EMPTY, EMPTY],
         [EMPTY, O, O],
         [X, EMPTY, EMPTY]]
result = ttt.minimax(board)
print(result)
