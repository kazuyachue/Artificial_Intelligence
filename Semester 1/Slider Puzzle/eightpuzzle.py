import sys
import collections
import time

def print_out(p):
    print(p[0:3]+"\n"+p[3:6]+"\n"+p[6:9]+"\n")

def findChildren(p):
    l = []
    loc = p.find(' ')
    if loc == -1:
        print("Error, no space!")
    else:
        if loc%3!=0:
            li = list(p)
            li[loc-1], li[loc] = li[loc], li[loc-1]
            l.append("".join(li))

        if loc%3!=2:
            li = list(p)
            li[loc+1], li[loc] = li[loc], li[loc+1]
            l.append("".join(li))

        if loc//3!=0:
            li = list(p)
            li[loc-3], li[loc] = li[loc], li[loc-3]
            l.append("".join(li))

        if loc//3!=2:
            li = list(p)
            li[loc+3], li[loc] = li[loc], li[loc+3]
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

start = time.clock()
root = sys.argv[1]
#goal = ''.join(sorted(root.replace(' ', '')))+ ' '
goal = "12345678 "
dctAlreadySeen = {root:""}
parseMe = collections.deque([root])
while True:
    if len(parseMe) == 0:
        print("No solution :(")
        break;
    puz = parseMe.popleft()
    if puz == goal:
        printPuzzle(puz, dctAlreadySeen)
        break;
    children = findChildren(puz)
    for x in children:
        if x not in dctAlreadySeen.keys():
            dctAlreadySeen[x] = puz
            parseMe.append(x)

print(time.clock()-start)
