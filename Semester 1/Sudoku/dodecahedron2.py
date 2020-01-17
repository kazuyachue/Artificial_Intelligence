import sys, time

lookupTable = {1: {2,3,4,5,6}, 2: {1,3,6,8,9}, 3:{1,2,4,9,10}, 4:{1,3,5,10,11}, 5:{1,4,6,7,11}, 6:{1,2,5,7,8},
7:{5,6,8,11,12}, 8:{2,6,7,9,12}, 9:{2,3,8,10,12}, 10:{3,4,5,9,12}, 11:{4,5,7,10,12}, 12:{7,8,9,10,11}}

def isInvalid(puz):
    for pentagons in lookupTable.keys():
        color = puz[pentagons-1]
        for neighbors in lookupTable[pentagons]:
            if puz[neighbors-1] != '.' and puz[neighbors-1] == color:
                return 1
    if '.' in puz:
        return 0
    return 2

def bruteForce(pzl, size):
    booleanish = isInvalid(pzl)
    if booleanish == 1: return ""
    if booleanish == 2: return pzl
    index = pzl.find('.')
    for possible in range(int(size)):
        subPzl = pzl[0:index] + str(possible) + pzl[index+1:]
        bF = bruteForce(subPzl, size)
        if bF: return bF
    return ""

root = '.' * 12
print(bruteForce(root,sys.argv[1]))
