import sys
import time
from heapq import heappush, heappop

global lookuptable
global spaces
global count
spaces = [{1,4}, {0,2,5}, {1,3,6}, {2,7}, {0,5,8}, {1,4,6,9}, {2,5,7,10}, {3,6,11}, {4,9,12}, {5,8,10,13}, {6,9,11,14}, {7,10,15}, {8,13}, {9,12,14}, {10,13,15}, {11,14}]

def print_out(p):
    print(p[0:4]+"\n"+p[4:8]+"\n"+p[8:12]+"\n" + p[12:16] + "\n")

def findChildren(p):
    l = []
    loc = p.index(' ')
    for i in spaces[loc]:
        li = list(p)
        li[loc], li[i] = li[i], li[loc]
        l.append("".join(li))
    return l

def isSolvable(puz):
    row_difference = (3 - puz.index(' ') // 4) & 1
    puz = puz.replace(" ","")
    inversion_count = (sum([1 for i in range(len(puz)-1) for j in range(i+1,len(puz)) if int(puz[i],16) > int(puz[j],16)]))&1
    return row_difference == inversion_count

def printPuzzle(p, d):
    l = []
    child = p
    while not child == "":
        l.append(child)
        child = d[child]
    for x in l[::-1]:
         print_out(x)
    print("Number of Steps: "+str(len(l)-1))
    print("Size of closed set: {}".format(len(d)))

def calcDistance(p):
    d = 0;
    for c in p:
        loc = p.find(c)
        d += abs(lookuptable[c]//4 - loc//4) +  abs(lookuptable[c]%4 - loc%4)
    return d

def solvePuz(root, goal):
    dctAlreadySeen = {root:""}
    dctParents = {root:""}
    #tuple(manhattan distance, puzzle, distance)
    parseMe = list()
    openDict = {}
    h = calcDistance(root)
    heappush(parseMe,(h, root, 0))
    openDict[root] = h
    global improved
    improved = 0;
    done = False
    if root == goal:
        printPuzzle(root, dctAlreadySeen)
    else:
        if isSolvable(root):
            while len(parseMe)>0:
                if done == True:
                    break
                tup = heappop(parseMe)
                puz = tup[1]
                if puz in openDict.keys():
                    openDict.pop(puz)
                d = tup[2]+1
                for x in findChildren(puz):
                    if x == goal:
                        dctAlreadySeen[x] = puz
                        dctAlreadySeen[puz] = dctParents[puz]
                        printPuzzle(x, dctAlreadySeen)
                        print("Size of open set: {}".format(len(openDict)))
                        done = True
                        break
                    if x in dctAlreadySeen.keys():
                        continue
                    heuristic = calcDistance(x)+d
                    if x not in openDict:
                        heappush(parseMe, (heuristic, x, d))
                        openDict[x] = heuristic
                    elif heuristic < openDict[x]:
                        improved+=1
                        heappush(parseMe, (heuristic, x, d))
                        openDict[x] = heuristic
                    if x not in dctParents.keys():
                        dctParents[x] = puz
                dctAlreadySeen[puz] = dctParents[puz]
        else:
            print("No solution")

start = time.clock()
root = sys.argv[1].upper()
goal = ''.join(sorted(root.replace(' ', '')))+ ' '
lookuptable = {c: goal.index(c) for c in goal}
solvePuz(root, goal)
print(f"Number improved: {improved}")
print("Time elapsed: {}".format(time.clock()-start))
