import sys, time, random
from msvcrt import getch
start = time.clock()

if len(sys.argv) < 2:
    board = '.' * 9
    token = 'O'
elif len(sys.argv) < 3:
    if len(sys.argv[1])==1:
        board = '.' * 9
        token = sys.argv[1].upper()
    else:
     board = sys.argv[1]
     token = 'O'
else:
    board = sys.argv[1]
    token = sys.argv[2].upper()

lookupTable = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def display(board):
    print('\n'.join([board[i*3:i*3+3] for i in range(3)]))

def whosMove(board):
    return board.count('X') == board.count('O')

def openPos(board):
    return {i for i in range(9) if board[i] == '.'}

def partitionMoves(board):
    p1, p2 = ('X', 'O') if whosMove(board) else ('O', 'X')
    #base case
    for x in lookupTable:
        s = ''.join([board[i] for i in x])
        if s == p1*3:
            return ({''}, {}, {})
        elif s == p2*3:
            return ({}, {''}, {})
        elif board.count('.') == 0:
            return ({}, {}, {''})
    good, bad, tie = set(), set(), set()
    for move in openPos(board):
        newGame = board[:move] + p1 + board[move+1:]
        tmpGood, tmpBad, tmpTie = partitionMoves(newGame)
        if tmpGood: bad.add(move)
        elif tmpTie: tie.add(move)
        else: good.add(move)
    return good, bad, tie

def makeMove(board, token):
    move = 'X' if whosMove(board) else 'O'
    if move == token:
        return board
    good, bad, tie = partitionMoves(board)
    print(good, bad, tie)
    if good:
        print("Winning move")
        pos = good.pop()
    elif tie:
        print("Tieing move")
        pos = tie.pop()
    else:
        print("Losing move")
        pos = bad.pop()
    board = board[:pos] + move + board[pos+1:]
    display(board)
    print("-----------")
    return board

def checkOver(board):
    for x in lookupTable:
        s = ''.join([board[i] for i in x])
        if s == 'O'*3:
            print('O wins!')
            return True
        elif s == 'X'*3:
            print('X wins!')
            return True
    if board.count('.') == 0:
        print('Tie!')
        return True
def playGame(board, token):
    while 1:
        board = makeMove(board, token)
        if checkOver(board):
            break
        while 1:
            print("please make a move (0-8):", end = " ", flush = True)
            index = int(getch())
            if board[index] != '.':
                print("Error: you cant play there!")
            else:
                break
        print(index)
        move = 'X' if whosMove(board) else 'O'
        board = board[:index] + move + board[index+1:]
        display(board)
        print("-----------")
        if checkOver(board):
            break

playGame(board, token)
