import sys
import time
import heapq

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

def calcDistance(p):
    d = 0;
    for c in p:
        loc = p.find(c)
        d += abs(lookuptable[c]//4 - loc//4) +  abs(lookuptable[c]%4 - loc%4)
    return d

def solvePuz(root, goal):
    dctAlreadySeen = {root:""}
    #tuple(manhattan distance, puzzle, distance)
    parseMe = [(calcDistance(root), root, 0)]
    heapq.heapify(parseMe)
    global count
    count = 0;
    if isSolvable(root):
        while True:
            tup = heapq.heappop(parseMe)
            count+=1;
            puz = tup[1]
            if puz == goal:
                printPuzzle(puz, dctAlreadySeen)
                break;
            children = findChildren(puz)
            d = tup[2]+1
            for x in children:
                if x not in dctAlreadySeen.keys():
                    dctAlreadySeen[x] = puz
                    heapq.heappush(parseMe, (calcDistance(x)+d, x, d))
    else:
        print("No solution")

start = time.clock()
root = sys.argv[1].upper()
goal = ''.join(sorted(root.replace(' ', '')))+ ' '
lookuptable = {c: goal.index(c) for c in goal}
solvePuz(root, goal)
print(f"Number removed: {count}")
print("Time elapsed: {}".format(time.clock()-start))
