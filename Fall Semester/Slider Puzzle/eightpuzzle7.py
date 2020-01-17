import sys
import collections
import time
import random

global lookupTable
lookupTable = [{1,3}, {0, 2, 4}, {1,5}, {0, 4, 6}, {1, 3, 5, 7}, {2,4,8}, {3,7}, {6,4,8}, {5,7}]

def print_out(p):
    print(p[0:3]+"\n"+p[3:6]+"\n"+p[6:9]+"\n")

def findChildren(p):
    l = []
    loc = p.find(' ')
    if loc>-1 and loc<9:
        for i in lookupTable[loc]:
            li = list(p)
            li[loc], li[i] = li[i], li[loc]
            l.append("".join(li))
    return l

def printPuzzle(p, d):
    l = []
    child = p
    while not child == "":
        l.append(child)
        child = d[child]
    for x in l[::-1]:
         print_out(x)
    print("Number of Steps: "+str(len(l)-1))

def num_Steps(p, d):
    child = p
    steps=0
    while not child == "":
        child = d[child]
        steps+=1
    return steps-1

def solvePuz(root):
    #root = sys.argv[1]
    #goal = ''.join(sorted(root.replace(' ', '')))+ ' '
    goal = "12345678 "
    dctAlreadySeen = {root:""}
    parseMe = collections.deque([root])
    while True:
        if len(parseMe) == 0:
            return 0
        puz = parseMe.popleft()
        if puz == goal:
            return num_Steps(puz, dctAlreadySeen)
        children = findChildren(puz)
        for x in children:
            if x not in dctAlreadySeen.keys():
                dctAlreadySeen[x] = puz
                parseMe.append(x)

t = time.clock()
solvePuz("12345687 ")
print(str(time.clock()-t))

fin = "12345678 "
numPuzzles = 0
total_time = 0
solved_puzzles = 0
solved_puzzle_steps = 0
for i in range(0,1000):
    l = list(fin)
    random.shuffle(l)
    s = ''.join(l)
    print(s)
    numPuzzles+=1
    start = time.clock()
    x = solvePuz(s)
    if x!=0:
        solved_puzzles+=1
        solved_puzzle_steps+=x
    total_time+= (time.clock()-start)

print(str(numPuzzles))
print("Average time: "+ str(total_time/numPuzzles))
print("Total time: "+str(total_time))
if solved_puzzles !=0:
    print("Average steps: "+ str(solved_puzzle_steps/solved_puzzles))

#0.717 seconds
#12.11 min
#21.99 depth
