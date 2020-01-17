import sys, time, random

def makeLookup(board):
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
    return lookupTable

def printBoard(board):
    print('\n'.join([board[i*8:i*8+8] for i in range(8)]))

def placeToken(b, t, p):
    if p == -1:
        return b
    lookupTable = makeLookup(b)
    you, opponent = ('X', 'O') if t == 'X' else ('O', 'X')
    b_list = list(b)
    for neighbors in lookupTable[p]:
        if b[neighbors] == opponent:
            if isSandwich(b, you, neighbors, p, lookupTable):
                diff = neighbors - p
                location = p
                while 1:
                    location = location + diff
                    if b[location] == you:
                        break;
                    b_list[location] = you
    b_list[p] = you
    b = ''.join(b_list)
    return b

def possibleMoves(board, to_move):
    you, opponent = ('X', 'O') if to_move ==  'X' else ('O', 'X')
    lookupTable = makeLookup(board)
    possible = set()
    for i in range(len(board)):
        if board[i] == opponent:
            for neighbors in lookupTable[i]:
                if board[neighbors] == '.':
                    if isSandwich(board, you, i, neighbors, lookupTable):
                        possible.add(neighbors)
    return possible

def isSandwich(board, you, i, n, lookupTable):
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

def negamax(board, token, levels):
    enemy = 'O' if token == 'X' else 'X'
    if not levels: return [evalBoard(list(board), token)]
    lm = possibleMoves(board, token)
    if not lm:
        nm = negamax(board, enemy, levels - 1) + [-1]
        return [-nm[0]]+nm[1:]
    nmList = sorted([negamax(placeToken(board, token, mv), enemy, levels-1) + [mv] for mv in lm])
    best = nmList[0]
    return [-best[0]] + best[1:]

def negamaxTerminal(board, token, alpha, beta):
    enemy = 'O' if token == 'X' else 'X'
    lm = possibleMoves(board, token)
    if not lm:
        lm = possibleMoves(board, enemy)
        if not lm: return [evalBoard(list(board),token), -3]
        nm = negamaxTerminal(board, enemy, -beta, -alpha) + [-1]
        return [-nm[0]] + nm[1:]
    best = []
    newBeta = -alpha
    for move in lm:
        nm = negamaxTerminal(placeToken(board, token, move), enemy, -beta, newBeta) + [move]
        if not best or nm[0] < newBeta:
            best = nm
            if nm[0] < newBeta:
                newBeta = nm[0]
                if -newBeta >= beta:
                    return [-best[0]] + best[1:]
    return [-best[0]] + best[1:]

def evalBoard(board_list, token):
    board = ''.join(board_list)
    lookupTable = makeLookup(board)
    weighting_matrix = [
    240, -20,  20,   5,   5,  20, -20, 240,
    -20, -40,  -5,  -5,  -5,  -5, -40, -20,
    20,  -5,  15,   3,   3,  15,  -5,  20,
    5,  -5,   3,   3,   3,   3,  -5,   5,
    5,  -5,   3,   3,   3,   3,  -5,   5,
    20,  -5,  15,   3,   3,  15,  -5,  20,
    -20, -40,  -5,  -5,  -5,  -5, -40, -20,
    240, -20,  20,   5,   5,  20, -20, 240
    ]
    for i in [0, 7, 56, 63]:
        if board[i] == token:
            for neighbor in lookupTable[i]:
                weighting_matrix[neighbor] *= -1
    #enemy = 'O' if token == 'X' else 'X'
    matrix = [1 if i == 'X' else -1 if i == 'O' else 0 for i in board_list]
    return sum(weighting_matrix[n] * matrix[n] for n in range(len(weighting_matrix))) + random.randint(0, 20)

def findBestMove(board, token, depth):
    ls = negamax(board, token, depth)
    return ls[-1]

def findBestMove2(board, token):
    ls = negamaxTerminal(board, token, -65, 65)
    return ls[-1]

class Strategy():
    def best_strategy(self, board, player, best_move, still_running):
        brd = ''.join(board).replace('?', '').replace('@', 'X').upper()
        token = 'X' if player == '@' else 'O'
        if brd.count('.') < 14:
            mv = findBestMove(brd, token, 1)
            mv1 = 11 + (mv//8) * 10 + (mv%8)
            best_move.value = mv1
            mv = findBestMove2(brd, token)
            mv1 = 11 + (mv//8) * 10 + (mv%8)
            best_move.value = mv1
        else:
            depth = 1
            while True:
                mv = findBestMove(brd, token, depth)
                mv1 = 11 + (mv//8) * 10 + (mv%8)
                best_move.value = mv1
                depth += 2
