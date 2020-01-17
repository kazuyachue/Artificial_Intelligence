import sys, time
start = time.clock()
board = sys.argv[1]
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

print(partitionMoves(board))
display(board)
print("Seconds:", time.clock() - start)

'''
1. show a tic tac toe board in 2-d
2. Given a board, whos move is it? assuming that X goes first
3. Set of free poistions on the board
all one line each
input it is going to get a game, 9 characters,
	what move can be made that can lead to a forced win, forced loss, tie moves

def partitionMoves(game):
	returns a tuple of three sets:
	good:set of moves which lead to a forced win
	bad: set of moves which can lead to a win for the opponent
	tie: the set of moves that can lead to a tie under optimal play
	recursive condition
	what sit he terminating condition?
		if the game is already over, then return appropriately win:('', {}, {}), loss:({}, {''}, {}), tie ({}, {}, {''})
		good, bad, tie = set(), set(), set()
		for each possible move:
			newGame = update new game w possible move
			tmpGood, tmpBad, tmpTie = partitionMoves(newGame) -> analyze for the enemy
			if tempGood: bad.add(possibleMove)
			else if tmpTie: tie.add(pozzibleMove)
			else: good.add(possibleMove)
		return good, bad, tie
'''
