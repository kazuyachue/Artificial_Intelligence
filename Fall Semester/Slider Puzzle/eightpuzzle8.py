import sys
import collections

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

def solvePuz(s, g):
    root = s
    goal = g
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

goal = "12345678 "
#goal = ''.join(sorted(root.replace(' ', '')))+ ' '

dctAlreadySeen = {goal:0}
parseMe = collections.deque([goal])
max_steps = 0
while True:
    if len(parseMe) == 0:
        max_steps = max(dctAlreadySeen.values())
    #    print("Max steps: " + str(max_steps))
        break;
    puz = parseMe.popleft()
    children = findChildren(puz)
    for x in children:
        if x not in dctAlreadySeen.keys():
            dctAlreadySeen[x] = dctAlreadySeen[puz]+1
            parseMe.append(x)

dctSteps = {}
for i in range(1, max_steps+1):
    dctSteps[i] = set()
for x in dctAlreadySeen.keys():
    if dctSteps.get(dctAlreadySeen.get(x)) != None:
        dctSteps.get(dctAlreadySeen.get(x)).add(x)

#for j in dctSteps.keys():
#    print(str(j)+":"+str(len(dctSteps[j])))

b = True
last = ""
slist = []
s = set()
for j in dctSteps.keys():
    if b:
        last = dctSteps.get(j).pop()
        s.add(last)
        slist.append(last)
        slist.append(j)
        b = False
    else:
        c = findChildren(last)
        last = dctSteps.get(j).pop()
        while last in c:
            if len(dctSteps.get(j))==1:
                b = True
                break;
            last = dctSteps.get(j).pop()
        if b == False:
            s.add(last)
            slist.append(last)
            slist.append(j)
print(str(len(s)))
for l in slist:
    print(l)
