import sys
import time
import random

global lookuptable
global spaces
spaces = [{1,4}, {0,2,5}, {1,3,6}, {2,7}, {0,5,8}, {1,4,6,9}, {2,5,7,10}, {3,6,11}, {4,9,12}, {5,8,10,13}, {6,9,11,14}, {7,10,15}, {8,13}, {9,12,14}, {10,13,15}, {11,14}]

def findChildren(p):
    l = []
    loc = p.index(' ')
    for i in spaces[loc]:
        li = list(p)
        c = li[i]
        prev = abs(lookuptable[c]//4 - i//4) +  abs(lookuptable[c]%4 - i%4)
        li[loc], li[i] = li[i], li[loc]
        new = abs(lookuptable[c]//4 - loc//4) +  abs(lookuptable[c]%4 - loc%4)
        l.append(("".join(li), new > prev))
    return l

def findOneDistance(c, p):
    loc_new = p.find(' ')
    loc_old = c.find(' ')
    char = c[loc_new]

    distance_new = abs(lookuptable[char]//4 - loc//4) +  abs(lookuptable[c]%4 - loc%4)
    distance_old = abs(lookuptable[c]//4 - loc//4) +  abs(lookuptable[c]%4 - loc%4)

start_time = time.clock()
t = time.clock() - start_time

prev_distance = 0
distance = 0
n = 0

puz = sys.argv[1]
lookuptable = {c: puz.index(c) for c in puz}

while t < 15:
    tup = random.choice(findChildren(puz))
    puz = tup[0]
    if tup[1]:
        prev_distance += 1
    else:
        prev_distance += -1
    distance += prev_distance
    n+=1
    t = time.clock() - start_time

print(f"N: {n}")
print(f"Time: {t} seconds")
print("manhattan distance / n: {}".format(distance/n))
print("N / Time: {}".format(n/t))

#N: 688523
#Time: 15.000006564101367 seconds
#manhattan distance / n: 37.24212844015378
#N / Time: 45901.51324652094
