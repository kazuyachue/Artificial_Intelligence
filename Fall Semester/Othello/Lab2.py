import sys, time

A1 = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

if len(sys.argv) < 2:
    board = '.' * 27 + 'OX' + '.' * 6 + 'XO' + '.' * 27
    token = 'X'
    position = '-1'
elif len(sys.argv) < 3:
    if sys.argv[1].is
    board = '.' * 27 + 'OX' + '.' * 6 + 'XO' + '.' * 27
    token = 'X'
    position = sys.argv[1]
elif len(sys.argv) < 4:
    if len(sys.argv[1]) == 64:
        board = sys.argv[1].upper()
        token = 'X'
    else:
        board = '.' * 27 + 'OX' + '.' * 6 + 'XO' + '.' * 27
        token = sys.argv[1].upper()
    position = sys.argv[2]
else:
    board = sys.argv[1].upper()
    token = sys.argv[2].upper()
    position = sys.argv[3]
if position[0].isalpha():
    position = (int(position[1]) - 1) * 8 + A1[position[0]]
position = int(position)

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

def placeToken(b, t, p):
    if position == -1:
        return b
    you, opponent = ('X', 'O') if t == 'X' else ('O', 'X')
    for neighbors in lookupTable[p]:
        if b[neighbors] == opponent:
            if isSandwich(b, you, p, neighbors):
                b_list = list(b)
                b_list[p] = you
                diff = neighbors - p
                while 1:
                    p = p + diff
                    if b[p] == you:
                        break;
                    b_list[p] = you
                b = ''.join(b_list)
    return b

def isSandwich(board, you, i, n):
    diff = n - i
    while 1:
        i = i + diff
        if i//8 in (0, 7) or i%8 in (0,7):
            return False
        elif board[i] == '.':
            return False
        elif board[i] == you:
            return True

board = placeToken(board, token, position)
printBoard(board)
print(board)
print(str(board.count('X')) + ':' + str(board.count('O')))
