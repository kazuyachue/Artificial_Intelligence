import sys
import time
from heapq import heappush, heappop

global lookupTable
lookupTable = {0: {1: 3, 2: 5}, 1: {3: 6, 4: 8}, 2: {4: 7, 5: 9}, 3: {4: 5, 1: 0, 6: 10, 7: 12}, 4: {7: 11, 8: 13},
5: {2: 0, 4: 3, 8: 12, 9: 14}, 6: {3: 1, 7: 8}, 7: {4: 2, 8: 9}, 8: {4: 1, 7: 6, }, 9: {5: 2, 8: 7}, 10: {6: 3, 11: 12},
11: {7: 4, 12: 13}, 12: {11: 10, 7: 3, 8: 5, 13: 14}, 13: {12: 11, 8: 4}, 14: {13: 12, 9: 5}}

#inverted up till 3
"""lookupTable = {0: {3: 1, 5: 2}, 1: {6: 3, 8: 4}, 2: {7: 4, 9: 5}, 3: {5: 4, 0: 1, 10: 6, 12: 7}, 4: {7: 11, 8: 13},
5: {2: 0, 4: 3, 8: 12, 9: 14}, 6: {3: 1, 7: 8}, 7: {4: 2, 8: 9}, 8: {4: 1, 7: 6, }, 9: {5: 2, 8: 7}, 10: {6: 3, 11: 12},
11: {7: 4, 12: 13}, 12: {11: 10, 7: 3, 8: 5, 13: 14}, 13: {12: 11, 8: 4}, 14: {13: 12, 9: 5}}"""

def print_out(p):
    print(p[0] + "\n" + p[1:3] + "\n" + p[3:6] + "\n" + p[6:10] + "\n" + p[10:])
    print("\n")

def printPuzzle(p, d):
    l = []
    l2 = []
    child = d[p]
    while not child[0] == "":
        l.append(f"{child[1]} -> {child[2]}")
        l2.append(child[0])
        child = d[child[0]]
    for x in l[::-1]:
         print(x)
    print("\n")
    for x in l2[::-1]:
         print_out(x)
def isPzlAtGoal(pzl):
    if pzl.count('*') == 1:
        return True
    return False

def nbrFromPzl(pzl, start, jumpedOver, destination):
    l = list(pzl)
    l[jumpedOver] = '_'
    l[destination] = l[start]
    l[start] = '_'
    pzl = "".join(l)
    return pzl

def nbrsFromPzl(pzl):
    s = set()
    for i in range(len(pzl)):
        if pzl[i] == '*':
            dic = lookupTable[i]
            for jump in dic.keys():
                if pzl[jump] == '*' and pzl[dic[jump]] == '_':
                    s.add((nbrFromPzl(pzl, i, jump, dic[jump]), i, dic[jump]))
    return s

space_location = int(sys.argv[1])
root = "*" * space_location + '_' + "*" * (14 - space_location)
parseMe = list()

dctAlreadySeen = {root:("", 'asdf', 'asdf')}
heappush(parseMe, (14, root))
while True:
    if len(parseMe) == 0:
        print("No solution :(")
        break;
    tup = heappop(parseMe)
    num_pegs = tup[0]
    puz = tup[1]
    if num_pegs == 1:
        printPuzzle(puz, dctAlreadySeen)
        break;
    children = nbrsFromPzl(puz)
    if len(children) == 0:
        continue
    for tuples in children:
        x = tuples[0]
        if x not in dctAlreadySeen.keys():
            dctAlreadySeen[x] = (puz, tuples[1], tuples[2])
            heappush(parseMe, (num_pegs - 1, x))
