import sys
import collections

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

goal = sys.argv[1]
#goal = ''.join(sorted(root.replace(' ', '')))+ ' '

dctAlreadySeen = {goal:0}
parseMe = collections.deque([goal])
max_steps = 0
while True:
    if len(parseMe) == 0:
        max_steps = max(dctAlreadySeen.values())
        print("Max steps: " + str(max_steps))
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
for j in dctSteps.keys():
    print(str(j)+":"+str(len(dctSteps[j])))
hardPuz = dctSteps[max_steps].pop()
print("\n" + dctSteps[max_steps].pop() + "\n")
solvePuz(hardPuz, goal)
