import sys, time

if len(sys.argv) < 2:
    board = '.' * 27 + 'OX' + '.' * 6 + 'XO' + '.' * 27
    to_move = 'X'
elif len(sys.argv) < 3:
    board = sys.argv[1].upper()
    to_move = 'X' if (len(board) - board.count('.')) % 2 == 0 else 'O'
else:
    board = sys.argv[1].upper()
    to_move = sys.argv[2].upper()

lookupTable = {}

for i in range(len(board)):
    s = set()
    if i%8 != 0:
        s.add(i-1) #left
        if i//8 != 0:
            s.add(i-9)#upper left
        if i//8 != 7:
            s.add(i+7)#lower left
    if i%8 != 7:
        s.add(i+1) #right
        if i//8 != 0:
            s.add(i-7)#upper right
        if i//8 != 7:
            s.add(i+9) #lower right
    if i//8 != 0:
        s.add(i-8) #up
    if i//8 != 7:
        s.add(i+8) #down
    lookupTable[i] = s

def printBoard(board):
    print('\n'.join([board[i*8:i*8+8] for i in range(8)]))

def possibleMoves(board, to_move):
    you, opponent = ('X', 'O') if to_move ==  'X' else ('O', 'X')
    possible = set()
    for i in range(len(board)):
        if board[i] == opponent:
            for neighbors in lookupTable[i]:
                if board[neighbors] == '.':
                    if isSandwich(board, you, i, neighbors):
                        possible.add(neighbors)
    return possible

def isSandwich(board, you, i, n):
    diff = i - n
    while 1:
        prev = i
        i = i + diff
        if i >= len(board):
            return False
        elif i not in lookupTable[prev]:
            return False
        elif board[i] == '.':
            return False
        elif board[i] == you:
            return True

moves_set = possibleMoves(board, to_move)
board_list = list(board)
for i in moves_set:
    board_list[i] = '*'
board = ''.join(board_list)
printBoard(board)
print(moves_set)
